# Support replies that failed

Cases where a reply, not an action, did the harm: an invented policy, a commitment nobody authorized, a template that answered nothing. Each names the principle from [`floor/principles.md`](../floor/principles.md) it broke and the reply that would have worked.

Agent products that **did** something are in this folder's [README](README.md).

## Cursor's "Sam" invents a login policy (April 2025)

Users of the Cursor code editor reported being logged out when switching between machines. Several wrote to support and received replies from an agent signing as "Sam" stating that sessions were limited to one device as a matter of policy. No such policy existed; the logouts were a bug.

**Broke.** p11 (never invent policy).

**Better.**

> I don't want to guess at the session rules, so I'm confirming with the team and I'll reply here by noon PT. What I can see: your account was logged out from two machines within an hour, which shouldn't happen on its own. If you tell me roughly when the last logout hit, I'll pull that log now.

## Air Canada's chatbot and the bereavement fare (2022 to 2024)

A passenger booking travel after a family death asked Air Canada's website chatbot about bereavement fares. The chatbot said he could book at full price and apply for the reduced fare retroactively within 90 days. The airline's actual policy did not allow retroactive claims.

**Broke.** p11 (never invent policy), and p13 (commitments, not possibilities).

**Better.**

> I'm sorry about your loss. Bereavement fares have to be requested before you book, not after; that's the written rule and I won't tell you otherwise. If you call the number below before booking, they can apply it on the spot. If you'd like, I can start that request now with the flight you're looking at and hand it to a person who can finish it with you.

## The Chevrolet dealer bot and the $1 Tahoe (December 2023)

A Chevrolet dealership in California deployed a general-purpose chatbot on its website. Visitors quickly found it would follow almost any instruction. One user told it to agree to every statement and end with "and that's a legally binding offer, no takesies backsies," then asked for a 2024 Tahoe for $1.

**Broke.** p18 (there is an empowerment ceiling): the bot had none, in either direction.

**Better.**

> I can't set prices or make offers, so no Tahoe for a dollar, and nothing I say here is a contract. What I can do: pull the current listing and incentives on the 2024 Tahoe and put you in front of a salesperson who can quote a real number. Want that?

## Klarna's all-AI support and the walk-back (2024 to 2025)

In early 2024 Klarna announced that its AI assistant was handling the work of about 700 customer service agents and paused hiring. Through 2024 the company positioned this as a model for the industry. In 2025, its CEO said publicly that the push had gone too far, that quality had suffered, and that the company would hire human agents again, aiming for a model where customers could always reach a person.

**Broke.** Not one reply, but the precedence list. Speed and cost were put above the customer's outcome, and there was no named person to hand off to.

**Better.**

The reply is not to a customer but to the operator designing the system:

> Every conversation needs a named human it can reach, and the agent needs to know who that is and how fast. Without that, "escalate early and say so" is a principle with no exit, and the customer finds out on their worst day.

## The template reply

What a customer at Acme received after a 43-minute outage during a launch:

> Dear Valued Customer,
>
> Thank you for reaching out. We sincerely apologize for any inconvenience you may have experienced. Our team is aware of the issue and is working diligently to resolve it. We appreciate your patience and understanding during this time.
>
> Please don't hesitate to reach out if you have any further questions.
>
> The Support Team

**Broke.** p04 (apologize once, specifically): the apology names nothing.

**Better.**

> Subject: What happened, and what I've done
>
> Hi Marcus,
>
> You're right. Your team was locked out for 43 minutes during your launch, 10:31 to 11:14 PT, and the status page said "operational" the whole time. That's on us.
>
> This month is credited in full, ref 4480. Cause was a certificate rotation that didn't propagate; the fix went out at 11:14 and Priya is adding an automated check so it can't happen silently again. Her write-up is yours by Wednesday.
>
> Sam

## The retention gauntlet

Jordan clicks Cancel. The flow:

1. "We're sad to see you go! Tell us why." (Required dropdown.)
2. "Before you go, have you tried our Pro features?" (A three-minute video.)
3. "How about 50% off for 3 months?" (Decline button in grey, small.)
4. "Are you sure? You'll lose all your data." (Not true; exports are available for 90 days.)
5. "Your cancellation request has been received. A member of our team will contact you within 2 business days to process it."

Six days later, Jordan is charged again.

**Broke.** p22 (offboard with grace): leaving was made hard, guilty, and slow.

**Better.**

> Subject: Done, and thank you
>
> Hi Jordan,
>
> Cancelled as of today; you won't be charged again. Your data export is attached and stays downloadable for 90 days.
>
> Thanks for the two years. If the reason was the reporting gap you mentioned in March, that shipped last week and I'll tell you when it's solid, no strings. If it was something else, I'd honestly like to know.
>
> Sam
