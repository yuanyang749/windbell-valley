# 风铃溪谷：制作提示词与实际流程

- [在线体验](https://yuanyang749.github.io/windbell-valley/)
- [成品仓库](https://github.com/yuanyang749/windbell-valley)
- [参考示例：sprite-gen 的 village-scene.gif](https://github.com/aldegad/sprite-gen/blob/main/docs/assets/village-scene.gif)
- [sprite-gen 工具与技能](https://github.com/aldegad/sprite-gen)

这份文件将多轮制作与修正整理成可复用的总提示词，并附上实际使用的素材生成提示词。交付形式是带音乐的预渲染村庄游览视频，以及可以横向拖动的静态大地图网页。

## 一、可直接复制的总提示词

适用于能生成图片、运行本地工具和操作 GitHub 的 AI 编程助手。开始前准备好 sprite-gen、Grok CLI 的订阅登录、RIFE 和 FFmpeg；图片使用助手内置的图像生成能力。实际音乐渲染使用了 macOS 系统乐器声库。

```text
请参考 https://github.com/aldegad/sprite-gen 中 docs/assets/village-scene.gif
的场景组织方式，制作一个新的、具有吉卜力式温暖手绘气质的村庄场景。
名称为“风铃溪谷 / Windbell Valley”。地图要足够大，人物和 NPC 可以自由设计。
请完成素材生成、动作制作、场景合成、配乐、网页展示和 GitHub Pages 发布。

【画面与地图】
使用明亮、柔和的水彩和不透明水彩手绘动画风格，细腻的棕色轮廓，奶油色墙面、
蓝绿色屋顶、鼠尾草绿植被与暖赭色阳光。原创村庄建筑与角色。

地图横向宽度至少 6000 像素，由三个相邻街区组成：
1. 山坡住居：小屋、乡间邮局、晾衣绳、果园、花园和石墙。
2. 村中集市：面包店、花果摊、老树、长椅、喷泉和风铃。
3. 河岸水车：水磨坊、溪流、石拱桥、柳树和菜园。

先分区生成约 3:1 的宽幅背景，再检查道路高度、光线、建筑尺度和衔接。
前方步行道路保持水平贯穿，清晰可走；两侧留出自然过渡区域。
背景中间层安排房屋、台阶、花丛和桥面，给 NPC 预留合理的站立位置。
背景图保持完整，人物使用独立的透明素材。

【主角】
设计一名乡间邮差少女和一只白狐伙伴，沿道路向右旅行。
少女有短棕发、赭黄色小披肩、奶油色上衣、深青色裙子、棕色靴子和斜挎邮包。
白狐有奶油白毛色、蓬松尾巴和一条简单的绿色围巾。
分别制作真实的走路和跑步动作循环，维持身份、服装与道具一致。

【三个 NPC】
园丁：草帽、绿色开衫、围裙和棕裙，手持浅蓝色水壶。她低头看花、轻微前倾，
抬起并倾斜水壶，倒出清晰的细水流与少量水滴，再回到起始姿态。

面包师：短赤褐发、头巾、奶油色袖子、蓝围裙和暖红棕裙。她用一只手稳托面包篮，
另一只手举起挥动，笑着招呼顾客售卖面包，再回到抱篮姿态。

吹笛老人：银发、短胡须、圆眼镜、蓝色背心、棕裤和小挎包。他双手保持持笛，
笛子贴着嘴，沉浸地轻摇头与肩膀，手指自然动作；笛子附近出现两三枚小金色音符，
缓缓上飘并消失，再回到起始姿态。老人应站在桥面上，近侧石栏遮住相应脚部。

【动作与后处理】
使用 Grok 订阅登录生成角色动作视频，保持镜头固定、人物大小固定。
三个 NPC 各制作一个约 4 秒的循环，使用同一张人物图作为首帧与末帧约束。
生成前扩展画布，为挥手、水流和音符留出空间。
角色图使用纯洋红色 #FF00FF 背景，服装避开同色；使用 sprite-gen 抠像和切循环。
先确认输入背景是真正均匀的纯色，再送入视频画布工具。

所有角色动画尽量使用已安装的本地 RIFE 补帧。保留通过质量检查的中间帧，
对变形的插帧使用工具已有的质量保护。保存每帧时长，补帧后维持原动作周期和速度。
NPC 的定位锚点固定在鞋底，水流和音符的边界不能改变人物位置。
逐帧检查手、脚、面包篮、水壶与笛子，并检查循环衔接和脚底滑动。

【场景合成】
主角和白狐沿前方道路移动，镜头横向跟随，逐渐展示三个街区。
为角色添加轻柔的地面阴影和少量前景植物。
老人的站立点按实际桥面确定，使用桥前侧石栏的独立遮挡层表达前后关系。
各 NPC 循环独立播放；完整视频形成一次从山坡到河岸的游览。
目标成品约 42 秒，1280 × 720，30 fps。

【环境动态】
水车外缘的水帘沿叶片持续下落，底部有细小水花、波纹和流向溪流的细水。
水车木质结构、石墙和岸边保持固定，以局部水流遮罩合成，使用本地 RIFE 补帧。
集市的三角旗只动旗面、喷泉只动水流和盆内波纹、大树枝梢与叶簇随风摆动。
保持旗绳、喷泉石质结构、树干和粗枝固定，少量落叶缓慢旋转飘落。
部分房屋烟囱增加淡淡炊烟，烟雾从准确的烟囱口起始，缓缓向上卷曲消散。
前景花簇加入少量蝴蝶和蜜蜂，真实扇翅、悬停与小范围飞行，避免遮住主角。
在原背景中选取晾衣绳、柳树垂枝与溪流水面区域，生成固定镜头的约 4 秒动作循环。
衣服上端保持挂在绳上、下摆随风轻摆；柳树主干保持稳定，只让外围枝梢轻摆；
溪流波纹与反光沿河道流动，桥、河岸、石头与草丛保持静止。
使用原画裁剪作为首尾帧，动画局部经过固定遮罩合回原图，并做边缘过渡和色调检查。
沿用 sprite-gen 循环检查与本地 RIFE 补帧，保护遮罩外原像素，检查循环衔接。
这次只让视频中的环境动起来，可拖动的大地图仍是静态图片。

【背景音乐】
创作一首原创、轻柔、温暖的三拍小曲，约 72 BPM。
以笛子旋律和尼龙弦木吉他分解和弦为主，加入轻弦乐、少量钟琴和低音。
旋律与和声适合春日乡间漫步。使用可用的本地乐器声库渲染，保留乐谱数据与 MIDI。
让音乐与完整视频一样长，开头和结尾自然淡入淡出，控制音量并避免削波。
将音乐合并进最终视频，浏览器点击“开启音乐”即可听到。

【网页与发布】
使用简单的静态 HTML、CSS 和 JavaScript 展示成品，风格与手绘村庄一致。
提供“动画游览 / 大地图”切换、地图横向拖动和街区跳转。
提供“园丁浇花 / 面包师挥手 / 老人吹笛”三个视频跳转按钮与音乐开关。
默认静音自动播放，并提供视频和大地图下载入口。

将网页实际需要的文件集中到 windbell-valley-web 文件夹：
index.html、assets/scene.mp4、assets/scene-poster.png、assets/windbell-valley.png，
以及 README.md、PROMPT.md 和 .nojekyll。
媒体使用相对路径，确保可以部署在 GitHub Pages 的仓库子路径下。
推送到当前用户的 GitHub 公开仓库 windbell-valley，并从 main 分支根目录发布 Pages。
如果同名仓库存在，先核对是否属于本项目，再决定如何更新。

【执行与验收】
先完成可以运行的场景，再逐步完善动作、桥面遮挡、配乐和发布。
复用 sprite-gen 已有的抠像、动画循环、插帧和场景合成模块。
持续保存关键提示词、素材、参数和检查结果，已有成品在替换前备份。
检查地图接缝、角色脚底、道具一致性、水流落点、音符位置、音乐和视频时长。
检查网页播放、音乐开关、三个动作跳转与大地图拖动。
上线后核对页面和素材可访问，视频服务器支持 HTTP Range 和按时间跳转。
完成实现、必要修正与验证，再交付公开网址和仓库链接。
```

## 二、实际制作过程与修正

### 1. 分区生成大地图

三个街区分别生成并统一尺度，实际每区为 2172 × 724，相邻街区重叠 96 像素，最终得到 6324 × 724 的完整地图。保留了统一的前方道路高度与晚春光照。

### 2. 生成角色并制作主角动画

先生成邮差少女、白狐与三名 NPC 的角色图。少女和白狐通过 Grok 动作视频、sprite-gen 后处理和 RIFE 补帧，获得可以重复播放的走路与跑步动画，再合成镜头游览。

### 3. 修正老人站立位置

第一次合成时老人鞋底落在桥拱外侧。修正时把站立锚点移到桥面，并从背景原图提取近侧石栏作为前景遮挡层，让老人站在栏杆后方。

在当前成品地图上，老人最终定位为 `[5490, 417]`，角色层级为 `z=10`，近侧石栏为 `z=11`。重新生成地图时应根据新的桥面重新判断位置。

### 4. 将三个静态 NPC 改为动作循环

使用各自角色图作为动作依据，每个 NPC 生成 4 秒、720p、固定镜头的视频，模型为 `grok-imagine-video-1.5`，通过 Grok 订阅登录调用。首尾使用同一张图约束闭合姿态。

一次输入预处理发现洋红背景的四个角并非同一种颜色。随后先使用 sprite-gen 提取透明人物，再合成到真正纯色的洋红画布，增加留白后继续生成动作。

动作出来后检查：面包师确实举手挥动并托住面包篮，园丁确实倾壶倒水，老人有轻微头肩摆动和飘动音符。

### 5. 抠像、切循环和 RIFE 补帧

复用 `video-frames` 去除洋红背景，使用参考图处理溢色与边缘，再由 `video-loop` 的 `pinned` 路线取出完整动作周期。

每个 NPC 的循环条带有 64 帧。调用 sprite-gen 的 RIFE v4.6 重采样与自动质量保护后，输出 128 帧、4 秒的素材，即 32 fps；最终场景视频按 30 fps 输出。人物定位依据初始姿态的鞋底固定，局部效果保留在同一画布中。

| NPC | 实际保留的 RIFE 中间帧 | 被质量保护拒绝的提案 | 输出帧数 | 动作周期 |
| --- | ---: | ---: | ---: | ---: |
| 园丁 | 59 | 5 | 128 | 4 秒 |
| 面包师 | 63 | 1 | 128 | 4 秒 |
| 吹笛老人 | 64 | 0 | 128 | 4 秒 |

这些数量来自此次成品报告；重新生成时应记录新的检查结果。

### 6. 原创配乐与合成

为场景编写了 16 小节、72 BPM、3/4 拍的 C 大调小曲：笛子主旋律、尼龙弦吉他分解和弦、轻弦乐、钟琴与原声低音。乐谱数据同时导出为 MIDI。

乐器通过 macOS 的 General MIDI 声库和 `AVAudioUnitSampler` 本地离线渲染，加入轻混响与淡入淡出，形成 42 秒立体声音轨，再用 FFmpeg 合并到 MP4。成品为 H.264 视频与 48 kHz AAC 音频。

### 7. 整理网页并发布

网页直接播放预渲染视频并展示静态全景图。音乐已经包含在视频中，因此页面只需要三份媒体成品。页面提供三名 NPC 的时间跳转、音乐开关、地图拖动、街区跳转与下载入口。

本地预览曾出现跳转后回到开头的问题，检查发现原静态服务不支持 HTTP Range；换用支持字节范围请求的服务后完成验证。GitHub Pages 上也检查了视频返回 `206 Partial Content` 与 `Accept-Ranges: bytes`。

仓库以 `main` 分支根目录发布，`.nojekyll` 保证静态文件直接提供。首次上线已核对部署成功、网页与本地页面一致、三个媒体文件可访问。上线时浏览器预览工具连接超时，线上检查使用 GitHub API 与 HTTP 完成；交互与播放检查此前在本地完成。

## 三、实际使用的图像生成提示词

以下保留生成素材时的英文原文，便于分别生成各个街区与角色。相邻街区和人物生成时使用已完成的背景作为风格参考。

### 1. 山坡住居

```text
Asset type: a wide horizontal scrolling 2D game village environment, first section of a much larger map. Make an ultrawide 3:1 panoramic landscape illustration, target 2400 x 800 pixels or greater, with a completely level side-view foreground walking lane. Art direction: original Studio Ghibli-inspired hand-painted animation background, luminous watercolor and gouache, carefully observed rustic architecture, soft sage foliage, warm ochre sunlight, pale blue distant haze, exquisite small lived-in details; clean HD painted artwork, no pixel art, no 3D render.
Scene: Windbell Valley, a tranquil hillside hamlet at late spring afternoon. In the middle of the panorama are three varied little cottages with warm plaster walls and aged blue-green tiled roofs, a tiny countryside postal station with a round red mail box, laundry gently hanging on a line, flowering climbing roses, firewood and potted herbs. Behind are apple orchards, layered soft green wooded hills and a spacious bright sky with high drifting clouds. A low irregular stone retaining wall separates the buildings' raised terraces from the sandy foreground lane. Path runs perfectly level horizontally across the whole image, spanning y=76% to 94% of the image; do not slant it into the distance. A narrow lower strip at y=94%-100% has sparse small grasses. Camera is a level lateral game camera, nearly front-on village facades, with a little visible roof depth. Sky/hills occupy upper 0%-24%, roofs and gardens middle 24%-75%. Entire roof silhouettes visible. Leave the front walking lane clear of major objects. The left and right 10% of image must contain only natural meadow/low hedge and continuous road, without houses, trees or fences touching the vertical edge; these unobtrusive transition areas allow joining to adjacent districts. Rich composition, human scale, lots of breathing room and six meters or more of continuous path, no cramped tiny diorama.
No people, no animals, no characters, no text or logos, no readable signs, no UI, no border, no vignette, no tiling duplicate houses. Fully opaque finished landscape. Warm sunlight comes from the upper left. This is a new original village, not a reproduction of any film location.
```

### 2. 村中集市

```text
Reference image is the first district of the same village. Generate a NEW ADJACENT DISTRICT, not a variation of those houses: an ultrawide 3:1 horizontal 2D side-scrolling game background, same painted scale, horizon, road height and late-spring light as the reference. Original Studio Ghibli-inspired hand-painted animation art, luminous watercolor/gouache, clean HD, subtle paper texture, no pixel art, no 3D. This middle district is a spacious village market square: a cozy low timber-and-plaster bakery with bread trays under a faded ochre awning; a blue-green market stall displaying flowers and citrus; a very old leafy plane tree with a little empty circular bench; small pastel bunting and windbells; one low stone fountain set BACK on the shop terrace, never on the front walking lane. Behind the square are soft wooded hills and pale blue summer sky with fluffy clouds. Architecture and tree silhouettes fit fully within the image. Terraced buildings and greenery occupy y=24%-75%; uninterrupted sandy walking lane lies horizontally at y=76%-94%; sparse foreground grasses at y=94%-100%; sky/hills at y=0%-24%. Do not slope or angle the lane into the distance. Keep the left and right 10% free of major props, houses, trunks and tall trees: only the same natural low meadow/hedge, matching hills, continuous road and foreground grass for joining to neighboring districts. Sun from upper left, warm ochre/cream and sage palette. No people or animals, no text, letters, logos, border, UI or readable sign. The district should feel generous and lived-in, not like a cramped diorama. Fully opaque panoramic background.
```

### 3. 河岸水车

```text
Reference image establishes the art style, scale, light and the lane's vertical placement for a long village map. Paint a NEW third district in the same original Studio Ghibli-inspired watercolor/gouache animation world: a wide 3:1 lateral 2D game background. A romantic riverside watermill with pale warm plaster and a mossy blue slate roof, a wooden water wheel, a clear narrow creek running behind a low stone retaining wall, a little arched footbridge IN THE MIDGROUND, soft reeds, white flowers, and a small vegetable garden with bean trellises. A dense green forest and far rolling hills stretch behind it, opening to luminous blue sky. A tall leafy willow grows behind the mill, away from the vertical edges. Keep the uninterrupted FRONT sandy walking lane completely flat and level, running through the full panorama at y=76%-94%, with sparse foreground grass y=94%-100%. Neither the creek nor bridge crosses this front lane. Architecture/garden terrace occupies y=24%-75%, sky/hills upper 0%-24%; same frontal facades with a little roof depth as the reference. Entire roofs and willow silhouette contained. BOTH the left and right 10% are quiet transition meadow/low hedge and continuous road, no buildings or trunks touching the side edges. Warm late-spring upper-left sunlight, soft sage greens and ochre creams, gentle natural watercolor texture, detailed clean HD illustration, no pixel art and no 3D. No people, no animals, no text or UI, no signs or logos, no border. A generous full-length scene, not a tiny diorama. Opaque background.
```

### 4. 邮差少女

```text
The reference is the world this character lives in; match its warm hand-painted Ghibli-inspired watercolor animation style, sage/ochre palette, clean thin cel lines, matte gouache fills, subtle painted shading, no pixel art, no photorealism or 3D. Generate ONE ORIGINAL GAME CHARACTER ONLY on a perfectly flat solid magenta #FF00FF background. A cheerful young adult countryside courier woman with short dark-brown bob hair, a simple ochre-yellow capelet over a pale cream shirt, a dark teal knee-length skirt, short brown walking boots and a warm red-brown leather satchel worn across the body. No hat, no long hair, no weapon. FULL BODY STRICT RIGHT-FACING SIDE PROFILE, both head and body face screen right; natural MID-STEP walking stance with the near foot forward and far foot back, arms relaxed, capelet compact near the shoulders and satchel visible. Entire feet, hands and costume are visible, no limb cropped. One figure centered, standing height around 75% of a square image, generous empty magenta margins all around, especially in front and behind the feet. No ground, no shadows, no floor oval, no scenery, no text, no second character, no motion marks. Do not put magenta in the character. Anatomically consistent two arms and two legs, readable natural silhouette, charming classic hand-drawn animated feature character design. This is an original character.
```

### 5. 白狐伙伴

```text
Use the reference landscape only for warm hand-painted color and lighting style. Create ONE original small fox companion game sprite in a Studio Ghibli-inspired watercolor/cel-animation style: pale ivory fur, warm cream shaded underside, tiny brown paws, charcoal nose, small lively dark eyes, large fluffy cream tail with a soft caramel tip and one plain sage-green neck scarf. A believable cute quadruped fox, no human anatomy, four legs, no hats, no shoes. FULL BODY STRICT RIGHT-FACING SIDE PROFILE in a mild natural walking mid-step, face and body facing screen right. Entire tail, ears and all paws inside the frame. Centered in a square image with plenty of flat empty margin; fox fills about 65% of width and 45% of height. Clean matte painted shapes with thin brown cel lines, soft painterly shading, no pixel art, no realistic fur strands, no 3D. Perfectly flat solid magenta #FF00FF background, no shadow, no floor, no grass, no scenery, no text or UI, no extra fox, no detached effects; magenta is absent from the fox. This is a new original creature.
```

### 6. 三名 NPC 角色图

```text
Reference image defines the scene art style. Create a horizontal THREE-COLUMN character asset sheet, approximately 3:1 aspect ratio, exactly three DISTINCT original village NPCs, one complete full-body NPC centered in each equal-width invisible cell. Warm original Ghibli-inspired hand-drawn watercolor/cel style, soft cream/ochre/sage tones and thin brown lines, matte painted shading, matching this sunlit village; no pixel art, no photorealism, no 3D. LEFT: a friendly middle-aged gardener woman with a simple straw hat, sage cardigan and warm brown skirt, holding a small pale-blue watering can close to her side; standing at a gentle three-quarter angle facing screen right. CENTER: a cheerful sturdy baker woman with short auburn hair, rolled cream sleeves, warm rust skirt and blue apron, holding a basket of bread close to her body; three-quarter view slightly toward the viewer. RIGHT: a kind silver-haired old man with a short soft beard, round glasses, muted blue vest and brown trousers, standing relaxed and playing a little wooden flute held close to the chest; three-quarter view facing slightly left. Keep feet on the SAME baseline, similar believable adult scale, each figure around 70% of cell height with safe margin on all sides. Entire straw hat, hands, watering can, basket and feet inside their OWN cell; no item crosses a cell boundary; props attached to hands, no disconnected items. A perfectly flat solid magenta #FF00FF background covers ALL empty areas. No ground, no shadows, no stools, no floor, no visible dividers or grid, no cell labels, no words, no UI, no extra people, no logos; magenta absent from the costumes. Render the three characters as separate reusable sprites, not as a scene.
```

### 7. 前景野花与蕨类

```text
Use reference image as a palette and painting style guide. Create an isolated low foreground verge of wildflowers and ferns for a scrolling 2D game, wide horizontal roughly 3:1 image, genuine transparent background. An irregular shallow cluster of graceful dark sage-green fern leaves, slender grass stems, small pale cream daisies, a few lavender-blue wildflowers and three mossy little pebbles. Original Ghibli-inspired hand-painted gouache/watercolor animation style, clean soft botanical silhouettes, upper-left late-afternoon light, natural brush details but no grain noise, no pixel art and no 3D. All roots meet a loosely horizontal base along the lower portion; foliage is LOW, a little uneven, not a huge bush or tree. Whole plant silhouettes and pebble edges visible, with transparent margin at left and right, around top and bottom. No soil slab, no opaque floor, no landscape, no people or creatures, no text, no panel, no cast shadow. The asset is foreground decoration, intended to partly frame a sandy lane without covering characters.
```

## 四、实际使用的 NPC 动作提示词

每段分别配合对应人物画布使用，画布同时提供给首帧和末帧。

### 园丁浇花

```text
Animate the SAME gardener woman from this character image in a single short forward looping performance. Locked camera and fixed framing; no zoom, pan, drift or changes of size. Preserve her straw hat, sage cardigan, cream apron, brown skirt, pale blue watering can, face, hands and painted cel/watercolor style exactly. Her feet stay planted at the same pixels throughout. She gently lifts and tips the watering can forward, pours a clearly visible thin sparkling pale-blue stream toward flowers just in front of her feet, with a few little water droplets, then returns the can to the exact initial pose. Her head looks down naturally toward the pouring water and her upper body leans only slightly. The pour is the main readable motion. Do not generate any plants, flowerpots, scenery, ground or floor: the receiving flowers will be supplied by the game background. All water stays inside this frame and above the foot baseline, and disappears naturally before the last frame. Complete one gentle watering gesture over four seconds and return smoothly to the attached last frame. Keep two arms and two hands consistent, can handle attached to the same hand, no extra limbs, no floating can. Perfectly flat pure magenta background across the whole frame, no gradient, shadow, checkerboard, text, labels or camera motion. Only the character and her local water effect animate. Natural smooth fluid motion, avoid held drawings and abrupt changes.
```

### 面包师挥手

```text
Animate the SAME friendly baker woman in a short forward looping game sprite performance. Camera absolutely locked with no zoom, drift or reframing; preserve her face, auburn hair and kerchief, cream sleeves, blue apron, rust skirt, bread basket and the watercolor/cel style. Feet remain planted, body size and position fixed. She supports the bread basket securely against her waist with one arm, lifts her free hand to shoulder height and gives two clear friendly hand waves as if greeting a customer and offering fresh bread; she smiles and leans forward just a little, then lowers the hand and returns to the exact original basket-holding pose shown by the last frame. One complete natural four-second gesture, smoothly cyclic. Keep every loaf in the basket, no disappearing basket, no growing hands, no extra arms or fingers, no floating props. Keep the wave below or beside her head so it remains fully contained in the padded image. Do not generate customers, stalls, counter, ground, floor, scenery or symbols. Pure perfectly flat magenta chroma background. No shadows, text, grid, camera motion or new decorations. Smooth fluid intermediate motion rather than held poses.
```

### 老人吹笛与音符

```text
Animate the SAME elderly flute player from this image, preserving his exact silver hair, beard, glasses, cream shirt, blue vest, brown trousers, little satchel and wooden flute, and the same warm painted animation style. Locked camera, fixed scale and fixed body position. Both feet stay planted. He keeps playing the flute at his lips with both hands, gently sways his shoulders and rocks/nods his head a few degrees with the music; his eyelids close in enjoyment and open again, fingers make small believable movements without ever detaching from the flute. A complete relaxed four-second cyclic performance, returning smoothly to the exact initial pose in the attached closing image. Two or three SMALL warm-golden hand-drawn music-note symbols emerge just past the flute tip, drift slowly upward a short distance, and fade away. These are local playful note illustrations, not words; they must be visible but modest, remain within the empty padded area and close to the flute, and disappear before the final frame. The note effect is explicitly requested. Do not generate a bridge, floor, stage, scenery, other people, text, labels or shadows. Keep the background perfectly flat pure magenta with no texture or gradient. Keep hands, flute and face anatomically coherent; no extra fingers or limbs. Smooth fluid motion, no abrupt head movements or camera drift.
```

## 五、实际工具链

内置图像生成 → Grok 订阅动作视频 → sprite-gen 抠像与循环 → 本地 RIFE 补帧 → 场景合成 → 本地原创配乐 → FFmpeg 音视频合成 → 静态网页 → GitHub 公开仓库与 GitHub Pages。

复现时按自己的生成结果检查几何位置、动作周期、插帧质量和网页播放。

## 六、环境动态更新（2026-10-12）

后续加入了晾衣微风、柳树垂枝与溪流反光三个局部循环，沿用原地图、人物和音乐。

1. 从原地图裁出三个区域，使用 Grok 订阅 `grok-imagine-video-1.5` 生成 4 秒、720p 的固定镜头视频，并用同一张裁剪图约束首尾。
2. 晾衣与溪流使用首段生成；柳枝首段变化偏轻，补生成了一段更清楚的轻风摆动后采用。
3. 用 FFmpeg 解码不透明场景视频并恢复原裁剪分辨率。以局部遮罩保留衣服、水面和枝梢区域，遮罩外直接使用原图；河水遮罩避开岸边与石头，树干与桥保持原像素。
4. 循环取样调用 sprite-gen 的 `pinned_cycle`，保留 96 个原始帧、4 秒周期。场景区域没有洋红底，因此没有使用人物的 chroma 抠像路线。
5. 调用既有 RIFE v4.6 重采样与质量保护，每个环境循环输出 192 帧、48 fps，周期仍为 4 秒。三个循环各实际保留 96 个 RIFE 中间帧。
6. 为不透明场景视频手工编写了局部遮罩与色调匹配，再接入 sprite-gen 场景渲染。检查确认遮罩外像素与原图逐帧完全一致。
7. 完整游览仍为 42 秒、1280 × 720、30 fps，保留原背景音乐；网页加入“晾衣微风”和“柳枝与溪流”时间跳转按钮。

### 环境视频原始提示词

#### 晾衣微风

```text
Animate this exact painted village crop with a gentle summer breeze. The camera is completely locked: preserve all pixel positions, framing, perspective, house, roof, fence posts, clothesline, flowers and foliage. Only the THREE main cloth pieces on the clothesline move: the blue-and-white checked cloth on the left, the large white sheet in the middle, and the cream cloth on the right. Their upper edges stay firmly attached to the same line and pegs. Their lower halves softly billow and flutter sideways a small distance, each with a slightly different phase, while retaining exactly the same fabric colors and pattern. A relaxed light breeze, not a storm: about a few source-image pixels of displacement at the hem, with graceful soft folds. Complete one smooth four-second wind cycle and return precisely to the supplied closing image. Keep the little blue towels and the surroundings still. Preserve the original delicate hand-painted watercolor/cel background style, sharpness, lighting and color. No camera motion, zoom, parallax, focus breathing, color shifts, changing architecture, new clothes, flying objects, people, animals, text or particles. This is an environmental animation plate for compositing into the original map.
```

#### 柳枝微风（采用的第二段）

```text
Bring the willow tree in this painted scene to life with a CLEARLY VISIBLE gentle breeze. The long hanging leafy twig sprays on BOTH outer sides and at the bottom of the crown swing slowly sideways, bend softly, and flutter throughout the shot. Their tips move about eight to twelve pixels at the original reference scale, then return. The leaves remain attached to their own twigs. This must show real flowing movement of the hanging branches, not just a still image or falling particles. The breeze builds gradually, the flexible twigs lean one way then gently settle back, completing one continuous four-second cycle that closes on the attached final image. The trunk and strong structural branches stay rooted and steady. Locked camera. Keep the original hand-painted watercolor/gouache style and the recognizable shapes of the tree, the mill and the village. Keep lighting and colors stable. No new objects, flying leaves, birds, particles, camera motion or zoom. Only wind-driven leafy twig motion.
```

#### 溪流水面

```text
Animate ONLY the CREEK WATER SURFACE underneath and downstream of the stone bridge in this exact painted scene. Completely locked camera and unchanged composition, scale, lighting and colors. The bridge, river banks, rocks, reeds, grass, buildings, water wheel, fences and tree trunk remain perfectly still and retain their exact positions and shapes. Create gentle continuous downstream flow toward the foreground and slightly toward screen left: small painted ripples and warm pale-blue/cream reflections glide along the water surface and curl around the fixed stones. Keep the waterline fixed and the flow shallow, natural and quiet. Preserve the watercolor/gouache texture; no photorealistic or glossy CGI water. No rising water, flooding, moving rocks, changing banks, exaggerated waves, splashes over the shore, mist or new objects. Produce a smoothly cyclic four-second reflection pattern, returning to the supplied final still without a visible pause or snap. Keep all water inside the existing creek. No camera pan, zoom, parallax, exposure flicker, new people, animals, text or particles. The clip is an environmental water plate for masked compositing onto the original map.
```

## 七、旗帜、喷泉、大树与生活气息（2026-10-12）

按照截图定位集市旗绳、喷泉和大树，新增以下效果，并保留前一版衣服、柳枝、溪流、人物与音乐。

1. 三角旗首段将旗尖翻到绳上方，重新生成并采用保持旗面下垂、仅轻柔横摆的第二段。三角旗、喷泉与大树枝梢分别从原地图裁图，用 Grok 订阅生成固定镜头、首尾约束的 4 秒片段。以局部遮罩保护旗绳、喷泉石柱、树干、粗枝和建筑。
2. 使用内置 imagegen 生成透明的蝶蜂组合、轻烟与一片黄绿色叶子。蝶蜂和炊烟再通过 Grok 订阅生成动作，sprite-gen 抠像与循环处理。炊烟初次抠像出现紫边，改用引擎的 full spill 与 palette 去污染处理，拒绝初次结果。
3. 五段新视频循环都是 96 个源帧、4 秒；RIFE 输出 192 帧、48 fps。旗帜、喷泉、大树、炊烟各保留 96 个中间帧；蝶蜂保留 90 个，6 个补帧提案被引擎质量保护拒绝。
4. 三片小落叶复用同一张生成的透明叶片，以确定性曲线路径、旋转和渐隐直接采样到 48 fps。这里没有用 RIFE，也没有重新绘制地图。
5. 炊烟叠在三个准确的烟囱口，使用错开的循环相位与轻透明度。三组蝶蜂分布在不同街区的前景花簇，每组两只蝴蝶、一只蜜蜂，随前景使用同样的视差。
6. 新增网页时间跳转按钮：旗帜与喷泉、大树与落叶、炊烟与花间飞舞。成品仍为 42 秒、1280 × 720、30 fps，沿用原配乐；可拖动的大地图仍为静态。

### 三角旗动作提示词

```text
Animate the SAME hanging triangular pennant flags on this curved rope with a VERY SOFT sideways breeze. At EVERY moment each triangle must remain HANGING DOWN BELOW its own section of rope. Its top edge stays attached in its original place; its lower point stays below the rope and gently shifts sideways only THREE to FIVE original-image pixels. Small relaxed fabric rippling and tiny bends, slightly staggered between flags. NEVER lift a flag above the line, never invert a triangle upward, never flip over, never stretch or change its size. This is a calm sunny day. Keep exactly the original flag colors and triangles. The rope, roof, foliage, fountain, lamp and entire background stay perfectly stationary. One smooth small-amplitude four-second cycle returning to the provided closing frame. Locked camera, unchanged framing, perspective, watercolor/gouache style, exposure and colors. No wind gusts, violent flapping, camera movement, new objects, people or particles.
```

### 喷泉动作提示词

```text
Animate the flowing water of this EXACT little painted village fountain. The stone finial, tiers, central pillar, circular basin and every piece of architecture remain completely rigid at their existing pixel positions. Thin graceful pale blue and creamy-white water jets continuously arc from the upper bowl down into the lower basin. Small droplets travel DOWN along the existing streams; delicate ripples shimmer INSIDE the basin and small modest splashes stay within its rim. Clearly readable continuous flowing water with a quiet summer mood, not a frozen water still. Retain exactly the current water levels and stream positions, hand-painted watercolor/gouache style and stable colors. Camera entirely locked, no pan or zoom, no scenery movement or focus breathing. Four-second cyclic water pattern returning smoothly to the pinned final frame. No moving stones, new jets, flooding, mist, bubbles covering the scene, text or people.
```

### 大树枝梢动作提示词

```text
Animate the leafy crown and slender flexible branch tips of this exact grand village tree in a gentle summer breeze. The clusters of green and yellow-green leaves sway softly back and forth with a clearly readable 5 to 9 original-pixel movement. Flexible small outer twigs bend naturally; individual leaves flutter on them with slightly staggered timing. The main trunk, big woody structural branches and ALL buildings, flags, fountain, bench, stone walls and surroundings stay perfectly fixed. Preserve the original tree silhouette, leaf colors, dappled watercolor/gouache brushwork, sunlight and contrast. Complete a graceful four-second wind cycle and end exactly on the attached still. Camera absolutely locked, no zoom, no parallax or whole-image drift. Do not add flying leaves in this plate: a few detached falling leaves will be composited separately. No changing tree species, missing branches, new foliage, animals, birds, text, storm or particles.
```

### 炊烟动作提示词

```text
Animate this SAME thin delicate hand-painted cooking-smoke plume. A continuous stream of very light cream-white translucent smoke emerges from the EXACT fixed tiny lower tip, rises slowly, curls gently to the right, and gradually dissolves near the top. Soft wisps roll through the shape, replenishing from below; clearly visible gentle upward flow rather than a rigid image sliding or pulsing. Preserve its slender scale, light airy watercolor brushwork and subtle soft edges. No black smoke, flames, explosion or broad cloud. The base stays fixed at the same pixel and no smoke crosses frame borders. Camera completely locked. Four-second continuous cycle returning smoothly to the supplied last frame; no snap or sudden opacity change. Entire empty background stays perfectly flat pure magenta #FF00FF, no gradient. No chimney, house, scenery, floor, shadow, text or new objects.
```

### 蝶蜂飞舞动作提示词

```text
Animate the SAME two little painted butterflies and SAME honeybee from this image. Exactly three insects, retaining their colors, original sizes, wing patterns and loose grouping. The cream and blue butterflies continuously open and close their wings naturally while drifting slowly along two small curved hovering paths with different phases. The bee quickly flutters its tiny wings and makes a small gentle figure-eight patrol. Keep each insect moving within its own broad empty patch, without colliding, changing species, disappearing or multiplying. Small local travel, less than 25 pixels at the reference image scale, above garden flowers that will be supplied later. Smooth real wing articulation, not rigid whole-picture bobbing. Preserve the delicate watercolor/gouache style. Camera locked, four-second cyclic flight returning smoothly to the supplied closing image. ALL empty space stays perfectly flat solid pure magenta #FF00FF. No shadows, floor, flowers, grass, trails, particles, labels, extra insects or new objects.
```

### 蝶蜂初始素材提示词（内置 imagegen）

```text
Use case: stylized-concept. Asset type: one reusable ambient garden insect overlay for a hand-painted 2D village animation. Create exactly TWO small original butterflies and ONE small honeybee flying in a loose horizontal grouping, with ample genuine transparent empty space between them and on every outer edge. Upper-left a pale cream butterfly with soft ochre edging and thin brown body, lower-right a muted sky-blue butterfly, near middle-right a little honey-yellow bee with tiny dark brown stripes and pale translucent wings. Their wings are visible in a mid-flutter pose; friendly natural insects, no faces. Match warm gouache and watercolor cel-animation backgrounds, delicate painted shapes, subtle natural shading and thin brown lines. Entire insects visible and each takes only about 12 percent of the full image width; leave plenty of empty flight room around the group. Horizontal composition approximately 2:1. Genuine transparent background, no flowers, branches, grass, scenery, ground, cast shadows, typography, grid, panels, labels, photorealism or 3D. The three insects together form a single ambient effect that will be animated over foreground flowers.
```

### 炊烟初始素材提示词（内置 imagegen）

```text
Use case: stylized-concept. Asset type: one isolated reusable chimney-smoke plume for a warm hand-painted village game. A single narrow, delicate cream-white and very pale cool gray plume of cooking smoke rises gracefully from a tiny point near the lower center, curls gently toward upper right, and thins into soft wispy strands. Painterly gouache/watercolor animation style with delicate translucent feathered edges and calm flowing contours. One connected elegant wispy plume, light airy domestic cooking smoke, not a broad cloud or steam explosion. Entire plume inside the image with generous genuine transparent margin on every side; plume occupies about 45 percent of width and 70 percent of height in a portrait composition. Smoke only. Genuine transparent background, NO chimney, house, fire, soot, black smoke, scene, ground, shadow, text, checkerboard or grid. Subtle modest smoke intended to be scaled down over distant rooftops.
```

### 落叶初始素材提示词（内置 imagegen）

```text
Use case: stylized-concept. Asset type: one tiny falling-leaf sprite for a hand-painted summer village tree. Paint a SINGLE fresh yellow-green small lobed plane-tree leaf, slightly angled, with a tiny warm brown stem and simple delicate veins, matching soft gouache and watercolor cel-animation background art. Natural clean readable silhouette, subtle warm sunlight and muted sage shadows, no photorealism. Entire leaf centered, occupying about half of the square image with generous transparent margin. Genuine transparent background, leaf only, no tree, branch, ground, other leaves, shadows, text, grid or 3D. This one leaf will be scaled very small and rotated along a gentle falling path.
```

## 八、水车流水（2026-10-12）

从原图裁出水车与底部小水道，以 Grok 订阅生成 4 秒固定镜头的水流片段。木质水车与石墙固定，薄水帘沿原轮缘和叶片落下，底部有小水花，再流入溪流。以固定局部遮罩保持水流以外的原像素，sprite-gen 取首尾约束循环并使用本地 RIFE v4.6 补帧。实测循环为 96 个原始帧，补帧后 192 帧、48 fps、4 秒，保留 96 个 RIFE 中间帧；遮罩外像素与原图一致。沿用 42 秒游览、既有动画和配乐，网页新增“水车流水”按钮。

### 实际水流视频提示词

```text
Animate ONLY the cascading water on this exact painted village waterwheel. A thin, continuous pale-blue and cream-white stream pours from the existing top inlet onto the outer rim, flows DOWN over the existing wooden paddles on the RIGHT side, and falls naturally into the small pool below. Visible moving highlights, slender ribbons and a few tiny droplets travel downward along the existing curved water path. At the foot, add delicate small splashes within the existing pool; the small lower cascade continues into the creek with modest ripples. Preserve the original watercourse, water levels and shorelines. The wooden wheel, spokes, hub, paddles, stone walls, roof, greenery, flowers and bridge must all remain rigidly fixed in their exact pixel positions and keep their original shapes. This plate animates the WATER only. Quiet gentle domestic mill flow, not a flood or a foaming torrent. Keep the original warm hand-painted gouache/watercolor texture, stable sunlight, colors, contrast and framing. Camera completely locked, no zoom, pan, whole-image motion, new objects, mist, text or people. Produce a continuous four-second water-flow cycle closing smoothly on the attached last frame, with no freeze or snap. Small readable changes in the moving water rather than changing the stone or wood.
```
