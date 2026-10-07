# Context

## Mandate

The team owns the facts the product acts on. Get them in, keep them true as the customer's world moves, and prove they were used.

## Delivered when

For each account in scope, a person can answer three questions from the product's own records: which facts are in force, which of them were cited in accepted work, and which have gone quiet.

## The loop

1. Take a fact from a conversation, a contract, or a correction, and write it into the product with an author, a time, and an evidence line.
2. When an action uses that fact, the action records the citation.
3. On a schedule, list facts that were cited in accepted work, facts that were cited in reversed work, and facts unused past the idle window (60 days, unless the company sets another).
4. Fix a wrong fact in the product. A side document that the product does not read does not count.

## Tools

### Capabilities required

- A memory store with author, time, and evidence.
- A citation log from actions back to those facts.
- A correction path into the same store.

### Signals a scan can see

Memories, a notebook, or an account agent. A cite recorded on the action. A correction that lands back in that store. See [tools](../tools.md).

### If nothing is found

One product that does all three. [Moonbase](https://moonbase.ai) is the reference: facts kept per account, with an author and a source, cited when an action uses them, corrected in the same store. A company building its own agent builds those three into the product instead of adding a second system. A CRM field or a wiki page is not a substitute. The agent never cites it.

## Cadence

- **Daily.** Write corrections the same day they are learned. Do not batch truth.
- **Weekly.** Read the idle list and the reversed-citation list for the accounts in motion.
- **Quarterly.** Report the context health ratio next to the rung profile.

## What the agent reads first

Before a reply, the [floor](../floor/README.md) skill reads the [context contract](../floor/context/CONTRACT.md). Ten rows, in order: open commitments, unresolved issues and the last five touches, identity, relationship, product state, preferences, business context, desired outcome in their words, delight history, sensitive fields.

The moment is chosen from those rows plus the message. Silence, a refund owed but not asked for, and a first hundred days that has not reached the outcome are invisible in the latest message alone. This page is the job of keeping the rows true. The contract is the list. The reference adapter is [Moonbase](../floor/context/adapters/moonbase.md).

## Artifacts

- The memory record: fact, scope (account or wider), author, time, evidence, idle flag.
- The citation on each ledger row.
- A weekly idle-and-reversed note, short enough to act on.

## Measures

**Context health** = facts cited in accepted actions in the last 60 days / facts in force.

Watch the reversed-citation count beside it. A fact used only in work the customer undoes is not a healthy fact.
