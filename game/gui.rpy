## gui.rpy — GUI 基础样式
## 《镜中城》使用自定义 screen 覆盖大部分默认 GUI，
## 此文件仅保留 Ren'Py 运行必需的基础样式。

init python:
    gui.init(1920, 1080)

## ── 字体 ──────────────────────────────────────────────────
define gui.text_font = "DejaVuSans.ttf"
define gui.name_text_font = "DejaVuSans.ttf"
define gui.interface_text_font = "DejaVuSans.ttf"

## 如果项目中放入了中文字体，取消以下注释并替换：
# define gui.text_font = "fonts/NotoSerifCJK-Regular.ttc"
# define gui.name_text_font = "fonts/NotoSansCJK-Medium.ttc"
# define gui.interface_text_font = "fonts/NotoSansCJK-Regular.ttc"

## ── 字号 ──────────────────────────────────────────────────
define gui.text_size = 28
define gui.name_text_size = 24
define gui.interface_text_size = 20
define gui.label_text_size = 24
define gui.notify_text_size = 18
define gui.title_text_size = 48

## ── 颜色 ──────────────────────────────────────────────────
define gui.accent_color = "#C0C0C0"
define gui.idle_color = "#888888"
define gui.idle_small_color = "#AAAAAA"
define gui.hover_color = "#FFFFFF"
define gui.selected_color = "#FFFFFF"
define gui.insensitive_color = "#4444447F"
define gui.muted_color = "#510028"
define gui.hover_muted_color = "#7A003D"

define gui.text_color = "#E8E8E8"
define gui.interface_text_color = "#E8E8E8"

## ── 按钮 ──────────────────────────────────────────────────
define gui.button_width = None
define gui.button_height = None
define gui.button_borders = Borders(6, 6, 6, 6)
define gui.button_text_font = gui.interface_text_font
define gui.button_text_size = gui.interface_text_size
define gui.button_text_idle_color = gui.idle_color
define gui.button_text_hover_color = gui.hover_color
define gui.button_text_selected_color = gui.selected_color
define gui.button_text_insensitive_color = gui.insensitive_color

## ── 滚动条 ─────────────────────────────────────────────────
define gui.scrollbar_size = 18
define gui.scrollbar_tile = False
define gui.scrollbar_borders = Borders(6, 6, 6, 6)

## ── 框体 ──────────────────────────────────────────────────
define gui.frame_borders = Borders(6, 6, 6, 6)
define gui.confirm_frame_borders = Borders(60, 60, 60, 60)
define gui.frame_tile = False

## ── 布局 ──────────────────────────────────────────────────
define gui.skip_frame_borders = Borders(24, 8, 75, 8)
define gui.notify_frame_borders = Borders(24, 8, 60, 8)

define gui.choice_button_width = 1100
define gui.choice_button_height = None
define gui.choice_button_tile = False
define gui.choice_button_borders = Borders(150, 8, 150, 8)
define gui.choice_button_text_font = gui.text_font
define gui.choice_button_text_size = gui.text_size
define gui.choice_button_text_xalign = 0.5
define gui.choice_button_text_idle_color = "#E8E8E8"
define gui.choice_button_text_hover_color = "#FFFFFF"

define gui.navigation_xpos = 60
define gui.skip_ypos = 15
define gui.notify_ypos = 68

## Ren'Py 需要这些变量存在，即使我们用自定义 screen 替代
define gui.slot_button_width = 414
define gui.slot_button_height = 309
define gui.slot_button_borders = Borders(15, 15, 15, 15)
define gui.slot_button_text_size = 20
define gui.slot_button_text_xalign = 0.5

define gui.page_button_borders = Borders(15, 6, 15, 6)
define gui.page_button_text_size = 20

## ── NVL 模式（保留默认，本游戏主要使用 ADV 模式）──────────
define gui.nvl_borders = Borders(0, 15, 0, 30)
define gui.nvl_height = 173
define gui.nvl_spacing = 15
define gui.nvl_name_xpos = 645
define gui.nvl_name_ypos = 0
define gui.nvl_name_width = 225
define gui.nvl_name_xalign = 1.0
define gui.nvl_text_xpos = 675
define gui.nvl_text_ypos = 12
define gui.nvl_text_width = 885
define gui.nvl_text_xalign = 0.0
define gui.nvl_thought_xpos = 360
define gui.nvl_thought_ypos = 0
define gui.nvl_thought_width = 1170
define gui.nvl_thought_xalign = 0.0
define gui.nvl_button_xpos = 675
define gui.nvl_button_xalign = 0.0
