## scripts/chapter3.rpy — 第三章：镜
## 镜墙的秘密，理解真话与假话背后可能藏着同一种善意

label chapter3:
    $ current_chapter = 3
    call chapter_start(3, "第三章：镜", "Chapter 3: Mirror")

    ## ── 主线：医生岩的镜像 ──
    jump ch3_doctor_yan

label ch3_doctor_yan:
    $ current_city = "mirror"
    scene bg mirror_wall_outside with dissolve

    "你发现一个左城的男人站在镜墙前，盯着镜子里的自己。"

    $ npc_rel.meet("yan")
    $ current_city = "left"
    show yan normal at center with dissolve

    yan "镜子里的我……在笑。"
    yan "我不会笑。我忘了怎么笑。"
    yan "上一次笑是什么时候……我不记得了。"
    yan "你说，镜子里的是我吗？"

    $ result = renpy.call_screen("language_wheel",
        truth_text="镜子里的你，可能是你遗忘的那一部分。",
        lie_text="镜子里的你，看起来很幸福。",
        context_text="岩盯着镜子里微笑着的自己。",
        chapter="ch3", npc="yan", scene="mirror_self")

    if result == "truth":
        $ npc_rel.adjust("yan", 5)
        $ tracker.set_flag("ch3_yan_truth")
        "岩沉默了很久。"
        yan "遗忘的……部分。"
        "他的手不自觉地摸向嘴角。"
        yan "我遗忘的，不是笑的方法。"
        yan "我遗忘的，是笑的理由。"
        $ tracker.collect_memory("memory_yan_smile")

    elif result == "lie":
        $ npc_rel.adjust("yan", 3)
        yan "幸福？"
        yan "（看着镜子里的自己）"
        yan "也许吧。也许镜子里的我确实幸福。"
        yan "但我不是镜子里的我。"

    elif result == "silent":
        $ npc_rel.adjust("yan", 8)
        "你和岩一起看了很久的镜子。"
        "镜子里的岩在笑，镜墙外的岩在沉默。"
        "两个「岩」之间的距离，就是左城和右城的距离。"
        yan "（突然，轻声）她临终的时候……对我说了一句话。"
        yan "她说「岩，不要忘记笑」。"
        $ tracker.collect_memory("memory_yan_wife")

    ## ── 主线：蜜语的丈夫明 ──
    jump ch3_meet_ming

label ch3_meet_ming:
    $ current_city = "mirror"
    scene bg right_city_hospital with dissolve
    $ current_city = "right"

    "右城的「沉默疗养院」——"
    "关押那些不再能说假话的人的地方。"

    $ npc_rel.meet("miyu")
    $ npc_rel.meet("ming")

    show miyu normal at left with dissolve
    miyu "他已经在这里三年了。"
    "她的声音依然温柔，但这次，温柔里有裂缝。"
    miyu "我每天来看他，对他说「你会好起来的」。"
    miyu "他……什么都不说。"

    $ current_city = "mirror"
    "你走进明的房间。"

    $ current_city = "right"
    show ming normal at right with dissolve
    "明坐在窗边，看着窗外。"

    $ result = renpy.call_screen("language_wheel",
        truth_text="你为什么不说话了？",
        lie_text="你的妻子很想你。",
        context_text="明看了你一眼，然后继续看窗外。",
        chapter="ch3", npc="ming", scene="sanatorium")

    if result == "truth":
        $ npc_rel.adjust("ming", 5)
        $ tracker.set_flag("ch3_ming_truth")
        "明苦笑。"
        ming "我说了三十年的假话。"
        ming "三十年。每一句都是谎言。"
        ming "「你今天真美」——不好看的时候。"
        ming "「我们的生活很好」——快破产的时候。"
        ming "「我很幸福」——每天晚上都在哭的时候。"
        ming "你知道最可怕的是什么吗？"
        ming "不是谎言本身——"
        ming "而是我说了三十年之后，我已经分不清哪些是真话、哪些是假话了。"
        $ tracker.collect_memory("memory_ming_truth")

    elif result == "lie":
        $ npc_rel.adjust("ming", 2)
        $ city_state.adjust_right(2)
        "明听到「你的妻子很想你」后，微微动了一下。"
        ming "……她？"
        ming "她每天来。每天说同样的话。"
        ming "「你会好起来的」。"
        ming "（声音很轻）也许她是对的。也许我会好。"
        ming "但——我分不清。"

    elif result == "silent":
        $ npc_rel.adjust("ming", 8)
        "你坐在明的身边，和他一起看窗外。"
        "窗外是右城的花海——假话催开的花。"
        "你们坐了很久。"
        "明看了你一眼。"
        ming "你是第一个不试图「治愈」我的人。"
        ming "（声音里有一丝温度）谢谢你。"

    ## ── 第三章结尾：发现镜墙文字 ──
    jump ch3_discovery

label ch3_discovery:
    $ current_city = "mirror"
    scene bg mirror_inside with dissolve

    "你深入镜墙内部，发现墙壁上刻着文字。"
    "「我把这座城市劈成两半。」"
    "「不是因为我相信分离是对的。」"
    "「而是因为我已经不知道如何让它们在一起。」"

    $ current_city = "shadow"
    $ npc_rel.meet("ying")
    show ying normal at center with dissolve

    ying "你想起来了吗？"
    ying "不，你还不到想起来的时候。"
    ying "但你应该知道——"
    ying "这面墙，不是惩罚，是逃避。"
    ying "造墙的人以为，把刀和药分开，就不会有人受伤。"
    ying "但没有刀，就无法切除腐烂。没有药，就无法治愈伤口。"
    ying "你，迟早要面对——刀和药，本来就是同一种东西。"

    $ tracker.set_flag("ch3_mirror_truth_revealed")
    $ tracker.set_flag("chapter_3_done")
    $ tracker.collect_memory("memory_mirror_text")

    $ current_city = "narrator"
    scene bg mirror_crack with dissolve
    "刀和药，本来就是同一种东西。"
    "这句话在你心里回响了很久。"

    call chapter_end(3)
    jump chapter4
