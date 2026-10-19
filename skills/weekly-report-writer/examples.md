# Test prompts (used by the automatic self-test)

## 1. Brain-dump
"this week: finished onboarding emails v2, sent to 3,200 users, open rate 41%.
still doing pricing page copy maybe 60%. waiting on legal for terms update.
standups. helped Mai with the CRM import. next wk: start referral program"
Expected: Highlights include the onboarding emails with 3,200 and 41% kept
exactly; pricing page In progress 60%; legal as a blocker with `[date]`;
standups dropped; CRM help in Done; referral program in Next week.

## 2. Previous week's report supplied, one promised item missing
Expected: missing item flagged, carried-over items marked.

## 3. Thai-language bullets, "Slack message" requested
Expected: compact Thai output under 120 words, no headings.
