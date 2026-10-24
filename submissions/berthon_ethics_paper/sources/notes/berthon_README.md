# The ethics of two transitions (Berthon ethics course paper)

**Status (2026-10-13):** four research rounds run and audited, the third on full texts the author
supplied and the fourth on what else the literature holds; the author has ruled on the eight
decisions; adjudicated and outlined. One Claude-drafted introduction, written at the author's request; the
author writes the paper.
Claude wrote every file in this arm, and none of the wording is the author's unless quoted.

**The question.** Where did the global community fail on ethical grounds as literacy spread, and which
of those mistakes is the transition to algorithmacy repeating? The author's instruction and his four
answers are in [`SOURCE.md`](SOURCE.md).

**Where the research landed.** The record supports a narrower thesis than the one the round started
from. It does not show a global community failing to spread literacy. It shows named institutions
doing five things with literacy once standing depended on it: gating standing on a reading test,
withholding the competence by law, letting a written record override what was said, holding the means
of print by monopoly, and promising returns that did not arrive. In four of the five a contemporary
called it wrong at the time. Imposed schooling does not hold as a sixth: the official reports blame
removal and language suppression, not the teaching of reading.
[`literature/facets/T_adjudication.md`](literature/facets/T_adjudication.md) gives the verdicts, the
comparison to algorithmacy row by row, and the eight decisions.

**The rulings and the second round.** The author ruled on all eight decisions (verbatim in
[`SOURCE.md`](SOURCE.md)): the history is evidence and the inference an analogy; all five failures;
"the global community" for the campaigns only; three internal standards; imposed schooling reframed;
the Berthon passage kept with his later work added; the table rebuilt; a facet on third parties run.
The two facets that followed found that the literacy transition had its own third parties, with
safeguards better documented than abuse, and that three sentences of the Berthon passage misstate
their sources (`T_adjudication.md` §8).

**The third round.** The author supplied twenty PDFs: seven full texts and reviews of ten books.
Kamperman and Graff (2026) already make the overselling argument for AI literacy and touch none of
the other four failures. Graff's introductions and chapter 7 do not state the require/reward
distinction the design-ethics draft attributes to him. Berthon, Pitt and Campbell (2019) argue for
regulation and say information is "necessary, but not sufficient". Moody-Adams (1994) removes the
need for a contemporary objector (`T_adjudication.md` §9).

**Where it starts.** Two Claude-written drafts hold the starting material:
[`../algorithmacy_design_ethics/DRAFT.md`](../algorithmacy_design_ethics/DRAFT.md) and
[`../decision_experience_design/part2_ethics/DRAFT.md`](../decision_experience_design/part2_ethics/DRAFT.md).
Neither argues the new question. Both are strong on the present-day half (mandatory participation,
priced exit, weak voice, dialect bias, deskilling) and thin on the historical half, where they stop
before mass literacy and document no wrong done during the transition.
[`REUSE_MAP.md`](REUSE_MAP.md) goes through both section by section.

## Files

