# Platform Spec

## 小红书

### 输出格式

最终平台适配包应使用可直接复制发布的纯文本格式。

- 不要使用 Markdown 标题语法，例如 `#`、`##`、`###`。
- 不要使用 Markdown 加粗或斜体语法，例如 `**重点**`、`*重点*`。
- 不要使用 Markdown 分割线。
- 不要使用 Markdown 表格、引用块、任务列表、图片嵌入语法或链接包装语法。
- 不要把最终发布包包在 Markdown 代码块里。
- 除小红书话题标签和 X/Twitter hashtag 外，最终交付中不要出现 Markdown 风格的 `#` 标记。
- 需要分区时，直接写纯文本栏目名，例如“小红书标题”“公众号正文”。
- 正文里的小标题直接独立成行，不加 Markdown 标记。
- 重点句通过独立成段、短句和换行体现，不用加粗符号。

### 内容定位

小红书不是文章搬运平台。适配时先把文章变成“一个人愿意收藏/转发/评论的经验或判断”。

优先突出：
- 我曾经怎么想，现在怎么想
- 一个反常识发现
- 一个可复用的方法
- 一个具体变化
- 一句能让人停下来的判断
- 一个值得保存的信息资产：表格、清单、榜单、模板、工具列表、数据字段、接入方式、步骤图、检查项

### 标题习惯

可用路线：
- 情绪代入：我终于明白...
- 反差冲突：原来...不是...
- 结果收益：...之后，我...
- 人群身份：给...的一点提醒
- 金句判断：...才是...

避免：
- 虚假承诺
- 过度焦虑
- 标题与正文不一致
- 连续多个感叹号

### 标题与封面协同

小红书标题和封面文案不是互相复读，而是从不同角度说同一件事。

推荐分工：
- 标题：更适合承担具体场景、结果反馈、身份代入、故事钩子。
- 封面：更适合承担核心利益、反差冲突、方法机制、最强金句。

组合方式：
- 标题讲结果，封面讲方法。
- 标题讲方法，封面讲收益。
- 标题讲情绪，封面讲判断。
- 标题讲工具，封面讲前后变化。
- 标题讲“发生了什么”，封面讲“为什么值得看”。

Example:
- 标题：草图给 AI，同事说架构图惊艳了
- 封面主文案：草图秒变架构图
- 封面副文案：理清逻辑，交给 AI

避免：
- 标题和封面使用完全相同的句子。
- 标题和封面只做近义词替换。
- 标题讲 A，封面讲 B，二者没有共同点击理由。

### 图片卡片

必须使用 3:4 竖版，建议 1080x1440。整组图保持同一比例。

执行要求：
- 每张图先判断最适合的来源：生图、文字设计、逻辑图、真实截图、用户拍摄或用户自己找图。
- 如果 AI 生成图最合适，默认必须调用生图工具生成实际图片文件；只输出提示词/brief 不算完成交付。
- 如果真实素材更合适，不要硬生成 AI 图。应明确建议用户自己截图、找图或拍摄，并说明具体找什么、从哪里找、画面里要有什么。
- 生成后必须返回每张图片的本地路径或可访问链接；自己找图方案则返回“待用户提供素材”和具体找图说明。
- 如果需要生图但无法生成图片，必须说明工具缺失或调用失败原因，并保留可直接用于补生成的 brief。
- 如果小红书图片选择生图，必须分别调用生图工具生成，一次调用只生成一张最终发布图。
- 生成前必须明确当前图片身份：封面图、内容图 1、内容图 2 等。
- 禁止把多张卡片写进一个 prompt 里生成 carousel preview、grid、contact sheet、拼图或总览图。
- 禁止只生成一张图片来代表整组小红书图文。

封面：
- 金句不超过 10 个字
- 字要大，移动端一眼可读
- 主体要清楚，不要用复杂长段文字
- 适合信息流快速扫读

