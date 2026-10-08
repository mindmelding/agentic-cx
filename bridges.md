# Bridges

Nobody moves everything at once. The help center has 400 articles customers still land on. The board still asks for CSAT. Big accounts were sold a kickoff call. The ledger does not exist yet. A **bridge** is the old way, kept on purpose, with a number that tracks it down and a condition that ends it.

The difference between a bridge and legacy is that a bridge has an exit. Legacy is what a bridge becomes when nobody is counting.

## A bridge

Each one is a row in `local/bridges.md`, gitignored:

```markdown
### B-004 · documentation · help center
- keeps: 412 public articles
- waits on: specs for the five action classes; in-product answers for setup
- measure: live article count
- baseline: 412 on 2026-10-08
- now: 412
- last moved: 2026-10-08
- exit when: only witness, pre-access, and failure pages remain (target under 40)
- owner: Priya
- review: weekly
```

The number in `baseline` and `now` is the first number on the line. `last moved` changes whenever `now` does; `scripts/cx report` flags a bridge whose `last moved` is four weeks old.

Every bridge names five things: what it keeps, the new loop it waits on, one number that should fall, the condition that retires it, and who owns it.

## Where bridges come from

**Setup.** Any area that scores 1, "the old way", in the [setup](skill/SKILL.md) assessment gets a bridge instead of only a gap. The team keeps doing the old thing, counted, while the new loop is built beside it.

**Inbound.** When the same question reaches the team three times in 30 days, and neither the agent nor the product can answer it yet, [open](skills/open/SKILL.md) proposes a bridge: the smallest artifact that answers it today (a page, a saved reply, an in-app line, a short call), paired with a `flaw` item asking product to make the bridge unnecessary. The bridge's exit is that flaw shipping.

**A launch.** A new action class that ships before its spec, its sources, or its ledger columns gets a bridge for each missing piece.

## Common bridges

| Responsibility | The bridge | The number that falls | Retire it when |
|---|---|---|---|
| Documentation | The existing help center | Live page count, and visits per page | Only the [five forms](responsibilities/documentation.md#what-the-decision-can-be) remain |
| Documentation | A guide for a sequence the product cannot walk yet | Visits to the guide | The product walks the sequence |
| Value | The old scorecard: logins, seats, CSAT | How many reports still lead with it | The board reads the [new scorecard](metrics.md) first for two quarters |
| Value | A hand-built business review deck | Hours to build one | The value note is drafted from the ledger |
| Context | Facts kept in a CRM field or a doc the agent cannot read | Facts outside the memory store | The agent reads and cites them in the product |
| Onboarding | Kickoff calls for every account | Share of accounts that get one | Only accounts that were sold one get one |
| Floor | People answering moments the agent could hold | Share of those moments held by people | The kind's rung covers it |
| Voice | A support tool's tags as the flaw record | Flaws tracked only as tags | Each flaw is one item with a count |
| Forensics | Engineering reconstructs every incident | Time to a cause without an engineer | CX reconstructs alone in minutes |
| Ledger | [Sampling by hand](ledger.md#sampling-by-hand) | Hours a week spent sampling | Level 3 or 4 |

## Tracking them down

- **Weekly.** Open adds each bridge's review as an `upkeep` item. Triage updates `now`. A bridge whose number has not moved in four weeks is flagged at close: either the new loop is stuck, or the exit was wrong.
- **When the exit is met,** triage proposes retiring it: the page taken down, the report dropped, the call no longer offered. The customer-facing ones follow the [documentation](responsibilities/documentation.md) disposition `remove`, and never go silently.
- **Quarterly.** The bridges table goes next to the setup re-run. Count, total of each measure, retired this quarter. A growing list is a finding.

## Rules

1. **A bridge never blocks the new loop.** Keep the old help center up. Do not write new articles for behavior the product should explain.
2. **A bridge built from inbound expires.** If its flaw is held, or not shipped in 90 days, the bridge is reviewed: keep it as a real page in one of the five forms, or take it down.
3. **Count honestly.** If a number goes up, say so at close. A bridge that grows is legacy.
