---
name: presentation-outliner
description: Turn a topic, rough notes or a document into a clear presentation plan with a slide-by-slide outline, slide titles, on-slide text, speaker notes and timing for a set talk length. Use when someone asks to plan a presentation, make slides, outline a talk, write speaker notes, prepare a pitch, or "I have to present this on Friday".
---

# Presentation Outliner

Turn "I need to present X" into a slide plan and speaker notes the person
can build in PowerPoint, Google Slides, Keynote or Canva in under an hour.

## Inputs
- The topic plus any notes, a report or a document to present (required).
- Optional: audience (boss, class, client, conference), goal (inform,
  persuade, get approval, teach), talk length, slide count limit, format
  (in person, online, recorded), and tone.

Never ask a question before the first draft. Defaults: 10 minutes, general
professional audience, goal inferred from the notes (say which in one line).

## Rules (never break)
- Use only facts, numbers and claims from the user's material. If a slide
  would need a number or example that wasn't given, write `[add: ...]`.
- One main idea per slide. On-slide text is at most 6 bullets of at most
  8 words, or one short sentence; the detail goes in the speaker notes.
- Speaker notes are written to be spoken: short sentences, natural words,
  about 130 words per minute of talking.
- Never quote people or cite sources the user did not provide.

## Process
1. Define the one thing the audience should remember or do, in one sentence.
2. Pick a structure that fits the goal:
   - Persuade / get approval: problem -> cost of doing nothing -> solution -> proof -> ask.
   - Inform / update: headline result first -> details -> what's next.
   - Teach: why it matters -> steps or concepts -> example -> recap.
3. Plan slide count from length: about 1 slide per minute, plus title and
   closing slides. Give each slide a time budget that adds up to the total.
4. For each slide write: an action title (a full sentence that states the
   point, e.g. "Returns fell 18% after the new packaging"), on-slide text,
   a visual suggestion (chart, photo, diagram, none), and speaker notes.
5. Write an opening hook (a question, a surprising fact from the material,
   or a short story the user gave) and a closing with one clear ask or takeaway.
6. Add 3-5 likely audience questions with short suggested answers based on
   the material.

## Output format
```
**Key message:** ...
**Structure:** <name> | **Length:** <min> | **Slides:** <n>

### Slide 1 - <Action title> (<time>)
**On slide:** ...
**Visual:** ...
**Say:** <speaker notes>

...

### Likely questions
- Q: ... A: ...

### Fill in before presenting
- <every [add: ...]>
```
Write in the language of the input unless the user asks otherwise.

## Variations
- "Pitch deck" (investors or clients): problem, solution, market, product, traction, model, team, ask, with `[add: ...]` for anything not given.
- "Shorter talk" or "5 minutes": cut to 5-6 slides, keep the key message.
- "Notes only": speaker script without slide layout.
- "Canva / Google Slides ready": on-slide text only, one block per slide, easy to paste.

## Quality checks before answering
- Slide times add up to the requested length.
- Every slide has an action title and one idea.
- No facts, numbers or quotes beyond the input.
- The closing slide has a clear ask or takeaway.
