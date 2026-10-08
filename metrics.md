# Metrics

The scorecard for a customer team whose product does the work. Every number here is a query over the [ledger](ledger.md), the memory store, or the floor's own record. Without a ledger, report each number with the level it came from. A number that needs a survey or a seat count to compute is either lagging or on the list of things not to report.

## Why the old scorecard breaks

Conventional success metrics count a person operating software. In a product the customer delegates to, successful use drives that number down. Logins fall when the agent works. Tickets fall when the agent answers. Neither tells you whether the work got done, or whether the customer trusts it to do more.

## What replaces what

| The old metric | What it assumed | The replacement | Where it lives |
|---|---|---|---|
| Logins, DAU, time in product | Use means a person in the app | **Accepted actions** per account per week | [Value](responsibilities/value.md) |
| Feature adoption | Turning a feature on is the win | **Rung profile**: each class's rung for the account, and whether it moved | [Change](responsibilities/change.md) |
| Time to first login, setup complete | Setup is the hard part | **Time to first accepted action** | [Onboarding](responsibilities/onboarding.md) |
| Onboarding completion | A checklist reflects progress | **Outcome reached in window**, against the outcome they stated | [Onboarding](responsibilities/onboarding.md) |
| CSAT on a ticket | The reply is the product | **Acceptance rate** and **edit distance** on the actions | [Change](responsibilities/change.md) |
| Deflection rate | A bot reply that ends the thread is a resolution | **Pickup rate × end-to-end resolution**. A reopen is not a deflection | [Forensics](responsibilities/forensics.md) |
| Health score built from usage | Busy accounts are healthy | **Reversal rate**, **edit distance trend**, **context health** | [Context](responsibilities/context.md) |
| Help center views, article count | More pages, more help | **Pages removed** because the product now says it, and **`never` lines verified** | [Documentation](responsibilities/documentation.md) |
| Ticket volume by tag | Volume is the signal | **Voice items by count**, and time from first sight to pass or hold | [Voice](responsibilities/voice.md) |
| First response time, handle time | Speed is the job | **Human hours on human moments**, and **handed off twice** | [Floor](floor/README.md) |

## The scorecard

Leading numbers move this week. Lagging numbers confirm, months later, that the leading ones were right. Report both. Act on the leading ones.

### Leading

| Measure | Definition | Healthy direction |
|---|---|---|
| Accepted actions | Actions a person accepted or let stand, per account per week | Up |
| Acceptance rate | Accepted / (accepted + edited + reversed), per class | Up, then flat above the promotion bar |
| Edit distance | How much a person changed an action before it went out, on classes at draft | Down |
| Reversal rate | Reversed / all, per class | Down. A spike demotes |
| Time to first accepted action | Signup to the first accepted instance | Down |
| Stalled accounts | New accounts that tripped a stall signal and have no person or skip | Zero at the end of each day |
| Context health | Facts cited in accepted actions in the last 60 days / facts in force | Up |
| `never` lines verified | Share checked against last week's actions | 100% |
| Time to a cause | Flagged action to reconstructed cause | Under two minutes |
| Voice decision time | First sight of a flaw to pass or hold | Down |
| Human hours on human moments | Share of the floor's hours spent in moments the agent should not hold alone | Up |

### Lagging

| Measure | Definition | Read it beside |
|---|---|---|
| Gross retention | Revenue kept from the accounts you started with | Rung profile |
| Net retention | Gross, plus expansion | Rungs moved, classes added |
| Outcome reached in window | New accounts that reached their stated outcome in 30 days | Time to first accepted action |
| Self-onboarded share | Accounts that graduated with no human step-in | Outcome reached in window |
| Passes accepted | Filed issues the product team took without a rewrite | Voice decision time |
| Pages per class | Public pages / action classes | Pages removed this quarter |
| Bridges retired | [Bridges](bridges.md) whose exit was met this quarter | Bridges opened, and any whose number rose |

## The ones that look good and lie

- **A rising renewal with no movement in accepted work.** They renewed on inertia. It is a warning.
- **A high self-onboarded share with a low outcome rate.** The agent is leaving people alone.
- **Falling ticket volume.** It can mean the agent resolved it. It can mean they stopped asking. Read it beside reversal rate.
- **A growing help center.** A page that teaches a prompt is a product bug.
- **CSAT on agent replies.** It grades the tone of the reply, not whether the action was right.

## Reviews

- **Weekly, one page.** The leading table for accounts in motion. Each red cell has an owner and a next step.
- **Quarterly.** The lagging table, each number next to the leading numbers it depends on. If retention moved and nothing under it did, say that the explanation is missing.

## Starting with nothing

You do not need all of this to start. The [two-week start](README.md#a-two-week-start) produces acceptance rate and a rung for one class. Those two are enough to tell a renewal story nobody else at the company can tell. Add the next number when someone asks a question the first two cannot answer.
