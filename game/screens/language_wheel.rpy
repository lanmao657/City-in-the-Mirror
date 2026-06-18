## screens/language_wheel.rpy — 语言轮盘系统
## 游戏的核心交互组件：真话 / 假话 / 沉默

screen language_wheel(truth_text, lie_text, context_text="",
                      silent_available=True,
                      chapter="", npc="", scene=""):
    modal True
    zorder 200

    # ── 半透明遮罩 ──
    add Solid("#000000") alpha 0.4

    # ── 轮盘主体 ──
    frame at wheel_appear:
        align (0.5, 0.5)
        xsize 920
        ysize 520
        background Solid("#1A1A2EF0")
        padding (30, 25, 30, 25)

        vbox:
            align (0.5, 0.5)
            spacing 15

            # ── 情境提示 ──
            if context_text:
                text context_text:
                    align (0.5, 0.0)
                    size 20
                    color "#808080"
                    text_align 0.5
                    italic True

            null height 5

            # ── 双选项区域 ──
            hbox:
                align (0.5, 0.5)
                spacing 30

                # ▸ 真话选项 ◂
                button:
                    action [
                        Function(mirror.add_choice, "truth", chapter, npc, scene),
                        SetVariable("last_choice", "truth"),
                        Return("truth"),
                    ]
                    xsize 380
                    ysize 300
                    background Solid("#3A4A5C")
                    hover_background Solid("#4A6FA5")
                    padding (25, 20, 25, 20)

                    vbox:
                        align (0.5, 0.5)
                        spacing 12

                        text "❄ 真话":
                            align (0.5, 0.0)
                            size 20
                            color "#4A90D9"
                            bold True

                        null height 5

                        text truth_text:
                            align (0.5, 0.5)
                            size 24
                            color "#D0DCE8"
                            text_align 0.5
                            xmaximum 330

                # ▸ 假话选项 ◂
                button:
                    action [
                        Function(mirror.add_choice, "lie", chapter, npc, scene),
                        SetVariable("last_choice", "lie"),
                        Return("lie"),
                    ]
                    xsize 380
                    ysize 300
                    background Solid("#4A3A2C")
                    hover_background Solid("#6A5A40")
                    padding (25, 20, 25, 20)

                    vbox:
                        align (0.5, 0.5)
                        spacing 12

                        text "假话 ✿":
                            align (0.5, 0.0)
                            size 20
                            color "#D4A574"
                            bold True

                        null height 5

                        text lie_text:
                            align (0.5, 0.5)
                            size 24
                            color "#FFF8E7"
                            text_align 0.5
                            xmaximum 330

            # ── 沉默选项（隐藏但可访问）──
            if silent_available:
                null height 10

                button at breathe:
                    action [
                        Function(mirror.add_choice, "silent", chapter, npc, scene),
                        SetVariable("last_choice", "silent"),
                        Return("silent"),
                    ]
                    align (0.5, 1.0)
                    xsize 140
                    ysize 45
                    background Solid("#9B9B9B20")
                    hover_background Solid("#9B9B9B40")
                    padding (15, 8, 15, 8)

                    text "沉默":
                        align (0.5, 0.5)
                        size 18
                        color "#9B9B9B"
                        text_align 0.5

                # 快捷键提示（极淡）
                text "按 S 键沉默" size 12 color "#505050":
                    align (0.5, 1.0)

    # 快捷键绑定
    if silent_available:
        key "s" action [
            Function(mirror.add_choice, "silent", chapter, npc, scene),
            SetVariable("last_choice", "silent"),
            Return("silent"),
        ]
    key "1" action [
        Function(mirror.add_choice, "truth", chapter, npc, scene),
        SetVariable("last_choice", "truth"),
        Return("truth"),
    ]
    key "2" action [
        Function(mirror.add_choice, "lie", chapter, npc, scene),
        SetVariable("last_choice", "lie"),
        Return("lie"),
    ]
