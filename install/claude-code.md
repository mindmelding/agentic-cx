# Claude Code

```
git clone https://github.com/mindmelding/agentic-cx.git
cd agentic-cx
scripts/cx init
claude
```

`CLAUDE.md` imports `AGENTS.md`, so Claude knows what the repo is. The six skills are in `.claude/skills/`, each a short pointer to the real skill in `skills/` or `skill/`:

| Command | Runs |
|---|---|
| `/cx-setup` | [`skill/SKILL.md`](../skill/SKILL.md) |
| `/cx-open` | [`skills/open/SKILL.md`](../skills/open/SKILL.md) |
| `/cx-floor` | [`skills/floor/SKILL.md`](../skills/floor/SKILL.md) |
| `/cx-triage` | [`skills/triage/SKILL.md`](../skills/triage/SKILL.md) |
| `/cx-close` | [`skills/close/SKILL.md`](../skills/close/SKILL.md) |
| `/cx-refresh` | [`skills/refresh/SKILL.md`](../skills/refresh/SKILL.md) |

Start with `/cx-setup`.

## Working from another directory

If you spend your day in the product repo, keep this one beside it and add it to the session:

```
claude --add-dir ~/agentic-cx
```

Then name the skill by path: "Run `~/agentic-cx/skills/open/SKILL.md`."

## Connectors

```
claude mcp add --transport http <name> <server-url> --header "Authorization: Bearer $YOUR_KEY"
```

Check with `/mcp` inside a session. More in [context-layer.md](context-layer.md).

## Permissions

Setup asks before reading anything, but Claude Code will also prompt for file reads outside the repo, such as past transcripts under `~/.claude/projects/`. Approve them one at a time the first run. Do not run setup in a mode that skips permission prompts.

`.claude/settings.json` pre-approves the `cx` helper commands and denies reads of `.env` files. Scheduled runs get their own, narrower allow list from `cx run`.

## Check it worked

`scripts/cx doctor`. After `/cx-setup` it reports no failures: the private files exist, are gitignored, and `stack.md` and `local/assessment.md` are written.
