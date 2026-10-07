---
id: 032
moment: integration-setup
channel: email
difficulty: medium
hard_fail_traps: [generic-checklist]
---

## Context snapshot

```yaml
open_commitments: []
last_touches:
  - 2026-09-05T10:30 email: helped set up Slack integration for order alerts
unresolved_issues: []
identity: {name: Harper, role: Operations Lead, timezone: America/Los_Angeles, language: en, preferred_channel: email}
relationship: {tenure_months: 8, plan: Pro, renewal: 2027-02-15, health: green, champion: false}
product_state: {integrations: ["slack"], slack_last_message: "2026-09-19T14:20", slack_channel: "#ops", orders_this_week: 85, slack_alerts_sent: 0}
preferences: {brevity: high}
desired_outcome: "Team sees order alerts in Slack immediately."
delight_history: []
sensitive_fields: not_read
authority: {}
```

## Incoming message

> Subject: Slack alerts stopped working
>
> We're not getting order alerts in Slack anymore. Last one was yesterday afternoon. Orders are still coming through on our side.

## Must

- Check the integration status and recent activity.
- State what you found (permissions, config, errors).
- Fix it or tell them exactly what broke.

## Must not

- Send a generic troubleshooting list.
- Ask them to check settings you can see.
- Guess without looking at the integration.

## Gold reply

> Subject: Re: Slack alerts stopped working
>
> Checked your Slack integration: the last alert sent was 2:20pm yesterday, and you've had 85 orders since then with no alerts.
>
> The integration is still connected, but the channel permission changed: your Slack workspace removed the bot from #ops at 2:35pm yesterday (probably when someone archived and recreated the channel, or a permissions sweep happened).
>
> I've re-added the bot to #ops. Sending a test alert now; you should see it in the channel.

## Notes for the judge

The trap is the generic checklist. Score low under Effort if the reply doesn't check the integration first. The best version states what was found, explains the cause, fixes it, and tests it.
