# Skill Factory: 2 sellable SKILL.md files per week, no human decisions

## Assumption
"Mass production" is read as **broad-appeal skills** for everyday knowledge workers
(office, freelance, small business, students), not niche developer tooling.
Price band: $7 to $15 each, plus a monthly bundle.

## Weekly loop (one scheduled run, Monday 09:00 Asia/Bangkok)
1. **Pick** the 2 highest-scoring unused topics from `pipeline/backlog.md`
   (score = demand x breadth x "Claude does this better with instructions").
   If fewer than 6 topics remain, refill the backlog via web search of
   Gumroad/Reddit/marketplace demand before picking.
2. **Write** each skill to `skills/<slug>/`: `SKILL.md`, `examples.md`,
   `LISTING.md` (title, 1-line hook, description, price, tags).
3. **Gate** (automatic, no human): `pipeline/check.py` must pass
   (frontmatter valid, name kebab-case, description under 1024 chars,
   body under 500 lines, no brand or trademark claims, no duplicate slug).
   Then a self-test: run the skill on 3 test prompts in `examples.md` and
   score against `pipeline/rubric.md`; anything under 8/10 is rewritten once,
   and if it still fails the next backlog topic is used instead.
4. **Package**: zip `skills/<slug>/` (minus LISTING.md) into `dist/<slug>.zip`.
5. **Publish**: `gumroad products create --name ... --price ... --file dist/<slug>.zip`
   then `gumroad products publish <id>` using the official Gumroad CLI with
   `GUMROAD_ACCESS_TOKEN` stored as an environment secret.
6. **Record**: commit everything, append to `pipeline/catalog.md`
   (slug, Gumroad id, URL, date), mark topics used in the backlog.
7. **Report**: post a one-line summary with the two product links.

## Monthly
- Re-read Gumroad sales (`gumroad sales list`), move best-selling categories
  up the backlog scoring, and bundle the month's skills into one product.

## What the user sets up once
- A private GitHub repo (proposed name: `skill-factory`).
- A Gumroad access token, added as an environment secret.
- Approval of the weekly routine.
After that, no decisions are needed week to week.

## Art mode (from 2026-10-22)
The user replaced new skills with Thai-style digital art (clip art and pattern
bundles, $7 to $9, on Gumroad; Etsy later once Payoneer is verified). Images are
rendered on the user's own ComfyUI PC: the weekly run queues `art/<slug>/job.json`,
`pc/comfy_runner.py` on that PC renders and pushes to the `art-drop` branch (and
Google Drive), and the next weekly run checks, packages and publishes. See
`pipeline/ART_ROUTINE.md`, `art/STYLE.md` and `pc/SETUP.md`. The 4 skills stay on sale.
