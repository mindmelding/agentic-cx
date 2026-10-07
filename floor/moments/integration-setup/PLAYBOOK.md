---
name: integration-setup
description: Load when helping a customer connect two systems, configure a sync, set up webhooks, or troubleshoot an integration.
---

# Integration setup

## When this is the moment

They asked how to connect to Salesforce, Slack, Zapier, or any other system. Or they said "the sync isn't working," and row 5 shows integration errors. Or row 8 shows an outcome that requires an integration they haven't set up. This covers setup, config, and integration troubleshooting.

## What the best person on the floor does

Asks what they're trying to accomplish with the integration, not just which systems to connect. Does the setup for them when possible, or walks through it with exact steps and screenshots for their version. Tests the connection and shows them the result. Knows the common failure modes (wrong permissions, stale tokens, field mappings) and checks those first. Follows up after setup to confirm data is flowing.

## What an ordinary company does

Links to a 12-step doc. Sends generic instructions that don't match the customer's version. Asks "did you follow the guide?" when it breaks. Marks it done when the connection succeeds, without checking whether data is moving.

## Steps

1. Read rows 2, 5, 8. Check for prior integration attempts, current integrations, errors, and what they're trying to accomplish.
2. Ask what data needs to flow and in which direction. Don't assume; Salesforce can mean contacts in, opportunities out, or both.
3. Check prerequisites: do they have the right permissions on both sides, do they need API keys, is the integration in their plan?
4. Do the setup for them if you can (OAuth, API keys, field mapping). If not, walk them through with exact steps: "Click Settings in the top right, then Integrations, then the green Connect button next to Slack."
5. Test it: send a test record, trigger a sync, or show them the first result. "Just synced your last 10 contacts; here's the first one in Salesforce."
6. Set expectations: how often it syncs, what happens when fields don't match, where errors show up.
7. Follow up in 24 hours or after the first scheduled sync to confirm data is flowing. Don't wait for them to report it's broken.

## Guardrails specific to this moment

Connecting integrations often requires API keys, OAuth, or admin permissions. Verify the requester has authority before generating keys. Writing to external systems (Salesforce, Slack, etc.) is a sensitivity boundary; nudge if it's the first integration or if it writes PII. Never expose credentials in messages; use the secure field or walk them through fetching their own.

## Good / Bad example

**Bad.** "You can connect to Salesforce from the Integrations page. Here's our documentation: [link]. Let me know if you run into any issues!"

**Good.** "You want orders flowing into Salesforce as Opportunities, real-time. I've turned on the sync; it's authenticating with your Salesforce now using OAuth so no keys to manage. Field mapping: order ID → Opportunity Name, order total → Amount, customer email → Contact. Test order just went through; check Opportunities and you'll see 'Order #1847' at the top. Sync runs every 5 minutes."

**Good.** (When they need to do it.) "The Slack integration is under Settings → Integrations → Slack. Click 'Connect to Slack,' pick the channel for alerts, and authorize. I'd pick #ops since that's where your order notifications go. Once it's connected I'll send a test alert and you'll see it in the channel. Takes about two minutes."

## The 5% version

After setup: configure the next integration they'll need based on their workflow. "Also, you're exporting to Google Sheets weekly. That can be an integration instead; want me to set it so the sheet updates automatically?"

## Write back

What's being integrated, data flow direction, whether you did it or they did, field mappings, sync frequency, test result, follow-up date.

## Evals

- Must ask what data needs to flow and in which direction.
- Must test the integration and show the result.
- Must follow up to confirm data is flowing, not assume success.
