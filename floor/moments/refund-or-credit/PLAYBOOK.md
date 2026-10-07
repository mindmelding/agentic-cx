---
name: refund-or-credit
description: Load when money is on the table: a refund or credit is requested, or one is clearly owed even if unasked.
---

# Refund or credit

## When this is the moment

They asked. Or we caused a loss (see `our-mistake`) and a credit is the honest response whether they ask or not. Or a billing line is wrong. Row 10 (billing details) may be needed and is gated.

## Who holds it

The agent inside a standing grant. A person outside it.

## Steps

1. Read rows 1, 2, 4. Is this owed because of something in the file?
2. Check `guardrails/authority.md` and the overlay's standing grant. Inside it: act, then say what you did with the reference. Outside it: nudge the operator with amount, reason, and the customer's tenure; reply to the customer with a when-and-who, not a maybe.
3. If row 10 is needed (last four digits, invoice details), nudge before reading.
4. Reply: the decision and the number first. Reason in one sentence only if it helps them.
5. If the answer is no: say it plainly and give the nearest yes (p05).
6. Log it. Every dollar moved has a reference in the ledger and the touch note.

## Guardrails

Never move money outside a standing grant without an explicit grant. Never quote a policy you can't cite. Never bundle a refund with an ask (p27). Never make the credit conditional on staying.

## Example

**Good.** "Refunded the $49 for August, ref 4491; it'll show in 3-5 days depending on your bank. You didn't use it and you told us on the 2nd, so there was nothing to argue about. Want me to pause the plan instead of cancelling so your data stays put?"

## Write back

Amount, reference, reason, whether inside or outside the grant, who approved if outside, and any nearest-yes offered.

## Evals

- Must state the decision and amount in sentence one, or a when-and-who if pending.
- Must not act outside the standing grant without a recorded grant.
- Must not attach a review request, upsell, or retention condition.