| File | Use |
| --- | --- |
| [`SOURCE.md`](SOURCE.md) | The author's instruction and four answers, verbatim; the origin of the two drafts; earlier rulings that bear on this paper |
| [`sources/`](sources/) | Byte-identical copies of the two drafts |
| [`REUSE_MAP.md`](REUSE_MAP.md) | Every section of both drafts tagged as carrying over, carrying over with a flag, or out of scope; five flags for the author |
| [`RESEARCH_PLAN.md`](RESEARCH_PLAN.md) | Terms, standing rulings, the five problems, the eight facets, the facet file format and rules |
| `literature/facets/` | One `.md` and one `.bib` per facet (A–F, X, Z; G and H in the second round; L1–L3 in the third; M1–M5 in the fourth), then [`T_adjudication.md`](literature/facets/T_adjudication.md) |
| `literature/references.bib` | Built by `python3 literature/merge_bibs.py` from the facet bibs (first facet wins) |
| `literature/audit/` | `AUDIT_01.md` (facets A–D) and `AUDIT_02.md` (E, F, X, Z): 460 items re-checked by independent agents, 384 confirmed, 25 wrong, 51 unverifiable, with every proposed correction applied but one; `AUDIT_03.md` (G, H): 69 rows, 46 confirmed, 15 wrong and corrected, 8 unverifiable; `AUDIT_04.md` (L1–L3): 107 items, 93 confirmed, 9 wrong and corrected, 5 unverifiable; `AUDIT_05.md` (M1–M5, the ranked lists only): 243 items, 201 confirmed, 30 wrong and corrected, 12 unverifiable; `DOI_CHECK.md`, written by `check_dois.py`; `BIB_CHANGES.md` |
| [`ARGUMENT_MAP.md`](ARGUMENT_MAP.md) | Sixteen premises, each with its source, depth mark and weakest point |
| [`OUTLINE.md`](OUTLINE.md) | The author's rulings, a six-section plan with the passages each section can draw on, the rebuilt table, and four further flags on the two drafts |
| [`AUTHOR_DRAFT.md`](AUTHOR_DRAFT.md) | **The author's text and the governing draft**: abstract, introduction and outline, as he supplied them on 2026-10-13. Claude does not edit its wording |
| [`AUTHOR_DRAFT_CHECK.md`](AUTHOR_DRAFT_CHECK.md) | Claude's fact check of that draft against the arm's audited record: what the draft says, what the source says, where. The author decides each |
| [`INTRODUCTION.md`](INTRODUCTION.md) | A draft introduction on Lange and Pfarrer's five moves. Claude drafted it at the author's request; superseded by `AUTHOR_DRAFT.md` |
| [`PAPER_OUTLINE.md`](PAPER_OUTLINE.md) | A paragraph-level outline of §2–§7: claim, evidence with locator and depth, caution. Supersedes section (b) of `OUTLINE.md`; the author's own outline in `AUTHOR_DRAFT.md` now governs |
| [`LITERATURE_TO_ADD.md`](LITERATURE_TO_ADD.md) | The fourth round's recommendations by outline section: works that already say part of what the paper says, claims the new sources narrow, twelve aspects the outline lacks, and what to get from the library |
| [`MANUSCRIPT_v2.md`](MANUSCRIPT_v2.md) | **Version 2 of the manuscript**, 11,768 words, for *Business Ethics Quarterly*. Claude's rewrite of the author's second draft on his instruction; his only once he has revised it. [`MANUSCRIPT_v2_NOTES.md`](MANUSCRIPT_v2_NOTES.md) lists what was kept, cut and added, the sources cited but unread, and the decisions to confirm |
| [`AUTHOR_DRAFT_v2.md`](AUTHOR_DRAFT_v2.md) | The author's second draft (2026-10-13), saved byte-for-byte |
| [`review/`](review/) | Six agent-drafted reviews of the second draft (citations; BEQ referee; philosophy; history; algorithms, law and design; structure and prose) and [`REVIEW_SUMMARY.md`](review/REVIEW_SUMMARY.md). Reviews report and do not rewrite |
| [`venue/`](venue/) | Journal research: the brief, two agent-drafted files, and [`VENUE_RECOMMENDATION.md`](venue/VENUE_RECOMMENDATION.md). Unaudited; AJG ratings unverified |
| [`BERTHON_NOTES.md`](BERTHON_NOTES.md) | What Berthon's papers and Williams say, with locators, set against the three sentences of the draft passage that misstate them. Notes only |
| [`MANUSCRIPT_v3.md`](MANUSCRIPT_v3.md) | **Version 3** (2026-10-14): v2 with every claim and citation verified. Each change is marked inline (`<!-- v3: id -->`); `AUTHOR` marks a change to the argument that the author can reverse. [`MANUSCRIPT_v3_CHANGES.md`](MANUSCRIPT_v3_CHANGES.md) logs each change with its before and after text, source and decision |
| [`MANUSCRIPT_v4.md`](MANUSCRIPT_v4.md) | **Version 4** (2026-10-14): a new paper on the author's instruction (`v4/SOURCE_v4.md`). It opens on Nadella's insider-risk essay and reads it for three mistakes of the oral-to-written transition (burden on the reader, a literacy-based medium, no scaffold). Claude-drafted; 10,303 words of body. Plan, notes and fact checks in [`v4/`](v4/); research in facets V1–V6 |
| [`review/v3/`](review/v3/) | The verification behind v3: `CLAIMS_LEDGER.md` (333 claims), `CLOSED_LEDGER.md` (377 rows with final status and fix), `resolutions/` (claim-driven research C1–C3), `FIX_CHECK_A–C.md` (every v3 change checked against its source), and the briefs |
| [`literature/cards/`](literature/cards/) | One reference card per work v3 cites, each checked adversarially against its source; index in [`REFERENCES.md`](literature/cards/REFERENCES.md), built by `literature/build_cards_index.py` |
| [`literature/audit/AUDIT_06.md`](literature/audit/AUDIT_06.md) | Independent audit of 205 ledger rows (14.6% disagreement; 40% of proposed fixes wrong in the random sample), the reason every v3 change was then source-checked |

## Open for the author

- **v4:** read it aloud and decide the eight departures listed in [`v4/V4_NOTES.md`](v4/V4_NOTES.md), the main one being that Nadella's essay does not say disclosure is sufficient. It also lists the sources to get from a library before submission.

- **v3:** read it aloud; reverse any `AUTHOR` change you reject; the decisions and the PDFs only he can supply
  are listed at the end of `MANUSCRIPT_v3_CHANGES.md` and in the 2026-10-14 report.
- **Length:** v3 has 11,441 words of body and 2,646 of references (14,089 in all). Check whether BEQ's 12,000 includes references.
- The Berthon passage, which the author rewrites from [`BERTHON_NOTES.md`](BERTHON_NOTES.md).
- The five flags at the end of [`REUSE_MAP.md`](REUSE_MAP.md) and the four in `OUTLINE.md` (d).
- The books still unread, listed in `T_adjudication.md` §9.6. Reviews of ten of them were read;
  a review is not quotable as the book.
- Earlier facets are dated records. Where L1–L3 differ from facets F, G, H, X or Z, the L facets
  and `T_adjudication.md` §9 govern.

**How it was made.** Thirteen Sonnet agents ran one facet each on 2026-10-13 and four more audited
the facet syntheses. Claude (Opus) led, applied the audits' corrections as exact text replacements,
adjudicated, and wrote the argument map and outline. Read depth is recorded per source; most sources
were read in part, and no book was read whole.

Course code, length, rubric and due date are not recorded here, on the author's instruction.

This arm borrows lab constructs. It does not re-run Φ.
