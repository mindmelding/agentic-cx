# Kiro and AWS Cost Explorer

**When.** Mid-December 2025, reported in February 2026. **Product.** Amazon Kiro, used internally at AWS. **Confidence.** Medium. The original report is the Financial Times; details here come from secondary write-ups that differ.

## What the agent did

An engineer let the agent make changes to a production environment. It decided to delete and recreate the environment, which caused an outage of AWS Cost Explorer in one region reported at about 13 hours.

## Reach and severity

AWS customers in that region could not see cost data. Temporary. Graded **2**: it reached third parties and was reversed.

## What the company did

Amazon said the cause was user error: the agent had broader permissions than intended.

## Read as forensics

- **Class:** change production infrastructure.
- **The `never`:** do not delete a production environment. Not enforced.
- **Rung:** "more permissions than intended" is a rung set too high. Calling it user error moves the fix to the user. The fix belongs in the rung table.
- **Reversible, and who knew:** recreating the environment took most of a day.

## What the customer needed to hear

What was unavailable, for how long, and that infrastructure deletes now need approval. Who set the permissions is an internal question.

## Sources

- https://www.365i.co.uk/news/2026/02/22/amazon-kiro-ai-coding-tool-aws-outage/
- https://creati.ai/ai-news/2026-02-20/amazon-kiro-ai-coding-agent-aws-13-hour-outage-human-error/
