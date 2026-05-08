---
name: text-card-renderer
description: Deterministically render exact Chinese text into SVG and PNG social cards. Use for 小红书备忘录图, 苹果备忘录风长文字图, 公众号逻辑图, X 信息图, 金句图, 清单图, 框架图, 对照图, or whenever image text must be accurate and should not use AI image generation.
---

# Text Card Renderer

Use this instead of AI image generation when text accuracy matters.

Default sizes:
- 小红书：1080x1440
- 公众号封面：900x383
- 公众号正文图：1200x675 or 1200x900
- X 图文卡：1600x900

Always save both SVG source and PNG output.

## Command

```bash
python3 Nemo-skills/text-card-renderer/scripts/render_text_card.py \
  --spec path/to/card.json \
  --out path/to/card.png
```

The script writes a sibling `.svg` beside the PNG.

## Layouts

- `note`: highest priority for 小红书文字图. Apple Notes-like long text card for 3-6 short paragraphs.
- `cover`: title-led cover.
- `quote`: strong sentence + short explanation.
- `stack`: vertical checklist/framework.
- `cards`: comparison or entry map.

For 小红书文字图, default to `note` unless the content is clearly a table, checklist, matrix, framework, or comparison.

## Minimal Note Spec

```json
{
  "width": 1080,
  "height": 1440,
  "layout": "note",
  "date": "AI 入口观察",
  "title": "聊天框不够用了",
  "paragraphs": [
    "第一段文字。",
    "第二段文字。",
    "第三段文字。"
  ]
}
```

After rendering, inspect the PNG for text accuracy, line breaks, spacing, and platform ratio.
