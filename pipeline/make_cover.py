#!/usr/bin/env python3
"""Draw store images for a skill. Usage: make_cover.py <slug>

Writes dist/<slug>-cover.png (1280x720) and dist/<slug>-thumb.png (600x600)
from the title and hook in skills/<slug>/LISTING.md (or bundles/<slug>/).
"""
import hashlib, pathlib, re, sys
from PIL import Image, ImageDraw, ImageFont

FONT_DIR = "/usr/share/fonts/opentype/inter/"
PALETTE = ["#2F5BEA", "#0E8A6A", "#C2410C", "#7C3AED", "#BE185D", "#0369A1", "#4D7C0F", "#B45309"]
INK, PAPER = "#14161A", "#F7F5F0"


def font(weight, size):
    for name in (f"Inter-{weight}.otf", f"InterDisplay-{weight}.otf"):
        p = pathlib.Path(FONT_DIR) / name
        if p.exists():
            return ImageFont.truetype(str(p), size)
    return ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", size)


def wrap(draw, text, fnt, width):
    lines, line = [], ""
    for word in text.split():
        trial = (line + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= width:
            line = trial
        else:
            lines.append(line)
            line = word
    return lines + [line] if line else lines


def block(draw, x, y, lines, fnt, fill, gap):
    for l in lines:
        draw.text((x, y), l, font=fnt, fill=fill)
        y += fnt.size + gap
    return y


def listing(slug):
    path = pathlib.Path(f"skills/{slug}/LISTING.md")
    if not path.exists():
        path = pathlib.Path(f"bundles/{slug}/LISTING.md")
    text = path.read_text(encoding="utf-8")
    f = dict(re.findall(r"^(\w+):\s*(.*)$", text, re.M))
    title = re.sub(r"\s*\(Skill for Claude\)\s*$", "", f["title"])
    return title, f.get("hook", ""), f.get("price_usd", "")


def main():
    slug = sys.argv[1]
    title, hook, price = listing(slug)
    accent = PALETTE[int(hashlib.md5(slug.encode()).hexdigest(), 16) % len(PALETTE)]
    out = pathlib.Path("dist"); out.mkdir(exist_ok=True)

    # Cover 1280x720: accent band on the left, title and hook on paper.
    img = Image.new("RGB", (1280, 720), PAPER); d = ImageDraw.Draw(img)
    d.rectangle([0, 0, 28, 720], fill=accent)
    d.text((96, 88), "SKILL FOR CLAUDE", font=font("SemiBold", 28), fill=accent)
    tf = font("Bold", 84)
    y = block(d, 96, 150, wrap(d, title, tf, 1080), tf, INK, 10)
    hf = font("Regular", 36)
    block(d, 96, y + 36, wrap(d, hook, hf, 1000)[:4], hf, "#454A52", 14)
    d.text((96, 620), "Drop-in SKILL.md  ·  Claude.ai, desktop app, Claude Code", font=font("Medium", 26), fill="#6B7079")
    img.save(out / f"{slug}-cover.png")

    # Thumbnail 600x600: solid accent, title in white.
    th = Image.new("RGB", (600, 600), accent); d = ImageDraw.Draw(th)
    d.text((48, 52), "SKILL FOR CLAUDE", font=font("SemiBold", 24), fill="#FFFFFFCC")
    tf = font("Bold", 64)
    lines = wrap(d, title, tf, 504)
    while len(lines) > 4:
        tf = font("Bold", tf.size - 6); lines = wrap(d, title, tf, 504)
    block(d, 48, 130, lines, tf, "#FFFFFF", 8)
    th.save(out / f"{slug}-thumb.png")
    print(out / f"{slug}-cover.png", out / f"{slug}-thumb.png")


if __name__ == "__main__":
    main()
