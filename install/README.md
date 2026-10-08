# Install

This manual is a folder of Markdown that your agent reads. There is nothing to build. Installing it means putting the repo where your agent works and running the setup skill once.

```
git clone https://github.com/mindmelding/agentic-cx.git && cd agentic-cx
scripts/cx init      # the private files: local/, the overlay, the queues, consent
scripts/cx doctor    # what is set up, what is missing, the next step
```

Then open your agent in the repo and run setup. `cx` needs Python 3.11 or newer and nothing else.

## Three steps

**1. Get the repo.**

```
git clone https://github.com/mindmelding/agentic-cx.git
cd agentic-cx
```

Your company's material never lands in tracked files. The setup skill writes it to `stack.md`, `voice-queue.md`, `context-inbox.md`, and `local/`, which are gitignored. A public clone is fine. If you want your notes versioned, keep `local/` in a separate private repo.

Then `scripts/cx init`. It creates those files from the templates, with a `local/consent.toml` that allows nothing yet, and never overwrites one that exists.

**2. Open your agent in the repo.** Each host finds the manual through a file it already reads:

| Host | It reads | Then say | Page |
|---|---|---|---|
| Claude Code | `CLAUDE.md`, and the skills in `.claude/skills/` | `/cx-setup` | [claude-code.md](claude-code.md) |
| Codex | `AGENTS.md` | "Run the setup skill." | [codex.md](codex.md) |
| Cursor | `AGENTS.md` | "Run the setup skill." | [cursor.md](cursor.md) |
| Gemini CLI, Copilot, Windsurf, and others | `AGENTS.md`, `GEMINI.md`, or a rules file you point at `AGENTS.md` | "Run the setup skill." | [other-hosts.md](other-hosts.md) |

**3. Run setup.** It asks permission, reads past chats and connected tools, interviews you on the gaps, and leaves a gap report and a first loop. About twenty minutes. Step 7 configures the floor: who you escalate to, what the agent may spend, and your own replies as examples.

## Connect your tools

Setup works better with your customer data connected: the CRM or account store, the support desk or inbox, the tracker product uses. Connect them in your agent host first, so setup can find them. See [context-layer.md](context-layer.md).

## Two other ways to use it

- **Without an agent.** Read [`README.md`](../README.md) and the [self-check](../assessment/index.html). The manual is written for people first.
- **Inside your product's support agent.** The [`floor/`](../floor/README.md) canon can be loaded into the agent that replies to your customers. See [customer-agent.md](customer-agent.md).

## Running the day on a schedule

The skills are meant to be run by a person at the start and end of the day. Open and close can also run on their own, from a scheduler:

```
# Weekdays 8:45 and 17:45
45 8  * * 1-5  ~/agentic-cx/scripts/cx run open
45 17 * * 1-5  ~/agentic-cx/scripts/cx run close
```

`cx run` picks the first agent host on your PATH (or `--harness`, or `CX_HARNESS`), the model tier from [`models.toml`](../models.toml), and Friday's tier for Friday's close. It writes the output to `local/runs/` as well as printing it. `--dry-run` prints the command instead.

What a run may do comes from `local/consent.toml`, not from the prompt alone:

- Only open and close run unattended. Setup, floor, triage, and refresh wait on a person, and `cx run` refuses them.
- On Claude Code, the run may edit only `local/`, `voice-queue.md`, and `context-inbox.md`, and call only the connectors consent lists. Anything else is denied, because nobody is there to approve it.
- Other hosts cannot scope tools per run. Codex runs in its workspace sandbox. For the rest, the rules reach the agent through the prompt, and `cx run` says so.
- Nothing is sent and nothing is filed. What would need a yes is listed under "Waiting on you."

## Staying current

`git pull` picks up changes to the manual. Your `local/` folder is never touched. Once a month, run the [refresh](../skills/refresh/SKILL.md) skill to re-check the parts that track fast-moving tools.

## Moving to another machine or agent

Copy `local/`, `stack.md`, `voice-queue.md`, and `context-inbox.md` into a fresh clone. That is everything the manual knows about your company.
