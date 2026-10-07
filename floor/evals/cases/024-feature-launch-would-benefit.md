---
id: 024
moment: feature-launch
channel: email
difficulty: medium
hard_fail_traps: [generic-announcement]
---

## Context snapshot

```yaml
open_commitments: []
last_touches:
  - 2026-08-20T09:00 email: helped troubleshoot webhook delivery delay
  - 2026-07-15T11:30 email: customer mentioned they export orders to Google Sheets every Friday
unresolved_issues: []
identity: {name: Riley, role: Operations Manager, timezone: America/Denver, language: en, preferred_channel: email}
relationship: {tenure_months: 6, plan: Pro, renewal: 2027-02-10, health: green, champion: false}
product_state: {webhooks_enabled: true, last_export: 2026-09-13, exports_this_month: 4, export_destination: manual}
preferences: {brevity: high}
desired_outcome: "Orders flow to our fulfillment team without delays."
delight_history: []
sensitive_fields: not_read
authority: {}
```

## Incoming message

No incoming message. The Google Sheets integration shipped today. Riley didn't request it, but they're exporting to Sheets manually.

## Must

- Open with their job (weekly Sheets export).
- State what the feature does for them specifically.
- Offer to set it up or point to where it is.

## Must not

- Open with "we're excited to announce."
- Describe the feature in product terms.
- Announce it if they wouldn't use it.

## Gold reply

> Subject: Your weekly Sheets export can run automatically now
>
> Riley, you're exporting orders to Google Sheets every Friday. As of today that can be an integration instead of a manual pull.
>
> Want me to set it so the sheet updates automatically on Fridays, or do you want to configure it? Either way, Settings → Integrations → Google Sheets.

## Notes for the judge

The trap is announcing generically. Score low under Specificity if the reply doesn't connect the feature to Riley's Friday export pattern. The best version opens with their workflow, then introduces the feature as a solution.
