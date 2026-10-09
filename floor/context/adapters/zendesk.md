---
id: adapter-zendesk
type: adapter
status: active
confidence: low
last_reviewed: 2026-10-09
---

# Adapter: Zendesk (help desk)

Through a Zendesk MCP server or the Support API. A help desk answers rows 2 and 3 well and little else, so pair it with the CRM's adapter for the rest. Map each row to the tool your host lists the first time, and write that down in `local/`.

## Reads

| Contract row | Source call | Notes |
|---|---|---|
| 1 Open commitments | Open and pending tickets where the last public comment is ours and promised something | Zendesk has no commitment field. Read the last agent comment on each open ticket |
| 2 Unresolved issues, last 5 touches | Tickets for the requester and their organization, not solved or closed; the last five public comments across them, newest first | Include tickets from colleagues at the same organization |
| 3 Identity | The user: name, time zone, locale; the organization | |
| 4 Relationship | The organization's fields and tags, if the team syncs plan or tier there | Usually partial. Use the CRM |
| 5 Product state | Not here. Product analytics alongside | |
| 6 Preferences | User and organization notes; past satisfaction ratings and their comments | A bad rating is a past bad experience. Read its comment |
| 7 Business context | Not here. The CRM and a web check | |
| 8 Desired outcome | Not here, unless a field holds it. The CRM, or ask once | |
| 9 Delight history | A local ledger | |
| 10 Sensitive fields | Nudge first | Ticket attachments and custom fields can hold personal data. Do not open them without a grant |

## Writes

- The reply as a draft: a private note holding the draft, or a public reply only where the overlay grants send.
- The touch note as an internal note on the ticket, in the contract's `touch` shape.
- Tags the team already uses. Do not invent tags.

## Known gaps

- Merged tickets keep their comments on the surviving ticket only. Follow the merge before saying "no history."
- Side conversations and voice calls may not appear in the comment list.
