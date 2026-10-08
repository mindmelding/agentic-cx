---
name: cx-open
description: Start of day. Read what is new since the last open, turn each thing into a queue item, carry out anything whose kind runs on its own, and post the top five. Use once each morning, by a person or on a schedule.
---

# Open

This fills the queue. [Triage](../triage/SKILL.md) works it. The queue, kinds, and rungs are in [`queue.md`](../../queue.md).

Read `stack.md`, `local/queue.md`, `local/rungs.md`, `local/rules.md`, `local/bridges.md`, yesterday's day note in `local/learnings/days/`, and `local/learnings/index.md`.

## Do this

1. **Read what is new** since the cursor at the top of `local/queue.md`, from the sources in `stack.md`:
   - customer mail and threads waiting on us,
   - the ledger: reversals, edit distance rising, stall signals, silences, classes that meet the promotion bar,
   - commits that touched a spec's `sources`,
   - incidents graded by forensics.
2. **Make items.** One per thing, with the fields in [`queue.md`](../../queue.md#an-item). A repeat of an open item updates it (a flaw's count, a new quote) rather than adding another. Apply the producer rules in `local/rules.md`: a muted source makes nothing.
3. **Listen for bridges.** When the same question has reached the team three times in 30 days and neither the agent nor the product can answer it, add a `bridge` item proposing the smallest thing that answers it today, and a `flaw` item asking product to make it unnecessary. See [bridges](../../bridges.md#where-bridges-come-from).
4. **Add today's cadence items.** On their day, the weekly and quarterly loops from the responsibility pages become `check`, `value`, or `upkeep` items: the boundary check, the idle-fact list, rereading holds, the renewal story for an account in motion, and each bridge's weekly review from `local/bridges.md`.
5. **Expire.** Run `scripts/cx queue --expire --apply`.
6. **Carry out what runs on its own.** Items whose kind sits at act-with-notice or act-silently in `local/rungs.md` are done now, never a sensitive one. Log each in `local/log.md` with disposition `done`.
7. **Save the cursor.**
8. **Post the board** from `scripts/cx queue --top 5`. At most eight lines:
   - what was done on its own, with item numbers and how to undo,
   - the top five open items,
   - how many are blocked, and the oldest open item.

Then stop. Working the queue is triage.

## On a schedule

When open runs headless, write the board to the top of today's day note instead of posting it. Do nothing a person has to see first.
