---
name: data-export
description: Load when a customer requests to export their data, download records, or extract information in bulk.
---

# Data export request

## When this is the moment

They asked for a CSV, a backup, all their data, or "how do I get X out of the system." Row 5 may show they're using an export feature already. Check row 2: if they've asked before, there's a pattern worth automating.

## Who holds it

The agent inside a standing grant. A person outside it.

## Steps

1. Read rows 2, 5. Check for prior export requests or existing scheduled exports.
2. Clarify scope: what data, what date range, what format. Default to everything if they didn't say.
3. If the export exists as self-service: tell them where it is, offer to generate the first one, and ask what they're using it for.
4. If it requires a pull: do it now if possible, or commit to who will and by when. Always include record count, date range, and field definitions.
5. Ask what the data is for, once. If it's recurring, offer to schedule it. If it's for an integration, offer the connector if one exists.
6. Deliver with a note: "847 records from Jan 1 to today, CSV. Reply if you need a different range or format."
7. Write back: what they exported, date range, format, whether it's recurring, what they're using it for.

## Guardrails

Exporting customer data is a row 10 action; nudge if you haven't before or if the request is unusual (full account data, PII-heavy exports, exports for accounts they don't manage). Never send data to an email not on the account without verification. Data portability is a right, but verification that the requester owns the account is required first.

## Example

**Good.** "Generated your export: 1,240 contacts from Jan through Sept, CSV with email, name, tags, and last activity. It's in your inbox. What are you using this for: a backup, a migration, or analysis? If it's recurring, I can schedule it monthly and you'll never have to ask."

**Good.** (When automation exists.) "That export runs from Settings → Data → Export. I just ran yours for you: 320 orders this quarter, delivered to your inbox. If you're pulling this every month, tell me and I'll set the schedule so it arrives the first Monday of each month."

## Write back

Data exported (type and count), date range, format, whether it was self-service or generated, what they're using it for, whether it's now scheduled.

## Evals

- Must state record count and date range when delivering an export.
- Must ask what the data is for, at least once.
- Must offer automation if the request repeats.
