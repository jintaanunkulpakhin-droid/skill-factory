---
name: sop-builder
description: Turn a rough description of how a task is done (notes, a voice memo transcript, a chat explanation or a messy checklist) into a clear standard operating procedure (SOP) with purpose, roles, numbered steps, checks and troubleshooting. Use when someone asks for an SOP, process document, how-to guide, checklist, work instruction, onboarding guide, or "write down how we do this".
---

# SOP Builder

Turn "here's roughly how we do it" into a step-by-step procedure that a new
person could follow on their first day without asking questions.

## Inputs
Accept any description of a process: rambling notes, a transcript of someone
explaining it, an old checklist, or chat messages. Optional: company or team
name, tools used, who performs it, how often, and the intended reader
(new hire, contractor, the whole team).

Never ask a question before the first draft. Where something important is not
stated, write `[confirm: ...]` in the step so the owner can fill it in.

## Process
1. Identify the process name, its purpose (why it exists, in one sentence),
   the trigger (what starts it) and the end result (how you know it is done).
2. List the roles involved and the tools, accounts or materials needed.
3. Break the work into numbered steps:
   - one action per step, starting with a verb ("Open", "Check", "Send")
   - name the exact tool, screen, field or file when given
   - put decisions as "If X, do Y. Otherwise, go to step N."
   - mark steps that are easy to get wrong with **Important:**
4. Add a quick check after any step where mistakes are costly
   ("Check: the invoice total matches the order").
5. Collect warnings, common mistakes and fixes into Troubleshooting.
6. Never invent tools, policies, amounts, deadlines, legal or safety rules.
   Only reorganise and clarify what was given, and mark gaps with `[confirm: ...]`.
7. If the process involves safety, money, personal data or legal
   requirements, add a one-line note that the owner should review it before use.

## Output format
```
# SOP: <Process name>

**Purpose:** <one sentence>
**When:** <trigger and frequency>
**Owner:** <role> | **Performed by:** <role(s)>
**Time needed:** <if known, else [confirm: time]>
**You need:** <tools, access, materials>

## Steps
1. ...
2. ...
   - If ..., then ...
   - **Check:** ...

## Done when
- ...

## Troubleshooting
| Problem | Fix |
|---|---|
| ... | ... |

## Open items to confirm
- <every [confirm: ...] listed again here>

_Version 1 - <date or [date]>_
```
Write in the language of the input unless asked otherwise.

## Variations
- "Checklist only": just the numbered steps as `- [ ]` boxes.
- "One-page" or "print": no Troubleshooting table, max 12 steps, group the rest.
- Several processes in one input: one SOP each, plus a short index.
- "Flowchart": add a Mermaid flowchart of the steps and decisions after the SOP.

## Quality checks before answering
- Every step starts with a verb and has one action.
- Every decision has both outcomes.
- Nothing invented; all gaps appear under Open items to confirm.
- A new person could finish the task using only this document.
