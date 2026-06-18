# 《镜中城》AI 美术素材生成 Prompt

> 本文档提供所有美术素材的 AI 生成提示词。
> 适用于 Midjourney / Stable Diffusion / ComfyUI / DALL-E 等工具。
> 建议分辨率：背景 1920×1080，立绘 800×1200（透明底），UI 元素按需裁切。

---

## 一、统一画风基底（所有 Prompt 共用）

每次生成时，在 prompt 末尾追加以下风格后缀：

```
style: Chinese ink wash painting meets modern concept art,
muted watercolor palette, soft atmospheric lighting,
cinematic composition, delicate brushstrokes,
subtle grain texture, melancholic beauty --ar 16:9 --s 750
```

> Midjourney 用户可直接追加 `--ar 16:9 --s 750 --style raw`
> SD 用户可搭配 LoRA：`ink_wash_painting` 或 `chinese_watercolor`

---

## 二、背景场景 Prompt

### ── 通用负面提示词 ──

```
Negative: text, watermark, signature, UI, HUD, HUD elements,
letters, words, blurry, low quality, jpeg artifacts,
photorealistic, 3D render, anime, cartoon, chibi,
bright saturated colors, neon, cyberpunk
```

---

### 2.1 序章 · 镜墙裂缝

**mirror_crack.jpg** — 序章开场

```
A vast dark chasm seen from inside, walls made of shattered mirror
fragments reflecting faint silvery light. The crack is narrow,
person-sized, with the left side emitting cold blue light and the
right side emitting warm golden light. A small piece of paper
fluttering in the wind. Mysterious, melancholic atmosphere.
Dark background, ethereal glow at center.
Chinese ink wash style, muted tones, cinematic.
--ar 16:9
```

**mirror_wall_outside.jpg** — 镜墙外景

```
An enormous mirror wall stretching from earth to sky, dividing
a valley city in half. The left half has angular grey stone
buildings in cold blue tones. The right half has flowing golden
structures in warm amber tones. The mirror surface is perfectly
smooth, reflecting distorted versions of both sides. A single
crack runs down the center. Twilight sky, dramatic lighting.
Wide establishing shot. Chinese ink wash concept art.
--ar 16:9
```

**mirror_inside.jpg** — 镜墙内部

```
Inside a vast mirror wall, silvery translucent walls covered in
faintly glowing engraved text in an unknown language. The text
seems to float just above the surface. Reflections multiply
infinitely. A narrow path of light runs through the center.
Ethereal, sacred atmosphere. Cool silver and deep indigo tones.
Chinese ink wash style, atmospheric perspective.
--ar 16:9
```

**mirror_center.jpg** — 镜墙中央（最终选择地）

```
The center of a mirror wall, where four ghostly translucent
figures stand facing the viewer. The figures represent the same
person at different ages: child, teenager, adult, and broken adult.
Behind them, a vast mirror surface cracks and glows. Rays of
light pour through the cracks. Dramatic, emotional scene.
Chinese ink wash painting, silver and pale gold tones.
--ar 16:9
```

---

### 2.2 左城 · 言真之地

**left_city_entrance.jpg** — 左城入口

```
Entrance to a city of grey stone buildings with sharp angular
architecture. Everything has been carved and cut into geometric
shapes. Narrow windows, tall walls, no curves. The sky is overcast
in cold blue-grey. Stone pathways with sharp edges. A few silent
figures walk with heads down. Cold, austere atmosphere.
Blue-grey color palette with touches of rust red.
Chinese ink wash style, dramatic shadows.
--ar 16:9
```

**left_city_street.jpg** — 左城街道

```
A street in a grey stone city where all buildings have sharp
angular edges as if cut by blades. Narrow alley between tall
stone walls. Hard shadows on cobblestone ground. A single bare
tree with angular branches. Occasional frost crystals float in
the air. Cold blue-grey lighting. No decorations, no flowers,
no warmth. Austere beauty. Chinese ink wash concept art.
--ar 16:9
```

**left_city_workshop.jpg** — 白岁工坊

```
Interior of a stone sculptor's workshop. Grey stone walls, a
wooden workbench covered in stone dust. Multiple unfinished stone
busts on shelves — all with expressionless faces. One bust in the
corner is different: a woman's face with the faintest hint of a
smile, half-completed. Chisel marks visible on every surface.
A single shaft of cold blue light from a narrow window.
Chinese ink wash style, chiaroscuro lighting.
--ar 16:9
```

