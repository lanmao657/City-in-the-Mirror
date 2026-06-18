## transforms/ui_animations.rpy — UI 微动效

## ── 呼吸效果 ──────────────────────────────────────────────

## 缓慢呼吸脉动（沉默选项提示、HUD 元素）
transform breathe:
    alpha 0.15
    linear 2.0 alpha 0.30
    linear 2.0 alpha 0.15
    repeat

## 快速呼吸（警告状态）
transform breathe_fast:
    alpha 0.3
    linear 0.8 alpha 0.7
    linear 0.8 alpha 0.3
    repeat

## ── 悬浮效果 ──────────────────────────────────────────────

## 缓慢上下悬浮（粒子、装饰元素）
transform gentle_float:
    yoffset 0
    linear 3.0 yoffset -8
    linear 3.0 yoffset 0
    repeat

## ── 旋转效果 ──────────────────────────────────────────────

## 缓慢旋转（镜面碎片粒子）
transform slow_rotate:
    rotate 0
    linear 20.0 rotate 360
    repeat

## ── 光效 ─────────────────────────────────────────────────

## 镜面边缘光效呼吸
transform mirror_edge_glow:
    alpha 0.2
    linear 3.0 alpha 0.5
    linear 3.0 alpha 0.2
    repeat

## 选项悬停光效扩展
transform hover_glow_expand:
    zoom 1.0 alpha 0.3
    linear 0.3 zoom 1.05 alpha 0.5
    linear 0.3 zoom 1.0 alpha 0.3
    repeat

## ── 选择反馈 ──────────────────────────────────────────────

## 选项确认闪烁
transform confirm_flash:
    alpha 1.0
    linear 0.1 alpha 0.5
    linear 0.1 alpha 1.0
    linear 0.1 alpha 0.3
    linear 0.15 alpha 0.0

## ── 成就通知 ──────────────────────────────────────────────

## 成就通知滑入
transform achievement_slidein:
    yoffset -80 alpha 0.0
    linear 0.5 yoffset 0 alpha 1.0

## 成就通知滑出
transform achievement_slideout:
    yoffset 0 alpha 1.0
    linear 0.5 yoffset -80 alpha 0.0

## 成就通知完整动画
transform achievement_show:
    yoffset -80 alpha 0.0
    linear 0.5 yoffset 0 alpha 1.0
    pause 2.5
    linear 0.5 yoffset -80 alpha 0.0
