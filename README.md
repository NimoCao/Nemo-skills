# Nemo-skills

Nemo 的 AI Skills 工具箱。

这里沉淀我自己在真实内容工作流里反复打磨过的 Skills。

目标不是堆很多花哨功能，而是把真正稳定、可复用的方法论做成可安装、可迁移、可持续演化的 Skill 仓库。

这个仓库目前包含两类内容：

- Skills: 遵循 Agent Skills 结构的可安装指令集，安装后 Agent 可自动加载
- References: 某些 Skill 会附带参考文档，用来承载方法论、示例库和执行细则

## 当前 Skill

- `guided-writer`: 访谈式写作 Skill，通过主持人式提问帮助用户从模糊想法中提炼出可成文材料，并在成稿后自动生成公众号标题与小红书标题候选
- `insight-essay-writer`: 观点文章写作 Skill，把已有观点、笔记或提纲写成 Nemo 风格的中文判断型文章，强调现象观察、克制批评、底层解释、具体场景和自然段落颗粒度
- `adapt-content-platforms`: 全平台内容自适应 Skill，将一篇文章改造成小红书、微信公众号与 X/Twitter 发布包，包括标题、封面/正文图片方案、平台正文、英文单帖和 thread
- `text-card-renderer`: 文字卡片渲染 Skill，将小红书/公众号/X 的金句图、清单图、框架图、对照图等从精确文字直接导出为 SVG 和 PNG，避免 AI 生图导致中文错字
- `clarify-ai-demand`: AI 需求校准 Skill，用户描述、分析或梳理需求时触发；先让 AI 渐进式理解需求，同时查找可参考的现成 Skill，再把模糊想法收束成包含关键对象抽象的 PRD

## Skill 特点

### `clarify-ai-demand`

这是一个用来“先把需求聊明白”的 Skill。
它适合在用户想分析、描述、梳理一个需求，或者想做 AI 工具、Agent、Prompt、自动化流程但还比较模糊时使用。

它不会一上来直接写 Prompt，而是先让 AI 做这些事：

- 复述：先说说它听懂了什么
- 校准：指出不确定、容易误解和需要追问的地方
- 参考：调用 `find-skills`、`npx skills find`、skills.sh / SkillHub 等渠道，查找是否有相关 Skill 可以借鉴
- 追问：把找到的 Skill 效果返回给用户，确认“这是不是你想要达成的效果”
- 抽象：提前定义关键对象，包括字段、状态、关系，以及前端如何呈现、后端如何存储/处理
- 收束：把需求变成一份可给产品、前端、后端和 Agent 实现使用的 PRD

它的核心理念是：

> 别急着写 Prompt，先让 AI 说说它听懂了什么，也把关键对象抽象清楚。

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

然后把访谈材料整理成文章 brief，交给 `insight-essay-writer` 负责最终成稿和文风控制，再进入标题包装阶段。

### `insight-essay-writer`

这是一个“已有观点成稿” Skill。
它适合在观点已经比较清楚、但还需要写成完整文章时使用。

它不负责长访谈，而是把用户提供的判断、笔记、对话片段或粗提纲整理成：

- 一个清晰的现象观察
- 一个克制但明确的核心判断
- 对“为什么大家会这样做”的理解
- 2-3 个可复用的判断标准
- 足够具体的产品、工作流或生活场景
- 自然的段落颗粒度，避免短句过密或 AI 味总结

除了 `SKILL.md` 之外，还包含：

- `agents/openai.yaml`
- `references/style-guide.md`

它和 `guided-writer` 的区别是：`guided-writer` 负责把模糊想法问出来，`insight-essay-writer` 负责把已经问出来的观点写得像一篇完整文章。

### `adapt-content-platforms`

这是一个内容分发适配 Skill。
输入是一篇文章，输出三个平台的完整发布方案：

- 小红书标题：3-5 个，20 个字以内，有网感
- 小红书封面图：3:4 竖版方案，突出 10 个字以内的金句
- 小红书内容图：2-5 张竖版内容卡片方案，提炼文章重点
- 小红书正文：符合小红书语气，带 emoji、互动和话题
- 公众号标题：3-5 个，25 个字以内，有网感但更克制
- 公众号封面图：公众号横版封面方案，不强制加字
- 公众号正文配图：默认 2-4 张，至少 1 张解释型或收藏型信息图，并标注插入位置
- 公众号正文：符合公众号长文阅读习惯，保留完整观点链路
- X 内容方向：明确英文受众、核心观点和首发格式
- X 单帖候选：3-5 条自然英文 post，适合信息流独立传播
- X Thread：默认 3-7 条，不强行一条说完，按 X 阅读节奏拆观点
- X 图文配图：必要时生成 1-2 张英文 quote/framework/contrast card

除了 `SKILL.md` 之外，还包含：

- `agents/openai.yaml`
- `references/platform-spec.md`

它的定位不是简单“改写同一篇文章”，而是把同一份内容拆成不同平台真正需要的资产。

### `text-card-renderer`

这是一个“确定性文字配图” Skill。
它适合生成小红书内容卡、公众号封面/正文逻辑图、X 信息图等文字必须准确的图片。

它不走 AI 生图，而是根据 JSON 规格生成 SVG，再导出 PNG。
适合这些场景：

- 金句图
- 框架图
- 清单图
- 对照图
- 三要素/步骤/入口结构图
- 公众号横版逻辑图

核心优势是：中文准确、尺寸稳定、可复用、可继续改 SVG 原稿。

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
├── clarify-ai-demand/
│   ├── SKILL.md
│   └── agents/
├── guided-writer/
│   ├── SKILL.md
│   └── references/
├── insight-essay-writer/
│   ├── SKILL.md
│   ├── agents/
│   └── references/
└── text-card-renderer/
    ├── SKILL.md
    └── scripts/
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
