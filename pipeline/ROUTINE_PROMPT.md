# Weekly run (no human decisions)
Repo: skill-factory. Read PLAN.md, pipeline/backlog.md, pipeline/rubric.md, pipeline/catalog.md.
0. First publish any catalog.md rows marked "draft <id>" with `python3 pipeline/publish.py --enable <id>`, and change "draft" to "live" on success. If Gumroad says a payment method is missing, leave them as drafts and say so in the report.
1. If fewer than 6 unused topics remain in backlog.md, add 10 broad-appeal topics found by web search (marketplace demand), skipping any slug in catalog.md.
2. Take the top 2 unused topics. For each, write skills/<slug>/SKILL.md, examples.md (3 test prompts), LISTING.md, modeled on skills/meeting-notes-to-actions.
3. Run `python3 pipeline/check.py skills/<slug>`. Self-test the skill on its 3 prompts and score with rubric.md. Below 8/10: rewrite once; still failing: drop it and take the next topic.
4. Copy pipeline/INSTALL.md into skills/<slug>/, then zip skills/<slug>/ without LISTING.md into dist/<slug>.zip. Run `python3 pipeline/make_cover.py <slug>` (cover and thumbnail images), then publish with `python3 pipeline/publish.py <slug>` (creates the product from LISTING.md, uploads the zip and images, publishes; uses $GUMROAD_ACCESS_TOKEN, never print it). It prints JSON; if "published" is false the product stays a draft (the "note" says why), so record the row as "draft <id>" and never rerun it for the same slug.
5. Mark the topics [x] in backlog.md, append rows to catalog.md, commit and push to main.
6. Report the two product links in one short message.
