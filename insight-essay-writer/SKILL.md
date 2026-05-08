---
name: insight-essay-writer
description: Write or polish Chinese insight essays from a user's existing ideas, notes, scattered judgments, or rough outline. Use when the user wants a complete article in Nemo's reflective, judgment-driven writing style: clear thesis, phenomenon observation, why-it-matters reasoning, concrete examples, moderate sentence granularity, and a calm but opinionated tone. Do not use for interview-style idea extraction; use guided-writer first if the user's idea is still vague.
---

# Insight Essay Writer

Use this skill to turn already-available thoughts into a complete Chinese essay with Nemo's writing style: calm, sharp, grounded, explanatory, and readable.

This skill is for **drafting and polishing**, not long interviews. If the user's idea is still vague, first ask only the minimum clarifying questions or use `guided-writer`.

## Core Output

Produce a complete Markdown draft by default. If the user asks to edit an existing draft, revise the draft in place while preserving the user's core judgment.

Default shape:

1. **Observation hook**: Start from a concrete phenomenon the user noticed.
2. **Qualified stance**: Acknowledge why the phenomenon is understandable or valuable.
3. **Core judgment**: State the user's sharper view.
4. **Why this happens**: Explain the deeper motivation, system pressure, or mental model behind the phenomenon.
5. **Your framework**: Name 2-3 criteria, distinctions, or questions that define the user's view.
6. **Examples**: Use concrete work/life/product examples to make the framework visible.
7. **Contrast**: Explain what weaker versions get wrong.
8. **Ending**: Return to the title-level judgment with a clean, memorable closing.

Do not force every essay into all eight sections. Use them as a thinking path.

## Style Rules

- Write like a thoughtful practitioner explaining a real judgment, not like a marketing essay or academic article.
- The tone should be calm but opinionated. Avoid cheap outrage.
- A little literary feeling is allowed, but only lightly. Use it around key claims, transitions, and endings; do not make the whole essay lyrical, misty, or self-consciously poetic.
- Preserve nuance: criticize the weak version of an idea while acknowledging why the ambition behind it may be correct.
- Prefer concrete nouns and work scenes over abstract slogans.
- Use first-person judgment when natural: “我会有一个感觉”, “我越来越觉得”, “我不太买账”.
- Use headings sparingly. Headings should clarify argument turns, not decorate.
- Paragraphs should usually contain 2-5 sentences. Keep punchline sentences short, but merge explanatory sentences into natural paragraphs.
- Use short standalone lines only for important pivots, not every sentence.
- Avoid list-heavy writing unless the concept genuinely needs comparison or checklist form.
- Avoid generic AI phrases such as “在当今快速发展的时代”, “赋能”, “颠覆”, “革命性”, “打造闭环”.
- Avoid sentimental or over-literary phrasing that makes the piece feel contrived, such as excessive metaphors, decorative scenery, or phrases that sound beautiful but do not advance the judgment.

## Drafting Workflow

1. Identify the user's real claim:
   - What phenomenon are they reacting to?
   - What do they think people are missing?
   - What distinction do they want to introduce?
   - What standard do they want to establish?

2. Build the article spine:
   - Phenomenon: What is happening?
   - Empathy: Why do people do this?
   - Judgment: Why is it not enough?
   - Framework: What should we use to judge it?
   - Concrete scenes: Where does this show up?
   - Closing: What sentence should the reader carry away?

3. Draft in the user's voice:
   - Keep the user's specific terms.
   - Use their conceptual framing.
   - Do not replace their taste with generic industry language.
   - If the user gives a strong phrase, preserve it or make it slightly cleaner.

4. Polish rhythm:
   - Merge adjacent short explanation lines.
   - Keep key claims as standalone lines when they need weight.
   - Add literary texture only if it sharpens the thought or gives the ending a clean aftertaste.
   - Remove repeated claims that do not deepen the argument.
   - Check that every section advances the piece.

5. Final self-check:
   - Does the article have a real judgment, not just summary?
   - Does it explain why the criticized behavior is tempting?
   - Does it offer a better standard?
   - Does it include concrete scenes?
   - Does it sound like a person with taste, not a content machine?

## Reference

When the task requires matching this style closely, read `references/style-guide.md`.
