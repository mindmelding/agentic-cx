---
name: cx-floor
description: During the day, when a customer is in front of you. Read their file, decide whether the agent or a person holds the moment, draft from the floor canon, and capture a fact or a flaw if the moment produced one. Use for a reply, a bug, a request, a renewal, a silence, or a stalled onboarding. Not for the morning board or the evening note.
---

# Floor

This is the work between open and close. One moment at a time. The agent handles most moments alone. This skill is mostly how a person on the team spends the time that frees: the moments that need a person, and going first.

The canon is in [`floor/`](../../floor/README.md), in this repo.

## Load

1. Read [`floor/MINDSET.md`](../../floor/MINDSET.md) and [`floor/PRECEDENCE.md`](../../floor/PRECEDENCE.md).
2. Read the customer's file before choosing a moment and before drafting. Use the context store in `stack.md`, through the rows in [`floor/context/CONTRACT.md`](../../floor/context/CONTRACT.md). If the file is empty, say so. Do not invent what they care about.
3. Pick one playbook from [`floor/moments/README.md`](../../floor/moments/README.md). Load a second only when the thread is clearly two moments. Most threads are `small-moment`.
4. Check who holds it, in [`floor/README.md`](../../floor/README.md#who-holds-the-moment), after any change in the overlay. If a person holds it, draft for that person and say so: the draft, the file in three lines, and what to decide. The person sends. If the agent holds it, draft to send.
5. Draft from that playbook. Anything sensitive (money, access, deletion, personal data, anything that leaves the building) waits for an explicit yes. See [`floor/guardrails/authority.md`](../../floor/guardrails/authority.md).
6. If the file supports a gesture in [`floor/delight/catalog.md`](../../floor/delight/catalog.md), and delight history does not already contain it, offer it after the reply is true. Thin evidence means skip it.

## Going first

When no one is waiting, work the lists before the inbox: the stall list from [onboarding](../../responsibilities/onboarding.md), then accounts that went quiet (`silence`), then a first clean autonomous run worth telling the customer about. One moment at a time, the same way.

## Record the moment

The playbook slug is part of the action. Record who held it, `agent` or `person`. When a ledger row is written, set `moment` to that slug beside the action class and the rung. A product action with no person in the thread leaves `moment` empty.

## Capture

Do not wait for close.

- A fact about them goes to context, the same way [open](../open/SKILL.md) writes a fact.
- A bug, a feature request, or our mistake also becomes or updates one row in `voice-queue.md`. The reply can still go out. The flaw is not only a reply.
- An edit a person made to the agent's draft is a lesson. If it would change the next draft, one line in the day note. If the agent got it wrong in a way a test could catch, propose an eval case.
- A phrase they used, or a reply you would not have written the same way twice, gets one line in today's day note under `local/learnings/days/`. Create the file from the sections in [close](../close/SKILL.md) if it is not there yet. Include the moment slug.

If the moment needs a pass, a hold, or a documentation call, say so and stop. That is [triage](../triage/SKILL.md), not this skill.
