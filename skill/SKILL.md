---
name: agentic-cx
description: Set up the agentic CX operating manual for the person running CX. Learn their role, read what past chats and connected tools already show, score each responsibility against where they are today, and write a gap report and stack.md. Use when someone adopts this repo, asks what their CX team is missing, or asks which tools they need. Re-run quarterly to show movement.
---

# Agentic CX setup

The operator's first day. The person in front of you runs CX, or is about to, at a company whose customers mostly meet the product through an agent. By the end they should know where they stand on each responsibility in [`../README.md`](../README.md), what is missing, and the one loop to start this week.

The rule under all of it: **look before you ask.** Their machine already knows a lot about their role, their tools, and their week. Read that first. Then confirm instead of asking, and ask only what nothing on disk could tell you.

Do not fork the pages in `responsibilities/`. They stay vendor-neutral. Everything this skill writes goes in `stack.md` and `local/`, both gitignored.

## 0. Ask to look

Say what you want to read and wait for a yes:

- Past chats and agent memory on this machine, for what they work on and which tools they name. Summaries only.
- Connector config for each agent host, for which tools are wired.
- The product repo, if they point at one: manifests, CI and compose config, docs, and the **names** of environment variables.

It never reads secret values, production data, or customer records. Customer words found in a chat are not copied into any file.

If they decline a source, skip it and ask about that part instead.

## 1. Look (silent)

**Past chats and memory.** Read what the host exposes. Look for the operator's title, team, recurring work, the tools they name, and what they complain about.

| Host | Where to look |
|---|---|
| Claude Code | `~/.claude/CLAUDE.md`, project `CLAUDE.md` files, memory files, and transcripts under `~/.claude/projects/` |
| Claude (desktop or web) | Memory and past conversations, when the host gives the agent access to them |
| Codex | `~/.codex/` instructions and session history |
| Cursor | Rules, `AGENTS.md`, and chat history, when exposed |
| Any | `AGENTS.md`, a personal notes repo, the README of the repo they pointed at |

If the host gives no access to past chats, say so in one line. Do not imply you read what you could not.

**Connected tools.** Read the MCP connector config for each host (`~/.claude.json`, `.mcp.json`, `~/.cursor/mcp.json`, `~/.codex/config.toml`, `~/.gemini/settings.json`), and the list of connectors the current host can see. A connector configured but not authorized is `partial`.

