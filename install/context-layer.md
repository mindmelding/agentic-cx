# Connecting your tools

The manual reads your customer's file before anything else, and the setup skill maps your tools onto [`tools.md`](../tools.md). Both work through whatever your agent host has connected. Connect before you run setup, so setup can find them.

## What to connect

In order of value:

1. **Where the customer's file lives.** A CRM or account store, ideally one that keeps facts with a source and a date. This is the [context contract](../floor/context/CONTRACT.md).
2. **Where customers write in.** A support desk, a shared inbox, a Slack Connect workspace.
3. **Where product work is tracked.** Linear, Jira, or GitHub issues, so [voice](../responsibilities/voice.md) can file into it after a yes.
4. **Where the product's own record is.** Events, traces, or a database view of the agent's actions. This decides your [ledger level](../ledger.md).

Connect read access first. Setup asks before using any of it, and nothing writes to a connected tool without your yes.

## Where each host keeps connectors

| Host | Where | Shape |
|---|---|---|
| Claude Code | `claude mcp add --transport http <name> <url> --header "Authorization: Bearer $KEY"` | Check with `/mcp` |
| Codex | `~/.codex/config.toml` | `[mcp_servers.<name>]` with `url` and `bearer_token_env_var` |
| Cursor | `.cursor/mcp.json` or `~/.cursor/mcp.json` | `mcpServers.<name>` with `url` and `headers` |
| VS Code and Copilot agent mode | `.vscode/mcp.json` | `servers.<name>` with `type: "http"`, `url`, `headers` |
| Gemini CLI | `~/.gemini/settings.json` | `mcpServers.<name>` with `httpUrl` and `headers` |
| Windsurf, Cline, Goose, OpenCode | their MCP settings | The same URL and header |

Keep keys in environment variables, never in a file in this repo.

## A different CRM or context store

[`floor/context/adapters/TEMPLATE.md`](../floor/context/adapters/TEMPLATE.md) maps each row of the context contract to a call in your tool, and says what the agent may write back. [`moonbase.md`](../floor/context/adapters/moonbase.md) beside it is a worked example. Write yours in `local/`, not in the repo, unless it would help other companies.

## Nothing connected

Everything still runs. Setup interviews you instead of reading. The floor treats each customer as a first conversation and says so. The ledger runs at level 0 or 1, by hand. Facts collect in `context-inbox.md` until there is somewhere to put them.
