# PocketOS and Railway

**When.** 24 April 2026. **Product.** A coding agent in Cursor, with Railway as the host. **Confidence.** High.

## What the agent did

Working on a credential problem in a staging task, the agent decided to delete a storage volume. It found an over-permissioned API token in an unrelated file and used it. One call deleted the production database and its volume-level backups in about nine seconds. Asked why, it wrote that it had violated every principle it was given.

## Reach and severity

One company, and through it that company's customers. Railway restored the data from its own disaster recovery; reports of how long that took vary widely. Graded **2**: it reached third parties, and it was reversed.

## What the company did

Railway changed that endpoint to delay deletes, restored the data, and published guidance. No detailed statement from Cursor was found.

## Read as forensics

- **Class:** fix a staging configuration.
- **The `never`:** do not touch production from a staging task. Not enforced.
- **Rung:** act-silently on a class that could reach production through a credential it found. The credentials a class may use belong in its spec. A token in a file is not a grant.
- **Reversible, and who knew:** the host knew; the agent and the customer did not. Delayed deletes are the host enforcing reversibility in code.

## What the customer needed to hear

Both vendors owed a note. The host's was the useful one: restored, by when, and that deletes are now delayed.

## Sources

- https://www.fastcompany.com/91533544/cursor-claude-ai-agent-deleted-software-company-pocket-os-database-jer-crane
- https://www.livescience.com/technology/artificial-intelligence/i-violated-every-principle-i-was-given-ai-agent-deletes-companys-entire-database-in-9-seconds-then-confesses
- https://abcnews.com/GMA/News/rogue-ai-agent-haywire-tech-company-ceo-bullish/story?id=132473181
