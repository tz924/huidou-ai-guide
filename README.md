# 灰豆 AI 光影引擎使用指南

为 Codex、Claude 及其他 AI 持续维护的中文操作指南。目标是覆盖灰豆制作剧本、图像、资产、视频、声音和成片的完整流程，让另一台电脑上的 AI 能凭文档和证据接手。

当前基线：Windows 灰豆 v7.7.1，2026-10-18–19 实测；34 项功能状态。主制作链路已跑通，新机补测已回收照相馆、无人空镜、图片工具、3D/绘梦和音视频参考小样，三镜头外部30秒审阅版已保存；正式工程包跨机媒体完整性、最终音画及 Claude 实测仍待完成。

## 从这里开始

1. AI 先读 [AGENTS.md](AGENTS.md)，再读 [当前进度](progress/STATUS.md) 和 [TODO](progress/TODO.md)。Claude 入口为 [CLAUDE.md](CLAUDE.md)，导入同一份规范。
2. 查阅 [完整操作手册](docs/GUIDE.md)、[功能验证清单](progress/FEATURE-MATRIX.csv)、[AI 工具适配](docs/AI-ADAPTERS.md)、[新机接手实测](evidence/records/2026-10-18-new-machine-handoff.md)、[剩余工具结果与限制](evidence/records/2026-10-18-remaining-tools.md)。
3. 换电脑按 [迁移与启动说明](docs/SECOND-COMPUTER.md) 配置路径、软件和桌面控制工具。
4. 测试后补充证据与手册，再提交推送。首次可直接使用 [接手提示词](prompts/RESUME.md)。

34项为功能分组，并非全部子功能通过。完整范围继续按[已发现功能与工作流审计](progress/WORKFLOW-AUDIT.md)逐项补齐。

```powershell
git clone https://github.com/tz924/huidou-ai-guide.git
cd huidou-ai-guide
```

这是私有仓库，另一台电脑须使用有仓库权限的 GitHub 账号。

## 项目范围

包括 MJ、Image 2.5、Nano Banana 2 生图，素材库，剧本拆解，图生视频，角色音色参考，剪辑、混音、字幕、导出，以及分镜、修图、3D、VR360 和绘梦等工具。

文档与测试素材可通过 Git 同步；灰豆安装包、登录态、额度、画布工程数据库及桌面控制能力不包含在仓库中。软件工程跨机同步方式尚未验证。只读文档的 AI 可以协助规划与写提示词，实际点击需要对应电脑的 Windows 桌面控制工具。

## 目录

| 路径 | 用途 |
|---|---|
| docs/ | 持续维护的操作指南、AI 适配、换机说明、完成标准 |
| progress/ | 当前进度、TODO、34 项验证清单 |
| evidence/ | 随仓库迁移的样图、试片、字幕、文件清单和 SHA256 |
| archive/2026-10-18/ | 旧机原始手册与日志，只作历史证据 |
| config/ | 每台电脑路径配置示例；本地配置被 Git 忽略 |
| templates/ | 标准测试记录与交接模板 |
| prompts/ | 给各类 AI 的可复制接手指令 |
| examples/ | 三镜头测试剧本 |
| scripts/ | 文档链接及证据哈希校验，无需第三方 Python 包 |

校验：`python scripts/validate.py`。本仓库没有灰豆 API 或一键自动执行灰豆的程序，文档中的按钮名及参数应随版本实测更新。
