#!/usr/bin/env python3
"""
《镜中城》音效生成器
使用 numpy + wave 模块程序化生成 10 个游戏音效
运行: python generate_sfx.py
输出: game/audio/sfx/*.wav
"""

import numpy as np
import wave
import os

SAMPLE_RATE = 44100
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "game", "audio", "sfx")

os.makedirs(OUTPUT_DIR, exist_ok=True)

# ── 工具函数 ──────────────────────────────────────────────

def save_wav(filename, data, sample_rate=SAMPLE_RATE, channels=1):
    """保存 numpy 数组为 WAV 文件"""
    data = np.clip(data, -1.0, 1.0)
    data_int = (data * 32767).astype(np.int16)
    filepath = os.path.join(OUTPUT_DIR, filename)
    with wave.open(filepath, 'w') as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(2)
        wf.setframerate(sample_rate)
        if channels == 2:
            stereo = np.column_stack((data_int, data_int))
            wf.writeframes(stereo.tobytes())
        else:
            wf.writeframes(data_int.tobytes())
    print(f"  [OK] {filename} ({len(data)/sample_rate:.2f}s)")

def sine(freq, duration, sr=SAMPLE_RATE):
    """生成正弦波"""
    t = np.linspace(0, duration, int(sr * duration), endpoint=False)
    return np.sin(2 * np.pi * freq * t)

def noise(duration, sr=SAMPLE_RATE):
    """生成白噪声"""
    return np.random.randn(int(sr * duration))

def envelope(data, attack=0.01, decay=0.05, sustain=0.7, release=0.1, sr=SAMPLE_RATE):
    """ADSR 包络"""
    n = len(data)
    a = int(attack * sr)
    d = int(decay * sr)
    r = int(release * sr)
    s = n - a - d - r
    env = np.concatenate([
        np.linspace(0, 1, max(a, 1)),
        np.linspace(1, sustain, max(d, 1)),
        np.full(max(s, 0), sustain),
        np.linspace(sustain, 0, max(r, 1)),
    ])[:n]
    return data * env

def fade_in(data, duration=0.05, sr=SAMPLE_RATE):
    n = int(duration * sr)
    data[:n] *= np.linspace(0, 1, n)
    return data

def fade_out(data, duration=0.1, sr=SAMPLE_RATE):
    n = int(duration * sr)
    data[-n:] *= np.linspace(1, 0, n)
    return data

def reverb(data, delay=0.03, decay=0.3, sr=SAMPLE_RATE):
    """简单延迟混响"""
    d = int(delay * sr)
    result = data.copy()
    result[d:] += data[:-d] * decay
    result[2*d:] += data[:-2*d] * decay * 0.5
    return result / np.max(np.abs(result) + 1e-10)

def lowpass(data, cutoff=1000, sr=SAMPLE_RATE):
    """简单低通滤波"""
    from numpy.fft import fft, ifft
    n = len(data)
    freqs = np.fft.rfftfreq(n, 1/sr)
    spectrum = np.fft.rfft(data)
    spectrum[freqs > cutoff] *= 0.01
    return np.fft.irfft(spectrum, n)

def highpass(data, cutoff=3000, sr=SAMPLE_RATE):
    """简单高通滤波"""
    from numpy.fft import fft, ifft
    n = len(data)
    freqs = np.fft.rfftfreq(n, 1/sr)
    spectrum = np.fft.rfft(data)
    spectrum[freqs < cutoff] *= 0.01
    return np.fft.irfft(spectrum, n)


# ══════════════════════════════════════════════════════════
# 音效生成
# ══════════════════════════════════════════════════════════

def gen_wheel_appear():
    """3.1 语言轮盘弹出 — 冷暖双音 + 混响"""
    t1 = sine(880, 0.3) * 0.4   # 冷色高音 A5
    t2 = sine(659, 0.4) * 0.3   # 暖色中音 E5
    t1 = envelope(t1, attack=0.005, decay=0.1, sustain=0.3, release=0.2)
    t2 = envelope(t2, attack=0.01, decay=0.1, sustain=0.3, release=0.3)

    result = np.zeros(int(SAMPLE_RATE * 0.6))
    result[:len(t1)] += t1
    result[int(SAMPLE_RATE*0.1):int(SAMPLE_RATE*0.1)+len(t2)] += t2
    result = reverb(result, delay=0.05, decay=0.4)
    result = fade_out(result, 0.15)
    save_wav("sfx_wheel_appear.wav", result * 0.7)


