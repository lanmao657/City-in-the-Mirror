## scripts/chapter6.rpy — 第六章：合
## 揭示主角的过去，情感高潮

label chapter6:
    $ current_chapter = 6
    call chapter_start(6, "第六章：合", "Chapter 6: Merge")

    ## ── 记忆回涌 ──
    jump ch6_memory_return

label ch6_memory_return:
    $ current_city = "mirror"
    scene bg mirror_inside with dissolve

    "镜墙内部的文字变得越来越多，越来越清晰。"
    "「我的名字是勿言。」"
    "「不，这不是我的名字。这是我对自己的命令。」"
    "「勿言——不要说话。因为我说的每一句话，都会伤害某个人。」"

    scene bg flashback_house with flashback_enter
    $ current_city = "narrator"

    "画面闪回——模糊的、碎片化的记忆。"

    "一个温暖的房间，你在做饭，一个孩子在旁边画画。"
    "「爸爸/妈妈，你看我画的画！」"
    "画里是一栋房子，房子里有两个人在笑。"

    scene bg flashback_rain with flashback_enter

    "雨夜，车里，你在开车。"
    "孩子坐在副驾驶，安全带系着。"
    "「没事的……很近……很快就到……」"

    scene bg flashback_hospital with flashback_enter

    "救护车的声音，红蓝的灯光。"
    "你躺在担架上，意识模糊。"
    "「孩子的情况……」"
    "声音被切断了。"

    scene bg flashback_river with flashback_enter

    "河。一条巨大的、无尽的河。"
    "你站在河边，手里抱着一个孩子的衣服。"
    "你跪在地上，无声地哭。"

    scene bg mirror_inside with flashback_exit

    $ current_city = "mirror"
    "你跪在地上，手在颤抖。"

    $ current_city = "narrator"
    "你想起来了。"
    "不是全部——但够了。"
    "你是这座城市的建造者。"
    "因为你犯了一个错。"
    "一个真话无法挽回的错。"
    "一个假话无法欺骗的错。"
    "所以你把真话和假话分开，造了两座城。"
    "你以为，这样就不会再有人受伤。"
    "但你错了。"

    $ tracker.collect_memory("memory_accident")
    $ tracker.set_flag("ch6_memory_returned")

    ## ── 面对四个"我" ──
    jump ch6_four_selves

label ch6_four_selves:
    scene bg mirror_center with dissolve

    $ current_city = "shadow"
    "四个模糊的身影出现在镜墙中央。"
    "童年勿言（7岁）：「你找到答案了吗？」"
    "少年勿言（16岁）：「你证明了什么？」"
    "成年勿言（30岁）：「你给孩子的是什么？」"
    "崩溃勿言（35岁）：「你让一切结束了吗？」"

    $ result = renpy.call_screen("language_wheel",
        truth_text="我犯了错。我失去了最珍贵的人。我无法原谅自己。",
        lie_text="我已经好了。我不再痛苦了。我找到了答案。",
        context_text="四个「你」同时看着你，等你开口。",
        chapter="ch6", npc="self", scene="four_selves")

    if result == "truth":
        $ tracker.set_flag("ch6_faced_truth")
        "四个「你」沉默了。"
        "成年勿言轻声说——"
        "「但你在镜墙里……等了多久？」"
        "「你不是在等答案。你是在等原谅。」"
        $ tracker.collect_memory("memory_forgiveness")

    elif result == "lie":
        $ tracker.set_flag("ch6_self_deception")
        "四个「你」看着你，然后——"
        "崩溃勿言轻声说——"
        "「你又在说假话了。」"
        "「你骗了自己多少年？」"
        $ current_city = "narrator"
        "镜墙微微震动。它记得你说的每一句假话。"

    elif result == "silent":
        $ tracker.set_flag("ch6_silent_acceptance")
        "你什么都不说，只是看着四个「你」。"
        "画面静止了很久。"
        "童年勿言走近你，伸出手。"
        "「你不想说也没关系。但我们都在这里。你可以哭。」"
        $ tracker.collect_memory("memory_child_hand")

    ## ── 核心记忆：小默 ──
    jump ch6_xiaomo_memory

label ch6_xiaomo_memory:
    scene bg flashback_child_room with flashback_enter

    $ current_city = "narrator"
    "你的孩子——小默，5岁。"
    "孩子在画画，画里是一个人在镜子里。"

    "「爸爸/妈妈，你看！镜子里的人在笑！」"
    "「这是谁？」"
    "「是你呀！你笑的时候，最好看了。」"
    "「爸爸/妈妈，你以后要多笑。你不笑的时候，我会害怕。」"

    scene bg mirror_center with flashback_exit

    $ current_city = "shadow"
    show ying normal at center with dissolve

    ying "小默……一直在河对岸等你。"
    ying "TA没有恨你。TA一直在画画。"
    ying "TA画的每一幅画里……都有你。"
    ying "你造了这座城市，是为了保护别人不再受伤。"
    ying "但你真正想保护的——是不要再有人经历你经历的事。"

    ying "我守了这面墙多久？我不记得了。"
    ying "但我知道——我的存在，就是为了等你准备好。"
    ying "现在你准备好了吗？"

    $ result = renpy.call_screen("language_wheel",
        truth_text="我不知道。但我知道我不能再逃避了。",
        lie_text="我准备好了。",
        context_text="影看着你，半边脸冷峻，半边脸柔和。",
        chapter="ch6", npc="ying", scene="ready_or_not",
        silent_available=True)

    $ tracker.set_flag("ch6_answered_ying")

    ying "好。"
    ying "那么——镜墙必须碎裂。"
    ying "不是因为你打破了它。而是因为它本来就撑不久了。"
    ying "在那之前——你需要做最后一件事。"
    ying "你需要做一次选择。"
    ying "不是为他们——是为你自己。"

    $ tracker.collect_memory("memory_ying_promise")
    $ tracker.set_flag("chapter_6_done")

    $ current_city = "narrator"
    "影化为光点，消散在空气中。"
    "你站在镜墙中央，看着两座城市的轮廓。"
    "该结束了。"

    call chapter_end(6)
    jump chapter7
