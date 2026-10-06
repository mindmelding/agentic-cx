# CX in the age of agents

An operating manual for customer experience at a company whose product does work on a customer's behalf. Written to be adopted by a new company as it stands, and adapted to the tools that company already runs.

The responsibilities below are the job. This page is the position they sit on. Day to day is four skills and a folder of learnings, so the record is not trapped in one harness. The schedule is [`routines.md`](routines.md). The skills are in [`skills/`](skills/README.md). Learnings are in [`learnings/`](learnings/README.md).

A setup skill in [`skill/SKILL.md`](skill/SKILL.md) interviews a repo, with permission to scan, and maps the tools in [`tools.md`](tools.md) onto whatever it finds. It runs once.

## The shift

Conventional customer-success metrics count a person operating software: logins, seats, time in the product, feature adoption. In a product the customer delegates to, successful use drives that time down. A scorecard built on sessions will call a healthy account quiet and a struggling account engaged.

The unit that replaces the session is a **delegated action**: the system did something, or declined to, for a named person, using specific context, and a human accepted it, edited it, ignored it, or reversed it. Actions of the same kind belong to one [action class](action-class.md). The spec, the rung, and the doc decision all attach to the class. The ledger stores the instances.

Two uses of AI stay separate:

- **Inward.** Models on the customer team's own bench: summaries, risk flags, QA, deflection. They keep the team small.
- **Outward.** The product the customer bought. This manual is about delivering that.

## Principles

1. **The unit is the delegated action.** If it is not in the ledger, it did not happen. Health, trust, release impact, and context quality are queries over that record.
2. **Context is the scarce input.** The team gets it in, keeps it true, and proves it was used.
3. **Promise the boundary.** Under non-determinism the durable promise is what the system will never do, enforced in code and checked against production.
4. **Autonomy is the deliverable.** Each capability sits on a rung for each customer and moves on a record of accepted work.
5. **Revenue stays on the scorecard.** Renewal and expansion are told as transformed work, with the actions underneath.

## Responsibilities

Each page uses the same headings: mandate, delivered when, the loop, tools, cadence, artifacts, measures.

| | Responsibility | Delivered when |
|---|---|---|
| 1 | [Context](responsibilities/context.md) | Facts the customer depends on are in the product, current, and cited in accepted work. |
| 2 | [Change](responsibilities/change.md) | A named group has moved a capability up a rung on evidence, or been told why it stays. |
| 3 | [Value](responsibilities/value.md) | Renewal and expansion cite transformed work from the ledger. |
| 4 | [Documentation](responsibilities/documentation.md) | The public promise matches production, and pages shrink as the product learns to say the rest. |
| 5 | [Forensics](responsibilities/forensics.md) | A harmful action has a severity, an owner, and a cause in under two minutes. |
| 6 | [Voice](responsibilities/voice.md) | A product flaw has been passed to the builders, or held, and the issue was already written in their tracker's shape. |

Tools are named as capabilities in [`tools.md`](tools.md). The skill fills a local `stack.md` with the products this company actually uses, and recommends a default only where a capability is missing.

## Cadence

The detail lives on each responsibility page. Across the team:

- **Daily.** Clear the moment queue, and the voice queue. Pass or hold each new flaw. Read what the system did that a person has to be the one to handle.
- **Weekly.** Check declared boundaries against last week's actions. Retire one page the product can now say itself.
- **Quarterly.** Review the rung profile. Attach the value story to the ledger. Propose the next promotions.

## A two-week start

Pick one [action class](action-class.md).

1. Write its boundary: what it may do, what it will never do, who approves.
2. Record every instance, the context it cited, and how a human disposed of it.
3. Check last week against the boundaries.
4. Publish the acceptance rate and the current rung.

If that produces one fact the company did not already know, extend the same shape to the next class. If it produces nothing, the unit is wrong and the rest of this manual should wait.

## Field note

Public research in October 2026, across customer leaders at Harvey, Lovable, AssemblyAI, Anthropic, Intercom, Clay, and others, already treats this job as value realization and change management for AI. Adoption is counted as transformed work. Deflection is counted as pickup times end-to-end resolution. Titles move quickly, and several well-known companies had no named leader a public search could verify. Use the pattern. Re-verify anyone before outreach.
