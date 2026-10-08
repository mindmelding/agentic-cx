# The queue

Everything this team has to do lands in one queue, and one loop works through it: [triage](skills/triage/SKILL.md). Setup fills it with the plan. Each morning, [open](skills/open/SKILL.md) fills it with what is new. The cadences on the responsibility pages fill it on their day. Then a person works it, top first, until it is empty or the day is.

The queue runs on the same unit the manual asks the product to run on. Each item is an action of a known kind. Each kind sits on a rung. Every decision the operator makes is logged, and the log is what earns a kind its next rung. The team's own work compounds the way the product's should.

Five files, all in `local/`, none committed:

| File | What it holds |
|---|---|
| `local/queue.md` | Open items |
| `local/log.md` | One line per closed item: what was proposed and what the operator did |
| `local/rungs.md` | The current rung for each kind, and when and why it moved |
| `local/rules.md` | Rules learned from repeated edits, each with its evidence and expiry |
| `local/bridges.md` | The old ways kept on purpose, each with a number that should fall and an exit. See [bridges](bridges.md) |

## An item

```markdown
### Q-0142 · stall · Acme
- why: no accepted action 9 days after signup; context floor met
- source: ledger query, 2026-10-08
- handler: floor/moments/onboarding-first-100-days
- rung: draft
- sensitive: no
- due: 2026-10-09
- status: open
```

A `setup` item also carries `done when:`, one line that says how anyone can tell it is finished.

`status` is one of `open`, `blocked` (with what it waits on, and a link), or closed with a disposition in the log. Items are numbered in order and never reused.

## Order

Triage takes the highest band first, then the earliest due date, then the oldest.

1. **A customer is waiting.** A thread with no reply from us.
2. **Harm.** A severity 1 or 2, or a broken `never`.
3. **Stalls.** Onboarding stalls and silences.
4. **Decisions waiting.** A flaw to pass or hold, a doc disposition, a promotion to propose.
5. **Setup.** The plan from setup.
6. **Upkeep.** Weekly checks, idle facts, rereading holds, refresh rows.

Open posts the top five as the board. An item untouched for 14 days expires to `dropped` with a line in the log, unless it is blocked.

## Kinds

Each kind has a handler, a starting rung, and a ceiling. The ceilings are set here, in the tracked manual, so the agent cannot raise them. `local/rungs.md` may hold a kind lower than its ceiling, never higher.

| Kind | What | Handler | Starts at | Ceiling |
|---|---|---|---|---|
| `reply` | A reply in a moment the agent holds | [floor](skills/floor/SKILL.md) | Draft | Act with notice |
| `reply-person` | A reply in a moment a person holds | [floor](skills/floor/SKILL.md) | Draft | **Draft** |
| `gesture` | A receipt, correction landed, prepared not done, held back | [templates](templates/customer/README.md) | Draft | Act with notice |
| `stall` | An onboarding stall | [onboarding](responsibilities/onboarding.md) | Draft | **Draft** |
| `silence` | Delegated work or replies stopped | [silence](floor/moments/silence/PLAYBOOK.md) | Draft | **Draft** |
| `incident` | Harm, graded by reach | [forensics](responsibilities/forensics.md) | Propose | **Propose** |
| `fact` | A fact to write into the context store | [context](responsibilities/context.md) | Draft | Act silently |
| `flaw` | A new product flaw to pass or hold | [voice](responsibilities/voice.md) | Propose | **Propose** |
| `flaw-evidence` | New evidence on a flaw already passed | [voice](responsibilities/voice.md) | Act with notice | Act silently |
| `spec-flag` | Mark a spec unverified after a commit | [documentation](responsibilities/documentation.md) | Draft | Act silently |
| `doc-decision` | No page, a promise line, a guide, an update, or a removal | [documentation](responsibilities/documentation.md) | Propose | Act with notice |
| `check` | A weekly boundary check, idle-fact list, or hold reread | the responsibility page it comes from | Draft | Act silently |
| `promotion` | A customer class ready for the next rung | [change](responsibilities/change.md) | Propose | **Draft** |
| `value` | A value story or a forwardable value note | [value](responsibilities/value.md) | Draft | **Draft** |
| `setup` | A step from the setup plan | [setup](skill/SKILL.md) | Propose | **Draft** |
| `upkeep` | A refresh row, a stale rule, a producer change | [refresh](skills/refresh/SKILL.md) | Draft | Act with notice |
| `bridge` | Open, review, or retire a bridge | [bridges](bridges.md) | Draft | Act with notice |

