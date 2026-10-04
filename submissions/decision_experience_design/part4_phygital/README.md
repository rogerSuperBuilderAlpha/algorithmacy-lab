# Part 4: Decision experience design in the phygital context (opened 2026-10-04)

**Status:** research run complete on 2026-10-04; **the gate is not met** (two of eleven items). The run produced nine research facets, an adjudication, a lead audit, an argument map and an outline. No draft exists and none is planned until the author asks for one. Claude wrote every file in this folder; none of the text is the author's.

**Thesis (author, 2026-10-04).** Decision experience design is not only a software or digital concept. Part 4 reviews physical decision experience design, starting from the issues raised by researchers who study physical/digital hybrid experience, known as the phygital.

**The question the run has to answer.** Parts 1 to 3 define decision experience design by one structure: an adaptive, opaque intermediary that reads several parties and commits an outcome binding on them. Part 1 also places the environment "arranged by an identifiable human designer" among the predecessors. Part 4 can therefore claim one or more of four things, and the run tests each against cases:

1. The phygital is the same algorithmic intermediary reaching into physical space.
2. A purely physical or human arrangement can itself be an intermediary, which would make a pre-digital decision experience design.
3. Physical design is only choice architecture and stays among the predecessors.
4. The physical layer is where the algorithm's ruling becomes a fact and where exit is priced, so it is where Part 1's design principles are kept or defeated.

**The test.** Four marks, taken from Part 1's wording: a distinct intermediary; it reads both parties; it binds both; it does not hold still. Part 3's test at the match is applied beside them.

**Author rulings (2026-10-04).**
- The run adjudicates the four claims case by case. The author rules after seeing the evidence.
- Cases cover retail, hospitality and leisure, transport, and warehouse and workplace.
- The hospitality arm (`submissions/hospitality_phygital/`) supplies sources only. Part 4 takes no construct and no sentence from it and does not cite the unpublished manuscript.
- Part 3 was pushed first (PR #800); this branch, `dxd-part4-phygital`, starts from its tip.

**Gate.** The run fails unless each item below is read in full text. Details and what I confirmed myself are in `literature/audit/AUDIT_00.md`.

| Item | Grade at start | Grade reached | Copy read |
| --- | --- | --- | --- |
| Batat 2024, phygital customer experience framework | abstract | **abstract: not met** | none |
| Batat 2026, *Journal of Services Marketing* framework paper | abstract | **abstract: not met** | none |
| Wilson-Nash 2026, "No App, No Entry" | abstract | full text | Wiley version of record |
| Bitner 1992 | not held | full text | journal scan on a course site |
| Kotler 1973 | not held | full text | image scan, read by OCR |
| Latour 1992, at declared pagination | reprint pages | full text, 1992 pages 225–258 declared | OCR of the 1992 scan and the reprint |
| Akrich 1992 | secondary notes | partial; her 1987 French original read in full in its place | OpenEdition reprint |
| Schüll 2012, design chapters | introduction | not obtained; Schüll 2005 and her 2012 *Limn* article read in full in their place | saved copies |
| Dourish 2001 or Suchman 1987/2007, beyond chapter 1 | not held | Suchman: full text of chapters 1–4 and 8 in the 1985 report that became the book | Xerox PARC report ISL-6 |
| Weiser 1991; Chalmers and Galani 2004; "beautiful seams" | full text (cards in another arm) | full text; the phrase traced to Weiser's 1994 slides | saved copies |
| Facet G: five cases with a regulator, court or company document | none | met: nine cases across all four domains | saved copies and live pages |

**What the run did (2026-10-04, local session).**
- Lead: scaffold, reuse harvest (`literature/REUSE.md`), gap search (facet Z).
- Eight agents (model: Fable), one per facet A–G and X, wrote 320 entries; `merge_bibs.py` kept 292.
- Lead audit: quotations for the gate and load-bearing sources checked against copies I opened; every DOI resolved on Crossref (221 of 223; no correction notices); web-page facts in facet G refetched.
- One agent (model: Fable) wrote the adjudication (facet T) from the eight facets.
- Lead: `ARGUMENT_MAP.md` and `OUTLINE.md`.

**What the run found, in one paragraph.** Two physical arrangements carry all four marks: ride-hail, and the airport gate with a human committing the outcome. Most designed physical environments read no one and apply one rule to everyone, which is choice architecture by that field's own definition. The physical layer is where rulings become facts and exit is priced, but that holds with or without an algorithm. No arrangement without a digital system carries all four marks; the closest are a human reader (which needs the author's ruling) and Akrich's electricity meter (two marks). See `OUTLINE.md` (a) and (f).

**Files.**

| File | Use |
| --- | --- |
| `OUTLINE.md` | Thesis, rulings, section plan with per-claim status flags, evidence against, jargon table, ten open questions |
| `ARGUMENT_MAP.md` | Each baseline argument from Parts 1–3 against the physical and phygital literature; what phygital researchers raise; the counter-case |
| `literature/REUSE.md` | Sources the lab already holds that bear on Part 4, with read depth and where each sits |
| `literature/facets/Z_gap_search.md` | Whether anyone already writes of decision design or choice architecture in phygital settings |
| `literature/facets/A`–`G`, `X` | One research facet each, `.md` and `.bib` (see `OUTLINE.md` for what each covers) |
| `literature/facets/T_adjudication.md` | The four marks applied to fifteen arrangements; strains on the test; collisions with Parts 1–3 |
| `literature/references.bib` | Built file: 292 entries |
| `literature/audit/AUDIT_00.md` | What the lead checked against sources, and what it did not |
| `literature/audit/BIB_CHANGES.md` | Merge decisions and proposed corrections, none applied |
| `literature/merge_bibs.py` | Builds `references.bib` from the facet bibs; `--check` confirms it is current |
| `literature/build_references.py` | Copied from Part 3; writes the reference list at the end of a `DRAFT.md` |

**Not yet made.** A draft. A citation audit of the abstract-level entries (88 across facets A, B, E and X).

**Open for the author.**
- The ten questions in `OUTLINE.md` section (f). The first, whether a human reader counts as the intermediary, constrains the rest.
- Six sentences in the live Part 1 that the sources do not support as worded (`T_adjudication.md` section 5).
- Library copies that would close the gate: Batat's two framework papers; then Schüll 2012, Akrich 1992, Dourish 2001, Larivière et al. 2017, van Doorn et al. 2017, and Barlow and Johnson 2026.
- Unconfirmed facts listed in `AUDIT_00.md` section 3.
- Corrections to other arms' records in `BIB_CHANGES.md` section 3, not applied.
