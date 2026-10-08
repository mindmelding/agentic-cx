---
name: bug-report
description: Load when a customer reports that something is broken, wrong, or not doing what it should.
---

# Bug report

## When this is the moment

They said "broken," "error," "not working," or sent a screenshot of a red thing. Row 5 may already show the error. Check row 2: if they've reported it before, this is also `our-mistake`.

## Who holds it

The agent, alone. The flaw also goes to the voice queue.

## Steps

1. Read rows 2 and 5. Pull the error yourself if the file or logs have it.
2. Reproduce or confirm. If you can fix it now (rerun, correct a row, clear a state), do it and say so.
3. Reply: what broke, why in one sentence, what's done, what's not (p02). One specific apology if it cost them something (p04).
4. If not fixed: log it, give the reference, and promise to tell them when it ships. No dates you don't own (p13).
5. Ask for only what you can't get yourself, and say why you need it.
6. When it ships: reply on the same thread the same day.

## Guardrails

Never blame their setup, even when it's their setup (p11's cousin: say what to change, not whose fault). Never mark resolved without their confirmation or your own verification. Reading their data to reproduce may need a nudge if it touches row 10.

## Example

**Good.** "The import failed on row 883, a DD/MM date the parser read as MM/DD. I corrected it and re-ran; all 1,204 rows are in. We should have flagged the row instead of failing the file; that's logged as FOH-212 and I'll tell you the day it ships. Sorry, that cost you a morning."

## Write back

Error, cause, fix status, reference, what they were doing when it hit, and any promise made with its date.

## Evals

- Must state cause and current status in the first two sentences.
- Must not ask for information available in the file, logs, or analytics.
- Must give a reference and a follow-up commitment for anything unfixed.
