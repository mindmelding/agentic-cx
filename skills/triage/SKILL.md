---
name: cx-triage
description: Work the queue. Take the top item, load its handler, do or draft the work at the item's rung, ask at most one decision, log what the operator did, and move to the next. Use for setup and for every workday after it. When a customer pings directly, floor is faster.
---

# Triage

The whole day runs through this skill. The queue, the kinds, the rungs, and the log are defined in [`queue.md`](../../queue.md). Read it once per session.

## Start

1. Read `local/queue.md`, `local/rungs.md`, and `local/rules.md`. If the queue does not exist, say so and offer [open](../open/SKILL.md), or [setup](../../skill/SKILL.md) if there is no `stack.md`.
2. Run `scripts/cx queue`. It prints open items in triage order and any item whose fields, kind, or rung are wrong. Fix the problems before working the queue. Skip `blocked` items, but say how many there are.

## For each item

1. **Show it.** One line: the item number, kind, account, and why now.
2. **Load the handler** named on the item, and the rules in `local/rules.md` that apply to this kind.
3. **Work at the item's rung.** The rung is the lower of the kind's rung in `local/rungs.md` and its ceiling in [`queue.md`](../../queue.md#kinds). A sensitive item is always propose.
   - **Propose:** say what you would do and why, in two or three lines. Ask yes or no.
   - **Draft:** prepare the whole thing (the reply, the fact, the issue, the disposition). Show it. Ask: send as is, edit, or reject.
   - **Act with notice or silently:** do it, and say in one line what you did and how to undo it.
4. **Carry it out** on a yes, or with the operator's edit. Anything sent outside the company follows [`floor/guardrails/authority.md`](../../floor/guardrails/authority.md).
5. **Log it.** Add `touched:` to the item if it stays open. When it closes, set its status and write one line in `local/log.md`, in the format in [`queue.md`](../../queue.md#the-log). If the operator edited, write what changed in one line. That line is what the system learns from.
6. **Demote if it was wrong.** A rejection because the work was wrong, or a reversal, drops the kind one rung in `local/rungs.md`. Say so in one line.
7. **Capture.** A new fact, flaw, or follow-up the item revealed becomes a new item, not a side note.
8. **Next.**

Stop when the queue is empty, when the operator says stop, or after 25 items. Then say what is left at the top.

## By kind

Most kinds follow their handler page. Two need more here.

### `flaw`

1. Show the flaw, the quote, the count, the resolution, and whether an issue already exists in the tracker `stack.md` names.
2. Ask: pass, or hold.
3. On hold, write the reason on the item and set it `blocked` until its count rises.
4. On pass, show the issue in the shape on the [voice](../../responsibilities/voice.md) page. File it only after a yes. If an issue already covers it, comment with the new quote and count instead.
5. Later evidence on a passed flaw becomes a `flaw-evidence` item, which can climb to act silently.

### `doc-decision`

1. Show the diff beside the spec's current `may` and `never`.
2. Ask for one disposition from the [documentation](../../responsibilities/documentation.md) page: no page, a promise line, a guide, an update, or a removal.
3. A change to a `never` line is sensitive. It always waits for a yes.

## Before you finish

If a decision today would surprise someone who was not here, add one line to today's day note in `local/learnings/days/`, and say close should look at it.
