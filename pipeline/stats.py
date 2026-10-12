#!/usr/bin/env python3
"""Print a Markdown table of sales per Gumroad product. Usage: stats.py
Page views are not offered by the Gumroad API; see Analytics in the Gumroad dashboard.
"""
import json, os, sys, urllib.request

TOKEN = os.environ.get("GUMROAD_ACCESS_TOKEN") or sys.exit("GUMROAD_ACCESS_TOKEN not set")
req = urllib.request.Request("https://api.gumroad.com/v2/products",
                             headers={"Authorization": "Bearer " + TOKEN})
products = json.load(urllib.request.urlopen(req, timeout=60))["products"]
rows = sorted(products, key=lambda p: (-(p.get("sales_count") or 0), p["name"]))
print("| Product | Live | Price | Sales | Revenue |")
print("|---|---|---|---|---|")
for p in rows:
    name = p["name"].replace(" (Skill for Claude)", "")
    print(f"| [{name}]({p.get('short_url')}) | {'yes' if p.get('published') else 'no'} | "
          f"{p.get('formatted_price')} | {p.get('sales_count') or 0} | ${(p.get('sales_usd_cents') or 0) / 100:.2f} |")
total = sum((p.get("sales_usd_cents") or 0) for p in products) / 100
print(f"\nTotal: {sum(p.get('sales_count') or 0 for p in products)} sales, ${total:.2f}")
