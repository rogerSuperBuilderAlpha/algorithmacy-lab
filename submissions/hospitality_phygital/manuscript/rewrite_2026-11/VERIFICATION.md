<!-- DRAFTED BY CLAUDE (Opus 5.5), 10 Nov 2026. Every check run on DRAFT_v6.md before handing it to the authors, with its result. Facts only were changed at this stage; no prose was rewritten for style beyond the one word noted. -->

# Verification of DRAFT_v6

## Results

| Check | How | Result |
|---|---|---|
| Every ledger sentence is in the manuscript, in order, and nothing else is | Script comparing `sbs/LEDGER.md` ("As written" where present) with `sbs/MANUSCRIPT.md`; reverse pass removing every ledger sentence | 287 of 287 found in order; the remainder is headings, keywords, list numerals and table titles only |
| Manuscript body and DRAFT_v6 body are identical | Normalized comparison | Identical |
| Body length | `wordcount.py`'s `strip_markdown`, Introduction to Conclusion | **8,314 words** (limit 9,000). `preflight.py`, which counts headings slightly differently, gave 8,335 before the last corrections |
| Section shares | Same count | Introduction 9%, first section 22%, second 20%, application 38%, conclusion 10%; all inside the venue's ranges (`journal/JOURNAL_MODEL.md`) |
| Paragraphs | Same count | 47 paragraphs; mean 167 words, median 176 (venue band 130–200) |
| Abstract | Whitespace count | 175 words (journal: 100–200) |
| First person | 'we', 'our', 'us' per 1,000 words | 4.5 (sample: 0.7–9.3) |
| In-text citations against the reference list | `check_citations.py DRAFT_v6.md cited_keys_v6.txt` | 107 checked; one flag, *Woodland v. Essex County Council 2013*, which is a case and is listed under Cases, not References. Not a defect |
| Journal format | `preflight.py` on a copy with numbered headings (the script expects them) | 20 of 23 pass. The three failures: legal citations are flagged because they live in the Cases and Legislation lists; the double quotes are the Act's nested 'stop' and the AI template placeholder; 'franchised' and 'promise' are false '-ise' hits. The abstract and highlights checks read the v4 front matter, not v6's |
| Every quotation against its source | Independent verifier (a separate agent, read-only), 79 quoted passages and eight paraphrases | No wording errors. Seven problems of sense or locator, listed below, all fixed |
| Quotations of the revised text in the reviewer letter | Script | 36 of 36 found verbatim in DRAFT_v6 |
| Register scan | Script | No 'has/have been' passives; no emphasis openers; 'actually' only inside two quotations; one 'simply' cut |
| Library | `build_index.py --check` | OK, 263 cards |

## Corrections made at verification

Each is recorded in `sbs/LEDGER.md` under the sentence it changed.

| Sentence | Was | Now | Source |
|---|---|---|---|
| S-237 | 'even a downgraded analogue route preserves a choice (2026: 978)' | A kept but downgraded analogue route is one of captivity's triggers (p. 978); letting consumers 'choose modes of access' prevents it (p. 981) | Wilson-Nash card. **v5 said the reverse of the source.** |
| S-238 | The 'personal cost and loss' attached to refusing the system | Attached to withdrawing from a service, as the source has it | Wilson-Nash card p. 979 |
| S-145 | The guest 'was received' | Was not turned away; the hotel paid for the test and arranged transport | Xiang card: the rule was not waived |
| S-088 | 'after repeated requests' | 'after repeated communications' | Xiang card |
| S-108 | Liability at para 7 | paras 7, 9 | Crinkley card |
| S-119 | 'a fee-paying provider's responsibilities' | 'the responsibilities of fee-paying schools' | Woodland card, para 25(5) |
| S-147 | Cocktails 'invented by regulars' | 'invented by customers and staff'; the regulars 'who drank them' | Lugosi 2009 card |
| S-140 | 'choosing not to complain' | '… about little things' | Moysidou and Stanley card |
| S-033 | 'King's (1995) authority' | 'the authority of King (1995)' | Checker misread the possessive |

## Corrections of v5 found while writing v6

v5 carried these; v6 does not.

| v5 | Problem | v6 |
|---|---|---|
| Calye's Case, a neighbour 'who is no traveller' (fol. 32b) | Not on the checked card | Quotes the card's passage: common inns 'are instituted for passengers and wayfaring men' (fol. 32b) |
| Golubovskaya et al. 2017: 1295 for 'offered at a price' | p. 1295 is about standardized procedures and scripts | Price cited to Lashley 2015: 5; p. 1295 quoted for scripts |
| Woodland para 24 as 'a relation of charge' | 'charge' is para 23's word; para 24 speaks of control over the claimant | Para 24 quoted |
| Article 29 Working Party p. 21, 'cancelling a booking is a legal effect' | The guidance's example is the cancellation of a contract | Says so; the application to a booking is marked as ours |
| EMTALA duty 'ends at stabilization' | Rests on a subsection no card covers | Refused; not stated |
| Weaver 2025 | Published 16:2, 2026 | Weaver (2026); bibliography corrected |
| Seven `[CHECK]` flags | Sources read only in abstract | None in v6 (`DECISIONS.md`, D6) |

## Debts left for the authors

1. **Baum and Laux (2026).** Quotations and pages (6, 6–8, 12) are from arXiv v2. The reference list renders the LNCS chapter (pp. 115–130, print date 2027). Before submission, either map the pages to the chapter or cite the arXiv version.
2. **Abstract-only sources.** Germann Molz (2026), Riordan (2024), Weaver (2026) and Kim et al. (2025) are described only as far as their abstracts go. Read them in full after your Bentley sign-in and check the four sentences that cite them (S-010, S-238, S-240).
3. **Accepted manuscripts.** v6 quotes none of them, so no journal page is owed. If you add a quotation from Bulley, Varley et al., Moysidou and Stanley, Lugosi (2009), O'Gorman (2009) or Lynch et al. (2011), take the page from the version of record.
4. **Your read-aloud.** No check above stands in for it (`~/.claude/CLAUDE.md`).
5. **The AI acknowledgment** and the reply to R3.1 (`DECISIONS.md`, conflict 1).
