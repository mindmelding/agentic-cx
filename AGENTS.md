# Agentic CX: instructions for agents

You are working inside an operating manual for the customer team at a company whose product is an agent. The person you work for runs CX there, or is setting it up. This file tells you how to use the repo. The manual itself starts at [`README.md`](README.md).

## First run

If `stack.md` does not exist at the repo root, the operator has not been set up. Offer to run the setup skill: [`skill/SKILL.md`](skill/SKILL.md). It asks permission before it reads anything, interviews the operator, scores where the team stands, and writes `stack.md` and `local/assessment.md`.

## The skills

Each is a Markdown file. Read it and follow it when the operator asks for it by name or describes it.

| Ask | Skill |
|---|---|
| "Set me up", "where do we stand", "what are we missing" | [`skill/SKILL.md`](skill/SKILL.md) |
| "Start the day", "what's new" | [`skills/open/SKILL.md`](skills/open/SKILL.md) |
| A customer is waiting, or "draft a reply to…" | [`skills/floor/SKILL.md`](skills/floor/SKILL.md) |
| A pass, hold, or documentation decision is waiting | [`skills/triage/SKILL.md`](skills/triage/SKILL.md) |
| "Wrap up", "end of day" | [`skills/close/SKILL.md`](skills/close/SKILL.md) |
| "Refresh the harness tables", monthly | [`skills/refresh/SKILL.md`](skills/refresh/SKILL.md) |

Paths inside the skills are relative to the skill file. Resolve them from the repo, not from wherever you were invoked.

## Rules

- **Customer data never enters git.** Write company and customer material only to `stack.md`, `voice-queue.md`, `context-inbox.md`, and `local/`. All four are gitignored. Never commit them, and never copy a customer's words into a tracked file.
- **Ask before you look.** Before reading past chats, connector data, a product repo, or any customer record, say what you want to read and wait for a yes. Never read secret values.
- **Sensitive actions wait for a yes.** Money, personal data, account access, deletion, and anything sent outside the company. See [`floor/guardrails/authority.md`](floor/guardrails/authority.md).
- **Everything customer-facing is a draft** until the overlay in `local/overlay/` grants otherwise.
- **The manual stays vendor-neutral.** Map tools to this company in `stack.md`. Do not edit `responsibilities/` to name their products.
- **Editing the manual itself** follows [`CONTRIBUTING.md`](CONTRIBUTING.md). Only when the operator asks.
