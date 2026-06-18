## screens/main_menu.rpy — 主菜单

screen main_menu():
    tag menu

    # ── 动态背景 ──
    add Solid("#0A0A15")

    # 背景层：镜墙裂缝（使用渐变和形状模拟）
    # 正式开发时替换为背景图: add "images/ui/main_menu_bg.png"
    add Solid("#1A1A2E") alpha 0.6

    # 中央裂纹光线效果
    add Solid("#C0C0C0") alpha 0.08:
        xsize 3 ysize 1080 xalign 0.5
    add Solid("#C0C0C0") alpha 0.04:
        xsize 8 ysize 1080 xalign 0.5
    add Solid("#4A90D9") alpha 0.03:
        xsize 200 ysize 1080 xalign 0.35
    add Solid("#D4A574") alpha 0.03:
        xsize 200 ysize 1080 xalign 0.65

    # ── 标题区域 ──
    vbox at chapter_title_enter:
        align (0.5, 0.25)
        spacing 8

        text "镜 中 城":
            style "game_title"
            size 64
            color "#E8E8E8"
            outlines [(2, "#40404080", 0, 0)]

        text "City of Mirrors":
            style "game_subtitle"
            size 22
            color "#808080"

    # ── 菜单项 ──
    vbox:
        align (0.5, 0.58)
        spacing 8

        for btn_text, btn_action in [
            ("开 始 游 戏", Start()),
            ("继 续 游 戏", ShowMenu("load_menu")),
            ("读 取 存 档", ShowMenu("load_menu")),
            ("设      置", ShowMenu("settings_screen")),
            ("退      出", Quit(confirm=False)),
        ]:
            button:
                action btn_action
                xsize 300
                ysize 55
                background None
                hover_background Solid("#FFFFFF10")
                padding (20, 12, 20, 12)

                text btn_text:
                    align (0.5, 0.5)
                    size 24
                    color "#909090"
                    hover_color "#FFFFFF"
                    text_align 0.5

    # ── 版本信息 ──
    text "v0.1.0" size 14 color "#404040":
        xalign 0.02 yalign 0.97

    # ── 装饰：左城冷色晕 ──
    add Solid("#4A90D9") alpha 0.02:
        xsize 600 ysize 600 xalign 0.1 yalign 0.7

    # ── 装饰：右城暖色晕 ──
    add Solid("#D4A574") alpha 0.02:
        xsize 600 ysize 600 xalign 0.9 yalign 0.3

    # 快速开始（开发用，按 S 跳过）
    # key "s" action Start()
