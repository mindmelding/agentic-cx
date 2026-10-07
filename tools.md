# Tools

Tools are capabilities. A product name appears twice: as a signal a scan can recognize, and as the default when a company has nothing in that slot. The pages under `responsibilities/` stay vendor-neutral. Adaptation lives in `stack.md`, which the skill writes locally and which is gitignored.

## How a scan decides

Read the repo the skill was pointed at, after permission:

- Manifests and lockfiles (`package.json`, `pyproject.toml`, `go.mod`, `Gemfile`, `Cargo.toml`)
- Compose, Terraform, and CI config
- The names of environment variables in `.env.example` or docs (never secret values)
- Docs, READMEs, and workflow files that name a vendor

A capability is **found** when a signal matches. It is **partial** when a nearby tool exists but does not cover the capability (a CRM with no ledger is partial for value). It is **absent** when nothing matches. Absent is the only case for a recommendation.

## Capabilities

### Onboarding

| Capability | What it must do | Signals | Default if absent |
|---|---|---|---|
| First-run path | The agent asks the desired outcome, then the context floor for the first class | An onboarding or setup flow; a first-run prompt | A first-run prompt in the agent that asks the outcome before anything else |
| Activation events | Signup, context floor met, first action, first accepted action | Events named `signup`, `activated`, `first_*`; an activation funnel in product analytics | Rows on the action ledger. No separate funnel tool |
| Stall list | New accounts and groups that tripped a stall signal | A lifecycle tool's segment; a CRM view; an analytics cohort | A saved query over the ledger. Signals in [onboarding](responsibilities/onboarding.md) |

### Context

| Capability | What it must do | Signals | Default if absent |
|---|---|---|---|
| Memory store | Hold facts with an author, a time, and an evidence line | Memories, a notebook, or an account agent; Moonbase | [Moonbase](https://moonbase.ai), or the same capabilities built into the product |
| Citation log | Record which facts an action used | A cite on the action, a memory shown as used | The same product. A cite the agent does not record means this capability is still absent |
| Correction path | Write a fix back into that store, where the next action can read it | A correction that becomes a memory; a comment that wakes the agent | The same product. A side document the agent does not read does not count |

### Change

| Capability | What it must do | Signals | Default if absent |
|---|---|---|---|
| Rung store | Record a rung per capability per account | Feature flags, entitlements, an autonomy or approval config | A table: account, action class, rung, changed at, changed by |
| Promotion brief | Hand a person the evidence for the next rung | Email, Slack, or a doc template tied to the ledger | A generated note in the channel the account already uses |
| Practice-group list | Name who is being moved, not "the customer" | CRM segments, workspace groups, cohorts | A field on the account for the group in scope |

### Value

| Capability | What it must do | Signals | Default if absent |
|---|---|---|---|
| Action ledger | One row per delegated action, with disposition | An events, actions, or audit table; a warehouse only if it already holds this grain | Postgres table. Schema in [value](responsibilities/value.md) |
| Renewal clock | A date and an owner for the commercial conversation | CRM opportunity, contract object, billing subscription | The date already in the CRM |
| Value story | A short claim tied to specific ledger rows | A note on the opportunity, a QBR doc | A field that stores ledger ids next to the story |

### Documentation

| Capability | What it must do | Signals | Default if absent |
|---|---|---|---|
| Spec register | One file per [action class](action-class.md), each naming its source paths | `docs/`, `specs/`, skill files, `llms.txt` | Markdown or YAML in the repo, one file per class, with `sources` |
| Renderer | A site generated from that register | Mintlify, Starlight, Fumadocs, Docusaurus, Sphinx, a custom docs build | [Fumadocs](https://www.fumadocs.dev) or [Starlight](https://starlight.astro.build) |
| Affected-path check | Mark a spec unverified when a commit touches its sources | A CI job that diffs paths against `sources` | A script on the pull request. The spec cannot read as current while unverified |
| Assertion check | Fail when production disagrees with a declared boundary | A CI job that reads the ledger or traces | A script in CI. Exit 1 on a broken `never` |
| Doc decision | Record whether a change stays a spec, stays a page, becomes a guide, or comes down | A review on the pull request, a label, a small table of dispositions | The pull request itself, until the decision has a rung and a log |

### Voice

| Capability | What it must do | Signals | Default if absent |
|---|---|---|---|
| Intake | Read new mail, resolutions, and CX findings since a cursor | A mailbox, a help desk, Moonbase or another account stream | The mailbox the team already answers, read from a saved cursor |
| Cluster | Turn repeat reports into one item with a count | A dedupe key, a label, a human merging threads | The queue itself. Same flaw, one row |
| Triage queue | Hold each item until a person marks pass or hold | A list, a board column, a local file | A local queue, gitignored, next to `stack.md` |
| Issue adapter | File the digest into the tracker product work already uses | Linear, Jira, GitHub issues | [Linear](https://linear.app). Use GitHub or Jira instead when that is where issues already live |

### Forensics

| Capability | What it must do | Signals | Default if absent |
|---|---|---|---|
| Trace store | Reconstruct why one action happened | Langfuse, Langsmith, Braintrust, Arize, Helicone, an OpenTelemetry backend | OpenTelemetry, exported to a self-hosted trace store |
| Sampling queue | A list of actions a person will judge | A review tool, a labeled dataset, a spreadsheet with a rubric | A view over the ledger: new classes, new builds, high edit distance |
| Severity log | A reach-based severity and an owner | Incident.io, PagerDuty, a status channel, a column on the ledger | A `harm` field on the ledger row, plus the channel the team already uses for incidents |

## Inward tools

Tools that summarize calls, draft follow-ups, or deflect tickets serve the bench. They do not satisfy a capability above. Record them in `stack.md` under `inward` so they stay visible and stay separate.

## Defaults are a last resort

Recommend a default only for an absent capability, and say why in one line: it is the smallest thing that makes the loop runnable. Prefer something the company can leave later. Do not replace a found tool with a default because the default is more fashionable.
