# Boundary

Where this team stops and the builders start. In an agent product the line is blurred, because a lot of what shapes the customer's experience is configuration, context, and evaluation, not code. This team does build. It builds in a different place.

## The rule

> **CX builds what is per-customer and what is evidence. Product builds what is for every customer and what is enforcement.**

Two tests settle most cases:

1. **Does it change for one account, or for all of them?** One account: this team. All of them: product.
2. **Does it stop the system from doing something, or prove that it did not?** Stopping it is enforcement, and lives in code. Proving it is evidence, and lives here.

## Who holds what

| Thing | Builds it | Holds the decision | Why |
|---|---|---|---|
| The action ledger and the write to it | Product | CX defines dispositions and owns the queries | The ledger is infrastructure. What counts as accepted is a customer question. |
| An action class spec: fires when, may, never, approval | CX drafts. Product reviews | CX, with product sign-off on `never` | The spec is the promise. The person who tells the customer owns the wording. |
| Enforcing a `never` | Product, in code | Product | A promise kept by a prompt is not kept. |
| Checking a `never` held in production | CX | CX | Evidence. A broken one becomes a bug for product through [voice](responsibilities/voice.md). |
| The rung mechanism: flags, approval config | Product | — | The same mechanism serves every account. |
| Which account is on which rung | CX | CX, applied after the sponsor's yes | The renewal motion of this era. |
| Per-account context: facts, instructions, overlays | CX | CX | The customer's world, one account at a time. |
| The memory store and its citation log | Product | — | Every account uses it. |
| The first-run flow | Product | — | One flow, every account. |
| What the agent asks first, and the context floor per class | CX | CX | The onboarding script. See [onboarding](responsibilities/onboarding.md). |
| Eval cases from real failures | CX writes them | Product runs them in CI and owns the pass bar | CX sees the failure first. Product owns the build. |
| The docs renderer, the affected-path check, the assertion check | Product, or a CX engineer | CX owns the doc decision | Pipeline work. Whoever builds it, the decision stays here. |
| The trace store | Product | — | Infrastructure. |
| Severity by reach, and the customer message | CX | CX | Reach is measured at the customer. |
| Root cause and the code fix | Product | Product | The cause is in the build. CX reconstructs what happened; product says why. |
| A product flaw | — | CX passes or holds; product prioritizes | See [voice](responsibilities/voice.md). |
| The floor canon and the reply voice | CX | CX | How the company talks is a customer decision. |
| Inward tools: summaries, QA, deflection on the team's own queue | CX, or bought | CX | They serve the bench. See [tools](tools.md#inward-tools). |

## The seams

Work crosses the line in four places. Each crossing has a shape, so nothing gets lost in a hallway conversation.

| Crossing | From CX | What product gets |
|---|---|---|
| A flaw | A voice item marked pass | An issue in their tracker, already written, with a count. |
| A broken `never` | A failed assertion check | A severity 1 or 2 and a forensic note: action, context, spec, build. |
| A failure to learn from | An eval case | A case in the eval set, with the expected behavior and the account it came from, anonymized. |
| A spec change | An unverified spec after a commit | The doc decision, and any change to `may` or `never` that needs their sign-off. |

Product crosses back in one place: a commit that touches a class's `sources`. That flags the spec, and the decision comes back here.

## Smells

- **CX ships a product code path.** Even a small one. The next build owns it and nobody on product knows it exists.
- **Product writes per-account context.** It ends up in a config file nobody on the floor can read or correct.
- **A `never` exists only in a prompt.** Move it to code, or take it off the promise page.
- **A help article explains how to get the agent to do the right thing.** That is a flaw. Pass it.
- **Eval cases only come from engineers.** The set tests what the builders imagined, not what customers did.
- **Root cause from the CX side.** A guess about the model, written into a customer message. Say what happened. Leave why to the people who can see the build.

## When the line moves

A thing done per account three times is a candidate for product. The third account to need the same context fix, the same first-run tweak, or the same workaround means the product should do it for everyone. Pass it through voice with the three accounts as evidence. Once it ships, take the per-account version out.
