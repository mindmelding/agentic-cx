---
name: cx-learn
description: Write one learning as a Markdown file any agent can read later. Use when a decision is non-obvious, a check changes a rule, or a teammate would not guess what was decided.
---

# Learn

The record is [`learnings/`](../../learnings/README.md). Write the file. Do not leave the learning only in the chat, in a harness memory, or in a tool that another agent cannot open.

## Do this

1. Take one decision. If several are tangled, write the one that would be costly to forget and mention the others in a sentence.
2. Create `learnings/YYYY-MM-DD-short-slug.md` with this frontmatter and nothing else required below it:

```yaml
---
date: YYYY-MM-DD
responsibility: context | change | value | documentation | forensics | voice
kind: fact | flaw | boundary | rung | doc
summary: one sentence
decision: what was decided
evidence: where this came from, as a path, link, or quote
---
```

3. Add one row to `learnings/index.md`. Newest first. Columns: date, responsibility, summary, file.
4. Reply with the path. If the decision changes a `never` line, a rung, or what gets a page, name the responsibility page a person should update next. Do not update it unless they ask.
