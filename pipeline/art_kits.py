#!/usr/bin/env python3
"""Upload kits for the channels without an upload API. Usage: art_kits.py <slug> [drop_dir]
Run art_package.py <slug> first. Writes:
  dist/<slug>-etsy/    the bundle zip, cover, thumbnail and ETSY.txt (title, 13 tags,
                       description, price) to paste into a new Etsy digital listing
  dist/<slug>-adobe/   one 2048px JPG per kept image + adobe_stock.csv (title,
                       keywords, category) for the Adobe Stock contributor portal
On the ComfyUI PC, comfy_runner.py runs this after the bundle is live and copies
both folders to the Google Drive folder.
"""
import csv, json, pathlib, re, shutil, sys
from PIL import Image

STOP = set("a an and the of with on in at to for from by into its his her their small big "
           "round single two three full each other some made".split())
GRAPHIC_RESOURCES = 8  # Adobe Stock category number


def subject(prompt):
    """The prompt without the house style that STYLE.md appends."""
    return re.split(r",\s*(flat vector|seamless decorative)", prompt)[0].strip()


def etsy_tags(tags, theme):
    out = []
    for t in tags + [f"{theme} clipart", "thai clipart", "digital download", "png bundle",
                     "commercial use", "transparent png", "thailand art"]:
        t = t.strip().lower()[:20].strip()
        if t and t not in out:
            out.append(t)
    return out[:13]


def main():
    slug = sys.argv[1]
    drop = pathlib.Path(sys.argv[2] if len(sys.argv) > 2 else ".art-drop")
    drop = drop / "drops" / slug if (drop / "drops" / slug).is_dir() else drop  # or the image folder itself
    job = json.loads(pathlib.Path(f"art/{slug}/job.json").read_text(encoding="utf-8"))
    text = pathlib.Path(f"art/{slug}/LISTING.md").read_text(encoding="utf-8")
    f = dict(re.findall(r"^(\w+):\s*(.*)$", text, re.M))
    desc = "\n".join(l.strip() for l in text.split("description: |", 1)[1].splitlines() if l.strip())
    tags = [t.strip() for t in f.get("tags", "").split(",") if t.strip()]
    theme = slug.rsplit("-", 1)[0].replace("-", " ")
    rej_file = pathlib.Path(f"art/{slug}/rejects.txt")
    rejects = set(rej_file.read_text().split()) if rej_file.exists() else set()
    prompts = {p["name"]: p["prompt"] for p in job["prompts"]}
    out = pathlib.Path("dist")

    etsy = out / f"{slug}-etsy"
    etsy.mkdir(parents=True, exist_ok=True)
    for name in (f"{slug}.zip", f"{slug}-cover.png", f"{slug}-thumb.png"):
        shutil.copy(out / name, etsy / name)
    big = (etsy / f"{slug}.zip").stat().st_size > 20e6
    (etsy / "ETSY.txt").write_text(
        f"TITLE (max 140)\n{f['title'][:140]}\n\n"
        f"PRICE\n{f['price_usd']} USD\n\n"
        f"TAGS (13)\n{', '.join(etsy_tags(tags, theme))}\n\n"
        "TYPE: Digital files. Who made it: I did. What is it: A finished product.\n"
        "Created with AI: yes (tick the AI box; choose 'Designed by').\n"
        + ("NOTE: the zip is over Etsy's 20 MB file limit; upload it in two parts.\n" if big else "")
        + f"\nDESCRIPTION\n{desc}\n\nThe preview images are the cover and thumbnail in this folder.\n",
        encoding="utf-8")

    adobe = out / f"{slug}-adobe"
    adobe.mkdir(parents=True, exist_ok=True)
    rows = []
    for p in sorted(drop.glob("*.png")):
        if p.stem in rejects:
            continue
        base = p.stem.rsplit("-", 1)[0]
        subj = subject(prompts.get(base, base.replace("-", " ")))
        kind = "seamless pattern" if job.get("kind") == "pattern" else "illustration isolated on white background"
        title = f"{subj[0].upper()}{subj[1:]}, Thai {theme} {kind}"[:200]
        words = [w for w in re.findall(r"[a-z]+", subj.lower()) if w not in STOP and len(w) > 2]
        keys = []
        for k in words + [t for t in tags if "png" not in t and "clipart" not in t] + ["thailand", "thai", "asian", "illustration", "flat", "cute",
                                 "festival", "culture", "decoration", "design element"]:
            if k not in keys:
                keys.append(k)
        img = Image.open(p).convert("RGB").resize((2048, 2048), Image.LANCZOS)  # Adobe needs 4 MP+
        name = f"{p.stem}.jpg"
        img.save(adobe / name, "JPEG", quality=95)
        rows.append([name, title, ", ".join(keys[:49]), GRAPHIC_RESOURCES, ""])
    with open(adobe / "adobe_stock.csv", "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["Filename", "Title", "Keywords", "Category", "Releases"])
        w.writerows(rows)
    print(json.dumps({"slug": slug, "etsy": str(etsy), "adobe": str(adobe), "adobe_images": len(rows)}))


if __name__ == "__main__":
    main()
