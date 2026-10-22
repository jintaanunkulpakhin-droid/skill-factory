# Weekly art run (no human decisions). Since 2026-10-22 this replaces skill steps 1 to 6.
Images are made on the user's own ComfyUI PC by pc/comfy_runner.py: it renders
every art/<slug>/job.json on main that has no drop yet and pushes the PNGs to the
art-drop branch (drops/<slug>/*.png + DONE). This run publishes what arrived and
queues the next jobs. Read art/STYLE.md and art/backlog.md first.

A. `git fetch origin art-drop`. If the branch exists, `git worktree add .art-drop origin/art-drop`.
B. Publish each drop that has drops/<slug>/DONE and whose slug is not yet in pipeline/catalog.md:
   1. `python3 pipeline/art_check.py <slug>` (automatic rejects go to art/<slug>/rejects.txt).
   2. Visual review: open every image not in rejects.txt and add its name (file name without
      .png) to rejects.txt if it shows any text or letters, a deformed or cut-off subject, a
      subject from the "Never prompt for" list in art/STYLE.md, or something off the theme.
      Also reject a clip art image whose background is not plain white (unless it is a scene).
   3. If fewer than the job's min_keep images are left, don't publish: add a catalog row
      "rejected" and say so in the report.
   4. `python3 pipeline/art_package.py <slug>`, then `python3 pipeline/art_publish.py <slug>`
      (uses $GUMROAD_ACCESS_TOKEN, never print it). Record the row like skills do: "live <id>",
      or "draft <id>" if "published" is false. Never rerun it for the same slug.
C. Queue jobs: a job is queued when art/<slug>/job.json exists but its slug has no DONE drop
   and is not in catalog.md. Until 2 jobs are queued, take the top unused theme in
   art/backlog.md, mark it [x], and write:
   - art/<slug>/job.json like art/loy-krathong-clipart/job.json: kind from the backlog line,
     12 to 16 prompts with short kebab-case names, each prompt = subject + the house style
     for that kind from STYLE.md, the STYLE.md negative prompt, per_prompt 2, min_keep 16.
   - art/<slug>/LISTING.md like art/loy-krathong-clipart/LISTING.md: price 7 for clipart,
     9 for patterns; describe only what the prompts make; keep the AI and license sentences.
   If fewer than 6 unused themes remain, add 8 more Thai or Asian themes following STYLE.md.
D. If a queued job is more than 8 days old with no drop, say "the ComfyUI PC has not picked
   up jobs since <date>" in the report. Never generate images anywhere else (no Higgsfield).
E. Promo for each bundle published this run, as in skill step 5 (promo file, then one
   Typefully X/Threads post for this run's bundles). Say what the files are and that they
   are AI-made. Copy dist/<slug>-cover.png next to the promo file for the user's posts.
F. Commit art/, pipeline/catalog.md and promo/ and push to main. If every drop on art-drop is
   now in catalog.md, delete the branch (`git push origin --delete art-drop`); the PC runner
   starts a fresh one.
G. Run skill step 7 (stats), then report in one short message: bundles published (links),
   jobs queued for the PC, PC status from D, and the stats table.
