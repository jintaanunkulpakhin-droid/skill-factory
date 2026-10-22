#!/usr/bin/env python3
"""Package one art drop. Usage: art_package.py <slug> [drop_dir]

Reads art/<slug>/job.json and LISTING.md, the images in <drop_dir>/drops/<slug>/
(default .art-drop, a worktree of the art-drop branch), skips names listed in
art/<slug>/rejects.txt, and writes:
  dist/<slug>.zip          finished files + LICENSE.txt
  dist/<slug>-cover.png    1280x720 preview grid
  dist/<slug>-thumb.png    600x600 preview
kind "clipart": white background made transparent, trimmed, PNG.
kind "pattern": mirrored 2x2 so the tile is seamless, 2048px JPG.
"""
import json, pathlib, re, sys, zipfile
import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont, ImageOps

INK, PAPER, ACCENT = "#14161A", "#F7F1E3", "#B8860B"
FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
LICENSE = """License: personal and commercial use

You may use these images in your own projects, printed or digital, including
products you sell (cards, invitations, classroom sheets, social posts, packaging).
You may not resell or share the image files themselves, alone or in a bundle,
or claim them as your own artwork.

These images were made with the help of AI image generation and reviewed by hand.
"""


def clipart(img):
    """Flood-fill the near-white background from the edges, make it transparent, trim."""
    rgb = img.convert("RGB")
    w, h = rgb.size
    key = (255, 0, 255)
    for xy in ((0, 0), (w - 1, 0), (0, h - 1), (w - 1, h - 1), (w // 2, 0), (w // 2, h - 1)):
        if min(rgb.getpixel(xy)) > 225:
            ImageDraw.floodfill(rgb, xy, key, thresh=40)
    bg = (np.asarray(rgb) == key).all(axis=2)
    alpha = Image.fromarray(np.where(bg, 0, 255).astype("uint8"), "L")
    alpha = alpha.filter(ImageFilter.MinFilter(3))  # drop the light halo at the edge
    out = img.convert("RGBA")
    out.putalpha(alpha)
    box = alpha.getbbox()
    return out.crop(box) if box else out


def pattern(img):
    """Mirror into a 2x2 tile: always seamless, at double size."""
    img = img.convert("RGB")
    w, h = img.size
    tile = Image.new("RGB", (w * 2, h * 2))
    tile.paste(img, (0, 0))
    tile.paste(ImageOps.mirror(img), (w, 0))
    tile.paste(ImageOps.flip(img), (0, h))
    tile.paste(ImageOps.flip(ImageOps.mirror(img)), (w, h))
    return tile


def preview(images, size, title):
    """Grid of images on paper with a title band at the bottom."""
    W, H = size
    band = int(H * 0.2)
    canvas = Image.new("RGB", (W, H), PAPER)
    cols = 4 if W > H else 3
    rows = 2 if W > H else 2
    cw, ch = W // cols, (H - band) // rows
    for i, im in enumerate(images[: cols * rows]):
        t = im.copy()
        t.thumbnail((cw - 16, ch - 16))
        x = (i % cols) * cw + (cw - t.width) // 2
        y = (i // cols) * ch + (ch - t.height) // 2
        canvas.paste(t, (x, y), t if t.mode == "RGBA" else None)
    d = ImageDraw.Draw(canvas)
    d.rectangle([0, H - band, W, H], fill=INK)
    size_px = int(band * 0.38)
    fnt = ImageFont.truetype(FONT, size_px)
    while d.textlength(title, font=fnt) > W - 64 and size_px > 14:
        size_px -= 2
        fnt = ImageFont.truetype(FONT, size_px)
    d.text((32, H - band + (band - size_px) // 2), title, font=fnt, fill=PAPER)
    return canvas


def main():
    slug = sys.argv[1]
    drop = pathlib.Path(sys.argv[2] if len(sys.argv) > 2 else ".art-drop")
    drop = drop / "drops" / slug if (drop / "drops" / slug).is_dir() else drop  # or the image folder itself
    job = json.loads(pathlib.Path(f"art/{slug}/job.json").read_text(encoding="utf-8"))
    text = pathlib.Path(f"art/{slug}/LISTING.md").read_text(encoding="utf-8")
    title = dict(re.findall(r"^(\w+):\s*(.*)$", text, re.M))["title"]
    rej_file = pathlib.Path(f"art/{slug}/rejects.txt")
    rejects = set(rej_file.read_text().split()) if rej_file.exists() else set()
    files = sorted(p for p in drop.glob("*.png") if p.stem not in rejects and p.name not in rejects)
    if not files:
        sys.exit(f"no images in {drop}")
    out = pathlib.Path("dist")
    out.mkdir(exist_ok=True)
    done = []
    with zipfile.ZipFile(out / f"{slug}.zip", "w", zipfile.ZIP_DEFLATED) as z:
        for i, p in enumerate(files, 1):
            img = Image.open(p)
            if job.get("kind") == "pattern":
                img = pattern(img)
                name, data = f"{slug}-{i:02d}.jpg", "JPEG"
            else:
                img = clipart(img)
                name, data = f"{slug}-{i:02d}.png", "PNG"
            tmp = out / name
            img.save(tmp, data, quality=92) if data == "JPEG" else img.save(tmp, data, optimize=True)
            z.write(tmp, name)
            tmp.unlink()
            done.append(img)
        z.writestr("LICENSE.txt", LICENSE)
    clean = re.sub(r"\s*\|.*$", "", title)
    preview(done, (1280, 720), clean).save(out / f"{slug}-cover.png")
    preview(done, (600, 600), f"{len(done)} files").save(out / f"{slug}-thumb.png")
    mb = (out / f"{slug}.zip").stat().st_size / 1e6
    print(json.dumps({"slug": slug, "images": len(done), "zip_mb": round(mb, 1)}))


if __name__ == "__main__":
    main()
