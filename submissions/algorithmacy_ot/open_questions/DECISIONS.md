# Decisions log, `ot-oq-2026-11`

> **[Written by Claude, the run's lead.]** Each entry gives the date, who decided, and what.

## 22 Nov 2026: Gate 0 (the author)

1. **Corpus:** every item OT published, of every type.
2. **Look-back:** volume 4(1)–(3) (early 2023) is read in full, so the corpus starts at 4(1).
3. **Baselines:** the run checks all three versions (GDOC, ASM, PAPER); see `BASELINES.md`.
4. **Pick-up:** forward citations are traced for the shortlist of about ten questions (S10).
5. **Commits:** standing approval to commit and push at stage boundaries on
   `research/ot-open-questions`. Records only; nothing merges without the author.
6. **Records stay in `open_questions/`.** Installing any into the Lima library waits for Gate 1.
7. **Plan:** Fable built it and assigned the models; the author approved it on 22 Nov.

## 22 Nov 2026: S0 (the lead)

- **The Google Doc baseline.** "Algorithmacy OT - claim-check edition 2026-10-10" (Drive, last modified
  11 Oct 2026) was re-exported on 22 Nov. It matches the 11 Oct snapshot apart from one whitespace line,
  so GDOC = that text.
- **Tools.** `fetch.py`, `check_dois.py`, `quote_check.py` and `build_index.py` were copied from
  `submissions/dxd_animation/library/tools/`, with the store path changed to
  `~/iit-playground/ot_open_questions_local/pdfs` and the User-Agent changed to a generic client name.
  `build_index.py`, `check_dois.py` and `quote_check.py` read the card schema of the earlier runs. They
  get adapted to the record schema at S8, before they run.
- **Not reused:** `lima_pdw/working/verify.py`, whose User-Agent carries a personal email address.

## Flags for the author (to report, not to fix)

- **APC.** OpenAlex lists OT with an APC of 0, while `JOURNAL_SPEC.md` gives US$1,000. To be checked
  against the SAGE page at S1.

## 22 Nov 2026: S4–S5 (the lead)

- **Pilot passed.** All 83 OQ quotations in the five pilot records were found in the text; every
  unmatched string came from extraction (page break, line-end hyphen, em-dash at line end). Recall met or
  exceeded the structure maps (Mena 23 items, Friedrich 18). Fable's pass rule that Ernst state "none"
  over-read the structure map, which counts only *numbered* questions; Ernst's eight closing calls,
  limitations and invitations are genuine and stay.
- **Text layers.** The `-layout` extraction set columns side by side and broke quote matching. Every
  `_paged.txt` was regenerated in reading order before S4b.
- **Answered questions are not open.** A question the paper raises and then answers itself, or one the
  theory attributes to its actors, is not an OQ (V01 removed four from chia2023). Ruled: keep the removals.
- **Boundary conditions stay as OQs** with `form: boundary_condition`. They mark where a theory stops,
  which is where another theory can enter. Synthesis weighs them below explicit questions and calls.
- **Lowering topic flags.** Verifiers may only raise flags. Flags that look too high (e.g.
  derekrobinson2025 `triads_third_parties: 1` on "cultural arbitrations") go to the Fable hand-check,
  which may lower them.
- **Repository copies.** Four records rest on manuscripts, not the version of record (derekrobinson2025,
  sasaki2024, phillips2024, hsu2024). Each is listed in `BROWSER_LIST.md` for replacement; quotations are
  re-checked if a version of record arrives.
- **A paper's own research question** (V02's query). When a paper states a question and answers it in the
  same text, the question is not open. It stays in the record but takes `form: own_research_question`,
  and synthesis uses it only to place the paper in a conversation, never as a question to answer. The
  Fable hand-check applies this uniformly (V02 flagged friedrich-01, fotaki-01/02, wright-01, winkler-01,
  gumusay-07). V02's removal of hawbaker-05/06/07 stands.
- **hawbaker2025 Caution** quotes three phrases from Nigam et al. (2025). The lead checked them against
  `nigam2025_ro.txt`: all three appear there once (22 Nov).
- **V03 queries.** werner2026 `evaluation_accountability: 2` accepted (accountability pressures are a
  named step in its process model). New `read_depth` token `full_vor_cover` for a repository cover sheet
  in front of the version of record (giovannoni2025, bartunek2025, nigam2025, orlikowski2023); the
  hand-check applies it.
- **V04 queries.** All five defaults stand (hsu-07 as `own_research_question`; the phillips p. 5 paired
  question stays not counted; orlikowski `platforms: 1`; inner quotation marks rendered as single marks
  are acceptable; licence taken from Crossref). The Fable hand-check may revisit any of them.

