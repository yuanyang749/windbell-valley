# 工具配方与执行顺序

[手册](handbook.md) · [坑点记录](pitfalls.md)

命令参数依据本地 `sprite-gen 2.42.0` 帮助核对。生成服务、工具选项与模型能力会变化；在新环境先读当前帮助和对应工具说明。以下素材路径是目录示例，需先准备输入。文档中的生成/安装/发布命令不构成执行授权。

## 1. 使用已安装工具的解释器

示例采用 Codex 常见安装位置；若实际位置不同，调整变量：

```sh
task_sprite_root="$HOME/.codex/skills/sprite-gen"
task_sprite_cli="$task_sprite_root/.venv/bin/sprite-gen"
task_scene_skill="$HOME/.codex/skills/animated-2d-scene-skill"
"$task_sprite_cli" --help
"$task_sprite_cli" video --help
"$task_sprite_cli" video-frames --help
"$task_sprite_cli" video-loop --help
ffmpeg -version
```

技能还在仓库中时，`task_scene_skill` 改为该目录的实际路径。RIFE 使用已安装的本地模型；需要安装时使用 `sprite-gen rife install` 并遵循项目授权，不在本包重复下载或分发权重。

## 2. 准备角色动作画布

前提：`source/npc/base-keyed.png` 已正确抠出并合成到均匀纯色，动作需要向前与头顶留空间。

```sh
mkdir -p working/npc
"$task_sprite_cli" video-canvas \
  --still source/npc/base-keyed.png \
  --out working/npc/canvas.png \
  --state attack --shape wide --key magenta \
  --report working/npc/canvas.report.json
```

这里借用工具的宽动作画布，动作本身由提示词定义；不是把 NPC 动作标成战斗。按当前角色选择形状和留白，检查输出后再生成视频。完整背景裁剪跳过此色键画布步骤。

## 3. 订阅路线生成短视频

前提：当前项目已授权本次生成，Grok 订阅已登录，参考图与提示词均已准备。用同一参考图作首末帧仅适用于该动作应回到原姿态的情况。

```sh
mkdir -p source/npc
env -u XAI_API_KEY "$task_sprite_cli" video \
  --image working/npc/canvas.png \
  --last-frame working/npc/canvas.png \
  --prompt-file prompts/npc-motion.txt \
  --out source/npc/clip.mp4 \
  --report source/npc/clip.report.json \
  --duration 4 --resolution 720p \
  --model grok-imagine-video-1.5 --no-audio
```

`env -u XAI_API_KEY` 只在这一次子进程中排除 API Key，示范案例选择的订阅路线；核对报告 `auth_source`，不把登录失败转成收费 API。其他项目明确选择 API 时按其要求调整。模型和时长是案例选项，先核对当前可用能力。

背景动画用原图裁剪替换 `--image` 和 `--last-frame`。独立环境音使用相应提示词和 `--audio`，后续抽取音轨；不要把带音频选项误用在只需静默精灵的任务。

## 4. 角色抠像与取循环

```sh
"$task_sprite_cli" video-frames \
  --clip source/npc/clip.mp4 \
  --reference working/npc/canvas.png \
  --key magenta --spill auto --decontam palette \
  --out-dir working/npc/extracted
```

阅读产生的帧报告，使用它的实际 fps。下面的 `24` 仅为命令示例，应替换为该报告值：

```sh
task_native_fps=24
"$task_sprite_cli" video-loop \
  --frames-dir working/npc/extracted/keyed \
  --out-dir working/npc/loop \
  --fps "$task_native_fps" --state idle \
  --cycle pinned --anchor none
```

`pinned` 适用于已经固定首末图的完整循环；走路/跑步使用工具对应的周期、接触和锚点处理。抠像、选帧输出都要检查。该命令不等于对所有帧做两倍密度的 RIFE；循环修复与整体重采样是不同步骤。

## 5. 不透明环境视频处理

这一条路线不使用 `video-frames` 的色键提取。按 [手册](handbook.md) 准备原裁剪、动态遮罩和保护区，然后：

1. 用 FFmpeg 解码并还原至原裁剪尺寸，使用 `ffprobe` 确认实际 fps/帧数。
2. 复用 `sprite-gen.video.loop.distance_matrix` 与 `pinned_cycle` 选择周期，不另写检测器。
3. 输出同尺寸 PNG、每帧原生时长和固定局部锚点。羽化和保护区是项目作者决定的数据，需要目视和像素检查。
4. 使用包内 RIFE 脚本并恢复同一遮罩；再合回原地图验证。

不要复制旧案例的裁剪框和遮罩坐标。仅当固定区域足够可靠时才做曝光匹配。当前安装版本的底层 API 可在工具源码中核对。

### 固定首末帧环境板的选周期配方

前提：源视频是固定帧率；`working/creek/masked` 已有全部按顺序、零填充命名的 RGBA PNG，与原裁剪同尺寸、使用同一遮罩；源视频开始和结束都应回到参考图。变帧率视频需要按实际时间戳处理，不套用以下帧数配方。

使用上述工具 Python 运行此配方，替换素材路径。引擎返回 `start`、`length`、`pin_error` 和 `pin_tolerance`；`pinned_cycle` 采用完整片段并去掉重复末帧，因此不能预先自行再删一次末帧。

本配方已对案例水车原片执行：193 张解码帧选出 192 帧，周期为 8 秒、原生 24 fps；它不包含遮罩绘制或源动作的目视验收。

