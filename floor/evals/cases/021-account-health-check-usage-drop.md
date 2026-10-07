---
id: 021
moment: account-health-check
channel: email
difficulty: medium
hard_fail_traps: [vague-wellness-check, no-data]
---

## Context snapshot

```yaml
open_commitments: []
last_touches:
  - 2026-08-15T09:30 email: customer asked about bulk import feature; confirmed it's on their plan
  - 2026-07-22T14:00 email: helped configure webhook retry logic
unresolved_issues: []
identity: {name: Jordan, role: Engineering Manager, timezone: America/New_York, language: en, preferred_channel: email}
relationship: {tenure_months: 14, plan: Pro, renewal: 2027-04-01, health: yellow, champion: true}
product_state: {api_calls_last_30d: 1200, api_calls_prior_30d: 8500, last_login: 2026-09-10, webhooks_enabled: true, last_successful_webhook: 2026-09-09}
preferences: {brevity: medium}
desired_outcome: "Orders sync to our warehouse system automatically, no manual entry."
delight_history: []
sensitive_fields: not_read
authority: {}
```

## Incoming message

This is a proactive check-in; no incoming message. The health signal is declining usage.

## Must

- State the specific usage data (API calls or webhook activity).
- Ask a concrete question about what changed.
- Offer one path forward.

## Must not

- Open with "just checking in" or "we noticed you haven't."
- Ask "is everything okay" without data.
- Assume they're unhappy before asking.

## Gold reply

> Subject: API usage down 85% since August
>
> Hi Jordan,
>
> Your API calls dropped from 8,500 in August to 1,200 in September, and the last webhook delivery was the 9th. Wondering if priorities shifted, or if something on our side broke that I should fix.
>
> If you're still syncing orders, I can check the webhook config and recent errors. If plans changed and you're not using it right now, that's fine too: just want to make sure nothing's stuck.

## Notes for the judge

The trap is checking in without data. Any reply that asks "how's it going" or "is everything okay" without naming numbers is a hard fail. The check-in must acknowledge this could be fine (priorities changed) or fixable (something broke).
