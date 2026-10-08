# Ledger, to start

Two ways in, matching the levels in [`ledger.md`](../../ledger.md).

**Level 4, native.** Hand [`ledger.sql`](ledger.sql) to product. It is the table in [value](../../responsibilities/value.md), with the five columns that cannot be skipped first.

**Level 1, sampled by hand.** Export what the agent did, as CSV, with at least `time`, `account`, `action_class`, and `ref`. Then:

```
scripts/cx ledger sample export.csv --per-account 20 > sheet.csv
# grade each row: disposition (accepted, edited, ignored, reversed, blocked) and a one-line why
scripts/cx ledger report sheet.csv
```

`sample` keeps the accounts you name with `--accounts`, takes up to the given number of rows from each at random (`--seed` makes it repeatable), and adds empty `disposition`, `why`, and `graded_by` columns. `report` gives acceptance per class with the sample size, labeled with the ledger level from `stack.md` (or `--level`), because a sample is never a census. Rows still ungraded are counted and left out of the rate.

The sheet holds customer records. Keep it in the house, never in git.
