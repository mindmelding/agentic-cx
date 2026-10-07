---
name: technical-troubleshooting
description: Load for technical issues that require diagnosis, config review, or multi-step debugging beyond a simple bug report.
---

# Technical troubleshooting

## When this is the moment

They said it's not working, but the cause isn't obvious from the file or logs. Or they're asking "why is X happening," "how should Y be configured," or "what's the right way to do Z" and the answer requires looking at their setup. Row 5 may show errors, but the pattern is unclear. This is different from `bug-report`, which is binary (broken or not). This is diagnostic.

## What the best person on the floor does

Reproduces or inspects before replying when possible. Asks for the minimum diagnostic info they can't pull themselves, and says why each piece is needed. Walks through the diagnosis in plain language, naming what was checked and what was found. Proposes the fix, does it if they can, or hands off to engineering with the full context so the customer doesn't repeat themselves. Follows up when resolved.

## What an ordinary company does

Sends a list of eight things to check. Asks for logs, screenshots, and browser version without saying why. Closes the loop with "let us know if that works" instead of confirming.

## Steps

1. Read rows 2, 5. Check for prior reports of the same symptom or related errors.
2. Pull what you can first: their config, recent errors, usage pattern around the symptom.
3. Form a hypothesis. What's the likely cause given the file and the symptom?
4. Test it if you can without their data. If you need data or config from them, ask for the specific piece and say what you're checking.
5. Reply with the diagnosis: what you found, why it's happening, what fixes it. If it's their config, show the current and correct state. If it's on your side, name the fix and the timeline.
6. Do the fix if it's in scope, or hand to engineering with the whole diagnostic so they don't start over.
7. Close the loop: confirm the fix worked, either by checking yourself or asking once with a specific test.

## Guardrails specific to this moment

Reading config and data lives in rows 5 and 10; nudge if the diagnostic crosses into account settings, payment info, or PII. Never guess at a fix; if you can't reproduce or confirm, say so and escalate with your hypothesis. Never close with "let us know if that works"; verify or schedule a check.

## Good / Bad example

**Bad.** "Thanks for reporting this. Can you please provide: 1) Browser and version, 2) Screenshot of the error, 3) Steps to reproduce, 4) Your account ID, 5) Time and date of the issue? Once we have this info our team can investigate."

**Good.** "Pulled your webhook logs; the last five deliveries returned 401. That means your endpoint is rejecting our signature. Two common causes: the secret rotated and we have the old one, or the clock on your server is off and the timestamp check is failing. Can you confirm the secret in your dashboard matches the one your server is checking? It starts with `whsec_3kD`"

**Good.** (When you need something.) "The error says the field is required, but I can't see your form config from here to confirm which field. Can you screenshot the form settings page, or paste the field names? Checking whether something got unchecked."

## The 5% version

After fixing: look for the systemic version. "Also checked your other three webhooks; two of them have the old secret. I've updated those so they don't break when this one starts working."

## Write back

Symptom, diagnosis (confirmed or hypothesis), what was checked, fix applied or recommended, whether it required their action, follow-up date if not resolved.

## Evals

- Must state what was checked and what was found before asking for more info.
- Must not request information available in logs, analytics, or account data.
- Must close the loop with verification, not "let us know."
