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
