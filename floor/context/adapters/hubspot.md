---
id: adapter-hubspot
type: adapter
status: active
confidence: low
last_reviewed: 2026-10-09
---

# Adapter: HubSpot (CRM)

Through HubSpot's MCP server or its CRM API. The calls below name HubSpot objects, not tool names: tool names differ by server and version, so map each row to the tool your host lists the first time you run it, and write that down in `local/`.

## Reads

| Contract row | Source call | Notes |
|---|---|---|
| 1 Open commitments | Open tasks associated with the company and its contacts, with owner and due date | Only what someone logged as a task. Promises made in email and never logged are missing; check row 2 |
| 2 Unresolved issues, last 5 touches | Open tickets on the company; the last five engagements (emails, calls, meetings, notes) across its contacts, newest first | Sort by timestamp yourself. Do not assume the default order is newest |
| 3 Identity | The contact record: name, job title, time zone, language | Time zone and language are often empty. Fall back to the thread |
| 4 Relationship | The company record and its open deals: lifecycle stage, plan or amount, close or renewal date, owner | Health is a custom property if it exists at all. Never quote it to the customer |
| 5 Product state | Not in HubSpot unless synced. Product analytics alongside | A property synced from the product can be days stale. Say so if it matters |
| 6 Preferences | Notes on the contact, and any custom property the team uses for preferences | |
| 7 Business context | The company record's industry and description, plus a fresh web check | Verify news before using it |
| 8 Desired outcome | A custom property or a pinned note, if the team keeps one | If empty, ask once and write it back as a note |
| 9 Delight history | Notes tagged by the team, plus a local ledger | HubSpot has no field for this. Keep it local if nobody tags |
| 10 Sensitive fields | Nudge first | Never pull billing or personal details without a grant |

## Writes

- The touch note as a note engagement on the contact, associated with the company, in the contract's `touch` shape.
- A commitment as a task with an owner and a due date.
- Outbound email as a draft only, unless the overlay grants send for that channel.

## Known gaps

- Engagements logged by integrations can be duplicated. Dedupe by timestamp and subject before counting touches.
- A contact can sit under several companies. Use the one on the deal or the ticket in front of you.
