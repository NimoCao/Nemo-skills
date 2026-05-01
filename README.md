# Nemo-skills

Nemo 的 AI Skills 工具箱。

这里沉淀我自己在真实内容工作流里反复打磨过的 Skills。

目标不是堆很多花哨功能，而是把真正稳定、可复用的方法论做成可安装、可迁移、可持续演化的 Skill 仓库。

这个仓库目前包含两类内容：

- Skills: 遵循 Agent Skills 结构的可安装指令集，安装后 Agent 可自动加载
- References: 某些 Skill 会附带参考文档，用来承载方法论、示例库和执行细则

## 当前 Skill

- `guided-writer`: 访谈式写作 Skill，通过主持人式提问帮助用户从模糊想法中提炼出可成文材料，并在成稿后自动生成公众号标题与小红书标题候选
- `adapt-content-platforms`: 全平台内容自适应 Skill，将一篇文章改造成小红书与微信公众号发布包，包括标题、图片方案和平台正文

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

然后再进入起草、润色，以及标题包装阶段。

### `adapt-content-platforms`

这是一个内容分发适配 Skill。
输入是一篇文章，输出两个平台的完整发布方案：

- 小红书标题：3-5 个，20 个字以内，有网感
- 小红书封面图：3:4 竖版方案，突出 10 个字以内的金句
- 小红书内容图：2-5 张竖版内容卡片方案，提炼文章重点
- 小红书正文：符合小红书语气，带 emoji、互动和话题
- 公众号标题：3-5 个，25 个字以内，有网感但更克制
- 公众号封面图：公众号横版封面方案，不强制加字
- 公众号正文：符合公众号长文阅读习惯，保留完整观点链路

除了 `SKILL.md` 之外，还包含：

- `agents/openai.yaml`
- `references/platform-spec.md`

它的定位不是简单“改写同一篇文章”，而是把同一份内容拆成不同平台真正需要的资产。

## 安装方式

### 通过 Agent 安装

在支持 Skills 的 Agent 中，直接提供仓库地址即可。

例如：

```text
安装这个 skill：https://github.com/NimoCao/Nemo-skills
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
git clone https://github.com/NimoCao/Nemo-skills.git
cp -r Nemo-skills/guided-writer ~/.claude/skills/
```

例如安装 `adapt-content-platforms` 到 Codex：

```bash
git clone https://github.com/NimoCao/Nemo-skills.git
cp -r Nemo-skills/adapt-content-platforms ~/.agents/skills/
```

## 仓库结构

```text
Nemo-skills/
├── LICENSE
├── README.md
├── adapt-content-platforms/
│   ├── SKILL.md
│   ├── agents/
│   └── references/
└── guided-writer/
    ├── SKILL.md
    └── references/
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
