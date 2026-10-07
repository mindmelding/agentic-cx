---
name: cx-refresh
description: Monthly. Re-verify the harness and vendor tables in enablement/, update stale rows from primary sources, and propose a change to the supervision practices only when the tools changed the practice. Also re-checks the standards status in agent-customers.md. Use once a month, or when a major harness or model release lands.
---

# Refresh

Keep the fast-moving part of the manual true. One pass, about thirty minutes.

Read [`enablement/README.md`](../../enablement/README.md) for the rules this follows.

## Do this

1. **Stale rows.** In [`enablement/harnesses.md`](../../enablement/harnesses.md), list every row whose `verified` date is more than 90 days old, and every row marked secondary.
2. **Verify.** For each, open the vendor's own documentation. Update the mechanism, the date, and the source. If the vendor page no longer says it, remove the row. Do not replace a primary source with a blog.
3. **New mechanisms.** Check the major harnesses and assistants for a new approval mode, undo, memory, or skills change since the last entry in the changelog. Add a row only with a source, and map it to a rung.
4. **Vendor guidance.** Check whether Anthropic, OpenAI, or Google published new guidance on human oversight. Add a row to [`vendor-guidance.md`](../../enablement/vendor-guidance.md) if so.
5. **Agent customers.** Re-check the status column in [`agent-customers.md`](../../agent-customers.md): protocol versions, whether a draft became a standard, whether something was abandoned.
6. **Practices.** Propose a change to [`supervising.md`](../../enablement/supervising.md) only if a change in the tools changes what a customer should do. Show the proposed change and wait for a yes. Customer evidence from the ledger outranks vendor advice.
7. **Changelog.** One entry in [`enablement/CHANGELOG.md`](../../enablement/CHANGELOG.md): what changed and why, with dates.

Do not name model versions in the durable files. Name the capability.
