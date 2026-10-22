#!/usr/bin/env python3
"""Draw a before/after demo image for a skill. Usage: make_demo.py <slug>

Reads skills/<slug>/demo.json ({"title", "input", "output": [lines]}): test
prompt 1 on the left, the skill's (shortened) answer on the right. Writes
dist/<slug>-demo.png (1280x720, a second store image) and dist/<slug>-demo.gif
(answer appears line by line, for social posts).
Output line prefixes: "# " heading, "* " bold, "- " bullet, "| " table row
(cells split by "|"), else plain.
"""
import hashlib, json, pathlib, sys
from PIL import Image, ImageDraw, ImageFont

INTER = "/usr/share/fonts/opentype/inter/Inter-{}.otf"
MONO = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"
PALETTE = ["#2F5BEA", "#0E8A6A", "#C2410C", "#7C3AED", "#BE185D", "#0369A1", "#4D7C0F", "#B45309"]
INK, PAPER, MUTED, CARD, LINE = "#14161A", "#F7F5F0", "#6B7079", "#FFFFFF", "#E2DED5"
W, H = 1280, 720
LEFT = (48, 120, 500, 672)
RIGHT = (532, 120, 1232, 672)


def f(weight, size):
    return ImageFont.truetype(INTER.format(weight), size)


def wrap(d, text, fnt, width):
    lines, line = [], ""
    for word in text.split(" "):
        trial = (line + " " + word).strip(" ")
        if d.textlength(trial, font=fnt) <= width:
            line = trial
        else:
            if line:
                lines.append(line)
            line = word
    return lines + [line]


def card(d, box, label, accent):
    d.rounded_rectangle(box, 18, fill=CARD, outline=LINE, width=2)
    d.text((box[0] + 24, box[1] + 20), label, font=f("SemiBold", 18), fill=accent)


def base(s, accent):
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, W, 10], fill=accent)
    d.text((48, 40), s["title"], font=f("Bold", 40), fill=INK)
    d.text((W - 48, 52), "sample run, output shortened", font=f("Medium", 20), fill=MUTED, anchor="ra")
    card(d, LEFT, "YOU PASTE", MUTED)
    card(d, RIGHT, "CLAUDE RETURNS (WITH THE SKILL)", accent)
    mono = ImageFont.truetype(MONO, 17)
    y = LEFT[1] + 60
    for para in s["input"].split("\n"):
        for l in wrap(d, para, mono, LEFT[2] - LEFT[0] - 48):
            if y > LEFT[3] - 30:
                break
            d.text((LEFT[0] + 24, y), l, font=mono, fill="#3A3F47")
            y += 25
    return img, d


def out_rows(d, s, accent):
    """Pre-layout the output: list of (draw_fn, height)."""
    width = RIGHT[2] - RIGHT[0] - 48
    rows = []
    for raw in s["output"]:
        if raw.startswith("# "):
            fnt, fill, text, ind = f("Bold", 22), INK, raw[2:], 0
        elif raw.startswith("* "):
            fnt, fill, text, ind = f("SemiBold", 18), accent, raw[2:], 0
        elif raw.startswith("- "):
            fnt, fill, text, ind = f("Regular", 18), INK, "•  " + raw[2:], 0
        elif raw.startswith("| "):
            fnt, fill, text, ind = f("Regular", 17), INK, raw[2:], 0
        elif raw == "":
            rows.append((None, 10)); continue
        else:
            fnt, fill, text, ind = f("Regular", 18), INK, raw, 0
        if raw.startswith("| "):
            cells = [c.strip() for c in text.split("|")]
            rows.append((("table", cells, fnt), 28))
            continue
        for i, l in enumerate(wrap(d, text, fnt, width - (22 if raw.startswith("- ") else 0))):
            rows.append((("text", ("    " + l) if (i and raw.startswith("- ")) else l, fnt, fill), fnt.size + 9))
    return rows


def draw_rows(d, rows, n, accent):
    y = RIGHT[1] + 60
    x = RIGHT[0] + 24
    for row, h in rows[:n]:
        if y + h > RIGHT[3] - 16:
            break
        if row and row[0] == "text":
            d.text((x, y), row[1], font=row[2], fill=row[3])
        elif row and row[0] == "table":
            cols = [x, x + 300, x + 560]
            for c, cell in zip(cols, row[1]):
                fill = {"Strong": "#0E8A6A", "Partial": "#B45309", "Missing": "#BE185D"}.get(cell, INK)
                d.text((c, y), cell, font=row[2], fill=fill)
            d.line([x, y + h - 4, RIGHT[2] - 24, y + h - 4], fill=LINE)
        y += h


def main():
    slug = sys.argv[1]
    s = json.loads(pathlib.Path(f"skills/{slug}/demo.json").read_text(encoding="utf-8"))
    out = pathlib.Path("dist"); out.mkdir(exist_ok=True)
    accent = PALETTE[int(hashlib.md5(slug.encode()).hexdigest(), 16) % len(PALETTE)]
    img, d = base(s, accent)
    rows = out_rows(d, s, accent)
    full = img.copy(); draw_rows(ImageDraw.Draw(full), rows, len(rows), accent)
    full.save(out / f"{slug}-demo.png")
    frames, durations = [img.copy()], [1800]
    for n in range(1, len(rows) + 1):
        fr = img.copy(); draw_rows(ImageDraw.Draw(fr), rows, n, accent)
        frames.append(fr); durations.append(180)
    durations[-1] = 4000
    pal = [fr.convert("P", palette=Image.ADAPTIVE, colors=64) for fr in frames]
    pal[0].save(out / f"{slug}-demo.gif", save_all=True, append_images=pal[1:],
                duration=durations, loop=0, optimize=True)
    print(out / f"{slug}-demo.png", out / f"{slug}-demo.gif")


if __name__ == "__main__":
    main()
