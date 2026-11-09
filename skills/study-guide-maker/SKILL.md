---
name: study-guide-maker
description: Turn lecture notes, textbook chapters, slides or a class transcript into a clear study guide with key concepts, definitions, worked examples, a one-page summary, flashcards and a practice quiz with an answer key. Use when a student pastes course material and asks for a study guide, revision notes, summary, flashcards, practice questions, a quiz, or "help me study for my exam".
---

# Study Guide Maker

Turn raw course material into something a student can actually revise from,
and test themselves on, using only what is in their material.

## Inputs
- Course material (required): notes, a chapter, slide text, a transcript.
- Optional: subject and level (high school, university, professional exam),
  exam date or format (multiple choice, essay, problems), topics the teacher
  stressed, and how many questions to make.

Never ask a question before the first draft.

## Rules (never break)
- Build everything from the material given. Do not add facts, dates,
  formulas or examples that are not in it. If something important looks
  missing or unclear in the notes, list it under "Check with your notes or teacher".
- Never change a definition, formula or number from the material.
- If the material seems to contain an error, keep it as written and flag it
  as "Possible error, check this".
- Make quiz answers verifiable: each answer key line cites the section of
  the guide it comes from.

## Process
1. Skim everything and split it into 3-8 topics in a logical order.
2. For each topic write:
   - the big idea in 1-2 sentences, in plain language
   - key terms with short definitions taken from the material
   - formulas, rules or steps exactly as given, with one worked example
     only if the material includes one
   - a common mistake or confusing pair, only if the material suggests one
3. Write a one-page summary: the whole course material in 10-15 bullets.
4. Make 10-20 flashcards (term or question on the front, short answer on the back).
5. Make a practice quiz matching the exam format if given, otherwise a mix:
   multiple choice (4 options, one correct, plausible wrong options),
   short answer, and one longer "explain" question. Put answers at the end.
6. Add a short revision plan if an exam date is given: which topics on which days,
   hardest topics first, ending with a full practice quiz.

## Output format
```
# Study guide: <subject or topic>

## Topic 1: <name>
**Big idea:** ...
**Key terms**
- **Term:** definition
**How it works / formula:** ...
**Watch out for:** ...

## One-page summary
- ...

## Flashcards
| Front | Back |
|---|---|

## Practice quiz
1. ...
   a) ... b) ... c) ... d) ...

## Answer key
1. b - <one-line reason> (Topic 1)

## Check with your notes or teacher
- ...
```
Write in the language of the material unless the user asks otherwise.

## Variations
- "Flashcards only" or "quiz only": just that part, with more items.
- "Explain like I'm new": simpler wording and an everyday analogy per topic.
- "Anki" or "Quizlet": flashcards as `front;back` lines, one per line.
- Very long material: one guide per chapter, then a combined summary.

## Quality checks before answering
- Every fact, definition and number comes from the material.
- Every quiz question has exactly one correct answer in the key, with its topic.
- Wrong options are plausible but clearly wrong according to the material.
- Gaps and possible errors are listed, not filled in.
