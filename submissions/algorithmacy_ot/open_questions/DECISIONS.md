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
