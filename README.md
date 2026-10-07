# CX in the age of agents

An operating manual for customer experience at a company whose product does work on a customer's behalf, often through an agent the customer talks to directly. It is for the person running CX there. The conventional support and success playbook measures the wrong things in that product, and this is the replacement. Written to be adopted by a new company as it stands, and adapted to the tools that company already runs.

The responsibilities below are the job. This page is the position they sit on. The day is four skills: [open](skills/open/SKILL.md) when you start, [floor](skills/floor/SKILL.md) and [triage](skills/triage/SKILL.md) while the work is happening, [close](skills/close/SKILL.md) when you stop. The schedule is [`routines.md`](routines.md).

The floor canon lives in [`floor/`](floor/README.md): how customers are supported when the agent answers most of what comes in. It says which moments the agent holds alone and which a person holds, and what people on the team do with the time the agent freed. What the day teaches stays in `local/learnings/`, gitignored, so it can move to another agent without publishing a customer's words. The shape of those files is in [`learnings/`](learnings/README.md).

Three pages frame the job:

- [`metrics.md`](metrics.md). The scorecard, and which old metric each number replaces.
- [`roles.md`](roles.md). Support, success, onboarding, and documentation, and what each becomes.
- [`boundary.md`](boundary.md). What CX builds, what product builds, and where work crosses.

A setup skill in [`skill/SKILL.md`](skill/SKILL.md) interviews the operator. With permission, it reads past chats, connected tools, and the product repo, scores each responsibility against where the team is today, and writes a gap report and a local `stack.md`. Run it once to start, and again each quarter.

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

Onboarding is numbered zero because it comes first in an account's life and repeats for every new group. The rest run for the life of the account. Each page uses the same headings: mandate, delivered when, the loop, tools, cadence, artifacts, measures.

| | Responsibility | Delivered when |
|---|---|---|
| 0 | [Onboarding](responsibilities/onboarding.md) | Each new account and group has a stated outcome, a first accepted action, and a person reached it when it stalled. |
| 1 | [Context](responsibilities/context.md) | Facts the customer depends on are in the product, current, and cited in accepted work. |
| 2 | [Change](responsibilities/change.md) | A named group has moved a capability up a rung on evidence, or been told why it stays. |
| 3 | [Value](responsibilities/value.md) | Renewal and expansion cite transformed work from the ledger. |
| 4 | [Documentation](responsibilities/documentation.md) | The public promise matches production, and pages shrink as the product learns to say the rest. |
| 5 | [Forensics](responsibilities/forensics.md) | A harmful action has a severity, an owner, and a cause in under two minutes. |
| 6 | [Voice](responsibilities/voice.md) | A product flaw has been passed to the builders, or held, and the issue was already written in their tracker's shape. |

Who holds each one, and how that changes with team size, is in [roles](roles.md). Tools are named as capabilities in [`tools.md`](tools.md). The skill fills a local `stack.md` with the products this company actually uses, and recommends a default only where a capability is missing.

## Cadence

The detail lives on each responsibility page. Across the team:

- **Daily.** Clear the stall list, the moment queue, and the voice queue. Pass or hold each new flaw. Read what the system did that a person has to be the one to handle.
- **Weekly.** Check declared boundaries against last week's actions. Retire one page the product can now say itself.
- **Quarterly.** Re-run the setup skill and compare the gap report to last quarter's. Review the rung profile. Attach the value story to the ledger. Propose the next promotions.

## A two-week start

Pick one [action class](action-class.md).

1. Write its boundary: what it may do, what it will never do, who approves.
2. Record every instance, the context it cited, and how a human disposed of it.
3. Check last week against the boundaries.
4. Publish the acceptance rate and the current rung.

If that produces one fact the company did not already know, extend the same shape to the next class. If it produces nothing, the unit is wrong and the rest of this manual should wait.

## Field note

Public research in October 2026, across customer leaders at Harvey, Lovable, AssemblyAI, Anthropic, Intercom, Clay, and others, already treats this job as value realization and change management for AI. Adoption is counted as transformed work. Deflection is counted as pickup times end-to-end resolution. Titles move quickly, and several well-known companies had no named leader a public search could verify. Use the pattern. Re-verify anyone before outreach.