**left_city_garden.jpg** — 静默花园

```
A stark garden in a grey stone city. Thorny shrubs and needle-leaf
plants grow between angular stone benches. Frost crystals cling to
everything. A mother and child sit on a bench — the mother's hand
is covered in ice crystals. A single leaf falls. Quiet, sorrowful
atmosphere. Cold blue-grey palette with hints of deep red.
Chinese ink wash painting, minimal composition.
--ar 16:9
```

**left_city_square.jpg** — 刻痕广场

```
A large stone square in an angular grey city. The ground is covered
in carved lines and text — thousands of inscriptions from generations
of truthful speech. A stone platform stands at center where a
philosopher addresses a silent crowd. The crowd's faces are sharp
and serious. Cold overhead light. Monumental, solemn atmosphere.
Blue-grey palette, dramatic perspective from below.
Chinese ink wash concept art.
--ar 16:9
```

---

### 2.3 右城 · 言美之地

**right_city_entrance.jpg** — 右城入口

```
Entrance to a city of flowing golden architecture. Buildings curve
and spiral like ribbons, made of silk and paper that shimmer.
Flower petals drift through warm amber air. Everything is adorned
with golden ornaments and soft fabrics. A wide welcoming gate
draped in warm-toned silk. Warm, inviting, but slightly artificial
atmosphere. Golden amber and rose palette.
Chinese ink wash style with warm watercolor washes.
--ar 16:9
```

**right_city_studio.jpg** — 云裳画室

```
Interior of a painter's studio at the top of a golden tower. Walls
covered in beautiful portrait paintings — every subject is smiling
perfectly, almost too perfectly. Easels with half-finished paintings.
Warm golden light from arched windows. Silk curtains billow gently.
A blank canvas stands in the center, pristine and untouched.
Warm amber and cream palette. Chinese ink wash style, soft lighting.
--ar 16:9
```

**right_city_square.jpg** — 花语广场

```
A magnificent square in a golden city. Ornate towers spiral upward,
covered in flowering vines. People in colorful robes exchange
compliments — flower petals appear in the air with each kind word.
Fountains of golden liquid. Beautiful but fragile — close inspection
reveals paper-thin walls and painted-on details. Warm golden light.
Chinese ink wash painting, rich warm palette.
--ar 16:9
```

**right_city_hospital.jpg** — 沉默疗养院

```
A quiet building in a golden city, but this one is different — its
colors are faded, its decorations are peeling. Inside, people sit
in silence, staring out windows. The warm golden light feels muted
here. A single window shows the bustling golden city outside, but
the room itself is still and grey. Melancholic contrast between
inside and outside. Chinese ink wash style, bittersweet tone.
--ar 16:9
```

**smile_garden.jpg** — 永笑花园

```
A garden in a golden city where every flower blooms permanently.
Artificial flowers made of light and words, maintained by constant
praise. Beautiful from a distance but fragile up close — some
flowers flicker like dying candles. A bench under a flowering tree
where a woman waits alone. Warm gold and pink palette with areas
of fading. Chinese ink wash style, dreamy yet fragile atmosphere.
--ar 16:9
```

---

### 2.4 闪回场景

**flashback_house.jpg** — 温暖的家（闪回）

```
A warm, cozy home interior bathed in golden evening light. A parent
cooks in the kitchen while a small child (age 5) draws at a table.
The child's drawing shows a house with two smiling figures. Warm
domestic scene, nostalgic and tender. Soft focus, warm amber tones
with a slight dreamlike haze. The edges of the image blur like a
fading memory. Chinese ink wash style, sentimental warmth.
--ar 16:9
```

**flashback_rain.jpg** — 雨夜车祸（闪回）

```
A rain-soaked night road seen through a car windshield. Wipers
creating arcs on the glass. Headlights reflecting on wet asphalt.
A child's car seat visible in the passenger side. Rain streaks
blur the world outside. Tension and dread in the atmosphere.
Dark blue and grey palette with harsh headlight glare.
Chinese ink wash style, dramatic noir lighting.
--ar 16:9
```

**flashback_hospital.jpg** — 医院（闪回）

