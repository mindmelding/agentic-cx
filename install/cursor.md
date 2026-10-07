# Cursor

Clone the repo and open the folder in Cursor:

```
git clone https://github.com/mindmelding/agentic-cx.git
cursor agentic-cx
```

Cursor's agent reads `AGENTS.md` at the root. In an Agent chat, say "Run the setup skill." Later: "start the day," "draft a reply to this," "wrap up."

To keep the manual beside your product code, add both folders to one workspace. The agent will find `AGENTS.md` in this one.

## Connectors

`.cursor/mcp.json` in this folder, or `~/.cursor/mcp.json` for every project:

```json
{
  "mcpServers": {
    "<name>": {
      "url": "<server-url>",
      "headers": { "Authorization": "Bearer ${env:YOUR_KEY}" }
    }
  }
}
```

A project-level `.cursor/mcp.json` with a key in it must not be committed. Use the environment variable form above. More in [context-layer.md](context-layer.md).

## Check it worked

After setup, `stack.md` and `local/assessment.md` exist and `git status` shows neither.
