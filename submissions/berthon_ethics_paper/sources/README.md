# Source versions and notes (copies, not edited here)

*Written by Claude on 2026-10-24.*

The eight versions of the paper, numbered in the order they were written. Each is byte-identical to its
origin; edit the origin, not the copy. `../PROVENANCE.md` gives each file's origin commit and sha256, and
`python3 -I literature/build_provenance.py --check` (run from the arm directory) exits 1 if any copy has
drifted.

| File | Origin | Date | Wording |
| --- | --- | --- | --- |
| `01_ade_DRAFT.md` | `submissions/algorithmacy_design_ethics/DRAFT.md` | 2026-09-19 | Claude |
| `02_dxd_part2_DRAFT.md` | `submissions/decision_experience_design/part2_ethics/DRAFT.md` | 2026-10-01 | Claude |
| `03_INTRODUCTION.md` | `submissions/berthon_ethics_course/INTRODUCTION.md` | 2026-10-13 | Claude, at the author's request; superseded by 04 |
| `04_AUTHOR_DRAFT.md` | `submissions/berthon_ethics_course/AUTHOR_DRAFT.md` | 2026-10-13 | **The author's** |
| `05_AUTHOR_DRAFT_v2.md` | `submissions/berthon_ethics_course/AUTHOR_DRAFT_v2.md` | 2026-10-13 | **The author's** |
| `06_MANUSCRIPT_v2.md` | `submissions/berthon_ethics_course/MANUSCRIPT_v2.md` | 2026-10-13 | Claude's rewrite of 05 |
| `07_MANUSCRIPT_v3.md` | `submissions/berthon_ethics_course/MANUSCRIPT_v3.md` | 2026-10-14 | Claude; 06 with every claim checked |
| `08_MANUSCRIPT_v4.md` | `submissions/berthon_ethics_course/MANUSCRIPT_v4.md` | 2026-10-14 | Claude, on the author's instruction (new thesis) |

`notes/` holds byte-identical copies of the supporting files the ledger cites: each arm's README,
source and research plans, outlines, fact checks, audits, reviews and change logs. The prefix names the
origin arm (`berthon_`, `berthon_v4_`, `berthon_review_`, `ade_`, `part2_`); `literature/card_sources.json`
maps each prefix to its origin directory.
