## scripts/chapter7.rpy — 第七章：渡
## 最终选择，多结局

label chapter7:
    $ current_chapter = 7
    call chapter_start(7, "第七章：渡", "Chapter 7: Ferry")

    ## ── 镜墙碎裂 ──
    jump ch7_mirror_shatters

label ch7_mirror_shatters:
    $ current_city = "mirror"
    scene bg mirror_wall_outside with dissolve

    "两座城市的居民都聚集在镜墙的两侧。"

    $ current_city = "left"
    show shiyan normal at left with dissolve
    shiyan "镜墙碎了……我们的真话会涌过去。"
    shiyan "准备好——这是战争。"

    $ current_city = "right"
    show huayan normal at right with dissolve
    huayan "镜墙碎了……不要害怕。"
    huayan "我们会用赞美保护自己。"

    $ current_city = "mirror"
    "镜墙碎裂——不是碎片飞散，而是像水一样融化。"
    "两座城市的人第一次看到彼此。"

    scene bg city_merge_chaos with dissolve

    $ current_city = "narrator"
    "混乱开始。"
    "左城居民喊——「你们都是骗子！你们的一切都是假的！」"
    "右城居民喊——「你们才是怪物！你们只会伤害人！」"

    $ current_city = "shadow"
    "影已经变得半透明。"
    ying "去吧。这是你的城市。这是你的选择。"
    ying "无论你选什么……我都会为你骄傲。"
    "影化为光点，消散了。"

    $ tracker.set_flag("ying_departed")

    ## ── 最终选择 ──
    jump ch7_final_choice

label ch7_final_choice:
    $ current_city = "mirror"
    scene bg city_merge_center with dissolve

    "你站在两座城市的交汇处。"
    "所有人都在看着你。"

    menu:
        "对所有人说真话":
            $ mirror.add_choice("truth", "ch7", "all", "final")
            $ tracker.set_flag("ending_truth")
            jump ending_truth

        "对所有人说假话":
            $ mirror.add_choice("lie", "ch7", "all", "final")
            $ tracker.set_flag("ending_lie")
            jump ending_lie

        "对左城说真话，对右城说假话":
            $ mirror.add_choice("truth", "ch7", "left", "final_split")
            $ mirror.add_choice("lie", "ch7", "right", "final_split")
            $ tracker.set_flag("ending_split")
            jump ending_split

        "沉默":
            $ mirror.add_choice("silent", "ch7", "all", "final")
            $ tracker.set_flag("ending_silent")
            jump ending_silent

## ═══════════════════════════════════════════════════════════
## 结局 A：真话
## ═══════════════════════════════════════════════════════════

label ending_truth:
    $ current_city = "mirror"
    "你深呼吸，然后——"

    "「这座城市是我的错。」"
    "「我把你们劈成两半，是因为我害怕。」"
    "「我害怕真话，也害怕假话。」"
    "「我以为把它们分开，就不会再有人受伤。」"
    "「但我错了。」"
    "「真话和假话，不是敌人。它们是同一枚硬币的两面。」"
    "「镜墙碎了，你们会重新学会两种语言。」"
    "「过程会很痛。但这是唯一的路。」"
    "「我不会再逃避了。」"

    scene bg ending_truth with dissolve
    $ current_city = "narrator"
    "一年后。"
    "两座城市合并了。过程比想象中更痛苦。"
    "但城市在重建。不完美，但真实。"
    $ tracker.collect_memory("memory_ending_truth")
    call chapter_end(7)
    jump ending_credits

## ═══════════════════════════════════════════════════════════
## 结局 B：假话
## ═══════════════════════════════════════════════════════════

label ending_lie:
    $ current_city = "mirror"
    "你微笑着说——"

    "「不要害怕。」"
    "「镜墙碎了，但一切都好。」"
    "「你们会发现，彼此其实没有那么不同。」"
    "「一切都会好起来的。」"

    scene bg ending_lie with dissolve
    $ current_city = "narrator"
    "一年后。"
    "两座城市表面上和平了。"
    "但你知道——和平建立在一句假话之上。"
    "这句假话，能撑多久？"
    $ tracker.collect_memory("memory_ending_lie")
    call chapter_end(7)
    jump ending_credits

## ═══════════════════════════════════════════════════════════
## 结局 C：分别说话
## ═══════════════════════════════════════════════════════════

label ending_split:
    $ current_city = "mirror"

    "你转向左城——"
    "「你们需要学会温柔。真话不需要是刀子。真话可以是沉默，是陪伴，是一个孩子画的画。」"
    "「但沉默不是因为害怕。沉默是因为——有些话，需要先用心去感受。」"

    "你转向右城——"
    "「你们需要学会诚实。假话不是毒药。假话可以是温柔，是善意，是一个人深夜的陪伴。」"
    "「但温柔不是欺骗。温柔是——知道真相之后，依然选择善良。」"

    scene bg ending_split with dissolve
    $ current_city = "narrator"
    "一年后。"
    "左城和右城的边界开始模糊。"
    "石匠白岁尝试了「圆角」的雕刻。"
    "画师云裳画了一幅真实的肖像。"
    "砾和瑶终于在一起了。"
    $ tracker.collect_memory("memory_ending_split")
    call chapter_end(7)
    jump ending_credits

## ═══════════════════════════════════════════════════════════
## 结局 D：沉默
## ═══════════════════════════════════════════════════════════

label ending_silent:
    $ current_city = "mirror"
    "你什么都不说。"
    "只是站在两城之间。"
    "闭上眼睛。"

    "然后——"
    "小默的画从你口袋里飘出来。"
    "画落在地上。"
    "画里是——一个人站在镜子前，镜子里的人在笑。"
    "画的背面写着一行字——小默的笔迹："

    "「爸爸/妈妈，笑一个。」"

    "所有人看到这幅画。"
    "左城的人看到：画里的笑是真实的。"
    "右城的人看到：画里的笑是温暖的。"
    "两城的人第一次——同时笑了。"

    scene bg ending_silent with dissolve
    $ current_city = "narrator"
    "沉默不是逃避。"
    "沉默是——给彼此空间，让心自己说话。"

    $ tracker.collect_memory("memory_ending_silent")

    ## 检查是否可解锁后日谈
    if achievements.all_memories_collected():
        jump epilogue

    call chapter_end(7)
    jump ending_credits

## ═══════════════════════════════════════════════════════════
## 后日谈：归家
## ═══════════════════════════════════════════════════════════

label epilogue:
    $ current_city = "narrator"
    scene bg black with dissolve
    $ renpy.pause(1.0)

    "—— 后日谈 · 归家 ——"

    scene bg river with dissolve

    "一条河。安静的、无尽的河。"
    "你站在河边。"

    "一个小小的身影从远处跑来。"

    "「爸爸/妈妈！」"
    "「你来了！我等了你好久！」"
    "「你看！我画了好多画！」"

    "你接过画。"
    "画里是镜中城——但已经不是两半了。"
    "画里有石匠在微笑，有画师在画真实的画。"
    "有砾和瑶在一起，有蜜语和明在一起。"
    "画面中央，是你——在笑。"

    "「爸爸/妈妈。你以后不用再道歉了。」"
    "「因为你已经——把一切都修好了。」"

    scene bg river_sunset with dissolve

    "这是一条无尽的河。"
    "河的此岸是过去，彼岸是未来。"
    "你站在中间。"
    "不逃避过去，不恐惧未来。"
    "只是——在这里。"
    "和你最重要的人，一起看河水流动。"

    $ achievements.unlock("epilogue")

    call chapter_end(7)
    jump ending_credits
