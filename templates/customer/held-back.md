# Held back

Restraint as a gesture. Customers remember the time the agent did not do the dumb thing longer than any gift.

## Fires when

The agent declined, or a check stopped an action, and the reason is one the customer would want to know about: an unusual amount, a recipient not seen before, an instruction that conflicts with a fact in the file, a likely prompt injection. Routine blocks are not sent.

## Fields

`action_not_taken`, `reason`, `what_it_would_take`, `ref`.

## Template

> I didn't {action} {when}. {Reason, one sentence, specific.}
> {What would make it go: their yes, a correction, nothing.}

## Example

> I didn't send the invoice to Northwind this morning. It's four times their usual amount, and the PO on file is for the old quantity.
> If it's right, reply "send" and it goes now.

## Do not

- Send it for an action blocked by a `never`. That one is not a judgment call. Say it plainly in the thread where it was asked, without ceremony.
- Make it sound like the agent saved the day. State the fact.
