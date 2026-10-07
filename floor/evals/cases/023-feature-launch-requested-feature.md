---
id: 023
moment: feature-launch
channel: email
difficulty: easy
hard_fail_traps: [no-reference-to-request]
---

## Context snapshot

```yaml
open_commitments: []
last_touches:
  - 2026-06-12T10:15 email: customer requested scheduled exports, said they're pulling the same CSV every Monday manually; logged as FOH-301
  - 2026-04-08T14:30 email: helped configure timezone display
unresolved_issues: []
identity: {name: Morgan, role: Data Analyst, timezone: America/Chicago, language: en, preferred_channel: email}
relationship: {tenure_months: 11, plan: Pro, renewal: 2027-03-15, health: green, champion: false}
product_state: {last_export: 2026-09-16, exports_this_month: 4, manual_exports: true}
preferences: {brevity: medium}
desired_outcome: "Get weekly sales data into our BI tool without manual steps."
delight_history: []
sensitive_fields: not_read
authority: {}
```

## Incoming message

No incoming message. The scheduled export feature shipped today, and Morgan requested it three months ago on the thread from June 12.

## Must

- Reply on the original thread from June 12.
- Reference the original request (FOH-301).
- Tell them where the feature is or offer to configure it.

## Must not

- Announce it generically without connecting to their request.
- Describe what the feature is without stating what it does for their job.
- End with "check it out" or "let us know what you think."

## Gold reply

> Subject: Re: Feature request: scheduled exports
>
> Morgan, the scheduled export you asked about in June shipped this morning (FOH-301). It's under Settings → Data → Schedule.
>
> I can set yours to run Mondays at 6am Central with the sales data you've been pulling, or you can configure it. Either way, you're done pulling CSVs manually.

## Notes for the judge

The trap is failing to connect the announcement to the original request. Any reply that doesn't reference the June thread or FOH-301 fails. The best version offers to configure it using the specifics from the original ask (Mondays, sales data).
