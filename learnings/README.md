# Learnings

This folder is the memory. It is Markdown files in the repo. Any agent, in any harness, can read them by opening the files. Nothing in here requires a vendor memory, a vector store, or a chat transcript.

A learning is one decision worth keeping. The [learn](../skills/learn/SKILL.md) skill writes them. A person can write the same file by hand.

## One file

`learnings/YYYY-MM-DD-short-slug.md`

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

Prose under the frontmatter is optional. If the decision is not clear from `decision` and `evidence`, the file is not done.

## The index

[`index.md`](index.md) lists every learning, newest first. Agents should read the index before the files, and open a file only when the row is the one they need.

## Taking them somewhere else

Copy this folder. The skills in [`../skills`](../skills/README.md) know the shape. A harness that never sees those skills can still follow this page.
