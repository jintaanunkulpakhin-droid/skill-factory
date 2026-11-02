---
name: invoice-and-quote-writer
description: Create clean, professional quotes (estimates) and invoices for freelancers and small businesses from rough notes about the client, work, hours, rates and payment terms, with correct line totals, tax and a polite cover email. Use when someone asks to make an invoice, quote, estimate, price proposal, bill a client, or turn "did 3 days of design at 5000 a day" into an invoice.
---

# Invoice and Quote Writer

Turn rough job notes into a correct, client-ready quote or invoice, with the
maths checked, plus a short email to send it with.

## Inputs
Rough notes are fine: client name, what was done or will be done, hours or
days, rates, fixed prices, expenses, discounts, deposit, currency, tax or
VAT rate, due date or payment terms, and the sender's business details.

Never ask a question before the first draft. Unknown details become
`[placeholders]`: `[Your business name]`, `[Tax ID]`, `[Bank details]`,
`[Invoice number]`.

## Rules (never break)
- Use only the prices, quantities and rates given. Never invent a price.
  If a line has no price, show it with `[price]` and leave it out of the total,
  then say so under Check before sending.
- Do the maths exactly, line by line: quantity x unit price = line total;
  subtotal; discount; tax on the taxable amount; total; minus deposit paid;
  amount due. Round money to 2 decimal places at each line.
- Apply tax only if a rate was given. Never guess tax rules for a country;
  if tax is likely needed but not stated, add `[tax rate]` and a note.
- Keep the currency the user gave; never convert unless asked with a rate.
- An invoice is a request for payment and needs a number, issue date and due
  date; a quote needs a validity date and must say it is not an invoice.

## Process
1. Decide the document type: quote (future work, "estimate", "how much
   would") or invoice (work done, "bill", "charge").
2. Build the line items: short description, quantity, unit, unit price, line total.
   Group small tasks under one clear line when the user listed them loosely.
3. Calculate totals as above and show the working in the Check section.
4. Add terms: due date (default 14 days from the issue date if none given,
   and say so), late-payment wording only if the user provided it,
   accepted payment methods as placeholders.
5. Write a short cover email (under 80 words) to send with it.

## Output format
```
# INVOICE / QUOTE
**From:** <business, contact, [Tax ID]>
**To:** <client>
**Number:** [Invoice number]   **Date:** <date or [date]>   **Due / Valid until:** <date>

| # | Description | Qty | Unit | Unit price | Total |
|---|---|---|---|---|---|

| | |
|---|---|
| Subtotal | |
| Discount | |
| Tax (<rate>%) | |
| **Total** | |
| Deposit paid | |
| **Amount due** | |

**Payment:** [Bank details / payment link]
**Notes:** <scope, terms, validity>

---
**Cover email**
<short email>

**Check before sending**
- <maths working, assumptions, every [placeholder]>
```
Write in the language of the notes unless the user asks otherwise; Thai
documents can show both Thai and English headings if asked.

## Variations
- "Convert this quote to an invoice": keep the lines, add number and due date, remove validity.
- "Payment reminder": a polite email referencing the invoice number, amount and due date.
- "Spreadsheet": also give the table as CSV with formulas described.
- "Hourly breakdown": one line per day or task with hours.

## Quality checks before answering
- Every line total and the grand total recomputed and correct.
- No invented prices, tax rates or business details.
- Document type, number and dates present.
- All placeholders listed under Check before sending.
