---
id: adr-2026-10-08-any-host-over-mcp
type: decision
status: active
confidence: low
last_reviewed: 2026-10-08
---

# Any host reaches the manual over MCP, and the company's files live in a house of their own

**Date.** 2026-10-08
**Decision.** `scripts/cx mcp serve` serves the manual over the Model Context Protocol, on stdio, with the standard library only: every tracked file as a resource, the six skills as prompts, and five tools (`manual_read`, `manual_search`, `lexicon_check`, `cx_status`, `cx_doctor`). The company's private files move to a **house**, the folder `CX_HOUSE` names, which defaults to the repo root so a clone works as before. MCP comes before a host-specific plugin because the manual has to read the same in every host and under every model.
**Evidence.** The 2026-10-08 decision on [entry points](2026-10-08-entry-points-point-at-the-repo.md) kept the manual in a clone because copying a skill out of the repo breaks its links. A server that resolves each link from the file it appears in keeps them working without moving anything, which answers that objection for every host at once. A package that updates the kit in place would overwrite notes kept inside it, so the house had to separate first. In a test, Claude Code with only this server connected searched the manual, failed a draft on the lexicon, and found the house, with no clone open.
**Alternatives.** A Claude Code plugin first (one host, and the operator asked for none to be favored). An npm or PyPI package (a build and a registry to keep for what a clone and `git pull` already do). Serving the private files over MCP too (a second door to customer data, when the host's own file tools already ask before they read).
**How to reverse.** If hosts stop supporting stdio servers, or prompts and resources stay unsupported where it matters, ship per-host packages built from the same files. If a house apart from the clone confuses more operators than it helps, keep `CX_HOUSE` as an option and stop recommending it. The entry-points decision stays active: pointer files are still how a host finds a clone.
