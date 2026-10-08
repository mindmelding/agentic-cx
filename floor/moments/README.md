---
id: moments
type: index
status: active
last_reviewed: 2026-10-08
---

# Moments

The situations a customer can be in, one playbook each, in Agent Skills format (`<slug>/PLAYBOOK.md`). A playbook gives the trigger, who holds the moment, the steps, the guardrails, one example, what to write back, and what the evals check.

## How to pick a playbook

1. `MINDSET.md` and `PRECEDENCE.md` are always loaded.
2. Read the file (`context/CONTRACT.md` rows 1 and 2) before you pick anything. The moment is often in the file, not in the message.
3. Load the one moment that matches. If the thread spans two (a bug report from someone who has also gone quiet), load the second. Never more than two.
4. If nothing matches, it's `small-moment`. Most things are.
5. Check who holds it, in the table below or the overlay. A person-held moment is drafted for a person, who sends it.

## The moments

Holders are the defaults from [`../README.md`](../README.md#who-holds-the-moment). Principles are in [`../principles.md`](../principles.md).

| Moment | Trigger | Holder | Leans on |
|---|---|---|---|
| [`first-reply`](first-reply/PLAYBOOK.md) | First message from someone we have never spoken to | Agent | p01, p02, p16 |
| [`small-moment`](small-moment/PLAYBOOK.md) | Transactional: a reset, an invoice line, where a setting is | Agent; a person steps into a few | p28, p07, p17 |
| [`onboarding-first-100-days`](onboarding-first-100-days/PLAYBOOK.md) | New account or group, or the stated outcome not yet reached | Agent until a stall | p21, p03, p10 |
| [`integration-setup`](integration-setup/PLAYBOOK.md) | Connecting systems, configuring a sync or webhook | Agent | p02, p06, p03 |
| [`technical-troubleshooting`](technical-troubleshooting/PLAYBOOK.md) | A problem that needs diagnosis, not just a report | Agent until two replies without converging | p02, p23, p26 |
| [`bug-report`](bug-report/PLAYBOOK.md) | Something is broken and they told us | Agent; the flaw goes to voice | p02, p03, p13, p19 |
| [`feature-request`](feature-request/PLAYBOOK.md) | They asked for something the product does not do | Agent; the request goes to voice | p14, p13, p15 |
| [`feature-launch`](feature-launch/PLAYBOOK.md) | We shipped something they asked for or would use | Agent | p10, p15, p08 |
| [`data-export`](data-export/PLAYBOOK.md) | They want their data out, once or on a schedule | Agent inside a grant | p24, p11, p06 |
| [`refund-or-credit`](refund-or-credit/PLAYBOOK.md) | Money is on the table, asked for or owed | Agent inside a grant | p18, p24, p05 |
| [`our-mistake`](our-mistake/PLAYBOOK.md) | Outage, incident, data issue, a promise we missed | Person | p19, p04, p24, p18 |
| [`angry-customer`](angry-customer/PLAYBOOK.md) | Heat in the message, or a thread that has gone bad | Person | p09, p26, p04 |
| [`their-bad-day`](their-bad-day/PLAYBOOK.md) | Layoffs, a champion who left, news they raised | Person | p09, p08, privacy |
| [`silence`](silence/PLAYBOOK.md) | Delegated work or replies stopped | Person | p20, p08 |
| [`account-health-check`](account-health-check/PLAYBOOK.md) | Checking an account's progress, especially when it drifts | Person | p20, p08, p10 |
| [`renewal-conversation`](renewal-conversation/PLAYBOOK.md) | Renewal inside 90 days | Person | p13, p24, p27 |
| [`cancellation-and-offboarding`](cancellation-and-offboarding/PLAYBOOK.md) | They want out | Person | p22, p05 |
| [`handoff-to-human`](handoff-to-human/PLAYBOOK.md) | The moment exceeds the agent's authority or knowledge, or they ask for a person | The crossing | p25, p26, p23 |

## Not yet written

Public outage communication, security incident, price change, expansion signal, executive complaint, advocacy ask, milestone, win-back, VIP. Until one is written, use the nearest moment above and `PRECEDENCE.md`. Win-back and milestones are partly covered by [value](../../responsibilities/value.md) and the [delight catalog](../delight/catalog.md).
