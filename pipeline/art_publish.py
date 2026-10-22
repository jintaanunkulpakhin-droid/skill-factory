#!/usr/bin/env python3
"""Publish one art bundle to Gumroad. Usage: art_publish.py <slug> [--draft]
Run art_package.py <slug> first (dist/<slug>.zip, -cover.png, -thumb.png).

Same upload flow as publish.py (shared helpers), but reads art/<slug>/LISTING.md
and adds the art notes instead of the skill explainer.
Prints JSON: id, url, published, files, note.
"""
import html, json, pathlib, re, sys, urllib.parse, uuid

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import publish as P  # noqa: E402  (needs GUMROAD_ACCESS_TOKEN)

ART_NOTES = (
    "<h3>What you get</h3>"
    "<p>A ZIP of high-resolution files (transparent PNG clip art or seamless JPG pattern tiles) "
    "and LICENSE.txt. Instant download.</p>"
    "<p><strong>License:</strong> personal and commercial use in your own designs and products. "
    "Please don't resell or share the files themselves.</p>"
    "<p><em>Made with AI image generation, then checked and cleaned up by hand.</em></p>")


def listing(slug):
    text = pathlib.Path(f"art/{slug}/LISTING.md").read_text(encoding="utf-8")
    fields = dict(re.findall(r"^(\w+):\s*(.*)$", text, re.M))
    body = " ".join(l.strip() for l in text.split("description: |", 1)[1].splitlines() if l.strip())
    tags = [t.strip() for t in fields.get("tags", "").split(",") if t.strip()]
    return fields["title"], int(float(fields["price_usd"]) * 100), "<p>" + html.escape(body) + "</p>" + ART_NOTES, tags


def main():
    slug = sys.argv[1]
    name, price, desc, tags = listing(slug)
    pid = P.call("POST", "/products", form={"name": name, "price": price, "description": desc})["product"]["id"]
    file_url = P.upload(pathlib.Path(f"dist/{slug}.zip"))
    file_id = "cli-upload-" + str(uuid.uuid4())
    rich = [{"title": "Page 1", "description": {"type": "doc", "content": [
        {"type": "fileEmbed", "attrs": {"id": file_id, "uid": str(uuid.uuid4()), "collapsed": False}},
        {"type": "paragraph"}]}}]
    path = "/products/" + urllib.parse.quote(pid, safe="")
    P.call("PUT", path, body={
        "description": desc, "tags": tags, "rich_content": rich,
        "files": [{"external_id": file_id, "url": file_url, "display_name": f"{slug}.zip"}]})
    P.add_media(pid, slug)
    note = None
    if "--draft" not in sys.argv:
        res = P.call("PUT", path + "/enable", fatal=False)
        note = res.get("message") if not res.get("success", True) else None
    prod = P.call("GET", path)["product"]
    print(json.dumps({"id": pid, "url": prod.get("short_url"), "published": prod.get("published"),
                      "files": len(prod.get("files") or []), "note": note}))


if __name__ == "__main__":
    main()
