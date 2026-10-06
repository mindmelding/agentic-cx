# Action class

A delegated action is one thing the product did, or declined to do, for a named person. An **action class** is the kind that action belongs to. The ledger stores instances. The spec, the rung, the value story, and the doc decision all attach to the class.

## What a class is

A class is one capability a customer can delegate, named so that many instances share a single contract. A sales-coaching product that writes a private note after each recorded call has a class, `post_call_debrief`. The note for Maya's call with Acme on Tuesday is an instance of it.

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
class: post_call_debrief
fires_when: a recorded sales call finishes and the recording is available
may:
  - post a private note to the rep who was on the call
  - include a follow-up draft the rep can copy
never:
  - message the buyer
  - invent a discount
  - put the note anywhere the buyer can read it
approval: the rep, before any follow-up is sent
default_rung: 1
sources:
  - src/coaching/debrief.ts
```

## What stays the same kind

A feature is usually a change inside a class that already exists. A tighter critique, a different tone, a faster model: same class, same spec, sources touched, spec re-checked.

A new class opens when the product can now do a kind of work with its own trigger, its own boundary, and its own rung. Practicing a call before it happens and debriefing a call after it happened are two classes. Two wordings of the debrief are one.

## What other pages mean by it

- [Context](responsibilities/context.md) records which facts an instance cited.
- [Change](responsibilities/change.md) stores a rung per class per account.
- [Value](responsibilities/value.md) groups ledger rows by class.
- [Documentation](responsibilities/documentation.md) keeps one spec per class and decides, after the sources change, whether anything public has to move.
- [Forensics](responsibilities/forensics.md) reconstructs one instance and may demote the class.
