# Onboarding

## Mandate

Get a new account, and each new group inside it, from signup to a first accepted action and then to the outcome they came for. In an agent product the user usually drives this. They start talking to the agent before anyone on this team has met them. The team designs the path the agent walks them down, and catches the ones it loses.

## Delivered when

Every account in its first window has a desired outcome in its own words, the context the first [action class](../action-class.md) needs, a starting rung, and a first action a person accepted. An account that stalled has been reached by a person, or someone decided not to and wrote down why.

## What is different now

Conventional onboarding is a kickoff, a checklist, and a series of calls. The customer success manager walks the customer through the product. In an agent product, the agent is the walkthrough. Most users never ask for a call. Some never see a setup screen.

That moves the work in three ways:

- **The path is a conversation, not a checklist.** What the agent asks first, which context it asks for, and what it offers to do before anything is connected are onboarding decisions. This team writes them. Product builds the flow.
- **Onboarding repeats.** An account is onboarded once. Each new group inside it onboards itself, often without telling anyone. A team that joins in month eight is on day one.
- **Human time goes to the stall.** The agent handles the ones that go well. A person steps in when the record says it is going badly, or when the account is large enough that a person was promised at the sale.

## The loop

1. **Ask the outcome.** On first run the agent asks what the user wants to be true in thirty days, and writes the answer as a fact in [context](context.md), in their words, with a target date.
2. **Seed the context floor.** Each action class names the minimum facts and connections it needs before a first action is worth trying. The agent asks for those and no more. A missing connection is asked for once, with the reason.
3. **Earn a first accepted action.** The class starts at rung 0 or 1, as its spec says. The first instance a person accepts is the activation event. Record it on the ledger.
4. **Watch for stalls.** A stall is a signal on the record, not a feeling:
   - No action in seven days after signup.
   - The first three instances reversed or ignored.
   - Edit distance not falling across the first ten.
   - The user asked the agent how to do something the agent should have done.
   - The context floor still incomplete after three days.
5. **Step in.** A stall opens the [`onboarding-first-100-days`](../floor/moments/onboarding-first-100-days/PLAYBOOK.md) moment for a person on the [floor](../floor/README.md). The person reads the file, does the next step for them if they can, and names a who and a when.
6. **Graduate.** The account leaves onboarding when it reaches the stated outcome, or when one class has a record strong enough to propose the next rung. Then it belongs to [change](change.md).
7. **Fix the path.** A stall that repeats across accounts is a flaw in the path. It goes to [voice](voice.md) if product has to change the flow, or to the first-run script if this team can.

## The outcome, in their words

Ask once, on day 0: "What do you want to be true in thirty days that isn't true now?" "The Wednesday report goes out without me touching it" is an outcome. "Get set up" is not. If the answer is vague, ask what they would show their boss. Write it down verbatim with a target date. Every later step is measured against it, and a customer who reaches it without anyone knowing what it was reached it by accident.

What shortens the road to it: do the first step for them before they log in, one next action per message, the first question answered within the hour, and the milestone named when they hit it, so they know it counted. Remove every step that exists for our convenience.

Check-ins do a piece of the work or are not sent. Day 7: "Data source connected, first run went through, 1,204 rows. It's scheduled for Wednesday 7am your time. I'll check it lands." Day 30: "Four Wednesdays, four reports, zero touches. Anything you'd change?"

## A sales-led kickoff

Some accounts were promised a person. The kickoff is a meeting with one purpose, named in the invite: "Agree what done looks like by October 14, and who does what." Invite the people who own the outcome, and say why each is there. Open by reading back the desired outcome and asking whether it is still right, and what would make it a failure. Touch the product only after that, and only the part that serves the goal. Close with every open item read aloud with a name and a date. Send the same list within the hour.

The agent prepares the file and drafts the follow-up. The person runs the room.

## Who holds what

| Part | Holder |
|---|---|
| The first-run flow and the activation events | Product builds them. |
| What the agent asks first, and the context floor per class | This team writes them, as part of the class spec. |
| The stall signals and the stall list | This team defines them. The list is a view on the ledger. |
| The human step-in | A person on the floor. |
| Sales-led kickoffs | A person, as below. The agent prepares the file. |

The line is drawn in full in [boundary](../boundary.md).

## Tools

### Capabilities required

- A first-run path where the agent asks the outcome and the context floor.
- Activation events on the ledger: signup, context floor met, first action, first accepted action.
- A stall list: accounts and groups in their first window that tripped a signal.
- A desired-outcome field in the memory store.

### Signals a scan can see

An onboarding or setup flow in the product. Events named `signup`, `activated`, `onboarded`, `first_*`. A product analytics tool with an activation funnel. Customer.io, Intercom, or another lifecycle tool sending onboarding messages. See [tools](../tools.md).

### If nothing is found

A first-run prompt in the agent that asks the outcome before it asks for anything else. Activation events as rows on the ledger, with no separate funnel tool. The stall list is a saved query. The step-in happens in the channel the account already uses.

## Cadence

- **Daily.** Read the stall list. Every stalled account gets a person or a written skip.
- **Weekly.** Read the stalls that repeated. One change to the first-run script, or one voice item.
- **Quarterly.** Time to first accepted action, by segment and by class. The self-onboarded share, and whether it moved.

## Artifacts

- The first-run script: what the agent asks, in order, and what it offers to do before anything is connected.
- The context floor, one list per class, kept in the class spec.
- The stall list.
- The graduation note: outcome reached or not, first class and its rung, handed to change.

## Measures

**Time to first accepted action.** From signup to the first instance a person accepted. This replaces time to first login and setup complete.

**Outcome reached in window.** Share of new accounts that reached their stated outcome within thirty days, unless the company sets another window. An account with no stated outcome counts as not reached.

**Self-onboarded share.** Share of accounts that graduated with no human step-in. It should rise. A high share with a low outcome rate means the agent is leaving people alone, not helping them.

**Stall recovery.** Of the accounts that stalled, the share that graduated after a person stepped in.
