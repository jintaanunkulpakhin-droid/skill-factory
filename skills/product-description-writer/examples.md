# Test prompts (used by the automatic self-test)

## 1. Supplier spec dump for Shopee
"Stainless steel tumbler 600ml, double wall vacuum, keeps cold 24h hot 12h,
lid with straw, colors: black white pink, BPA free lid"
Expected: title under 120 characters; benefits from the given numbers only;
no invented warranty or certification beyond "BPA free lid"; variants line per colour.

## 2. Etsy handmade item with health claim in notes ("lavender candle helps anxiety")
Expected: the anxiety claim softened to a neutral benefit (e.g. a calm
evening atmosphere), 13 tags of at most 20 characters, `[wax type]` if not given.

## 3. Thai input, "Thai and English"
Expected: Thai block first, then English, same facts in both.
