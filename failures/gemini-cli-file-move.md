# Gemini CLI file move

**When.** July 2025. **Product.** Google Gemini CLI. **Confidence.** High on the event, medium on the wording of Google's statement.

## What the agent did

A user asked it to move project files into a new folder. Creating the folder failed silently. The agent carried on, and each "move" overwrote the file before it, until one file was left. It then told the user it had failed completely and catastrophically.

## Reach and severity

One user's local files, not recovered. It stayed inside the customer, but the loss was permanent. Graded here as a **2**: irreversible loss inside the customer is not minor, even with no third party.

## What the company did

A spokesperson pointed to the CLI's permission prompts, sandboxing, and checkpointing, and said users should review the commands the agent proposes.

## Read as forensics

- **Class:** reorganize files.
- **The `never`:** do not overwrite a file that exists. Nothing enforced it.
- **Rung:** the user approved the commands, so the class was at draft. A draft whose consequences the reviewer cannot see is not a meaningful approval.
- **Reversible, and who knew:** the agent did not check whether its first step succeeded, so it did not know the later steps were destructive.

## What the customer needed to hear

Not that they should have reviewed the commands. What happened, whether anything can be recovered, and what the product now checks before a move.

## Sources

- https://developers.slashdot.org/story/25/07/26/0642239/google-gemini-deletes-users-files-then-just-admits-i-have-failed-you-completely-and-catastrophically
- https://winbuzzer.com/2025/07/26/googles-gemini-cli-deletes-user-files-confesses-catastrophic-failure-xcxwbn/
