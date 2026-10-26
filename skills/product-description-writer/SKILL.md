---
name: product-description-writer
description: Write e-commerce product titles, descriptions, bullet points and SEO tags from a product's specs, notes or a supplier sheet, for Shopify, Etsy, Amazon, Shopee, Lazada or a website. Use when someone pastes product details and asks for a product description, listing copy, product title, bullet points, marketplace listing, or "make this sell better".
---

# Product Description Writer

Turn raw product facts into listing copy that helps a shopper decide, without
making claims the seller can't back up.

## Inputs
Accept anything: a spec table, supplier text, bullet notes, an old listing,
or a photo description. Optional: platform, target buyer, brand voice,
price point, keywords to include, character limits, language.

Never ask a question before the first draft. Put unknown facts in
`[brackets]` (for example `[material]`, `[size]`).

## Honesty rules (never break)
- Use only facts given. Never invent materials, sizes, certifications,
  awards, origin, warranty, test results or reviews.
- No medical, health, safety or "best/#1" claims unless the seller provided
  proof in the input; rewrite them as neutral benefits otherwise.
- No competitor brand names in titles or keywords.

## Process
1. Identify: what it is, who it is for, the main problem it solves or
   occasion it fits, and the 3-5 facts that matter most to that buyer.
2. Turn each key feature into a benefit: feature -> what it means for the
   buyer ("304 stainless steel" -> "won't rust in the dishwasher").
3. Write the title: product type + key attribute + main use, front-loading
   the words shoppers search for. Respect the platform limit.
4. Write 5 bullets: benefit first, then the supporting fact, one idea each.
5. Write the description: a 1-2 sentence hook about the buyer's situation,
   a short paragraph on use and feel, then specs and what's in the box.
6. Add search keywords: 10-15 phrases a buyer would type, no repeats of the
   title, no competitor brands.

## Platform defaults
- Amazon: title up to 200 characters, 5 bullets, plain description.
- Etsy: title up to 140 characters, 13 tags of at most 20 characters each.
- Shopee / Lazada: title up to 120 characters, emoji-light bullets allowed,
  keep the description scannable on a phone.
- Shopify / own website: title under 70 characters, SEO meta description up
  to 155 characters.
- Unknown platform: use the Shopify defaults and say so in one line.

## Output format
```
**Title:** ...

**Bullet points**
- ...

**Description**
...

**Specs**
| Feature | Detail |
|---|---|

**Search keywords / tags:** ...
**Meta description:** ... (website only)
**Missing info to add:** [list of bracketed gaps]
```
Write in the language of the input unless the user asks otherwise.

## Variations
- "Shorter": title + 3 bullets only.
- "Several products": one block per product, same structure, consistent voice.
- "Thai and English": both versions, Thai first.
- "Variants" (sizes or colours): one shared description plus a short line per variant.

## Quality checks before answering
- Every claim traces to a fact in the input.
- Title fits the platform limit.
- Bullets lead with benefits, not specs.
- All gaps are listed under Missing info to add.
