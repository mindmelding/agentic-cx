---
name: handoff-to-human
description: Load when the moment exceeds your authority, your knowledge, or your confidence, or when the customer asks for a person.
---

# Handoff to human

## When this is the moment

Anything in `guardrails/escalation.md`'s immediate list. A policy you can't cite. Two replies without convergence. The customer asks for a person. A sensitive action the operator hasn't granted. Your own confidence is under what the stakes require.

## Who holds it

The crossing itself: the agent hands the moment to a named person.

## Steps

1. Read rows 1, 2, 4 in full. You're about to summarize them.
2. Write the escalation note in the five-part shape from `guardrails/escalation.md`: who and context, the ask in their words, what's been told and promised with times, your best answer and confidence, what you need.
3. Tell the customer: the person's name, the reason in plain words, and the time by which they'll hear. If you can't name a time, name when you'll come back with one.
4. If the human is late, you follow up with the customer before they have to ask: "Priya's running behind; new time is 4pm. I'm sorry for the slip."
5. After the human resolves it, write back the outcome so the next agent doesn't start cold either.

## Guardrails

Never escalate without telling the customer. Never escalate "to the team"; escalate to a person. Never share internal notes verbatim with the customer as part of the handoff. If the escalation is because of a sensitive action, the nudge goes to the operator, not the customer.

## Example

**Good.** To the customer: "This one's above what I should answer alone; it changes your contract terms. Priya owns that. She has this whole thread and you'll hear from her by 2pm PT today. I'll make sure of it."

To Priya: "Dana at Acme (Pro, 2 years, healthy, renewal in 60 days). Asking for a 99.9% uptime commitment in writing after Tuesday's 43-minute outage. I've credited the month (ref 4480) and told her you'd reply by 2pm PT. I think we can offer the standard SLA addendum; not sure about the penalty clause she mentioned. Need: your call on the addendum, and the reply."

## Write back

Who it went to, when, the promise made to the customer, the human's outcome when known, and a flag that the customer has been handed off once on this thread (twice is a failure).

## Evals

- Must name a specific person and a time in the customer-facing message.
- Must include all five parts of the escalation note.
- Must not require the customer to restate anything.
