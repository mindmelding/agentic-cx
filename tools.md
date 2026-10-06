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

### Context

| Capability | What it must do | Signals | Default if absent |
|---|---|---|---|
| Memory store | Hold facts with an author, a time, and an evidence line | Tables or docs named memory, notebook, knowledge; vector stores tied to accounts | A versioned table in the product's own database |
| Citation log | Record which facts an action used | A `cited` field on events, traces, or prompts | A `context_cited` array on the action ledger |
| Correction path | Write a fix back into the product | An API or UI for editing memories; a comment that wakes an agent | The same table, written by the customer team with a source |

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
| Spec register | One file per action class in version control | `docs/`, `specs/`, skill files, `llms.txt` | Markdown or YAML in the repo, one file per class |
| Renderer | A site generated from that register | Mintlify, Starlight, Fumadocs, Docusaurus, Sphinx, a custom docs build | [Fumadocs](https://www.fumadocs.dev) or [Starlight](https://starlight.astro.build) |
| Assertion check | Fail when production disagrees with a declared boundary | A CI job that reads the ledger or traces | A script in CI. Exit 1 on a broken `never` |

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
