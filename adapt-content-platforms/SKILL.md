---
name: adapt-content-platforms
description: Transform a source article into platform-native content packages for Xiaohongshu and WeChat Official Account. Use when the user provides an article, draft, transcript, notes, or long-form idea and asks to adapt, repurpose, distribute, package, or rewrite it for 小红书, 微信公众号, 新媒体, multi-platform publishing, titles, cover images, carousel images, captions, or social media content.
---

# 全平台内容自适应

将一篇文章改造成可发布的平台内容包。目前只支持：
- 小红书
- 微信公众号

默认一次性输出两个平台的完整方案。不要只做摘要；要完成标题、图片方案、正文与发布细节。

## Core Workflow

1. **读懂原文**
   - 提取核心观点、读者痛点、反常识点、金句、故事/案例、行动建议。
   - 判断文章更适合的主叙事：观点型、经验复盘型、教程型、趋势观察型、情绪共鸣型。
   - 保留作者的真实判断，不要把原文洗成泛泛的 AI 内容。

2. **拆成平台资产**
   - 小红书：先抓点击，再用图文卡片降低阅读门槛。
   - 微信公众号：先建立阅读理由，再用完整结构承接深度。
   - 图片输出要给出可直接交给设计/生图工具的规格、文案、构图、风格和每张图的文字内容。

3. **按固定结构交付**
   - 先输出“小红书”，再输出“微信公众号”。
   - 如用户明确只要某个平台，只输出该平台。
   - 如用户要求真实生成图片，优先调用可用的图片生成能力；否则输出图片 brief 与图中文字。

4. **做发布前检查**
   - 标题长度合规。
   - 小红书封面金句不超过 10 个字。
   - 小红书正文像真人发帖，不像公众号摘要。
   - 微信公众号正文保留深度，不像短视频口播稿。

## Xiaohongshu Output

Use the detailed card and copy rules in `references/platform-spec.md` when producing Xiaohongshu deliverables.

Output exactly these sections:

### 小红书标题

Generate 3-5 titles:
- 20 个中文字符以内
- 有网感，但不做低质标题党
- 每个标题要走不同角度：情绪、反差、结果、身份代入、观点判断
- 可以使用口语词，但不要堆砌感叹号

### 小红书封面图

Provide one cover image plan:
- 比例：优先 3:4 竖版
- 建议尺寸：1080x1440 或同等 3:4 高清尺寸
- 封面文字：10 个字以内，必须来自或忠于文章最强金句
- 画面要让人 1 秒看懂“这篇在讲什么”
- 输出：封面金句、视觉风格、构图、配色、主体元素、生图提示词或设计 brief

### 小红书内容图

Create 2-5 carousel cards:
- 与封面保持同一比例和同一视觉系统
- 每张只表达一个重点，不要把文章塞满
- 从文章中摘抄或改写重点内容；可以压缩，但不要篡改观点
- 输出每张图的：卡片标题、卡片文字、视觉建议

### 小红书正文

Write a platform-native caption:
- 300-800 字为默认范围；复杂文章可更长，但要分段短
- 开头 2-3 行先给情绪/冲突/结果，不要铺背景
- 使用适量 emoji，通常每 1-3 段一个即可；不要每句都加
- 语气像真实创作者分享：具体、轻一点、有判断
- 结尾带互动问题或轻 CTA
- 带 5-8 个话题，混合大词、细分词、内容主题词

## WeChat Official Account Output

Use the detailed long-form rules in `references/platform-spec.md` when producing WeChat deliverables.

Output exactly these sections:

### 公众号标题

Generate 3-5 titles:
- 25 个中文字符以内
- 有网感，但更克制、可信、适合深读
- 覆盖不同标题路线：判断型、解释型、反差型、问题型、金句型
- 避免“震惊、必看、没人告诉你”等廉价刺激词

### 公众号封面图

Provide one cover image plan:
- 比例：优先 2.35:1 横版，常用尺寸 900x383 或等比高清尺寸
- 不用强调文字；除非标题本身很短且用户要求加字
- 更像文章气质的视觉入口：干净、可读、主题明确
- 输出：视觉风格、构图、配色、主体元素、生图提示词或设计 brief

### 公众号正文

Rewrite the article for WeChat reading habits:
- 保留完整观点链路，不要只做平台摘要
- 开头要有 hook：场景、冲突、判断、问题或个人触发点
- 用清晰小标题组织阅读节奏
- 段落短一些，但逻辑要连续
- 适当保留原文金句和例子
- 结尾回到主判断，并给读者一个可带走的洞察

## Output Template

```markdown
## 小红书

### 小红书标题
1. ...
2. ...

### 小红书封面图
- 比例/尺寸：
- 封面金句：
- 视觉 brief：
- 生图提示词：

### 小红书内容图
1. 卡片标题：
   卡片文字：
   视觉建议：

### 小红书正文
...

话题：#... #...

## 微信公众号

### 公众号标题
1. ...
2. ...

### 公众号封面图
- 比例/尺寸：
- 视觉 brief：
- 生图提示词：

### 公众号正文
...
```

## Quality Bar

- 不要让两个平台的标题只是同义改写。
- 不要把小红书正文写成“本文主要讲了”。
- 不要把公众号正文写成小红书正文的加长版。
- 图片卡片文字必须少而准；宁可 3 张干净图，也不要 5 张拥挤图。
- 若原文信息不足，先基于原文生成可用版本，并标注“可补充的信息”，不要卡住不输出。
