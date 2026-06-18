## screens/pause_menu.rpy — 暂停菜单

screen pause_menu():
    tag menu
    modal True

    # 毛玻璃遮罩
    add Solid("#000000A0")

    # 菜单容器
    frame:
        align (0.5, 0.5)
        xsize 360
        ysize 400
        background Solid("#1A1A2EF0")
        padding (30, 30, 30, 30)

        vbox:
            align (0.5, 0.5)
            spacing 10

            for btn_text, btn_action in [
                ("返回游戏", Return()),
                ("读取存档", ShowMenu("load_menu")),
                ("设    置", ShowMenu("settings_screen")),
                ("返回主菜单", MainMenu(confirm=True)),
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
                        color "#B0B0B0"
                        hover_color "#FFFFFF"
                        text_align 0.5

    # 快捷键
    key "K_ESCAPE" action Return()
