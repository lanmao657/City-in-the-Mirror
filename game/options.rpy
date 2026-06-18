## options.rpy — 游戏元数据与基础配置
## 《镜中城》City of Mirrors

define config.version = "0.1.0"
define build.name = "CityOfMirrors"

define gui.about = _p("""
《镜中城》—— 真话与假话的世界

一座城市被镜墙劈成两半：
左城的人只能说真话，但极度冷漠；
右城的人满口甜言蜜语，却虚伪至极。

你是唯一能说两种话的人。
""")

define build.directory_name = "CityOfMirrors"
define build.executable_name = "CityOfMirrors"

## 窗口设置
define config.screen_width = 1920
define config.screen_height = 1080
define config.window_title = "镜中城 | City of Mirrors"

## 渲染设置
define config.gl_resize = True
define config.image_cache_size_mb = 512

## 存档设置
define config.has_autosave = True
define config.autosave_on_choice = True
define config.autosave_on_quit = True
define config.autosave_slots = 3
define config.save_directory = "CityOfMirrors saves"

## 音频设置
define config.default_music_volume = 0.8
define config.default_sfx_volume = 0.9
#define config.default_voice_volume = 1.0

## 文字设置
define config.default_text_cps = 40
define config.default_afm_time = 15

## 转场默认值
define config.enter_transition = dissolve
define config.exit_transition = dissolve
define config.intra_transition = dissolve
define config.after_load_transition = dissolve
define config.end_game_transition = dissolve

## 禁用右键菜单（使用自定义暂停菜单）
define config.game_menu_action = ShowMenu("pause_menu")
