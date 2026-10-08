# Codex

```
git clone https://github.com/mindmelding/agentic-cx.git
cd agentic-cx
codex
```

Codex reads `AGENTS.md` at the repo root, which lists the skills and the rules. Say "Run the setup skill." Later: "start the day," "draft a reply to this," "wrap up."

Use the default approval mode for setup. It reads files outside the repo (past sessions, connector config) and should ask each time.

## Connectors

Add MCP servers to `~/.codex/config.toml`:

```toml
[mcp_servers.<name>]
url = "<server-url>"
bearer_token_env_var = "YOUR_KEY"
```

More in [context-layer.md](context-layer.md).

## Check it worked

After setup, `stack.md` and `local/assessment.md` exist and `git status` shows neither.
