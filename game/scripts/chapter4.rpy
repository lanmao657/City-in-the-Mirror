## scripts/chapter4.rpy — 第四章：虚
## 右城崩塌，展示"美"的代价

label chapter4:
    $ current_chapter = 4
    call chapter_start(4, "第四章：虚", "Chapter 4: Void")

    show screen city_health_hud

    ## ── 右城崩塌 ──
    $ current_city = "right"
    scene bg right_city_square with dissolve

    "花塔开始摇晃。"
    "右城的一切都建立在假话之上——建筑、花园、甚至空气中的温暖。"
    "当假话的力量衰减，一切都会碎裂。"

    "广场上的人们开始惊慌。他们对花塔说——"
    "「你是世界上最坚固的塔！你永远不会倒！」"
    "假话起了作用——花塔暂时稳住了。"
    "但几秒后，花塔表面出现裂纹。假话的力量在衰减。"

    ## ── 花言登场 ──
    $ npc_rel.meet("huayan")
    show huayan normal at center with dissolve

    huayan "不用担心。我会处理。"
    "花言微笑着说，但这次的微笑有裂缝。"
    "他开始对花塔说更多的假话。每说一句，他的嘴唇就裂开一点。"

    $ current_city = "mirror"
    "花言走到你面前。"
    $ current_city = "right"

    huayan "你。你是那个能说真话的人。"
    "他的嘴唇裂开，流出血——这是他三十年来第一次说真话。"
    huayan "救救它。"

    $ current_city = "narrator"
    "花言的声音不再有微笑的弧度。这是他真实的声音——疲惫的、苍老的、恳求的。"

    ## ── 核心选择：如何拯救右城 ──
    $ current_city = "right"
    $ result = renpy.call_screen("language_wheel",
        truth_text="右城需要学会说真话，即使它会痛。",
        lie_text="让我来帮你说更多的假话，修复这座城市。",
        context_text="花言看着崩塌中的花塔，眼神里有恐惧。一个说了一辈子假话的人，第一次向你求救。",
        chapter="ch4", npc="huayan", scene="save_right_city")

    if result == "truth":
        $ city_state.adjust_right(-5)
        $ city_state.adjust_left(3)
        $ tracker.set_flag("ch4_introduce_truth")

        huayan "你……要摧毁右城的根基？"
        "花言震惊了。但他没有拒绝。"
        huayan "如果这是唯一的路……"

        $ current_city = "narrator"
        "右城开始引入真话。过程是痛苦的——"
        "有人的画碎了，因为画里的人不再是「最美的」。"
        "有人的笑容消失了，因为他们终于承认「我不开心」。"
        "花塔的金色外层开始剥落，露出里面脆弱的纸板。"

        "但——有些建筑开始用石头重建。"
        "比纸板更丑，但更结实。"
        "有人在新建的石墙上刻下了第一句真话：「这座墙不完美，但它是真的。」"

    elif result == "lie":
        $ city_state.adjust_right(5)
        $ tracker.set_flag("ch4_reinforce_lies")

        huayan "（微笑）明智的选择。"
        "你开始帮花言说更多的假话来修复城市。"

        $ current_city = "narrator"
        "花塔稳住了。花园重新绽放。金色的光芒重新笼罩了整个广场。"
        "人们欢呼着。他们对你说——「你是右城的恩人！」"
        "但你知道——这只是暂时的。根基更脆弱了。"

        "花言的笑容完美无瑕。但你注意到，他的眼角，有细微的血丝。"
        "每说一句假话，他都在付出代价。而你，正在加速这个代价。"

    elif result == "silent":
        $ city_state.adjust_right(2)
        $ tracker.set_flag("ch4_third_way")

        $ current_city = "narrator"
        "你什么都没说。"
        "你走到花塔前，用手触摸它的裂缝。"
        "裂缝在你手下缓慢地——不是被假话修补，也不是被真话切除——"
        "而是被时间，一点一点地，接受了。"

        $ current_city = "right"
        huayan "你在做什么？你没有说话。"
        $ current_city = "narrator"
        "你没有回答。但裂缝不再扩大了。"
        "也许有些东西，不需要被修复。只需要被看见。"

        $ tracker.collect_memory("memory_tower_crack")

    ## ── 沉默疗养院支线 ──
    if tracker.get_flag("ch4_third_way"):
        $ current_city = "right"
        scene bg right_city_hospital with dissolve

        "你来到沉默疗养院。明坐在窗边，和之前一样。"
        "但这一次，他转过头看了你一眼。"

        $ current_city = "right"
        show ming normal at center with dissolve

        ming "你没有说话。在花塔前面。"
        ming "（声音很轻）我看到了。"
        ming "也许……不说话，也是一种回答。"

        $ current_city = "narrator"
        "他重新看向窗外。但这一次，他的嘴角微微上扬了一点。"

        $ npc_rel.adjust("ming", 3)
        hide ming with dissolve

    ## ── 第四章结尾 ──
    hide screen city_health_hud
    $ tracker.set_flag("chapter_4_done")

    $ current_city = "narrator"
    scene bg mirror_crack with dissolve
    "右城在变化。缓慢的，痛苦的，但是——真实的变化。"
    "有些东西碎了。但碎裂的地方，光照了进来。"

    call chapter_end(4)
    jump chapter5
