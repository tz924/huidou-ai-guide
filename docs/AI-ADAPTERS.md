# 不同 AI 如何接手

本项目把软件操作路径、验证标准和进度放在普通 Markdown/CSV 中，具体鼠标、截图、控件 API 由当前工具环境提供。跨 AI 文档入口已配置，执行兼容性仍需在目标电脑实测。

| AI | 入口 | 桌面操作条件 | 当前实测 |
|---|---|---|---|
| Codex | 根目录 AGENTS.md | 当前会话实际提供的 Windows computer-use 技能/工具 | 旧机 Codex＋sky 已实测；新机未测 |
| Claude Code / Claude | 根目录 CLAUDE.md 导入 AGENTS.md；其他 Claude 界面手动提供这些文件 | 当前 Claude 环境有可控制目标 Windows 桌面的工具，并获授权 | 文档入口已准备，实际执行未测 |
| 其他 AI | 手动加载 AGENTS.md、STATUS、TODO 和本页 | 对应桌面控制工具；否则只能提供文字辅助 | 未测 |

## 统一操作接口（语义协议，不是可直接调用的 API）

1. 发现：列出当前可控窗口，确认灰豆标题与软件版本。
2. 观察：取新截图和可访问控件；确认当前项目、节点和是否有任务。
3. 动作：单次点击、输入、滚动、拖动或按键。
4. 复查：用新截图、任务状态或文件结果确认动作实际生效。
5. 记录：模型、完整提示词、真实引用、参数、提交状态、自动下载路径和待验收项。

这五步映射到工具实际暴露的 API；不要编造 list_windows/click 等函数名。先读当次工具文档，按其限制操作。无音频播放/听验能力时只能标注“媒体参数已检查，语义待听验”。

## Codex 的历史实现

旧机使用 computer-use 技能、node_repl 和 @oai/sky。工具持久变量及窗口编号属于旧会话，不在 Git 中迁移。新机必须重新初始化和发现窗口。没有同类工具的 Codex CLI 也不能因有 AGENTS.md 就直接控制 Windows。

## Claude 的实现边界

CLAUDE.md 用 @AGENTS.md 导入共同规范。Claude Code 的文件/终端能力不等于 Windows 图形界面控制能力；在目标环境核对可用连接。先做“截图识别窗口→打开无付费面板→关闭面板”的小测试，再提交生成。

## 配置入口依据

根目录 AGENTS.md 的项目规范入口依据 [OpenAI 官方说明](https://learn.chatgpt.com/docs/agent-configuration/agents-md)；CLAUDE.md 与 @ 导入依据 [Claude 官方说明](https://code.claude.com/docs/en/memory)。2026-10-18 核对。此处仅说明文档加载方式，不保证任何客户端具有桌面控制能力。