```
A hospital corridor in harsh fluorescent light. Red and blue
emergency lights flashing through windows. A gurney is rushed
down the hallway — motion blur. Medical staff in the background.
The perspective is low, as if seen from someone lying down.
Cold white and clinical green with flashing red-blue accents.
Chinese ink wash style, urgent and disorienting.
--ar 16:9
```

**flashback_river.jpg** — 冥河（闪回）

```
An infinite dark river under a starless sky. The water is perfectly
still, reflecting nothing. A lone figure kneels at the water's
edge, clutching a child's garment. The river stretches to the
horizon in both directions. Utterly silent and vast. Deep indigo
and black palette with a faint silvery shimmer on the water.
Chinese ink wash style, existential emptiness.
--ar 16:9
```

**flashback_child_room.jpg** — 小默的房间（闪回）

```
A child's room with drawings covering every wall. Crayon drawings
of houses, families, and a figure standing in front of a mirror
that reflects someone smiling. A small desk with crayons scattered
across it. Warm afternoon light through a window. A child's laughter
seems to echo. Nostalgic, tender, slightly sad — like visiting a
room that no one lives in anymore. Warm amber and soft pastels.
Chinese ink wash style, bittersweet memory.
--ar 16:9
```

---

### 2.5 结局场景

**city_merge_chaos.jpg** — 城市融合混乱

```
Two cities colliding — angular grey stone buildings merging with
flowing golden structures. The boundary between them cracks and
shatters. People from both sides face each other in confusion
and anger. Debris floats in the air — stone fragments and flower
petals mixed together. Dramatic sky split between cold blue and
warm gold. Chaotic, tense energy. Chinese ink wash concept art,
dynamic composition.
--ar 16:9
```

**city_merge_center.jpg** — 融合中心

```
The center point where two cities merge. A single figure stands
at the convergence, facing the viewer. On the left, angular grey
buildings. On the right, flowing golden structures. The ground
beneath the figure shows both stone and silk textures blending.
All the people of both cities watch from behind. A moment of
suspended tension before resolution. Cinematic, epic scale.
Chinese ink wash style, dramatic central composition.
--ar 16:9
```

**ending_truth.jpg** — 结局A（真话）

```
A city one year after reconstruction. New buildings mix angular
stone foundations with warm golden decorations. Imperfect but real.
People walk the streets — some still awkward with new emotions.
A sunrise breaks through clouds, casting long honest shadows.
Hopeful but realistic atmosphere. Muted warm and cool tones
finding balance. Chinese ink wash style, dawn of a new era.
--ar 16:9
```

**ending_lie.jpg** — 结局B（假话）

```
A golden city that looks perfect from a distance, but close up
the buildings are paper-thin, the flowers are fading. A figure
sits at the mirror wall fragments, looking at a child's drawing
that still shows someone smiling. The golden light feels fragile,
like it could shatter. Beautiful but precarious. Bittersweet
atmosphere. Chinese ink wash style, gilded fragility.
--ar 16:9
```

**ending_split.jpg** — 结局C（分别说话）

```
A city square where stone and silk architecture coexist. A stone
sculptor works on a rounded sculpture — his first. A painter
creates an honest portrait — not美化, but real. Two young lovers
hold hands across the old boundary line. Imperfect harmony.
Warm afternoon light mixing with cool shadows. Chinese ink wash
style, gentle coexistence.
--ar 16:9
```

**ending_silent.jpg** — 结局D（沉默）

```
A vast empty space filled with soft light. A child's drawing lies
on the ground — it shows a figure standing before a mirror, and
the reflection is smiling. Around the drawing, fragments of a
mirror wall dissolve into light particles. Two cities visible in
the distance, slowly merging into one. Profound silence and peace.
Ethereal silver and soft gold palette. Chinese ink wash style,
transcendent beauty.
--ar 16:9
```

**river.jpg** — 后日谈 · 河

```
A serene infinite river at sunset. The water reflects golden and
blue light. A small figure runs toward the viewer on the riverbank,
holding up drawings. The river stretches to the horizon — this
side is the past, the far side is the future. A figure stands
at the water's edge, waiting. Warm sunset colors blending with
cool water tones. Peaceful, healing, hopeful. Chinese ink wash
style, luminous beauty.
--ar 16:9
```

**river_sunset.jpg** — 后日谈 · 夕阳

