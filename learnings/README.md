# Learnings

Two layers.

**The shape is in this folder.** It is committed, company-agnostic, and enough for any agent to write a valid learning without loading a skill.

**The record is in `local/learnings/`.** It is gitignored. It holds the day notes and the promoted decisions for one company. Copy `local/` onto another machine, or point another harness at it. Do not commit it. Customer words do not belong in the public manual.

This is the same split as [front-of-house](https://github.com/scmancillas/front-of-house): the canon is shared, and what a house learns stays in its overlay. Here the overlay is `local/learnings/`. Close writes it. Floor appends a line during the day when a phrase or a miss should not wait until evening.

## A day note

`local/learnings/days/YYYY-MM-DD.md`

Sections, each allowed to be empty: Landed, Missed, New situation, Phrase, Delight. Then what is still open tomorrow.

## A learning

`local/learnings/YYYY-MM-DD-short-slug.md`

```yaml
---
date: YYYY-MM-DD
responsibility: context | change | value | documentation | forensics | voice
kind: fact | flaw | boundary | rung | doc
summary: one sentence
decision: what was decided
evidence: path, link, or quote
---
```

[`index.md`](index.md) in this folder is the empty template. The live index is `local/learnings/index.md`, newest first. Agents read that index before opening a file.
