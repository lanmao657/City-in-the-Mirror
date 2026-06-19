#!/usr/bin/env python3
"""
《镜中城》BGM 生成器
程序化生成 7 首循环背景音乐
运行: python generate_bgm.py
输出: game/audio/music/*.wav + web/audio/music/*.wav
"""

import numpy as np
import wave
import os

SAMPLE_RATE = 44100
GAME_DIR = os.path.join(os.path.dirname(__file__), "game", "audio", "music")
WEB_DIR = os.path.join(os.path.dirname(__file__), "web", "audio", "music")
os.makedirs(GAME_DIR, exist_ok=True)
os.makedirs(WEB_DIR, exist_ok=True)

def save_wav(filename, data, sr=SAMPLE_RATE):
    data = np.clip(data, -1.0, 1.0)
    data_int = (data * 32767).astype(np.int16)
    for d in [GAME_DIR, WEB_DIR]:
        with wave.open(os.path.join(d, filename), 'w') as wf:
            wf.setnchannels(1)
            wf.setsampwidth(2)
            wf.setframerate(sr)
            wf.writeframes(data_int.tobytes())
    dur = len(data) / sr
    print(f"  [OK] {filename} ({dur:.1f}s)")

def sine(freq, dur, sr=SAMPLE_RATE):
    t = np.linspace(0, dur, int(sr*dur), endpoint=False)
    return np.sin(2*np.pi*freq*t)

def pad(freq, dur, sr=SAMPLE_RATE):
    """持续合成 pad 音色（正弦波叠加 + 微失谐）"""
    t = np.linspace(0, dur, int(sr*dur), endpoint=False)
    s  = np.sin(2*np.pi*freq*t) * 0.3
    s += np.sin(2*np.pi*(freq*1.003)*t) * 0.25  # 微失谐 +3 音分
    s += np.sin(2*np.pi*(freq*0.997)*t) * 0.25  # 微失谐 -3 音分
    s += np.sin(2*np.pi*(freq*2)*t) * 0.1        # 八度泛音
    return s

def noise(dur, sr=SAMPLE_RATE):
    return np.random.randn(int(sr*dur))

def lowpass(data, cutoff, sr=SAMPLE_RATE):
    from numpy.fft import rfft, irfft, rfftfreq
    n = len(data)
    spec = rfft(data)
    freqs = rfftfreq(n, 1/sr)
    spec[freqs > cutoff] *= 0.02
    return irfft(spec, n)

def fade_in(data, dur=0.5, sr=SAMPLE_RATE):
    n = int(dur*sr)
    data[:n] *= np.linspace(0, 1, n)
    return data

def fade_out(data, dur=1.0, sr=SAMPLE_RATE):
    n = int(dur*sr)
    data[-n:] *= np.linspace(1, 0, n)
    return data

def reverb(data, delay=0.04, decay=0.3, sr=SAMPLE_RATE):
    d = int(delay*sr)
    r = data.copy()
    r[d:] += data[:-d] * decay
    r[2*d:] += data[:-2*d] * decay*0.5
    r[3*d:] += data[:-3*d] * decay*0.25
    return r / (np.max(np.abs(r)) + 1e-10)

