## systems/npc_relationship.rpy — NPC 关系系统
## 管理 NPC 关系值、状态查询和便捷操作

init python:

    class NPCRelationship:
        """
        NPC 关系管理的便捷接口。
        底层数据存储在 characters.rpy 的 npc_data 字典中。
        """

        # 关系等级阈值
        LEVEL_HOSTILE  = 0    # 0-19  敌意/冷漠
        LEVEL_NEUTRAL  = 20   # 20-39 中立
        LEVEL_WARM     = 40   # 40-59 温暖
        LEVEL_TRUSTED  = 60   # 60-79 信任
        LEVEL_BONDED   = 80   # 80-100 深厚

        def get(self, npc_id, key="relationship"):
            """获取 NPC 的某个属性"""
            return npc_data.get(npc_id, {}).get(key, None)

        def set_relationship(self, npc_id, value):
            """直接设置关系值"""
            if npc_id in npc_data:
                npc_data[npc_id]["relationship"] = max(0, min(100, value))

        def adjust(self, npc_id, delta):
            """调整关系值，返回实际变化"""
            if npc_id not in npc_data:
                return 0
            old = npc_data[npc_id]["relationship"]
            npc_data[npc_id]["relationship"] = max(0, min(100, old + delta))
            actual = npc_data[npc_id]["relationship"] - old
            if actual != 0:
                tracker.log_event("relationship_change", {
                    "npc": npc_id,
                    "delta": actual,
                    "new_value": npc_data[npc_id]["relationship"],
                })
            return actual

        def get_level(self, npc_id):
            """返回关系等级名称"""
            rel = self.get(npc_id, "relationship") or 0
            if rel >= 80:
                return "bonded"
            elif rel >= 60:
                return "trusted"
            elif rel >= 40:
                return "warm"
            elif rel >= 20:
                return "neutral"
            return "hostile"

        def get_level_display(self, npc_id):
            """返回中文关系等级"""
            level = self.get_level(npc_id)
            display_map = {
                "hostile": "冷漠",
                "neutral": "中立",
                "warm":    "温暖",
                "trusted": "信任",
                "bonded":  "深厚",
            }
            return display_map.get(level, "未知")

        def get_color(self, npc_id):
            """返回关系等级对应的 UI 颜色"""
            level = self.get_level(npc_id)
            color_map = {
                "hostile": "#C44B4B",
                "neutral": "#9B9B9B",
                "warm":    "#D4A574",
                "trusted": "#5C8A5C",
                "bonded":  "#7EC8B0",
            }
            return color_map.get(level, "#9B9B9B")

        def meet(self, npc_id):
            """标记 NPC 已相遇"""
            if npc_id in npc_data:
                npc_data[npc_id]["met"] = True

        def is_met(self, npc_id):
            """检查是否已相遇"""
            return npc_data.get(npc_id, {}).get("met", False)

        def set_flag(self, npc_id, flag_name, value=True):
            """设置 NPC 专属标记"""
            if npc_id in npc_data:
                npc_data[npc_id]["flags"][flag_name] = value

        def get_flag(self, npc_id, flag_name, default=False):
            """获取 NPC 专属标记"""
            return npc_data.get(npc_id, {}).get("flags", {}).get(flag_name, default)

        def above(self, npc_id, threshold):
            """关系值是否高于阈值"""
            return (self.get(npc_id, "relationship") or 0) > threshold

        def below(self, npc_id, threshold):
            """关系值是否低于阈值"""
            return (self.get(npc_id, "relationship") or 0) < threshold

# 全局实例
default npc_rel = NPCRelationship()
