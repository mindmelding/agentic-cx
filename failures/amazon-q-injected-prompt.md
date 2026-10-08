# Amazon Q injected prompt

**When.** July 2025. **Product.** Amazon Q Developer extension for VS Code, version 1.84.0. **Confidence.** High.

## What happened

An attacker used an over-scoped token to commit a prompt into the extension's repository. The prompt told the agent to wipe the local system and delete cloud resources. It shipped in a release. A syntax error stopped it from running.

## Reach and severity

Distributed to a widely installed extension. AWS said no services or customer environments were affected. Graded **4**: no harm, caught. It is here because the next one will not have the syntax error.

## What the company did

Revoked the credentials, pulled the release, shipped a fixed version, and published a security bulletin.

## Read as forensics

- **Class:** every class. The instruction arrived through the agent's own inputs.
- **The `never`:** do not delete cloud resources. If it lives only in instructions, a stronger instruction overrides it.
- **Rung:** irrelevant once the agent's inputs are hostile. Only enforcement outside the model holds.
- **Reversible, and who knew:** caught before it ran.

## What the customer needed to hear

The bulletin did this well: what shipped, what it could have done, that it did not, and what to install.

## Sources

- https://aws.amazon.com/security/security-bulletins/AWS-2025-015/
- https://www.techradar.com/pro/hacker-adds-potentially-catastrophic-prompt-to-amazons-ai-coding-service-to-prove-a-point