def loop_seamless(data, sr=SAMPLE_RATE):
    """确保首尾可以无缝循环（交叉淡化 1 秒）"""
    n = len(data)
    cross = min(int(1.0*sr), n//4)
    data[:cross] *= np.linspace(0, 1, cross)
    data[-cross:] *= np.linspace(1, 0, cross)
    data[:cross] += data[-cross:]
    return data


# ══════════════════════════════════════════════════════════
# BGM 生成
# ══════════════════════════════════════════════════════════

def gen_bgm_menu():
    """主菜单 — 空灵、神秘"""
    dur = 30
    n = int(SAMPLE_RATE * dur)
    result = np.zeros(n)

    # 基础 drone：低沉持续音
    result += pad(55, dur) * 0.25  # A1

    # 缓慢移动的高音泛音
    for i in range(8):
        freq = 220 * (1 + i*0.125)  # A3 附近的泛音列
        t = np.linspace(0, dur, n, endpoint=False)
        env = np.sin(2*np.pi*(0.03+i*0.005)*t) * 0.5 + 0.5
        result += np.sin(2*np.pi*freq*t) * env * 0.04

    # 偶尔的钢琴音（正弦波模拟）
    piano_notes = [220, 261, 329, 392, 329, 261, 220, 196]
    for i, freq in enumerate(piano_notes):
        start = int(i * dur/len(piano_notes) * SAMPLE_RATE)
        note = sine(freq, 3.0) * 0.15
        note *= np.exp(-np.linspace(0, 3, len(note)))
        end = min(start+len(note), n)
        result[start:end] += note[:end-start]

    result = lowpass(result, 3000)
    result = reverb(result, 0.06, 0.4)
    result = fade_in(result, 2.0)
    result = fade_out(result, 2.0)
    result = loop_seamless(result)
    save_wav("bgm_menu.wav", result * 0.6)


def gen_bgm_left_city():
    """左城 — 冷冽大提琴 drone"""
    dur = 40
    n = int(SAMPLE_RATE * dur)
    result = np.zeros(n)

    # 低沉 drone
    result += pad(73, dur) * 0.3   # D2
    result += pad(110, dur) * 0.15 # A2

    # 缓慢的旋律线（大提琴模拟）
    melody_notes = [
        (146, 6), (130, 4), (146, 8), (110, 5),
        (130, 6), (146, 4), (164, 6), (146, 8),
    ]
    pos = 0
    for freq, length in melody_notes:
        note_dur = length
        start = int(pos * SAMPLE_RATE)
        note = sine(freq, note_dur) * 0.12
        # 大提琴包络：慢起慢落
        note *= np.minimum(np.linspace(0, 1, len(note))*3, 1.0)
        note *= np.exp(-np.linspace(0, note_dur*0.5, len(note)))
        end = min(start+len(note), n)
        result[start:end] += note[:end-start]
        pos += length * 0.9

    # 冰裂声点缀
    for i in range(15):
        start = int(np.random.uniform(2, dur-2) * SAMPLE_RATE)
        click = noise(0.05) * 0.08
        click = np.abs(click)
        click *= np.exp(-np.linspace(0, 8, len(click)))
        end = min(start+len(click), n)
        result[start:end] += click[:end-start]

    result = lowpass(result, 2500)
    result = reverb(result, 0.05, 0.5)
    result = fade_in(result, 3.0)
    result = fade_out(result, 3.0)
    result = loop_seamless(result)
    save_wav("bgm_left_city.wav", result * 0.5)


def gen_bgm_right_city():
    """右城 — 温暖八音盒 + 竖琴"""
    dur = 30
    n = int(SAMPLE_RATE * dur)
    result = np.zeros(n)

    # 温暖和弦 pad
    result += pad(261, dur) * 0.1   # C4
    result += pad(329, dur) * 0.08  # E4
    result += pad(392, dur) * 0.06  # G4

    # 八音盒琶音（高音正弦波）
    notes = [523, 659, 784, 1047, 784, 659, 523, 392,
             523, 659, 784, 1047, 1318, 1047, 784, 659]
    note_dur = dur / len(notes)
    for i, freq in enumerate(notes):
        start = int(i * note_dur * SAMPLE_RATE)
        note = sine(freq, note_dur * 1.5) * 0.1
        # 八音盒包络：快起快落
        note *= np.exp(-np.linspace(0, note_dur*2, len(note)))
        # 故意让个别音走调
        if i % 5 == 3:
            note += sine(freq * 1.015, note_dur * 1.5) * 0.05  # 走调 15 音分
        end = min(start+len(note), n)
        result[start:end] += note[:end-start]

    # 风铃声
    for i in range(20):
        freq = np.random.uniform(2000, 6000)
        start = int(np.random.uniform(0, dur) * SAMPLE_RATE)
        chime = sine(freq, 0.3) * 0.03
        chime *= np.exp(-np.linspace(0, 6, len(chime)))
        end = min(start+len(chime), n)
        result[start:end] += chime[:end-start]

    result = lowpass(result, 4000)
    result = reverb(result, 0.04, 0.35)
    result = fade_in(result, 1.5)
    result = fade_out(result, 1.5)
    result = loop_seamless(result)
    save_wav("bgm_right_city.wav", result * 0.55)


def gen_bgm_mirror():
    """镜墙 — 两种旋律交织"""
    dur = 45
    n = int(SAMPLE_RATE * dur)
    left_part = np.zeros(n)   # 左声道：冷色大提琴
    right_part = np.zeros(n)  # 右声道：暖色八音盒

    # 左侧冷色 drone
    left_part += pad(73, dur) * 0.2
    # 左侧旋律（大提琴）
    left_melody = [(146, 5), (130, 4), (110, 6), (130, 4), (146, 8)]
    pos = 0
    for freq, length in left_melody:
        start = int(pos * SAMPLE_RATE)
        note = sine(freq, length) * 0.1
        note *= np.minimum(np.linspace(0, 1, len(note))*2, 1.0)
        note *= np.exp(-np.linspace(0, length*0.3, len(note)))
        end = min(start+len(note), n)
        left_part[start:end] += note[:end-start]
        pos += length * 0.85

    # 右侧暖色 drone
    right_part += pad(261, dur) * 0.15
    # 右侧旋律（八音盒）
    right_melody = [(523, 3), (659, 3), (523, 4), (392, 3), (523, 6)]
    pos = 0
    for freq, length in right_melody:
        start = int(pos * SAMPLE_RATE)
        note = sine(freq, length) * 0.08
        note *= np.exp(-np.linspace(0, length*1.5, len(note)))
        end = min(start+len(note), n)
        right_part[start:end] += note[:end-start]
        pos += length * 0.85

    # 中段融合（第 15-30 秒）
    t = np.linspace(0, 1, n)
    blend = np.clip((t - 0.33) * 3, 0, 1) * np.clip((0.67 - t) * 3, 0, 1)
    result = left_part * (1 - blend) + right_part * (1 - blend) + (left_part + right_part) * blend * 0.5

    result = lowpass(result, 3000)
    result = reverb(result, 0.05, 0.4)
    result = fade_in(result, 3.0)
    result = fade_out(result, 3.0)
    result = loop_seamless(result)
    save_wav("bgm_mirror.wav", result * 0.5)


def gen_bgm_flashback():
    """闪回 — 模糊怀旧钢琴"""
    dur = 25
    n = int(SAMPLE_RATE * dur)
    result = np.zeros(n)

    # 暖色 pad 底层
    result += pad(220, dur) * 0.08
    result += pad(277, dur) * 0.06

    # 钢琴旋律（正弦波 + 磁带颤音）
    melody = [330, 392, 440, 523, 440, 392, 330, 294, 330, 262, 294, 330, 392, 440, 523, 587]
    note_dur = dur / len(melody)
    for i, freq in enumerate(melody):
        start = int(i * note_dur * SAMPLE_RATE)
        t = np.linspace(0, note_dur*2, int(SAMPLE_RATE*note_dur*2), endpoint=False)
        # 磁带颤音
        vibrato = 1 + 0.003 * np.sin(2*np.pi*3.5*t)
        note = np.sin(2*np.pi*freq*vibrato*t) * 0.12
        note *= np.exp(-np.linspace(0, note_dur*3, len(note)))
        end = min(start+len(note), n)
        result[start:end] += note[:end-start]

    # 每 8 秒的静默（记忆断裂）
    for gap_start_s in [8, 18]:
        gap_start = int(gap_start_s * SAMPLE_RATE)
        gap_end = int((gap_start_s + 1.5) * SAMPLE_RATE)
        gap_end = min(gap_end, n)
        result[gap_start:gap_end] *= np.linspace(1, 0.05, gap_end-gap_start)

    # 低通 + 大量混响 = 水下质感
    result = lowpass(result, 2000)
    result = reverb(result, 0.08, 0.5)
    result = fade_in(result, 2.0)
    result = fade_out(result, 3.0)
    result = loop_seamless(result)
    save_wav("bgm_flashback.wav", result * 0.5)


def gen_bgm_final_choice():
    """最终选择 — 紧张到释放"""
    dur = 60
    n = int(SAMPLE_RATE * dur)
    result = np.zeros(n)

    # 心跳低频脉冲（前半段）
    for i in range(60):
        t_pos = i * 1.0  # 每秒一次
        start = int(t_pos * SAMPLE_RATE)
        if start >= n: break
        pulse = sine(40, 0.3) * 0.2
        pulse *= np.exp(-np.linspace(0, 8, len(pulse)))
        end = min(start+len(pulse), n)
        # 音量随时间递增
        vol = min(1.0, 0.3 + t_pos/dur*1.5)
        result[start:end] += pulse[:end-start] * vol

    # 逐渐加入的弦乐 pad
    strings_start = int(10 * SAMPLE_RATE)
    t_arr = np.linspace(0, 1, n)
    strings_env = np.clip((t_arr - 0.15)*5, 0, 1) * np.clip((0.85 - t_arr)*5, 0, 1)
    result += pad(220, dur) * strings_env * 0.15
    result += pad(277, dur) * strings_env * 0.12
    result += pad(330, dur) * strings_env * 0.1

    # 高潮段（第 40-50 秒）
    climax_start = int(40 * SAMPLE_RATE)
    climax_end = int(50 * SAMPLE_RATE)
    climax_env = np.zeros(n)
    climax_env[climax_start:climax_end] = np.sin(np.linspace(0, np.pi, climax_end-climax_start))
    result += pad(440, dur) * climax_env * 0.2
    result += pad(554, dur) * climax_env * 0.15

    # 骤停（第 50-53 秒）
    silence_start = int(50 * SAMPLE_RATE)
    silence_end = int(53 * SAMPLE_RATE)
    result[silence_start:silence_end] *= np.linspace(1, 0, silence_end-silence_start)

    # 释放（最后 7 秒）
    release_start = int(53 * SAMPLE_RATE)
    release_env = np.zeros(n)
    release_env[release_start:] = np.linspace(0, 1, n-release_start)
    result += pad(261, dur) * release_env * 0.2   # C4
    result += pad(329, dur) * release_env * 0.15  # E4
    result += pad(392, dur) * release_env * 0.1   # G4

    result = lowpass(result, 3500)
    result = reverb(result, 0.05, 0.35)
    result = fade_in(result, 1.0)
    result = fade_out(result, 2.0)
    save_wav("bgm_final_choice.wav", result * 0.45)


def gen_bgm_ending():
    """结局 — 平静温暖治愈"""
    dur = 40
    n = int(SAMPLE_RATE * dur)
    result = np.zeros(n)

    # 温暖和弦 pad
    result += pad(261, dur) * 0.15  # C4
    result += pad(329, dur) * 0.12  # E4
    result += pad(392, dur) * 0.1   # G4
    result += pad(523, dur) * 0.06  # C5

    # 古琴音色（正弦波 + 快速衰减）
    guqin_notes = [
        (262, 4), (330, 3), (392, 4), (523, 3), (440, 5),
        (392, 3), (330, 4), (262, 6), (294, 3), (330, 4),
        (392, 5), (523, 4), (659, 3), (523, 5), (392, 4),
    ]
    pos = 0
    for freq, length in guqin_notes:
        start = int(pos * SAMPLE_RATE)
        if start >= n: break
        t_note = np.linspace(0, length, int(SAMPLE_RATE*length), endpoint=False)
        note = np.sin(2*np.pi*freq*t_note) * 0.1
        # 古琴包络：弹拨感
        note *= np.exp(-np.linspace(0, length*0.8, len(note)))
        note *= np.minimum(np.linspace(0, 0.05, len(note))*20, 1.0)
        end = min(start+len(note), n)
        if end > start:
            result[start:end] += note[:end-start]
        pos += length * 0.8

    # 轻声哼唱（极低频 pad）
    result += pad(196, dur) * 0.04  # G3
    result += pad(220, dur) * 0.03  # A3

    # 河流环境音（低通噪声）
    river = noise(dur) * 0.03
    river = lowpass(river, 500)
    result += river

    result = lowpass(result, 3500)
    result = reverb(result, 0.06, 0.4)
    result = fade_in(result, 3.0)
    result = fade_out(result, 4.0)
    result = loop_seamless(result)
    save_wav("bgm_ending.wav", result * 0.5)


# ══════════════════════════════════════════════════════════

if __name__ == "__main__":
    print("《镜中城》BGM 生成器")
    print("=" * 40)

    bgms = [
        ("主菜单 · 裂镜", gen_bgm_menu),
        ("左城 · 石之沉默", gen_bgm_left_city),
        ("右城 · 蜜语花园", gen_bgm_right_city),
        ("镜墙 · 之间", gen_bgm_mirror),
        ("闪回 · 碎影", gen_bgm_flashback),
        ("最终选择 · 渡", gen_bgm_final_choice),
        ("结局 · 归", gen_bgm_ending),
    ]

    for name, func in bgms:
        print(f"\n生成: {name}")
        func()

    print("\n" + "=" * 40)
    print(f"全部完成！共 7 首 BGM")
    print(f"Ren'Py: {GAME_DIR}")
    print(f"Web:    {WEB_DIR}")
