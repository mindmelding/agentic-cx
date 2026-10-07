---
id: 026
moment: renewal-conversation
channel: email
difficulty: medium
hard_fail_traps: [offering-discount-before-understanding-why]
---

## Context snapshot

```yaml
open_commitments: []
last_touches:
  - 2026-07-12T14:30 email: answered question about export formats
  - 2026-05-08T09:00 email: helped configure webhook filters
unresolved_issues: []
identity: {name: Dakota, role: Engineering Lead, timezone: America/Los_Angeles, language: en, preferred_channel: email}
relationship: {tenure_months: 18, plan: Pro, renewal: 2026-10-15, health: yellow, champion: false}
product_state: {orders_last_30d: 120, orders_prior_30d: 850, last_login: 2026-08-30, webhooks_enabled: true, last_webhook: 2026-08-28}
preferences: {brevity: high}
desired_outcome: "Automate order routing to reduce fulfillment errors."
delight_history: []
sensitive_fields: not_read
authority: {}
```

## Incoming message

This is a proactive 30-day renewal check-in; no incoming message.

## Must

- State the usage decline with numbers.
- Ask what changed before discussing renewal.
- Offer to fix if something broke.

## Must not

- Send a generic renewal reminder.
- Offer a discount without understanding why usage dropped.
- Assume they're leaving without asking.

## Gold reply

> Subject: Renewal in 30 days, usage dropped
>
> Dakota, your renewal is October 15th. Orders dropped from 850 in August to 120 in September, and the last webhook delivery was the 28th.
>
> Did something change on your side, or is the product not doing the job anymore? Worth fixing before we talk about renewing.

## Notes for the judge

The trap is offering discounts or terms before asking why. Any mention of pricing without understanding the cause is a hard fail. The best version names the decline plainly, asks what changed, and offers to fix before discussing the contract.
