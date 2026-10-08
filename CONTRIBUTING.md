# Contributing

This is a canon of opinions, not a wiki. Contributions that make it sharper are welcome; contributions that make it longer are not.

## What gets merged

- **A principle** with a why, a when-it-doesn't-apply, and a good/bad pair. One opinion per file.
- **A playbook** (`moments/<slug>/PLAYBOOK.md`) in the existing shape. Add an eval case only if it tests behavior the fifteen in `floor/evals/cases/` do not.
- **An exemplar** with a "why it works." Anonymized or synthetic. No real customer data, ever.
- **A failure case** in `failures/`, in the shape its README gives, with a reputable source.
- **An eval case** that catches a real failure you saw.
- **A source** with a "what we took" paragraph. Never a bare link.
- **A legend**: a dated story of a gesture that landed and the reusable move.
- **A lexicon change**, argued. Adding a banned phrase needs one sentence on why it fails.
- **A context adapter** for a CRM or context layer that isn't covered.

## What doesn't

- Generic best practice without an opinion.
- Anything that loosens a guardrail. Overlays narrow; the canon doesn't loosen.
- Company-specific policy. That's your overlay.

## Before you open a PR

There is nothing to build. Check that every relative link you touched resolves, that no file names a real customer, and that customer-facing copy (gold replies, template examples) passes `scripts/cx check --gold --templates`. CI runs the same, plus `python3 scripts/test_cx.py`. If the check flags your prose, rewrite from the source idea; don't patch the sentence.

## Reversing an opinion

Open a PR that adds a `decisions/YYYY-MM-DD-<slug>.md` with the evidence and flips the principle's `status`. Opinions here are meant to be argued. They're just not meant to be vague.
