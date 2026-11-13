<!-- DRAFTED BY CLAUDE (Opus 5.5), 13 Nov 2026, v8 run. The hand-off report for Roger and Pierre: what v8 changed, what was checked, and what is theirs to decide. Counts are computed from DRAFT_v8.md and the v8 ledgers at the time of writing; the commands that produce them are named beside each. -->

# v8 report

## What v8 is

v8 answers one request: keep all of v7's research and argument, restore Pierre's insights in his own words where they still hold, and make the paper plainly a contribution to phygital hospitality research. It is written to the model of Germann Molz (2018) in this journal.

- **The argument is v7's.** The role of host specifies the core duties; holding out, reliance and control of the guest's space bind them to a particular party; what stays with a host that performs through others depends on the duty; and, as the paper's own step, during the stay the guest's claim justifies a further duty to keep a timely route to correction.
- **The phygital layer is new.** The theory opens on Batat's definition and the dual-place movement, treats AI as a constitutive mediator, and draws the 'phygital arrangement' from this journal's network hospitality. Interruptibility returns as the further duty's design consequence.
- **The shape is the model's.** Two contrasting scenes (Garcia et al.'s pricing algorithm; Batat's Le Petit Chef), the thesis with 'we argue', a roadmap, a theoretical context in three subsections, a short approach, then the walk: the parties one by one, the stay, the touchpoint. Each stop closes on what it showed.

## Counts

| Measure | v8 | Target or comparison | Source |
|---|---|---|---|
| Body words | 8,840 | ≤ 9,000 | `wordcount.py DRAFT_v8.md` |
| Mean sentence / paragraph (words) | 26.6 / 137 | model 26.9 / 133; v7 32.3 / 188 | STYLE_PROFILE.md method |
| Sentences over 50 words; longest | 9; 62 words | v7: 15; 61 | same |
| 'We/our/us' per 1,000 words | 8.0 | model 5.3; venue band 4–8 | same |
| Sentences by provenance (ledger entries placed) | Pierre verbatim 50 · Pierre adapted 30 · Claude 194 | — | DRAFT_v8_marked.md |
| Pierre's insights with a recorded outcome | 56 of 56 | every one | PIERRE_LEDGER.md |
| Pierre's eligible sentences not placed | 112 of 216, each listed with its reason | — | OUTLINE.md, last table |
| v7 sentences accounted for | 228 carried, 32 cut with reasons | every one | KEEP_V7_CROSSWALK.md |
| References · cases · legislation | 63 · 22 · 10 | — | DRAFT_v8.md |

