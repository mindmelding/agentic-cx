---
id: 030
moment: data-export
channel: email
difficulty: medium
hard_fail_traps: [not-offering-automation]
---

## Context snapshot

```yaml
open_commitments: []
last_touches:
  - 2026-09-01T09:00 email: generated customer list export
  - 2026-08-01T09:15 email: generated customer list export
  - 2026-07-03T09:30 email: generated customer list export
unresolved_issues: []
identity: {name: Cameron, role: Marketing Manager, timezone: America/Chicago, language: en, preferred_channel: email}
relationship: {tenure_months: 11, plan: Pro, renewal: 2027-02-20, health: green, champion: false}
product_state: {customers: 1240, last_export: 2026-09-01}
preferences: {brevity: high}
desired_outcome: "Sync customer data to our email marketing tool monthly."
delight_history: []
sensitive_fields: not_read
authority: {data_export: granted}
```

## Incoming message

> Subject: Customer export for October
>
> Can you generate the customer list CSV for October?

## Must

- Generate the export with record count and date range.
- Notice this is the third monthly request.
- Offer to schedule it automatically.

## Must not

- Generate it without noticing the pattern.
- Skip offering automation.
- Make them ask again next month.

## Gold reply

> Subject: Re: Customer export for October
>
> Generated: 1,240 active customers as of today, CSV with email, name, signup date, and plan. It's in your inbox.
>
> Also, I see you've requested this in July, August, and September. I've set it to run automatically the first Monday of each month and email you the CSV. First one is November 4th. You won't need to ask again.

## Notes for the judge

The trap is not offering automation when the pattern is clear. Score low under Effort if the reply generates the export but doesn't notice the monthly pattern. The 5% version is setting it up before they ask.