```
Two figures — an adult and a small child — sit by a river at
sunset, looking at drawings together. The child's drawings show
a complete city, people smiling, flowers growing. The adult is
smiling for the first time. The river flows gently between the
past and the future. Golden hour light, warm and encompassing.
The most beautiful scene in the entire game. Chinese ink wash
style, emotional warmth, closure.
--ar 16:9
```

---

## 三、角色立绘 Prompt

> 每个角色需要：1 张基础立绘 + 4 种表情变体
> 建议尺寸：800×1200px，PNG 透明底
> 生成时追加：`character sheet, full body, transparent background, clean linework`

### 通用负面提示词（立绘）

```
Negative: text, watermark, signature, multiple characters,
extra limbs, deformed, ugly, blurry, low quality,
photorealistic face, 3D render, anime style, chibi,
busy background, landscape elements
```

### 通用风格后缀（立绘）

```
style: Chinese ink wash painting meets modern illustration,
delicate watercolor coloring, clean linework,
muted elegant palette, portrait composition --ar 2:3 --s 800
```

---

### 3.1 主角：勿言

**wuyan_base.jpg** — 基础立绘

```
A gender-neutral figure in their late 20s, wearing a long grey
robes with subtle watercolor texture. Short to medium length dark
hair. Calm, contemplative expression. Eyes that carry deep sadness
but also quiet determination. Standing in a neutral pose, hands
at sides. The figure seems to belong to neither side — neither
cold nor warm. Misty ethereal aura around them.
Full body portrait, transparent background.
Chinese ink wash illustration style.
```

**表情变体：**

| 文件名 | 表情 | prompt 追加 |
|--------|------|------------|
| wuyan_neutral.jpg | 平静 | `calm neutral expression, eyes looking forward` |
| wuyan_sad.jpg | 悲伤 | `quietly sad expression, eyes downcast, barely holding back tears` |
| wuyan_determined.jpg | 坚定 | `determined expression, eyes focused forward, jaw set` |
| wuyan_smile.jpg | 微笑 | `gentle warm smile, eyes soft, the first genuine smile` |

---

### 3.2 左城角色

**baisui.jpg** — 白岁（石匠，62岁）

```
An elderly stone sculptor, age 62. Weathered face with scars from
flying stone chips. Strong working hands covered in calluses and
small cuts. Short grey hair, sharp piercing eyes that miss nothing.
Wearing simple dark grey work clothes. A chisel tucked into his
belt. Standing straight despite his age, rigid posture like the
stone he carves. Deep wrinkles that map a life of silence.
Full body portrait, transparent background.
Chinese ink wash illustration, cold blue-grey tones.
```

| 文件名 | 表情 | 追加 |
|--------|------|------|
| baisui_neutral.jpg | 冷静 | `expressionless, stone-like calm, watching carefully` |
| baisui_surprised.jpg | 惊讶 | `slightly surprised, one eyebrow raised, rare vulnerability` |
| baisui_pain.jpg | 痛苦 | `pain hidden behind stoic expression, eyes glistening` |
| baisui_soft.jpg | 柔和 | `rare soft expression, the ghost of a memory smile` |

---

**xiaoxue.jpg** — 小雪（学生，14岁）

```
A 14-year-old girl with short dark hair. Wearing dark practical
clothes typical of the grey city. Ice crystal traces on her hands
— evidence of speaking truth. Curious bright eyes that contrast
with her somber clothing. A sketchbook clutched to her chest.
Small for her age but with a fierce inner light. The only
young person who dares to question the rules.
Full body portrait, transparent background.
Chinese ink wash illustration, cold blue tones with hints of light.
```

| 文件名 | 表情 |
|--------|------|
| xiaoxue_curious.jpg | `curious expression, eyes wide, leaning forward slightly` |
| xiaoxue_afraid.jpg | `afraid to speak, lips pressed together, ice forming on hands` |
| xiaoxue_hope.jpg | `hopeful expression, a small brave smile breaking through` |
| xiaoxue_cry.jpg | `tears freezing on cheeks, sad but defiant` |

---

**shiyan.jpg** — 石言（长老，78岁）

```
An austere old man, age 78, the chief elder of the truth city.
Thin and gaunt, leaning on a staff made of crystallized truth —
it looks like frozen lightning. Deep-set eyes under heavy brows.
His face is a mask of severity. Wearing dark layered robes with
angular silver ornaments. Every line on his face speaks of rigid
conviction. Behind the stern exterior, the faintest crack of
hidden grief.
Full body portrait, transparent background.
Chinese ink wash illustration, dark cold palette.
```

