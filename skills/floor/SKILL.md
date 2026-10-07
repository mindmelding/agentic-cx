---
name: cx-floor
description: During the day, when a customer is in front of you. Read their file, handle one moment from the floor canon, and capture a fact or a flaw if the moment produced one. Use for a reply, a bug, a request, a renewal, or a silence. Not for the morning board or the evening note.
---

# Floor

This is the work between open and close. One moment at a time.

The canon is in [`floor/`](../../floor/README.md), in this repo.

## Load

1. Read [`floor/MINDSET.md`](../../floor/MINDSET.md) and [`floor/PRECEDENCE.md`](../../floor/PRECEDENCE.md).
2. Read the customer's file before choosing a moment and before drafting. Use the context store in `stack.md`, through the rows in [`floor/context/CONTRACT.md`](../../floor/context/CONTRACT.md). If the file is empty, say so. Do not invent what they care about.
3. Pick one playbook from [`floor/moments/README.md`](../../floor/moments/README.md). Load a second only when the thread is clearly two moments. Most threads are `small-moment`.
4. Draft from that playbook. Anything sensitive (money, access, deletion, personal data, anything that leaves the building) waits for an explicit yes. See [`floor/guardrails/authority.md`](../../floor/guardrails/authority.md).
5. If the file supports a gesture in [`floor/delight/catalog.md`](../../floor/delight/catalog.md), and delight history does not already contain it, offer it after the reply is true. Thin evidence means skip it.

## Record the moment

The playbook slug is part of the action. When a ledger row is written, set `moment` to that slug beside the action class and the rung. A product action with no person in the thread leaves `moment` empty.

## Capture

Do not wait for close.

- A fact about them goes to context, the same way [open](../open/SKILL.md) writes a fact.
- A bug, a feature request, or our mistake also becomes or updates one row in `voice-queue.md`. The reply can still go out. The flaw is not only a reply.
- A phrase they used, or a reply you would not have written the same way twice, gets one line in today's day note under `local/learnings/days/`. Create the file from the sections in [close](../close/SKILL.md) if it is not there yet. Include the moment slug.

If the moment needs a pass, a hold, or a documentation call, say so and stop. That is [triage](../triage/SKILL.md), not this skill.
