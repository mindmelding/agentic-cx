---
name: cx-open
description: Start of day. Read what is new, split facts from product flaws, and leave a short board of what to handle today. Use once each morning. Do not file anything.
---

# Open

Run this at the start of the day. It replaces a second morning meeting.

Read [`routines.md`](../../routines.md), [`responsibilities/context.md`](../../responsibilities/context.md), and [`responsibilities/voice.md`](../../responsibilities/voice.md). Use `stack.md` when it exists.

## Do this

1. Read yesterday's day note if it exists: `local/learnings/days/`. Read `local/learnings/index.md` and `voice-queue.md` so a repeat is not a new item.
2. Read only what is new since `cursor` in the front matter of `voice-queue.md`. Mail, a resolution or workaround, and a flaw from the work.
3. For each thing, choose one:
   - **Context.** A fact about the customer. Write it with an author, a time, and a source into the store `stack.md` names. If there is no store yet, add a row to the table in `context-inbox.md`.
   - **Voice.** A flaw in the product. Update one row in the `voice-queue.md` table, in the columns it already has. The same flaw increments `Count` and adds a quote. A new row starts with `Count` 1, your pass or hold in `Proposal`, and `State` `open`.
   - **Skip.** Say so in one line.
4. Set `cursor` to the time of the newest thing you read, ISO 8601 with its offset.
5. Post the board, and stop. At most five lines: what arrived, what is still open (holds, unverified specs, stalled onboardings with no person or skip), and which of the two daytime skills to use first (`floor` if someone is waiting, `triage` if a decision is waiting). Do not file an issue. Do not edit a spec.

`voice-queue.md`, `context-inbox.md`, and `local/` stay on the machine. Their shapes are in [`templates/house/state/`](../../templates/house/state/README.md). Write a `|` inside a cell as `\|`.
