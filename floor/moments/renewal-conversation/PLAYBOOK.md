---
name: renewal-conversation
description: Load for conversations about subscription renewals, contract extensions, or plan changes at 90, 60, or 30 days before renewal date.
---

# Renewal conversation

## When this is the moment

Row 4 shows a renewal date inside 90 days and either the customer asked about renewal, or you're reaching out at the 60-day or 30-day mark. Also load if they mention canceling, downgrading, or "evaluating options." Row 4 health and row 5 usage are the predictors; this conversation is shaped by what those say.

## What the best person on the floor does

Opens by asking what's working and what isn't, with specifics from the file. Listens for the job-to-be-done and whether it's being accomplished. Addresses gaps before talking about the renewal. If usage is strong and outcomes are met, confirms continuity and asks about expansion in their terms. If usage is weak, names it and asks what changed before proposing solutions. Treats churn as recoverable until the customer says otherwise.

## What an ordinary company does

Sends a renewal reminder 30 days out. Defaults to auto-renew and never checks health. Escalates to sales when they mention canceling. Offers discounts before understanding the reason.

## Steps

1. Read rows 2, 4, 5, 8. Tenure, renewal date, health score, usage trend, and whether they're hitting the stated outcome.
2. If reaching out first: open with the data, not the calendar. "You're hitting 8,000 API calls a month, up from 2,000 in March. Renewal's in 45 days; want to walk through whether the plan still fits?"
3. If they brought it up: acknowledge, ask what's driving the question. "What's changed since we last talked about this?"
4. Address any gap or blocker they name before discussing terms. Fix it if you can, or commit to who will and by when.
5. If they're expanding: propose the next tier in terms of what they're trying to do, not features. If they're stable: confirm continuity and check for blockers.
6. If they're considering leaving: ask why once, plainly. Fix the fixable. Escalate to a human for plan changes, pricing, or retention decisions beyond your grant.
7. Write back: renewal status, health score, usage trend, gaps named, actions taken, escalation if any.

## Guardrails specific to this moment

Never offer discounts, pricing changes, or custom terms without explicit authority. Never assume auto-renew means health. Reading payment history and contract terms lives in row 10; nudge if you haven't. Cancellations and downgrades require a human, not just for the conversation but for the company's learning.

## Good / Bad example

**Bad.** "Your subscription renews in 30 days. Click here to update your payment method or review your plan. Thank you for your business!"

**Good.** (Strong usage.) "Renewal's in 60 days. You've processed 12,000 orders through the sync this year, and I see you added two warehouses in August. Usage fits your current plan, but if you're adding more, the next tier gives you five warehouses instead of three and the cost per order drops. Want to look at the math?"

**Good.** (Weak usage.) "Renewal's in 60 days. I noticed usage dropped off after July: two imports last month vs. twenty in June. Did something change on your side, or is the product not doing the job anymore? Worth fixing before we talk about renewing."

## The 5% version

For a strong account: renew early at the current rate and add one setup for the next phase of their work. "Renewed at the same terms, good for another year. Also, you mentioned hiring a second ops person in Q1; I've documented the setup for them so they're live in a day instead of a week."

## Write back

Renewal date, current health and usage, what's working, what's not, any plan change discussed, next owner and date, escalation path if they're leaving.

## Evals

- Must reference specific usage or outcome data in the opening.
- Must ask what's changed if usage or health is declining.
- Must not offer pricing changes or discounts without authority.
