## systems/city_state.rpy — 城市健康度系统
## 追踪左城和右城的整体状态，影响场景外观和NPC行为

init python:

    class CityState:
        """
        城市状态系统。

        追踪两座城市的健康度，影响：
        - 场景背景的外观（裂缝、颜色饱和度等）
        - NPC 的对话内容和行为
        - 可用的支线和事件
        - 最终结局的细节
        """

        # 健康度等级阈值
        HEALTH_HEALTHY  = 70   # 70-100 健康
        HEALTH_UNSTABLE = 40   # 40-69  不稳定
        HEALTH_CRISIS   = 0    # 0-39   危机

        def __init__(self):
            self.left_health = 100
            self.right_health = 100
            self.left_unrest = 0     # 左城不安定度
            self.right_unrest = 0    # 右城不安定度
            self.mirror_integrity = 100  # 镜墙完整度

        # ── 健康度操作 ────────────────────────────────────

        def adjust_left(self, delta):
            """调整左城健康度，返回实际变化量"""
            old = self.left_health
            self.left_health = max(0, min(100, self.left_health + delta))
            actual = self.left_health - old
            if actual != 0:
                tracker.log_event("city_health_change", {
                    "city": "left",
                    "delta": actual,
                    "new_value": self.left_health,
                })
            return actual

        def adjust_right(self, delta):
            """调整右城健康度"""
            old = self.right_health
            self.right_health = max(0, min(100, self.right_health + delta))
            actual = self.right_health - old
            if actual != 0:
                tracker.log_event("city_health_change", {
                    "city": "right",
                    "delta": actual,
                    "new_value": self.right_health,
                })
            return actual

        def adjust_mirror(self, delta):
            """调整镜墙完整度"""
            self.mirror_integrity = max(0, min(100, self.mirror_integrity + delta))

        # ── 状态查询 ──────────────────────────────────────

        def get_left_status(self):
            """返回左城健康等级: 'healthy' / 'unstable' / 'crisis'"""
            if self.left_health >= self.HEALTH_HEALTHY:
                return "healthy"
            elif self.left_health >= self.HEALTH_UNSTABLE:
                return "unstable"
            return "crisis"

        def get_right_status(self):
            """返回右城健康等级"""
            if self.right_health >= self.HEALTH_HEALTHY:
                return "healthy"
            elif self.right_health >= self.HEALTH_UNSTABLE:
                return "unstable"
            return "crisis"

        def get_left_color(self):
            """返回左城状态对应的 HUD 颜色"""
            status = self.get_left_status()
            colors = {
                "healthy":  "#4A90D9",  # 正常蓝
                "unstable": "#D4A574",  # 警告暖色
                "crisis":   "#C44B4B",  # 危机红
            }
            return colors[status]

        def get_right_color(self):
            """返回右城状态对应的 HUD 颜色"""
            status = self.get_right_status()
            colors = {
                "healthy":  "#D4A574",  # 正常暖金
                "unstable": "#D4A574",  # 警告
                "crisis":   "#C44B4B",  # 危机红
            }
            return colors[status]

        def either_in_crisis(self):
            """是否有任一城市处于危机状态"""
            return self.left_health < self.HEALTH_UNSTABLE or \
                   self.right_health < self.HEALTH_UNSTABLE

        def both_healthy(self):
            """两城是否都健康"""
            return self.left_health >= self.HEALTH_HEALTHY and \
                   self.right_health >= self.HEALTH_HEALTHY

        # ── 不安定度 ──────────────────────────────────────

        def add_unrest(self, city, amount):
            """增加城市不安定度"""
            if city == "left":
                self.left_unrest = min(100, self.left_unrest + amount)
            else:
                self.right_unrest = min(100, self.right_unrest + amount)

        def reduce_unrest(self, city, amount):
            """降低城市不安定度"""
            if city == "left":
                self.left_unrest = max(0, self.left_unrest - amount)
            else:
                self.right_unrest = max(0, self.right_unrest - amount)

        def get_unrest(self, city):
            """获取城市不安定度"""
            return self.left_unrest if city == "left" else self.right_unrest

# 全局实例
default city_state = CityState()
