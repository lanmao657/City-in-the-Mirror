## scripts/epilogue.rpy — 后日谈：归家
## 触发条件：任意结局 + 全部记忆碎片收集

label epilogue:
    $ current_city = "narrator"
    scene bg black with dissolve
    $ renpy.pause(1.0)

    "—— 后日谈 · 归家 ——"

    scene bg river with dissolve
    $ current_bgm = "bgm_ending"

    "一条河。安静的、无尽的河。"
    "你站在河边。"

    "一个小小的身影从远处跑来。"

    $ current_city = "narrator"

    "「爸爸/妈妈！」"
    "「你来了！我等了你好久！」"
    "「你看！我画了好多画！」"

    "你接过画。"
    "画里是镜中城——但已经不是两半了。"
    "画里有石匠在微笑，有画师在画真实的画。"
    "有砾和瑶在一起，有蜜语和明在一起。"
    "画面中央，是你——在笑。"

    "小默抬头看着你，眼睛亮亮的。"

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
