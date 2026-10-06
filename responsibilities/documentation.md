# Documentation

## Mandate

This team owns the contract: what the product promises, the few pages that must exist, and the check that production still agrees. Page count should fall as the product grows.

## Delivered when

Each action class has a spec a person and a machine can read. Every public page is one of the forms below, or it has been deleted because the product now says it. A declared `never` that production broke has failed a check.

## The loop

1. Write one spec per action class: when it fires, what it may do, what it will never do, who approves, which code implements it.
2. Render the human site from that register. Agents may draft. A person owns the boundary lines.
3. On each release, check the boundaries two ways. Against the code paths the spec names. Against last week's ledger.
4. When a page explains behavior the product can say in the moment, file the product change and remove the page once it ships.

A page survives for a reason:

| Form | Why it exists |
|---|---|
| Witness | The system cannot credibly testify to its own constraints. |
| Pre-access | There is no agent to ask yet. Setup, connect, the first step. |
| Failure | Asking the system is the move that fails. |
| Living state | What this account's agent believes, what is connected, what it did. The product publishes it. This team defines what must be on it. |
| Machine spec | The file a customer's coding agent reads. |

Anything else is a candidate for deletion.

## Tools

### Capabilities required

- A spec register in version control.
- A renderer that builds the site from that register.
- An assertion check that fails the build or the weekly job when a boundary and production disagree.

### Signals a scan can see

`docs/`, `specs/`, `llms.txt`, skill files. Mintlify, Starlight, Fumadocs, Docusaurus, Sphinx, or a custom docs build. A CI job that mentions docs, specs, or the ledger. See [tools](../tools.md).

### If nothing is found

Markdown or YAML in the repo, one file per class. Render with Fumadocs or Starlight. A CI script that exits 1 when a `never` breaks.

## Cadence

- **Daily.** Nothing, unless a check failed.
- **Weekly.** Run the assertion check. Remove or reclassify one page.
- **Quarterly.** Count pages. The count should be lower than last quarter, or each addition should be one of the five forms.

## Artifacts

- The spec file.
- The generated site.
- The check output: which claims disagreed with production, and whether the spec or the product was wrong.
- The deletion log: page, date, what replaced it.

## Measures

Share of `never` lines verified against production in the last week. Page count, and how many pages were removed because the product now speaks. A growing site is a finding, not a publishing win.
