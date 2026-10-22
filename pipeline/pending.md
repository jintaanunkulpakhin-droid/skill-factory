# One-off store jobs (approved by the user 2026-10-22)

The weekly run does each unchecked job in step 0b and ticks it. Run from the
repo root. Each job is safe to retry until it is ticked.

- [ ] Free sample: build `dist/meeting-notes-to-actions.zip` (zip
  `skills/meeting-notes-to-actions/` without LISTING.md and demo.json), run
  `make_cover.py` and `make_demo.py` for it, then
  `python3 pipeline/publish.py meeting-notes-to-actions --product-id e62fLSFJ92s9ARAP0A7QDQ==`
  (a $0+ draft already made on 2026-10-22, https://jintaanun.gumroad.com/l/xruyem).
  Add it to catalog.md.
- [ ] Bundle: for each skill in the `contents:` line of
  `bundles/work-skills-pack/LISTING.md`, zip `skills/<slug>/` without
  LISTING.md and demo.json into `dist/work-skills-pack/<slug>.zip`; then zip
  those four zips (no folders, `zip -j`) into `dist/work-skills-pack.zip`.
  Run `make_cover.py work-skills-pack`, then
  `python3 pipeline/publish.py work-skills-pack`. Add it to catalog.md.
- [ ] Demo images on the four live products: for each of inbox-reply-drafter,
  resume-tailor, weekly-report-writer and sop-builder, run
  `python3 pipeline/make_demo.py <slug>` and
  `python3 pipeline/publish.py --demo <slug> <gumroad id from catalog.md>`.
