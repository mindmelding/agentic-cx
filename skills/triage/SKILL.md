---
name: cx-triage
description: Decide pass or hold on each voice item, and no-page, promise-line, or guide on a flagged spec. File only after an explicit yes. Use after intake, or when a commit has marked a spec unverified.
---

# Triage

Read [`responsibilities/voice.md`](../../responsibilities/voice.md) and [`responsibilities/documentation.md`](../../responsibilities/documentation.md). Use the adapter in `stack.md` when a pass is accepted. One item at a time.

## Voice

For each open row in `voice-queue.md`:

1. Show the flaw, the quote, the count, the resolution, and whether an issue already exists.
2. Ask: pass, or hold.
3. On hold, write the reason on the row. Leave it in the queue.
4. On pass, show the issue in the voice page's shape. File it only after the person says yes. If an issue already covers it, comment with the new quote and the new count instead of opening another.
5. Mark the row passed, with the link.

A flaw that has never been passed does not get filed on its own. New evidence on a flaw already passed can be added, and the person is told.

## Documentation

When a spec is unverified because a commit touched its `sources`:

1. Show the diff beside the current `may` and `never`.
2. Ask for one disposition: no page, because the product reveals the behavior; a line on the promise page; or a guide, because a person still has to walk a sequence before the product can.
3. Apply the disposition only after a yes. A change to a `never` line always waits for that yes.

## Then

If the decision would surprise someone who was not here, say so and tell them to run the learn skill before stopping.
