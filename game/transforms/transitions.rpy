## transforms/transitions.rpy — 场景转场动画

## ── 基础转场 ──────────────────────────────────────────────

## 左城进入：画面碎裂后重组（模拟石板裂开）
transform left_city_enter:
    alpha 0.0
    linear 0.3 alpha 0.5
    linear 0.2 alpha 0.3
    linear 0.3 alpha 1.0

## 右城进入：画面融化后浮现（模拟花瓣展开）
transform right_city_enter:
    alpha 0.0
    linear 0.5 alpha 0.3
    linear 0.5 alpha 0.7
    linear 0.5 alpha 1.0

## 镜墙穿越：镜面折射效果
transform mirror_cross:
    alpha 0.0
    zoom 1.2
    linear 0.3 zoom 1.0 alpha 0.5
    linear 0.4 zoom 0.95 alpha 0.8
    linear 0.3 zoom 1.0 alpha 1.0

## ── 章节转场 ──────────────────────────────────────────────

## 章节标题淡入
transform chapter_title_enter:
    alpha 0.0 yoffset 20
    linear 1.0 alpha 1.0 yoffset 0

## 章节标题淡出
transform chapter_title_exit:
    alpha 1.0
    linear 1.0 alpha 0.0 yoffset -20

## 章节标题完整动画
transform chapter_title_show:
    alpha 0.0 yoffset 30
    linear 1.0 alpha 1.0 yoffset 0
    pause 2.0
    linear 1.0 alpha 0.0 yoffset -30

## ── 记忆闪回 ──────────────────────────────────────────────

## 闪回进入：画面边缘出现老胶片效果
transform flashback_enter:
    alpha 0.0
    matrixcolor TintMatrix("#FFE8A0") * SaturationMatrix(0.6)
    linear 0.5 alpha 1.0

## 闪回退出
transform flashback_exit:
    alpha 1.0
    linear 0.5 alpha 0.0

## ── 元素动画 ──────────────────────────────────────────────

## 从下方升起（对话框进入）
transform rise_from_bottom:
    yoffset 50 alpha 0.0
    linear 0.4 yoffset 0 alpha 1.0

## 向下沉没（对话框退出）
transform sink_to_bottom:
    yoffset 0 alpha 1.0
    linear 0.3 yoffset 30 alpha 0.0

## 中央缩放出现（语言轮盘）
transform wheel_appear:
    alpha 0.0 zoom 0.8
    linear 0.4 alpha 1.0 zoom 1.0

## 中央缩放消失
transform wheel_disappear:
    alpha 1.0 zoom 1.0
    linear 0.3 alpha 0.0 zoom 1.1

## 左侧选项碎裂效果
transform truth_shatter:
    alpha 1.0
    linear 0.15 alpha 0.8 xoffset -5
    linear 0.15 alpha 0.5 xoffset -15
    linear 0.2 alpha 0.0 xoffset -30

## 右侧选项融化效果
transform lie_melt:
    alpha 1.0 yoffset 0
    linear 0.2 alpha 0.8 yoffset 3
    linear 0.2 alpha 0.5 yoffset 8
    linear 0.2 alpha 0.0 yoffset 20

## 沉默选项消隐效果
transform silent_fade:
    alpha 1.0
    linear 0.5 alpha 0.0

## ── 文字动画 ──────────────────────────────────────────────

## 文字逐行淡入（旁白用）
transform text_line_fadein:
    alpha 0.0
    linear 0.5 alpha 1.0

## 文字打字机出现后停留
transform text_type_appear:
    alpha 0.0
    linear 0.3 alpha 1.0

## ── HUD 动画 ──────────────────────────────────────────────

## HUD 元素淡入
transform hud_fadein:
    alpha 0.0
    linear 0.5 alpha 1.0

## HUD 元素淡出
transform hud_fadeout:
    alpha 1.0
    linear 0.5 alpha 0.0

## 章节名出现（左上角）
transform chapter_name_appear:
    alpha 0.0 xoffset -20
    linear 0.5 alpha 1.0 xoffset 0

## 章节名消失
transform chapter_name_disappear:
    alpha 1.0
    linear 0.5 alpha 0.0 xoffset -20
