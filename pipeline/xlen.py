#!/usr/bin/env python3
"""Print the X character count of a post (each link counts as 23). Usage: xlen.py "<text>"
Exits 1 if over 280."""
import re, sys
n = len(re.sub(r"https?://\S+", "x" * 23, sys.argv[1]))
print(n)
sys.exit(0 if n <= 280 else 1)