内容图：
- 2-5 张
- 每张一个观点，但必须讲完整。
- 内容图不是一句话海报，不能只有几个字。
- 当内容是大段观点、文章摘录、个人判断、解释性文字时，优先做成“备忘录图”，而不是传统信息卡。
- 内容图不只服务金句传播，也要服务收藏和获得感。每组图文默认至少 1 张“收藏型干货图”，除非原文没有任何可结构化信息。
- 收藏型干货图适合把这些内容视觉化：不同场景/人群/行业的对照，不同步骤，不同工具或平台，不同数据字段，不同接入方式，推荐优先级，避坑清单，检查清单，模板句式。
- 当原文有“电商、线索类、本地生活分别需要什么数据”“API、导出、截图、表单分别适合什么情况”这类信息时，优先做成表格或矩阵图。
- 当原文有“最值得先做的几件事”“最适合接入的几类数据源”“常见问题排行”这类信息时，优先做成榜单或清单图。
- 单张图中文字建议 80-180 个中文字符；复杂观点可到 220 字，但必须保持移动端可读。
- 结构建议：大标题 + 突出重点句 + 一段说明文字，或大标题 + 突出重点句 + 2-3 条短 bullet。
- 收藏型干货图的结构可以是：大标题 + 一句使用说明 + 简洁表格/矩阵/榜单/检查项。表格列数控制在 2-3 列，行数控制在 3-6 行。
- 用户只阅读图片上的文字，也应该能明白这一页想表达什么。
- 优先摘取或改写原文里的金句、关键判断、方法步骤、对比关系，但不要把观点压缩到失真。
- 允许突出部分关键词、金句、数字或判断，但突出文字不能替代完整说明文字。
- 收藏型干货图必须让用户感觉“保存后还能用”，不能只是把一段话换行排版。

### 小红书图片类型

优先级：
1. 备忘录图：小红书文字图默认首选。
2. 文字图/信息卡：保留，但只在清单、框架、对照、表格等结构化内容更合适时使用。
3. 视觉图：用于故事、情绪、场景或隐喻。

#### 1. 封面图

特点：
- 文本是主视觉。
- 画面、人物、图形、质感都服务于让标题更醒目。
- 封面文字必须短，默认不超过 10 个字。
- 适合承载最强金句、反差判断、情绪入口。

Prompt template:

```text
Generate one single Xiaohongshu cover image, 3:4 vertical, 1080x1440.
Image type: cover image where text is the main visual.
Main Chinese text, exact and large: <封面金句>
Optional small Chinese subtitle, exact: <副标题>
Topic: <文章主题>
Audience: <目标读者>
Visual direction: bold editorial social-media cover, strong typographic hierarchy, the Chinese text dominates the composition, background elements only support the message.
Composition: large centered or upper-third title, generous safe margins, mobile-readable text, one clear focal area, no clutter.
Background/visual elements: <与文章相关的背景元素>
Palette and style: <配色与风格>
Constraints: create exactly one final 3:4 image, not a carousel, not a grid, not a mockup preview. Do not add extra text, logos, QR codes, watermarks, English copy, or unrelated symbols.
```

#### 2. 备忘录图

特点：
- 像苹果备忘录/系统笔记截图，而不是海报或信息图。
- 适合承载大段文字、观点解释、文章摘录、个人判断、小红书“文字流”内容。
- 文字是主角，背景和装饰要克制。
- 单张通常包含标题 + 3-6 段正文，正文可 300-700 字，但必须移动端可读。
- 视觉建议：浅色背景、暖白纸张、圆角、大留白、顶部轻量系统栏/日期/小圆点。
- 文字必须准确，优先用 `text-card-renderer` 的 `note` layout 导出 SVG + PNG，不要用 AI 生图。

Spec example:

```json
{
  "width": 1080,
  "height": 1440,
  "layout": "note",
  "date": "AI 入口观察",
  "title": "聊天框不够用了",
  "paragraphs": [
    "最近看 AI 新闻，我发现一个很明显的变化：大模型公司不只是在卷模型了。",
    "它们开始抢 Office、浏览器、终端这些看起来很旧的入口。",
    "这些东西表面看很散，但背后其实是同一件事：AI 公司都在抢任务现场。"
  ]
}
```

#### 3. 文字图 / 信息卡

