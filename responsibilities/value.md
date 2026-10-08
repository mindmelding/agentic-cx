# Value

## Mandate

Own retention, expansion, and the commercial conversation. The proof is transformed work, taken from the ledger.

## Delivered when

A renewal or expansion conversation cites specific actions: what ran, how often a person accepted or reversed it, and which rungs moved. A story with no ledger rows under it is not ready to tell.

## The loop

1. Every delegated action lands in the ledger, including the ones a person ignored or reversed. Rows of the same kind share an [action class](../action-class.md).
2. Through the term, tag a value story to the rows that support it. The story names the workflow that changed.
3. At renewal, the review is those stories plus the rung profile. Seat charts stay out of the deck.
4. Expansion is the next capability that is ready to climb, or the next group ready to start at draft.

## Tools

### Capabilities required

- An action ledger at the grain of one delegated action.
- A renewal date and an owner.
- A place to attach a story to ledger ids.

### Signals a scan can see

An events, actions, or audit table. A CRM opportunity or a billing subscription. A QBR doc or a note field. See [tools](../tools.md).

### If nothing is found

Postgres, with the columns below. The renewal date is the one already in the CRM. The story stores the ledger ids it depends on.

Suggested columns: id, time, build, account, actor, action class, moment, rung, held by (`agent` or `person`), context cited, payload, boundary checks, disposition (`accepted`, `edited`, `ignored`, `reversed`, `blocked`), disposed by, edit diff, later outcome, harm.

If product has not built it, the [ledger](../ledger.md#when-there-is-no-ledger) page says how to run this loop from reconstructed, observed, or sampled rows, and how to label a story that rests on them.

`moment` is the playbook slug from [`floor/moments`](../floor/moments/README.md) when a person was on the other end. It is empty when the product acted and no reply was owed.

## When an account is leaving

Nobody churns loudly. The decision is made weeks earlier, and it shows in the record before it shows in a message. One signal is a reason to look. Two is a reason to act.

| Signal | Where it shows | The honest play |
|---|---|---|
| Delegated work that stopped | Accepted actions fell to near zero, or a class went unused | Name the date it changed, ask if something broke on their side, offer to do a piece of the work |
| Reversals and edits rising | Disposition trend on a class that was stable | Fix the cause first. Propose a demotion before they ask for one |
| Champion left | Context rows 3 and 7 | Find the successor, document what the champion set up, ask the successor's outcome in their words |
| Seats flat, people gone | Seat pricing with the agent doing the work | Say the numbers plainly and offer the smaller plan before they ask |
| Contract and billing questions | Notice periods, auto-renew, two invoice questions in a month | Answer exactly, cite the clause, then ask what prompted it |
| Outcome never reached or never recorded | Onboarding never graduated | Ask the outcome again, then do the next step for them |

Find the reason, fix the reason, then talk about money if money is the reason. Never discount first. A discount on a product that is not working is a slower cancellation.

When the reason is real and cannot be fixed, help them leave well (p22 in [`floor/principles.md`](../floor/principles.md)). After the cancellation is done, ask one question: "What was the thing that made you decide?" Record the answer in their words. The only honest win-back is a single message, sent when that reason is fixed, quoting it back. If it is never fixed, they never get one.

## Cadence

- **Daily.** No commercial ritual. The ledger write is the product's job.
- **Weekly.** One story tagged to rows, for an account that is actually in motion.
- **Quarterly.** The renewal review: volume, acceptance, edit distance, rungs moved.

## Artifacts

- The ledger.
- The value story: the workflow, the rows, the commercial ask.
- The renewal note a sponsor can forward.

## Measures

Gross retention and net retention, read next to acceptance rate and rungs moved. A rising renewal number with no movement in accepted work is a warning, not a win.