**The product repo.** If they pointed at one, scan it the way [`../tools.md`](../tools.md#how-a-scan-decides) describes.

Match everything to the capabilities in `tools.md`. Mark each `found`, `partial`, or `absent`. A nearby product that does not do the job is `partial`: a CRM is not an action ledger.

## 2. Confirm what you found

One message. A short list, in plain sentences, of what the disk already said, then one question: "Anything to change?"

- Their role, team, and who they report to.
- What the product does, and who its customer is.
- Who answers customers today: the agent, people, or both.
- The tools you found, grouped by responsibility.

Record their corrections. Do not re-ask anything they confirmed.

## 3. Ask the unknowns, one per turn

Only what nothing on disk answered. Offer a default they can accept with "yes." Never a form. Never two questions in one message.

- Team size, and who holds each function in [`../roles.md`](../roles.md) today, by name. "Nobody" is an answer.
- Which channel the team works in: Slack, email, a ticket tool.
- Which tools are inward only: summaries, deflection, QA on the team's own queue.
- Whether product has a tracker CX can file into, and who on product owns the line in [`../boundary.md`](../boundary.md).
- For each `partial` or `absent` capability: where it lives today, if anywhere, who may write it, and whether they will take the default in `tools.md`.
- What they would show their CEO to prove CX worked last quarter. The answer says which old metrics they are still reporting.
- How the product is priced. Run the interview in [`../pricing.md`](../pricing.md#interview), one question per turn, after looking at the pricing page and any contract they share.

## 4. Score the gap

For each responsibility, pick one level, with one line of evidence from what you read or heard:

| Level | Means |
|---|---|
| 0 Not done | Nobody holds it. |
| 1 The old way | Someone holds it, measured with the old scorecard: logins, tickets, CSAT, article count. |
| 2 Instrumented | The capabilities in `tools.md` exist and data flows, but the loop is not run on its cadence. |
| 3 Running | The loop runs on its cadence, and the measure from [`../metrics.md`](../metrics.md) is reported. |

Score all seven, plus the floor:

| Area | Level 3 looks like |
|---|---|
| [Onboarding](../responsibilities/onboarding.md) | Time to first accepted action reported. Stall list read daily. |
| [Context](../responsibilities/context.md) | Facts in the product with an author and a citation. Context health reported. |
| [Change](../responsibilities/change.md) | A rung per class per account. Promotions proposed on evidence. |
| [Value](../responsibilities/value.md) | Renewal stories cite ledger rows. |
| [Documentation](../responsibilities/documentation.md) | One spec per class. `never` lines checked weekly. Page count falling. |
| [Forensics](../responsibilities/forensics.md) | Any action reconstructed in minutes. Severity by reach. |
| [Voice](../responsibilities/voice.md) | Each flaw one item with a count, passed or held daily. |
| [Floor](../floor/README.md) | Moments split between agent and people. People's time goes to the moments a person holds. |

Record the [ledger level](../ledger.md#when-there-is-no-ledger), 0 to 4. Most scores above 2 depend on it.

Also note, for each, whether CX or product holds it today, and whether that matches [`../boundary.md`](../boundary.md). A mismatch is a finding, not a fault.

## 5. Write

**`stack.md`** at the root of this repo. One section per responsibility, then `inward`:

```markdown
## Context
- Memory store: found, Postgres `memories` (product repo)
- Citation log: absent, accept default, `context_cited` on the ledger
- Correction path: partial, memories are editable in admin, no customer path yet
```

**`local/assessment.md`**, the gap report:

```markdown
# Assessment, YYYY-MM-DD

Operator: <name, title>. Team: <n>. Answers customers today: <agent | people | both>. Ledger level: <0-4>.

| Area | Level | Evidence | Holder | Gap | Next step |
|---|---|---|---|---|---|

## Metrics you can report today
## Metrics still on the old scorecard
## Where the CX and product line sits differently from boundary.md
## Pricing
## First loop
```

The first loop names one [action class](../action-class.md) to instrument, using only tools now in `stack.md`, and points at the [two-week start](../README.md#a-two-week-start).

On a re-run, keep the old assessment and write a new dated one. The point is the movement.

**`local/queue.md`, the setup plan.** Turn the gaps into `setup` items, in the shape in [`../queue.md`](../queue.md#an-item), ordered so each one unblocks the next. Ten to twenty items, each small enough to finish in one sitting, each with a `done when` line. Typical items:

- connect the context store, the inbox, or the tracker named in `stack.md`
- start sampling 20 actions a week for one account, if the ledger is below level 2
- write the first action class spec, with its `never` lines and `sources`
- ask product for the five ledger columns, as a `flaw` item to pass
- define the stall signals and the first-run question
- fill the overlay (step 7)

Any area that scored 1, the old way, also gets a bridge in `local/bridges.md`, in the shape in [`../bridges.md`](../bridges.md#a-bridge): what it keeps, what it waits on, the number that should fall, its baseline today, and its exit. The team keeps the old thing running, counted, while the new loop is built beside it.

Work that product owns goes in as `blocked`, linked to the item that asks for it, so the plan shows the whole path. Also create `local/rungs.md` with every kind at its starting rung from [`../queue.md`](../queue.md#kinds), and an empty `local/log.md` and `local/rules.md`.

## 6. Read it back

In paragraphs, the way a colleague would say it. Not a table dump.

1. Where they stand, in two sentences.
2. The three biggest gaps, each with why it matters for an agent product and the smallest step to close it.
3. The first loop, how many setup items are in the queue, and the bridges, with the number each one starts at.

Then ask one question: "Start working the plan now, or set up the floor first?" Working the plan is [triage](../skills/triage/SKILL.md). Setup items are worked the same way as every day's work after them.

## 7. Set up the floor (when they say so)

This configures the agent that drafts customer replies, and fills the company overlay. About fifteen minutes. Same rule: look before you ask.

**Where the overlay lives.** `local/overlay/`, copied from [`../templates/house/overlay/`](../templates/house/overlay/README.md). Nothing in it is ever committed.

**Confirm what is known.** Most answers came from steps 1 to 3. Bundle them in one message and ask "Anything to change?": who they are and how they sign off, what the company sells and to whom, the customer's file (the context source), how customers are told apart from prospects, the channels customers write in.

**Ask the rest, one per turn, each with a default they can accept with "yes":**

| Ask | Default | Writes to |
|---|---|---|
| Two of their own replies they're proud of, or two you found that they confirm | Skip allowed. The most valuable answer here | `exemplars.md` |
| Anything they never want said | The canon lexicon | `voice-overrides.md` |
| Who handles billing, security, product, and anything with a lawyer, and in which time zone | The operator, for everything | `people.md` |
| Which written policies exist: refunds, SLAs, retention, plan changes | None. Anything unwritten is escalated | `policies.md` |
| How much the agent may credit per incident without asking | 0. Every credit is a nudge | `authority.md` |
| The same for gifts and gestures | 0 | `authority.md` |
| Which customer fields may be read freely | Name, email, company, plan, time zone | `authority.md` |
| When to say it is an agent, beyond when asked | When it materially matters | `authority.md` |
| What first value looks like for a new customer | What the product repo or onboarding docs suggest | `product.md` |
| Which moments a person holds, if different from the [floor default](../floor/README.md#who-holds-the-moment) | The default | `authority.md` |
| How far back to look for what needs doing: 7, 14, or 30 days | 14 | `in-motion.md` |

Write after every answer, and confirm what was saved in five words or fewer. A half-finished interview is still progress.

**End with work, not "ready."** Read the window through the customer's file and add three to five items to the queue for what needs doing: overdue promises, threads waiting on us, onboarding stalls, accounts that went quiet, a first clean autonomous run worth telling a customer about. Each with a draft and the file it came from. Add one gesture from [`../floor/delight/catalog.md`](../floor/delight/catalog.md) if the record supports one. Everything is a draft. Ask: "Which one first?" Draft that one in full. Whatever they change is the first line of today's day note.

## After

Offer to walk one responsibility page and substitute their tool names in conversation. Leave the pages in `responsibilities/` unchanged, so the manual stays shareable.
