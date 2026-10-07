# Floor

How customers are supported when the product is an agent. The agent answers most of what comes in. This canon is for the agent when it replies, and more so for the people on the team, who spend the time the agent freed on the moments that need a person.

It moved here from [front-of-house](https://github.com/scmancillas/front-of-house). Paths named inside these files are relative to this directory. Where `MINDSET.md` and the playbooks say "you," they mean whoever is on the floor for that moment, a person or the agent.

## Load

1. [`MINDSET.md`](MINDSET.md) and [`PRECEDENCE.md`](PRECEDENCE.md).
2. The customer's file, using [`context/CONTRACT.md`](context/CONTRACT.md). The moment is often in the file.
3. One playbook from [`moments/`](moments/README.md). A second only when the thread is clearly two moments. If nothing matches, [`small-moment`](moments/small-moment/PLAYBOOK.md).
4. Who holds it, from the table below.

Delight is a second decision, after the playbook, from [`delight/catalog.md`](delight/catalog.md). It needs one verifiable detail and a clear delight history.

## Who holds the moment

The agent holds the fast, clean ninety-five percent. People hold the moments where the customer needs to know a person is there, or where the stakes are above what the agent is granted. The agent still reads the file and drafts. A person sends.

| Holder | Moments |
|---|---|
| **The agent, alone** | [`small-moment`](moments/small-moment/PLAYBOOK.md), [`first-reply`](moments/first-reply/PLAYBOOK.md), [`integration-setup`](moments/integration-setup/PLAYBOOK.md), [`feature-launch`](moments/feature-launch/PLAYBOOK.md), [`feature-request`](moments/feature-request/PLAYBOOK.md), [`bug-report`](moments/bug-report/PLAYBOOK.md), [`technical-troubleshooting`](moments/technical-troubleshooting/PLAYBOOK.md) |
| **The agent, inside a grant** | [`refund-or-credit`](moments/refund-or-credit/PLAYBOOK.md) and [`data-export`](moments/data-export/PLAYBOOK.md). Inside a standing grant in `guardrails/authority.md`, the agent acts. Outside it, a person decides. |
| **The agent, until a signal** | [`onboarding-first-100-days`](moments/onboarding-first-100-days/PLAYBOOK.md). The agent walks the path. A stall signal from [onboarding](../responsibilities/onboarding.md) moves it to a person. |
| **A person, the agent drafts** | [`our-mistake`](moments/our-mistake/PLAYBOOK.md), [`angry-customer`](moments/angry-customer/PLAYBOOK.md), [`their-bad-day`](moments/their-bad-day/PLAYBOOK.md), [`silence`](moments/silence/PLAYBOOK.md), [`cancellation-and-offboarding`](moments/cancellation-and-offboarding/PLAYBOOK.md), [`renewal-conversation`](moments/renewal-conversation/PLAYBOOK.md), [`account-health-check`](moments/account-health-check/PLAYBOOK.md) |
| **The crossing** | [`handoff-to-human`](moments/handoff-to-human/PLAYBOOK.md). How the agent hands any moment to a named person. |

Any moment moves to a person when [`guardrails/escalation.md`](guardrails/escalation.md) says so: two replies without converging, a customer asking for a person, an unhappy executive, anything that smells like security or legal.

The table is a default. A company can move a moment in its overlay. Moving one toward the agent is a rung change and follows [change](../responsibilities/change.md): a record of accepted drafts first. Moving one toward a person needs only a reason.

## What the freed time is for

A person on the floor is not a slower agent. When a person holds a moment, they bring what the agent cannot:

- **Presence.** On the bad day, on our mistake, on the way out, a name the customer can hold.
- **Going first.** The stall list, the silence list, a milestone worth naming. A person reaches out before the customer has to.
- **Judgment on the five percent.** The agent can find the detail. A person decides the gesture is worth making.
- **Teaching.** An edit to a draft is a lesson. A wrong fact gets corrected in the store. A failure becomes an eval case in [`evals/`](evals/rubric.md).

A person who spends the day on moments the agent could hold alone is a sign the class is on the wrong rung. Move it.

## What stays out of this folder

A company overlay is not in this folder. Grants, learned phrases, and what was already sent stay in `local/` at the repo root. The day note in `local/learnings/days/` is the old inbox. Lessons do not come back into this canon.

Install adapters, evals tooling, and the check script still live in the front-of-house repo until the packaging pass. Edit the canon here.
