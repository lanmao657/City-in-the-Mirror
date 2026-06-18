## scripts/chapter5.rpy — 第五章：真
## 左城的规则侵蚀，展示"真"的代价

label chapter5:
    $ current_chapter = 5
    call chapter_start(5, "第五章：真", "Chapter 5: Truth")

    show screen city_health_hud

    $ current_city = "left"
    scene bg left_city_garden with dissolve

    "左城的真话规则，正在侵蚀最基本的人际关系。"

    ## ── 母亲与孩子 ──
    "你看到一个母亲和孩子在花园里。"
    "孩子吃了一口母亲做的饭。"

    "孩子的嘴唇颤抖了——左城的规则让他说出真话——"
    "「妈妈，这个饭真的很难吃。」"
    "母亲的手冻伤了。"

    $ result = renpy.call_screen("language_wheel",
        truth_text="你做的饭确实不好吃，但你做的爱是最好的。",
        lie_text="别担心，下次会好的。",
        context_text="母亲看着冻伤的手，孩子的眼泪流下来。",
        chapter="ch5", npc="mother", scene="garden")

    if result == "truth":
        $ city_state.adjust_left(3)
        $ tracker.set_flag("ch5_mother_truth")
        "母亲愣住，然后轻声笑了一下。"
        "「爱……是最好的吗？」"
        "手上的冰霜开始融化——真话的治愈力量，当它触动了真实的情感。"

    elif result == "lie":
        $ tracker.set_flag("ch5_mother_lie")
        "母亲看着你，震惊。"
        "「你……你可以说假话？」"
        "恐惧——但随即，她摸了摸孩子冻伤的手。"
        "「假话……原来可以说得这么温柔。」"

    elif result == "silent":
        $ npc_rel.adjust("xiaoxue", 3)
        "你蹲下来，帮母亲包扎冻伤的手。"
        "孩子也蹲下来，帮母亲吹手。"
        "三个人在花园里，不说一句话。"
        "但画面里有一种安静的温暖。"
        $ tracker.collect_memory("memory_mother_silence")

    ## ── 哲学家的演讲 ──
    $ current_city = "narrator"
    scene bg left_city_square with dissolve

    "刻痕广场上，一个左城哲学家在演讲。"

    "「我们把真话当作武器。用它切割一切。」"
    "「但武器会伤人。」"
    "「我用真话伤害了我爱的人。」"
    "「我需要的，不是更多的真话——而是学会如何温柔地说真话！」"

    $ current_city = "left"
    show shiyan normal at center with dissolve
    "石言长老出现了。"
    shiyan "你在动摇左城的根基。"
    shiyan "真话不需要温柔。真话就是真话。"

    $ result = renpy.call_screen("language_wheel",
        truth_text="你的沉默，比你说过的任何真话都更伤人。",
        lie_text="你说得很好，左城需要你的声音。",
        context_text="石言长老正要转身离开。",
        chapter="ch5", npc="shiyan", scene="philosopher_speech")

    if result == "truth":
        $ npc_rel.adjust("shiyan", -5)
        $ tracker.set_flag("ch5_confronted_shiyan")
        "石言停下脚步。"
        "他的背影微微颤抖。"
        "但他没有回头。"
        $ current_city = "narrator"
        "有些真话，需要时间才能到达。"

    elif result == "lie":
        $ tracker.set_flag("ch5_supported_philosopher")
        "哲学家看了你一眼，微微点头。"
        "「谢谢你。」"

    elif result == "silent":
        "你看着石言的背影，什么都没说。"
        "石言走远了。"
        "广场上的人群沉默了很久。"
        $ tracker.collect_memory("memory_shiyan_back")

    hide screen city_health_hud
    $ tracker.set_flag("chapter_5_done")

    $ current_city = "narrator"
    scene bg mirror_crack with dissolve
    "左城在裂开。但裂开的地方，光照了进来。"

    call chapter_end(5)
    jump chapter6
