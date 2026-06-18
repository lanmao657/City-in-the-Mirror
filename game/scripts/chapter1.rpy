## scripts/chapter1.rpy — 第一章：醒
## 左城路线 — 从镜墙裂缝走向左城

label chapter1_left:
    $ current_city = "left"
    call chapter_start(1, "第一章：醒", "Chapter 1: Awake")

    scene bg left_city_entrance with left_city_enter
    $ current_location = "stone_district"

    "空气里有一种奇怪的安静。"
    "不是寂静——而是所有的声音都被削去了圆润的部分，只剩下棱角。"

    ## ── 遇见石匠白岁 ──
    jump ch1_meet_baisui

label ch1_meet_baisui:
    $ npc_rel.meet("baisui")
    show baisui normal at center with dissolve

    $ current_city = "left"
    baisui "你不是这里的人。"

    $ result = renpy.call_screen("language_wheel",
        truth_text="我不知道自己是哪里的人。",
        lie_text="我是从很远的地方来的。",
        context_text="石匠停下手里的刻刀，看着你。",
        chapter="ch1", npc="baisui", scene="first_meet")

    if result == "truth":
        $ npc_rel.adjust("baisui", 5)
        $ city_state.adjust_left(2)
        baisui "真话。但没有温度。"
        baisui "左城的人不欢迎外人。不是因为敌意——"
        baisui "而是因为我们不知道如何跟外人说话。"

    elif result == "lie":
        $ npc_rel.adjust("baisui", -3)
        $ tracker.set_flag("ch1_lied_to_baisui")
        baisui "……你可以说假话。"
        baisui "你是右城的人？"
        "石匠的眼神锐利起来，手不自觉地握紧了刻刀。"

    elif result == "silent":
        $ npc_rel.adjust("baisui", 8)
        $ tracker.set_flag("ch1_silent_to_baisui")
        "你沉默着站在原地。"
        "石匠看着你，过了很久，点了点头。"
        baisui "你选择沉默。聪明。"
        baisui "在左城，沉默是最好的通行证。"
        pause 0.5
        baisui "……但也是一种逃避。"

    ## ── 白岁介绍左城 ──
    scene bg left_city_street with dissolve

    $ current_city = "narrator"
    "白岁带你走进左城的街道。"
    "灰色的建筑棱角分明，像被真话切割过的几何体。"
    "偶尔有人走过，但没有人说话。"
    "他们的嘴唇紧闭，眼神却锐利得像刀。"

    $ current_city = "left"
    baisui "左城的人不说多余的话。"
    baisui "因为每一句真话都有力量——"
    baisui "说「你很孤独」，空气就会凝结冰霜。"
    baisui "说「这件衣服很丑」，衣服就会碎裂。"

    "你低头看自己的灰色长袍，还好——没有人评价它。"

    ## ── 石雕场景 ──
    scene bg left_city_workshop with dissolve

    "白岁的工坊在石之区的深处。"
    "四周摆满了石雕——每一座都是人的脸。"
    "但所有的脸都没有表情。"

    $ current_city = "narrator"
    "你在角落里发现了一座未完成的雕像。"
    "那是一张女人的脸。"
    "嘴角微微上扬——这是一个微笑。"
    "但在左城，微笑是不可能的。"

    $ current_city = "left"
    baisui "……那是我的妻子。"
    baisui "她二十年前去了右城。"
    baisui "再也没有回来。"

    $ result = renpy.call_screen("language_wheel",
        truth_text="你想去找她吗？",
        lie_text="她一定在等你。",
        context_text="白岁看着未完成的雕像，刻刀悬在半空。",
        chapter="ch1", npc="baisui", scene="wife_statue")

    if result == "truth":
        $ npc_rel.adjust("baisui", 3)
        baisui "……想。"
        baisui "但我害怕。"
        baisui "我只会说真话。"
        baisui "我不知道如何对一个听了二十年假话的人说真话。"

    elif result == "lie":
        $ npc_rel.adjust("baisui", -2)
        $ city_state.adjust_left(-1)
        baisui "（长久的沉默）"
        baisui "……你又在说假话了。"
        baisui "你怎么知道她在等我？"
        baisui "你连她是谁都不知道。"

    elif result == "silent":
        $ npc_rel.adjust("baisui", 5)
        "你什么都没说，只是看着那座未完成的雕像。"
        "白岁也沉默了。"
        "工坊里只剩下远处凿石的声音。"

    $ tracker.set_flag("ch1_baisui_done")

    ## ── 通往镜墙 ──
    jump ch1_mirror_encounter

label ch1_mirror_encounter:
    scene bg mirror_wall_outside with dissolve
    $ current_city = "mirror"

    "你来到镜墙前。"
    "镜面光滑如水，倒映着你的样子——但你不知道那是谁。"

    ## 遇见守镜人影
    $ npc_rel.meet("ying")

    $ current_city = "shadow"
    ying "你做了选择。"
    ying "每一个选择，都会改变这条裂缝的形状。"
    ying "但你还不明白——"
    ying "裂缝的形状，就是你的形状。"

    $ tracker.set_flag("ch1_mirror_visited")
    $ tracker.set_flag("chapter_1_done")

    ## 第一章结束
    scene bg mirror_crack with dissolve
    $ current_city = "narrator"

    "你闭上眼睛。"
    "在黑暗中，你看到了一个模糊的画面——"
    "一个孩子，在笑。"
    "你伸手想触碰，但画面碎裂了。"

    "你睁开眼睛。"
    "镜墙在你身后，安静地矗立着。"
    "你还不知道，这面墙是谁建的。"
    "但你已经知道了——"
    "它不该存在。"

    call chapter_end(1)
    jump chapter2
