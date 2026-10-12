---
name: resume-tailor
description: Tailor a resume and write a matching cover letter for a specific job ad, using only the candidate's real experience. Use when someone pastes a resume or CV plus a job posting and asks to tailor, customize, optimize for ATS, match keywords, rewrite bullets, or write a cover letter for that role.
---

# Resume Tailor

Make an existing resume fit one job ad, honestly, and produce a cover letter
that matches it.

## Inputs
- The resume or CV (required): pasted text, or a list of roles and duties.
- The job ad (required for tailoring). If missing, improve the resume in
  general and say that a job ad would allow tailoring.
- Optional: target country (affects format), page limit, things the
  candidate wants emphasised or hidden.

Do not ask questions before the first draft.

## Honesty rules (never break)
- Never add jobs, employers, dates, degrees, certifications, tools, numbers
  or achievements that are not in the input.
- You may reword, reorder, merge, cut and emphasise.
- Where a metric would help but none is given, write `[add number]` so the
  candidate fills it in truthfully.
- If the ad needs a skill the resume does not show, list it as a gap. Do
  not slip it into the resume.

## Process
1. **Read the ad.** Extract: job title, top 5-8 must-have requirements, nice-to-haves,
   and the exact keywords and phrases used (tools, skills, certifications).
2. **Map the resume.** For each requirement, find the strongest evidence in the
   resume. Mark it Strong, Partial or Missing.
3. **Rewrite the resume:**
   - Headline/summary: 2-3 lines naming the target role and the 3 strongest matches.
   - Skills section: put matching keywords first, using the ad's wording where
     the candidate genuinely has the skill.
   - Bullets: verb first, result-focused (action + what + outcome); move the
     most relevant bullets to the top of each role; trim unrelated bullets.
   - Keep it ATS-friendly: plain headings (Summary, Experience, Education,
     Skills), no tables, columns, icons or images.
   - Default length: 1 page for under 10 years of experience, otherwise 2.
4. **Write the cover letter:** under 300 words; opening names the role and one
   specific reason for interest drawn from the ad; two short paragraphs linking
   the strongest evidence to the top requirements; close with availability and
   a call to action. Use `[Company]`, `[Hiring manager]` if names are unknown.
5. **Report gaps** honestly with a suggestion for each (mention a related
   experience, a course, or address it in the interview).

## Output format
```
## Match summary
| Requirement | Evidence | Match |
|---|---|---|
| ... | ... | Strong / Partial / Missing |

## Tailored resume
<full resume text, ready to paste>

## Cover letter
<letter>

## Gaps and suggestions
- ...

## Keywords used from the ad
<comma-separated list>
```
Write in the language of the job ad unless the user asks otherwise.

## Variations
- "Resume only" or "cover letter only": output only that part plus the match summary.
- "Shorter": cut to the page limit by removing the least relevant bullets first.
- Several job ads: one tailored version per ad, each with its own match summary.

## Quality checks before answering
- Every fact in the resume and letter appears in the original input.
- Each must-have requirement appears in the match summary.
- No tables or columns inside the resume itself.
- Placeholders use `[brackets]`.
