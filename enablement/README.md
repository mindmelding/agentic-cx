# Enablement

What this team teaches customers about supervising an agent. The customer bought software and got a new kind of colleague. Most of them have never managed delegated work from a machine: when to review, how to correct, when to let go, how to take it back. Nobody else is teaching them. That makes it this team's job, and one of the most useful things it can publish.

This folder changes faster than the rest of the manual, because the tools people learn supervision in change every month. It is split so the durable part stays still and the fast part is easy to refresh.

| File | What it holds | How fast it changes |
|---|---|---|
| [`supervising.md`](supervising.md) | Practices that hold whatever the model or harness: review, correct, delegate, promote, stop, take back | Slowly. Changed by decision |
| [`harnesses.md`](harnesses.md) | How the tools customers already use do approval, undo, memory, and skills today, and what each maps to on the rungs | Monthly. Every claim dated |
| [`vendor-guidance.md`](vendor-guidance.md) | What the model vendors themselves recommend for human oversight | When a vendor publishes |
| [`CHANGELOG.md`](CHANGELOG.md) | What changed in the two files above, and why | Every refresh |

## Why harnesses matter to a product that is not one

Your customers learn how to supervise agents in the tools they already use: a coding agent's permission modes, a chat assistant's memory, a browser agent's confirmation prompts. They arrive at your product with those words and those expectations. Borrow them. A rung explained as "like plan mode" lands faster than a rung explained from scratch.

The same files help in two other places. The team's own bench runs on these harnesses. And a customer's agent calling your product ([agent customers](../agent-customers.md)) behaves according to its harness's rules, not yours.

## How it stays current

- **Every harness claim carries a `verified` date and a source.** A claim with no source is removed. A claim older than 90 days is marked stale in the table until someone checks it.
- **Primary sources first.** Vendor documentation beats a blog. When only secondary sources exist, the row says so.
- **No model version names** in the durable files. Model names change quarterly and date the advice. Name a capability ("a separate model reviews each action before it runs"), not a release.
- **The refresh is a skill.** [`skills/refresh`](../skills/refresh/SKILL.md) runs monthly: re-verify each row in `harnesses.md`, check vendor guidance for anything new, propose changes to `supervising.md` only when a change in the tools changes the practice, and write the changelog.
- **Customer evidence outranks vendor advice.** When the ledger shows customers supervising differently from what this folder says works, the folder is wrong. Change it, and say so in the changelog.