def gen_truth():
    """3.2 真话选择 — 冰晶音，清脆"""
    dur = 0.6
    n = int(SAMPLE_RATE * dur)
    t = np.zeros(n)
    t[:int(SAMPLE_RATE*0.6)] += sine(1318, 0.6) * 0.5  # E6
    t[:int(SAMPLE_RATE*0.5)] += sine(1568, 0.5) * 0.3  # G6
    t = envelope(t, attack=0.002, decay=0.08, sustain=0.1, release=0.5)
    t = reverb(t, delay=0.02, decay=0.5)
    t = fade_out(t, 0.2)
    # 加一点噪声模拟冰裂
    nd = noise(0.6) * 0.05
    nd = highpass(nd, 6000)
    nd = envelope(nd, attack=0.001, decay=0.02, sustain=0, release=0.05)
    t[:len(nd)] += nd
    save_wav("sfx_truth.wav", t * 0.6)


def gen_lie():
    """3.3 假话选择 — 暖色钟声，柔和"""
    dur = 0.7
    n = int(SAMPLE_RATE * dur)
    t = np.zeros(n)
    t[:int(SAMPLE_RATE*0.7)] += sine(523, 0.7) * 0.4   # C5
    t[:int(SAMPLE_RATE*0.6)] += sine(659, 0.6) * 0.25  # E5
    t[:int(SAMPLE_RATE*0.5)] += sine(784, 0.5) * 0.15  # G5
    t = envelope(t, attack=0.01, decay=0.15, sustain=0.2, release=0.5)
    t = reverb(t, delay=0.04, decay=0.4)
    t = fade_out(t, 0.2)
    save_wav("sfx_lie.wav", t * 0.6)


def gen_silent():
    """3.4 沉默选择 — 极轻的风声"""
    n = noise(1.0) * 0.08
    n = lowpass(n, 800)
    n = envelope(n, attack=0.1, decay=0.2, sustain=0.1, release=0.6)
    save_wav("sfx_silent.wav", n * 0.3)


def gen_chapter():
    """3.5 章节转场 — 深沉锣声"""
    dur = 3.0
    n = int(SAMPLE_RATE * dur)
    t = np.zeros(n)
    t[:int(SAMPLE_RATE*3.0)] += sine(65, 3.0) * 0.5    # 低音 C2
    t[:int(SAMPLE_RATE*2.5)] += sine(130, 2.5) * 0.3   # C3
    t[:int(SAMPLE_RATE*2.0)] += sine(196, 2.0) * 0.15  # G3
    t = envelope(t, attack=0.01, decay=0.5, sustain=0.15, release=2.5)
    t = reverb(t, delay=0.06, decay=0.5)
    t = fade_out(t, 0.5)
    save_wav("sfx_chapter.wav", t * 0.5)


def gen_achievement():
    """3.6 成就解锁 — 三音阶上升 C-E-G"""
    notes = [523, 659, 784]  # C5, E5, G5
    result = np.zeros(int(SAMPLE_RATE * 2.0))
    for i, freq in enumerate(notes):
        t = sine(freq, 0.4) * 0.3
        t = envelope(t, attack=0.005, decay=0.1, sustain=0.3, release=0.3)
        start = int(i * SAMPLE_RATE * 0.25)
        result[start:start+len(t)] += t
    result = reverb(result, delay=0.03, decay=0.35)
    result = fade_out(result, 0.3)
    save_wav("sfx_achievement.wav", result * 0.6)


