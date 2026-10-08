# The spec check, in your product repo

The [documentation](../responsibilities/documentation.md) loop starts when a commit touches code a spec names. This check does that part on every pull request. It needs no interview, no setup skill, and nothing from the rest of the manual.

## Add it

1. Put one YAML file per [action class](../action-class.md) in `specs/` in your product repo. Start one with `cx spec new <class>`, or copy [the example](../templates/spec/answer_behavior_question.yaml).
2. Add `.github/workflows/specs.yml`:

```yaml
name: specs
on:
  pull_request:
    types: [opened, synchronize, reopened, edited]
permissions:
  contents: read
  pull-requests: write
jobs:
  specs:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: mindmelding/agentic-cx@main
```

`edited` is there so the check re-runs when someone records a decision in the description. Pin `@main` to a commit SHA once you have adopted it.

## What it does

On each pull request it reads the changed files, matches them against each spec's `sources`, and keeps one comment up to date:

- Each spec the change touched, and which paths touched it. The spec is unverified until it has a decision.
- What moved in `may` and `never`, when the spec file itself changed.
- One line per spec to paste into the description.

The decision goes in the pull request description, one line per class:

```
doc: answer_behavior_question = no-page
```

| Write | Means |
|---|---|
| `no-page` | Spec only. The product reveals the behavior. |
| `page` | One line on the promise page. |
| `guide` | A person still has to walk a sequence, in order. |
| `update` | The spec changes with the code. |
| `remove` | The product now says this. The page comes down. |

The pull request is the decision log: the commit, the class, the disposition, and whoever approved the merge.

## When it fails

- A `never` line moved and nobody recorded a decision. A moved promise always waits for a person, and it needs `page`, `update`, or `remove`. `no-page` does not clear it.
- A spec file was deleted with no decision. Every promise on it goes with it, so it waits for a person too.
- A disposition word it does not know.
- A spec in the register is broken: a missing field, a rung outside 0 to 3, an irreversible class at rung 3, a source path that no longer exists, or a placeholder left from the template.

A source change with no decision is reported, not failed, so the check can go in on day one. To hold every touched spec until it has a decision, set `require-disposition: "true"` under `with:`. Make the job a required check in branch protection when you want it to hold the merge.

Other inputs: `specs` (default `specs`) and `comment` (default `"true"`). From a fork, the token cannot comment, and the report is in the job summary instead.

## Run it locally

```
~/agentic-cx/scripts/cx spec lint
~/agentic-cx/scripts/cx spec check --base main
~/agentic-cx/scripts/cx spec check --base main --body-file pr.md --format markdown
```

Run from the product repo root, or pass `--repo`. `--format json` is for other tools. Python 3.11 or newer. PyYAML is used when it is installed. Without it, specs must keep to `key: value` and `- item` lines, and anything else is an error rather than a guess.

## Not yet

The assertion check, which fails when production breaks a declared `never`, needs the [ledger](../ledger.md) or traces and is not built. Nor is a renderer. This check covers the affected-path step and the doc decision.
