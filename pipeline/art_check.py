#!/usr/bin/env python3
"""Automatic gate for one art drop. Usage: art_check.py <slug> [drop_dir]

Flags images that are unreadable, the wrong size, nearly blank, colour noise, or near
duplicates of an earlier image (16x16 average hash). Appends flagged names to
art/<slug>/rejects.txt and prints how many remain. FAIL if fewer than
job["min_keep"] (default 12) are left. The visual review in ROUTINE_PROMPT.md
adds its own rejects to the same file afterwards.
"""
import json, pathlib, sys
import numpy as np
from PIL import Image, ImageStat


def ahash(img):
    px = np.asarray(img.convert("L").resize((16, 16)), dtype=float).ravel()
    return int("".join("1" if v > px.mean() else "0" for v in px), 2)


def main():
    slug = sys.argv[1]
    drop = pathlib.Path(sys.argv[2] if len(sys.argv) > 2 else ".art-drop")
    drop = drop / "drops" / slug if (drop / "drops" / slug).is_dir() else drop  # or the image folder itself
    job = json.loads(pathlib.Path(f"art/{slug}/job.json").read_text(encoding="utf-8"))
    rej_file = pathlib.Path(f"art/{slug}/rejects.txt")
    rejects = set(rej_file.read_text().split()) if rej_file.exists() else set()
    want = (job.get("width", 1024), job.get("height", 1024))
    seen, flagged, kept = [], [], 0
    for p in sorted(drop.glob("*.png")):
        if p.stem in rejects:
            continue
        try:
            img = Image.open(p)
            img.load()
        except Exception:
            flagged.append((p.stem, "unreadable")); continue
        if img.size != want:
            flagged.append((p.stem, f"size {img.size}")); continue
        if max(ImageStat.Stat(img.convert("L")).stddev) < 8:
            flagged.append((p.stem, "blank")); continue
        a = np.asarray(img.convert("RGB"), dtype=float)
        if np.abs(np.diff(a, axis=1)).mean() > 45:  # AMD/ROCm colour noise on the PC
            flagged.append((p.stem, "noise")); continue
        h = ahash(img)
        if any(bin(h ^ o).count("1") <= 12 for o in seen):
            flagged.append((p.stem, "duplicate")); continue
        seen.append(h)
        kept += 1
    if flagged:
        with rej_file.open("a", encoding="utf-8") as f:
            f.writelines(f"{name}\n" for name, _ in flagged)
    for name, why in flagged:
        print("reject", name, why)
    need = job.get("min_keep", 12)
    print(("PASS" if kept >= need else "FAIL") + f": {kept} kept, need {need}")
    sys.exit(0 if kept >= need else 1)


if __name__ == "__main__":
    main()
