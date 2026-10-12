# Animated 2D Scene Skill · 二维动画场景制作

将风铃溪谷的制作过程、实际失败和修正方法沉淀为可阅读手册与 Codex Skill，供新的场景展示和游戏项目借鉴。

- [制作手册](references/handbook.md)：从素材规划到遮罩、补帧、声音、展示与游戏接入。
- [坑点记录](references/pitfalls.md)：症状、原因、处理方法和复查方式。
- [提示词模板](references/prompts.md)：地图、人物、流水、树枝、旗帜、水车和环境音。
- [工具配方](references/tool-recipes.md)：核对过的命令和 RIFE 辅助脚本。
- [风铃溪谷案例](references/windbell-valley.md)：实际参数、遮罩示意、验证结果与局限。
- [技能入口](SKILL.md)：给 AI 助手的按需执行指导。

## 已验证与待接入的部分

风铃溪谷完成了参考图动画、抠像、局部遮罩、RIFE、42 秒视频、原创音乐、环境声和 GitHub Pages 展示。网页播放预渲染视频，大地图是静态图片。

包内提供游戏接入合同和验收建议。没有附带通用游戏引擎，也没有把风铃溪谷改成可交互游戏。制作的新项目应在其运行时中验证这些接入步骤。

## 在新项目中使用

### 直接使用仓库中的技能文件

告诉支持文件读取的 AI 助手：

```text
请读取本仓库 animated-2d-scene-skill/SKILL.md，按它和当前项目说明制作二维动画场景。
本项目目标是可交互游戏（或：预渲染场景展示）。
先检查现有素材和工具，完成一个本地可运行切片，记录素材、提示词、参数和验收结果。
模型、风格、联网生成与发布范围以我在当前项目中的要求为准。
```

### 安装到 Codex 技能目录

仓库目录是分发包；复制到 Codex 技能目录后才能作为已安装技能发现。下面命令从仓库根目录运行，目标已存在时会停止，避免覆盖已有技能：

```sh
task_skill_root="${CODEX_HOME:-$HOME/.codex}/skills"
task_skill_target="$task_skill_root/animated-2d-scene-skill"
if [ -e "$task_skill_target" ]; then
  printf '%s\n' "目标已存在，请先核对已有技能：$task_skill_target"
else
  mkdir -p "$task_skill_root"
  cp -R animated-2d-scene-skill "$task_skill_target"
fi
```

在识别到新技能的 Codex 会话中使用：

```text
$animated-2d-scene-skill
为当前游戏制作一段河流环境循环，复用已有地图和运行时。
先完成本地素材及可玩切片；生成、发布等动作遵循本项目已有授权。
```

## 工具与兼容性

原案例使用 `sprite-gen 2.42.0`、本地 RIFE v4.6、FFmpeg、Codex 内置生图以及 Grok 订阅登录；原创音乐使用 macOS 乐器声库。它们是案例环境，不是所有新项目的强制选择。

`scripts/resample_asset.py` 依赖安装了 `sprite-gen`、Pillow 和 RIFE 的 Python 环境。执行前核对当前工具版本，读取 [工具配方](references/tool-recipes.md)。

## 维护方式

新项目遇到实际问题时，补充失败证据、修正和验收结果，再更新相应指导。新坐标、转速、画布大小和音量属于具体项目参数；不要直接覆盖通用建议。

新技能的基线评估发现旧制作提示词缺少实时接入、坐标合同和明确时间规则，因此新增了对应章节。技能结构与本地资源链接、辅助脚本行为和模拟项目决策应一并验证；这些检查不等于已验证所有引擎或生成模型。

## 本版验证记录（2026-10-12）

- 技能结构、UI 元数据、包内资源链接与代码示例语法检查通过；包内没有私人绝对路径。
- 环境选周期配方对实际水车原片执行：193 张解码帧选出 192 帧，24 fps，8 秒。
- RIFE 辅助脚本使用四张实际水车相位帧组成的小样本：4→8 帧，24→48 fps，时长、锚点和固定遮罩保留。
- 辅助脚本拒绝已有输出、不等帧时长和尺寸错误的遮罩。
- 只读模拟游戏任务验证了路线选择和执行计划；未据此宣称游戏运行时已经完成。

## 许可与来源

本目录中的技能、手册、辅助脚本和案例示意图采用 [MIT License](LICENSE)。该许可范围为本目录，不改变仓库其他目录的许可状态。

制作工具 [sprite-gen](https://github.com/aldegad/sprite-gen) 是独立项目，依其自身许可使用；本包通过接口复用它，没有分发其源码、模型权重或生成服务凭据。

案例的完整原始提示词保留在公开仓库的 [PROMPT.md](https://github.com/yuanyang749/windbell-valley/blob/main/PROMPT.md)，安装技能后仍可通过该链接查看。
