# Change

## Mandate

Move a named group from doing the work themselves to delegating it, one capability at a time, on evidence.

## Delivered when

Every capability in scope has a rung for that account, a person who owns the move, and a record of why it last changed. A group that is not ready has been told so, with the evidence.

## The loop

The rungs:

| Rung | What happens |
|---|---|
| 0 Propose | The system says what it would do. Nothing changes. |
| 1 Draft | It prepares the work. A person sends it. |
| 2 Act with notice | It acts, tells a person, and reversal is one step. |
| 3 Act silently | It acts. The action is in the record. |

1. Start a new capability at 0 or 1. The spec says which.
2. Watch acceptance, edit distance, and boundary violations for that class on that account.
3. When the record is strong, propose the next rung to the sponsor. The proposal carries the evidence. Applying the rung waits for their yes.
4. A serious reversal or a broken `never` drops the rung immediately and opens a forensic review.

A strong record, unless the company sets a tighter one: 50 consecutive instances, acceptance at or above 95 percent, no boundary violations. Promotion is proposed by the system and applied by a person.

## Tools

### Capabilities required

- A rung stored per capability per account.
- A promotion brief a sponsor can read.
- A named practice group, smaller than "the whole customer."

### Signals a scan can see

Feature flags, entitlements, an approval or autonomy config. CRM segments or workspace groups. The channel the account already uses. See [tools](../tools.md).

### If nothing is found

A table: account, action class, rung, changed at, changed by. The brief is a note in the channel they already have. The group is a field on the account.

## Cadence

- **Daily.** Nothing, unless a demotion fired.
- **Weekly.** Review classes close to a promotion. Send at most the briefs that are ready.
- **Quarterly.** Walk the rung profile with the sponsor. The meeting is that chart and the list of what would have to be true to move the next capability.

## Artifacts

- The rung table.
- The promotion brief: class, current rung, proposed rung, acceptance, reversals, boundary check, the ask.
- The demotion note, linked to the forensic record.

## Measures

The rung profile of an account, and whether it moved. Edit distance on classes still at draft. Time from "the record qualifies" to "the sponsor was asked."