特点：
- 图片本身只起背景作用。
- 核心是卡片上的可阅读文字信息。
- 适合承载观点拆解、对比关系、方法步骤、关键句、表格、榜单、清单、工具列表、数据字段、接入方式、检查项。
- 优先级低于备忘录图。只有当内容明显需要表格、矩阵、清单、对照、榜单或步骤时才使用。
- 背景要弱，不抢文字，留足干净的文字区域。
- 读者不看正文配文，只看图片文字，也能理解这一页的完整观点。
- 不是短句海报，不能只放几个字。
- 当文字图是收藏型干货图时，要优先使用结构化版式，例如 2-3 列表格、四象限矩阵、Top 5 榜单、步骤清单、检查清单。不要把表格做成密密麻麻的小字。

Prompt template:

```text
Generate one single Xiaohongshu text card, 3:4 vertical, 1080x1440.
Image type: text-first card where the image is only a subtle background.
Main Chinese heading, exact and large: <卡片标题>
Highlighted Chinese sentence, exact: <突出重点>
Chinese explanatory body text, exact: <说明文字，80-180 个中文字符>
Topic: <文章主题>
Visual direction: clean readable editorial information card, text is the primary content, background is quiet and secondary.
Composition: strong text hierarchy, large heading, highlighted sentence, readable paragraph or 2-3 short bullets, generous margins, high contrast, mobile-readable typography.
Background/visual elements: subtle abstract shapes, soft product/workspace texture, simple UI fragments, or light illustration related to <卡片含义>; keep opacity low and avoid visual noise.
Palette and style: <配色与风格>
Constraints: create exactly one final 3:4 image, not a carousel, not a grid, not a mockup preview. Preserve the specified Chinese text accurately. Do not add extra text beyond the specified Chinese copy, logos, QR codes, watermarks, English copy, or unrelated symbols.
```

收藏型干货图 prompt add-on:

```text
This is a save-worthy practical information card. Use a clean structured layout such as a compact table, ranked list, checklist, or comparison matrix. Keep Chinese text mobile-readable. Use clear dividers, labels, and spacing. The card should feel useful enough for the reader to save for later.
```

#### 4. 视觉图

特点：
- 整体视觉负责表达含义。
- 文字起辅助说明作用，但仍需让读者读完后理解这张图的观点。
- 适合表达故事场景、隐喻、情绪、冲突、前后变化。
- 画面必须一眼能看懂，不能只做抽象氛围。
- 视觉图可以比文字图更少字，但不能只有几个字；建议包含 40-100 个中文字符的辅助说明。

Prompt template:

```text
Generate one single Xiaohongshu visual card, 3:4 vertical, 1080x1440.
Image type: visual-led card where imagery communicates the main meaning and text is secondary.
Chinese heading or label, exact: <辅助标题>
Small Chinese explanatory text, exact: <辅助说明，40-100 个中文字符>
Topic: <文章主题>
Core meaning to express visually: <这张图要表达的含义>
Visual direction: strong editorial illustration or product-lifestyle scene, clear metaphor, one main subject, readable at mobile feed size.
Composition: visual subject dominates, text placed in a clean safe area, no clutter, strong focal point, 3:4 vertical framing.
Scene/subject: <具体场景或视觉隐喻>
Palette and style: <配色与风格>
Constraints: create exactly one final 3:4 image, not a carousel, not a grid, not a mockup preview. Preserve the specified Chinese text accurately. Do not add extra text beyond the specified Chinese copy, logos, QR codes, watermarks, English copy, or unrelated symbols.
```

### 正文习惯

推荐结构：
1. 开头：一个强钩子，直接说变化、痛点、反差或结论
2. 中段：用 2-4 个短小段落展开，穿插 emoji 做节奏点
3. 结尾：一句总结 + 一个互动问题
4. 话题：5-8 个

Emoji 使用：
- 可用于段首提示情绪或结构，如：✨、🤔、📌、🧠、🚀、💡
- 不要每句话都加
- 不要让 emoji 替代信息密度

格式要求：
- 小红书正文不要使用 Markdown 标题和加粗语法。
- 小红书正文可以保留自然换行、编号和话题标签。
- 不要输出 Markdown 图片语法，图片路径单独列在图片资产部分。

## 微信公众号

### 内容定位

