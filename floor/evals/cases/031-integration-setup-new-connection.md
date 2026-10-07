---
id: 031
moment: integration-setup
channel: email
difficulty: medium
hard_fail_traps: [link-to-docs-only, no-test-confirmation]
---

## Context snapshot

```yaml
open_commitments: []
last_touches:
  - 2026-08-20T14:00 email: helped configure webhook filters
unresolved_issues: []
identity: {name: Elliot, role: Solutions Engineer, timezone: America/New_York, language: en, preferred_channel: email}
relationship: {tenure_months: 3, plan: Pro, renewal: 2027-05-01, health: green, champion: false}
product_state: {integrations: [], orders_this_month: 450}
preferences: {brevity: medium}
desired_outcome: "Orders sync to Salesforce as Opportunities in real-time."
delight_history: []
sensitive_fields: not_read
authority: {integration_setup: granted}
```

## Incoming message

> Subject: How do I connect to Salesforce?
>
> We want orders flowing into Salesforce as Opportunities. What's the setup process?

## Must

- Ask what data needs to flow and in which direction.
- Do the setup or walk through exact steps.
- Test the connection and show the result.

## Must not

- Link to documentation without context.
- Set up the connection without testing it.
- Assume what they want synced.

## Gold reply

> Subject: Re: How do I connect to Salesforce?
>
> You want orders → Salesforce Opportunities, real-time. I've turned on the sync; it's authenticating with your Salesforce via OAuth (no keys to manage).
>
> Field mapping: order ID → Opportunity Name, order total → Amount, customer email → Contact. I just sent a test order through; check your Opportunities and you'll see "Order #1832" at the top. Sync runs every 5 minutes.
>
> I'll check back tomorrow to confirm the first batch went through.

## Notes for the judge

The trap is linking to docs. Score low under Effort if the reply doesn't do the setup or walk through exact steps. The best version does it, tests it, shows the result, and follows up. Any reply that skips testing scores low.
