---
name: clarify-ai-demand
description: Use whenever the user is describing, analyzing, clarifying, sorting out, discussing, or exploring a need, requirement, workflow pain, product idea, Agent idea, automation request, tool request, or Prompt-writing goal. Trigger even if the user only says they want to "分析需求", "梳理需求", "描述需求", "聊聊需求", "看看这个需求", "做个工具", "做个 Agent", or "写个 Prompt". The skill progressively understands the demand, searches for relevant existing skills or references when possible, asks whether found skills match the user's intended outcome, then turns the need into a minimum usable scenario, tool shape, inputs, outputs, boundaries, and next-step Prompt or implementation brief.
---

# AI 需求校准

## Overview

This skill helps users avoid rushing into Prompt writing or implementation before the need is clear. It treats AI as a demand-calibration partner: first let AI say what it understood, search for relevant existing skills or references, then use progressive questions to turn a vague wish into a usable tool plan.

Use this skill especially when the user says things like:
- “我想做一个 AI 工具/Agent，但还没想清楚。”
- “帮我写一个 Prompt” but the task is broad or ambiguous.
- “我想用 AI 提效/自动化这个工作流。”
- “我有一个需求，你先帮我理一下。”
- “先别急着做，帮我看看这个需求到底是什么。”
- “帮我分析/梳理/描述一下这个需求。”
- “这个需求能不能做成一个 skill/Agent/工具？”
- “我想找找有没有现成 skill 可以参考。”

## Core Principle

Do not start by writing the final Prompt, product spec, or implementation plan.

Start by helping the user see what their need actually is.

While clarifying the demand, also look outward: if the request resembles a reusable skill, workflow, template, or known capability, try to find existing skills that can be referenced or installed.

The default first response should include a short restatement:

> 我先说说我听懂了什么。

Then surface uncertainty:

> 这里我还不确定的地方是...

Then ask the most useful next question.

If skill discovery is useful, also say:

> 我也会顺手找找有没有现成 skill 可以参考，看看它们达成的效果是不是你想要的。

## Workflow

### Step 1: Restate What You Heard

Translate the user's vague expression into a clearer hypothesis.

Cover:
- what problem the user seems to want to solve
- who uses it
- when it happens
- what pain or repeated decision it may reduce
- what the output might be

Keep this tentative. Use phrases like:
- “我理解你不是想要 X，而是更像想解决 Y。”
- “如果我没理解错，这个需求的核心不是生成内容，而是减少判断成本。”
- “这个需求现在还像一个愿望，不像一个工具任务。”

### Step 2: Identify The Demand Type

Classify the need into one primary type:
- **判断型**: help choose, prioritize, evaluate, decide next action
- **整理型**: turn messy inputs into structured assets
- **生成型**: produce text, images, plans, scripts, or deliverables
- **复盘型**: analyze feedback and extract lessons or next moves
- **监控型**: watch signals and notify or summarize
- **执行型**: perform a concrete repeated operation

If multiple types apply, choose the one that creates the most user value first. Avoid building a “万能助手” unless the user explicitly needs broad exploration.

### Step 3: Search For Relevant Skills Or References

When the demand may map to an existing reusable capability, search for skills before inventing everything from scratch.

Use available discovery paths in this order:
- If a `find-skills` skill or equivalent local capability is available, use its workflow.
- If command execution is available, run targeted searches such as `npx skills find [query]`.
- Check public skill directories such as skills.sh or SkillHub-like platforms when accessible.
- If no search capability is available, say so briefly and continue with demand clarification from first principles.

Search with keywords derived from the demand type and domain. For example:
- content planning demand -> `npx skills find content writing`
- React performance demand -> `npx skills find react performance`
- spreadsheet reporting demand -> `npx skills find spreadsheet report`
- PDF/document workflow -> `npx skills find pdf docx`

Return found candidates in a compact form:

```markdown
我找到几个可能相关的 skill：
1. skill/package:
   - 它解决什么：
   - 可能适合你的地方：
   - 安装/查看：
2. ...

你想要的是更接近其中哪个效果？
```

Do not treat discovered skills as final answers. Use them as mirrors for requirement clarification:
- “这个 skill 达成的效果，是你想要的吗？”
- “你想要它的哪一部分，不想要哪一部分？”
- “如果它不够贴合，我们需要补的差异是什么？”

If no relevant skill is found, state that clearly, then proceed to design the minimum usable scenario.

### Step 4: Ask Calibration Questions

Ask one to three questions at a time. Prefer concrete questions over abstract strategy.

Use these six questions as the default checklist:

1. Who will use this, and in what exact moment?
2. What messy input does the user already have?
3. What decision or output should the tool produce?
4. What would make the result “good enough”?
5. What should the tool explicitly not do?
6. How will the user use the result in the next step?

If the user is stuck, offer two or three candidate interpretations and ask them to choose or revise.

### Step 5: Find The Minimum Usable Scenario

Before proposing a full product, identify the smallest scenario where the tool can be genuinely useful.

Output this in one compact block:

```markdown
最小可用场景：
- 使用者：
- 触发时刻：
- 输入：
- AI 要做的判断/处理：
- 输出：
- 下一步动作：
- 不做什么：
```

The scenario should be small enough to test quickly, but meaningful enough that the user would actually reuse it.

### Step 6: Convert Into A Tool Brief

Once the scenario is clear, produce a practical brief:

```markdown
工具名称：
解决的问题：
目标用户：
核心流程：
1. ...
2. ...
3. ...
输入字段：
- ...
输出格式：
- ...
边界条件：
- ...
成功标准：
- ...
第一版 Prompt / Agent 指令：
...
```

If the user wants implementation, continue into code or product design only after this brief is agreed.

When relevant skills were found, include a short comparison:

```markdown
可参考 skill：
- 最接近的是：
- 可以借鉴：
- 不适合/需要改造：
- 我建议第一版自己做成：
```

## Response Style

- Be conversational, not consultant-like.
- Use “我先说说我听懂了什么” as the default opening move.
- Treat early conclusions as hypotheses, not final answers.
- Push for concreteness without interrogating the user.
- Search for relevant skills when the need sounds reusable, and use candidates to help the user confirm the desired outcome.
- Do not overbuild. Prefer a small useful tool to a grand undefined Agent.
- When the user asks only for a Prompt, still check whether the demand is clear enough before writing it.

## Example

User:
“我想做一个帮我写小红书的 Agent。”

Good response:

```markdown
我先说说我听懂了什么。

你表面上想要的是“小红书文案生成”，但我不确定真正的痛点是不是写正文。它可能更像是：每天不知道写什么、素材太散、发完之后不知道怎么复盘。

所以我会先把它理解成一个内容工作流需求，而不是单纯的文案生成需求。

我也会顺手找找有没有现成的写作/内容工作流 skill 可以参考。找到之后我会把它们的效果列出来，你可以判断：你想要的是不是这种能力。

我想先确认一个问题：
你最卡的是写之前的选题判断，写的时候的表达，还是写完之后的数据复盘？
```

After the user answers, continue calibration and only then produce the tool brief or Prompt.
