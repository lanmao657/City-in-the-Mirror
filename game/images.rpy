## images.rpy — 图片资源定义与占位
## 所有正式美术素材在此统一管理
## 开发阶段使用纯色占位，正式制作时替换为实际图片

## ── 背景图（全部接入实际素材）─────────────────────────────

## 通用
image bg black = Solid("#0A0A15")
image bg white = Solid("#F5F5F5")

## 镜墙
image bg mirror_crack = "images/backgrounds/mirror_crack.png"
image bg mirror_wall_outside = "images/backgrounds/mirror_wall_outside.png"
image bg mirror_inside = "images/backgrounds/mirror_inside.png"
image bg mirror_center = "images/backgrounds/mirror_center.png"

## 左城
image bg left_city_entrance = "images/backgrounds/left_city_entrance.png"
image bg left_city_street = "images/backgrounds/left_city_street.png"
image bg left_city_workshop = "images/backgrounds/left_city_workshop.png"
image bg left_city_garden = "images/backgrounds/left_city_garden.png"
image bg left_city_square = "images/backgrounds/left_city_square.png"

## 右城
image bg right_city_entrance = "images/backgrounds/right_city_entrance.png"
image bg right_city_studio = "images/backgrounds/right_city_studio.png"
image bg right_city_square = "images/backgrounds/right_city_square.png"
image bg right_city_hospital = "images/backgrounds/right_city_hospital.png"
image bg smile_garden = "images/backgrounds/smile_garden.png"

## 闪回
image bg flashback_house = "images/backgrounds/flashback_house.png"
image bg flashback_rain = "images/backgrounds/flashback_rain.png"
image bg flashback_hospital = "images/backgrounds/flashback_hospital.png"
image bg flashback_river = "images/backgrounds/flashback_river.png"
image bg flashback_child_room = "images/backgrounds/flashback_child_room.png"

## 结局
image bg city_merge_chaos = "images/backgrounds/city_merge_chaos.png"
image bg city_merge_center = "images/backgrounds/city_merge_center.png"
image bg ending_truth = "images/backgrounds/ending_truth.png"
image bg ending_lie = "images/backgrounds/ending_lie.png"
image bg ending_split = "images/backgrounds/ending_split.png"
image bg ending_silent = "images/backgrounds/ending_silent.png"
image bg river = "images/backgrounds/river.png"
image bg river_sunset = "images/backgrounds/river_sunset.png"

## ── 角色立绘占位 ──────────────────────────────────────────
## 使用 Solid 配合 Transform 来模拟立绘占位区域

## 左城角色（冷色调）
image baisui normal = Solid("#3A4A5C", xsize=400, ysize=600)
image xiaoxue normal = Solid("#5A7A9C", xsize=350, ysize=550)
image shiyan normal = Solid("#2A3A4C", xsize=420, ysize=620)
image yan normal = Solid("#4A6A8C", xsize=400, ysize=600)
image li normal = Solid("#5A8AAC", xsize=380, ysize=580)

## 右城角色（暖色调）
image yunshang normal = Solid("#C49060", xsize=380, ysize=600)
image miyu normal = Solid("#D4A574", xsize=370, ysize=590)
image huayan normal = Solid("#B08050", xsize=420, ysize=620)
image ming normal = Solid("#A09070", xsize=400, ysize=600)
image yao normal = Solid("#D0A090", xsize=350, ysize=560)

## 镜墙角色
image ying normal = Solid("#808090", xsize=400, ysize=600)
image hua_child normal = Solid("#909098", xsize=300, ysize=450)

## ── 表情变体占位 ──────────────────────────────────────────
## 正式开发时为每个角色创建 4-6 套表情
## 示例：image baisui smile = "images/characters/left_city/baisui_smile.png"

# image baisui angry = Solid("#2A3A4C", xsize=400, ysize=600)
# image yunshang sad = Solid("#A07040", xsize=380, ysize=600)

## ── UI 元素占位 ──────────────────────────────────────────
## 使用 Solid + Frame 实现 9-slice 效果的占位
## 正式开发时替换为设计好的 UI 素材

## 左城对话框背景
image ui_left_dialogue_bg = Solid("#1A1A2ED0")

## 右城对话框背景
image ui_right_dialogue_bg = Solid("#2A2418D0")

## 中性对话框背景
image ui_neutral_bg = Solid("#1A1A2EF0")

## 按钮状态占位
image ui_left_btn_idle = Solid("#3A4A5C")
image ui_left_btn_hover = Solid("#4A6FA5")
image ui_left_btn_selected = Solid("#4A90D9")
image ui_left_btn_insensitive = Solid("#2A3040")

image ui_right_btn_idle = Solid("#4A3A2C")
image ui_right_btn_hover = Solid("#6A5A40")
image ui_right_btn_selected = Solid("#D4A574")
image ui_right_btn_insensitive = Solid("#3A3020")

## 轮盘背景
image ui_wheel_bg = Solid("#1A1A2EF0")
