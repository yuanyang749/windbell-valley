# 风铃溪谷 · Windbell Valley

[在线体验](https://yuanyang749.github.io/windbell-valley/)

手绘村庄动画展示：邮差少女与白狐沿着春日小路，走过山坡住居、村中集市和河岸水车。

- 6324 × 724 完整地图，可横向拖动并跳转街区。
- 42 秒游览视频，1280 × 720、30 fps。
- 园丁浇花、面包师挥手、老人摇头吹笛与飘动音符，角色动画使用 RIFE 补帧。
- 原创 72 BPM 三拍背景曲，笛子、木吉他、轻弦乐等声部；音乐已合并在视频中。
- 晾晒衣服轻摆、柳树垂枝随风摇动、溪流反光流动，环境循环使用本地 RIFE 补帧。
- 三角旗飘动、喷泉水流、集市大树枝梢摇曳与少量落叶；部分烟囱升起炊烟，前景花簇有蝴蝶和蜜蜂扇翅飞舞。
- 水车缓慢转动，外缘水帘持续下落，底部有小水花与下游细流，使用局部遮罩和 RIFE 补帧。
- 经过大树、喷泉、水车和溪流时，环境声随距离渐入渐出并改变左右声场，伴随少量轻柔风铃。
- 默认静音播放，点击“开启声音”同时收听配乐和环境声。

## 制作提示词

[PROMPT.md](PROMPT.md) 包含可直接复制的总提示词、实际制作过程、后续修正，以及地图、人物和 NPC 动作的原始生成提示词。

## 可复用制作手册与 Skill

[animated-2d-scene-skill](animated-2d-scene-skill/README.md) 将本项目经验整理为可独立阅读的制作手册和 Codex 技能包：

- [制作手册](animated-2d-scene-skill/references/handbook.md)：参考图动画、抠像、遮罩、循环、RIFE、声音及交付。
- [坑点记录](animated-2d-scene-skill/references/pitfalls.md)：真实错误、修正与验证方法。
- [提示词模板](animated-2d-scene-skill/references/prompts.md)：适用于新地图、角色和环境动作。
- [技能入口与安装](animated-2d-scene-skill/README.md)：在新项目中使用，附保持时长和锚点的 RIFE 辅助脚本。

技能包与手册采用目录内的 [MIT License](animated-2d-scene-skill/LICENSE)，许可范围为该目录。本案例验证了预渲染展示；包内的游戏接入指导需在具体项目运行时验证。

## 文件

```text
index.html                 页面、样式和交互
PROMPT.md                  制作流程与可复用提示词
animated-2d-scene-skill/    开源制作手册、Codex Skill、模板与辅助脚本
assets/scene.mp4            带背景音乐的游览视频
assets/scene-poster.png     视频封面
assets/windbell-valley.png  完整地图
.nojekyll                  GitHub Pages 静态发布标记
```

## 本地预览

在此文件夹运行：

```sh
npx --yes http-server@14.1.1 . -a 127.0.0.1 -p 8080 -c-1
```

浏览器打开 `http://127.0.0.1:8080/`。该服务支持视频按时间跳转。

## GitHub Pages

仓库使用 `main` 分支根目录发布，无需构建。后续更新页面或替换 `assets` 中的成品，提交并推送即可自动发布。

场景参考了 [aldegad/sprite-gen 的村庄示例](https://github.com/aldegad/sprite-gen/blob/main/docs/assets/village-scene.gif)。本场景地图与人物通过图像生成制作，NPC 动作通过 Grok 订阅视频生成、sprite-gen 后处理和本地 RIFE 补帧完成；音乐为此场景编写并在本地渲染。
