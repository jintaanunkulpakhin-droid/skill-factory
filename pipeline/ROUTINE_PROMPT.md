# Weekly run (no human decisions)
Repo: skill-factory. Read PLAN.md, pipeline/backlog.md, pipeline/rubric.md, pipeline/catalog.md.
0. First publish any catalog.md rows marked "draft <id>" with `python3 pipeline/publish.py --enable <id>`, and change "draft" to "live" on success. If Gumroad says a payment method is missing, leave them as drafts and say so in the report.
1. Topic freeze until 2026-11-07: take topics in backlog order and do not reorder, reprice or replace them before then. If fewer than 6 unused topics remain in backlog.md, add 10 broad-appeal topics found by web search (marketplace demand), skipping any slug in catalog.md.
2. Take the top 2 unused topics. For each, write skills/<slug>/SKILL.md, examples.md (3 test prompts), LISTING.md, modeled on skills/meeting-notes-to-actions.
3. Run `python3 pipeline/check.py skills/<slug>`. Self-test the skill on its 3 prompts and score with rubric.md. Below 8/10: rewrite once; still failing: drop it and take the next topic.
4. Copy pipeline/INSTALL.md into skills/<slug>/, then zip skills/<slug>/ without LISTING.md into dist/<slug>.zip. Run `python3 pipeline/make_cover.py <slug>` (cover and thumbnail images), then publish with `python3 pipeline/publish.py <slug>` (creates the product from LISTING.md, uploads the zip and images, publishes; uses $GUMROAD_ACCESS_TOKEN, never print it). It prints JSON; if "published" is false the product stays a draft (the "note" says why), so record the row as "draft <id>" and never rerun it for the same slug.
5. Write promo/<YYYY-MM-DD>.md (run date) with ready-to-paste posts for each new skill, modeled on promo/2026-10-12.md: Reddit (title + body, useful first, link last), X (under 280 chars), Facebook group, and Thai. Only claim what SKILL.md actually does. The user posts Reddit, Facebook and Thai community posts by hand; never post those yourself.
   Then schedule ONE combined post for both new skills on X and Threads with the Typefully connector (create_draft, social_set_id 341088, publish_at "next-free-slot", same text on both, under 280 characters counting each link as 23). The user approved this auto-posting on 2026-10-12. First check get_social_set_details: if publishing_quota.remaining is 0, schedule it for 12:00 Asia/Bangkok on the day the quota resets instead of next-free-slot. If Typefully refuses, skip it and say so in the report. Copy the file to /mnt/project-files/skill-factory/promo/ if that folder exists.
6. Mark the topics [x] in backlog.md, append rows to catalog.md, commit and push to main.
7. Run `python3 pipeline/stats.py` for the sales table (the API has no page views).
8. Report in one short message: the two product links, a link to the promo file, when the X/Threads post is scheduled, and the stats table.

ART MODE (from 2026-10-22, the user chose to replace new skills with Thai-style art):
do step 0 (and 0b if present) above, then follow pipeline/ART_ROUTINE.md instead of
steps 1 to 6 and 8. No new skills are written. The live skills stay on sale and stay in stats.
