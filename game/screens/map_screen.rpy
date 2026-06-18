## screens/map_screen.rpy — 城市地图导航

## ── 地点数据 ──────────────────────────────────────────────

init python:
    map_locations = {
        # 左城
        "stone_district": {
            "name": "石之区", "city": "left",
            "x": 0.25, "y": 0.35, "unlocked": True,
        },
        "carve_square": {
            "name": "刻痕广场", "city": "left",
            "x": 0.25, "y": 0.50, "unlocked": True,
        },
        "silent_garden": {
            "name": "静默花园", "city": "left",
            "x": 0.25, "y": 0.65, "unlocked": True,
        },
        # 右城
        "paint_district": {
            "name": "绘梦区", "city": "right",
            "x": 0.75, "y": 0.35, "unlocked": True,
        },
        "flower_square": {
            "name": "花语广场", "city": "right",
            "x": 0.75, "y": 0.50, "unlocked": True,
        },
        "smile_garden": {
            "name": "永笑花园", "city": "right",
            "x": 0.75, "y": 0.65, "unlocked": True,
        },
        # 镜墙
        "mirror_wall": {
            "name": "镜墙", "city": "mirror",
            "x": 0.50, "y": 0.45, "unlocked": True,
        },
        "crack": {
            "name": "裂缝", "city": "mirror",
            "x": 0.50, "y": 0.60, "unlocked": True,
        },
    }

    def get_location_color(city):
        colors = {"left": "#4A90D9", "right": "#D4A574", "mirror": "#C0C0C0"}
        return colors.get(city, "#808080")

## ── 当前位置 ──────────────────────────────────────────────
default current_location = "crack"
default visited_locations = {"crack"}

## ── 地图 Screen ───────────────────────────────────────────

screen map_screen():
    tag menu
    modal True

    # 背景遮罩
    add Solid("#000000D0")

    # 地图标题
    text "镜 中 城" align (0.5, 0.08) size 36 color "#C0C0C0":
        outlines [(1, "#404040", 0, 0)]

    # ── 左城区域标签 ──
    text "左 城 · 言真之地" xalign 0.25 ypos 0.18 size 20 color "#4A90D980"
    # ── 右城区域标签 ──
    text "右 城 · 言美之地" xalign 0.75 ypos 0.18 size 20 color "#D4A57480"

    # ── 镜墙分隔线 ──
    # Solid("#C0C0C040", xsize=2, ysize=500):
    #     align (0.5, 0.5)

    # ── 地点标记 ──
    for loc_id, loc in map_locations.items():
        button:
            xpos int(loc["x"] * 1920) - 25
            ypos int(loc["y"] * 1080) - 25
            xsize 150
            ysize 50
            background None

            action [
                SetVariable("current_location", loc_id),
                Function(visited_locations.add, loc_id),
                Hide("map_screen"),
            ]

            hbox:
                spacing 8

                # 位置指示器
                if loc_id == current_location:
                    text "◉" size 22 color get_location_color(loc["city"])
                elif loc_id in visited_locations:
                    text "●" size 18 color get_location_color(loc["city"])
                else:
                    text "○" size 18 color "#606060"

                # 地名
                text loc["name"] size 18 color (
                    "#FFFFFF" if loc_id == current_location
                    else get_location_color(loc["city"]) + "CC"
                )

    # ── 底部操作栏 ──
    hbox align (0.5, 0.92) spacing 40:
        textbutton "前往" action NullAction() style "system_button"
        textbutton "返回" action Hide("map_screen") style "system_button"

    # 快捷键
    key "m" action Hide("map_screen")
    key "K_ESCAPE" action Hide("map_screen")
