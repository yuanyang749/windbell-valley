# 可复用提示词模板

[手册](handbook.md) · [工具配方](tool-recipes.md)

模板中的 `{变量}` 需要替换为当前项目的真实要求后再提交。模型参数能够明确表达的方向、时长、背景键等，在选项与提示词间保持一致；使用工具自动补充方向句时，避免重复或互相矛盾。

这些模板是制作起点，不保证一次生成成功。原案例实际提交的提示词见公开仓库中的 [PROMPT.md](https://github.com/yuanyang749/windbell-valley/blob/main/PROMPT.md)。

## 1. 整体任务简报

```text
请为当前项目制作二维动画场景。
交付目标：{预渲染视频展示 / 可交互游戏 / 实时场景展示}。
请先读取项目说明和现有组件，复用已有地图、渲染器与工具。

画面风格：{画材、色调、线条、视角、光照}。
地图与行走区域：{尺寸、坐标单位、道路/支撑面、相机范围}。
角色与动作：{对象身份、动作顺序、道具、方向}。
环境动态：{具体区域、允许运动部位、固定部位}。
声音：{音乐方向、声源位置、需要的环境声}。
素材与模型选择：{已有素材、图片/视频提供方、当前登录方式}。
允许的执行范围：{本地处理、已授权生成、发布范围、成本或重试约束}。

先交付一个本地可运行切片，验证后逐步扩展。
保存参考图、提示词、实际调用报告、裁剪框、锚点、遮罩、帧时长与验收证据。
新地图重新标定坐标；保留动作周期；检查中间帧与循环衔接。
按目标分别完成视频网页验收或真实游戏运行时验收。
```

## 2. 分区背景

输入：已采用相邻区域的风格参考图，或明确的统一画面规范。

```text
Create an original {aspect ratio} panoramic 2D environment for {project}.
Match the reference's {painting medium, palette, light direction, camera angle,
building scale and road height}. This is the {district purpose} section.
Include {specific buildings, vegetation and landscape}.
Keep the traversable lane at {vertical band} continuously across the image,
with {perspective and slope requirements}. Reserve {areas} for characters,
support surfaces and foreground occlusion.
Leave the joining edges as {low-complexity transition areas}.
Fully opaque environment. No characters, animals, interface, captions or logos
unless explicitly required. Keep entire important silhouettes within frame.
```

## 3. 角色动作循环

输入：人物动作画布。需要色键时，画布为已验证的纯色；手脚和道具有动作余量。

```text
Animate this EXACT {character identity and design}.
Locked camera. Keep the same canvas framing, body scale, identity, clothes,
prop design and {support points}. Preserve the reference's {visual style}.

Perform one readable complete action over {duration} seconds:
{ordered action phases, which hand holds which prop, direction and amplitude}.
The {other hand / feet / fixed prop} stays {explicit constraint}.
Return naturally to the supplied closing pose without a pause or snap.
{Requested attached effects: where they start, their path and disappearance}.

No camera pan or zoom, framing drift, extra limbs, changing prop count,
unrequested scenery or text. Keep every required part within the canvas.
{Background requirements consistent with the selected video route}.
```

替换动作段的实例：

- 面包师：一手稳托篮子，另一手抬到肩旁挥两次，回到起始持篮姿态。
- 园丁：看向花，倾壶产生细水流，再扶正水壶；水流不改变人物的支撑面。
- 吹笛者：双手持续持笛、笛子贴嘴；头肩轻摆，少量音符从笛口附近飘起并消失。

走路和跑步单独描述真实步态，并使用工具对应的周期和接触处理，不直接套用“脚不移动”的待机约束。

## 4. 通用背景局部动画

输入：最终地图上的原始裁剪，而非人物色键画布。

```text
Animate ONLY {moving region} in this exact reference crop.
Locked camera and unchanged composition, scale, lighting and painted style.
{Moving elements} perform {direction, amplitude, speed and phase}.
{Fixed structures, shoreline, attachment points and foreground props}
remain stationary in their original pixel positions and keep their shapes.
Keep all motion inside {allowed region}, with room for the intended amplitude.
Produce a continuous {duration}-second cycle returning to the supplied closing
image without a visible pause, reverse or snap. No new objects, camera motion,
exposure flicker, text or unrequested effects.
```

具体动作段：

| 对象 | 允许的运动 | 固定内容 |
| --- | --- | --- |
| 河流 | 波纹、反光向下游移动，绕过现有石块 | 水位、岸线、桥、石块 |
| 喷泉 | 水线向下流，盆内小水花和波纹 | 石质喷口、柱体、盆沿 |
| 三角旗 | 旗面轻摆；旗尖始终在绳下 | 绳索、旗顶挂点、两端支架 |
| 晾衣 | 下摆和袖口轻摆 | 绳、夹子、衣物上端 |
| 大树 | 外围叶簇、细枝轻摆 | 树干、粗枝、主轮廓和近侧遮挡 |
| 柳树 | 垂枝末端小幅自然摆动 | 主干、岸边、建筑 |

落叶、烟雾和昆虫可使用独立透明/色键素材或程序粒子；根据实际方式记录来源。不要要求背景视频同时生成所有分离效果。

## 5. 水车刚性转动与水流

输入：清晰可见轮辐、轴心和前景支撑的局部参考图。

```text
Animate this EXACT wooden waterwheel as a rigid mechanical wheel at the same
oblique perspective. The wheel turns steadily {visible rotation direction};
the paddles on {side} move {direction} along the falling water.
The center stays at the same pixel. Spokes, rims and paddles rotate together
with consistent count, thickness, material and elliptical perspective.
Keep the stationary shaft/support, stone walls, roof, plants and foreground
stones fixed. No bending, melting, spoke replacement, hub drift, size breathing,
wobble, reverse, pause or rebound.
The existing narrow water sheet continuously descends along {water path},
with a few small splashes inside the existing lower pool.
Locked camera, unchanged painted style, colors and light.
Create a {duration}-second continuous cycle returning to the closing image.
No new scenery, flood, mist, people, text or camera movement.
```

如果项目需要精确 RPM/转角，额外写清要求并实测；无法达到时按现有引擎能力考虑分层旋转或其他确定性方案，不能仅凭提示词宣布实现精确机械运动。

## 6. 炊烟、昆虫等独立效果

输入：风格一致的独立效果参考图，画布预留完整运动范围。

```text
Animate these exact {effect identities and count} in a locked canvas.
{Smoke: starts at the fixed source, rises slowly, curls and fades.}
{Insects: flutter wings, hover and travel along small irregular paths.}
Keep scale, identity and {fixed source positions} stable.
All required motion stays inside the frame. Preserve {style}.
Create a {duration}-second loop with a natural closing state.
No extra particles or insects, scenery, camera movement or text.
Use {background treatment appropriate to the chosen extraction route}.
```

## 7. 独立环境声

输入：可提供对应环境参考图。若使用视频模型生成音频，视频可只用于抽取声音。

```text
AUDIO IS THE MAIN DELIVERABLE: clean natural recording-style ambience of
{soft leaves in a mild breeze / a small courtyard fountain / a shallow stream
and very faint wooden wheel creaks}. Peaceful {setting}, restrained intensity,
continuous detailed texture throughout {duration} seconds.
No music, melody, percussion, speech, voices, clipping, electronic hum,
musical introduction or ending. No storm, roaring waterfall or dramatic impact.
Visuals: locked camera, preserve the supplied reference scene.
```

保存音轨并试听，检查实际是否有多余音乐、人声或噪声。生成的录音风格不等于现场录音。
