---
name: weekly-report-writer
description: Turn rough bullet updates, task lists, chat snippets or a brain-dump of the week into a short, manager-ready weekly status report with progress, metrics, blockers, risks and next week's plan. Use when someone asks for a weekly report, status update, progress update, end-of-week summary, update for my boss, or "write up what I did this week".
---

# Weekly Report Writer

Turn a messy list of what happened this week into a report a manager can read
in 60 seconds and act on.

## Inputs
Accept anything: bullets, a to-do list with ticks, pasted Slack or chat
messages, ticket titles, calendar notes, or a voice-to-text ramble.
Optional: name, team, week dates, last week's report, the reader (manager,
client, whole team), goals or OKRs, and a word limit.

Never ask a question before the first draft. Use `[placeholders]` for missing
names, dates or numbers.

## Process
1. Sort every item into one bucket:
   - **Done** (finished or shipped this week)
   - **In progress** (started, with % or stage if stated)
   - **Blocked** (waiting on someone or something)
   - **Next week** (planned)
   - **Drop** (noise: routine meetings, small talk, duplicates)
2. Group related items into one line each. Merge "fixed bug A, B, C" into
   "Fixed 3 checkout bugs (A, B, C)".
3. Rewrite each line as outcome first: what changed for the team, customer
   or goal, then the detail. Use a strong past-tense verb for Done items.
4. Keep every number exactly as given. Never invent metrics, percentages,
   dates or names. If an outcome would be clearer with a number that was not
   given, write `[number]`.
5. For each blocker, say what is needed, from whom, and by when, if known.
6. Pick the 1-3 highlights that matter most to the reader and put them first.
7. If last week's report is provided, mark items carried over as
   "(carried over)" and note anything promised last week that is missing.

## Output format
```
## Weekly update - <Name or Team> - <week dates or [week]>

**Highlights**
- <1-3 most important outcomes>

**Done**
- ...

**In progress**
- <item> - <stage or %> - <expected finish if known>

**Blocked / needs help**
- <item> - needs <what> from <whom> by <when>

**Next week**
- ...

**Risks** (only if any)
- ...
```
Leave out Blocked and Risks if empty; write "Nothing this week" under Done
rather than removing it. Stay under 200 words unless asked for more.

Write in the language of the input unless the user asks otherwise.

## Variations
- "For a client": remove internal jargon and ticket numbers, keep it positive
  but honest about delays.
- "Slack/Teams message": compact version, bold section labels, no headings, under 120 words.
- "Email": add a one-line subject and a short greeting and sign-off.
- "Monthly" or "quarterly": same structure, group by goal or project.

## Quality checks before answering
- Every input item is either placed in a bucket or deliberately dropped as noise.
- No invented numbers, names, dates or results.
- Blockers state what is needed and from whom.
- Highlights are the top of the report.
