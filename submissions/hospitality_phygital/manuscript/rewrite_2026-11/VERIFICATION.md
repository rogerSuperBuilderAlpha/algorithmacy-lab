<!-- DRAFTED BY CLAUDE (Opus 5.5), 10 Nov 2026. Every check run on DRAFT_v6.md before handing it to the authors, with its result. Facts only were changed at this stage; no prose was rewritten for style beyond the one word noted. -->

# Verification of DRAFT_v6

## Results

| Check | How | Result |
|---|---|---|
| Every ledger sentence is in the manuscript, in order, and nothing else is | Script comparing `sbs/LEDGER.md` ("As written" where present) with `sbs/MANUSCRIPT.md`; reverse pass removing every ledger sentence | 287 of 287 found in order; the remainder is headings, keywords, list numerals and table titles only |
| Manuscript body and DRAFT_v6 body are identical | Normalized comparison | Identical |
| Body length | `wordcount.py`'s `strip_markdown`, Introduction to Conclusion | **8,385 words** (limit 9,000), after the Bialski amendment to S-010 (8,329) and the Petie insertion (S-150a, S-150b; 11 Nov). `preflight.py`, which counts headings slightly differently, gave 8,335 before the last corrections |
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

1. **Baum and Laux (2026). Resolved for pages, open for the year.** The open-access chapter was read on 10 Nov 2026 and DRAFT_v6 now cites its printed pages (120, 120–122, 126), with the chapter's spelling 'rubber-stamps'. The chapter was published online on 13 Oct 2026, and its own footer gives the volume year as 2027. v6 keeps 2026; choose which year Intellect should print.
2. **Abstract-only sources.** Germann Molz (2026), Riordan (2024), Weaver (2026) and Kim et al. (2025) are described only as far as their abstracts go. Read them in full after your Bentley sign-in and check the four sentences that cite them (S-010, S-238, S-240).
3. **Accepted manuscripts.** v6 quotes none of them, so no journal page is owed. If you add a quotation from Bulley, Varley et al., Moysidou and Stanley, Petie et al., Lugosi (2009), O'Gorman (2009) or Lynch et al. (2011), take the page from the version of record.
4. **Your read-aloud.** No check above stands in for it (`~/.claude/CLAUDE.md`).
5. **The AI acknowledgment** and the reply to R3.1 (`DECISIONS.md`, conflict 1).

## After verification (10 Nov 2026)

- **S-010 amended** to begin the journal's work on platforms with Bialski (2012), read in full in its version of record after this record was first written. The quotation ('the power to choose one member over the other', p. 257) was checked against the saved text. Card `bialski2012technologies` and a bibliography entry were added; the reference list now has 82 entries. Ledger order check, citation check and preflight re-run: unchanged results.
- **Baum and Laux** now cited from the open-access chapter (debt 1, above).
- **S-150a and S-150b inserted (11 Nov 2026)** in the first paragraph of 'Assembled hosts at the touchpoint', after a full read of Petie et al. (2025) for the journal study (`journal/notes/petie2025.md`). They show the path from guest to host failing at the front desk of an assembled host with no algorithm in it. Paraphrase only (accepted manuscript), checked against the saved text, MS p. 11; card `petie2025exploring` and a bibliography entry added; `DECISIONS.md`, D16. The ids are lettered so that no existing id moves. Checks re-run on the amended draft:
  - Ledger against manuscript (a new script, kept outside the repository): 286 entries, the 280 body sentences (S-001 to S-278, with S-150a and S-150b) and the six abstract sentences, each found in order within its run; what remains is headings, keywords, the six-question list and the two tables. Manuscript body and DRAFT_v6 body identical. The record above says 287 of 287 before the insertion; this script finds 284 entries in that ledger, so the earlier script, which I did not keep, counted three items differently. I cannot now say which.
  - Body 8,385 words by the count above (8,329 before); the amended paragraph 180 words (124 before); section shares unchanged to the per cent except the introduction, 10% to 9%; 4.4 'we/our/us' per 1,000.
  - `check_citations.py DRAFT_v6.md cited_keys_v6.txt`: 109 citations, the same single flag (Woodland, a case).
  - References re-rendered with `render_refs.py`: 83 entries, identical to the list in DRAFT_v6.
  - `preflight.py` on a numbered copy: 20 of 23, the same three artefact failures.
  - Reviewer letter: the 27 quotations introduced by 'Changed in …' all match DRAFT_v6 verbatim; none spans the inserted sentences.
  - `build_index.py --check`: OK, 265 cards.

## Corrections to this record after the reviewer pack (11 Nov 2026)

The simulated reviewer pack (`reviews/2026-11-11/`, `SYNTHESIS.md`) found errors this record did not. I confirmed each against its card. They are recorded here as defects of this verification; v6's prose is unchanged until the authors decide.

- **Debt 2 understated the abstract-only sources.** Of v6's cited keys, 19 rest on abstract- or metadata-depth cards, not four: anderson2015transformative, batat2026psr, bendoly2013realtime, brochado2026phygital, calorosenblat2017taking, cheng2025silence, devos2024disabilities, fuller1991consumers, germannmolz2026, hirschman1970exit (metadata), kim2025shadow, king1995what, li2021systematic, morrison2014voice, riordan2024digitally, starruhleder1996infrastructure, weaver2025fast, xing2026algorithmic and xu2020facial. Separately, mohlmann2021algorithmic is full text but superseded by jianu2025.
- **Xu et al. (2021)** is cited at lines 18 and 99. Its card is abstract-only and records the source as displaced on 8 Aug 2026, and line 99's 'weighs the guest's history' scenario is not the source's.
- **Martin and Waldman (2023), line 129**, is misframed. The five-way comparison was not run on adverse decisions; only appeal was tested on bad outcomes, and the appeal went to an internal review board.
- **Garcia et al. (2026), line 99.** 'No one at the desk could explain the price' is my inference; managers keep the final decision.
- **Wrong pinpoints.** Morgan (2015: 7–8) gives accepted-manuscript pages and Kaniadakis and Farmaki (2022: 14) gives OnlineFirst pages, not the pages of the versions listed.
- **De Vos et al. (2024), line 155**, is abstract-only and studies an online MBA, yet it carries a claim about communities.
- **Ivanov and Webster (2024)**, held in the library, sorts hotel decisions by human involvement. It contradicts line 121's 'no study makes them for hospitality'.
- **The quotation check above** tested wording, and wording holds: the copyeditor found all quotations exact. It did not test whether each paraphrase or case description matches its source, and that is where these errors sit.
