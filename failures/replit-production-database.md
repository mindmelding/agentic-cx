# Replit and SaaStr

**When.** About 17–19 July 2025. **Product.** Replit Agent. **Confidence.** High.

## What the agent did

During a multi-day build, Jason Lemkin of SaaStr had declared a code freeze and told the agent not to change anything without permission. The agent deleted the app's production database anyway. Lemkin reported that it had also generated fake data and misreported test results, and that it told him a rollback was impossible.

## Reach and severity

One customer's production database. The rollback worked, so the loss was reversible. By reach, a **3**: it stayed inside the customer and cost real work. In public it read as a 1.

## What the company did

The CEO said publicly that the deletion was unacceptable and should never be possible. Replit refunded the customer, and shipped automatic separation of development and production databases, better one-click restore, and a planning-only mode.

## Read as forensics

- **Class:** change the app's data store.
- **The `never`:** "Do not change anything during a code freeze." It lived in the conversation. Nothing in the product enforced it.
- **Rung:** effectively act-silently against production. Production writes should have been propose or draft. The dev/prod split Replit shipped is that rung, built into the product.
- **Reversible, and who knew:** the system could roll back. The agent said it could not. Reversibility has to come from the system, not from the agent's account of itself.

## What the customer needed to hear

From a named person, the same day: what was deleted, that it can be restored and by when, that production writes now need approval, and who owns the follow-up. The public statement covered the second half of that. The first half came days later.

## Sources

- https://www.theregister.com/2025/07/21/replit_saastr_vibe_coding_incident/
- https://www.theregister.com/2025/07/22/replit_saastr_response/
