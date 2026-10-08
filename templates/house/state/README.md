# State files

The three files the skills write at the root of a clone, and the shape each keeps. Agents write them, people read them, and `scripts/cx status` and `scripts/cx doctor` parse them. All three are gitignored.

| File | Written by | Created by |
|---|---|---|
| [`stack.md`](stack.md) | Setup, step 5 | Setup. Its absence means setup has not run |
| [`voice-queue.md`](voice-queue.md) | Open, floor, triage | `scripts/cx init` |
| [`context-inbox.md`](context-inbox.md) | Open, floor | `scripts/cx init` |

Rules that hold across all three:

- Front matter between `---` lines is `key: value`, one per line.
- A table keeps its header row exactly as the template has it. Add rows; do not add, drop, or rename columns.
- One row per line. A `|` inside a cell is written `\|`.
- Dates are `YYYY-MM-DD`. A time is ISO 8601 with its offset: `2026-10-08T08:45:00-07:00`.
- Prose is fine anywhere else in the file. The parser reads only the front matter, the tables, and the capability lines.

`scripts/cx doctor` names any line it cannot read, with its line number.
