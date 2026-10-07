# Test prompts (used by the automatic self-test)

## 1. Messy bullets
"mtg w/ design + eng. ship v2 landing page fri? sara said ok if copy done.
tom to do copy by wed. pricing still undecided, ask finance. bug in signup form - ken"

Expected: decision "ship Friday if copy is done" is conditional, so it goes in
Open questions or is noted as conditional; Tom/copy/Wednesday; Ken/signup bug/Unassigned date;
pricing as open question with "ask finance" as an action (Unassigned).

## 2. Transcript with speakers
A 20-line transcript where two people disagree and nothing is decided.
Expected: Decisions section says "None recorded" or is omitted; disagreement listed as open question.

## 3. Thai-language notes
Expected: the full output is in Thai.
