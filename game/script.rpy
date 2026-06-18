## script.rpy — 主脚本入口
## 《镜中城》游戏主流程控制

## ── 全局状态 ──────────────────────────────────────────────

## 当前章节编号（用于存档显示和条件判断）
default current_chapter = 0

## 是否已完成至少一周目
default game_completed = False

## ── 游戏开始 ──────────────────────────────────────────────

label start:
    ## 初始化游戏状态
    $ game_started = True
    $ current_chapter = 0
    $ current_city = "narrator"
    $ current_chapter_name = ""
    $ current_chapter_en = ""

    ## 显示 HUD
    show screen game_hud

    ## 进入序章
    jump prologue

## ── 序章：镜中醒来 ────────────────────────────────────────

label prologue:
    $ current_chapter = 0
    $ current_city = "narrator"

    scene bg black

    "你醒来时，面前是一面镜子。"
    "镜子里的人，是你。"
    "但你不知道那是谁。"

    scene bg mirror_crack with dissolve

    "你的手里有一张纸条，上面写着一个字——"
    "「勿言」"
    "你不记得这是你的名字，还是一个命令。"
    "裂缝的两边，各有微弱的光。"
    "一边是冷蓝色，一边是暖金色。"

    ## 第一个选择：向左或向右
    menu:
        "向左走——冷蓝色的光":
            $ current_city = "left"
            $ tracker.set_flag("first_direction", "left")
            jump chapter1_left

        "向右走——暖金色的光":
            $ current_city = "right"
            $ tracker.set_flag("first_direction", "right")
            jump chapter1_right

## ── 选择结果处理辅助标签 ───────────────────────────────────

label apply_choice:
    ## 根据 last_choice 更新城市状态
    if last_choice == "truth":
        pass  # 真话的后果由具体剧情处理
    elif last_choice == "lie":
        pass  # 假话的后果由具体剧情处理
    elif last_choice == "silent":
        pass  # 沉默的后果由具体剧情处理
    return

## ── 章节开始辅助标签 ───────────────────────────────────────

label chapter_start(chapter_num, cn_name, en_name):
    $ current_chapter = chapter_num
    $ current_chapter_name = cn_name
    $ current_chapter_en = en_name

    scene bg black with dissolve
    $ renpy.pause(0.5)

    ## 章节标题显示
    show text "[cn_name]" at chapter_title_show:
        xalign 0.5 yalign 0.4
    $ renpy.pause(3.0)
    hide text

    return

## ── 章节结束处理 ───────────────────────────────────────────

label chapter_end(chapter_num):
    $ tracker.set_flag("chapter_%d_done" % chapter_num, True)
    $ achievements.check_and_unlock_chapter(chapter_num)

    if chapter_num == 7:
        $ game_completed = True
        jump ending_credits

    return

## ── 结局字幕 ──────────────────────────────────────────────

label ending_credits:
    $ current_city = "narrator"
    $ current_chapter_name = ""
    $ current_chapter_en = ""

    scene bg black with dissolve
    $ renpy.pause(1.0)

    "《镜中城》"
    "感谢游玩。"

    $ alignment = mirror.get_alignment()
    if alignment == "truth_seeker":
        "你选择了真话。"
        "真实的路从不容易，但每一步都踏实。"
    elif alignment == "lie_weaver":
        "你选择了温柔。"
        "善意的语言可以是光，也可以是药。"
    elif alignment == "silent_one":
        "你选择了沉默。"
        "有时候，最有力的语言是不说话。"
    elif alignment == "balanced":
        "你找到了平衡。"
        "真正的智慧，是知道何时诚实，何时温柔。"
    else:
        "你走了一条独特的路。"

    $ renpy.pause(2.0)

    "你的选择统计："
    "真话：[mirror.truth_score]  假话：[mirror.lie_score]  沉默：[mirror.silent_count]"
    "镜像值：[mirror.get_alignment_display()]"

    if achievements.all_memories_collected():
        "你收集了全部记忆碎片。"
        "后日谈已解锁。"

    return
