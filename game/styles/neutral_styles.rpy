## styles/neutral_styles.rpy — 中性 UI 样式
## 用于镜墙区域、系统菜单、存档界面

## ── 通用中性窗口 ──────────────────────────────────────────
style neutral_window is default:
    background Frame("ui/neutral_bg.png", 20, 20)
    padding (30, 25, 30, 25)

## ── 系统菜单按钮 ──────────────────────────────────────────
style system_button is default:
    background Solid("#FFFFFF10")
    hover_background Solid("#FFFFFF20")
    selected_background Solid("#FFFFFF30")
    insensitive_background Solid("#FFFFFF08")
    padding (40, 16, 40, 16)
    xminimum 300

style system_button_text is default:
    font gui.interface_text_font
    size 26
    color "#C0C0C0"
    hover_color "#FFFFFF"
    selected_color "#E8E8E8"
    insensitive_color "#606060"
    text_align 0.5
    xalign 0.5

## ── 标题文字 ──────────────────────────────────────────────
style game_title is default:
    font "DejaVuSans.ttf"  # 替换为方正清刻本悦宋
    size 64
    color "#E8E8E8"
    text_align 0.5
    xalign 0.5

style game_subtitle is default:
    font gui.interface_text_font
    size 24
    color "#808080"
    text_align 0.5
    xalign 0.5
    italic True

## ── 设置界面 ──────────────────────────────────────────────
style settings_label is default:
    font gui.interface_text_font
    size 22
    color "#A0A0A0"

style settings_value is default:
    font gui.interface_text_font
    size 22
    color "#E8E8E8"

## ── 存档位 ───────────────────────────────────────────────
style save_slot_frame is default:
    background Solid("#FFFFFF08")
    hover_background Solid("#FFFFFF15")
    padding (20, 15, 20, 15)
    xminimum 700
    yminimum 120

style save_slot_text is default:
    font gui.interface_text_font
    size 18
    color "#B0B0B0"

style save_slot_chapter is default:
    font gui.interface_text_font
    size 22
    color "#E8E8E8"