微信公众号适合承载完整观点、个人判断和更长的思考链路。适配时不要只“口语化”，要重新组织阅读体验。

公众号正文不用怕长。它不是摘要位，而是完整承接深度的长文位。只要原文里的观点、例子、反驳、转折、方法和结论对理解文章有帮助，就应该写进正文。

优先突出：
- 文章为什么值得读
- 问题背后的变化
- 作者的判断与证据
- 对读者有什么启发

### 标题习惯

可用路线：
- 判断型：...正在改变...
- 解释型：为什么...
- 反差型：你以为...其实...
- 问题型：...到底意味着什么？
- 金句型：...，才是...

控制在 25 个中文字符以内。可以有网感，但要可信。

### 封面图

默认使用 2.35:1 横版，常用尺寸 900x383 或等比高清尺寸。

执行要求：
- 先判断封面类型，再决定是否生图或建议用户自己找图。
- 如果 AI 生成图最合适，默认必须调用生图工具生成实际图片文件；只输出提示词/brief 不算完成交付。
- 如果真实产品图、真实截图、用户拍摄图或资料图更合适，不要硬生成 AI 图。直接输出找图/截图/拍摄建议，并说明为什么真实素材更适合。
- 生成后必须返回图片的本地路径或可访问链接；自己找图方案则返回“待用户提供素材”和具体找图说明。
- 如果需要生图但无法生成图片，必须说明工具缺失或调用失败原因，并保留可直接用于补生成的 brief。

公众号封面类型：

1. 文字图
- 适合强观点、判断型、反差型文章。
- 用大标题或短金句吸引人，文字必须短、醒目、可信。
- 不要堆长句，不要做成小字海报。
- 适合标题本身有判断力度，或者文章缺少具象场景但观点很强。

2. 逻辑图
- 适合解释一套架构、流程、系统关系、方法论、事物逻辑。
- 用模块、层级、箭头、路径、对照关系或简洁框架表达结构。
- 不追求细节完整，而追求让读者一眼知道“这篇在讲一套结构”。
- 适合 AI 系统、工作流、产品架构、商业模式、认知框架等主题。

3. 故事图
- 适合有具体人物、场景、冲突、前后变化或情绪转折的文章。
- 画面要像一个故事瞬间，而不是抽象氛围图。
- 适合个人经历、复盘、线下场景、用户案例、生活观察。

4. 自己找图
- 适合真实产品、真实界面、真实案例、真实数据、真实工作流、真实场景更有说服力的文章。
- 可以建议用户截图：产品页面、设置页、工作流界面、聊天记录、评论区、数据面板、草图、文件夹结构、真实作品前后对比。
- 可以建议用户拍摄：桌面工作现场、手稿、白板、线下空间、设备、产品使用场景。
- 可以建议用户从公开资料找：官网截图、产品发布图、公开演示图、论文/报告中的图表，但要提醒注意版权和来源。
- 当真实素材能提供证据感、现场感或可信度时，优先自己找图，而不是生成一张“看起来很像”的 AI 图。

封面共同要求：
- 主题明确
- 风格干净
- 与文章情绪一致
- 适合作为长文入口，而不是广告 banner

### 正文配图

公众号正文默认需要 2-4 张配图。它们不是装饰，也不是小红书卡片复用，而是帮助长文完成三件事：让读者停一下、把复杂关系讲清楚、留下可保存或可转发的信息资产。

正文配图执行要求：
- 每篇公众号默认提供 2-4 张正文配图，除非用户明确不要配图。
- 至少 1 张必须是解释型或收藏型信息图。
- 每张图都要说明建议插入位置，位置要和正文结构绑定，例如“第 1 个小标题后”“案例段落后”“方法清单前”“结尾前”。
- 每张图都要先判断图片来源：生图、逻辑图设计、真实截图、用户拍摄、公开资料图或不用图。
- 如果 AI 生成图最合适，默认必须调用生图工具生成实际图片文件；只输出提示词/brief 不算完成交付。
- 如果真实素材更有证据感，优先建议用户自己找图/截图/拍摄，并说明画面里应该有什么。
- 生成后必须返回图片的本地路径或可访问链接；自己找图方案则返回“待用户提供素材”和具体找图说明。

