---
id: adapter-intercom
type: adapter
status: active
confidence: low
last_reviewed: 2026-10-09
---

# Adapter: Intercom (messenger and help desk)

Through Intercom's MCP server or its REST API. Intercom holds the conversation and some account data; pair it with the CRM's adapter where the CRM is the record. Map each row to the tool your host lists the first time, and write that down in `local/`.

## Reads

| Contract row | Source call | Notes |
|---|---|---|
| 1 Open commitments | Open and snoozed conversations and tickets where our last part promised something | No commitment field. Read the last admin reply |
| 2 Unresolved issues, last 5 touches | Open conversations and tickets for the contact and their company; the last five conversation parts across them, newest first | Include colleagues at the same company |
| 3 Identity | The contact: name, email, location and time zone, language | |
| 4 Relationship | The company: plan, size, custom attributes the team syncs | Usually partial. Use the CRM for renewal |
| 5 Product state | Contact and company custom attributes and events, if the product sends them | Often the best source here. Check how fresh the last event is |
| 6 Preferences | Notes on the contact, and past conversation ratings | |
| 7 Business context | The company record, plus a fresh web check | Verify news before using it |
| 8 Desired outcome | A custom attribute or a note, if the team keeps one | If empty, ask once and write it back as a note |
| 9 Delight history | A local ledger | |
| 10 Sensitive fields | Nudge first | |

## Writes

- The reply as a draft: an internal note holding the draft, or a reply only where the overlay grants send.
- The touch note as a note on the contact, in the contract's `touch` shape.

## Known gaps

- Fin or another bot may have answered first. Read the whole conversation, including bot parts, before replying.
- Leads and users are both contacts. Check the role before assuming a customer.
