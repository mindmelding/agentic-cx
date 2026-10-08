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

Under them: how many items closed today, how many are open, and the top three for tomorrow. Run `scripts/cx queue --expire --apply` to expire items untouched for 14 days.

If today held a decision a new teammate would not guess (a pass, a hold, a `never` line, a "no documentation" call), write a learning now in `local/learnings/YYYY-MM-DD-short-slug.md`, in the shape in [learnings](../../learnings/README.md), and add a row to `local/learnings/index.md`.

## Friday

Run `scripts/cx report`. It does the counting: the week's numbers, the kinds that clear the promotion bar, rungs that should have dropped, kinds with enough edits to judge as a rule, producers with five drops in a row, and bridges that stopped moving. Work from it, not from reading the log by eye. Then, in this order, asking before each change:

1. **Promotions.** For each kind that clears the bar in [`queue.md`](../../queue.md#promotion), propose the next rung: the kind, the rung now and next, the last 20 lines behind it, what would change, and how to undo it. On a yes, write it to `local/rungs.md`. Never above the ceiling.
2. **Rules.** The report lists kinds with three edits in 30 days. Where they are the same edit, propose a rule with its evidence. On a yes, add it to `local/rules.md` and write it where the next draft will read it.
3. **Producers.** Where five items in a row from one source or kind were dropped, propose narrowing that producer. On a yes, it becomes a rule.
4. **Expiring rules.** A rule past its expiry becomes an `upkeep` item.
5. **Bridges.** Flag any bridge whose number has not moved in four weeks, and propose retiring any whose exit is met. See [bridges](../../bridges.md#tracking-them-down).
6. **Learnings.** Promote or discard the week's day notes. At most five.
7. **Report.** Paste the `scripts/cx report` output into the day note, with one line on what you would change next week.

Do not rewrite the manual. Do not file an issue from here. Filing is triage.
