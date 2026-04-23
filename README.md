# Nemo-skills

Nemo 的 AI Skills 工具箱。

这里先只沉淀一个我自己在真实工作流里反复打磨过的 Skill：
`guided-writer`。

目标不是堆很多花哨功能，而是先把一个真正稳定、可复用的方法论做成可安装、可迁移、可持续演化的 Skill 仓库。

这个仓库目前包含两类内容：

- Skills: 遵循 Agent Skills 结构的可安装指令集，安装后 Agent 可自动加载
- References: 某些 Skill 会附带参考文档，用来承载方法论、示例库和执行细则

## 当前 Skill

- `guided-writer`: 访谈式写作 Skill，通过主持人式提问帮助用户从模糊想法中提炼出可成文材料

## Skill 特点

### `guided-writer`

这是目前方法论最完整的一个 Skill。
除了 `SKILL.md` 之外，还包含 `references/` 目录：

- `references/content_methodology.md`
- `references/question_examples.md`

它的定位不是“直接替你写”，而是先通过短访谈把用户脑海里的模糊想法提炼成：

- 核心判断
- 文章方向
- 关键例子
- 读者落点

然后再进入起草与润色阶段。

## 安装方式

### 通过 Agent 安装

在支持 Skills 的 Agent 中，直接提供仓库地址即可。

例如：

```text
安装这个 skill：https://github.com/your-name/Nemo-skills
```

### 手动安装

1. 下载仓库 ZIP，或直接 clone：

```bash
git clone https://github.com/NimoCao/Nemo-skills.git
```

2. 把你想安装的 Skill 文件夹整体复制到对应工具的 Skills 目录下。

常见安装路径：

| 工具 | 路径 |
| --- | --- |
| Claude Code | `~/.claude/skills/` |
| OpenClaw | `~/.openclaw/skills/` |
| Codex | `~/.agents/skills/` |

例如安装 `guided-writer` 到 Claude Code：

```bash
git clone https://github.com/your-name/Nemo-skills.git
cp -r Nemo-skills/guided-writer ~/.claude/skills/
```

## 仓库结构

```text
Nemo-skills/
├── CLAUDE.md
├── LICENSE
├── README.md
└── guided-writer/
```

## 设计原则

- 先解决真实问题，再抽象成 Skill
- Skill 尽量短、准、可执行
- 方法论复杂时，拆到 `references/` 中承载
- 优先服务真实工作流，而不是做演示型 Prompt

## 后续可扩展

后续如果有需要，可以继续加入：

- 更多写作类 Skills
- 研究分析类 Skills
- 个人工作流自动化 Skills
- 配套 prompts 或 examples 目录

## License

MIT
