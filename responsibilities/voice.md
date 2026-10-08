# Voice

## Mandate

The team owns the path from a product flaw to a decision. Mail, a resolution, and a flaw found while doing the job all arrive as one kind of item. A person passes it to the team that builds the product, or holds it. What gets passed is already written so it can be filed without a rewrite.

A fact about the customer is [context](context.md), not voice. The read happens once. "They export a CSV because the file fails" is context for that account. The failure itself is voice.

## Delivered when

Every flaw from those sources is one item, with a count and a quote. A person has marked it pass or hold. A pass is an issue in the tracker the product team uses, or a comment on the issue that already covers it. A hold stays in the queue with the resolution attached.

## The loop

1. Read what is new since the last pass. Customer mail, a resolution or workaround, and a flaw someone on this team hit while doing the work.
2. Keep the facts about the customer on the context path. Keep the product flaw here.
3. Match the flaw to an open item. The same flaw adds a quote and increments the count. It does not open a second item.
4. Draft the issue in the shape below. Do not create it yet.
5. A person marks pass or hold. Pass creates the issue, or comments on the open one. Hold keeps the item.

The first weeks, a person confirms every pass. Once the same flaw has been passed without edits, new evidence can be added to that issue and the person is told. A flaw that has never been passed still waits.

## Tools

### Capabilities required

- An intake of mail, resolutions, and findings, with a cursor so each pass reads only what is new.
- A way to cluster repeats into one item.
- A queue of items waiting for pass or hold.
- An adapter that files the digest into the tracker the product team already uses.

### Signals a scan can see

A mailbox, a help desk, or an account stream such as Moonbase. An issue tracker: Linear, Jira, GitHub issues. See [tools](../tools.md).

### If nothing is found

Read the mailbox the team already answers, from a saved cursor. Cluster in the queue itself. File into [Linear](https://linear.app) when product work has no tracker yet. If product work already lives in GitHub issues or Jira, that tracker is the adapter and Linear is not added beside it.

## Cadence

- **Daily.** Clear what the last pass added. Pass or hold each new item.
- **Weekly.** Reread the holds. A workaround that is still in use is the reason the item is still there.
- **Quarterly.** Of the items passed, how many shipped. Of the holds, which keep showing up.

## Artifacts

The item:

| Field | What it holds |
|---|---|
| Flaw | The product problem in one line. |
| Quote | The customer's words, short. |
| Account | Who hit it, and when. |
| Resolution | What CX already did, including a workaround. |
| Count | How many times this flaw has shown up. |
| Evidence | Links to the message, the call, or the session. |
| Proposal | Pass, or hold. |
| State | Open until a person decides. Then held, with the reason, or passed, with the link. |

The issue, filed only on pass:

```markdown
## What happened
One paragraph. The flaw, in the customer's situation.

## Evidence
Quote, account, date, link.

## Already tried
The resolution or workaround.

## Ask
The product change, one sentence.

Seen 4 times.
```

The queue is local. It is not part of this manual. The skill writes it beside `stack.md`, and both stay uncommitted.

## Measures

Time from first sight of a flaw to a pass or a hold. Share of passes that matched an issue already open. Share of filed issues the product team accepted without a rewrite.
