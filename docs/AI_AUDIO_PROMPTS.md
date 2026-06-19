# 《镜中城》AI 音频生成 Prompt

> 适用于 Suno / Udio / Stable Audio 等 AI 音乐生成工具。
> 每首 BGM 建议生成 2-3 个版本，选最好的那个。

---

## 一、BGM（7 首）

### 1.1 主菜单 — 「裂镜」

**Suno Prompt：**

```
Gentle ethereal ambient music, solo piano with soft reverb, 
Chinese ink wash painting atmosphere, mysterious and contemplative,
single mirror crack visualized in sound — a sustained note that 
fragments into delicate overtones, 
very slow tempo, spacious silence between notes, 
minor key, no drums, 
cinematic meditation music
```

**风格标签：** `ambient, cinematic, meditation, piano, ethereal`
**BPM：** 50-60
**时长目标：** 2-3 分钟（循环）
**情绪：** 神秘、空灵、微微的哀伤

---

### 1.2 左城 — 「石之沉默」

**Suno Prompt：**

```
Dark minimalist cello solo, cold and austere atmosphere,
single sustained cello notes with long decay, 
occasional sharp staccato bow strokes like chisel on stone,
vast empty space in the arrangement,
ice crystals forming — high frequency glass harmonica whispers,
no harmony, no rhythm, pure isolation,
deep melancholy, restrained emotion,
Chinese ink wash aesthetic translated to sound
```

**风格标签：** `cello, minimalist, dark ambient, experimental`
**BPM：** 自由节奏（无固定 BPM）
**时长目标：** 3-4 分钟（循环）
**情绪：** 冷冽、克制、压抑中的温柔
**关键乐器：** 大提琴独奏、偶尔的玻璃琴泛音

---

### 1.3 右城 — 「蜜语花园」

**Suno Prompt：**

**

Suno Prompt（中文版参考）：

```
Warm music box melody with harp arpeggios, 
golden afternoon light feeling, 
flowing silk-like textures,
beautiful but slightly off-key — a music box that has been 
playing too long, some notes bend unnaturally,
wind chimes and soft bell tones,
sugar-coated surface hiding something fragile,
waltz-like gentle rhythm, 3/4 time,
bittersweet beauty, nostalgic warmth,
Studio Ghibli meets Chinese tea ceremony music
```

**风格标签：** `music box, harp, waltz, ambient, nostalgic`
**BPM：** 80-90
**时长目标：** 3 分钟（循环）
**情绪：** 温暖、甜蜜、微妙的不安
**关键乐器：** 八音盒、竖琴、风铃
**特殊要求：** 部分音符刻意走调 5-10 音分，制造"不真实的美"

---

### 1.4 镜墙 — 「之间」

**Suno Prompt：**

```
Two contrasting melodies playing simultaneously and slowly merging,
left voice: cold solo cello in minor key,
right voice: warm music box in major key,
starting from opposite sides of the stereo field,
gradually moving toward center,
when they meet, they create unexpected beautiful harmony,
then separate again,
glass wall shattering effect as transition,
ethereal reverb, spacious mix,
cinematic tension and resolution,
minimalist orchestral, emotional
```

**风格标签：** `cinematic, orchestral, minimalist, stereo experiment`
**BPM：** 70
**时长目标：** 4-5 分钟
**情绪：** 对立→接近→冲突→和解
**关键设计：** 左声道冷色大提琴，右声道暖色八音盒，中段融合

---

### 1.5 闪回 — 「碎影」

**Suno Prompt：**

```
Distorted nostalgic piano melody, like a memory fading in and out,
warm piano notes that blur and smear with heavy reverb,
occasionally interrupted by sudden silence then return,
underwater quality — all frequencies slightly muffled,
a child's laughter sample buried deep in the mix,
building emotional intensity then suddenly cutting to silence,
film score style, deeply personal,
memory of happiness turning to loss,
piano with tape warble effect, lo-fi warmth
```

**风格标签：** `piano, lo-fi, cinematic, emotional, nostalgia`
**BPM：** 65
**时长目标：** 2-3 分钟
**情绪：** 温暖→模糊→心碎→空白
**关键设计：** 钢琴旋律间穿插 2-3 秒完全静音（模拟记忆断裂）

