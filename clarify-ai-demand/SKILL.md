---
name: clarify-ai-demand
description: Use when the user has a vague need, workflow pain, product idea, Agent idea, automation request, or Prompt-writing goal and wants help clarifying it before execution. This skill guides the AI to first restate, question, and progressively understand the demand, then turn it into a concrete minimum usable scenario, tool shape, inputs, outputs, boundaries, and next-step Prompt or implementation brief.
---

# AI 需求校准

## Overview

This skill helps users avoid rushing into Prompt writing or implementation before the need is clear. It treats AI as a demand-calibration partner: first let AI say what it understood, then use progressive questions to turn a vague wish into a usable tool plan.

Use this skill especially when the user says things like:
- “我想做一个 AI 工具/Agent，但还没想清楚。”
- “帮我写一个 Prompt” but the task is broad or ambiguous.
- “我想用 AI 提效/自动化这个工作流。”
- “我有一个需求，你先帮我理一下。”
- “先别急着做，帮我看看这个需求到底是什么。”

## Core Principle

Do not start by writing the final Prompt, product spec, or implementation plan.

Start by helping the user see what their need actually is.

The default first response should include a short restatement:

> 我先说说我听懂了什么。

Then surface uncertainty:

> 这里我还不确定的地方是...

Then ask the most useful next question.

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

### Step 3: Ask Calibration Questions

Ask one to three questions at a time. Prefer concrete questions over abstract strategy.

Use these six questions as the default checklist:

1. Who will use this, and in what exact moment?
2. What messy input does the user already have?
3. What decision or output should the tool produce?
4. What would make the result “good enough”?
5. What should the tool explicitly not do?
6. How will the user use the result in the next step?

If the user is stuck, offer two or three candidate interpretations and ask them to choose or revise.

### Step 4: Find The Minimum Usable Scenario

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

### Step 5: Convert Into A Tool Brief

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

## Response Style

- Be conversational, not consultant-like.
- Use “我先说说我听懂了什么” as the default opening move.
- Treat early conclusions as hypotheses, not final answers.
- Push for concreteness without interrogating the user.
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

我想先确认一个问题：
你最卡的是写之前的选题判断，写的时候的表达，还是写完之后的数据复盘？
```

After the user answers, continue calibration and only then produce the tool brief or Prompt.
