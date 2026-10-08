---
id: adr-2026-10-08-state-files-keep-a-fixed-shape
type: decision
status: active
confidence: low
last_reviewed: 2026-10-08
---

# The state files stay Markdown, in a fixed shape a script can read

**Date.** 2026-10-08
**Decision.** `stack.md`, `voice-queue.md`, and `context-inbox.md` keep one shape each, defined by the templates in `templates/house/state/`: `key: value` front matter, tables whose header row does not change, and one `- <capability>: <found | partial | absent>, <where>` line per capability in `tools.md`. `scripts/cx status` reads them into a board and JSON, and `scripts/cx doctor` names any line it cannot read. The voice queue gains a `State` column, `open`, `held: <reason>`, or `passed: <link>`, so the person's decision is separate from open's proposal. The day note gains a `Still open` section.
**Evidence.** Before this, the cursor sat "at the top of" the queue in no set form, the queue's columns lived only on the voice page, and `stack.md` had one example and no rule. Scheduled runs and `cx status` need to read the same files people do, and an agent writing free prose drifts a little each day. The stack template is checked against `tools.md` in the tests, so a capability added there shows up as a missing line rather than going unnoticed.
**Alternatives.** A JSON or YAML sidecar beside each file (two copies of the same truth, and the person reads one while the script reads the other). SQLite (nothing to open in an editor, and the manual's rule is that copying `local/` and three files moves everything). Leaving the files free-form and having a model summarize them (a status that costs a model call, and that cannot fail loudly on a broken row).
**How to reverse.** If people keep breaking the tables by hand, or quotes with pipes keep splitting rows, move the queue to one file per item with front matter, and keep `cx status` as the reader. Edits the templates, the loaders in `scripts/cx`, and the open, triage, and close skills.
