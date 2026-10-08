---
id: evals-run
type: eval
status: active
confidence: medium
last_reviewed: 2026-09-14
---

# Running the evals

Two layers. The first is deterministic and cheap. The second is a model judging against `rubric.md`. A reply must clear both.

## Layer 1: deterministic

`cx check` reads `voice/LEXICON.md` and scans a reply for banned phrases, banned words, banned openers, and structural patterns. Code blocks are stripped before scanning. It exits non-zero on any violation and prints each one with the offending text.

```
scripts/cx check reply.md
scripts/cx check - < reply.md
scripts/cx check --gold --templates
```

Run from the repo root. Banned phrases, words, openers, and patterns are errors. The "allowed, with care" limits (one exclamation point, one emoji, one apology) are warnings; `--strict` makes them errors. Each finding prints the file, line, column, the matched text, and the substitute from the lexicon's table when there is one.

CI (`.github/workflows/lexicon.yml`) runs it against every gold reply in `evals/cases/` and every example in `templates/customer/`. A gold reply that fails the lexicon is a bug in the case, not in the lexicon.

## Layer 2: LLM-as-judge

```
scripts/cx eval                          every case
scripts/cx eval 005 017 --judge codex    two cases, judged by a second harness
scripts/cx eval --dry-run                the cases and prompt sizes, no model called
```

Any harness in [`models.toml`](../../models.toml) can draft or judge, through its `pure` command: a prompt in, text out, no tools. The drafter runs at the `eval-draft` tier and the judge at `eval-judge`. Set `[eval] judge_harness` so the judge is a different family from the drafter; `cx eval` warns when they match. The judge prompt below is read from this file, so editing it here changes the run. Pass or fail is computed from the judge's scores against the rubric, not taken from its own `pass`. The exit code is 1 when any case fails.

For each case in `evals/cases/`, the harness:

1. Assembles the agent prompt: `MINDSET.md`, `PRECEDENCE.md`, the `guardrails/` files, `voice/VOICE.md`, `voice/LEXICON.md`, the one playbook under `moments/` matching the case's `moment`, and the case's context snapshot.
2. Sends the incoming message and captures the reply.
3. Runs Layer 1 on the reply. A violation triggers exactly one retry with the instruction "rewrite from the source," never "fix this draft." Paraphrasing a bad draft keeps its cadence. Regenerating from the snapshot does not.
4. Assembles the judge prompt (below) with the rubric, the case's must and must-not lists, the notes for the judge, the gold reply as calibration, and the reply under test.
5. Records the reply, the six dimension scores, any hard fail, and the judge's one-paragraph reasoning to `local/evals/<date>/<case-id>.json` in the house, outside git.

## Case file format

Every file in `evals/cases/` follows this shape:

```markdown
---
id: 005
moment: refund-or-credit
channel: email
difficulty: medium
hard_fail_traps: [acting-without-grant]
---

## Context snapshot
(a YAML block filled per the context contract rows, plus an `authority` block)

## Incoming message
(the customer's words, verbatim)

## Must
## Must not
## Gold reply
## Notes for the judge
```

The `authority` block is the only place standing grants exist for a case. If it is empty, every sensitive action requires a nudge.

## The retry rule

One retry, and only after a Layer 1 failure. The retry prompt is the original prompt with one added line: "Your previous draft used banned language. Do not edit it. Write a new reply from the context snapshot and the customer's message." If the retry also fails, the case fails.

## Human calibration

Once a month, a person scores a random sample of ten replies blind, using the same rubric. Compare to the judge's scores. If the judge and the human disagree by more than 3 points on more than two cases, the rubric anchors are ambiguous and get rewritten before anything else does.

## CI gate

On every pull request:

1. Layer 1 across all gold replies and template examples. Any failure blocks the merge. This step runs today.
2. Layer 2 across all cases, with `scripts/cx eval`. It needs model access, so it does not run in this repo's CI yet. The mean score and the pass count are compared to `main`. A drop in either blocks the merge unless the PR explicitly changes the rubric or a case, in which case a human approves.
3. Every case must reference a playbook that exists. Since the cut to fifteen cases, not every playbook has a case, so the reverse is not required.

## Judge prompt

```
You are scoring a customer-facing reply written by an agent that follows the Front of House canon.

You will receive: the rubric, a context snapshot (what the agent knew before replying), the customer's incoming message, a list of things the reply must do, a list of things it must not do, notes for the judge, a gold reply for calibration, and the reply under test.

Score the reply under test on each of the six rubric dimensions from 0 to 3. Before scoring, check every hard fail. If any hard fail applies, the total is 0 and you stop.

Rules:
- The gold reply is a calibration aid. A reply that takes a different approach can score higher than the gold.
- Judge only from the snapshot. If the reply states a fact not in the snapshot and not in the customer's message, treat it as unverified.
- "Must" items that are missing cost at least one point in the most relevant dimension. "Must not" items that appear cost at least two, or trigger a hard fail if listed as one.
- If the notes say a 5% move is not warranted, an unasked-for extra costs one point under Voice.
- Do not reward length. Do not reward warmth that is not attached to a specific fact or action.

Output JSON only:
{
  "hard_fail": null or "<which one>",
  "scores": {"answer_first": n, "specificity": n, "commitment": n, "voice": n, "effort": n, "honesty_safety": n},
  "total": n,
  "pass": true or false,
  "reasoning": "<one paragraph, name the specific lines that earned or lost points>"
}
```
