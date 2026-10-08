# Other hosts

Any agent that can read files in a folder can run this manual. The entry point is [`AGENTS.md`](../AGENTS.md). Most hosts read it on their own. For the rest, point the host's instructions file at it.

| Host | What to do |
|---|---|
| Gemini CLI | Open it in the repo. `GEMINI.md` tells it to read `AGENTS.md` |
| GitHub Copilot (agent mode) | Open the repo. Copilot reads `AGENTS.md`. If your version does not, add `.github/copilot-instructions.md` with one line: "Read AGENTS.md and follow it." |
| Windsurf | `.windsurf/rules/agentic-cx.md` with that same line |
| Cline | `.clinerules/agentic-cx.md` with that same line |
| Anything else | Put that line wherever the host takes standing instructions, and run it from the repo root |

Then say "Run the setup skill."

A host that speaks MCP can skip all of this and connect to the manual directly: [mcp.md](mcp.md).

## Why not install the skills on their own

Tools that install Agent Skills into a global folder copy each `SKILL.md` out of the repo. These skills link to the manual around them (the floor canon, the responsibility pages, the templates), and those links break once the file is moved. Work from the clone.

## Connectors

Every host that supports MCP takes the same three things: a name, the server URL, and an authorization header. Where each host keeps them is in [context-layer.md](context-layer.md).
