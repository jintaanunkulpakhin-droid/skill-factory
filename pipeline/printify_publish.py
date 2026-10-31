#!/usr/bin/env python3
"""Put one art bundle on Printify products. Usage: printify_publish.py <slug> [--count N]
Run art_package.py <slug> first. Takes the first N (default 2) images from
dist/<slug>.zip and makes a mug and a tote bag from each in the first Printify
shop (the Pop-Up Store, or Etsy once connected), priced at cost x 1.6, then
publishes. Needs PRINTIFY_API_TOKEN. Prints JSON with the product ids.
"""
import base64, json, os, pathlib, re, sys, urllib.request, zipfile

API = "https://api.printify.com/v1"
TOKEN = os.environ.get("PRINTIFY_API_TOKEN") or sys.exit("PRINTIFY_API_TOKEN not set")
PRODUCTS = [("mug", re.compile(r"\bmug\b.*11\s*oz|11\s*oz.*\bmug\b", re.I)),
            ("tote bag", re.compile(r"\btote bag\b", re.I))]
MARKUP = 1.6


def call(method, path, body=None, fatal=True):
    req = urllib.request.Request(API + path, method=method,
                                 data=json.dumps(body).encode() if body is not None else None,
                                 headers={"Authorization": "Bearer " + TOKEN, "User-Agent": "skill-factory",
                                          "Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=120) as r:
            raw = r.read()
            return json.loads(raw) if raw.strip() else {}
    except urllib.error.HTTPError as e:
        msg = f"{method} {path} failed: HTTP {e.code} {e.read()[:300]!r}"
        if fatal:
            sys.exit(msg)
        return {"error": msg}


def blueprint(pattern):
    """First catalog blueprint whose title matches, with its first print provider."""
    for bp in call("GET", "/catalog/blueprints.json"):
        if pattern.search(bp["title"]):
            providers = call("GET", f"/catalog/blueprints/{bp['id']}/print_providers.json")
            if providers:
                return bp, providers[0]
    sys.exit(f"no blueprint matches {pattern.pattern}")


def price(cost):
    """Cost x markup, ending in .99."""
    return max(int(cost * MARKUP / 100) * 100 + 99, cost + 300)


def main():
    slug = sys.argv[1]
    count = int(sys.argv[sys.argv.index("--count") + 1]) if "--count" in sys.argv else 2
    text = pathlib.Path(f"art/{slug}/LISTING.md").read_text(encoding="utf-8")
    f = dict(re.findall(r"^(\w+):\s*(.*)$", text, re.M))
    theme = re.sub(r"\s*\|.*$", "", f["title"]).replace("Clip Art", "").strip()
    tags = [t.strip() for t in f.get("tags", "").split(",") if t.strip()][:10]
    shop = call("GET", "/shops.json")[0]["id"]
    with zipfile.ZipFile(f"dist/{slug}.zip") as z:
        images = [n for n in z.namelist() if n.endswith((".png", ".jpg"))][:count]
        uploads = [call("POST", "/uploads/images.json", {
            "file_name": n, "contents": base64.b64encode(z.read(n)).decode()})["id"] for n in images]
    made = []
    for kind, pattern in PRODUCTS:
        bp, prov = blueprint(pattern)
        variants = call("GET", f"/catalog/blueprints/{bp['id']}/print_providers/{prov['id']}/variants.json")["variants"][:10]
        ids = [v["id"] for v in variants]
        for i, image_id in enumerate(uploads, 1):
            title = f"{theme} {kind.title()}, Thai Design {i}"
            prod = call("POST", f"/shops/{shop}/products.json", {
                "title": title, "tags": tags,
                "description": f"<p>{theme} artwork printed on a {kind}. Thai-inspired design, "
                               f"made with AI image generation and checked by hand.</p>",
                "blueprint_id": bp["id"], "print_provider_id": prov["id"],
                "variants": [{"id": v, "price": 2000, "is_enabled": True} for v in ids],
                "print_areas": [{"variant_ids": ids, "placeholders": [{"position": "front", "images": [
                    {"id": image_id, "x": 0.5, "y": 0.5, "scale": 1, "angle": 0}]}]}]})
            full = call("GET", f"/shops/{shop}/products/{prod['id']}.json")
            call("PUT", f"/shops/{shop}/products/{prod['id']}.json", {"variants": [
                {"id": v["id"], "price": price(v["cost"]), "is_enabled": True}
                for v in full["variants"] if v["id"] in ids]})
            # Pop-Up Store products are live once created; publish pushes to Etsy/Shopify if connected.
            pub = call("POST", f"/shops/{shop}/products/{prod['id']}/publish.json", {
                "title": True, "description": True, "images": True, "variants": True, "tags": True,
                "keyFeatures": True, "shipping_template": True}, fatal=False)
            made.append({"id": prod["id"], "title": title, "publish_error": pub.get("error")})
    print(json.dumps({"slug": slug, "shop": shop, "products": made}))


if __name__ == "__main__":
    main()
