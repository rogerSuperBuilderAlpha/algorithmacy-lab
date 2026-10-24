# Cards in this arm

*Written by Claude on 2026-10-24.*

Every card here is a byte-identical copy of a card in another arm. None was rewritten, merged or
normalized; `../../PROVENANCE.md` records the origin and sha256 of each. The unified table is
`../CARD_INDEX.md`; works carded in more than one library are in `../DUPLICATES.md`; works DXD Part 2
cites with no card anywhere are in `../NO_CARD.md`.

| Subfolder | Origin | What came over |
| --- | --- | --- |
| `berthon_ethics_course/` | `submissions/berthon_ethics_course/literature/cards/` | all 193 cards (the stale generated `REFERENCES.md` left behind) |
| `algorithmacy_design_ethics/` | `submissions/algorithmacy_design_ethics/literature/library/` | the whole library: 188 cards, `INDEX.md`, and five working notes kept in place so their sibling links work (`counter_agent_search_notes.md`, `fairness_matrix_2026-09-19.md`, `gemini_report_citation_audit.md`, `journal_scan_memo.md`, `triadic_hf_search_notes.md`) |
| `dxd_foundation/` | `submissions/dxd_foundation/literature/library/` | only the 35 cards matching a key or DOI that DXD Part 2 cites |
| `algorithmacy_scaffolding/` | `submissions/algorithmacy_scaffolding/literature/library/` | only the 5 matching cards |

## Two formats

- **Y (berthon_ethics_course, 188 of its 193).** Frontmatter between `---` lines: `citekey`, `title`,
  `authors`, `year`, `doi`, `source_basis` (full-text / partial-text / abstract / secondary),
  `pages_read`, `local_path`, `sha256`, `manuscript_lines`, `ledger_rows`, `verified` (true / corrected /
  writer-grounded / pending). Then `## Summary`, `## Key facts it relies on`, `## Critical notes`.
- **H (the other three libraries, and five berthon cards copied from dxd_foundation).** An H1 citation
  line, then `**Identifier:** … · **Read depth:** …` (full_text / partial / abstract_only / secondary),
  then `## What it argues`, `## Relation to the argument`, `## Caution`, and in most cards an
  `## S2 adversarial verification` with a `**Verdict:**` (confirmed / corrected / could not verify).

## How paths inside a card resolve

Y cards name files of their origin arm as bare text (`facets/B_print_1450_1800.md`, `review/R4_history.md`,
`audit/AUDIT_01.md`, ledger rows such as `P4-002`). Read them against
`submissions/berthon_ethics_course/`; `manuscript_lines` point into that arm's `MANUSCRIPT_v2/v3.md`
(here `../../sources/06_` and `07_`). H cards link siblings by filename, which still works inside each
subfolder; their `RESEARCH_PLAN*` and `DRAFT.md` references resolve against
`submissions/algorithmacy_design_ethics/` (or `dxd_foundation/`). `local_path` fields point to PDFs on
the author's disk outside the repo.