| 文件名 | 表情 |
|--------|------|
| shiyan_stern.jpg | `stern authoritative expression, commanding presence` |
| shiyan_shaken.jpg | `shaken, mask cracking, eyes betraying hidden pain` |
| shiyan_back.jpg | `view from behind, walking away, shoulders slightly slumped` |
| shiyan_accept.jpg | `quiet acceptance, eyes closed, staff lowered` |

---

**yan.jpg** — 岩（医生，45岁）

```
A middle-aged surgeon from the grey city, age 45. Precise and
controlled in every movement. Short dark hair with early grey
streaks. Clean-shaven face with sharp features. Wearing a simple
dark coat over medical attire. His hands are steady — surgeon's
hands. Eyes that have seen too much death to show emotion, but
carry an ancient sadness. Hasn't smiled in years.
Full body portrait, transparent background.
Chinese ink wash illustration, muted cold tones.
```

| 文件名 | 表情 |
|--------|------|
| yan_neutral.jpg | `clinical neutral expression, controlled and precise` |
| yan_mirror.jpg | `staring at reflection, confused — the mirror version smiles` |
| yan_grief.jpg | `rare crack in composure, suppressed grief surfacing` |
| yan_smile.jpg | `attempting a smile for the first time in years, awkward but real` |

---

**li.jpg** — 砾（少年诗人，17岁）

```
A 17-year-old boy poet from the grey city. Lean build, angular
features that mirror the city's architecture. Dark unkempt hair.
Intense eyes that burn with unspoken emotion. Wearing a worn grey
jacket. Carries a collection of stone tablets inscribed with
his poems. His posture shifts between confident defiance and
youthful vulnerability. Every gesture is sharp and expressive.
Full body portrait, transparent background.
Chinese ink wash illustration, cold tones with emotional warmth.
```

| 文件名 | 表情 |
|--------|------|
| li_poetry.jpg | `reciting poetry, eyes closed, passionate expression` |
| li_love.jpg | `looking toward mirror wall, longing in eyes, vulnerable` |
| li_cry.jpg | `first tears, overwhelmed, not hiding it anymore` |
| li_smile.jpg | `rare genuine smile after hearing her voice through the wall` |

---

### 3.3 右城角色

**yunshang.jpg** — 云裳（画师，28岁）

```
A beautiful young woman painter, age 28. Long flowing hair like
a waterfall. Wearing an elegant but slightly worn silk dress in
warm amber tones — the hem has been mended. She carries herself
with practiced grace. Paint-stained fingers. Eyes that see beauty
in everything but hide a deep question: what does real beauty
look like? The most beautiful person in the golden city, yet
she has never painted herself.
Full body portrait, transparent background.
Chinese ink wash illustration, warm golden palette.
```

| 文件名 | 表情 |
|--------|------|
| yunshang_smile.jpg | `practiced beautiful smile, warm but slightly rehearsed` |
| yunshang_wonder.jpg | `genuine wonder, seeing something truly beautiful for the first time` |
| yunshang_sad.jpg | `quiet sadness beneath the beauty, looking at a blank canvas` |
| yunshang_painting.jpg | `focused while painting, brush in hand, deeply absorbed` |

---

**miyu.jpg** — 蜜语（甜言建筑师，35岁）

```
A cheerful woman in her mid-30s. Bright warm smile that never
fades — even when it should. Wearing colorful practical work
clothes with flower patterns, but close inspection reveals
patches and repairs. Her fingernails have glue residue from
repairing buildings with sweet words. Hair tied back practically.
Despite her relentless optimism, there are dark circles under
her eyes that makeup can't fully hide.
Full body portrait, transparent background.
Chinese ink wash illustration, warm palette with hidden shadows.
```

| 文件名 | 表情 |
|--------|------|
| miyu_cheerful.jpg | `relentlessly cheerful smile, bright and unwavering` |
| miyu_crack.jpg | `smile cracking for a moment, real worry showing through` |
| miyu_hope.jpg | `genuine hope, not performed — the real emotion behind the mask` |
| miyu_cry.jpg | `finally crying, smile gone, real tears — the most honest she's been` |

