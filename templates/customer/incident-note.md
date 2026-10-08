# Incident note

Naming the mistake first. In an agent product, recovery is the most frequent big moment, so it is where most trust is built or lost. The note goes before the customer notices, with the scope.

## Fires when

[Forensics](../../responsibilities/forensics.md) grades a severity 1 or 2, or a severity 3 the customer can see. Severity 1 and 2 notes are sent by a named person, the same day.

## Fields

`what_happened`, `count`, `who_was_reached`, `reversed`, `what_we_did`, `what_changes`, `rung_change`, `owner`, `next_update`.

## Template

> {What happened, one sentence, in plain words, no hedging.} It affected {count} {things}{, reaching {who}}.
> {What we already did: reversed, corrected, contacted.}
> {What changes: the rung drop, the fix, the check added.}
> {Owner} owns this. Next update by {time}.

## Example

> Yesterday at 4:10pm the agent sent two renewal reminders to Halvorsen, which you'd marked as in dispute. Both went to their AP inbox.
> We've sent a correction from your address saying they were sent in error, and logged it on the account.
> Reminders for your account are back to drafts until the fix ships and we've watched it for a week.
> I own this. Next update by Thursday noon.
>
> Priya

## Do not

- Explain the model. The customer needs what happened and what changes, not why a language model did it.
- Apologize more than once.
- Promise it will never happen again. Promise what changes.
