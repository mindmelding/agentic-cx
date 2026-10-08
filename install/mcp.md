# Any host, over MCP

The manual can serve itself to any agent host that speaks the Model Context Protocol: Claude Code, Codex, Cursor, Gemini CLI, VS Code, and the agent your product runs. Every host gets the same skills, the same rules, and the same lexicon check, whatever model it runs.

## Three steps

```
git clone https://github.com/mindmelding/agentic-cx.git ~/.agentic-cx/manual
CX_HOUSE=~/.agentic-cx/house ~/.agentic-cx/manual/scripts/cx init
~/.agentic-cx/manual/scripts/cx mcp config claude --house ~/.agentic-cx/house
```

The last line prints the setup for your host. Run it, or paste it where it says. Swap `claude` for `codex`, `cursor`, `gemini`, `vscode`, or `json` (the plain `mcpServers` shape most other hosts take). Python 3.11 or newer, and nothing else.

Then, in the host: "Run the setup prompt from agentic-cx." Most hosts list the skills as prompts or slash commands.

## Two folders

| Folder | Holds | Updated by |
|---|---|---|
| The manual, `~/.agentic-cx/manual` above | This repo. Nothing about your company | `git pull` |
| The house, `CX_HOUSE` | `stack.md`, the two queues, and `local/` | The skills, and you |

Keeping them apart means an update never touches your notes, and your notes never sit in a git checkout. Moving to another machine is copying the house. A clone used the old way, with the house at the repo root, keeps working; `CX_HOUSE` is only for when you want them apart.

Set `CX_HOUSE` for every `cx` command too (`cx doctor`, `cx status`, `cx run`), or export it in your shell profile.

## What the host gets

| Kind | What |
|---|---|
| Prompts | The six skills: `setup`, `open`, `floor`, `triage`, `close`, `refresh`. Each comes with where the house is and how to follow its links |
| Resources | Every file of the manual, at `cx://manual/<path>` |
| `manual_read` | One file. A relative link resolves from the file it appears in, so a skill's links work as they do in a clone |
| `manual_search` | A phrase across the manual |
| `lexicon_check` | A draft reply against the house lexicon. Every customer-facing draft goes through it |
| `cx_status` | What is waiting, without customer quotes |
| `cx_doctor` | What is missing, and the next step |

## What it never does

It serves the manual and reads the house to summarize it. It never serves a private file, never writes anything, and never reads outside those two folders. The host reads and writes the private files with its own file tools, after the same yes as always (`local/consent.toml`). There are no keys in any of this.

## Scheduled runs

`cx run open` and `cx run close` start a host from the command line, and work the same with a separate house. See [running the day on a schedule](README.md#running-the-day-on-a-schedule).
