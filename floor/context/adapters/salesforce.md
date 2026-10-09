---
id: adapter-salesforce
type: adapter
status: active
confidence: low
last_reviewed: 2026-10-09
---

# Adapter: Salesforce (CRM)

Through a Salesforce MCP server or the REST API. The calls below name standard objects and fields. Orgs customize heavily, so confirm each field exists in this org the first time, and write the mapping down in `local/`.

## Reads

| Contract row | Source call | Notes |
|---|---|---|
| 1 Open commitments | Open Tasks related to the Account and its Contacts (`Status` not completed), with `OwnerId` and `ActivityDate` | Only what was logged. Check row 2 for promises made in email |
| 2 Unresolved issues, last 5 touches | Open Cases on the Account; the last five Tasks and Events, plus logged emails, ordered by date, newest first | Order explicitly in the query |
| 3 Identity | The Contact: `Name`, `Title`, and any time zone or language field the org added | Fall back to the thread when empty |
| 4 Relationship | The Account, its open Opportunities (`StageName`, `Amount`, `CloseDate`), and its Contract (`EndDate`) for renewal | Health is usually a custom field. Never quote it to the customer |
| 5 Product state | Not in Salesforce unless synced. Product analytics alongside | Synced fields lag. Say so if it matters |
| 6 Preferences | Notes on the Contact, and any custom field the team uses | |
| 7 Business context | The Account's `Industry` and `Description`, plus a fresh web check | Verify news before using it |
| 8 Desired outcome | A custom field or a note, if the team keeps one | If empty, ask once and write it back |
| 9 Delight history | Notes the team tags, plus a local ledger | |
| 10 Sensitive fields | Nudge first | Never pull billing or personal details without a grant |

## Writes

- The touch note as a completed Task (or a Note) on the Contact, related to the Account, in the contract's `touch` shape.
- A commitment as an open Task with an owner and `ActivityDate`.
- Outbound email as a draft only, unless the overlay grants send for that channel.

## Known gaps

- Field-level security can hide a field from the integration user. A missing value is not proof the value is empty.
- Person Accounts change the Account and Contact split. Check which model the org uses.
