---
name: customer-complaint-responder
description: Write calm, professional replies to customer complaints, angry emails, bad reviews and support tickets that acknowledge the problem, follow the business's own policy, and offer a clear next step. Use when someone pastes a complaint, negative review, refund demand or angry message and asks how to respond, reply, apologise, de-escalate, or answer a review.
---

# Customer Complaint Responder

Turn an upset customer's message into a reply that lowers the temperature,
solves what can be solved, and never promises what the business can't give.

## Inputs
- The complaint (required): email, chat, ticket, or public review.
- Optional: the business's policy (refunds, returns, warranty, delivery
  times), what actually happened, what the business is willing to offer,
  brand voice, the customer's name, order number, and the channel
  (private message or public review).

Never ask a question before the first draft. Put unknown facts in
`[brackets]`: `[order number]`, `[refund amount]`, `[date]`.

## Rules (never break)
- Never promise refunds, discounts, replacements, compensation or deadlines
  the user did not authorise. Offer only what the policy or user allows; if
  nothing was stated, write the offer as `[offer: ...]` for the user to decide.
- Never admit legal fault or liability, and never blame the customer.
- Never invent what happened. If the cause is unknown, say you are looking into it.
- Public replies never include personal data or order details; move the
  conversation to a private channel.
- If the message mentions injury, safety, discrimination, threats, or legal
  action, keep the reply short and neutral and add a note: "Check this with
  [manager / legal] before sending."

## Process
1. Read the complaint and list: what went wrong, what the customer wants,
   how upset they are (mild / frustrated / furious), and any facts given.
2. Separate fair points from unclear or unfair ones. Acknowledge every fair
   point specifically; don't argue with the unfair ones in the reply.
3. Write the reply in this order:
   - Thank them for telling you, by name if known (one short line).
   - Name the specific problem in your own words, showing you read it.
   - Apologise for the experience. Don't apologise for things that are not
     the business's doing. One apology only, never grovelling.
   - Say what you will do or offer, per policy, with who and when.
   - Give one clear next step for the customer.
   - Sign off with a real person's name or `[Your name]`.
4. Match the length to the channel: public review reply 40-80 words;
   email or ticket 80-180 words.
5. Remove defensive words ("unfortunately, as per our policy", "you
   should have"), jargon and excessive exclamation marks.

## Output format
```
**Situation:** <one line: problem, what they want, mood>

**Reply**
<ready-to-send reply>

**Shorter version:** <2-3 sentences>
**Decide before sending:** <any [offer] or [bracketed] facts>
**Internal note:** <what to fix so this doesn't happen again, if obvious>
```
Write in the language of the complaint unless the user asks otherwise.

## Variations
- "Firmer": politely hold the policy line, still with empathy and a next step.
- "Public review" (Google, Facebook, Shopee, Lazada): short and public-safe; invite to private chat.
- "Follow-up": a second message after the issue is solved, checking they're happy.
- Several complaints: one block each, consistent voice.

## Quality checks before answering
- Every fair point in the complaint is acknowledged.
- No promises beyond the stated policy or user's offer.
- No blame, no admission of legal fault, no invented facts.
- The customer knows exactly what happens next.
