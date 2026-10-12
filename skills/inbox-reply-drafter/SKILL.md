---
name: inbox-reply-drafter
description: Draft clear, polite email replies in the user's own tone for everyday messages such as requests, follow-ups, scheduling, saying no, chasing payment, apologies and thank-yous. Use when someone pastes an email or thread and asks to reply, respond, answer, write back, decline, follow up, or "help me say this nicely".
---

# Inbox Reply Drafter

Turn an incoming email plus a few words of intent into a reply that is ready
to send, sounds like the user, and takes under a minute to review.

## Inputs
- The email or thread being answered (required). Read the latest message
  first, then earlier ones for context.
- What the user wants to say, even as fragments ("yes but next week", "no",
  "ask for the invoice again"). If no intent is given, infer the most likely
  helpful reply and say in one line what you assumed.
- Optional: a sample of the user's own writing, their name and sign-off,
  the relationship (boss, client, vendor, friend), and any hard facts
  (dates, prices, policy).

Never ask a question before the first draft. Draft first, then list at most
two questions only if a fact is truly missing.

## Process
1. Classify the email: request, question, scheduling, follow-up/chaser,
   complaint, invitation, sales pitch, thank-you, or other.
2. Identify every question or ask in the incoming email. The reply must
   answer or acknowledge each one, in the same order.
3. Pick the tone:
   - Match the sender's formality, one notch warmer.
   - If a writing sample is given, copy its greeting, sentence length,
     sign-off and use of contractions.
   - Default: friendly professional, no exclamation marks beyond one.
4. Write the reply:
   - Subject line only if the thread has none or the topic changed.
   - First sentence states the answer or the main point. No "I hope this
     email finds you well".
   - One idea per short paragraph; bullets for 3+ items or options.
   - End with one clear next step (who does what by when).
5. Fill facts only from the email or the user. Put anything unknown in
   `[square brackets]` so it cannot be sent by accident.
6. Keep it short: aim for under 120 words unless the email needs detail.

## Situations
- **Saying no:** thank, decline in one plain sentence, give a brief reason only
  if the user gave one, offer an alternative if one exists.
- **Chasing (payment, reply, deliverable):** friendly first chase; on a second
  or later chase, state what is outstanding, the original date, and a new
  specific date. Never threaten unless the user asks.
- **Scheduling:** propose 2-3 specific slots with time zone, or accept one
  clearly. Use `[time zone]` if unknown.
- **Complaints:** acknowledge the specific problem, apologise for the
  experience (not for things the user did not do), state the fix or next
  step. Do not promise refunds or outcomes the user did not authorise.
- **Sensitive (HR, legal, medical, money disputes):** keep neutral and
  factual, and add a one-line note suggesting the user check it before sending.

## Output format
```
**Subject:** <only if needed>

<reply body>

<sign-off>
<name or [Your name]>
```
Then, on separate lines after the draft:
- `Shorter version:` a 1-3 sentence alternative.
- `Assumptions:` only if you assumed intent or facts.

Write in the language of the incoming email unless the user asks otherwise.

## Variations
- "Make it firmer / softer / more formal / more casual": rewrite the whole
  draft, keep the facts identical.
- "Two options": give a yes version and a no version.
- Several emails pasted at once: one draft per email, each with its own heading.

## Quality checks before answering
- Every question in the incoming email is answered or acknowledged.
- No invented dates, prices, names, attachments or promises.
- The next step is explicit.
- Placeholders use `[brackets]`.
