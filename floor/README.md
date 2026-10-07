# Floor

The canon an agent loads before a reply. It moved here from [front-of-house](https://github.com/scmancillas/front-of-house). Paths named inside these files are relative to this directory.

Load, in order:

1. [`MINDSET.md`](MINDSET.md) and [`PRECEDENCE.md`](PRECEDENCE.md).
2. The customer's file, using [`context/CONTRACT.md`](context/CONTRACT.md). The moment is often in the file.
3. One playbook from [`moments/`](moments/README.md). A second only when the thread is clearly two moments. If nothing matches, [`small-moment`](moments/small-moment/PLAYBOOK.md).

Delight is a second decision, after the playbook, from [`delight/catalog.md`](delight/catalog.md). It needs one verifiable detail and a clear delight history.

A company overlay is not in this folder. Grants, learned phrases, and what was already sent stay in `local/` at the repo root. The day note in `local/learnings/days/` is the old inbox. Lessons do not come back into this canon.

Install adapters, evals, and the check script still live in the front-of-house repo until the packaging pass. Edit the canon here.