**Retiring a bridge customers can see** (a public page, a call they were promised) is sensitive.

**Sensitive overrides the kind.** An item that touches money, personal data, account access, deletion, a `never` line, or anything sent outside the company is handled at propose, whatever its kind's rung. Its `sensitive` field says which.

### What the rungs mean here

| Rung | The agent | The operator |
|---|---|---|
| 0 Propose | Says what it would do and why | Decides, then the agent does it |
| 1 Draft | Prepares the whole thing | Accepts, edits, or rejects; the agent carries it out on a yes |
| 2 Act with notice | Does it, and lists it in the receipt | Can undo it in one step |
| 3 Act silently | Does it | Sees it only in the log and the Friday report |

## The log

`local/log.md`, append-only, one line per closed item:

```
2026-10-08 | Q-0142 | stall | draft | asked Dana's outcome, offered to connect the source | edited | cut the second paragraph
```

Date, item, kind, rung it ran at, what the agent proposed in one line, the disposition, and the edit in one line if there was one. Dispositions: `accepted` (as proposed), `edited`, `rejected`, `deferred`, `dropped`, `done` (acted at rung 2 or 3), `reversed` (undone after the fact).

## How it compounds

### Promotion

At Friday's [close](skills/close/SKILL.md), any kind whose record clears the bar is proposed for the next rung, as a [promotion offer](templates/customer/promotion-offer.md) written to the operator:

- the last 20 items of that kind accepted without an edit,
- none rejected or reversed,
- at least two weeks at the current rung,
- and the next rung at or below the ceiling.

The operator says yes or no. A yes is written to `local/rungs.md` with the date and the log lines behind it.

### Demotion

A `rejected` with a reason that the work was wrong, or any `reversed`, drops that kind one rung the same day. Triage says so in one line and writes it to `local/rungs.md`. The way back is the same bar.

### Rules from edits

When the same kind of edit shows up on three items of one kind within 30 days (the same paragraph cut, the same detail added, the same flaw always held), close proposes a rule:

```markdown
### R-007 · reply · learned 2026-10-17 · expires 2027-01-15
- rule: no second paragraph in a first reply unless they asked two questions
- evidence: Q-0142, Q-0151, Q-0163
- written to: local/overlay/voice-overrides.md
```

On a yes, the rule goes where the next draft will read it: the overlay, the voice overrides, or the producer that creates the item. It expires after 90 days unless the log keeps confirming it, and a rule that expires becomes an `upkeep` item to renew or drop.

### Producers that learn

The queue should hold what the operator acts on. When five items in a row from the same source or kind are `dropped`, close proposes narrowing that producer: a threshold raised, a source muted, a kind made weekly. On a yes, it becomes a rule in `local/rules.md` like any other.

### Before the operator arrives

A scheduled [open](install/README.md#running-the-day-on-a-schedule) may carry out items whose kind sits at act-with-notice or act-silently, and nothing else. It never touches a sensitive item. It writes a [receipt](templates/customer/receipt.md) to the top of the day note: what it did, with the item numbers, and how to undo each one.

## The Friday report

Close writes it to the day note. One short table and three numbers:

| Kind | Rung | Items | Accepted unedited | Edited | Rejected or reversed |
|---|---|---|---|---|---|

- Share of items closed without an operator edit.
- Share handled at act-with-notice or above.
- Items still open, and the oldest.

The same numbers the manual tells you to report for a customer, about your own team. A rising share handled without edits is the team getting more autonomous. A rising share of rejections is the rungs moving too fast.
