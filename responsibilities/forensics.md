# Forensics

## Mandate

When the system does harm, or might have, this team can say what happened, how far it reached, and what changes before that [action class](../action-class.md) runs again.

## Delivered when

Any flagged action has a severity, an owner, and a reconstructed cause. The cause names the context it had, the spec it followed, the boundary checks it ran, and the build it was on. Target is under two minutes for the reconstruction, because the person asking is often on a call.

## The loop

1. Pull the action from the ledger and the trace. Reconstruct context, spec, checks, and build.
2. Grade severity by reach, not by how embarrassed the team is.

| Severity | Test | Response |
|---|---|---|
| 1 | Reached a third party, irreversible, materially wrong | Drop the capability to propose. Tell the customer the same day. |
| 2 | Reached a third party, reversible or minor; or lost the customer's own data or work for good | Drop to draft. A person contacts them. |
| 3 | Stayed inside the customer, and cost real work | A written review within two days. |
| 4 | Stayed inside, a person caught it, no cost | Add it to the sample set. |

3. Demote the rung when the severity says so. The change page owns the rung. This page owns the incident.
4. Feed the case into the sample set so the next build is graded against it.

Public cases, read this way, are in [`failures/`](../failures/README.md).

Sampling is stratified. Oversample new classes, the first week of a build, high-risk classes, new accounts, and unusual edit distance. A model may judge the volume. A person audits the judge on a fixed slice. When those two stop agreeing, the numbers are paused.

## Tools

### Capabilities required

- A trace store that can rebuild one action.
- A sampling queue.
- A severity log with an owner.

### Signals a scan can see

Langfuse, Langsmith, Braintrust, Arize, Helicone, or any OpenTelemetry backend. A review set or labeled dataset. Incident.io, PagerDuty, or a status channel. See [tools](../tools.md).

### If nothing is found

OpenTelemetry into a self-hosted trace store. The sampling queue is a view on the ledger. Severity is a field on the ledger row, announced in the incident channel the team already has.

## Cadence

- **Daily.** Open turns these into queue items: a first clean autonomous run worth telling the customer about, edit distance climbing, a champion who left, a severity 2 that needs a person. Cap the queue. A second inbox is a failed design.
- **Weekly.** Audit the judge on the fixed slice. Close or advance every open severity 1 and 2.
- **Quarterly.** Read severities next to rungs. A capability that keeps demoting is not ready to climb.

## Artifacts

- The forensic note: action id, context, spec, checks, build, what differed from a good run.
- The severity record and the customer message, if one was required.
- The sample set entry.

## Measures

Time to a cause. Agreement between the model judge and the person on the audited slice. Open severity 1 and 2 older than their response window. Deflection, if the team measures it, is pickup rate times end-to-end resolution. A bot reply that the customer reopens is not deflection.
