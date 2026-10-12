# Weekly run (no human decisions)
Repo: skill-factory. Read PLAN.md, pipeline/backlog.md, pipeline/rubric.md, pipeline/catalog.md.
0. First publish any catalog.md rows marked "unpublished" (rebuild their zips as in step 4) and replace those rows with the Gumroad id and URL.
1. If fewer than 6 unused topics remain in backlog.md, add 10 broad-appeal topics found by web search (marketplace demand), skipping any slug in catalog.md.
2. Take the top 2 unused topics. For each, write skills/<slug>/SKILL.md, examples.md (3 test prompts), LISTING.md, modeled on skills/meeting-notes-to-actions.
3. Run `python3 pipeline/check.py skills/<slug>`. Self-test the skill on its 3 prompts and score with rubric.md. Below 8/10: rewrite once; still failing: drop it and take the next topic.
4. Copy pipeline/INSTALL.md into skills/<slug>/, then zip skills/<slug>/ without LISTING.md into dist/<slug>.zip. Publish with the Gumroad CLI: `gumroad products create` (name, price, description from LISTING.md, --file the zip), then `gumroad products publish <id>`. Token is $GUMROAD_ACCESS_TOKEN. If the token or CLI is unavailable, keep the products unpublished and report that.
5. Mark the topics [x] in backlog.md, append rows to catalog.md, commit and push to main.
6. Report the two product links in one short message.
