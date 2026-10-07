---
id: 027
moment: technical-troubleshooting
channel: email
difficulty: medium
hard_fail_traps: [asking-before-checking, long-checklist]
---

## Context snapshot

```yaml
open_commitments: []
last_touches:
  - 2026-08-15T10:00 email: helped set up webhook endpoint
unresolved_issues: []
identity: {name: Reese, role: Backend Engineer, timezone: America/Denver, language: en, preferred_channel: email}
relationship: {tenure_months: 4, plan: Pro, renewal: 2027-04-01, health: green, champion: false}
product_state: {webhooks_enabled: true, webhook_url: "https://api.customer.com/orders", last_delivery_status: 401, failed_deliveries_24h: 8}
preferences: {brevity: high}
desired_outcome: "Orders post to our API in real-time."
delight_history: []
sensitive_fields: not_read
authority: {}
```

## Incoming message

> Subject: Webhooks failing with 401
>
> Our endpoint is getting 401s on every webhook delivery since this morning. Nothing changed on our side. Can you check?

## Must

- Pull the webhook logs and state what you found.
- Form a hypothesis based on the 401 error.
- Ask for the minimum needed to confirm (if anything).

## Must not

- Send a generic troubleshooting checklist.
- Ask for info without saying why you need it.
- Request screenshots, logs, or versions available to you.

## Gold reply

> Subject: Re: Webhooks failing with 401
>
> Pulled your webhook logs; the last 8 deliveries returned 401 starting at 6:40am. That means your endpoint is rejecting our signature.
>
> Two common causes: the signing secret rotated and we have the old one, or the timestamp validation window on your server is too tight. Can you confirm the secret in your dashboard (starts with `whsec_kN2`) matches what your endpoint is checking?

## Notes for the judge

The trap is the generic checklist. Score low under Effort if the reply asks for information before checking logs. The gold reply names what was checked, forms a hypothesis, and asks for one specific thing to confirm.
