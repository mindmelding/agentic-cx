# Failures

Public cases where an agent product took a harmful or wrong action for a customer. Each one is read the way [forensics](../responsibilities/forensics.md) would read it: the action class, the boundary that should have held, the rung it was on, the severity by reach, and what the customer needed to hear.

Support chatbots that said something wrong are in [`floor/examples/hall-of-shame/`](../floor/examples/hall-of-shame/). This folder is for products that **did** something.

| Case | When | What the agent did | Severity by reach | Lesson |
|---|---|---|---|---|
| [Replit and SaaStr](replit-production-database.md) | Jul 2025 | Deleted a production database during a code freeze, then said rollback was impossible | 3 | A `never` in a prompt is not a `never` |
| [Gemini CLI file move](gemini-cli-file-move.md) | Jul 2025 | Overwrote a user's files one by one after a silent failure | 2 | Irreversible inside the customer is not minor |
| [Antigravity drive wipe](antigravity-drive-wipe.md) | Dec 2025 | Deleted a whole drive while clearing a cache | 2 | Destructive classes do not run silently |
| [PocketOS and Railway](pocketos-production-database.md) | Apr 2026 | Found a stray token and deleted production and its backups in nine seconds | 2 | The class's credentials are part of its boundary |
| [Kiro and AWS Cost Explorer](kiro-aws-outage.md) | Dec 2025 | Deleted and recreated a production environment | 2 | "User error" is a rung that was set too high |
| [Operator and the eggs](operator-eggs.md) | Feb 2025 | Bought groceries when asked to research them | 2 | Research and purchase are two classes |
| [OpenClaw inbox](openclaw-inbox.md) | Feb 2026 | Bulk-deleted email after losing a confirm-first instruction | 2 | Instructions can fall out of context. Gates cannot |
| [Amazon Q injected prompt](amazon-q-injected-prompt.md) | Jul 2025 | Shipped with a prompt telling it to wipe systems; it failed to run | 4 | The boundary has to hold against the agent's own inputs |

Severities use the table in [forensics](../responsibilities/forensics.md). Several of these read as a 1 in the headlines and a 2 or 3 by reach. That gap is the point of grading by reach.

## What repeats

1. **The `never` lived in a prompt.** A code freeze, "confirm before acting," "ask before submitting an order." Each was an instruction the agent could lose or override. The [boundary](../boundary.md) rule is that product enforces a `never` in code. Every case here where a stated rule failed is a case where it was only stated.
2. **The rung was too high for an irreversible class.** Deleting a drive, a volume, or an environment ran at act-silently, or close to it. Irreversible actions start at propose and stay at act-with-notice at most.
3. **The class could reach more than its job.** An over-permissioned token, permissions broader than intended. The credentials a class can use belong in its spec beside `may` and `never`.
4. **The agent misreported reversibility.** Replit's agent said rollback was impossible. It was not. Reversibility is a property the team knows from the system, not from the agent's account of itself.
5. **The agent's apology stood in for the company's.** "I have failed you completely and catastrophically." "I violated every principle I was given." A confession from the agent is not an [incident note](../templates/customer/incident-note.md). A named person, the same day, with the scope and what changes.
6. **The company blamed the user.** "User error," "users should review commands." If the rung let it happen, the rung is ours. Say what changes.

## Adding a case

One file per case, in the shape below. Only cases with at least one reputable source. Mark anything that only secondary sources report. Do not add a case from a researcher's demonstration unless real users were harmed.

```markdown
# <Case>

**When.** **Product.** **Confidence.** high | medium

## What the agent did
## Reach and severity
## What the company did
## Read as forensics
- Class:
- The `never` that should have held, and where it lived:
- Rung it ran at, and the rung it should have been at:
- Reversible, and who knew:
## What the customer needed to hear
## Sources
```
