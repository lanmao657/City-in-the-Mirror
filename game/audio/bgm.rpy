## audio/bgm.rpy — 背景音乐定义
## 《镜中城》7 首程序化生成 BGM

## ── BGM 通道设置 ──────────────────────────────────────────

init python:
    renpy.music.register_channel("bgm", mixer="music", loop=True)

## ── BGM 定义 ──────────────────────────────────────────────

define audio.bgm_menu = "audio/music/bgm_menu.wav"
define audio.bgm_left_city = "audio/music/bgm_left_city.wav"
define audio.bgm_right_city = "audio/music/bgm_right_city.wav"
define audio.bgm_mirror = "audio/music/bgm_mirror.wav"
define audio.bgm_flashback = "audio/music/bgm_flashback.wav"
define audio.bgm_final_choice = "audio/music/bgm_final_choice.wav"
define audio.bgm_ending = "audio/music/bgm_ending.wav"

## ── 便捷播放函数 ──────────────────────────────────────────

init python:
    def play_bgm(name, fadein=2.0):
        """播放 BGM，带淡入"""
        renpy.music.play(name, channel="bgm", fadein=fadein, loop=True)

    def stop_bgm(fadeout=2.0):
        """停止 BGM，带淡出"""
        renpy.music.stop(channel="bgm", fadeout=fadeout)

    def crossfade_bgm(name, fadein=2.0, fadeout=2.0):
        """交叉渐变到新 BGM"""
        renpy.music.play(name, channel="bgm", fadein=fadein, fadeout=fadeout, loop=True)