---

### 1.6 最终选择 — 「渡」

**Suno Prompt：**

```
Epic cinematic build-up, starting with single heartbeat-like 
deep bass pulse,
strings gradually entering one by one, building tension,
choir-like sustained pads rising in volume,
reaching a climax of overwhelming emotional sound,
then suddenly dropping to complete silence for 3 seconds,
then a single pure note emerges — either warm (major) 
or cold (minor) depending on choice,
resolving into peaceful resolution,
orchestral film score, Hans Zimmer inspired,
emotional catharsis through sound
```

**风格标签：** `cinematic, orchestral, epic, emotional, film score`
**BPM：** 70 → 120 → 60（速度变化）
**时长目标：** 4-5 分钟
**情绪：** 紧张积累 → 爆发 → 骤停 → 释放
**关键设计：** 中段有 3 秒完全静音，然后一个音符打破沉默

---

### 1.7 结局 — 「归」

**Suno Prompt：**

```
Peaceful healing ambient music, warm piano and soft strings,
sunrise over water feeling, gentle and complete,
every musical phrase resolves beautifully — no tension left,
soft choir hums in background like distant memory,
river flowing sounds woven into the music naturally,
the most beautiful and complete piece in the collection,
Chinese traditional instrument guqin blended with 
modern ambient piano,
hope after darkness, warmth after cold,
serene closure, emotional healing
```

**风格标签：** `ambient, healing, piano, strings, peaceful`
**BPM：** 60-70
**时长目标：** 3-4 分钟
**情绪：** 平静、释然、温暖、完整
**关键乐器：** 钢琴 + 古琴 + 弦乐 + 轻声合唱

---

## 二、环境音（4 个）

> 这些可以用 Suno 的 "Create Sound" 功能，或用 freesound.org 下载后混音。

### 2.1 左城环境音

```
Cold wind blowing through narrow stone alleys,
occasional ice cracking sounds, 
distant stone chisel strikes echoing,
footsteps on stone pavement,
complete absence of birdsong or life sounds,
desolate winter atmosphere,
binaural recording style, immersive
```

**叠加元素：**
- 低频风声（持续）
- 偶尔冰裂声（每 15-20 秒一次）
- 远处凿石声（每 30 秒一次）
- 脚步回声（可选）

### 2.2 右城环境音

```
Gentle warm breeze carrying flower petals,
wind chimes tinkling softly and randomly,
distant murmur of people exchanging compliments — 
unintelligible warm voices,
occasional silk rustling sounds,
sugar-sweet atmosphere, like walking through a garden,
stereophonic immersive field recording
```

**叠加元素：**
- 风铃声（随机，柔和）
- 花瓣飘落的细微沙沙声
- 远处人群低语（不可辨识，温暖氛围）
- 偶尔的布料摩擦声

### 2.3 镜墙环境音

```
Ethereal resonant hum, like singing bowls underwater,
occasional crystalline chime — mirror surface vibrating,
deep sub-bass drone that you feel more than hear,
ghostly whispers in the reverb tail,
infinite space feeling — no walls, no ceiling,
sacred mysterious atmosphere,
spatial audio, 3D immersive
```

**叠加元素：**
- 持续低频共鸣（如颂钵）
- 随机玻璃/镜面振动音
- 混响尾部的幽灵低语
- 偶尔的"裂缝"声（清脆短促）

### 2.4 河流环境音（后日谈）

```
Slow gentle river flowing over smooth stones,
very quiet, meditative water sounds,
occasional single water drop creating expanding ripples,
no wind, no birds — just water and silence,
healing ASMR quality,
endless peaceful river at dusk
```

---

## 三、音效（10 个）

> 这些建议用 Suno 的短音效功能或用 Web Audio API 程序化生成。

### 3.1 语言轮盘弹出

```
Soft glass chime ascending, ethereal reverb tail,
two-tone: first note cold (high pitch), second note warm (lower pitch),
like a magical mirror surface appearing,
clean and minimal, 1.5 seconds
```

**备选：** 程序化生成 — 两个正弦波（440Hz + 523Hz），各 0.3 秒，带指数衰减

