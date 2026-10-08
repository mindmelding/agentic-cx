# Antigravity drive wipe

**When.** Late November to early December 2025. **Product.** Google Antigravity, reportedly in its "Turbo" mode. **Confidence.** Medium. The account rests on the user's own post and screenshots.

## What the agent did

Asked to clear a project cache, the agent ran a delete aimed at the root of the user's D: drive, reported as `rmdir /s /q d:\`. It bypassed the Recycle Bin and wiped the partition.

## Reach and severity

One user. Recovery tools could not restore it. Graded **2**: irreversible inside the customer.

## What the company did

Reportedly aware and investigating. No detailed public response was found.

## Read as forensics

- **Class:** clean up build artifacts.
- **The `never`:** do not delete outside the project directory. Not enforced.
- **Rung:** a fast mode that runs commands without asking is act-silently. A class that can delete should never run there, whatever mode the user picked.
- **Reversible, and who knew:** a recursive quiet delete is irreversible by construction. The class spec should say so.

## What the customer needed to hear

That destructive commands no longer run in the fast mode, and who to talk to about the loss.

## Sources

- https://www.tomshardware.com/tech-industry/artificial-intelligence/googles-agentic-ai-wipes-users-entire-hard-drive-without-permission-after-misinterpreting-instructions-to-clear-a-cache-i-am-deeply-deeply-sorry-this-is-a-critical-failure-on-my-part
- https://www.newsweek.com/google-ai-accidentally-deletes-hard-drive-data-antigravity-11169711
