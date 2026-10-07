---
name: meeting-notes-to-actions
description: Turn messy meeting notes, chat logs or call transcripts into a clean summary of decisions, action items with owners and deadlines, and open questions. Use when someone pastes notes or a transcript and asks for a recap, action items, follow-ups, minutes, or "what did we agree".
---

# Meeting Notes to Actions

Convert raw meeting material into a recap people can act on in under a minute.

## Inputs
Accept anything: bullet notes, a transcript with speaker names, a chat export,
or a voice-to-text dump. If a meeting date, attendee list or project name is
given, use it. Never ask a question before producing the first draft.

## Process
1. Read everything once. Identify the meeting's purpose in one sentence.
2. Extract **decisions**: only things the group clearly agreed. If agreement is
   uncertain, put the item under Open Questions instead.
3. Extract **action items**. For each, find:
   - the task, written as a verb-first instruction
   - the owner (a named person; if none was named, write `Unassigned`)
   - the deadline (as stated; convert relative dates like "next Friday" to a
     real date only if the meeting date is known, otherwise keep the words)
4. Extract **open questions** and **risks** raised but not resolved.
5. Drop small talk, repeated points and anything off topic.
6. Do not invent owners, dates, numbers or decisions. When unsure, flag it with `(?)`.

## Output format
Use exactly this structure, in the language of the notes:

```
## <Meeting name or purpose> - <date if known>

**Summary:** <2-3 sentences>

### Decisions
- ...

### Action items
| # | Task | Owner | Due |
|---|------|-------|-----|
| 1 | ... | ... | ... |

### Open questions
- ...

### Follow-up message (ready to send)
<A short, friendly message to attendees listing each owner's tasks>
```

Leave out a section only if it would be empty, and say "None recorded" for
Action items rather than removing that section.

## Variations
- "Just the action items": output only the table.
- "Minutes" or "formal": add an Attendees line and use neutral, past-tense wording.
- Very long transcripts: group decisions and actions by agenda topic.

## Quality checks before answering
- Every action item has a verb, an owner field and a due field.
- Nothing appears that is not supported by the notes.
- The follow-up message matches the table exactly.
