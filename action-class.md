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
| Context floor | The facts and connections an account needs before a first instance is worth trying. |
| Reach | The systems and credentials an instance may use. Anything it can reach that is not listed is a defect. |
| Reversible | Whether an instance can be undone in one step, and by whom. Irreversible classes never run silently. |
| Sources | The code paths that implement it. A change here marks the spec unverified. |

A copy to start from is [`templates/spec/answer_behavior_question.yaml`](templates/spec/answer_behavior_question.yaml). `cx spec new <class>` writes a blank one.

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
reach:
  - read access to the company's event stream
reversible: yes. An answer changes nothing
context_floor:
  - the company's event stream is connected
  - the activation event is named
sources:
  - src/analytics/answer.ts
  - src/analytics/what-changed.ts
```

## What stays the same kind

A feature is usually a change inside a class that already exists. Naming which group moved, instead of only returning a total, is the same class. The sources change, and the spec is re-checked. The [documentation example](responsibilities/documentation.md) is this case: the update is flagged, and the decision is that no page is needed, because the answer itself reveals the new behavior.

A new class opens when the product can now do a kind of work with its own trigger, its own boundary, and its own rung. Answering a question and warning a team that activation fell, without being asked, are two classes. Two ways of explaining the same change are one.

## What other pages mean by it

- [Onboarding](responsibilities/onboarding.md) keeps the context floor for each class, and counts the first accepted instance as activation.
- [Context](responsibilities/context.md) records which facts an instance cited.
- [Change](responsibilities/change.md) stores a rung per class per account.
- [Value](responsibilities/value.md) groups ledger rows by class.
- [Documentation](responsibilities/documentation.md) keeps one spec per class and decides, after the sources change, whether anything public has to move.
- [Forensics](responsibilities/forensics.md) reconstructs one instance and may demote the class.
- [Voice](responsibilities/voice.md) turns the same flaw, seen across instances, into one item a person can pass to the builders.

## When a person is on the other end

The class is the capability. The moment is the situation. An instance that is also a reply records the playbook that fired, from [`floor/moments`](floor/moments/README.md), on the ledger row next to the class and the rung. `answer_behavior_question` often has no moment. A broken import handled on the floor can have both: the class, if the product did something, and `bug-report`. The [floor skill](skills/floor/SKILL.md) chooses the playbook after reading the [context contract](floor/context/CONTRACT.md).
