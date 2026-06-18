## styles/right_city_styles.rpy — 右城 UI 样式
## 暖金色调，圆角，软边，丝绸质感

## ── 对话框窗口 ─────────────────────────────────────────────
style right_city_window is default:
    background Frame("ui/right_dialogue_bg.png", 30, 30)
    padding (45, 35, 45, 25)
    xminimum 1600
    xmaximum 1600
    yminimum 250
    ymaximum 300
    xpos 160
    ypos 760

## ── 名字标签框 ─────────────────────────────────────────────
style right_city_namebox is default:
    background Solid("#D4A574")
    padding (15, 8, 15, 8)
    xminimum 120
    xpos 45
    ypos -40

## ── 名字文字 ──────────────────────────────────────────────
style right_city_name_text is default:
    font gui.name_text_font
    size 24
    color "#FFFFFF"
    bold True

## ── 对话正文 ──────────────────────────────────────────────
style right_city_dialogue_text is default:
    font gui.text_font
    size 28
    color "#FFF8E7"
    line_spacing 12
    xalign 0.5
    text_align 0.5

## ── 按钮（右城风格）────────────────────────────────────────
style right_city_button is default:
    background Frame("ui/right_btn_idle.png", 15, 15)
    hover_background Frame("ui/right_btn_hover.png", 15, 15)
    selected_background Frame("ui/right_btn_selected.png", 15, 15)
    insensitive_background Frame("ui/right_btn_insensitive.png", 15, 15)
    padding (25, 14, 25, 14)
    xminimum 200

style right_city_button_text is default:
    font gui.button_text_font
    size 22
    color "#FFF8E7"
    hover_color "#FFFFFF"
    selected_color "#D4A574"
    insensitive_color "#8A8070"
