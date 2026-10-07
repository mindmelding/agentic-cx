---
name: first-reply
description: Load when replying to a person we have never spoken to before, in any channel.
---

# First reply

## When this is the moment

The context contract returns nothing on row 2 for this person, or they say "first time writing in." It might still be a known account (a new user at an existing customer), so check row 4 before you assume the whole relationship is new.

## Who holds it

The agent, alone.

## Steps

1. Read rows 2, 3, 4 of `context/CONTRACT.md`. If row 4 shows an existing account, read row 1 too; we might owe their team something.
2. Answer. If you can't yet, say who will and by when (p03).
3. Match their register (p09). If they wrote two lines, you write two to four.
4. If you're an agent and it's a channel where that matters, say so once, plainly (p12). Don't lead with it.
5. Write back: row 3 identity details, their stated goal if they gave one (row 8), and the touch note.

## Guardrails

Nothing sensitive on a first reply without a nudge; you don't yet know who this person is relative to the account. No "welcome to the family." No survey link.

## Example

**Good.** "Hi Ana. Exports live under Settings, then Data, then the Export button top right. CSV and JSON both work. If you're pulling this weekly, tell me and I'll set up the scheduled version so you don't have to. I'm Sam, and I'll be your reply on this thread."

## Write back

Name as signed, role if stated, channel, timezone from the thread, the question, the goal if they said one, and the touch note.

## Evals

- Must answer or commit to a when-and-who in sentence one.
- Must not ask for anything already in the signup record or the account file.
- Must not use a banned opener or "welcome" boilerplate.
