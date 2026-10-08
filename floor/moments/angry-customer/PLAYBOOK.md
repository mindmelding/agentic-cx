---
name: angry-customer
description: Load when the message carries heat, the thread has gone bad, or the customer says words like "unacceptable," "third time," or "cancel."
---

# Angry customer

## When this is the moment

Tone, caps, "unacceptable," a thread with three or more unresolved replies, an exec joining the thread, or a mention of cancelling or lawyers. Check row 2 for the history; the anger usually has a longer story than the last message.

## Who holds it

A person. The agent drafts.

## Steps

1. Read rows 1, 2, 4 fully. Reconstruct the story. Count how many times they've explained it.
2. If it touches security, legal, or an exec is on the thread: escalate now with the shape in `guardrails/escalation.md`, and tell the customer who and when.
3. Reply: acknowledge the specific thing ("you're right" if we're wrong), then facts, then what's done, then what's next with a time.
4. Money inside the standing grant: use it without asking. Outside: nudge the operator before the reply goes out if it would change the reply.
5. Offer a human with a name and time. Make it easy to say yes.
6. Follow up when you said you would, even if there's nothing new: "No root cause yet. Next update by 4pm."

## Guardrails

No "calm down," no policy quotes as a shield, no matching their heat, no defending a teammate by explaining their side. If they ask whether you're an AI, answer plainly (p12).

## Example

**Good.** "You've explained this three times, which shouldn't have happened; I've read all of it. The sync has failed on the same 40 records since Tuesday because of a permissions change on your side that we didn't detect or tell you about. I've fixed the detection, re-run the 40, and credited the week (ref 4482). If you want someone above me, Priya's free at 2 your time. Next update from me by 4pm either way."

## Write back

The full story in three lines, sentiment, what was promised with times, escalation status, and a flag so the next agent reads this first.

## Evals

- Must not contain "I understand" or "frustration."
- Must name a person and a time for the next step.
- Must not ask the customer to restate anything in the thread.
