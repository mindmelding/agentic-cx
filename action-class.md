# Action class

A delegated action is one thing the product did, or declined to do, for a named person. An **action class** is the kind that action belongs to. The ledger stores instances. The spec, the rung, the value story, and the doc decision all attach to the class.

## What a class is

A class is one capability a customer can delegate, named so that many instances share a single contract. A product-analytics agent that answers questions about user behavior has a class, `answer_behavior_question`. Priya asking "what changed in activation this week?" on Thursday is an instance of it.

Every class carries:

| Field | What it fixes |
|---|---|
| Name | The id used by the ledger, the rung table, and the spec file. |
| Fires when | The event that starts it. |
| May | What an instance is allowed to do. |
| Never | What no instance may do. The boundary. |
| Approval | Who has to say yes, and at which rung. |
| Default rung | Where a new account starts. |
| Sources | The code paths that implement it. A change here marks the spec unverified. |

```yaml
class: answer_behavior_question
fires_when: someone on the team asks how people are using their product
may:
  - answer from that company's own events
  - name the group of users that accounts for a change
never:
  - invent a number that is not in the events
  - show one customer's users to another customer
approval: none for a read. The answer is the action
default_rung: 3
sources:
  - src/analytics/answer.ts
  - src/analytics/what-changed.ts
```

## What stays the same kind

A feature is usually a change inside a class that already exists. Naming which group moved, instead of only returning a total, is the same class. The sources change, and the spec is re-checked. The [documentation example](responsibilities/documentation.md) is this case: the update is flagged, and the decision is that no page is needed, because the answer itself reveals the new behavior.

A new class opens when the product can now do a kind of work with its own trigger, its own boundary, and its own rung. Answering a question and warning a team that activation fell, without being asked, are two classes. Two ways of explaining the same change are one.

## What other pages mean by it

- [Context](responsibilities/context.md) records which facts an instance cited.
- [Change](responsibilities/change.md) stores a rung per class per account.
- [Value](responsibilities/value.md) groups ledger rows by class.
- [Documentation](responsibilities/documentation.md) keeps one spec per class and decides, after the sources change, whether anything public has to move.
- [Forensics](responsibilities/forensics.md) reconstructs one instance and may demote the class.
