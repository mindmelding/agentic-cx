---
name: cx-close
description: End of day. Write the day note and carry over what is open. On Friday, read the week's log, propose rung promotions, propose rules from repeated edits, narrow producers that only make dropped items, and write the autonomy report. Use once at the end of the day.
---

# Close

Capture is cheap. Judgment waits for Friday. The queue, log, and rules are defined in [`queue.md`](../../queue.md).

## Every day

Write or finish `local/learnings/days/YYYY-MM-DD.md`. Five sections, one or two lines each, with item numbers as pointers. Leave a section empty rather than inventing an entry.

```markdown
# YYYY-MM-DD

## Landed
## Missed
## New situation
## Phrase
## Delight
```

Under them: how many items closed today, how many are open, and the top three for tomorrow. Expire items untouched for 14 days, unless blocked, with a line in the log.

If today held a decision a new teammate would not guess (a pass, a hold, a `never` line, a "no documentation" call), write a learning now in `local/learnings/YYYY-MM-DD-short-slug.md`, in the shape in [learnings](../../learnings/README.md), and add a row to `local/learnings/index.md`.

## Friday

Read the week's lines in `local/log.md`. Then, in this order, asking before each change:

1. **Promotions.** For each kind that clears the bar in [`queue.md`](../../queue.md#promotion), propose the next rung: the kind, the rung now and next, the last 20 lines behind it, what would change, and how to undo it. On a yes, write it to `local/rungs.md`. Never above the ceiling.
2. **Rules.** For each kind where the same edit shows up three times in 30 days, propose a rule with its evidence. On a yes, add it to `local/rules.md` and write it where the next draft will read it.
3. **Producers.** Where five items in a row from one source or kind were dropped, propose narrowing that producer. On a yes, it becomes a rule.
4. **Expiring rules.** A rule past its expiry becomes an `upkeep` item.
5. **Bridges.** Flag any bridge whose number has not moved in four weeks, and propose retiring any whose exit is met. See [bridges](../../bridges.md#tracking-them-down).
6. **Learnings.** Promote or discard the week's day notes. At most five.
7. **Report.** The table and three numbers from [`queue.md`](../../queue.md#the-friday-report), plus open bridges and how far each number has fallen, in the day note.

Do not rewrite the manual. Do not file an issue from here. Filing is triage.
