---
name: cx-intake
description: Read what is new since the last pass. Split each item into a customer fact or a product flaw. Write both down and stop before anything is filed. Use at the start of the day or when new mail, a resolution, or a finding arrives.
---

# Intake

Read [`routines.md`](../../routines.md), [`responsibilities/context.md`](../../responsibilities/context.md), and [`responsibilities/voice.md`](../../responsibilities/voice.md). If `stack.md` exists, use the tools it names. If it does not, ask once where new signal lives, then continue.

## Do this

1. Read `learnings/index.md` and `voice-queue.md` so a repeat is not a new item.
2. Read only what is new since the last cursor. Mail, a sent resolution or workaround, and a flaw someone hit while doing the work.
3. For each thing, choose one:
   - **Context.** A fact about the customer. Write it with an author, a time, and a source, into the store `stack.md` names. If there is no store yet, append it to `context-inbox.md`.
   - **Voice.** A flaw in the product. Update one row in `voice-queue.md` using the item fields on the voice page. The same flaw increments the count and adds a quote.
   - **Skip.** Neither. Say so in one line and move on.
4. Save the cursor (the last message id, event id, or time) at the top of `voice-queue.md`.
5. Stop. Report how many facts and how many flaws. Tell the person to run triage. Do not file an issue. Do not edit a spec.

`voice-queue.md` and `context-inbox.md` stay on the machine. They are gitignored.