---

**huayan.jpg** — 花言（长老，70岁）

```
An elderly man in magnificent flowered robes, chief elder of the
golden city, age 70. His robes are the most ornate in the city —
layers of golden silk with embroidered flowers that seem to move.
A permanent慈祥 (benevolent) smile on his face. But his eyes are
calculating, sharp beneath the warmth. Silver hair arranged
perfectly. Carries an air of absolute control. The mask of kindness
hides decades of manipulation and hidden pain.
Full body portrait, transparent background.
Chinese ink wash illustration, rich gold and deep amber.
```

| 文件名 | 表情 |
|--------|------|
| huayan_benevolent.jpg | `benevolent smile, wise elder appearance, composed` |
| huayan_calculation.jpg | `calculating gaze, smile unchanged but eyes cold` |
| huayan_broken.jpg | `mask shattered, first real expression: exhaustion and pain` |
| huayan_truth.jpg | `speaking truth for the first time, lips bleeding, agonized` |

---

**ming.jpg** — 明（蜜语的丈夫，40岁）

```
A man in his early 40s who has stopped speaking. Sitting by a
window, staring out. Thin, pale from years indoors. Wearing a
simple faded shirt — the only unadorned person in the golden city.
His eyes are the most striking feature: once warm, now empty,
like someone who has forgotten the difference between truth and
lies. Hands resting on his lap, still. A man who has lost the
ability to feel his own emotions.
Full body portrait, transparent background.
Chinese ink wash illustration, muted warm tones fading to grey.
```

| 文件名 | 表情 |
|--------|------|
| ming_empty.jpg | `empty stare, looking through the viewer, disconnected` |
| ming_pain.jpg | `suppressed pain surfacing, brow furrowed, lips trembling` |
| ming_smile.jpg | `first small smile in years, fragile, uncertain` |
| ming_peace.jpg | `peaceful acceptance, eyes softened, quietly present` |

---

**yao.jpg** — 瑶（倾听者，16岁）

```
A 16-year-old girl with gentle features. Soft dark hair with a
few flower petals caught in it. Wearing a simple but pretty dress
in warm rose tones. She has a habit of tilting her head when
listening — she's always listening. A sketchbook and charcoal
pencil are her constant companions. Her eyes are unusually perceptive
for her age — she sees through pretense. The only person in the
golden city who seeks out truth.
Full body portrait, transparent background.
Chinese ink wash illustration, warm rose and amber tones.
```

| 文件名 | 表情 |
|--------|------|
| yao_listen.jpg | `listening intently, head tilted, eyes focused beyond the mirror` |
| yao_blush.jpg | `blushing, embarrassed but brave, about to speak truth` |
| yao_pain.jpg | `lips bleeding after speaking truth, but smiling through the pain` |
| yao_love.jpg | `gentle loving expression, looking at the sculpture through the mirror` |

---

### 3.4 镜墙角色

**ying.jpg** — 守镜人 · 影

```
A mysterious figure who is half of one city and half of the other.
Left side of face is angular and cold-toned (grey stone texture).
Right side is soft and warm-toned (golden light). Wearing a grey
hooded cloak that bridges both sides. Neither old nor young.
Neither male nor female. Eyes that have watched for millennia.
Half the face is always in shadow. A being made of mirror —
slightly translucent at the edges, with faint reflective quality.
Full body portrait, transparent background.
Chinese ink wash illustration, silver and dual-tone palette.
```

| 文件名 | 表情 |
|--------|------|
| ying_neutral.jpg | `serene neutral expression, ancient patience` |
| ying_knowing.jpg | `knowing half-smile, sees through everything` |
| ying_sad.jpg | `rare sadness, knowing what must happen next` |
| ying_peace.jpg | `peaceful acceptance, fading slightly, at peace with dissolution` |

---

**hua_child.jpg** — 失语的孩子 · 画（7岁）

```
A 7-year-old child born in the mirror wall's crack. Grey eyes
that hold no expression — not sad, not happy, just present.
Short messy hair. Wearing a simple grey tunic that seems to
be made of mirror mist. Always holding a crayon or brush.
Small and slight, almost translucent at the edges. The child
cannot speak at all — communicates only through drawings.
An otherworldly, liminal presence. Neither of any city.
Full body portrait, transparent background.
Chinese ink wash illustration, ethereal grey-silver palette.
```

