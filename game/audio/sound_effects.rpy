## audio/sound_effects.rpy — 音效定义
## 《镜中城》全部程序化生成音效

## ── 音效通道设置 ──────────────────────────────────────────

init python:
    renpy.music.register_channel("sfx", mixer="sfx", loop=False)
    renpy.music.register_channel("sfx_ui", mixer="sfx", loop=False)

## ── 音效定义 ──────────────────────────────────────────────

## 核心交互音效
define audio.sfx_wheel_appear = "audio/sfx/sfx_wheel_appear.wav"
define audio.sfx_truth = "audio/sfx/sfx_truth.wav"
define audio.sfx_lie = "audio/sfx/sfx_lie.wav"
define audio.sfx_silent = "audio/sfx/sfx_silent.wav"

## 转场音效
define audio.sfx_chapter = "audio/sfx/sfx_chapter.wav"
define audio.sfx_scene_change = "audio/sfx/sfx_scene_change.wav"

## 氛围音效
define audio.sfx_mirror_crack = "audio/sfx/sfx_mirror_crack.wav"
define audio.sfx_flashback = "audio/sfx/sfx_flashback.wav"

## UI 音效
define audio.sfx_dialogue = "audio/sfx/sfx_dialogue.wav"
define audio.sfx_achievement = "audio/sfx/sfx_achievement.wav"

## ── 便捷播放函数 ──────────────────────────────────────────

init python:
    def play_sfx(name, channel="sfx"):
        """播放指定音效"""
        renpy.music.play(name, channel=channel)

    def play_choice_sfx(choice_type):
        """根据选择类型播放对应音效"""
        if choice_type == "truth":
            renpy.music.play("audio/sfx/sfx_truth.wav", channel="sfx")
        elif choice_type == "lie":
            renpy.music.play("audio/sfx/sfx_lie.wav", channel="sfx")
        elif choice_type == "silent":
            renpy.music.play("audio/sfx/sfx_silent.wav", channel="sfx")

    def play_wheel_sfx():
        """播放语言轮盘出现音效"""
        renpy.music.play("audio/sfx/sfx_wheel_appear.wav", channel="sfx_ui")

    def play_achievement_sfx():
        """播放成就解锁音效"""
        renpy.music.play("audio/sfx/sfx_achievement.wav", channel="sfx_ui")
