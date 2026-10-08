---
id: adr-2026-10-08-unattended-runs-go-through-cx
type: decision
status: active
confidence: low
last_reviewed: 2026-10-08
---

# Unattended runs go through `cx`, and a consent file is the yes

**Date.** 2026-10-08
**Decision.** `scripts/cx` is the one entry point for everything that is not a conversation: `init` creates the private files, `doctor` says what is missing, `models` prints the tier table, and `run` starts a skill with nobody answering. Each "ask before you look" yes is recorded in `local/consent.toml`, gitignored. An unattended run reads that file instead of asking, and on hosts that can scope tools per run, `cx run` turns it into the allow list. Only open and close run unattended. Setup, floor, triage, and refresh wait on a person.
**Evidence.** The install page told operators to schedule `claude -p "Run skills/open/SKILL.md"` with read access only, but open writes the queue cursor and close writes the day note, and permission was granted in a chat that a scheduled run never sees. `models.toml` described `cx run` and `cx models` before either existed. A rule held only in a prompt is not held ([boundary](../boundary.md): "A promise kept by a prompt is not kept"), so the allow list, not the prompt, keeps the Claude Code run to the private files and the consented connectors. A first run of `cx run open` on a fresh clone posted the board, wrote nothing, and listed setup under "Waiting on you."
**Alternatives.** Leave scheduling as raw host commands (each operator rebuilds the permission flags, and most will grant too much). Keep consent in `stack.md` (it is prose written for people, and a parse error there would widen or narrow access silently). Let every skill run unattended and skip the steps that need a yes (triage and floor have nothing left once you skip them).
**How to reverse.** If hosts gain a standard way to declare per-run permissions from a file, drop the allow-list building in `cx run` and point the host at `local/consent.toml`. If operators keep editing consent by hand into states `doctor` cannot explain, move it into the setup flow alone. Either change edits `scripts/cx`, `models.toml`, `install/README.md`, and the "Ask before you look" rule in `AGENTS.md`.
