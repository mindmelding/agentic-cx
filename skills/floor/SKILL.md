---
name: cx-floor
description: During the day, when a customer is in front of you. Read their file, handle one moment, and capture a fact or a flaw if the moment produced one. Use for a reply, a bug, a request, a renewal, or a silence. Not for the morning board or the evening note.
---

# Floor

This is the work between open and close. One moment at a time.

The hospitality canon lives in [front-of-house](https://github.com/scmancillas/front-of-house). Use it when it is on disk. Do not copy it into this repo. This repo decides what happens to a fact and a flaw. That repo decides how the reply is written.

## Find the canon

First match wins:

1. The `front_of_house` path in `stack.md`.
2. A checkout named `front-of-house` next to this repo, or at `~/Documents/GitHub/front-of-house`.

If none of those exist, follow the short rules below and say the canon is not loaded.

## When the canon is loaded

1. Read `MINDSET.md`.
2. Read the customer's file before drafting. Use the context store in `stack.md`. If it is empty, say so. Do not invent what they care about.
3. Pick one playbook from `moments/README.md`. Load a second only when the thread is clearly two moments. Most threads are `small-moment`.
4. Draft from that playbook. Anything sensitive (money, access, deletion, personal data, anything that leaves the building) waits for an explicit yes.
5. After the moment, capture. Do not wait for close.
   - A fact about them goes to context, the same way [open](../open/SKILL.md) writes a fact.
   - A bug, a feature request, or our mistake also becomes or updates one row in `voice-queue.md`. The reply can still go out. The flaw is not only a reply.
   - A phrase they used, or a reply you would not have written the same way twice, gets one line in today's day note under `local/learnings/days/`. Create the file from the sections in [close](../close/SKILL.md) if it is not there yet.

## When the canon is not loaded

Read the file. Answer the thing in the first sentence. Do not invent a policy or a date. Then do step 5 above.

If the moment needs a pass, a hold, or a documentation call, say so and stop. That is [triage](../triage/SKILL.md), not this skill.
