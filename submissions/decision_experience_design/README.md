# Decision Experience Design (literature review — opened 2026-09-30)

**Status:** review drafted 2026-09-30 (`REVIEW.md`, ~8,600 words + 150 references, Claude-drafted for the
author's revision); citation audit under `literature/audit/`. Seven facet searches under `literature/facets/`. A Substack essay drafted the same day (a Claude Doc,
not in the repo) surveys the practitioner uses only.

**Published.** Part 1, "Decision Experience Design: Yes, another XD", went live on Substack on 2026-09-30:
<https://rogerhuntphdcand.substack.com/p/decision-experience-design>. The final text is archived in
`published/2026-09-30_decision-experience-design.md`. That text is the author's revision, and where it differs from `REVIEW.md` (the earlier Claude draft), the
published text governs. Part 2, "Decision Experience Design Ethics", is drafted in `part2_ethics/`
from the author's capstone pitch (`part2_ethics/PITCH.md`). Part 3, on decision markets, is in
`part3_prediction_markets/`. The physical-space essay is archived in `physical_space/`, with the
citation audit in `physical_space/CITATION_AUDIT.md`.

**Thesis (the author's, 2026-09-30).** UX design became a profession by importing cognitive science
and human factors: how people read a screen, cognitive load, visual and haptic perception. As
coordination moves from literacy to algorithmacy, the decision replaces the screen as the unit of
design, and a new set of cognitive problems comes with it. Decision Experience Design (DXD) is where
the practice is going and should go, and its practitioners should become experts in algorithmacy
the way UX designers became experts in reading and perception.

**What this arm has to establish.**
1. The current literature on the term itself (thin: practitioner and grey sources, 2023–2026).
2. The precursor literatures that already design decisions under other names — choice architecture
   and digital nudging, decision support and cognitive systems engineering.
3. The historical claim about UX's cognitive foundations (the left side of the analogy).
4. The cognitive findings on deciding with and through algorithms (the right side).
5. How algorithmacy differs from the competence constructs a reviewer will raise (algorithmic
   literacy, AI literacy, algorithmic awareness), so that "DXD experts in algorithmacy" means more
   than "UX designers who know about AI."

**Relation to other arms.** Borrows the construct from `org_frontier/essays/literacy_or_algorithmacy.md`
and `../lima_pdw/`. Closest neighbours: `../algorithmacy_scaffolding/` (novice/expert cognition,
HCI scaffolding for users) and `../algorithmacy_design_ethics/` (algorithmacy is not literacy
extended; legibility is the literacy-paradigm remedy).

**Ruling (author, 2026-09-30): this arm sides with design-ethics.** Algorithmacy is not legibility.
The scaffolding and dial-response arms lean toward legibility remedies; this arm does not follow
them. DXD expertise in algorithmacy means designing for the three design-ethics principles —
agentic parity via counter-delegation, structural refusal, bounded outputs and operational
predictability — not for a user who reads the algorithm more skilfully. Transparency findings
enter the review as evidence about *when* predictability holds, not as a case for legibility.

**Ruling (author, 2026-09-30): the numeracy framing, not Ong's.** The literacy→algorithmacy move is
argued on the numeracy model — numeracy predicts decision quality independent of general ability
(Peters et al., 2006) — so the claim is that algorithmacy *moderates the quality of decisions made
through algorithmic intermediaries*, which is testable. The review does not claim that algorithmic
mediation restructures cognition the way Ong (1982) says writing did; Street's (1984) critique of
that great-divide claim stands. The UX analogy is carried at this level: UX designers needed
expertise in the capacities that predict task performance (reading, load, perception); DXD designers
need expertise in the capacity that predicts decision quality through an intermediary.

## Files

| File | Use |
| --- | --- |
| `REVIEW.md` | Thematic synthesis, gap check, argument map |
| `literature/facets/F1…F7_*.md` | Per-facet search log, annotated entries, synthesis (F7 = numeracy addendum) |
| `literature/facets/F1…F7_*.bib` | Per-facet BibTeX |
| `literature/references.bib` | Merged bibliography (201 entries; 150 cited) |
| `literature/cited_keys.txt` | Keys cited in REVIEW.md |
| `literature/build_references.py` | Regenerates REVIEW.md's References from the two files above |
| `literature/audit/AUDIT_0*.md` | Per-batch citation audit (metadata + claim checks) |
| `SEARCH_LOG.md` | Every query, source, date and count, merged from the facets |
