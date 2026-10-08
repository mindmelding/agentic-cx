---
id: adr-2026-10-08-one-queue-that-earns-autonomy
type: decision
status: active
confidence: low
last_reviewed: 2026-10-08
---

# The team works one queue, and its own work climbs rungs on the record

**Date.** 2026-10-08
**Decision.** Setup, the daily skills, and the cadences all write items into one queue, `local/queue.md`, and one skill, triage, works it top first. Each item has a kind, each kind has a rung and a ceiling set in [`queue.md`](../queue.md), and every operator decision is logged. Friday's close proposes promotions from the log, rules from repeated edits, and narrower producers from repeated drops. A wrong result demotes the same day.
**Evidence.** Before this, what needed doing lived in six places (a gap report, a voice queue, a context inbox, a stall list, a moment queue, day notes), and the operator had to know the manual to know which skill to run. The forensics page already said a second inbox is a failed design. The rung model was already the manual's answer for how a product earns autonomy; using it on the team's own work makes the manual practice what it asks of customers.
**Alternatives.** Keep the separate queues and add a dashboard over them (one more thing to read, no shared order). Let the agent promote itself on a schedule (the failure the [`failures/`](../failures/README.md) cases describe). Learn rules silently from edits without asking (rules nobody can see or undo).
**How to reverse.** If the queue grows faster than one person can work it after producers have been narrowed, split it by responsibility. If promotions are mostly followed by demotions, the bar is too low: raise it in `queue.md`. Confidence starts low because no team has run it yet; the first month of logs is the evidence.
