# Pricing

How the product is priced decides which CX numbers the customer's finance team will read, and whether good CX work raises or lowers the bill. This team rarely sets the price. It always lives with the consequences. So it should know the model cold, and say early when the model works against the customer.

The [setup skill](skill/SKILL.md) runs the interview below.

## The models

| Model | Billable unit | Examples (public, verified 2026-10-07) | What it does to CX |
|---|---|---|---|
| **Seat** | A person with access | Most software before agents | Success shrinks the bill. When the agent does the work, people stop logging in, and seats look like waste at renewal. The value note has to carry the renewal alone |
| **Usage or credits** | Compute, tokens, or credits per action | Agentforce flex credits; Devin's compute units (secondary) | Hard for the customer to forecast. Opacity is the top complaint. The receipt has to translate credits into work |
| **Per action or conversation** | Each action, or each conversation the agent handles | Agentforce per conversation (secondary) | Unwanted actions cost money. Reversals and ignored actions should not be billed, and the customer will ask |
| **Per outcome** | A defined result: a resolution, a qualified lead, a saved cancellation | [Fin](https://fin.ai/pricing) at $0.99 per outcome, [Sierra](https://sierra.ai/blog/outcome-based-pricing-for-ai-agents), [Zendesk](https://www.zendesk.com/newsroom/articles/zendesk-outcome-based-pricing) | Lines up best with value, if the definition is right. The definition is usually the vendor's detection logic, not the customer's judgment. CX is where that gap shows up |
| **Per agent** | An agent priced like a hire | AI SDR products (secondary) | Invites comparison with a person's salary and output. The value note has to answer "is it as good as a hire" with the ledger |
| **Hybrid** | A platform fee plus one of the above | The most common model in 2026 by several analyses (secondary) | Inherits the issues of the variable part |

## Where the rung meets the bill

The rung profile and the bill move together, and not always in the customer's favor:

- **Outcome, action, or usage pricing.** A promotion means more work runs, so the bill rises. A [promotion offer](templates/customer/promotion-offer.md) that raises the bill is sent by a person, and says so plainly, with the expected change.
- **Seat pricing.** A promotion means fewer people need the product, so the next renewal shrinks. Say this inside the company before it shows up in a forecast.
- **Any model.** A reversal or a blocked action that is billed is a voice item. The customer is paying for a mistake.

## The disputed unit

When pricing is per outcome, the customer's finance team will eventually ask whether something counted as a resolution actually resolved anything. Prepare for that question before it arrives:

1. Write the definition in the customer's words, from the contract.
2. Map it to ledger dispositions. A billed outcome that a person later reversed is the case to watch.
3. Report, beside the bill, the share of billed outcomes a person later reversed or reopened.
4. If that share is material, raise it inside the company before the customer does.

## Interview

Asked once, during setup, one question at a time. Look first in the product repo, the pricing page, and any contracts the operator can share.

1. How is the product priced today, and what is the billable unit?
2. Who defined that unit, and is the definition written in the contract?
3. Is the billable unit a row in the ledger, or computed somewhere else? Can the two be reconciled?
4. Does moving an account up a rung change its bill? Up or down?
5. Who at the customer sees the bill, and is that the same person who supervises the agent?
6. Has a customer ever disputed a charge? What was the unit in question?
7. How is the renewal price set, and who in CX is in that conversation?
8. Is pricing expected to change in the next two quarters?

## What the setup skill writes

A short section in `local/assessment.md`:

```markdown
## Pricing
Model: <seat | usage | action | outcome | agent | hybrid>, billable unit: <...>
Unit in the ledger: <yes | reconciled | no>
Promotion moves the bill: <up | down | no>
Bill reader vs supervisor: <same | different, names>
Risk: <one line, or none>
```

A risk is worth one line when the billable unit is not in the ledger, when a promotion raises the bill and nobody has said so, when seats will fall as the agent works, or when billed outcomes are later reversed.
