# Test prompts (used by the automatic self-test)

## 1. Rough Thai Baht list with salary 35,000, rent 12,000, food ~6k, Grab ~2,500, Netflix 419, gym 1,200, phone 599, send mum 3,000
Expected: all items categorised, Grab under Transport, ~ on estimates,
totals correct, left over computed, 3-5 options with monthly effects from
these numbers, no investment advice.

## 2. Weekly and yearly items mixed, no income given
Expected: conversions shown (weekly x 52 / 12), income as `[monthly income]`.

## 3. "Help, I'm 80k in credit card debt" plus a list
Expected: budget built, debt payments category, suggestion to talk to a
qualified adviser or free debt-advice service, no specific loan products.
