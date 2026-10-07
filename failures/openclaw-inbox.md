# OpenClaw inbox

**When.** Posted 23 February 2026. **Product.** OpenClaw, an open-source personal agent. **Confidence.** High on the event, medium on the count and the cause.

## What the agent did

A user asked it to sort her inbox and suggest what to delete or archive, and to confirm before acting. It started deleting older email in bulk. Stopping it from her phone did not work. She stopped it by killing the process. The likely cause, unconfirmed, is that the confirm-first instruction was dropped when the agent compacted its context on a large inbox. It had behaved correctly on a test inbox.

## Reach and severity

One user, hundreds of emails reported deleted. Recoverability unclear. Graded **2** if the loss was permanent, **3** if not.

## What the company did

Open source, so no vendor response.

## Read as forensics

- **Class:** two classes again. "Suggest" and "delete."
- **The `never`:** do not delete without confirmation. It lived in the conversation, and the conversation was summarized away.
- **Rung:** the user set propose. The product had no way to hold it there except the instruction.
- **Reversible, and who knew:** the stop control did not work remotely. A stop that does not stop is a boundary failure of its own.

## What the customer needed to hear

That the confirm-first setting is now enforced outside the conversation, and that stop works from every surface.

## Sources

- https://www.fastcompany.com/91497841/meta-superintelligence-lab-ai-safety-alignment-director-lost-control-of-agent-deleted-her-emails
- https://www.windowscentral.com/artificial-intelligence/meta-summer-yue-director-openclaw-ai-email-deletion
