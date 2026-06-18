## scripts/chapter2.rpy — 第二章：裂
## 砾与瑶的爱情故事，真话与假话的冲突

label chapter2:
    $ current_chapter = 2
    call chapter_start(2, "第二章：裂", "Chapter 2: Crack")

    ## ── 主线：砾与瑶的相遇 ──
    jump ch2_main_line

label ch2_main_line:
    $ current_city = "mirror"
    scene bg mirror_wall_outside with dissolve

    "镜墙前，有两个年轻人隔着镜面对视。"
    "左边是一个拿着石刻诗集的少年。"
    "右边是一个手里握着画笔的女孩。"

    $ npc_rel.meet("li")
    $ npc_rel.meet("yao")

    $ current_city = "left"
    show li normal at left with dissolve
    li "她每天都在那边听我念诗。"
    li "但我念的都是真话——"
    li "真话像刀子。"
    li "我不知道她为什么还愿意听。"

    $ current_city = "right"
    show yao normal at right with dissolve
    yao "他每天都在那边念诗。"
    yao "每一句都像在切开什么。"
    yao "但——"
    yao "每一句里都有温度。"
    yao "只是他自己不知道。"

    ## ── 核心选择：如何帮助砾和瑶 ──
    $ current_city = "mirror"

    $ result = renpy.call_screen("language_wheel",
        truth_text="传达砾的真话——「我喜欢你」——给瑶。",
        lie_text="对瑶说砾想听她的回应，引导她自己说出来。",
        context_text="砾请你帮忙传达一句话。那句话是真话。",
        chapter="ch2", npc="li_yao", scene="relay_message",
        silent_available=True)

    if result == "truth":
        $ npc_rel.adjust("li", 5)
        $ npc_rel.adjust("yao", 3)
        $ city_state.adjust_left(5)
        $ city_state.adjust_right(3)
        $ tracker.set_flag("ch2_relayed_truth")
        jump ch2_truth_path

    elif result == "lie":
        $ npc_rel.adjust("li", 3)
        $ npc_rel.adjust("yao", 5)
        $ tracker.set_flag("ch2_taught_truth")
        jump ch2_lie_path

    elif result == "silent":
        $ npc_rel.adjust("li", 8)
        $ npc_rel.adjust("yao", 8)
        $ tracker.set_flag("ch2_let_them_be")
        jump ch2_silent_path

label ch2_truth_path:
    $ current_city = "left"
    li "谢谢你。"
    "你把砾的话带给了瑶。"

    $ current_city = "right"
    "瑶听到后，嘴唇微微颤抖。"
    yao "我……我没办法说出真话回应。"
    yao "但——"
    "她拿起画笔，画了一幅画。"
    "画里是砾的样子。比真人更真实。"
    yao "告诉他……画里的人，在笑。"

    $ current_city = "narrator"
    "砾看到画后，第一次——流泪了。"
    "不是因为悲伤。"
    "而是因为画里的自己在笑，而他已经忘了怎么笑。"
    jump ch2_end

label ch2_lie_path:
    $ current_city = "right"
    "你没有直接传达砾的话。"
    "而是来到瑶身边，坐在镜墙前。"

    $ current_city = "mirror"
    "你对瑶说——"
    "「你可以试试，说出一句真话。」"
    "「不一定要回应砾。只是——对镜子里的自己说。」"

    $ current_city = "right"
    "瑶犹豫了很久。"
    "然后，她对着镜子里的自己——"
    yao "我……可能真的喜欢他。"
    "她的嘴唇裂开，渗出血丝。"
    "在右城，说真话是有代价的。"
    "但她笑了。一个真实的、不完美的笑。"

    $ current_city = "left"
    "砾听到了。隔着镜墙，他听到了。"
    li "……她说了真话。"
    li "她真的说了真话。"
    $ current_city = "narrator"
    "砾第一次流泪了。"
    jump ch2_end

label ch2_silent_path:
    $ current_city = "mirror"
    "你什么都没做。"
    "你坐在镜墙前，看着他们。"

    "砾开始在镜墙上刻下石头心。"
    "瑶开始在镜墙另一侧画画。"
    "两个人不知道对方在做什么——"
    "但他们的手，隔着镜墙，做着同样的事。"

    "几天后——"
    "石头心和画在裂缝处相遇。"
    "形成了一个完整的图案。"

    $ current_city = "narrator"
    "你看着这个图案。"
    "没有语言。没有翻译。没有桥梁。"
    "只是两个人，在用各自的方式，说着同一句话。"

    $ tracker.set_flag("ch2_mirror_pattern")
    $ tracker.collect_memory("memory_mirror_heart")

    jump ch2_end

label ch2_end:
    $ tracker.set_flag("chapter_2_done")

    $ current_city = "narrator"
    scene bg mirror_crack with dissolve

    "镜墙的裂缝，好像变大了一点。"
    "但也变得更美了。"

    call chapter_end(2)
    jump chapter3
