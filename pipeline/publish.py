#!/usr/bin/env python3
"""Publish one skill to Gumroad. Usage: publish.py <slug> [--product-id ID] [--draft]
       publish.py --enable <product-id>   (publish an existing draft)
       publish.py --media <slug> <product-id>   (attach cover and thumbnail)
       publish.py --demo <slug> <product-id>    (attach only the demo image)
Run make_cover.py <slug> and make_demo.py <slug> first: products get
dist/<slug>-cover.png and -thumb.png, plus dist/<slug>-demo.png as a second
cover when it exists.

Reads skills/<slug>/LISTING.md (or bundles/<slug>/LISTING.md), uploads dist/<slug>.zip, attaches it to the
product (creating the product if no id is given) and publishes it.
Needs GUMROAD_ACCESS_TOKEN in the environment. Prints JSON: id, url, published.
Mirrors the upload flow of the official Gumroad CLI (presign, S3 PUT, complete).
"""
import base64, hashlib, html, json, os, pathlib, re, sys, urllib.parse, urllib.request, uuid

API = "https://api.gumroad.com/v2"
TOKEN = os.environ.get("GUMROAD_ACCESS_TOKEN") or sys.exit("GUMROAD_ACCESS_TOKEN not set")


def call(method, path, form=None, body=None, fatal=True):
    headers = {"Authorization": "Bearer " + TOKEN}
    data = None
    if body is not None:
        data, headers["Content-Type"] = json.dumps(body).encode(), "application/json"
    elif form is not None:
        data = urllib.parse.urlencode(form).encode()
        headers["Content-Type"] = "application/x-www-form-urlencoded"
    req = urllib.request.Request(API + path, data=data, method=method, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            out = json.load(r)
    except urllib.error.HTTPError as e:
        sys.exit(f"{method} {path} failed: HTTP {e.code} {e.read()[:300]!r}")
    if not out.get("success", True):
        if not fatal:
            return out
        sys.exit(f"{method} {path} failed: {str(out)[:300]}")
    return out


# Added to every product page: many buyers don't know what a skill is.
SKILL_EXPLAINER = (
    "<h3>What is a Claude Skill?</h3>"
    "<p>A skill is a small instruction file that teaches Claude to do one job the same good way "
    "every time. You install it once and then just ask normally. No prompt to copy each time, "
    "and no coding.</p>"
    "<p><strong>Install in about a minute:</strong> in Claude.ai or the Claude desktop app, turn on "
    "\"Code execution and file creation\" in Settings &gt; Capabilities, then upload the zip in "
    "Customize &gt; Skills. In Claude Code, unzip it into ~/.claude/skills/. "
    "Works on every Claude plan, including Free.</p>")


def listing_path(slug):
    for root in ("skills", "bundles"):
        p = pathlib.Path(f"{root}/{slug}/LISTING.md")
        if p.exists():
            return p
    sys.exit(f"no LISTING.md for {slug}")


def to_html(body):
    """Blank-line separated paragraphs; lines starting with "- " become a list."""
    out = []
    for para in re.split(r"\n\s*\n", body.strip()):
        lines = [l.strip() for l in para.splitlines() if l.strip()]
        head, items = [], []
        for l in lines:
            if l.startswith("- "):
                items.append(l[2:])
            elif items:
                items[-1] += " " + l
            else:
                head.append(l)
        if head:
            out.append("<p>" + html.escape(" ".join(head)) + "</p>")
        if items:
            out.append("<ul>" + "".join("<li>" + html.escape(i) + "</li>" for i in items) + "</ul>")
    return "".join(out)


def listing(slug):
    """Returns name, price in cents, HTML description, tags and extra create fields."""
    text = listing_path(slug).read_text(encoding="utf-8")
    fields = dict(re.findall(r"^(\w+):\s*(.*)$", text, re.M))
    desc = to_html(text.split("description: |", 1)[1]) + SKILL_EXPLAINER
    tags = [t.strip() for t in fields.get("tags", "").split(",") if t.strip()]
    extra = {}
    if fields.get("suggested_price_usd"):  # pay what you want, from price_usd up
        extra = {"customizable_price": "true",
                 "suggested_price_cents": int(float(fields["suggested_price_usd"]) * 100)}
    return fields["title"], int(float(fields["price_usd"]) * 100), desc, tags, extra


def upload(path):
    size = path.stat().st_size
    pre = call("POST", "/files/presign", form={"filename": path.name, "file_size": size})
    if len(pre.get("parts", [])) != 1:
        sys.exit("expected a single upload part for a small zip")
    part = pre["parts"][0]
    req = urllib.request.Request(part["presigned_url"], data=path.read_bytes(), method="PUT")
    with urllib.request.urlopen(req, timeout=120) as r:
        etag = r.headers.get("ETag", "").strip('"')
    if not etag:
        sys.exit("upload returned no ETag")
    done = call("POST", "/files/complete", body={
        "upload_id": pre["upload_id"], "key": pre["key"],
        "parts": [{"part_number": part["part_number"], "etag": etag}]})
    return done["file_url"]


def add_media(pid, slug, demo_only=False):
    """Attach dist/<slug>-cover.png as cover, dist/<slug>-thumb.png as thumbnail
    and dist/<slug>-demo.png (if present) as a second cover."""
    base = "/products/" + urllib.parse.quote(pid, safe="")
    media = [] if demo_only else [("covers", f"dist/{slug}-cover.png"), ("thumbnail", f"dist/{slug}-thumb.png")]
    if pathlib.Path(f"dist/{slug}-demo.png").exists():
        media.append(("covers", f"dist/{slug}-demo.png"))
    for kind, path in media:
        data = pathlib.Path(path).read_bytes()
        md5 = base64.b64encode(hashlib.md5(data).digest()).decode()
        blob = call("POST", "/direct_uploads", form={
            "purpose": "media", "blob[filename]": pathlib.Path(path).name, "blob[byte_size]": len(data),
            "blob[checksum]": md5, "blob[content_type]": "image/png"})
        headers = dict(blob["direct_upload"].get("headers") or {})
        headers.setdefault("Content-Type", "image/png"); headers.setdefault("Content-MD5", md5)
        req = urllib.request.Request(blob["direct_upload"]["url"], data=data, method="PUT", headers=headers)
        urllib.request.urlopen(req, timeout=120).close()
        call("POST", f"{base}/{kind}", form={"signed_blob_id": blob["signed_id"]})


def main():
    if sys.argv[1] == "--media":
        add_media(sys.argv[3], sys.argv[2]); print("media added"); return
    if sys.argv[1] == "--demo":
        add_media(sys.argv[3], sys.argv[2], demo_only=True); print("demo added"); return
    if sys.argv[1] == "--enable":
        prod = call("PUT", "/products/" + urllib.parse.quote(sys.argv[2], safe="") + "/enable")["product"]
        print(json.dumps({"id": sys.argv[2], "url": prod.get("short_url"), "published": prod.get("published")}))
        return
    slug = sys.argv[1]
    pid = sys.argv[sys.argv.index("--product-id") + 1] if "--product-id" in sys.argv else None
    name, price, desc, tags, extra = listing(slug)
    if not pid:
        pid = call("POST", "/products", form={"name": name, "price": price, "description": desc, **extra})["product"]["id"]
    file_url = upload(pathlib.Path(f"dist/{slug}.zip"))
    file_id = "cli-upload-" + str(uuid.uuid4())
    rich = [{"title": "Page 1", "description": {"type": "doc", "content": [
        {"type": "fileEmbed", "attrs": {"id": file_id, "uid": str(uuid.uuid4()), "collapsed": False}},
        {"type": "paragraph"}]}}]
    call("PUT", "/products/" + urllib.parse.quote(pid, safe=""), body={
        "description": desc, "tags": tags, "rich_content": rich,
        "files": [{"external_id": file_id, "url": file_url, "display_name": f"{slug}.zip"}]})
    add_media(pid, slug)
    path = "/products/" + urllib.parse.quote(pid, safe="")
    note = None
    if "--draft" not in sys.argv:
        res = call("PUT", path + "/enable", fatal=False)
        note = res.get("message") if not res.get("success", True) else None
    prod = call("GET", path)["product"]
    print(json.dumps({"id": pid, "url": prod.get("short_url"), "published": prod.get("published"),
                      "files": len(prod.get("files") or []), "note": note}))


if __name__ == "__main__":
    main()