def gen_mirror_crack():
    """3.7 镜墙碎裂 — 玻璃碎裂 + 低频隆隆"""
    dur = 2.0
    n = int(SAMPLE_RATE * dur)
    # 玻璃碎裂：高频噪声爆发
    glass = noise(dur) * 0.6
    glass = highpass(glass, 4000)
    glass = envelope(glass, attack=0.001, decay=0.15, sustain=0.05, release=1.5)
    # 碎片叮当
    tinkle = np.zeros(n)
    for _ in range(30):
        freq = np.random.uniform(3000, 8000)
        start = int(np.random.uniform(0.2, 1.5) * SAMPLE_RATE)
        dur2 = np.random.uniform(0.05, 0.15)
        note = sine(freq, dur2) * np.random.uniform(0.05, 0.15)
        note = envelope(note, attack=0.001, decay=0.03, sustain=0, release=0.05)
        end = min(start+len(note), n)
        tinkle[start:end] += note[:end-start]
    # 低频隆隆
    rumble = noise(dur) * 0.3
    rumble = lowpass(rumble, 200)
    rumble = envelope(rumble, attack=0.01, decay=0.3, sustain=0.1, release=1.5)

    result = glass + tinkle + rumble
    result = reverb(result, delay=0.04, decay=0.3)
    save_wav("sfx_mirror_crack.wav", result * 0.5)


def gen_flashback():
    """3.8 记忆闪回 — 磁带倒带 + 反向混响"""
    # 逐渐上升的频率扫频（倒带感）
    t = np.linspace(0, 1.5, int(SAMPLE_RATE * 1.5))
    freq_sweep = np.linspace(200, 2000, len(t))
    sweep = np.sin(2 * np.pi * freq_sweep * t) * 0.3
    sweep = envelope(sweep, attack=0.05, decay=0.3, sustain=0.4, release=0.7)
    # 钢琴音被"吸走"
    piano = sine(440, 0.5) * 0.2
    piano = piano[::-1]  # 反向
    piano = envelope(piano, attack=0.01, decay=0.1, sustain=0.3, release=0.1)

    result = np.zeros(int(SAMPLE_RATE * 1.5))
    result[:len(sweep)] += sweep
    result[:len(piano)] += piano
    result = fade_out(result, 0.2)
    save_wav("sfx_flashback.wav", result * 0.5)


def gen_dialogue():
    """3.9 对话框出现 — 丝绸展开声"""
    n = noise(0.5) * 0.15
    n = lowpass(n, 2000)
    n = envelope(n, attack=0.01, decay=0.05, sustain=0.2, release=0.2)
    n = fade_out(n, 0.1)
    save_wav("sfx_dialogue.wav", n * 0.25)


def gen_scene_change():
    """3.10 场景切换 — 交叉渐变过渡"""
    # 风声淡出
    wind_out = noise(2.0) * 0.3
    wind_out = lowpass(wind_out, 1500)
    wind_out = envelope(wind_out, attack=0.01, decay=0.2, sustain=0.5, release=0.8)
    # 风声淡入
    wind_in = noise(2.0) * 0.3
    wind_in = lowpass(wind_in, 1500)
    wind_in = wind_in[::-1]
    wind_in = envelope(wind_in, attack=0.01, decay=0.2, sustain=0.5, release=0.8)
    wind_in = wind_in[::-1]

    result = np.zeros(int(SAMPLE_RATE * 2.0))
    n = len(result)
    # 交叉渐变
    result += wind_out[:n] * np.linspace(1, 0, n)
    result += wind_in[:n] * np.linspace(0, 1, n)
    save_wav("sfx_scene_change.wav", result * 0.3)


# ══════════════════════════════════════════════════════════
# 执行生成
# ══════════════════════════════════════════════════════════

if __name__ == "__main__":
    print("《镜中城》音效生成器")
    print("=" * 40)

    generators = [
        ("语言轮盘弹出", gen_wheel_appear),
        ("真话选择", gen_truth),
        ("假话选择", gen_lie),
        ("沉默选择", gen_silent),
        ("章节转场", gen_chapter),
        ("成就解锁", gen_achievement),
        ("镜墙碎裂", gen_mirror_crack),
        ("记忆闪回", gen_flashback),
        ("对话框出现", gen_dialogue),
        ("场景切换", gen_scene_change),
    ]

    for name, func in generators:
        print(f"\n生成: {name}")
        func()

    print("\n" + "=" * 40)
    print(f"全部完成！文件保存在: {OUTPUT_DIR}")
    print(f"共生成 {len(generators)} 个 WAV 音效文件")