正文配图类型：

1. 解释型信息图
- 适合框架、流程、因果链、系统关系、方法步骤。
- 可用模块、箭头、路径、分层结构、流程线或简化图形表达。
- 图中文字要短，但信息关系要清楚。

2. 收藏型干货图
- 适合清单、对照表、检查项、字段列表、工具列表、决策规则、模板句式。
- 保存后应该还能独立使用。
- 可以比封面信息更密，但必须移动端可读。

3. 证据截图/真实素材图
- 适合产品界面、数据面板、工作流截图、聊天记录、评论反馈、真实作品前后对比。
- 当真实性本身能增强说服力时，优先截图或用户素材，不要生成一张“像截图”的假图。

4. 故事/场景图
- 适合个人经历、案例转折、现场感强的文章。
- 画面要对应正文里的具体场景，不要只是抽象氛围。

5. 金句/转折图
- 适合在长文中段或结尾放大关键判断。
- 文字要克制，不要做成小红书式标题党。

推荐比例：
- 横版：1200x675，适合故事图、逻辑图、封面风格延展。
- 4:3：1200x900，适合信息图、截图说明、方法清单。
- 方图：1080x1080，适合金句图、对照图、简单框架。
- 4:5：1080x1350，适合复杂信息图；注意不要变成小红书 3:4 竖卡口吻。

插入节奏建议：
- 开头 3-5 段内通常不急着放图，先让读者进入问题。
- 第 1 张正文图适合放在核心问题或主判断之后，帮助读者形成心智图。
- 中段配图适合承接案例、流程、对照、清单。
- 结尾前可放 1 张回扣主判断的金句图或总结图。
- 不要连续堆图；图片之间应有足够正文推进。

### 正文习惯

推荐结构：
1. 标题后直接进入 hook，不写空泛导语
2. 用 3-6 个小标题推进；复杂长文可以更多，但每个小标题都必须承担推进功能
3. 每个小标题下有一个明确功能：提出问题、解释原因、给出例子、推进判断、落到读者
4. 段落保持短，但逻辑不要碎
5. 结尾回扣开头，形成完整闭环

长度原则：
- 不要为了“平台适配”把文章压缩成短摘要。
- 宁可正文长一点，也要覆盖所有关键判断和必要支撑。
- 如果原文是观点文，公众号正文应接近完整改写：保留主判断、解释链路、关键例子、反方/误区、作者结论。
- 可以删掉重复、松散和平台不适配的段落，但不能删掉理解文章所必需的关键点。
- 判断一个公众号版本是否合格，不看它短不短，而看读者是否不需要回原文也能理解完整观点链路。

公众号可以比小红书更克制：
- 少用 emoji，默认不用
- 少用网络热词
- 多用完整句和清晰转折
- 可以保留作者的个人经历和复杂判断

格式要求：
- 公众号正文标题直接写标题文本，不要写成 `# 标题`。
- 公众号正文小标题直接独立成行，不要写成 `## 小标题`。
- 不要使用 `**加粗**` 或其他 Markdown 强调语法。
- 不要使用 Markdown 表格、引用块、任务列表、链接包装或分割线。
- 不要使用 Markdown 图片语法；公众号封面路径在封面图资产部分单独列出。
- 重点句通过独立成段、自然重复和上下文位置体现，不要靠加粗符号。

## X / Twitter

### 内容定位

X 不是长文摘要平台。适配时先把文章变成一个能在英文信息流里成立的观点、观察或框架。

优先突出：
- 一个 counterintuitive take
- 一个清晰的 builder/operator lesson
- 一个可复用 mental model
- 一个前后变化或具体结果
- 一个简短但有判断的 personal observation

X 内容必须使用自然英文。不要逐句翻译中文，不要保留中文平台语气，也不要把中文长段落硬拆成英文碎片。

### 格式选择

根据内容强度选择格式：

- Single post: 适合一个强判断、一个反常识观察、一个短故事结论。
- Thread: 适合有因果链、步骤、框架、经验复盘或多个例子的内容。
- Image post: 适合一句强观点加一张英文 quote/framework/contrast card。
- Image thread: 适合“文字 thread + 1-2 张框架图或对照图”。

