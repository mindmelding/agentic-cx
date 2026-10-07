# Inside your product's support agent

The [`floor/`](../floor/README.md) canon is written so the agent that replies to your customers can load it. This page is for the engineer wiring it in. There is no generated bundle yet. You load the files.

## What to load

Always, in this order:

1. [`floor/MINDSET.md`](../floor/MINDSET.md) and [`floor/PRECEDENCE.md`](../floor/PRECEDENCE.md)
2. [`floor/guardrails/`](../floor/guardrails/never.md): `never.md`, `authority.md`, `escalation.md`, `privacy.md`
3. [`floor/voice/VOICE.md`](../floor/voice/VOICE.md) and [`floor/voice/LEXICON.md`](../floor/voice/LEXICON.md)
4. Your company overlay: the filled-in files from [`templates/house/overlay/`](../templates/house/overlay/README.md)

About 3,500 words before the overlay. Then, per conversation:

5. The customer's file, as the rows in [`floor/context/CONTRACT.md`](../floor/context/CONTRACT.md), from a tool call
6. One playbook from [`floor/moments/`](../floor/moments/README.md), chosen from the file and the message. Load the frontmatter of all playbooks up front and the body of one on demand. That is what the Agent Skills format is for.

Load [`floor/principles.md`](../floor/principles.md) too if the context budget allows. The playbooks cite it.

## What to wire

- **Who holds the moment.** The table in [`floor/README.md`](../floor/README.md#who-holds-the-moment) is the default. Moments a person holds go to a person, with the agent's draft attached, through your handoff path.
- **The authority gate.** Anything sensitive stops and asks the operator. Enforce the standing grants in code, not only in the prompt. The [failures](../failures/README.md) are what happens otherwise.
- **The write-back.** After each substantive reply, post the touch note from the contract to your context store.
- **The ledger row.** Record the moment slug and `held_by` beside the action class. See [`ledger.md`](../ledger.md).
- **The lexicon.** Check each draft against the banned lists in `LEXICON.md` before it sends.

## How to test it

The fifteen cases in [`floor/evals/cases/`](../floor/evals/cases/) each give a customer file, a message, and a gold reply. Feed the first two, compare against the third with [`floor/evals/rubric.md`](../floor/evals/rubric.md). Use a judge model from a different family than the one drafting.
