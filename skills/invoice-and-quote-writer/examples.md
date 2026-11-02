# Test prompts (used by the automatic self-test)

## 1. Freelance designer invoice
"invoice for Bloom Cafe: logo design 3 days at 5,000 THB/day, menu layout
flat 4,500, printing cost 1,200 reimbursed, 10% discount on design only,
deposit 5,000 paid, VAT 7%"
Expected: correct maths shown (design 15,000, discount 1,500, etc.), VAT only
where the user's notes imply, amount due after deposit, placeholders for
business details and invoice number, assumptions about which lines are
taxable stated in Check before sending.

## 2. Quote with one unpriced item
Expected: unpriced line shown with `[price]`, excluded from the total and
flagged; validity date and "this is a quote, not an invoice" note.

## 3. Thai notes, "Thai and English headings"
Expected: bilingual headings, THB kept, no currency conversion.
