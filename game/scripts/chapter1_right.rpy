## scripts/chapter1_right.rpy — 第一章：醒（右城路线）

label chapter1_right:
    $ current_city = "right"
    call chapter_start(1, "第一章：醒", "Chapter 1: Awake")

    scene bg right_city_entrance with right_city_enter
    $ current_location = "paint_district"

    "空气里有一种奇怪的温暖。"
    "不是真正的温暖——而是所有的声音都被加了蜜，"
    "连风声都像在低语赞美。"

    ## ── 遇见画师云裳 ──
    jump ch1_meet_yunshang

label ch1_meet_yunshang:
    $ npc_rel.meet("yunshang")
    show yunshang normal at center with dissolve

    $ current_city = "right"
    yunshang "天哪——你是我见过最好看的人！"
    yunshang "你的眉眼……像是从画里走出来的。"
    yunshang "可以让我为你画一幅肖像吗？"

    $ result = renpy.call_screen("language_wheel",
        truth_text="我不记得自己长什么样，所以无法确认你的话。",
        lie_text="你的画一定很美，我非常期待。",
        context_text="画师看着你，眼睛里有真诚的期待。",
        chapter="ch1", npc="yunshang", scene="first_meet")

    if result == "truth":
        $ npc_rel.adjust("yunshang", 2)
        $ tracker.set_flag("ch1_truth_to_yunshang")
        yunshang "不记得……没关系。"
        yunshang "在我的画里，你会比你想象的更美。"
        "她轻声对自己说——"
        yunshang "有时候，画里的真实比现实的真实……更值得存在。"

    elif result == "lie":
        $ npc_rel.adjust("yunshang", 5)
        $ city_state.adjust_right(2)
        yunshang "真的吗？你真的期待吗？"
        "她的眼睛亮起来，开始快速调色。"
        yunshang "我一定会画出你最美的样子！"

    elif result == "silent":
        $ npc_rel.adjust("yunshang", 8)
        "你什么都没说，只是微微点了点头。"
        "云裳看着你，过了好一会儿。"
        yunshang "你……不说话？"
        "这次她的微笑不太一样——更安静，更真实。"
        yunshang "没关系。有些人用眼神说话。"
        yunshang "你的眼睛……在说很多话。"

    ## ── 云裳为你画像 ──
    scene bg right_city_studio with dissolve

    "云裳的画室在绘梦区的最高处。"
    "四面墙上挂满了肖像——每一幅里的人都在微笑。"
    "但仔细看，这些微笑都太过完美。"
    "完美到不像真的。"

    $ current_city = "right"
    yunshang "我画了无数人的肖像。"
    yunshang "但——"
    "她的声音低了下来。"
    yunshang "我从未画过自己。"

    $ result = renpy.call_screen("language_wheel",
        truth_text="因为你不知道自己的真实长什么样？",
        lie_text="你太美了，画不出比你本人更美的画。",
        context_text="云裳站在一幅空白画布前，手里拿着画笔。",
        chapter="ch1", npc="yunshang", scene="self_portrait")

    if result == "truth":
        $ npc_rel.adjust("yunshang", 3)
        "云裳的手微微颤抖了一下。"
        yunshang "……你说得对。"
        yunshang "我不知道。"
        yunshang "在右城，我们只知道如何美化一切。"
        yunshang "但「真实」……那个词，我已经很久没听过了。"

    elif result == "lie":
        $ npc_rel.adjust("yunshang", 2)
        $ city_state.adjust_right(1)
        yunshang "（微笑）谢谢你。"
        "但她的微笑没有到达眼睛。"

    elif result == "silent":
        $ npc_rel.adjust("yunshang", 6)
        "你走到空白画布前，和她一起看着。"
        "画布上什么都没有。"
        "但你们一起看了很久。"
        yunshang "（轻声）也许……空白也是一种真实。"

    $ tracker.set_flag("ch1_yunshang_done")

    ## ── 通往镜墙 ──
    jump ch1_mirror_encounter_right

label ch1_mirror_encounter_right:
    scene bg mirror_wall_outside with dissolve
    $ current_city = "mirror"

    "你来到镜墙前。"
    "镜面光滑如水，倒映着你的样子——但你不知道那是谁。"

    $ npc_rel.meet("ying")

    $ current_city = "shadow"
    ying "你做了选择。"
    ying "每一个选择，都会改变这条裂缝的形状。"
    ying "但你还不明白——"
    ying "裂缝的形状，就是你的形状。"

    $ tracker.set_flag("ch1_mirror_visited")
    $ tracker.set_flag("chapter_1_done")

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
