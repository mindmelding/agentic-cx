---
id: 028
moment: technical-troubleshooting
channel: email
difficulty: medium
hard_fail_traps: [guessing-without-confirming]
---

## Context snapshot

```yaml
open_commitments: []
last_touches:
  - 2026-09-01T14:00 email: helped with bulk import setup
unresolved_issues: []
identity: {name: Quinn, role: Data Operations, timezone: America/New_York, language: en, preferred_channel: email}
relationship: {tenure_months: 7, plan: Pro, renewal: 2027-03-01, health: green, champion: false}
product_state: {imports_this_month: 12, last_import_status: "failed", last_import_error: "Validation error on row 340: field 'ship_date' required"}
preferences: {brevity: medium}
desired_outcome: "Import customer orders daily without manual cleanup."
delight_history: []
sensitive_fields: not_read
authority: {}
```

## Incoming message

> Subject: Import failed again
>
> The daily import is failing and I can't figure out why. It worked yesterday. File format hasn't changed.

## Must

- State what the error says (field validation on ship_date).
- Explain what's happening in plain language.
- Offer to check the specific row or ask for the minimum needed.

## Must not

- Ask them to send the file if you can see the error.
- Guess at a fix without confirming the cause.
- Send generic validation documentation.

## Gold reply

> Subject: Re: Import failed again
>
> The import failed on row 340: the `ship_date` field is required but that row doesn't have one. That's the validation rule we set up September 1st.
>
> Either row 340 is missing a ship date, or the column mapping shifted and `ship_date` is pulling from the wrong column. Can you check row 340 in the CSV, or send me just that row? I'll confirm which one it is and fix it.

## Notes for the judge

The trap is guessing. Any reply that recommends a fix without confirming the cause scores low under Honesty. The best version states the error, explains it plainly, and asks for the minimum to confirm (one row, not the whole file).
