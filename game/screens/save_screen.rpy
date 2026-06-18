## screens/save_screen.rpy — 自定义存档/读档界面

screen save_slots(title_text, is_save=True):
    tag menu
    modal True

    add Solid("#000000D0")

    # 标题
    text title_text align (0.5, 0.06) size 32 color "#C0C0C0"

    # 存档位列表
    vbox:
        align (0.5, 0.5)
        spacing 12

        for slot_idx in range(1, 11):
            $ slot_name = "Slot %d" % slot_idx
            $ save_data = renpy.slot_json(slot_name)

            button style "save_slot_frame":
                action (
                    [FileSave(slot_name) if is_save else FileLoad(slot_name)]
                )
                xsize 800

                hbox:
                    spacing 20

                    # 缩略图
                    add FileScreenshot(slot_name):
                        xsize 160
                        ysize 90
                        if not save_data:
                            alpha 0.3

                    # 存档信息
                    vbox:
                        spacing 5
                        if save_data:
                            $ ch_name = save_data.get("extra_info", {}).get("chapter", "")
                            $ truth_c = save_data.get("extra_info", {}).get("truth", 0)
                            $ lie_c = save_data.get("extra_info", {}).get("lie", 0)
                            $ silent_c = save_data.get("extra_info", {}).get("silent", 0)

                            text slot_name size 16 color "#808080"
                            text ch_name style "save_slot_chapter"
                            hbox spacing 10:
                                text "❄ %d" % truth_c size 16 color "#4A90D9"
                                text "✿ %d" % lie_c size 16 color "#D4A574"
                                text "◇ %d" % silent_c size 16 color "#9B9B9B"
                        else:
                            text slot_name size 16 color "#606060"
                            text "——空存档位——" size 20 color "#404040" italic True

    # 底部按钮
    hbox align (0.5, 0.92) spacing 40:
        textbutton "返回" action Return() style "system_button"

    key "K_ESCAPE" action Return()


screen save_menu():
    use save_slots("存 档", is_save=True)

screen load_menu():
    use save_slots("读取存档", is_save=False)
