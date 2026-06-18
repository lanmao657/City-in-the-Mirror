## systems/consequence.rpy — 后果追踪系统
## 追踪剧情选择的长期后果，管理全局标记和条件检查

init python:

    class ConsequenceTracker:
        """
        后果追踪系统。

        flags         — 全局剧情标记（dict: str → any）
        memories      — 已收集的记忆碎片（set of str）
        unlocked_scenes — 已解锁的隐藏场景（set of str）
        events_log    — 关键事件日志（list of dict）
        """

        def __init__(self):
            self.flags = {}
            self.memories = set()
            self.unlocked_scenes = set()
            self.events_log = []

        # ── 标记系统 ──────────────────────────────────────

        def set_flag(self, flag_name, value=True):
            """设置一个剧情标记"""
            self.flags[flag_name] = value

        def get_flag(self, flag_name, default=False):
            """获取剧情标记，不存在时返回 default"""
            return self.flags.get(flag_name, default)

        def toggle_flag(self, flag_name):
            """切换标记状态"""
            self.flags[flag_name] = not self.flags.get(flag_name, False)

        def has_flag(self, flag_name):
            """检查标记是否存在且为真"""
            return bool(self.flags.get(flag_name, False))

        # ── 记忆碎片系统 ─────────────────────────────────

        def collect_memory(self, memory_id):
            """收集一个记忆碎片，返回是否为新碎片"""
            if memory_id in self.memories:
                return False
            self.memories.add(memory_id)
            self.log_event("memory_collected", {"id": memory_id})
            return True

        def has_memory(self, memory_id):
            """检查是否已收集某记忆碎片"""
            return memory_id in self.memories

        def get_memory_count(self):
            """返回已收集的记忆碎片数量"""
            return len(self.memories)

        MEMORY_TOTAL = 12  # 总记忆碎片数量

        def get_memory_progress(self):
            """返回收集进度字符串"""
            return "%d/%d" % (len(self.memories), self.MEMORY_TOTAL)

        def all_memories_collected(self):
            """是否收集了全部记忆碎片"""
            return len(self.memories) >= self.MEMORY_TOTAL

        # ── 隐藏场景解锁 ─────────────────────────────────

        def unlock_scene(self, scene_id):
            """解锁隐藏场景"""
            self.unlocked_scenes.add(scene_id)

        def is_scene_unlocked(self, scene_id):
            """检查隐藏场景是否已解锁"""
            return scene_id in self.unlocked_scenes

        # ── 条件检查系统 ─────────────────────────────────

        def check_conditions(self, conditions):
            """
            检查一组条件是否全部满足。

            conditions 格式 (dict):
                "flag_xxx"          → get_flag("xxx") 为 True
                "no_flag_xxx"       → get_flag("xxx") 为 False
                "mirror_truth_gt"   → mirror.truth_ratio > value
                "mirror_lie_gt"     → mirror.lie_ratio > value
                "mirror_silent_gt"  → mirror.silent_ratio > value
                "mirror_alignment"  → mirror.get_alignment() == value
                "memory_count_gte"  → 收集的记忆碎片 >= value
                "memory_xxx"        → has_memory("xxx") 为 True
                "rel_npc_gt"        → npc_data[npc].relationship > value
                "city_left_gt"      → city_state.left_health > value
                "city_right_gt"     → city_state.right_health > value
                "scene_unlocked"    → is_scene_unlocked 为 True
                "chapter_done"      → has_flag("chapter_X_done") 为 True
            """
            for key, expected in conditions.items():
                # 标记检查
                if key.startswith("no_flag_"):
                    if self.has_flag(key[8:]):
                        return False
                elif key.startswith("flag_"):
                    if not self.has_flag(key[5:]):
                        return False

                # 镜像值检查
                elif key == "mirror_truth_gt":
                    if not (mirror.truth_ratio > expected):
                        return False
                elif key == "mirror_lie_gt":
                    if not (mirror.lie_ratio > expected):
                        return False
                elif key == "mirror_silent_gt":
                    if not (mirror.silent_ratio > expected):
                        return False
                elif key == "mirror_alignment":
                    if mirror.get_alignment() != expected:
                        return False

                # 记忆碎片检查
                elif key == "memory_count_gte":
                    if len(self.memories) < expected:
                        return False
                elif key.startswith("memory_"):
                    if not self.has_memory(key[7:]):
                        return False

                # NPC 关系检查
                elif key.startswith("rel_") and key.endswith("_gt"):
                    npc_id = key[4:-3]
                    rel = npc_data.get(npc_id, {}).get("relationship", 0)
                    if not (rel > expected):
                        return False

                # 城市健康度检查
                elif key == "city_left_gt":
                    if not (city_state.left_health > expected):
                        return False
                elif key == "city_right_gt":
                    if not (city_state.right_health > expected):
                        return False

                # 场景解锁检查
                elif key == "scene_unlocked":
                    if not self.is_scene_unlocked(expected):
                        return False

            return True

        # ── 事件日志 ─────────────────────────────────────

        def log_event(self, event_type, data=None):
            """记录一个关键事件"""
            self.events_log.append({
                "type": event_type,
                "data": data or {},
                "chapter": getattr(store, "current_chapter", ""),
                "mirror_alignment": mirror.get_alignment(),
            })

        def get_events_by_type(self, event_type):
            """按类型筛选事件日志"""
            return [e for e in self.events_log if e["type"] == event_type]

# 全局实例
default tracker = ConsequenceTracker()
