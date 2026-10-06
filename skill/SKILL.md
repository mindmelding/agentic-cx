---
name: agentic-cx
description: Adapt the agentic CX operating manual to this company's tools. Scan the repo with permission, interview only the gaps, and write stack.md. Use when someone adopts this repo, asks which CX tools they need, or wants the five responsibilities mapped onto their stack.
---

# Agentic CX setup

Adapt [`../README.md`](../README.md) to the company in front of you. Do not fork the responsibility pages. Those stay vendor-neutral. The adaptation is a local `stack.md` at the repo root (gitignored).

## Before any scan

Say what you want to read and wait for a yes. The scan covers manifests, compose and CI config, docs, and the **names** of environment variables. It does not read secret values, production data, or customer records.

If they decline, skip the scan and interview every capability in [`../tools.md`](../tools.md).

## Scan

From the repo they point at (this one, or the product repo):

1. Dependencies and infrastructure files.
2. Docs and workflows that name a vendor.
3. Env-var names in examples only.

Match what you find to the capabilities in `tools.md`. Mark each capability `found`, `partial`, or `absent`. A nearby product that does not do the job is `partial`: a CRM is not an action ledger.

## Interview

Ask only for gaps, in one pass. Group the questions by responsibility. For each `partial` or `absent` capability:

- Where does this live today, if anywhere?
- Who is allowed to write it?
- If it is absent, will they accept the default in `tools.md`, or name something else?

Also ask, once:

- Which channel does this team already work in (Slack, email, a ticket tool, something else)?
- Which tools are inward only (summaries, deflection, QA on the team's own queue)?

Do not propose a vendor for a capability you marked `found`.

## Write stack.md

Create `stack.md` at the root of this operating-manual repo. One section per responsibility, then `inward`. For each capability:

```markdown
## Context
- Memory store: found, Postgres `memories` (product repo)
- Citation log: absent, accept default, `context_cited` on the ledger
- Correction path: partial, memories are editable in admin, no customer path yet
```

End with a short "first loop" that names the single action class they should instrument, using only the tools now listed. Point at the two-week start in the README.

## After

Offer to walk one responsibility page and substitute their tool names in conversation. Leave the pages in `responsibilities/` unchanged, so the manual stays shareable.
