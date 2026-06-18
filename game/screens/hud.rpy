## screens/hud.rpy — HUD 系统
## 章节名、镜像值指示器、记忆碎片进度、城市健康度

## ── 主 HUD ────────────────────────────────────────────────

screen game_hud():
    zorder 100

    # 左上：章节信息（带淡入淡出）
    if current_chapter_name:
        vbox at chapter_name_appear:
            xpos 40
            ypos 25
            spacing 4

            text current_chapter_name:
                size 24
                color "#E8E8E8"
                outlines [(1, "#00000080", 0, 0)]
            if current_chapter_en:
                text current_chapter_en:
                    size 16
                    color "#808080"
                    italic True

    # 右上：菜单按钮
    textbutton "≡" action ShowMenu("pause_menu"):
        xpos 1840
        ypos 25
        text_size 30
        text_color "#FFFFFF80"
        text_hover_color "#FFFFFF"
        background None

    # 左下：记忆碎片进度
    if tracker.get_memory_count() > 0:
        hbox at hud_fadein:
            xpos 40
            ypos 1020
            spacing 8

            for i in range(tracker.MEMORY_TOTAL):
                if i < tracker.get_memory_count():
                    add Solid("#E8E8E8", xsize=8, ysize=8)
                else:
                    add Solid("#404040", xsize=8, ysize=8)

    # 对话框区域：镜像值指示器
    if show_mirror_hint and mirror.total_all > 0:
        use mirror_indicator


## ── 镜像值指示器 ───────────────────────────────────────────

screen mirror_indicator():
    zorder 101

    frame:
        xalign 1.0
        ypos 770
        xoffset -180
        xsize 180
        ysize 10
        background Solid("#00000060")
        padding (0, 0, 0, 0)

        bar:
            value AnimatedValue(mirror.get_bar_value(), 1.0, 0.5)
            xsize 180
            ysize 10
            left_bar Solid("#4A90D9")
            right_bar Solid("#D4A574")

    # 两端标签
    text "❄" size 12 color "#4A90D980":
        xalign 1.0 ypos 768 xoffset -215
    text "✿" size 12 color "#D4A57480":
        xalign 1.0 ypos 768 xoffset -172


## ── 城市健康度 HUD（第四、五章出现）─────────────────────────

screen city_health_hud():
    zorder 100

    frame:
        align (0.5, 0.0)
        yoffset 15
        xsize 400
        ysize 50
        background Solid("#00000060")
        padding (20, 10, 20, 10)

        hbox:
            align (0.5, 0.5)
            spacing 10

            # 左城健康
            vbox:
                xsize 150
                text "左城" size 16 color city_state.get_left_color():
                    xalign 0.0
                bar:
                    value city_state.left_health
                    range 100
                    xsize 150
                    ysize 8
                    left_bar Solid(city_state.get_left_color())

            # 中间镜面标记
            text "◇" size 18 color "#C0C0C0":
                yalign 0.5

            # 右城健康
            vbox:
                xsize 150
                text "右城" size 16 color city_state.get_right_color():
                    xalign 1.0
                bar:
                    value city_state.right_health
                    range 100
                    xsize 150
                    ysize 8
                    left_bar Solid(city_state.get_right_color())


## ── 当前章节变量 ──────────────────────────────────────────
default current_chapter_name = ""
default current_chapter_en = ""
default current_chapter_num = 0
