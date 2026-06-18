## styles/left_city_styles.rpy — 左城 UI 样式
## 冷蓝灰色调，直角，硬边，石材质感

## ── 对话框窗口 ─────────────────────────────────────────────
style left_city_window is default:
    background Frame("ui/left_dialogue_bg.png", 20, 20)  # 9-slice 切片
    padding (40, 30, 40, 20)
    xminimum 1600
    xmaximum 1600
    yminimum 250
    ymaximum 300
    xpos 160
    ypos 760

## ── 名字标签框 ─────────────────────────────────────────────
style left_city_namebox is default:
    background Solid("#4A90D9")
    padding (15, 8, 15, 8)
    xminimum 120
    xpos 40
    ypos -40  # 嵌入对话框左上角

## ── 名字文字 ──────────────────────────────────────────────
style left_city_name_text is default:
    font gui.name_text_font
    size 24
    color "#FFFFFF"
    bold True

## ── 对话正文 ──────────────────────────────────────────────
style left_city_dialogue_text is default:
    font gui.text_font
    size 28
    color "#E8E8E8"
    line_spacing 10
    xalign 0.0
    text_align 0.0

## ── 按钮（左城风格）────────────────────────────────────────
style left_city_button is default:
    background Frame("ui/left_btn_idle.png", 10, 10)
    hover_background Frame("ui/left_btn_hover.png", 10, 10)
    selected_background Frame("ui/left_btn_selected.png", 10, 10)
    insensitive_background Frame("ui/left_btn_insensitive.png", 10, 10)
    padding (20, 12, 20, 12)
    xminimum 200

style left_city_button_text is default:
    font gui.button_text_font
    size 22
    color "#B8C4D0"
    hover_color "#FFFFFF"
    selected_color "#4A90D9"
    insensitive_color "#5A5A6A"
