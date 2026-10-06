# Skills

Four skills run the manual. They are plain Markdown. Any agent can follow one by reading its `SKILL.md`. Nothing here depends on a particular harness.

Point the agent at one file. Do not load all four unless a routine says so.

| Skill | When | Stops when |
|---|---|---|
| [intake](intake/SKILL.md) | New mail, a resolution, or a flaw from the day's work | Facts and flaws are written down. Nothing is filed. |
| [triage](triage/SKILL.md) | After intake, or when a commit flags a spec | Each item is passed, held, or sent back to context. |
| [learn](learn/SKILL.md) | A decision a new teammate would not guess | One file exists under [learnings](../learnings/README.md) and the index has a row. |
| [check](check/SKILL.md) | Once a week | A list of at most five things. Then stop. |

The schedule is [routines](../routines.md). The first-time setup, which maps tools, stays at [skill/SKILL.md](../skill/SKILL.md).

Learnings live in the repo as files, not in the agent's memory. Copy the `learnings/` folder and these skills onto another machine, or another harness, and the record comes with them.
