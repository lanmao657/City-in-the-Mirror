## screens/settings_screen.rpy — 设置界面

screen settings_screen():
    tag menu
    modal True

    add Solid("#000000D0")

    text "设 置" align (0.5, 0.06) size 32 color "#C0C0C0"

    frame:
        align (0.5, 0.5)
        xsize 700
        ysize 700
        background Solid("#1A1A2EE0")
        padding (40, 30, 40, 30)

        vbox:
            spacing 25
            xalign 0.5

            # ── 文字速度 ──
            hbox:
                spacing 20
                text "文字速度" style "settings_label" yalign 0.5 min_width 160
                bar:
                    value Preference("text speed")
                    xsize 350 ysize 8
                    left_bar Solid("#C0C0C0")
                    right_bar Solid("#404040")

            # ── 自动播放速度 ──
            hbox:
                spacing 20
                text "自动速度" style "settings_label" yalign 0.5 min_width 160
                bar:
                    value Preference("auto-forward time")
                    xsize 350 ysize 8
                    left_bar Solid("#C0C0C0")
                    right_bar Solid("#404040")

            null height 10
            text "—— 音频 ——" size 16 color "#606060" xalign 0.5

            # ── 音乐音量 ──
            hbox:
                spacing 20
                text "音乐" style "settings_label" yalign 0.5 min_width 160
                bar:
                    value Preference("music volume")
                    xsize 350 ysize 8
                    left_bar Solid("#C0C0C0")
                    right_bar Solid("#404040")

            # ── 音效音量 ──
            hbox:
                spacing 20
                text "音效" style "settings_label" yalign 0.5 min_width 160
                bar:
                    value Preference("sound volume")
                    xsize 350 ysize 8
                    left_bar Solid("#C0C0C0")
                    right_bar Solid("#404040")

            null height 10
            text "—— 显示 ——" size 16 color "#606060" xalign 0.5

            # ── 全屏 ──
            hbox:
                spacing 20
                text "全屏" style "settings_label" yalign 0.5 min_width 160
                textbutton "[Fullscreen]":
                    action Preference("display", "toggle")
                    style "system_button"

            # ── 镜像值指示器显示 ──
            hbox:
                spacing 20
                text "镜像值显示" style "settings_label" yalign 0.5 min_width 160
                textbutton ("[开启]" if show_mirror_hint else "[关闭]"):
                    action ToggleVariable("show_mirror_hint")
                    style "system_button"

    # 底部按钮
    hbox align (0.5, 0.92) spacing 40:
        textbutton "恢复默认" action [
            Preference("text speed", 40),
            Preference("music volume", 0.8),
            Preference("sound volume", 0.9),
        ] style "system_button"
        textbutton "返回" action Return() style "system_button"

    key "K_ESCAPE" action Return()
