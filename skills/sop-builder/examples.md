# Test prompts (used by the automatic self-test)

## 1. Rambling explanation
"ok so when an order comes in on shopee we check stock in the google sheet,
if it's there we pack it, print the label from the shopee app, and drop at
kerry before 4. if not in stock message the customer and offer refund or wait.
oh and always photo the package before sealing"
Expected: trigger = new Shopee order; stock decision with both outcomes;
photo step marked Important; 4pm cutoff kept; refund policy details as
`[confirm: ...]`; no invented tools.

## 2. Old checklist with missing details
Expected: steps rewritten verb-first, gaps listed under Open items to confirm.

## 3. Thai-language voice memo transcript, "checklist only"
Expected: Thai `- [ ]` checklist only.
