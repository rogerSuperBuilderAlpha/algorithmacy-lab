# Algorithmacy for *Organization Theory*

A submission arm for a theory article at *Organization Theory*: algorithmacy as the sensibility a
person needs to coordinate with another person when the exchange runs through an opaque, adaptive
algorithmic intermediary that evaluates and binds them both. Target: a submission-ready draft before
the end of 2026.

**Status, 2026-10-07 — the arm opens.** The paper comes out of the OS/OT Paper Development Workshop in
Lima (5–7 October 2026), where the workshop version drew the comment that it read like an essay. That
version is frozen at
[`../lima_pdw/archive/2026-09-10_PAPER_submitted.md`](../lima_pdw/archive/2026-09-10_PAPER_submitted.md).
The author began the rebuild the same week: an introduction of their own, and a second section first
drafted with another AI assistant, which the author rules is their working draft. Both are seated in
[`manuscript/PAPER.md`](manuscript/PAPER.md), wording unchanged — 961 words of an 8,900-word body.
Claude carded the six sources the new text cites that the library lacked, re-read Stark and Vanden
Broeck, and checked the draft against all of them; the result is
[`manuscript/FLAGS_2026-10-07.md`](manuscript/FLAGS_2026-10-07.md), five claims the cited source does
not support and seven that drift from it. None is applied. Sections 3–6 are unwritten in `PAPER.md`.

**Later on 2026-10-07 the author asked for a full draft.** It is
[`manuscript/DRAFT_2026-10-07_claude.md`](manuscript/DRAFT_2026-10-07_claude.md): about 5,900 words of body,
two-thirds of it the author's own prose carried from the introduction and the Lima paper, the rest
Claude's and tagged as such. It follows the sources where the flags found the earlier wording wrong.
It is about 3,000 words under budget, in the mechanics and the discussion, because the research lines
are unrun. Rule 1 below was set aside for that one file at the author's instruction; it still governs
`PAPER.md`.

## Rules for this arm

1. **`manuscript/PAPER.md` is the author's prose.** Claude edits what the author writes: citation
   checks, cohesion reading, structural notes, length. Claude does not generate manuscript prose and
   does not run review-then-rewrite loops over it. The author's read-aloud is the last gate.
2. **Wrong facts are flagged, not fixed.** A flag gives the correct value and its source; the author
   rules; only ruled fixes go in.
3. **Anything Claude writes inside the manuscript is marked** `[CLAUDE: …]`.
4. **A source is quotable only at full-text depth.** See
   [`manuscript/CITATION_DEPTH.md`](manuscript/CITATION_DEPTH.md).
5. **[`JOURNAL_SPEC.md`](JOURNAL_SPEC.md) wins on format.** 11,000 words including references;
   double-anonymized.
6. **The repo is public.** No publisher PDF or extracted full text is committed. No agent contacts the
   journal.

## Contents

