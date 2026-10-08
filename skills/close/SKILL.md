---
name: cx-close
description: End of day. Write the day note, name what is still open, and on Friday promote at most a few of those notes into learnings. Use once at the end of the day. Do not start new work.
---

# Close

Run this at the end of the day. Capture is cheap. Judgment waits for Friday, except when a decision would be costly to forget overnight.

## The day note

Write or finish `local/learnings/days/YYYY-MM-DD.md`. Five sections, one or two lines each, with a pointer (a thread, a queue row, a commit), then `Still open`. Leave a section empty rather than inventing an entry.

```markdown
# YYYY-MM-DD

## Landed
## Missed
## New situation
## Phrase
## Delight
## Still open
```

Under `Still open`, one bullet per thing still open tomorrow: voice rows whose `State` is `open`, and specs still unverified. That list is the start of tomorrow's open, and `scripts/cx status` counts it.

## A decision that should not wait

If today included a pass, a hold, a `never` line, or a "no documentation" call that a new teammate would not guess, write one learning now. Do not leave it only in the day note.

Create `local/learnings/YYYY-MM-DD-short-slug.md`:

```yaml
---
date: YYYY-MM-DD
responsibility: onboarding | context | change | value | documentation | forensics | voice | floor
kind: fact | flaw | boundary | rung | doc
summary: one sentence
decision: what was decided
evidence: path, link, or quote
---
```

Add one row to `local/learnings/index.md`, newest first. Columns: date, responsibility, summary, file.

## Friday

After the day note, do the weekly pass. Cap it at five:

1. Specs still unverified.
2. Voice holds whose count went up.
3. Day notes from the week that should become a learning, or should be discarded.

Ask before promoting a note into a learning file. Discard in one line on the day note. Do not rewrite the manual. Do not file an issue from here. Filing is triage.
