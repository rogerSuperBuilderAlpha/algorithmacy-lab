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

- All 66 items read: 13 reader batches (7 Opus, 6 Sonnet, including the pilot). Every record passed the
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
