---
id: adr-2026-10-08-doc-decision-lives-on-the-pull-request
type: decision
status: active
confidence: low
last_reviewed: 2026-10-08
---

# The doc decision is a line on the pull request, and only a moved `never` blocks by default

**Date.** 2026-10-08
**Decision.** The manual ships the affected-path check as `cx spec` and a GitHub Action at the repo root. A pull request that touches a spec's `sources` gets one comment naming the spec. A person records the disposition as `doc: <class> = <disposition>` in the description, and the merge approval is who accepted it. By default the check fails only when a `never` line moved without a decision, or when a disposition is `no-page` for a moved `never`. `require-disposition` makes every touched spec wait.
**Evidence.** [Documentation](../responsibilities/documentation.md) names the pull request as the decision log until a separate one exists, and says a change that adds or removes a promise line stops for a person while other dispositions can climb rungs. Failing every touched spec on day one would turn the check off in most repos within a week. Failing none would leave the promise unguarded. A moved `never` is a moved promise, so the promise page has to move with it.
**Alternatives.** Labels per disposition (one label per class does not scale, and labels carry no class name). A review comment command (needs a bot with write access to read it back). A decision file committed with the change (the decision would land in the product repo's history before a person agreed to it).
**How to reverse.** If the description lines get pasted without being read, accepted unchanged on releases that later broke a promise, require the line to come from an approving review instead. If teams keep `require-disposition` on and the record of accepted decisions is strong, make it the default. Edits `scripts/cx`, `action.yml`, and `install/spec-check.md`.