### 3.2 真话选择确认

```
Sharp crystalline chime, like ice forming,
single clean high note with long reverb tail,
satisfying click underneath, 
like pressing a cold stone button,
0.8 seconds
```

### 3.3 假话选择确认

```
Warm soft bell tone, like a music box note,
slightly rounded attack, gentle decay,
like touching a silk cushion,
0.8 seconds
```

### 3.4 沉默选择确认

```
Almost silent — a very faint breath of wind,
single low frequency whisper that fades immediately,
the sound of choosing not to speak,
barely audible, 1 second
```

### 3.5 章节转场

```
Deep resonant gong struck once, 
with long reverb that slowly fades into the next scene's ambience,
cinematic chapter break, 
solemn and important feeling,
3 seconds
```

### 3.6 成就解锁

```
Three ascending notes in major chord: C-E-G,
warm celesta or glockenspiel tone,
satisfying completion sound,
bright but not jarring,
1.5 seconds
```

### 3.7 镜墙碎裂

```
Massive glass wall shattering in slow motion,
thousands of tiny fragments tinkling as they fall,
deep bass rumble underneath,
epic destruction beauty,
2-3 seconds
```

### 3.8 记忆闪回进入

```
Tape rewind sound mixed with piano note being sucked backwards,
reverse reverb effect,
sudden shift from present to past,
disorienting but not scary,
1.5 seconds
```

### 3.9 对话框出现

```
Soft fabric unfolding sound, like silk banner dropping,
very subtle, non-intrusive,
barely noticeable but adds tactile quality,
0.5 seconds
```

### 3.10 场景切换

```
Two-part transition: 
first half — current scene fading out with wind,
second half — new scene fading in with its ambient texture,
crossfade bridge, seamless,
2 seconds
```

---

## 四、生成工作流

### Suno 推荐流程

```
1. 打开 suno.com → Create
2. 选择 Custom Mode
3. 粘贴上方 Prompt 到 Lyrics/Description 框
4. 设置 Instrumental（纯音乐）或 Vocal（有哼唱）
5. 风格标签填入 Style 栏
6. 生成 2-3 个版本，选最好的
7. 下载 MP3，放到 game/audio/music/ 目录
```

### 文件命名规范

```
game/audio/
├── music/
│   ├── bgm_menu.mp3          ← 1.1 主菜单
│   ├── bgm_left_city.mp3     ← 1.2 左城
│   ├── bgm_right_city.mp3    ← 1.3 右城
│   ├── bgm_mirror.mp3        ← 1.4 镜墙
│   ├── bgm_flashback.mp3     ← 1.5 闪回
│   ├── bgm_final_choice.mp3  ← 1.6 最终选择
│   └── bgm_ending.mp3        ← 1.7 结局
├── ambient/
│   ├── ambient_left_city.mp3 ← 2.1
│   ├── ambient_right_city.mp3← 2.2
│   ├── ambient_mirror.mp3    ← 2.3
│   └── ambient_river.mp3     ← 2.4
└── sfx/
    ├── sfx_wheel_appear.mp3  ← 3.1
    ├── sfx_truth.mp3         ← 3.2
    ├── sfx_lie.mp3           ← 3.3
    ├── sfx_silent.mp3        ← 3.4
    ├── sfx_chapter.mp3       ← 3.5
    ├── sfx_achievement.mp3   ← 3.6
    ├── sfx_mirror_crack.mp3  ← 3.7
    ├── sfx_flashback.mp3     ← 3.8
    ├── sfx_dialogue.mp3      ← 3.9
    └── sfx_scene_change.mp3  ← 3.10
```

---

## 五、注意事项

1. **Suno 生成的 MP3 采样率**通常是 44.1kHz，Ren'Py 直接支持
2. **BGM 循环**：生成后如果有明显的首尾断裂，告诉我，我用代码做无缝循环处理
3. **音量平衡**：BGM 和环境音需要混音时，我可以在代码中设置独立音量
4. **免费额度**：Suno 免费版每天 5 首，7 首 BGM 需要 2 天；环境音和音效可以混合在一首长曲里生成，然后我用代码切割
