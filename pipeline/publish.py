#!/usr/bin/env python3
"""Publish one skill to Gumroad. Usage: publish.py <slug> [--product-id ID] [--draft]
       publish.py --enable <product-id>   (publish an existing draft)

Reads skills/<slug>/LISTING.md, uploads dist/<slug>.zip, attaches it to the
product (creating the product if no id is given) and publishes it.
Needs GUMROAD_ACCESS_TOKEN in the environment. Prints JSON: id, url, published.
Mirrors the upload flow of the official Gumroad CLI (presign, S3 PUT, complete).
"""
import json, os, pathlib, re, sys, urllib.parse, urllib.request, uuid

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


def listing(slug):
    text = pathlib.Path(f"skills/{slug}/LISTING.md").read_text(encoding="utf-8")
    fields = dict(re.findall(r"^(\w+):\s*(.*)$", text, re.M))
    desc = " ".join(l.strip() for l in text.split("description: |", 1)[1].splitlines() if l.strip())
    tags = [t.strip() for t in fields.get("tags", "").split(",") if t.strip()]
    return fields["title"], int(float(fields["price_usd"]) * 100), desc, tags


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


def main():
    if sys.argv[1] == "--enable":
        prod = call("PUT", "/products/" + urllib.parse.quote(sys.argv[2], safe="") + "/enable")["product"]
        print(json.dumps({"id": sys.argv[2], "url": prod.get("short_url"), "published": prod.get("published")}))
        return
    slug = sys.argv[1]
    pid = sys.argv[sys.argv.index("--product-id") + 1] if "--product-id" in sys.argv else None
    name, price, desc, tags = listing(slug)
    if not pid:
        pid = call("POST", "/products", form={"name": name, "price": price, "description": desc})["product"]["id"]
    file_url = upload(pathlib.Path(f"dist/{slug}.zip"))
    file_id = "cli-upload-" + str(uuid.uuid4())
    rich = [{"title": "Page 1", "description": {"type": "doc", "content": [
        {"type": "fileEmbed", "attrs": {"id": file_id, "uid": str(uuid.uuid4()), "collapsed": False}},
        {"type": "paragraph"}]}}]
    call("PUT", "/products/" + urllib.parse.quote(pid, safe=""), body={
        "tags": tags, "rich_content": rich,
        "files": [{"external_id": file_id, "url": file_url, "display_name": f"{slug}.zip"}]})
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
