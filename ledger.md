# Ledger

The record of every **delegated action**: one row each time the product did something, or declined to, for a named person, and what a person did about it. Most numbers in [metrics](metrics.md) are queries over it. The [value](responsibilities/value.md) page has the full column list.

The ledger is product's to build ([boundary](boundary.md)). This team often starts without one. This page is how to run the manual anyway, and what to ask product for.

## The fewest columns that work

If product can add only five, ask for these:

| Column | Why it cannot be skipped |
|---|---|
| `time` | Every trend needs it. |
| `account` | Rungs, stories, and stalls are per account. |
| `action_class` | Acceptance means nothing until it is grouped by class. |
| `disposition` | `accepted`, `edited`, `ignored`, `reversed`, or `blocked`. This is the column almost nobody has. |
| `ref` | A link back to the trace, the message, or the record the action changed. Forensics starts here. |

`rung`, `context_cited`, `moment`, and `held_by` come next. Everything else can wait.

## When there is no ledger

Run the manual one level down, and say which level you are on. Every number reported on a lower level carries its level, so nobody mistakes a sample for a census.

| Level | Source | What you can run |
|---|---|---|
| **4 Native** | A ledger with dispositions. | Everything. |
| **3 Reconstructed** | Product events, audit logs, or traces joined into rows. Disposition is inferred from what happened next. | Acceptance by proxy, onboarding, forensics, value stories. Rungs, carefully. |
| **2 Observed** | The agent's output where this team can see it: the email it sent, the Slack message, the record it wrote in the customer's CRM. | Disposition by watching what the customer did to the output. Value stories. Stall signals. |
| **1 Sampled** | A person grades actions by hand: twenty per account per week, from screen share, an export, or the customer's own review. | Acceptance rate with a stated sample size. Rung proposals, with the sample attached. Eval cases. |
| **0 Told** | What the customer says in calls and mail. | Voice and context only. No acceptance rate. No rung moves. |

### Inferring disposition

At levels 2 and 3, disposition is read from what happened to the output after the agent produced it:

| What you see | Read it as |
|---|---|
| Sent, published, or kept, unchanged after a set window (48 hours by default) | `accepted` |
| Changed by a person before it went out, or within the window | `edited` |
| Undone, deleted, rolled back, or redone by hand | `reversed` |
| Never opened, never sent, left in draft past the window | `ignored` |
| The agent said it would not, or a check stopped it | `blocked` |

Write the rules down per class, and keep them stable. A proxy that changes every month is worse than none.

### Sampling by hand

Level 1 is slow and it works. Pick the accounts in motion, not all of them. Twenty actions per account per week is enough to see acceptance move. Grade each one with the disposition above and one line on why. The grades are also the first eval cases, because each `edited` and `reversed` is a failure a person already explained.

`scripts/cx ledger sample` makes the sheet from any CSV export, and `scripts/cx ledger report` reads it back as acceptance per class, with the sample size and the level on every number. See [`templates/ledger/`](templates/ledger/README.md), which also holds the table to hand product for level 4.

The customer can help. A champion who reviews the agent's work already decides accept, edit, or undo. Asking them to say which, for a week, is a small ask and a good conversation.

## What each responsibility does without one

- **Onboarding.** Stall signals from level 2: no output in seven days, outputs left in draft, the user asking how to do what the agent should do.
- **Context.** Unchanged. It lives in the memory store, not the ledger.
- **Change.** No promotion below level 1. A promotion brief states its level and sample size.
- **Value.** A renewal story can cite sampled or observed rows, labeled as such. Do not extrapolate a sample into a total.
- **Documentation.** The `never` check runs on whatever level exists, and says which. A `never` checked against a sample is checked against a sample.
- **Forensics.** Needs a trace. Without one, severity and reach still work. The cause goes to product.
- **Voice.** Unchanged.

## Getting to level 4

The ledger is the first item passed through [voice](responsibilities/voice.md). The issue is the five columns above, with the evidence that sampling by hand produced: the acceptance rate, how many hours the sample took, and the renewal it supported. A team that has been sampling by hand for a month has the best argument for a ledger anyone at the company can make.