默认优先输出 thread，因为一篇中文文章通常不需要被压成一条英文 post。只有当核心观点足够短、足够锋利时，才推荐 single post 作为首发。

### 英文写法

好的 X 英文应该：
- Short, direct, concrete.
- Use one idea per post.
- Sound like a person with a real point of view.
- Keep sentence rhythm varied: short claim, then context, then turn.
- Use plain words over abstract nouns.
- Preserve the author's judgment, not the original sentence order.

避免：
- "In today's fast-paced world..."
- "This article discusses..."
- "Here are some thoughts..."
- 过度使用 "unlock", "game-changer", "revolutionize", "10x" 等空泛增长黑话。
- 每条都用同一个句式开头。
- 过多 hashtag。默认 0 个，最多 2 个。

### 单帖

单帖要求：
- 280 characters 以内。
- 第一行必须有观点密度，不能是背景介绍。
- 可以用 1 个自然换行制造停顿。
- 必须独立成立，读者不看原文也能懂。

可用结构：
- Counterintuitive claim + why it matters.
- Personal discovery + broader lesson.
- Before/after contrast + takeaway.
- One sharp sentence + one concrete example.

### Thread

Thread 要求：
- 默认 3-7 条。
- 每条控制在 280 characters 以内。
- 第一条负责 hook：冲突、反常识、结果、问题或强判断。
- 中间每条只推进一个功能：解释、例子、框架、对比、行动建议。
- 最后一条要收束，不要只是“thanks for reading”。
- 可以编号，例如 `1/`、`2/`，但不要让编号压过内容。
- 不要把长文按段落机械切开；每条都要像可以在信息流里单独读懂的小单元。

Thread 常见结构：
1. Hook: the surprising or useful claim.
2. Context: what people usually get wrong.
3. Shift: the author's actual insight.
4. Example/framework: make it concrete.
5. Action/takeaway: what the reader can do or rethink.

### X 图文配图

X 配图不是必须，但当文章里有强框架、对照关系、短金句或可视化信息资产时，应提供 1-2 张英文配图方案。

先判断来源：
- 如果框架卡、quote card、contrast card 更合适，可以生成英文图文卡。
- 如果真实产品截图、真实界面、公开 demo、数据图或现场照片更有可信度，不要硬生成 AI 图；建议用户找图/截图，并说明具体应该找什么。
- X 的真实截图尤其适合用于产品观点、工具对比、界面体验、数据反馈和案例拆解。

推荐比例：
- 16:9: 适合框架图、简单流程、横向对照。
- 1:1: 适合 quote card、观点卡、单一视觉钩子。
- 4:5: 适合信息密度稍高的 framework card，在移动端占屏更大。

图片文字要求：
- 必须是英文。
- 短标题 + 可选副标题，或 3-5 个短标签。
- 不要把完整 thread 塞进图里。
- Quote card 标题建议 6-12 个英文单词。
- Framework card 建议最多 5 个节点或 2-3 列对照。

Prompt template:

```text
Generate one single X/Twitter image post asset, <ratio and size>.
Image type: <quote card / framework card / contrast card / diagram-like visual / editorial image>.
Main English text, exact: <headline or quote>
Optional small English subtitle or labels, exact: <subtitle or compact labels>
Topic: <article topic>
Audience: <target English-speaking audience>
Visual direction: clean editorial social-media image for X, high signal, readable on mobile, not a marketing banner.
Composition: one clear focal point, generous safe margins, strong text hierarchy if text is used, no clutter.
Visual elements: <framework, contrast, diagram, workspace, product UI, or metaphor relevant to the idea>
Palette and style: <style>
Constraints: create exactly one final image, not a carousel, not a grid, not a mockup preview. Preserve the specified English text accurately. Do not add extra text, logos, QR codes, watermarks, Chinese copy, or unrelated symbols.
```

### 发布建议

交付时给出一个明确推荐：
- Best version: single post / thread / image post / image thread.
- Why: one short reason.
- Optional reply prompt: one short English question to invite replies.

推荐要偏执行，不要输出一堆同权选项让用户再重新判断。
