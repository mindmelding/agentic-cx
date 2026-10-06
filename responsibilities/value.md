# Value

## Mandate

Own retention, expansion, and the commercial conversation. The proof is transformed work, taken from the ledger.

## Delivered when

A renewal or expansion conversation cites specific actions: what ran, how often a person accepted or reversed it, and which rungs moved. A story with no ledger rows under it is not ready to tell.

## The loop

1. Every delegated action lands in the ledger, including the ones a person ignored or reversed.
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

Suggested columns: id, time, build, account, actor, action class, rung, context cited, payload, boundary checks, disposition (`accepted`, `edited`, `ignored`, `reversed`, `blocked`), disposed by, edit diff, later outcome, harm.

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