| Path | What it is |
| --- | --- |
| [`JOURNAL_SPEC.md`](JOURNAL_SPEC.md) | The journal's requirements, extracted from its guidelines, with the word budget |
| [`AGENDA.md`](AGENDA.md) | Open questions, the author's first |
| [`FEEDBACK.md`](FEEDBACK.md) | What the Lima reviewers said. Mostly empty: the author's to fill |
| [`RESEARCH_PLAN.md`](RESEARCH_PLAN.md) | The six lines of new reading the unwritten sections need |
| [`manuscript/PAPER.md`](manuscript/PAPER.md) | **The live draft** |
| [`manuscript/sbs_schoeneborn2026/`](manuscript/sbs_schoeneborn2026/) | **The rebuild in progress.** The paper mapped sentence by sentence onto Schoeneborn, Dobusch & Seidl (2026): `MODEL_BRIEF.md`, `MODEL.md`, `OUR_BRIEF.md`, `OUTLINE.md`, `MANUSCRIPT.md`, `LEDGER.md`. **Done for the whole paper**: 228 model sentences answered by 227 of ours. `ASSEMBLED.md` is the clean copy with abstract and references: about 7,040 words of body, 65 references, about 8,760 all-in |
| [`manuscript/process/TARGET_STRUCTURE_porsfelt2026.md`](manuscript/process/TARGET_STRUCTURE_porsfelt2026.md) | Full template of Porsfelt, Vestergaard & Hjorth (2026), the author's other named target; `process/structure_2026_*.md` hold the structures of the seven other 2026 theory articles |
| [`manuscript/DRAFT_2026-10-08_full.md`](manuscript/DRAFT_2026-10-08_full.md) | **The claims source for the rebuild.** The tight draft brought to the length and reference count of the OT models by adding sourced content only: about 6,750 words of body, 78 references, about 9,200 all-in |
| [`manuscript/DRAFT_2026-10-08_tight.md`](manuscript/DRAFT_2026-10-08_tight.md) | Superseded by the full draft. The hard-cut version. Cut hard on the author's instruction: no roadmap, no hand-offs, no hedges, no research-questions paragraph. About 4,800 words of body, 7,200 all-in, 74 references. The author's four introduction paragraphs are uncut |
| [`manuscript/DRAFT_2026-10-08.md`](manuscript/DRAFT_2026-10-08.md) | Superseded by the tight draft. 7,600 words of body. The plain draft with the author's three changes of 8 October: no driver or freelancer examples, the oracy → literacy → algorithmacy argument stated in its own section, and citations placed as the OT articles place them (75 references). Cut on 8 October to about 7,600 words of body, 10,070 all-in |
| [`manuscript/CITATION_REVIEW_2026-10-08.md`](manuscript/CITATION_REVIEW_2026-10-08.md) | How four OT articles cite, the target taken from them, what was added, and what is still missing |
| [`manuscript/DRAFT_2026-10-07_plain.md`](manuscript/DRAFT_2026-10-07_plain.md) | Superseded by the 8 October draft. Second attempt, written plainly after the author rejected the first: each paragraph states its point and then explains it. About 7,000 words of body. The four introduction paragraphs are the author's, corrected; the rest is Claude's wording of the author's argument |
| [`manuscript/PARAGRAPH_REVIEW_2026-10-08_after_cut.md`](manuscript/PARAGRAPH_REVIEW_2026-10-08_after_cut.md) | The current review: what was cut, section shares and every paragraph of the cut draft against four OT articles |
| [`manuscript/PARAGRAPH_REVIEW_2026-10-08.md`](manuscript/PARAGRAPH_REVIEW_2026-10-08.md) | Word counts and a paragraph-by-paragraph check of the plain draft against four OT articles; the four paragraph maps are in `manuscript/process/model_paragraphs_*.md` |
| [`manuscript/DRAFT_2026-10-07_claude.md`](manuscript/DRAFT_2026-10-07_claude.md) | **Rejected by the author on 2026-10-07.** The first full draft by Claude, on the author's instruction; every paragraph tagged as the author's verbatim, the author's edited, or Claude's. Not the author's text |
| [`manuscript/DRAFT_NOTES_2026-10-07.md`](manuscript/DRAFT_NOTES_2026-10-07.md) | What the draft is made of, every change to the author's wording, and what is still thin |
| [`manuscript/OUTLINE.md`](manuscript/OUTLINE.md) | The architecture: budget, each section's job, a packet per section |
| [`manuscript/FLAGS_2026-10-07.md`](manuscript/FLAGS_2026-10-07.md) | Source checks on sections 1 and 2, awaiting rulings |
| [`manuscript/MODEL_PAPERS.md`](manuscript/MODEL_PAPERS.md) | How five OT theory articles are built, and a check of the six-phase table |
| [`manuscript/CARRYOVER.md`](manuscript/CARRYOVER.md) | Which of the Lima paper's sections fit which new section, by line |
| [`manuscript/CITATION_DEPTH.md`](manuscript/CITATION_DEPTH.md) | What may be quoted |
| [`manuscript/process/`](manuscript/process/) | The two Google Doc texts as pulled, and the Stark and Vanden Broeck re-read. Not a source of truth |
| `reviews/` | Review rounds, when there are any |

## The library is shared

This arm keeps no literature of its own. Cards live in
[`../lima_pdw/literature/cards/`](../lima_pdw/literature/cards/) (415 as of today), with the seven
construct hearings in `../lima_pdw/literature/steelmans/` and the naming hazards in
`../lima_pdw/literature/TRAPS.md`. New cards go there, in that format, and the index is rebuilt with
`python3 _build_index.py` from `../lima_pdw/literature/`.

## Related arms

- [`../lima_pdw/`](../lima_pdw/) — the workshop paper and the library.
- [`../proposals/`](../proposals/) — a different paper due at the same journal on 2027-01-31.
- [`../triadic_reduction/`](../triadic_reduction/) — the Peirce, Simmel and Quine sources behind the
  introduction's "irreducible triads".
