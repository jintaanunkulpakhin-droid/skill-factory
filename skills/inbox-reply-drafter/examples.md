# Test prompts (used by the automatic self-test)

## 1. Decline with fragments
Incoming: "Hi, could you speak at our customer meetup on 14 Nov and also
share your slides from last year?" Intent: "no to talk, yes slides".
Expected: thanks, a clear no to the talk, slides offered with `[link]`
placeholder, both asks answered in order, under 120 words.

## 2. Second payment chase, no intent given beyond "chase again"
Incoming thread: invoice #2041 sent 1 Sep, due 30 Sep, one earlier reminder.
Expected: polite but firm, states invoice number, amount as `[amount]` if not
given, original due date, asks for payment by a specific new date or a reply;
no threats.

## 3. Thai-language email asking to reschedule a meeting
Expected: the full reply is in Thai, proposes 2-3 slots or `[time]`
placeholders, includes a shorter version.