**'Phygital' by place** (abstract 1, in the bracketed proposal only (Roger's text has none, though the title does); Statement of Contribution 3; Highlights 2; Introduction 5; Theoretical context 14; Approach 1; The parties 1, in the lead-in, besides the heading; During the stay 1; At the touchpoint 4; Conclusion 4). Every section of the body now uses the word; 'During the stay' gained it in the claim-audit pass, through the defined term 'phygital arrangement'.

**Phygital works cited, and how deeply each was read.** Read in full: Batat (2021, 2024, 2026), Batat and Hammedi (2023), Shabnam et al. (2026), Mameli et al. (2026), Suh et al. (2026), Liu et al. (2026), Binesh and Syah (2026), Ariyogi et al. (2026), Germann Molz (2018). Abstract or chapter list only, and cited only for what those say: Batat (2019), Germann Molz (2026), Lee and Lu (2024). Not reached, and not cited: Riordan (2024), Weaver (2026), Gao et al. (2026), De Vos et al. (2026), Brochado et al. (2026), Batat's PSR (2026), which Bentley does not hold.

## What was checked

- **Claims.** Two independent verifiers checked every sentence of Pierre's and every new or restated sentence against its source (VERIFY_V8_A.md, VERIFY_V8_B.md). The first checked 79 sentences (67 supported, 11 partly, 1 not supported); the second checked 114 (93 supported, 19 partly, 1 not supported, 1 that no source dates). Seven fixes restore hedges or conditions that v7's audit had made and v8 had lost (O-119, O-175, O-199, O-226, O-235, O-239, O-241f). Four sentences are retagged because their provenance was wrong, and the rest narrow a claim to what its source says. Every fix was checked by hand against the source before it entered the ledger, and each is logged under 'Revisions after the v8 claim audit' in LEDGER.md with the sentence it replaced.
- **Citations.** `check_citations.py DRAFT_v8.md cited_keys_v8.txt` reports 'citations OK'. Two reference-list faults were found and fixed while drafting the letters: Batat's PSR and Casalegno et al. sat in the list with no sentence citing them, and the first gave Batat's cited 2026 work a wrong letter.
- **Preflight.** `preflight.py DRAFT_v8.md` passes 19 of 23 checks. The four failures are false positives: legislation and hand-listed cases that the citation resolver cannot parse; 'App. 274' in a case reference; nested quotation marks inside quotations and titles; and 'realised', which is Lord Denning's spelling inside a quotation. The front-matter checks read FRONT_MATTER_v8.md and pass.
- **Letters.** `build_letters_v8.py` copies every quoted sentence of the revision from the ledger and checks it against DRAFT_v8.md, and checks all 33 quotations of the reviewers against the full reviews. Both pass.
- **Not checked by any script.** Whether the prose reads well. That is your read-aloud.

## Decisions that are yours

1. **The AI acknowledgment and the answer to Reviewer 3 (R3.1).** See the cover. The acknowledgment in DRAFT_v8 says Claude drafted the revised article; the journal permits AI only for readability and language.
2. **The register risk with Reviewer 3.** v8 follows the model in using 'we' and occasional questions, and restores paired sentences of Pierre's that R3 may read as the rhetoric it disliked. The letter lists them (R3.1). Three sentences use a wider 'we' than the authors (R3.5).
3. **Your abstract says 'six questions'.** v8's list has seven, because Pierre's 'who must answer if it is disputed?' returns as question 7. Change the number or cut the question. The abstract is otherwise yours, verbatim; the bracketed phygital sentence after it is Claude's proposal (196 of 200 words with it).
4. **Keywords.** Proposed: phygital hospitality; algorithmic mediation; host duties; standing; interruptibility; accountability.
5. **The welcome close.** The conclusion ends on Pierre's 'somebody still owes the guest a welcome' (O-284), after Claude's restatement of the question (O-283). Keep both, or end on one.
6. **The title.** Unchanged. In v8 each word of the subtitle names something the paper defines.
7. **Section weights.** Following the model's weights would have passed 9,000 words, so the theory runs about 26% of the body (model 21%) and the walk about 49% (model 54%) (V8-D10, V8-D11). Every section stays inside the venue's bands.
8. **Well-being.** v8 never uses the word, which the call and the editor's fourth suggestion name. The letters point to what v8 says about costs to guests (Wilson-Nash et al.) and to staff (Jianu et al.).
9. **Industry gains.** Pierre's sentence on gains (O-261) carries no source of its own.
10. **Hospitals and care homes (R2.4).** v8 says the argument reaches other phygital services where several firms stand behind one touchpoint, and names no other sector.
11. **Anonymity.** v8 cites five works by Batat, a guest editor, and none by Mosca or De Vos. It does not cite Berthon et al. (2026), which is a co-author's work.
12. **Pierre's unplaced sentences.** 112 eligible sentences did not fit the word limit; OUTLINE.md lists each with its reason, so you can trade any of them back in.

## Things to check before submission

- **Garcia et al. (2026):** read only as the CESifo working paper; the published page numbers are needed if any quotation stays.
- **Hemmington (2007):** the quotation's page (15) is the author version's; the version of record runs pp. 747–755.
- **Lee and Lu (2024):** cited at the card's abstract summary; re-open the abstract.
- **Suh et al. (2026):** cited by section ('sec. 6'); the verifier found the passage at p. 14 of the PDF.
- **Everett v Comojo:** the control quotation ('The management is in control of the premises …') carries no paragraph number.
- **Hotel Proprietors Act 1956:** confirm that s. 1(1), not s. 1(3), carries the duty to receive.
- **Abstract or chapter-list depth, one clause each:** Batat (2019), Bendoly (2013), Germann Molz (2026), Li and Sun (2025), Roelofsen and Minca (2018).
- **Cheng and Foley (2019) and Edelman et al. (2017):** checked against their cards, which record full-text reads in August; neither text is held locally.
- **Closed by the verifiers:** Pitt-Rivers's trade tag ('the anthropologist', p. 501); 'for its brand' in Hayman (pp. 275, 279); the PHIVE gloss (pp. 13, 16).

## Corrections to earlier records

- **'Constitutive mediator'.** The v8 plan said the editor had endorsed the phrase. Her seven suggestions, as the September letter lists them, do not include it, and it does not occur in the review files of 11 Nov. The letter to the editor presents it as the paper's framing.
- **PHYGITAL_POSITION.md** says v8 engages Mosca and De Vos. It does not cite either.
- **The v7 letter's answer to R3.14** treated the submitted Table 2 as the six questions. In the submitted version Table 1 held the questions and Table 2 the roadmap; the v8 letter answers about the roadmap.

## Outside this task, flagged only

- The repository check `hospitality-citations-agree` runs `check_citations.py` on the old `DRAFT.md` and fails: it cites Weaver (2025) where the reference list has 2026. v8 is unaffected, and nothing was changed.
