# Test prompts (used by the automatic self-test)

## 1. Career switcher
Resume: 4 years retail store supervisor (scheduling 12 staff, inventory, cash
handling). Ad: junior operations coordinator asking for Excel, scheduling,
vendor coordination and SAP.
Expected: transferable bullets moved up, Excel only if present, SAP listed
as a gap (not added), `[add number]` placeholders, cover letter under 300 words.

## 2. Senior engineer, long resume, no job ad
Expected: general improvement, notes that tailoring needs a job ad, no
invented metrics.

## 3. Job ad in Thai, resume in English
Expected: output in Thai (language of the ad), all facts preserved.