## 22 Nov 2026: the author's standing instruction

The author connected Chrome and said: keep going, launch the reader batches, do not ask for approvals, get
through the whole process, read all the papers carefully and compile all the open questions. Taken as:
`ALGORITHMACY_BRIEF.md` is approved as written; the lead rules every query a stage raises and logs it
here; the run continues to `REPORT.md` without stopping at gates other than Gate 1.

- **S3 via Chrome.** PDFs fetched in the author's logged-in Chrome from the article page's own origin
  (`/doi/pdf/<doi>?download=true`), one every 8 s, saved to `~/Downloads` as `otoq_<key>.pdf`, then moved
  into the store by `work/register_downloads.sh`. Versions of record replaced the four manuscript copies
  (kept as `<key>_repo.pdf`).

## 22 Nov 2026: S4b complete (the lead)

- All 66 items read: 15 reader batches (8 Opus, 7 Sonnet, including the two pilot batches; corrected 22 Nov, it first read 13). Every record passed the
  readers' quote self-check apart from extraction artifacts noted in each Caution.
- **Outside the corpus but in the conversation.** scherer2023 replies to Zuboff (2022, *Organization
  Theory* 3(3)), which predates the window. dion2025 critiques Schoeneborn and colleagues' organizationality
  work published outside OT. Synthesis notes these as conversations that continue beyond the corpus; the
  run does not add the earlier pieces.
- **racker2024 issue.** Crossref gives issue 2; the PDF prints none. Crossref is used.
- **V06 flag queries** (garud2025 algorithms_ai/platforms; abend2024 and stevenson2024
  evaluation_accountability) go to the Fable hand-check. The flag means evaluation of people or
  organizations as practice, not criteria for judging scholarly theory.
- **V08 queries.** (1) krautzberger2024 `triads_third_parties: 1` stands for now; Fable may revert.
  (2) Answered questions the reader did not record stay under Not counted; the ruling covers how recorded
  ones are classed, not adding new ones. (3) skade2025 OQ-04 stays a `future_research_call`, because the
  paper only partly closes the gap.
- **V07 queries.** Folding near-duplicate own questions into one `own_research_question` OQ is accepted,
  since those questions never count as open. The flag scale is the reader brief's: 1 = in passing,
  2 = central. Crossref's title punctuation stands. schildt OQ-05 stays an `invitation`.
- **V10 queries.** (1) Calls the paper fulfils itself stay under Not counted, by the same logic as answered
  questions. (2) The three flags stay at 1. Racker's "accountability" means who does which sub-task, which
  is coordination, not evaluation. Justesen's mediating technicians are intermediaries, so Fable may raise
  that flag to 2 at hand-check.
- **V09 queries.** Accepted: friesl2023 evaluation 2 (moral evaluating is one of its two mechanisms) and
  jackwerthrice2023 intermediaries 1 (brokering). leitzinger2023 OQ-33 stays separate from OQ-29, because
  it has a different addressee and section.
- **V12 queries.** scherer2023 accountability 2 accepted. whyte2023 `intermediaries` is lowered to 1 at
  hand-check unless Fable finds an intermediary actor, since technology mediating experience is not a
  party standing between parties. Zuboff (2022) is outside the corpus, so there is no exchange_id.
- **V11 queries.**
  1. dion2025 `triads_third_parties` is lowered to 1 at hand-check. Its Thirdness is a relation among
     three terms of meaning, not among social parties (p. 8, p. 15). Synthesis records it separately as
     the corpus's one Peircean argument, because the author's dissertation work on Peirce's reduction
     thesis touches it directly.
  2. brennecke2025 intermediaries 2 accepted (brokerage section, pp. 11–13).
  3. dion2025 OQ-01 as `own_research_question` accepted.
  4. patriotta2025's theorized failure modes stay under Not counted. Only conditions the authors place
     outside their model are boundary conditions.
  5. Quotations in a Verification section do not count toward the 800-word cap.

## 22 Nov 2026: S5 complete

All 66 records are verified across V01–V12, plus V05 (re-anchoring to the versions of record). No record
holds a quotation that is absent from its source.

## 22 Nov 2026: S8 (partial)

- `EDGES.tsv`: 52 citation edges among corpus articles; most cited within the corpus are gumusay2024 (6),
  orlikowski2023 (5) and cornelissen2024 (4). The prasad2024 → abend2024 edge stays. Prasad cites Abend's
  essay under a pre-publication title (noted by reader A4), so the target is the same article.
