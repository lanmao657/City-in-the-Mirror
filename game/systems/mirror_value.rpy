## systems/mirror_value.rpy — 镜像值系统
## 追踪玩家的真话/假话/沉默倾向，影响 UI 色调和剧情走向

init python:

    class MirrorValue:
        """
        镜像值系统：追踪玩家所有选择的倾向。

        属性:
            truth_score   — 真话选择次数
            lie_score     — 假话选择次数
            silent_count  — 沉默选择次数
            choices       — 完整选择历史 [{type, chapter, npc, scene}]

        对齐类型 (alignment):
            truth_seeker — 真话倾向 >70%
            lie_weaver   — 假话倾向 >70%
            silent_one   — 沉默 >40%
            balanced     — 真话和假话均在 30%-70%
            neutral      — 初始状态
        """

        def __init__(self):
            self.truth_score = 0
            self.lie_score = 0
            self.silent_count = 0
            self.choices = []

        def add_choice(self, choice_type, chapter="", npc="", scene=""):
            """记录一次选择"""
            self.choices.append({
                "type": choice_type,
                "chapter": chapter,
                "npc": npc,
                "scene": scene,
            })
            if choice_type == "truth":
                self.truth_score += 1
            elif choice_type == "lie":
                self.lie_score += 1
            elif choice_type == "silent":
                self.silent_count += 1

        @property
        def total(self):
            """总选择次数（不含沉默）"""
            return self.truth_score + self.lie_score

        @property
        def total_all(self):
            """总选择次数（含沉默）"""
            return self.truth_score + self.lie_score + self.silent_count

        @property
        def truth_ratio(self):
            """真话占比（0.0 ~ 1.0），仅在有选择时返回"""
            if self.total == 0:
                return 0.5
            return self.truth_score / self.total

        @property
        def lie_ratio(self):
            """假话占比"""
            if self.total == 0:
                return 0.5
            return self.lie_score / self.total

        @property
        def silent_ratio(self):
            """沉默在所有选择中的占比"""
            if self.total_all == 0:
                return 0.0
            return self.silent_count / self.total_all

        def get_alignment(self):
            """
            返回当前对齐类型。

            优先级：
            1. 沉默占比 >40% → silent_one
            2. 真话占比 >70% → truth_seeker
            3. 假话占比 >70% → lie_weaver
            4. 真话和假话均在 30%-70% → balanced
            5. 其他 → neutral
            """
            if self.total_all == 0:
                return "neutral"

            if self.silent_ratio > 0.4:
                return "silent_one"
            if self.truth_ratio > 0.7:
                return "truth_seeker"
            if self.lie_ratio > 0.7:
                return "lie_weaver"
            if 0.3 <= self.truth_ratio <= 0.7:
                return "balanced"
            return "neutral"

        def get_water_color(self):
            """
            根据对齐类型返回 UI 色调。
            返回 (r, g, b) 元组，值域 0-255。
            """
            alignment = self.get_alignment()
            color_map = {
                "truth_seeker": (74, 108, 165),   # 冷蓝 #4A6FA5
                "lie_weaver":   (216, 168, 124),   # 暖金 #D8A87C
                "silent_one":   (140, 140, 150),   # 灰色 #8C8C96
                "balanced":     (126, 200, 176),   # 青绿 #7EC8B0
                "neutral":      (180, 180, 190),   # 浅灰 #B4B4BE
            }
            return color_map.get(alignment, (180, 180, 190))

        def get_water_hex(self):
            """返回十六进制颜色字符串"""
            r, g, b = self.get_water_color()
            return "#%02X%02X%02X" % (r, g, b)

        def get_alignment_display(self):
            """返回用于 UI 显示的对齐名称"""
            name_map = {
                "truth_seeker": "言真者",
                "lie_weaver":   "织谎者",
                "silent_one":   "沉默者",
                "balanced":     "渡者",
                "neutral":      "行者",
            }
            return name_map.get(self.get_alignment(), "行者")

        def get_bar_value(self):
            """
            返回用于 HUD 渐变条的数值 (0.0 ~ 1.0)。
            0.0 = 完全真话，1.0 = 完全假话。
            """
            return self.lie_ratio

        def check_threshold(self, threshold_type, value):
            """
            检查是否满足阈值条件。
            threshold_type: "truth_ratio" / "lie_ratio" / "silent_ratio" / "total"
            """
            if threshold_type == "truth_ratio":
                return self.truth_ratio >= value
            elif threshold_type == "lie_ratio":
                return self.lie_ratio >= value
            elif threshold_type == "silent_ratio":
                return self.silent_ratio >= value
            elif threshold_type == "total":
                return self.total_all >= value
            return False

        def get_history_for_chapter(self, chapter):
            """返回指定章节的所有选择"""
            return [c for c in self.choices if c["chapter"] == chapter]

        def get_history_for_npc(self, npc):
            """返回与指定 NPC 相关的所有选择"""
            return [c for c in self.choices if c["npc"] == npc]

# 全局实例
default mirror = MirrorValue()
