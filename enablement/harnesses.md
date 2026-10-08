# Harnesses

How the agent tools customers already use handle approval, undo, memory, and skills, and what each maps to on the rungs in [change](../responsibilities/change.md). Use the right-hand column to explain your own product's rungs in words customers already know.

Every row has a `verified` date and a source. Rows older than 90 days are stale until rechecked by [`skills/refresh`](../skills/refresh/SKILL.md). "Secondary" means no vendor page was checked.

## Approval and autonomy

| Harness | Mechanism | Maps to | Verified | Source |
|---|---|---|---|---|
| Claude Code | `plan`: research and propose; nothing changes until the plan is approved | Rung 0, propose | 2026-10-07 | [docs](https://code.claude.com/docs/en/permission-modes) |
| Claude Code | `default` (manual): reads run; everything else asks | Rung 1, draft | 2026-10-07 | [docs](https://code.claude.com/docs/en/permission-modes) |
| Claude Code | `acceptEdits`: file edits and common file commands run without asking | Rung 2 for edits | 2026-10-07 | [docs](https://code.claude.com/docs/en/permission-modes) |
| Claude Code | `auto`: actions run, and a separate model reviews each one and blocks anything beyond the request, aimed at unrecognized infrastructure, or driven by content the agent read | Rung 2, with a check in front | 2026-10-07 | [docs](https://code.claude.com/docs/en/permission-modes) |
| Claude Code | `dontAsk` and `bypassPermissions`: only pre-approved tools, or no prompts at all; bypass is documented for isolated environments only | Rung 3 | 2026-10-07 | [docs](https://code.claude.com/docs/en/permission-modes) |
| Claude Code | Deny rules hold in every mode, including bypass | A `never` enforced outside the model | 2026-10-07 | [docs](https://code.claude.com/docs/en/permission-modes) |
| Codex | Two layers: an approval policy (`untrusted`, `on-request`, `never`) and an OS sandbox (`read-only`, `workspace-write`, `danger-full-access`) | Rung and reach, set separately | 2026-10-07, secondary | [summary](https://codex.danielvaughan.com/2026/03/26/codex-cli-approval-modes-sandbox-security) |
| Cursor | Background agents work in cloud machines and deliver a pull request | Rung 1, draft, at the level of a whole change | 2026-10-07, secondary | [summary](https://www.morphllm.com/cursor-background-agents) |

What carries over: the best harnesses separate **how much the agent may do on its own** from **what it can reach**, and keep a short list of things denied in every mode. Your product's rungs should do the same.

## Undo

| Harness | Mechanism | Limit worth teaching | Verified | Source |
|---|---|---|---|---|
| Claude Code | A checkpoint before each edit; rewind restores code, conversation, or both | Does not undo shell side effects or changes made outside the tool. Not a replacement for version control | 2026-10-07 | [docs](https://code.claude.com/docs/en/checkpointing) |
| Cursor | Automatic checkpoints before agent edits, revertible in one click | Same class of limit: local edits, not external effects | 2026-10-07, secondary | [summary](https://www.morphllm.com/cursor-background-agents) |

What carries over: customers believe "undo" covers more than it does. Say which of your actions are reversible and which are not, in the product, at the moment it matters.

## Memory and instructions

| Mechanism | What it is | Verified | Source |
|---|---|---|---|
| Project instruction files (`AGENTS.md`, `CLAUDE.md`) | Plain files in a project that the agent reads every session. `AGENTS.md` is now stewarded by the Linux Foundation's Agentic AI Foundation | 2026-10-07, secondary | [report](https://thenewstack.io/anthropic-donates-the-mcp-protocol-to-the-agentic-ai-foundation/) |
| Assistant memory (Claude, ChatGPT) | Facts the assistant keeps across chats, increasingly as individual entries a person can view and edit | 2026-10-07, partly secondary | [ChatGPT release notes](https://help.openai.com/en/articles/6825453-chatgpt-release-notes) |

What carries over: customers now expect to see and edit what an agent believes about them. A product whose memory is invisible will be compared to ones where it is not.

## Skills

| Mechanism | What it is | Verified | Source |
|---|---|---|---|
| Agent Skills | Folders with a `SKILL.md` that teach an agent a procedure, loaded when relevant. An open format supported across most coding agents and several assistants | 2026-10-07, secondary | [report](https://www.unite.ai/anthropic-opens-agent-skills-standard-continuing-its-pattern-of-building-industry-infrastructure) |

What carries over: customers can increasingly hand an agent a written procedure. If your product accepts customer-written procedures, the class spec decides what a procedure may and may not override.
