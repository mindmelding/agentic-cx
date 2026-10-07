# Skills

Four skills. Plain Markdown. Any agent follows one by reading its `SKILL.md`.

| When | Skill | Stops when |
|---|---|---|
| Start of day | [Open](open/SKILL.md) | The board is posted. Nothing is filed. |
| During the day | [Floor](floor/SKILL.md) | One customer moment is handled, and any fact or flaw from it is written down. |
| During the day | [Triage](triage/SKILL.md) | The waiting item is passed, held, or given a doc disposition. |
| End of day | [Close](close/SKILL.md) | The day note exists. Friday's close has promoted or discarded the week. |

The schedule is [routines](../routines.md). Setup, once, is [skill/SKILL.md](../skill/SKILL.md).

The floor skill loads [`floor/`](../floor/README.md): mindset, precedence, and one moment playbook, after reading the customer's file. Lessons from those moments stay in `local/learnings/`, which is gitignored and is what you copy when you change agents. The shape of a learning is in [learnings](../learnings/README.md).
