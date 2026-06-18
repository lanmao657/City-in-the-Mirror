## characters.rpy — 角色定义与属性初始化
## 《镜中城》所有角色的 Ren'Py Character 对象和相关属性

## ── 全局状态变量 ────────────────────────────────────────────
## 当前所在城市：left / right / mirror / neutral
default current_city = "mirror"

## 上一次语言轮盘选择：truth / lie / silent / None
default last_choice = None

## 是否显示镜像值提示条
default show_mirror_hint = True

## 游戏进度标记
default game_started = False

## ── 主角 ──────────────────────────────────────────────────
## 勿言 —— 无名无姓，由玩家塑造性格
define w = Character(
    "勿言",
    color="#C0C0C0",
    who_outlines=[(1, "#404040")],
    what_color="#E8E8E8",
)

## ── 旁白 ──────────────────────────────────────────────────
define narrator_voice = Character(
    None,
    what_color="#C0C0C0",
    what_italic=True,
    what_size=26,
)

## ── 守镜人 ────────────────────────────────────────────────
define ying = Character(
    "影",
    color="#E8E8E8",
    who_outlines=[(1, "#606060")],
    what_color="#E8E8E8",
)

## ── 左城角色 ──────────────────────────────────────────────
define baisui = Character(
    "白岁",
    color="#4A90D9",
    who_outlines=[(1, "#1A2A3E")],
    what_color="#B8C4D0",
)

define xiaoxue = Character(
    "小雪",
    color="#8AB4D9",
    who_outlines=[(1, "#2A3A4E")],
    what_color="#D0DCE8",
)

define shiyan = Character(
    "石言",
    color="#3A4A5C",
    who_outlines=[(1, "#1A1A2E")],
    what_color="#A0A8B0",
)

define yan = Character(
    "岩",
    color="#5A7A9C",
    who_outlines=[(1, "#2A3A4E")],
    what_color="#B0C0D0",
)

define li = Character(
    "砾",
    color="#6A8AAC",
    who_outlines=[(1, "#2A3A5E")],
    what_color="#C0D0E0",
)

## ── 右城角色 ──────────────────────────────────────────────
define yunshang = Character(
    "云裳",
    color="#D4A574",
    who_outlines=[(1, "#8B6914")],
    what_color="#FFF8E7",
)

define miyu = Character(
    "蜜语",
    color="#E8B88C",
    who_outlines=[(1, "#A07040")],
    what_color="#FFFDF5",
)

define huayan = Character(
    "花言",
    color="#C49060",
    who_outlines=[(1, "#8B6030")],
    what_color="#FFF0D0",
)

define ming = Character(
    "明",
    color="#B8A080",
    who_outlines=[(1, "#706040")],
    what_color="#F0E8D8",
)

define yao = Character(
    "瑶",
    color="#E0A090",
    who_outlines=[(1, "#A06050")],
    what_color="#FFE8E0",
)

## ── 镜墙角色 ──────────────────────────────────────────────
define hua_child = Character(
    "画",
    color="#A8B8C8",
    who_outlines=[(1, "#607080")],
    what_color="#E8E8E8",
    what_italic=True,
)

## ── NPC 属性数据 ──────────────────────────────────────────
## 每个NPC的状态字典：关系值、是否已相遇、关键标记
default npc_data = {
    "baisui": {
        "name": "白岁",
        "city": "left",
        "relationship": 30,
        "met": False,
        "flags": {},
    },
    "xiaoxue": {
        "name": "小雪",
        "city": "left",
        "relationship": 30,
        "met": False,
        "flags": {},
    },
    "shiyan": {
        "name": "石言",
        "city": "left",
        "relationship": 20,
        "met": False,
        "flags": {},
    },
    "yan": {
        "name": "岩",
        "city": "left",
        "relationship": 30,
        "met": False,
        "flags": {},
    },
    "li": {
        "name": "砾",
        "city": "left",
        "relationship": 30,
        "met": False,
        "flags": {},
    },
    "yunshang": {
        "name": "云裳",
        "city": "right",
        "relationship": 30,
        "met": False,
        "flags": {},
    },
    "miyu": {
        "name": "蜜语",
        "city": "right",
        "relationship": 30,
        "met": False,
        "flags": {},
    },
    "huayan": {
        "name": "花言",
        "city": "right",
        "relationship": 20,
        "met": False,
        "flags": {},
    },
    "ming": {
        "name": "明",
        "city": "right",
        "relationship": 30,
        "met": False,
        "flags": {},
    },
    "yao": {
        "name": "瑶",
        "city": "right",
        "relationship": 30,
        "met": False,
        "flags": {},
    },
    "ying": {
        "name": "影",
        "city": "mirror",
        "relationship": 50,
        "met": False,
        "flags": {},
    },
    "hua_child": {
        "name": "画",
        "city": "mirror",
        "relationship": 50,
        "met": False,
        "flags": {},
    },
}
