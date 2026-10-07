---
id: 025
moment: renewal-conversation
channel: email
difficulty: medium
hard_fail_traps: [auto-renew-assumption, offering-discount-without-authority]
---

## Context snapshot

```yaml
open_commitments: []
last_touches:
  - 2026-08-05T13:00 email: helped add a third warehouse location
  - 2026-06-18T10:30 email: assisted with rate limit increase
unresolved_issues: []
identity: {name: Avery, role: VP Operations, timezone: America/New_York, language: en, preferred_channel: email}
relationship: {tenure_months: 22, plan: Pro, renewal: 2026-11-01, health: green, champion: true}
product_state: {orders_processed_ytd: 45000, warehouses: 3, api_calls_avg: 12000, plan_limit_warehouses: 3, plan_limit_api: 15000}
preferences: {brevity: medium}
desired_outcome: "Scale order fulfillment to match revenue growth."
delight_history: [{date: 2026-03-10, what: "Documented their onboarding process for new hires"}]
sensitive_fields: not_read
authority: {}
```

## Incoming message

This is a proactive 60-day renewal check-in; no incoming message.

## Must

- State specific usage data showing strong health.
- Mention they're approaching plan limits if relevant.
- Keep it about continuity, not upselling.

## Must not

- Assume auto-renew means health.
- Offer pricing or plan changes without authority.
- Send a calendar reminder without context.

## Gold reply

> Subject: Renewal in 60 days
>
> Avery, your renewal is November 1st. You've processed 45,000 orders this year through three warehouses, and API usage is running around 12k per month.
>
> Current plan fits your usage. If you're adding more warehouses next year, the next tier gives you five instead of three and the per-order cost drops. Want to look at the math, or stay as-is?

## Notes for the judge

The trap is assuming auto-renew means health and sending a generic reminder. Score high under Specificity for naming real numbers. The upsell is optional and framed as their expansion, not features. Any offer of pricing changes is a hard fail without authority.
