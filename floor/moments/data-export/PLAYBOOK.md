---
name: data-export
description: Load when a customer requests to export their data, download records, or extract information in bulk.
---

# Data export request

## When this is the moment

They asked for a CSV, a backup, all their data, or "how do I get X out of the system." Row 5 may show they're using an export feature already. Check row 2: if they've asked before, there's a pattern worth automating.

## What the best person on the floor does

Generates the export if they can, in the format requested, and delivers it with the record count and date range. Tells them where the export feature lives if it's self-service. Asks once what the data is for, and offers the better path when one exists (an integration, a scheduled export, an API endpoint). Never makes them wait for a manual pull when the system can do it. Remembers the need and offers to automate it if it repeats.

## What an ordinary company does

Points to the export button with no context. Sends a ticket to engineering for a manual pull. Delivers a CSV with no record count, no date range, no explanation of fields. Makes them ask again next month.

## Steps

1. Read rows 2, 5. Check for prior export requests or existing scheduled exports.
2. Clarify scope: what data, what date range, what format. Default to everything if they didn't say.
3. If the export exists as self-service: tell them where it is, offer to generate the first one, and ask what they're using it for.
4. If it requires a pull: do it now if possible, or commit to who will and by when. Always include record count, date range, and field definitions.
5. Ask what the data is for, once. If it's recurring, offer to schedule it. If it's for an integration, offer the connector if one exists.
6. Deliver with a note: "847 records from Jan 1 to today, CSV. Reply if you need a different range or format."
7. Write back: what they exported, date range, format, whether it's recurring, what they're using it for.

## Guardrails specific to this moment

Exporting customer data is a row 10 action; nudge if you haven't before or if the request is unusual (full account data, PII-heavy exports, exports for accounts they don't manage). Never send data to an email not on the account without verification. Data portability is a right, but verification that the requester owns the account is required first.

## Good / Bad example

**Bad.** "You can export your data from the Settings page. Let me know if you need any help!"

**Good.** "Generated your export: 1,240 contacts from Jan through Sept, CSV with email, name, tags, and last activity. It's in your inbox. What are you using this for: a backup, a migration, or analysis? If it's recurring, I can schedule it monthly and you'll never have to ask."

**Good.** (When automation exists.) "That export runs from Settings → Data → Export. I just ran yours for you: 320 orders this quarter, delivered to your inbox. If you're pulling this every month, tell me and I'll set the schedule so it arrives the first Monday of each month."

## The 5% version

For a recurring export: schedule it before they ask the second time. "Also, I saw you exported this same data in July and September. I've set it to run on the first of each month and email you the CSV automatically. First one is November 1st."

## Write back

Data exported (type and count), date range, format, whether it was self-service or generated, what they're using it for, whether it's now scheduled.

## Evals

- Must state record count and date range when delivering an export.
- Must ask what the data is for, at least once.
- Must offer automation if the request repeats.
