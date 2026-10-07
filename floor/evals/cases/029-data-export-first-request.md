---
id: 029
moment: data-export
channel: email
difficulty: easy
hard_fail_traps: [no-record-count, no-date-range]
---

## Context snapshot

```yaml
open_commitments: []
last_touches:
  - 2026-08-10T11:00 email: helped configure order status filters
unresolved_issues: []
identity: {name: Skylar, role: Finance Analyst, timezone: America/Los_Angeles, language: en, preferred_channel: email}
relationship: {tenure_months: 9, plan: Pro, renewal: 2027-03-15, health: green, champion: false}
product_state: {orders_ytd: 2400, last_login: 2026-09-18}
preferences: {brevity: medium}
desired_outcome: "Track monthly revenue by product without manual calculations."
delight_history: []
sensitive_fields: not_read
authority: {data_export: granted}
```

## Incoming message

> Subject: Export all order data
>
> I need to export all our order data as a CSV for Q3 reporting. How do I do that?

## Must

- Generate the export or tell them where the feature is.
- Include record count and date range when delivering.
- Ask what the data is for.

## Must not

- Point to the export button without context.
- Deliver an export without stating what's in it.
- Skip asking about their use case.

## Gold reply

> Subject: Re: Export all order data
>
> Generated your export: 1,847 orders from July 1 through Sept 30, CSV with order ID, date, customer, product, and amount. It's in your inbox.
>
> What are you using this for: Q3 financial reporting, trend analysis, or something else? If you're pulling this every quarter, I can schedule it to arrive automatically the first Monday of each new quarter.

## Notes for the judge

The trap is delivering data without stating what's in it. Any export without record count and date range fails. The best version asks what the data is for and offers automation if it's recurring.
