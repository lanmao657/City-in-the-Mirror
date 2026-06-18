## screens/dialogue.rpy — 对话框系统
## 根据 current_city 动态切换对话框样式

## ── 左城对话框 ─────────────────────────────────────────────

screen say_left(who, what):
    style_prefix "left_city"

    window at rise_from_bottom:
        id "window"

        vbox:
            if who is not None:
                window:
                    id "namebox"
                    style "left_city_namebox"
                    text who style "left_city_name_text" id "who"

            text what style "left_city_dialogue_text" id "what"

    # 快速继续指示器
    if not renpy.in_rollback():
        text "▷" size 16 color "#4A90D980":
            xalign 1.0 yalign 1.0 xoffset -20 yoffset -15

## ── 右城对话框 ─────────────────────────────────────────────

screen say_right(who, what):
    style_prefix "right_city"

    window at rise_from_bottom:
        id "window"

        vbox:
            if who is not None:
                window:
                    id "namebox"
                    style "right_city_namebox"
                    text who style "right_city_name_text" id "who"

            text what style "right_city_dialogue_text" id "what"

    # 右城的装饰光晕（通过悬浮的半透明图片实现）
    # add "ui/right_glow.png" alpha 0.15 xalign 0.5 yalign 1.0 at gentle_float

    if not renpy.in_rollback():
        text "▷" size 16 color "#D4A57480":
            xalign 1.0 yalign 1.0 xoffset -20 yoffset -15

## ── 镜墙 / 中性对话框 ──────────────────────────────────────

screen say_mirror(who, what):
    style_prefix "neutral"

    window at rise_from_bottom:
        id "window"
        xsize 1600
        yminimum 250
        xalign 0.5
        yalign 0.85
        background Solid("#1A1A2ED0")
        padding (40, 30, 40, 20)

        vbox:
            if who is not None:
                hbox:
                    spacing 10
                    null width 5
                    text who size 24 color "#E8E8E8" bold True id "who"

            null height 10
            text what size 28 color "#E8E8E8" id "what"

    if not renpy.in_rollback():
        text "▷" size 16 color "#C0C0C080":
            xalign 1.0 yalign 1.0 xoffset -20 yoffset -15

## ── 旁白对话框（无框，文字浮在画面上）────────────────────────

screen say_narrator(who, what):
    zorder 50

    frame at text_line_fadein:
        xalign 0.5
        yalign 0.38
        xsize 1200
        background None
        padding (0, 0, 0, 0)

        text what:
            size 26
            color "#C0C0C0"
            italic True
            text_align 0.5
            xalign 0.5
            line_spacing 16

## ── 守镜人 · 影 的对话框（半透明雾气风格）───────────────────

screen say_shadow(who, what):
    zorder 50

    # 银色光晕背景
    frame at text_line_fadein:
        xalign 0.5
        yalign 0.65
        xsize 1000
        background Solid("#C0C0C018")
        padding (40, 30, 40, 30)

        vbox:
            spacing 10
            text what:
                size 28
                color "#E8E8E8"
                text_align 0.5
                xalign 0.5
                line_spacing 14

## ── 动态路由 ──────────────────────────────────────────────

## 重写默认 say screen，根据 current_city 路由到对应样式
screen say(who, what):
    if current_city == "left":
        use say_left(who, what)
    elif current_city == "right":
        use say_right(who, what)
    elif current_city == "shadow":
        use say_shadow(who, what)
    elif current_city == "narrator":
        use say_narrator(who, what)
    else:
        use say_mirror(who, what)