```python
import json
import os
import subprocess
from pathlib import Path
from sprite_gen.video.loop import distance_matrix, pinned_cycle

clip = Path("source/creek/clip.mp4")
frames_dir = Path("working/creek/masked").resolve()
output = Path("working/creek/source").resolve()
if output.exists():
    raise FileExistsError("choose a new source output directory")
files = sorted(frames_dir.glob("frame-*.png"))
if len(files) < 3:
    raise ValueError("need the complete decoded pinned clip")
probe = json.loads(subprocess.check_output([
    "ffprobe", "-v", "error", "-show_streams", "-of", "json", str(clip)
]))
video = next(s for s in probe["streams"] if s["codec_type"] == "video")
numerator, denominator = map(int, video["avg_frame_rate"].split("/"))
fps = numerator / denominator
if fps <= 0:
    raise ValueError("invalid native frame rate")
if video.get("nb_frames", "").isdigit() and len(files) != int(video["nb_frames"]):
    raise ValueError("decoded frame count differs from the clip")
cycle = pinned_cycle(distance_matrix(files), seam_max=2.0)
if cycle["pin_error"] > cycle["pin_tolerance"]:
    raise ValueError("pinned ends did not close; inspect source and loop report")
selected = files[cycle["start"]:cycle["start"] + cycle["length"]]
records = [{"file": os.path.relpath(p, output), "duration": 1 / fps}
           for p in selected]
output.mkdir(parents=True, exist_ok=False)
(output / "loop.report.json").write_text(json.dumps({
    "clip": clip.name, "fps": fps, "cycle": cycle,
    "duration_seconds": len(selected) / fps
}, indent=2) + "\n", encoding="utf-8")
(output / "asset.json").write_text(json.dumps({
    "kind": "sprite-gen-asset", "version": 1,
    "anchor": [0, 0], "frames": records
}, indent=2) + "\n", encoding="utf-8")
```

`seam_max=2.0` 是本版本工具默认和案例使用值，不是任意素材的审美阈值。不要为通过检查自动放宽；报告通过后仍观看中间动作与连续循环。未固定端点的视频应使用工具适合该动作的其他周期路线。

### 外部帧描述示例

下面是 `sprite-gen-asset` 描述格式示例。两张帧图必须真实存在，路径相对该 JSON；这里的帧数仅用于说明结构：

```json
{
  "kind": "sprite-gen-asset",
  "version": 1,
  "anchor": [0, 0],
  "frames": [
    {"file": "frames/frame-000.png", "duration": 0.041666666666666664},
    {"file": "frames/frame-001.png", "duration": 0.041666666666666664}
  ]
}
```

角色把 `anchor` 改为对应画布内实际脚底；源帧已经选好完整周期，不重复加入闭合帧。

## 6. 保持时长的 RIFE 辅助脚本

前提：源资产已完成动作、循环和尺寸检查；脚本只接受等帧时长循环。输出目录必须尚未存在。

```sh
"$task_sprite_root/.venv/bin/python" \
  "$task_scene_skill/scripts/resample_asset.py" \
  --asset working/creek/source/asset.json \
  --out-dir working/creek/rife \
  --factor 2 --mask working/creek/mask.png
```

角色或没有固定环境遮罩的素材省略 `--mask`。

输出包含 PNG 帧、`asset.json` 和 `rife-report.json`。脚本调用引擎 `resample(..., between="auto")`，恢复原总时长和锚点，不把拒绝提案当作有效插帧。对于环境遮罩，仅接受同尺寸 `L` 模式 PNG，并要求源帧为不透明或已使用该固定遮罩；不能替代随人物变化的透明边缘。

脚本拒绝：既有输出目录、不等帧时长、遮罩尺寸/模式错误、与固定遮罩冲突的动态 alpha。缺少引擎或 RIFE 会明确报错，不下载模型，也不换解释器或提供方。

兼容性检查使用本地真实水车相位帧验证输出时长、锚点与固定遮罩，并检查错误输入和禁止覆盖行为；这不保证未来所有 `sprite-gen` 版本的内部接口兼容。

## 7. 合成与导出

已经写好当前工具支持的场景规范后：

```sh
"$task_sprite_cli" scene-render \
  --spec scene.json --out-dir render-new --formats mp4,png
```

场景规范由已安装工具说明定义，本包制作记录不是其替代。游戏资源优先使用工具已有图集与引擎导出路线；`compose-atlas` 需要合法的 component-row run，不能把任意帧目录直接传入。`export-aseprite` 需要已合成图集的清单。先核对 `--help` 和现有项目导入器，再决定所需转换。

### 检查视频和抽取环境声

```sh
ffprobe -v error -show_streams -show_format -of json render-new/scene.mp4
ffmpeg -hide_banner -nostdin -v error -i render-new/scene.mp4 -f null -
ffmpeg -hide_banner -nostdin -i source/ambience/clip.mp4 \
  -vn -ar 48000 -ac 2 source/ambience/raw.wav
```

抽取目标必须为新文件，先试听再制作循环。视频完整解码通过之后仍要检查实际画面和声音。

## 8. 浏览器与发布

```sh
npx --yes http-server@14.1.1 public -a 127.0.0.1 -p 8080 -c-1
```

这是案例验证过的预览服务选择，会按需获取 npm 包；使用当前项目已有服务同样可以。实际测试视频跳转与声音开关，必要时核验字节范围响应。对外发布以当前项目授权和部署平台为准。
