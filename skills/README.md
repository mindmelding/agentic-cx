# Skills

One queue, worked by [triage](triage/SKILL.md), defined in [`queue.md`](../queue.md). Plain Markdown. Any agent follows one by reading its `SKILL.md`.

| When | Skill | Stops when |
|---|---|---|
| Start of day | [Open](open/SKILL.md) | New things are items, what may run on its own is done, and the board is posted. |
| During the day | [Triage](triage/SKILL.md) | The queue is empty, the operator stops, or 25 items are done. Each one is logged. |
| When a customer pings | [Floor](floor/SKILL.md) | One moment is handled and logged, and any fact or flaw is in the queue. |
| End of day | [Close](close/SKILL.md) | The day note exists. On Friday, promotions, rules, and the autonomy report have been proposed. |
| Monthly | [Refresh](refresh/SKILL.md) | Every harness row is verified within 90 days, and the changelog says what moved. |

The schedule is [routines](../routines.md). Setup, once, is [skill/SKILL.md](../skill/SKILL.md).

The floor skill loads [`floor/`](../floor/README.md): mindset, precedence, and one moment playbook, after reading the customer's file. Lessons from those moments stay in `local/learnings/`, which is gitignored and is what you copy when you change agents. The shape of a learning is in [learnings](../learnings/README.md).
