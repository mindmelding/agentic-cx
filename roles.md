# Roles

The functions a head of CX already knows, and what each becomes when the customer mostly meets the product through an agent. The [responsibilities](README.md#responsibilities) are the jobs. A role is a person, or part of one, holding some of them.

## From function to responsibility

| Function | What it was | What it becomes | Responsibilities |
|---|---|---|---|
| **Support** | Answer tickets. Measured on speed and CSAT. | The agent answers most of them. People hold the moments the agent should not hold alone, with the time the agent freed. Every edit a person makes to an agent draft is evidence. | [Floor](floor/README.md), [Voice](responsibilities/voice.md) |
| **Onboarding and implementation** | Kickoff, checklist, walkthrough calls. | Design the path the agent walks the user down. Catch the accounts it loses. Run a human kickoff only where one was sold. | [Onboarding](responsibilities/onboarding.md) |
| **Customer success** | Drive adoption and health, run QBRs, own the renewal. | Move named groups up the rungs on evidence, and tell the renewal story from the ledger. | [Change](responsibilities/change.md), [Value](responsibilities/value.md) |
| **Documentation and enablement** | Write the help center. Grow it. | Keep one spec per action class, a short promise page, and the check that production agrees. Take pages down when the product can say it. | [Documentation](responsibilities/documentation.md) |
| **Knowledge management** | Keep internal macros and articles current. | Keep the facts the agent acts on true, inside the product, per account. | [Context](responsibilities/context.md) |
| **Support operations and QA** | Sample tickets, grade agents, run tooling. | Reconstruct any action, grade harm by reach, sample by risk, audit the model judge. | [Forensics](responsibilities/forensics.md) |
| **Voice of the customer** | A quarterly deck of themes. | A daily queue: each flaw one item with a count, passed or held, already written in the tracker's shape. | [Voice](responsibilities/voice.md) |

## The role with no old name

**CX engineer.** Builds in the space between the customer and the product, without shipping product code. Writes the per-account context, the first-run script, the class specs and their `never` lines, and the eval cases taken from real failures. Runs the queries behind the [scorecard](metrics.md). The pattern elsewhere is the forward-deployed engineer. Here it reports to CX, because the material is the customer's world.

Hire one when the team spends more time asking product for a query, a config change, or a context fix than it spends with customers. Until then, one person on the team holds it part-time. What this role builds, and where it stops, is in [boundary](boundary.md).

## The floor, with freed time

Conventional support spends most of its hours on the transactional ninety-five percent. The agent takes most of that. The hours that come back are not a headcount saving first. They go to:

1. **The moments that need a person.** Our mistake, their bad day, an angry customer, a cancellation, a renewal, a silence. [`floor/README.md`](floor/README.md#who-holds-the-moment) says which moments a person holds and which the agent holds alone.
2. **Going first.** The stall list, the silence list, a first clean autonomous run worth telling the customer about. A person reaches out before the customer has to.
3. **The five percent.** The unreasonable gesture, grounded in one verifiable detail from the file. The agent can find the detail. A person decides it is worth doing.
4. **Teaching the agent.** Each edit to a draft, each correction to a fact, each new eval case. This is the work that frees the next hour.

A floor that spends its freed time answering what the agent could have answered has the wrong rung on that class. Move it.

## By team size

| Team | Who holds what |
|---|---|
| **One person** | Everything, on the [routines](routines.md). Open, triage, close, with the queue as the whole to-do list. Onboarding is the `stall` items. Value is one story per renewal. Forensics is the severity column on the ledger. Product holds the ledger and the rung mechanism. |
| **Three** | A head of CX who holds value, change, and the boundary with product. A floor lead who holds the floor, onboarding step-ins, and voice. A CX engineer who holds context, documentation, and forensics. |
| **Eight or more** | Split the floor by segment, not by tier. Onboarding gets an owner when stalls exceed what the floor can reach in a day. Documentation and forensics get owners when there are more classes than one person can keep verified each week. Each responsibility has one named owner, even when several people work it. |

At every size, each of the seven responsibilities has one name next to it. A responsibility everyone holds is held by no one.
