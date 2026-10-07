# Correction landed

The agent-era version of remembering how someone takes their coffee. Remembering is expected of an agent. Proving that a correction changed the work is what lands.

## Fires when

A fact the customer corrected has been cited in later actions. Send once, after the correction has been used at least three times or within a week, whichever comes first.

## Fields

`correction` (their words), `corrected_at`, `applied_count`, `fixed_retroactively`.

## Template

> You told me {when} that {correction, their words}. I've used it on {applied_count} since{, and fixed the {fixed_retroactively} already queued}.

## Example

> You told me Tuesday that Acme goes by its legal name on invoices. I've used it on 14 since, and fixed the 3 that were already queued.

## Do not

- Send it for a correction the customer made in anger, until the thread has cooled.
- Send it more than once per correction, or more than twice a month per account.
