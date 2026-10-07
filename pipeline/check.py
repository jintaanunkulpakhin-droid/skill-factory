#!/usr/bin/env python3
"""Automatic gate for a skill folder. Usage: check.py skills/<slug>"""
import re, sys, pathlib

def fail(msg):
    print("FAIL:", msg); sys.exit(1)

d = pathlib.Path(sys.argv[1])
p = d / "SKILL.md"
if not p.exists(): fail("missing SKILL.md")
text = p.read_text(encoding="utf-8")
m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
if not m: fail("no frontmatter")
front, body = m.groups()
fields = dict(re.findall(r"^(\w+):\s*(.+)$", front, re.M))
name, desc = fields.get("name", ""), fields.get("description", "")
if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", name) or len(name) > 64: fail("bad name")
if name != d.name: fail("name must match folder")
if not desc or len(desc) > 1024 or "<" in desc or ">" in desc: fail("bad description")
if any(w in name for w in ("claude", "anthropic")): fail("reserved word in name")
if len(body.splitlines()) > 500: fail("body over 500 lines")
for f in ("examples.md", "LISTING.md"):
    if not (d / f).exists(): fail(f"missing {f}")
print("PASS:", name)
