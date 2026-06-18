## systems/achievements.rpy — 成就系统
## 管理游戏成就的解锁和查询

init python:

    class AchievementSystem:
        """
        成就系统。

        成就分为四类：
        - chapter   — 章节通关成就
        - choice    — 特殊选择成就
        - collection — 收集成就
        - secret    — 隐藏成就
        """

        # 成就定义表
        ACHIEVEMENTS = {
            # 章节成就
            "awaken": {
                "name": "醒",
                "desc": "你开始了旅程",
                "category": "chapter",
                "secret": False,
            },
            "crack": {
                "name": "裂",
                "desc": "你看到了爱的两面",
                "category": "chapter",
                "secret": False,
            },
            "mirror": {
                "name": "镜",
                "desc": "你看到了真相的一角",
                "category": "chapter",
                "secret": False,
            },
            "void": {
                "name": "虚",
                "desc": "你看到了美丽的代价",
                "category": "chapter",
                "secret": False,
            },
            "truth": {
                "name": "真",
                "desc": "你看到了真实的力量",
                "category": "chapter",
                "secret": False,
            },
            "merge": {
                "name": "合",
                "desc": "你面对了自己的过去",
                "category": "chapter",
                "secret": False,
            },
            "ferry": {
                "name": "渡",
                "desc": "你做出了最终选择",
                "category": "chapter",
                "secret": False,
            },

            # 特殊选择成就
            "first_silence": {
                "name": "沉默是金",
                "desc": "第一次选择沉默",
                "category": "choice",
                "secret": False,
            },
            "balanced_path": {
                "name": "行走于中间",
                "desc": "保持平衡选择到第三章",
                "category": "choice",
                "secret": False,
            },
            "all_silence_ch1": {
                "name": "寂静之声",
                "desc": "在第一章的所有选择中保持沉默",
                "category": "choice",
                "secret": True,
            },

            # 收集成就
            "memory_collector": {
                "name": "拾遗者",
                "desc": "收集第一块记忆碎片",
                "category": "collection",
                "secret": False,
            },
            "memory_master": {
                "name": "完整之人",
                "desc": "收集全部记忆碎片",
                "category": "collection",
                "secret": False,
            },

            # 隐藏成就
            "epilogue": {
                "name": "归家",
                "desc": "你终于找到了回家的路",
                "category": "secret",
                "secret": True,
            },
            "liar_truth": {
                "name": "假中之真",
                "desc": "在右城选择说真话超过五次",
                "category": "secret",
                "secret": True,
            },
            "truthful_lie": {
                "name": "真中之假",
                "desc": "在左城选择说假话超过五次",
                "category": "secret",
                "secret": True,
            },
        }

        def __init__(self):
            self.unlocked = set()  # 已解锁的成就 ID

        def unlock(self, achievement_id):
            """解锁成就，返回是否为新解锁"""
            if achievement_id in self.unlocked:
                return False
            if achievement_id not in self.ACHIEVEMENTS:
                return False
            self.unlocked.add(achievement_id)
            tracker.log_event("achievement_unlocked", {"id": achievement_id})
            return True

        def is_unlocked(self, achievement_id):
            """检查成就是否已解锁"""
            return achievement_id in self.unlocked

        def get_info(self, achievement_id):
            """获取成就信息"""
            ach = self.ACHIEVEMENTS.get(achievement_id)
            if not ach:
                return None
            return {
                "id": achievement_id,
                "unlocked": achievement_id in self.unlocked,
                **ach,
            }

        def get_all_by_category(self, category):
            """获取指定分类的所有成就"""
            result = []
            for aid, info in self.ACHIEVEMENTS.items():
                if info["category"] == category:
                    result.append(self.get_info(aid))
            return result

        def get_unlocked_count(self):
            """已解锁数量"""
            return len(self.unlocked)

        def get_total_count(self):
            """总成就数量"""
            return len(self.ACHIEVEMENTS)

        def get_progress_display(self):
            """返回进度字符串"""
            return "%d/%d" % (self.get_unlocked_count(), self.get_total_count())

        def check_and_unlock_chapter(self, chapter_num):
            """检查并解锁章节成就"""
            chapter_map = {
                1: "awaken",
                2: "crack",
                3: "mirror",
                4: "void",
                5: "truth",
                6: "merge",
                7: "ferry",
            }
            aid = chapter_map.get(chapter_num)
            if aid:
                return self.unlock(aid)
            return False

# 全局实例
default achievements = AchievementSystem()

# ── 成就通知 Screen ───────────────────────────────────────

screen achievement_notification(achievement_id):
    zorder 300

    $ ach_info = achievements.get_info(achievement_id)

    if ach_info:
        frame:
            align (0.5, 0.05)
            xsize 500
            ysize 80
            background Solid("#1A1A2ECC")
            padding (20, 15, 20, 15)

            hbox:
                spacing 15
                align (0.5, 0.5)

                text "✦":
                    size 28
                    color "#C0C0C0"
                    yalign 0.5

                vbox:
                    spacing 4
                    text ach_info["name"]:
                        size 22
                        color "#E8E8E8"
                    text ach_info["desc"]:
                        size 16
                        color "#9B9B9B"

    timer 3.0 action Hide("achievement_notification")
