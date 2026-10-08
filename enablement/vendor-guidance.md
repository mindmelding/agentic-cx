# Vendor guidance

What the model vendors recommend for human oversight of agents. Their advice is written for builders. The column on the right is what it means for the customers this team supports.

| Vendor | What they recommend | For customers | Source |
|---|---|---|---|
| Anthropic | Read-only by default. A person approves before the agent changes code or systems. People can grant standing permission for routine work. Make the agent's reasoning visible | Start at propose or draft. Standing grants are the rungs. Show why, not only what | [framework](https://www.anthropic.com/news/our-framework-for-developing-safe-and-trustworthy-agents) |
| OpenAI | Hand off to a person when failures or retries exceed a limit, and for high-risk or irreversible actions such as refunds, cancellations, and payments. Layered guardrails, with a risk rating per tool | Irreversible classes need a person in the loop. Repeated failure is a handoff, not another try | [guide summary](https://www.maginative.com/article/how-to-build-ai-agents-a-detailed-practical-guide-from-openai/) |
| Google | Agents need a well-defined human controller, limited powers, and observable actions. Combine fixed rules (such as spend limits that allow, block, or ask) with the model's own judgment, because the model alone is not enough while prompt injection works | Name the person accountable for each agent. Put limits in settings. Show the customer what it did | [paper](https://research.google/pubs/an-introduction-to-googles-approach-for-secure-ai-agents/) |

Verified 2026-10-07. When a vendor publishes new guidance, add a row and note it in the [changelog](CHANGELOG.md).