- `DOI_CHECK.md`: 0 mismatches across 66 records.

## 22 Nov 2026: S6 (fit)

The two Opus scorers worked blind to each other, A in corpus order and B in reverse. Over 619 open
questions they agree exactly on 92.9%, within one point on 99.8%, with quadratic-weighted kappa 0.878. Only
one OQ differs by 2 or more (jaser2024-11: A=2, B=0). Neither scorer gave a 4. A gave seven 3s and B four;
both gave 3 to stark2024-01, stark2024-06, hinds2024-04 and hinds2024-17. 38 OQs scored 2 or more from at
least one scorer, and Fable adjudicates them at S7. Caveat: both scorers used the same brief, so their
agreement measures the brief's reliability, not its validity. The S11 critics test validity.

## 22 Nov 2026: S7 rulings (the lead)

- **schoeneborn2026 exchange_id `v6i4-organizationality`.** The lead instructed this at H3, with TIERS X4
  as the basis. Hand-check found the stronger basis: Schoeneborn et al. name Dion et al. (2025) four times
  and list it in their references.
- **schoeneborn2026 `evaluation_accountability`** stays at 1. Accusation and scapegoating attribute
  actorhood; they do not evaluate performance.
- **scherer2023-12 removed** at hand-check, because it states the thesis and asks nothing. The H2
  reclassifications (scherer-09 and jaser-08 to `limitation`) are accepted.
- **H1.** Final fit 3 holds for stark2024-06 and hinds2024-04 only. Fable lowered stark-01 and hinds-17
  from 3/3 to 2, against both scorers, and gave reasons from the text. racker2024-05/06 stay as
  `boundary_condition`. Quotations in Fit and Hand-check sections fall outside the 800-word cap, the same
  as Verification. OQ-hinds2024-25 was added at hand-check, so it has no S6 scores; Fable's 2 stands, and
  the S11 critics will test it with the rest.
- **H4/H5.** Neither batch has a final fit above 1. Accepted: whyte2023 `intermediaries: 1`, because the
  intermediary actors appear only in passing; pozner2023 `intermediaries: 2`, because the media stand
  between scandal entrepreneurs and publics in every stage; dugay2024 `communication: 2` and
  `intermediaries: 1`; derekrobinson2025 `triads_third_parties: 0`. winkler2025-07 stays an
  `own_research_question` on the hsu-07 precedent. werner2026 `intermediaries: 1` stands.
- **Pointers for synthesis.** patriotta2025 (p. 16) faults "dyadic relational processes", and dion2025
  argues for Thirdness. These are the corpus's two anti-dyadic moves, and neither involves a social third
  party. dugay2024 is a contrast case: formalization as the classical answer to opaque rules.

## 22 Nov 2026: S9a (clustering)

- O (Opus) found 48 recurring conversations and 19 singletons. F (Fable) found 30 conversations, 11
  cross-cutting questions and 50 singletons. Both worked from the QUESTIONS table while the hand-check was
  still editing records, so both member lists get one more pass at reconciliation, after S7 ends.
- **Blindness.** O saw no fit data. After its clustering was complete, F read the first 12 lines of
  `hand_check/HC_H1.md`, which hold fit notes on four articles, plus the hand-check lines inside records.
  F's conversations were already fixed by then, so the lead judges the clustering unaffected. The
  disclosure is kept here.
- **H6.** All 110 scored rows are at final 0 or x. Its five calls are accepted: ocasio2023-04 added;
  friesl2023-06 is a call; friesl2023 evaluation stays 2, because its "moral evaluating" is people
  judging work in practice; jorgensen2023 intermediaries 0; fotaki2023-07 kept. Records missed OT
  citations wherever the text layer breaks "Organization / Theory" across lines, so `EDGES.tsv` is rebuilt
  with whitespace normalized (S8 v2).
- **H7.** Nothing in the batch is above fit 1. Accepted: wright2023-01 as an `own_research_question`;
  krautzberger2024 triads 0; garud2025 algorithms_ai and platforms stay 1, literacy_competence 2;
  lantela2024 evaluation 0. mutch2025-06 stays: "organizational scholars need to take the law seriously"
  is addressed to others, unlike scherer2023-12, which states the thesis. seidemann2024-16 stays separate.
