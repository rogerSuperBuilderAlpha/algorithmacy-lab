# Lima literature — the working library

This folder is the Lima support arm's bibliography. It is not the manuscript and it is not
the dissertation research library. The live manuscript is
[`../manuscript/PAPER.md`](../manuscript/PAPER.md); where a card and the paper disagree, the
paper wins until the author changes it.

## What lives here

| path | what it is |
|---|---|
| [`REFERENCES.md`](REFERENCES.md) | The **accepted abstract's** fifteen citations, verified 2026-08-13, four flagged on substance |
| [`ZHOU_2025_INSTRUMENT.md`](ZHOU_2025_INSTRUMENT.md) | Zhou, Lei, Liu, Huang & Hou (2025) — the rival algorithmic-competency scale, all twelve items |
| [`cards/`](cards/) | The working library: the 18 August sweep plus two Paper 2 sources the sweep missed |
| [`COVERAGE.md`](COVERAGE.md) | Paper 2's **44** cited works → Lima card, dissertation card, depth, status |
| [`TRAPS.md`](TRAPS.md) | Live citation hazards (wrong paper, wrong author, two Zhou 2025s, withdrawn work) |
| [`INDEX.md`](INDEX.md) | Generated listing, grouped by cluster then read depth |
| [`steelmans/`](steelmans/) | Full-text hearings of extant constructs |
| [`models/`](models/) | Architecture memos for construct development and genre-match papers |
| [`pdfs/`](pdfs/) | Local publisher PDFs. Gitignored. See `pdfs/README.md` |
| [`_build_index.py`](_build_index.py) | Regenerates `INDEX.md` from `cards/*.md` |

The eleven dissertation-format cards that closed Paper 2's library gap sit one level up, in
[`../library/`](../library/). They were installed into `dissertation/research/library/` on
2026-08-19. Read the review edition in `cards/` for Lima work; the `library/` copy is the
one that entered the dissertation shelf.

## The three libraries

| layer | path | role |
|---|---|---|
| Manuscript | `../manuscript/PAPER.md` | Live Lima draft. The archived twelve-section text still sits in `dissertation/current/paper2/PAPER.md`. |
| Dissertation shelf | `dissertation/research/library/` | Canonical shared bibliography (~1,788 entries). Indexes via `_build_indexes.py`. |
| Install archive | `../library/` | Eleven Paper 2 sources written in the dissertation schema. Frozen. |
| This folder | `literature/cards/` | Lima working library. Paper-2–focused. Usually carries `Cluster:`. |

When a slug exists in both Lima folders, do not merge them. Nine overlapping slugs have
different bodies (`barney1991`, `hancock2020`, `hymes1972`, `longmagerko2020`,
`rittergemunden2003`, `sandberg2000`, `schreiner2009`, `spitzberg2006`, `teece1997`).
`guzmanlewis2020` and `spitzbergcupach1984` were copied into `cards/` from `library/`
because the sweep never wrote them.

## Card format

Required, going forward:

- Title line (`# Author (year). *Title*…`)
- `Identifier:` · `Read depth:` · `Source read:`
- `## What it argues`
- `## Relation to the argument`
- `## Caution`

Preferred: `Cluster:`, `Source-tier:`, `Evidence basis:`.

`Relation last checked:` is the dissertation schema. It is not required here. Cards that
came from `../library/` carry it; sweep cards usually do not. Do not rewrite existing
cards just to add a field.

Read-depth tags in use: `full_text`, `author_manuscript`, `extended_preview`,
`abstract_plus_reviews`, `abstract_only`, `citing_reconstruction`, `publisher_record`,
`metadata_only`. Say on `Source read:` exactly what was and was not obtained.

## How to add a card

1. Write `cards/<slug>.md` in the format above. Prefer the dissertation slug when the
   work is already on that shelf.
2. If the same work was carded under a second filename, keep both and put a junior-slug
   pointer on the non-canonical file (see the three duals in `INDEX.md`).
