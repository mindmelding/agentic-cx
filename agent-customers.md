# Agent customers

More of the requests your product receives come from a customer's agent, not from a person: a coding agent reading your docs, an assistant calling your API through a connector, another company's agent negotiating with yours. The customer is still a person or a company. The thing in front of you is their delegate.

This page is how each responsibility changes when that happens. The standards named below move fast. Their status is re-checked monthly by [`skills/refresh`](skills/refresh/SKILL.md).

## Who is on the other end

Every request from an agent has a **principal**: the person or company it acts for. The ledger records both.

- `actor`: the agent, with whatever identity it presented.
- `principal`: the person or account it acts for.
- `principal_rung`: what the principal has allowed that agent to do in your product.

A disposition can now come from an agent: a customer's agent accepts, edits, or retries your agent's output. Record which. An acceptance by an agent is weaker evidence than an acceptance by a person. Promotions use person dispositions unless the principal has said otherwise.

## By responsibility

- **Onboarding.** The first reader of your docs may be an agent setting up the integration for a person. The context floor has to be reachable by it: a machine-readable spec, a connector, a clear first call. Stall signals include an agent retrying the same failing call.
- **Context.** The customer's agent arrives with its own memory and instructions. Facts it passes you are evidence, not truth. Record where a fact came from.
- **Change.** Rungs apply to agents too. A customer may let a person's actions run silently and require their agent's to be confirmed. Store the rung per principal and per actor type.
- **Value.** Work done through the customer's agent is still delegated work. Count it, labeled.
- **Documentation.** The **machine spec** form in [documentation](responsibilities/documentation.md) becomes the primary reader. Write the spec so an agent can act on it without a person.
- **Forensics.** Prompt injection arrives through what agents send you. Reconstruct which content the action read, and whose agent supplied it.
- **Voice.** An agent that keeps failing on the same call is a flaw report nobody wrote. Count it like one.
- **Floor.** Some tickets will be filed by agents. Reply to the person they act for, in the channel the person uses, unless the principal has said the agent may handle it.

## Errors written for agents

An agent cannot ask a follow-up question the way a person can. Every error your product returns should say:

1. What failed, in one sentence.
2. Whether retrying is safe, and when.
3. What would make it succeed: a missing field, a permission, a person's approval.
4. A stable code the agent can match on.
5. Where a person can see the same error, so the principal is not surprised.

An error that only makes sense to a person ("Something went wrong, please contact support") produces retries, and retries produce load and duplicate actions.

## Surfaces and standards

| Surface | What it is for | Status | Verified |
|---|---|---|---|
| MCP (Model Context Protocol) | Exposing your product's tools and data to any agent that speaks it. Now stewarded by the Linux Foundation's Agentic AI Foundation | Widely adopted. The 2026-07-28 spec moves client registration to client ID metadata documents | 2026-10-07 ([spec](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization/client-registration)) |
| A2A (Agent2Agent) | One agent delegating a task to another, across companies | Linux Foundation project, in major clouds; v1.0 added signed agent cards (secondary) | 2026-10-07 ([LF](https://www.linuxfoundation.org/press/a2a-protocol-surpasses-150-organizations-lands-in-major-cloud-platforms-and-sees-enterprise-production-use-in-first-year)) |
| `AGENTS.md` | Instructions for coding agents working in a repository | Stewarded by the Agentic AI Foundation | 2026-10-07, secondary |
| `llms.txt` | A docs index for language models | Partly adopted. No evidence search engines use it. May help coding agents find docs | 2026-10-07, secondary |
| Web Bot Auth | Agents sign their HTTP requests so a site can tell which agent is calling | IETF working-group draft, not yet a standard. Cloudflare runs a signed-agents program on it | 2026-10-07 ([Cloudflare](https://blog.cloudflare.com/signed-agents/)) |
| Agent payments (ACP, AP2, card-network agent tokens) | An agent paying on a person's behalf, with a record of what the person authorized | Several competing protocols. Status changes often; verify before building on one | 2026-10-07, secondary |

Use what your customers' agents already speak. Do not pick a standard for its press coverage.

## Measures

- Share of actions where the actor was a customer's agent, by class.
- Error recovery: share of agent calls that failed and then succeeded without a person.
- Repeated failures per agent per day. A rising number is a voice item.
