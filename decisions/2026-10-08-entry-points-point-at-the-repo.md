---
id: adr-2026-10-08-entry-points-point-at-the-repo
type: decision
status: active
confidence: medium
last_reviewed: 2026-10-08
---

# Hosts reach the manual through short pointer files, not generated adapters

**Date.** 2026-10-08
**Decision.** The manual runs from a clone of the repo. Each host finds it through a file it already reads, written by hand and kept to a few lines: `AGENTS.md` is the entry point, `CLAUDE.md` imports it, `GEMINI.md` points at it, and `.claude/skills/<name>/SKILL.md` points Claude Code at each real skill under `skill/` and `skills/`. Moment playbooks stay `PLAYBOOK.md` with Agent Skills frontmatter (`name`, `description`), so they are routed by description and loaded one at a time. Nothing is generated.
**Evidence.** The skills and playbooks link to the canon around them: the responsibilities, the templates, the guardrails. Any install that copies a `SKILL.md` out of the repo breaks those links, which is why the earlier decision renamed playbooks away from `SKILL.md`. The generator that decision relied on (`scripts/build_adapters.py`) lived in front-of-house and was never brought over. Pointer files are short enough that drift is easy to see, and Claude Code listed the six `/cx-*` skills from `.claude/skills/` as soon as they existed.
**Alternatives.** Port the generator (more moving parts to keep a few short files in step). Publish the skills for global install with `npx skills add` (breaks the relative links). A plugin per host (packaging work with no user asking for it yet).
**How to reverse.** If a host cannot run from a clone, or the pointer files drift from the skills they name, build a generator. The one place a bundle is already wanted is a customer-facing reply agent ([`install/customer-agent.md`](../install/customer-agent.md)), which today loads the files by hand.
