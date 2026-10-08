# Documentation

## Mandate

This team owns the contract: what the product promises, the few pages that must exist, and the check that production still agrees. Page count should fall as the product grows.

## Delivered when

Each action class has a spec a person and a machine can read. Every public page is one of the forms below, or it has been deleted because the product now says it. A declared `never` that production broke has failed a check.

## The loop

A class is defined in [action-class.md](../action-class.md). Documentation keeps one spec per class, and the spec names the code that implements it.

1. Write the spec: when it fires, what it may do, what it will never do, who approves, the default rung, and the source paths.
2. Render the human site from that register. Agents may draft. A person owns the boundary lines.
3. On each change to a source path, mark that spec unverified. The same change checks the spec against the code, and the weekly job checks it against the ledger.
4. Decide what the change does to the public record. The decision is one of the dispositions below. It starts with a person, and the same decision can climb a rung once it keeps being right.
5. When a page explains behavior the product can say in the moment, the decision is to remove it once that ships.

### Example

A B2B company sells an agent that product teams use to ask about user behavior. Someone types "what changed in activation this week?" and the agent answers from that company's events. The class is [`answer_behavior_question`](../action-class.md). It may answer from their events and name the group that moved. It may never invent a number, and it may never show one customer's users to another. `sources` lists `src/analytics/answer.ts` and `src/analytics/what-changed.ts`.

The release is a change inside that class. Until now the agent returned a total: "Activation fell 12%." The new code in `what-changed.ts` makes it name the group: new accounts invited fewer teammates, returning accounts held steady.

The commit touches a path on the spec, so the spec is flagged unverified before anyone writes a page. A person looks at the diff and records the decision: **no documentation.**

The behavior shows up in the answer the next time someone asks.

> Activation fell 12% this week. New accounts invited fewer teammates. Returning accounts held steady. I can list the accounts if you want them.

A guide called "How to ask what changed" would teach a prompt for a question the agent should just answer. The article would exist because the answer stayed a bare number. That is a product bug. The fix is the sentence in the answer, and the flagged spec is closed as "no page."

The promise page does not move either. The agent still never invents a number and still never crosses a customer boundary. Nothing on the public promise changed, so nothing is added there.

The first times a change like this ships, a person confirms "no documentation." After that call has been accepted without edits on several releases that do not touch a `never` line, the check can propose it and wait for a yes. A change that would add or remove a promise line still stops for a person.

### What the decision can be

| Disposition | Use it when |
|---|---|
| Spec only | The class is real and a customer's agent can read the file. No page. |
| Page | One claim, in one of the forms below. |
| Guide | A sequence a person still has to walk, in order, because the product does not walk it yet. Elevating a page to a guide is a decision, recorded like the others. |
| Update | The code changed the boundary or the trigger. The spec changes with it. |
| Remove | The product now says this, or does this. The page or guide comes down. |

An existing help center rarely fits these on day one. Keep it, as a [bridge](../bridges.md): count the live pages, and take them down as each class's spec and the product's own answers replace them. A page written because inbound keeps asking something the product cannot answer yet is a bridge too, paired with the flaw that would make it unnecessary.

A page or guide survives for a reason:

| Form | Why it exists |
|---|---|
| Witness | The system cannot credibly testify to its own constraints. |
| Pre-access | There is no agent to ask yet. Setup, connect, the first step. |
| Failure | Asking the system is the move that fails. |
| Living state | What this account's agent believes, what is connected, what it did. The product publishes it. This team defines what must be on it. |
| Machine spec | The file a customer's coding agent reads. This is the spec itself. |

### How the decision gains autonomy

This is the same ladder as [change](change.md), applied to the doc decision rather than to the customer's action.

| Rung | What happens |
|---|---|
| 0 Propose | The check names the specs a commit touched and stops. A person classifies each one. |
| 1 Draft | The check proposes a disposition, with the diff and the current spec beside it. A person accepts or edits. |
| 2 Act with notice | Repeated, low-risk dispositions apply. Marking a spec unverified is the usual one. A person can reverse it. Elevating a guide and removing a page stay at draft until their own record is strong. |
| 3 Act silently | A disposition that has been accepted without edit, on a class whose boundary did not move, applies and appears in the decision log. |

A new company starts at 0. A rung moves on the record of accepted decisions, the same way a customer capability does. Removing a witness line does not go silent. A boundary a person has to stand behind stays with a person.

## Tools

### Capabilities required

- A spec register in version control, each class naming its source paths.
- A renderer that builds the site from that register.
- An affected-path check that marks a spec unverified when a commit touches those paths.
- An assertion check that fails when a boundary and production disagree.
- A decision log: commit, class, proposed disposition, rung, who accepted it.

### Signals a scan can see

`docs/`, `specs/`, `llms.txt`, skill files. Mintlify, Starlight, Fumadocs, Docusaurus, Sphinx, or a custom docs build. A CI job that maps a commit to the specs whose `sources` changed. See [tools](../tools.md).

### If nothing is found

Markdown or YAML in the repo, one file per class, with a `sources` list. Render with Fumadocs or Starlight. A CI script that marks those specs unverified and exits 1 when a `never` breaks. The decision log can be the same pull request until a separate store exists.

## Cadence

- **Daily.** Clear the specs a commit marked unverified. At the first rung that means a person classifies each one.
- **Weekly.** Run the assertion check. Remove or reclassify one page.
- **Quarterly.** Count pages. The count should be lower than last quarter, or each addition should be one of the five forms.

## Artifacts

- The spec file, including `sources`.
- The generated site.
- The decision log: commit, class, disposition, rung, who accepted.
- The check output: which claims disagreed with production, and whether the spec or the product was wrong.

## Measures

Share of `never` lines verified against production in the last week. Page count, and how many pages were removed because the product now speaks. While the old help center is a bridge, its live page count against the baseline. A growing site is a finding, not a publishing win.