3. From this directory: `python3 _build_index.py`.
4. If Paper 2 cites the work, add a row to `COVERAGE.md`.
5. Install into `dissertation/research/library/` only with a per-action go-ahead, in
   that library's schema, then run its `_build_indexes.py`. A Lima review card is not
   an install.

## Dual filenames

Three works were carded twice by parallel agents on 18 August. Both files stay.

- `klawitter2018` ← `klawitterhargittai2018`
- `cotter2020` ← `cotterreisdorf2020`
- `longmagerko2020` (Paper 2 / dissertation slug) ← `long2020` (fuller, `full_text`)

## Read before Lima

Four items the 18 August memo ranked by what they could change. Status as of 2026-08-19,
after the Phase 1 hearings:

1. **Sutherland et al. (2020), gig literacies.** Closed. Read from the PDF; steelman at
   `steelmans/sutherland2020.md`. "Building relationships" is the authors' own heading and
   the discrimination survives, because the literacy works *beside* or *off* the platform.
2. **Sandberg (2000).** Closed at the card level — `cards/sandberg2000.md` is now
   `full_text` via OCR, and the architecture memo is `models/sandberg2000.md`. Two figures
   in §4 still need checking against the scan; see the 19 August review's housekeeping.
3. **Dominguez Castillo (2026).** Not in Paper 2's reference list. Carded at
   `cards/dominguezcastillo2026.md`. Still unread; the memo flagged it as a possible
   normative challenge.
4. **Spitzberg (2006).** Closed. Full text is on the dissertation shelf and in both Lima
   folders, from Oxford's free JCMC HTML. Steelman at `steelmans/spitzberg2006.md`.

The sweep findings themselves are in [`../REVISION_MEMO.md`](../REVISION_MEMO.md).

## Phase 1 hearings — status

Seven constructs, seven memos, in `steelmans/`. All seven exist as of 2026-08-19.

| # | Construct | Memo | Written from |
|---|---|---|---|
| 1 | Algorithmic competency | `zhou2025apjhr.md` | **Journal PDF** (APJHR 63: e70004), on the dissertation shelf |
| 2 | Gig literacies | `sutherland2020.md` | `pdfs/sutherland2020.pdf` |
| 3 | Reactivity / invisible cage | `rahman2021.md` | Author-deposited accepted manuscript, dissertation shelf |
| 4 | CMC competence | `spitzberg2006.md` | Oxford Academic full text |
| 5 | AI literacy | `longmagerko2020.md` | **Camera-ready full text**, via the Internet Archive |
| 6 | Human–machine communication | `guzmanlewis2020.md` | `pdfs/guzmanlewis2020.pdf` |
| 7 | AI-mediated communication | `hancock2020.md` | Oxford Academic full text |

## Phase 2 architecture memos — status

Five genre-match papers, five memos, in `models/`. All five exist as of 2026-08-19.

| Paper | Memo | Its job |
|---|---|---|
| Rahman (2021), *ASQ* 66(4) | `rahman2021.md` | Condition-then-conduct findings; the data-source table with a "use in analysis" column |
| Cameron (2024), *ASQ* 69(2) | `cameron2024.md` | Opening on an anomaly; researcher position as conduct; coding reported as rounds |
| Curchod et al. (2020), *ASQ* 65(3) | `curchod2020.md` | "This theory does not reach," findings split by level, protocol in an appendix |
| Sandberg (2000), *AMJ* 43(1) | `sandberg2000.md` | How a qualitative study *produces* a competence construct |
| Suddaby (2010), *AMR* 35(3) | `suddaby2010.md` | The four elements of construct clarity, as section jobs |

What both phases changed for the manuscript is collected in [`FINDINGS.md`](FINDINGS.md).
All seven hearings are now written from the article. What remains are page anchors for three sources
read from HTML or a camera-ready, and the Spitzberg & Cupach (1984) monograph.
