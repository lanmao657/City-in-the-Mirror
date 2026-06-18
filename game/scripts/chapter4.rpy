## scripts/chapter4.rpy — 第四章：虚
## 右城崩塌，展示"美"的代价

label chapter4:
    $ current_chapter = 4
    call chapter_start(4, "第四章：虚", "Chapter 4: Void")

    show screen city_health_hud

    $ current_city = "right"
    scene bg right_city_square with dissolve

    "花塔开始摇晃。"
    "右城的一切都建立在假话之上——建筑、花园、甚至空气中的温暖。"
    "当假话的力量衰减，一切都会碎裂。"

    $ npc_rel.meet("huayan")
    show huayan normal at center with dissolve

    $ current_city = "right"
    huayan "不用担心。我会处理。"
    "花言微笑着说，但这次的微笑有裂缝。"

    $ current_city = "mirror"
    "花言走到你面前。"
    $ current_city = "right"
    huayan "你。你是那个能说真话的人。"
    "他的嘴唇裂开，流出血——这是他三十年来第一次说真话。"
    huayan "救救它。"

    ## ── 核心选择：如何拯救右城 ──
    $ result = renpy.call_screen("language_wheel",
        truth_text="右城需要学会说真话，即使它会痛。",
        lie_text="让我来帮你说更多的假话，修复这座城市。",
        context_text="花言看着崩塌中的花塔，眼神里有恐惧。",
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
        "有人的画碎了，有人的笑容消失了。"
        "但——有些建筑开始用石头重建。"
        "比纸板更丑，但更结实。"

    elif result == "lie":
        $ city_state.adjust_right(5)
        $ tracker.set_flag("ch4_reinforce_lies")
        huayan "（微笑）明智的选择。"
        "你开始帮花言说更多的假话来修复城市。"
        $ current_city = "narrator"
        "花塔稳住了。花园重新绽放。"
        "但你知道——这只是暂时的。"
        "根基更脆弱了。"

    elif result == "silent":
        $ city_state.adjust_right(2)
        $ tracker.set_flag("ch4_third_way")
        $ current_city = "narrator"
        "你什么都没说。"
        "你走到花塔前，用手触摸它的裂缝。"
        "裂缝在你手下缓慢地——不是被假话修补，也不是被真话切除——"
        "而是被时间，一点一点地，接受了。"
        $ tracker.collect_memory("memory_tower_crack")

    hide screen city_health_hud
    $ tracker.set_flag("chapter_4_done")

    $ current_city = "narrator"
    scene bg mirror_crack with dissolve
    "右城在变化。缓慢的，痛苦的，但是——真实的变化。"

    call chapter_end(4)
    jump chapter5