- **Compiler fix.** `compile_questions.py` now skips any block beginning "- Removed" (it missed
  scherer2023-12's "Removed at hand-check").
- **H8.** Nothing in the batch is above fit 1. Five reclassified to `own_research_question` (friedrich-01,
  pavlisa-01, porsfelt-01/02/03). ernst2026 literacy_competence 2 and mena2026 triads 1 stand. The
  nine friedrich-03 to -11 questions are put to practitioners, not researchers, and synthesis weights
  them accordingly.

## 22 Nov 2026: S7 complete

All 66 records have been hand-checked by Fable (H1–H8). `fit/FIT_FINAL.tsv` holds the final score for
every OQ, using Fable's adjudication wherever either scorer gave 2 or more, and otherwise max(A, B) ≤ 1.
The counts: 0 = 484, 1 = 94, 2 = 25, 3 = 2, 4 = 0, x = 79. The two 3s are stark2024-06 and hinds2024-04.
The 2s sit in stark2024 (7), hinds2024 (8), justesen2024 (3), phillips2024 (3), hsu2024, scherer2023,
racker2024 and suddaby2024 (1 each).

## 22 Nov 2026: S10 (pick-up)

- **Pick-up corpus.** 272 citing works were triaged (OpenAlex and OpenCitations) and 19 carded: 10 in P1
  (4 upgraded to full text from PDFs the lead fetched in Chrome) and 9 in P2. Gap search: 43 queries
  (OpenAlex, Consensus); Scholar Gateway was unavailable ("Access denied").
- **bujold2026 → `answers` on candidate 3 is accepted, with its scope stated.** It answers the partner-or-
  medium question for the worker–organization relation: an intermediary acting on behalf of the
  organization that evaluates the worker. No two people are linked. It is the closest rival to candidate 3,
  and it names two of the three parts (keeping track, interpreting) as conditions, not abilities.
- **Not fetched:** zientara2026 (SAGE 403 in the browser), hall2025 (closed book review), akhil2026 and
  ivarsson2026 (AISeL bot-check; not bypassed). Their cards stay abstract-only, and the report says so.

## 22 Nov 2026: S12 (report)

- Fable traced `REPORT.md`: 101 items, 89 ok, 8 corrected in place, and 4 unsupported. The lead revised all
  four, and each revision is marked "[lead's revision after trace, row n]". On row 83 the trace was itself
  wrong. PAPER §2 ¶2 does read "evaluates and binds them both"; the lead checked all three baselines and
  quoted each version's own wording.
- Fixes in other files from the trace: S10's "272 citing works" means 272 citing rows, which are 261
  distinct works. The "algorithm— will" space in OQ-stark2024-07 came from a line break and is removed
  everywhere; QUESTIONS has been recompiled. The brief's locators for "evaluates and binds" are corrected.
  `critic/CRITIC.md` calls the two Stark passages "consecutive paragraphs", but one paragraph on Yates's
  book lies between them. The ruling does not depend on this, and the file is left as Fable wrote it.

## 23 Nov 2026: S13 (community concerns, recency-weighted), opened at the author's request

- **The author's request:** review all the questions, group them so that a paper exploring algorithmacy can
  address the community's general concern, and give priority to the most recent papers, with questions
  from 2–3 years ago as context. The aim is prevailing, persistent questions that the research addresses.
- **Why a new stage, not a re-sort of S9:** S9 clustered narrowly (54 conversations) and ordered by breadth,
  not recency. S6/S7 fit was scored per question. No 2025–26 question scored above 1 (2025: 109 at 0, 9 at 1;
  2026: 90 at 0, 13 at 1). A recency-first search therefore has to work at the level of a concern, and the
  report must say that the recent stack holds no direct question at fit 2 or more.
- **Design (lead's assignment, following the S9 pattern):** S13a two blind stackings of all 605 open
  questions, Fable and Opus, 8–14 stacks, 2025–26 as primary evidence; S13b Fable reconciles and the counts
  are recomputed by script; S13c Opus maps the stacks against `ALGORITHMACY_BRIEF.md` at concern level and
  names the recent questions algorithmacy addresses; S13d a hostile OT critic (Opus) on the mapping;
  S13e Fable rules. Status labels: prevailing (≥3 pieces in 2025–26), persistent (both periods), fading
  (none since 2024), new (2025–26 only).
- **S13b (Fable):** 12 stacks; counts recomputed by `tools/stack_counts.py` and matched. Time/history ruled a
  cross-cutting thread, not a stack (flagged as the ruling most likely to be reversed). Blindness: Fable
  opened `DECISIONS.md` and saw the S13 sentence on fit by year; it reports that it did not use it. The lead
  accepts the map; the sentence names no stack and no answer.
- **S13c–e:** two blind mappers (Opus) put five 2025–26 questions at fit 2; the critic (Opus) showed they scored
  after crediting a change of level, and put all at 1. Fable ruled at source: OQ-schoeneborn2026-06 at 2 (a
  soft 2, above both blind scorers), all other recent anchors at 1; R08 (actorhood) holds with reframing at
  concern level; R06 shoehorned; Stark & Vanden Broeck 2024 (-06, fit 3) and Hinds & von Krogh 2024 (-04, fit 3
  with scope change) carry the answer. The lead checked the citing counts (Schoeneborn 2026: 0; Stark 2024:
  127) and the FLAGS A1 row against their files. Result in `synthesis/stacks/RULING_S13.md`; Gate 1 reopens
  for the author.

## 23 Nov 2026: S14 (gap search and verification for the 5Cs introduction), at the author's request

- **Request:** run the gap search for the actorhood opening and deep research to confirm everything in
  `manuscript/intro_5c_2026-11-23/INTRODUCTION_5C.md`, so the introduction sells the question robustly.
- **Assignment (lead):** S14a gap search (Opus); S14b owed reads + citation/claim verification of every
  sentence (Opus); S14c search for a published case of a counterpart blamed for a platform's verdict
  (Opus); S14d independent verifier of every quotation the three return (Opus); S14e Fable rules on the gap
  claim and on each sentence of the introduction. Paywalled items the agents cannot reach are fetched by
  the lead in Chrome. Store: `~/iit-playground/ot_open_questions_local/s14/`; outputs: `open_questions/s14/`.
- **S14 result (lead):** verifier (S14d) and Fable (S14e) rulings applied to the introduction as version 2:
  four marked edits to the author's sentences (G7, C2, C3; G4/K2 carried), Claude's sentences revised per
  `s14/RULING_S14.md` §2, one Opening sentence added (Rahman et al.; Curchod et al.), and two HOLD passages
  resting on abstract-only sources (Fu et al.; Zheng & Zhu; Buhmann et al.). The lead re-checked at source
  every new quotation (Rahman preprint p. 6; Curchod AAM pp. 21, 22; Rosenblat & Stark p. 3772; Lee et al.
  p. 1608; Stark & Vanden Broeck p. 9; Schoeneborn et al. p. 9) and the three references added from records
  (Crossref). Paywalled and still unread: Fu et al. (SAGE 403), Vergne & Wry (Wiley 403), Curchod VoR (403);
  Raval & Dourish download did not land. Placement moves of the author's sentences left to the author.

## 23 Nov 2026: S15 (owed reads and gap rerun), continuing S14 without the author

- Chrome fetches: Vesa & Tienari 2022, Cameron 2024, Stelmaszak et al. 2026 (Wiley, after its JS check
  cleared unaided), Maric 2025 thesis (JKU). Abstracts captured: Zheng & Zhu 2026 (Emerald redirects to
  abstract), Buhmann et al. 2021 (CBS portal, no file). Not obtained: Fu et al. 2025 (SAGE asks for an
  institutional sign-in the lead may not perform), Vergne & Wry 2014 (Wiley 403), Rahman et al. VoR (AOM
  403), Hohenstein & Jung 2020 (ScienceDirect check did not clear; not bypassed).
- S15a (Opus) read the new texts; S15b (Sonnet) reran Scholar Gateway (ACCESS_DENIED) and Semantic Scholar
  (HTTP 429 throughout): no records. The lead ran 6 Google Scholar queries in Chrome instead (no CAPTCHA;
  raw results in the store); S15c (Opus) screens the new hits. Then Fable rules (S15d).
- **S15d applied (lead):** introduction v3 per `s15/RULING_S15.md` §1: HOLD passages released as
  abstract-marked [C: …] text; Chong et al. (2024, ACM PDF fetched in Chrome, all nine quotations and pp. 7,
  10 checked by the lead) joins Lee et al. and anchors the "everyday case"; Ohme et al. (2025) cited at A3;
  Vesa & Tienari credited at X4; marked "cf. Cameron" on the author's K2 sentence; new [NEEDS] on one-off
  pairs. The *Business & Society* call stays out of the text (submission note). Owed and needing the
  author's sign-in: Fu et al., Zheng & Zhu, Khan.
- **Author's ruling (23 Nov):** the introduction must sell the question first and be built from the open
  questions *OT* papers leave at their ends, not from their claims. Version 4 rebuilt accordingly from 14
  open questions in `QUESTIONS.tsv` (table in the file). The lead checked all 18 quotations against the
  text layers (all on the stated pages) and built the references from Crossref. v3 kept as
  `INTRODUCTION_5C_v3.md`.
