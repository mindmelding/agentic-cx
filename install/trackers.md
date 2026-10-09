# Filing into your tracker

[Voice](../responsibilities/voice.md) files one issue per flaw, and only after a person says pass. The issue has one shape whatever the tracker. This page is where that shape lands in the three trackers most teams use. Connect the tracker in your host first ([context-layer.md](context-layer.md)), then name it under Voice in `stack.md`.

| Part of the issue | Linear | Jira | GitHub issues |
|---|---|---|---|
| Title: the flaw, one line | Title | Summary | Title |
| What happened, Evidence, Already tried, Ask | Description, Markdown | Description | Body, Markdown |
| Seen N times | The last line of the description, updated on each repeat | Same | Same |
| Where it goes | The team that owns the product area | The project that owns it, issue type Bug or Story as product prefers | The product repo |
| Marked as from CX | A label the product team agrees to, such as `from-cx` | A label or component | A label |

## Before filing

Search the tracker for an open issue with the same flaw. If one exists, do not open a second: add a comment with the new quote, the account, and the new count, and set the voice queue row to `passed: <that issue's link>`. Triage does this already; this table only says where the words go.

## What never goes in

- A customer's name or email when the tracker is visible outside the company, such as a public GitHub repo. Write the account the way the product team's privacy rule allows, or link to the record instead.
- Anything from `local/`. The issue is written fresh from the queue row.

The tool calls differ by host and server. Map them the first time triage files, and keep the mapping in `local/`.
