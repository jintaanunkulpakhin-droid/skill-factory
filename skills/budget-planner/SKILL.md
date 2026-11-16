---
name: budget-planner
description: Turn a list of income and expenses (notes, a bank statement export or a rough list) into a clear monthly personal budget with categories, totals, savings rate, and practical options to save more. Use when someone asks to make a budget, plan monthly spending, see where their money goes, save more, or organise their expenses.
---

# Budget Planner

Turn a messy list of money in and money out into a monthly budget the person
understands, with the maths checked and realistic options to improve it.

## Inputs
Any list of income and spending: notes ("rent 12k, grab food maybe 4k"),
a pasted bank or card statement, or a spreadsheet export. Optional: goals
(emergency fund, trip, paying off a card), currency, pay dates, household size.

Never ask a question before the first draft. If income is missing, build the
spending side and show income as `[monthly income]`.

## Rules (never break)
- Use only the user's numbers. Never invent amounts; estimates the user
  calls "about" or "maybe" are marked `~`.
- Convert to a monthly figure clearly: weekly x 52 / 12, yearly / 12,
  one-off costs shown separately. Show the conversion in the Check section.
- Do the maths exactly and show totals; round to whole currency units.
- Keep the user's currency. Never convert unless asked with a rate.
- This is budgeting help, not financial, tax, legal or investment advice.
  Do not recommend specific investments, loans, credit products or
  providers. For debt problems or big decisions, suggest talking to a
  qualified adviser or a free debt-advice service.
- Suggestions must be options the user can choose, not judgements about
  their spending.

## Process
1. Clean the list: merge duplicates, convert everything to monthly, and put
   each item in one category: Housing, Utilities and bills, Food and
   groceries, Eating out and delivery, Transport, Debt payments, Insurance and
   health, Subscriptions, Personal and shopping, Family and gifts, Savings,
   Other.
2. Mark each category Essential, Flexible or Savings.
3. Totals: income, essentials, flexible, savings, money left over (or the gap).
4. Compare with the 50/30/20 guide (needs / wants / savings) as a reference
   only, not a rule, and show the person's own split.
5. Offer 3-5 specific, optional ideas that come from their own list, each with
   an estimated monthly effect using their numbers (e.g. "2 delivery meals a
   week fewer: about 1,200 less, based on your 600 per order").
6. If a goal is given, show how many months it takes at the current and at an
   improved savings amount.

## Output format
```
## Monthly budget - <month or [month]>

| Category | Type | Monthly |
|---|---|---|

| Summary | Amount | % of income |
|---|---|---|
| Income | | 100% |
| Essentials | | |
| Flexible | | |
| Savings | | |
| **Left over / gap** | | |

**Your split vs 50/30/20:** ...

### Options to consider
1. ... (about <amount>/month)

### Goal timeline
...

### Check
- <conversions, assumptions, ~estimates, [placeholders]>
```
Write in the language of the input unless the user asks otherwise.

## Variations
- "Spreadsheet": also give the table as CSV with a total row.
- "Couple" or "household": a column per person plus a shared column.
- "Irregular income": budget on the lowest recent month and show a buffer.
- Statement pasted: group transactions by merchant first, then by category.

## Quality checks before answering
- Every amount comes from the input or is a shown conversion.
- Totals and percentages recomputed and correct.
- No specific investment, loan or product recommendations.
- Options are framed as choices, with their monthly effect.
