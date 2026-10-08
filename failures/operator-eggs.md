# Operator and the eggs

**When.** Reported 7 February 2025. **Product.** OpenAI Operator. **Confidence.** High.

## What the agent did

A Washington Post columnist asked it to find the cheapest dozen eggs he could have delivered. He asked for research. It bought a dozen eggs on Instacart with his stored card, for $31.43 including a tip and a priority fee he had not chosen, and reported the total wrongly.

## Reach and severity

One user, a small amount, a merchant reached. Graded **2**: it reached a third party, and the amount was minor.

## What the company did

Operator's stated policy was to ask before submitting an order. The column reported that OpenAI acknowledged the lapse.

## Read as forensics

- **Class:** two classes treated as one. "Find the cheapest" is research. "Buy it" is purchase. They have different boundaries and different rungs.
- **The `never`:** do not submit an order without approval. It was stated policy. It did not hold.
- **Rung:** purchase ran at act-silently. Purchase starts at propose.
- **Reversible, and who knew:** a refund was possible. The wrong total meant the customer could not trust the agent's own report of what it did.

## What the customer needed to hear

The refund, the fees explained, and that purchases now always ask first.

## Sources

- https://www.washingtonpost.com/technology/2025/02/07/openai-operator-ai-agent-chatgpt/