| 文件名 | 表情 |
|--------|------|
| hua_drawing.jpg | `focused on drawing, holding crayon to paper, completely absorbed` |
| hua_watch.jpg | `watching silently, holding drawing, observing everything` |
| hua_offer.jpg | `offering a drawing to someone, small gesture of connection` |
| hua_smile.jpg | `the faintest smile — rare, precious, like sunlight through clouds` |

---

## 四、UI 元素 Prompt

### 4.1 对话框

**ui_dialogue_left.png** — 左城对话框

```
A dark rectangular dialogue box frame, angular corners (no
rounding), made of carved grey stone texture. Subtle blue-grey
color (#1A1A2E). Thin bright blue border line at top. Interior
is semi-transparent dark. 9-slice compatible — corners, edges,
and center should tile. Clean minimal design, no decorations.
1600x300 pixels. PNG with alpha.
```

**ui_dialogue_right.png** — 右城对话框

```
A warm rectangular dialogue box frame, rounded corners (20px
radius), made of silk-like texture with golden shimmer. Warm
amber color (#FFF8E7 at 75% opacity). No hard border — use a
soft golden glow instead. Interior is semi-transparent warm.
9-slice compatible. Elegant, flowing design.
1600x300 pixels. PNG with alpha.
```

### 4.2 语言轮盘背景

**ui_wheel_bg.png** — 轮盘背景

```
A rectangular panel background for a choice wheel UI. Dark blue-
grey (#1A1A2E) at 95% opacity. Subtle glass-like sheen. Slight
frosted glass texture. Rounded corners (8px). No decorations
inside — just the clean panel. 900x500 pixels. PNG with alpha.
```

### 4.3 按钮

**ui_btn_truth.png / ui_btn_truth_hover.png** — 真话按钮

```
A rectangular button with angular corners. Dark blue-grey gradient
(#2A3A4C to #3A4A5C). Thin blue border (#4A90D9 at 30% opacity).
Clean and minimal. Hover version: brighter gradient (#3A4A5C to
#4A6FA5), border at 60% opacity, subtle glow.
350x300 pixels. PNG with alpha.
```

**ui_btn_lie.png / ui_btn_lie_hover.png** — 假话按钮

```
A rectangular button with rounded corners (12px). Dark warm gradient
(#3A2E20 to #4A3A2C). Thin golden border (#D4A574 at 30% opacity).
Elegant and warm. Hover version: brighter gradient, border glows.
350x300 pixels. PNG with alpha.
```

---

## 五、生成工作流建议

### 推荐工具组合

| 用途 | 推荐工具 | 原因 |
|------|---------|------|
| 背景图 | Midjourney v6 + Photoshop | 画质最好，后期方便 |
| 角色立绘 | Stable Diffusion + ControlNet | 可精确控制姿势和一致性 |
| UI 元素 | Figma / Photoshop | 精确像素控制 |
| 批量表情 | SD + IP-Adapter | 保持角色一致性 |

### 角色一致性工作流

```
1. 先用 MJ/SD 生成角色基础立绘（最好的一张）
2. 用 IP-Adapter / Reference Only 锁定角色特征
3. 通过修改 prompt 中的表情描述生成变体
4. 在 Photoshop 中微调，确保风格统一
```

### 色彩一致性检查清单

- [ ] 左城所有素材：色温偏冷（#3A4A5C 系）
- [ ] 右城所有素材：色温偏暖（#D4A574 系）
- [ ] 镜墙素材：中性银白（#C0C0C0 系）
- [ ] 所有素材：去饱和 20-30%，保持水墨感
- [ ] 所有素材：添加微弱颗粒纹理

---

## 六、批量生成脚本参考（Midjourney）

```
# 批量生成背景图的 /imagine 命令参考

/imagine prompt: [上方各场景 prompt] + style: Chinese ink wash painting
meets modern concept art, muted watercolor palette, soft atmospheric
lighting, cinematic composition, delicate brushstrokes, subtle grain
texture --ar 16:9 --s 750 --v 6

# 批量生成立绘的 /imagine 命令参考

/imagine prompt: [上方各角色 prompt] + character sheet, full body,
transparent background, clean linework, Chinese ink wash illustration
style, delicate watercolor coloring --ar 2:3 --s 800 --v 6
```
