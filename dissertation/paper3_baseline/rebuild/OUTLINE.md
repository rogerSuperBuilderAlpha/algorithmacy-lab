# Paper 3 — outline (architectural; detailed outline follows per-section research)

Working title: *Scoring Coordination by Structure: A Graded Typology of Triadic Demand and Five
Corporate Cases.*

Register: Yin theory-driven demonstration of the Paper 2 instrument (not theory-building, not
outcome-validation). ORM venue. Nagel style (CLAUDE.md). Every number from a `rebuild/` script.
The five real-corporation cases are the spine; the catalog and typology are supporting breadth.

Grounding: `research/case_study_methodology.md` (method), `research/framing_and_positioning.md`
(theory, gap, objections). Per-section deep research (Stage 2c) fills the open items before the
detailed outline.

## §1 Introduction — from a yes/no classifier to a graded structural score, applied to real firms

- Paper 2 answered *whether* a coordination form is triadic (Φ > 0). Paper 3 asks *how much* and
  *which real organizations sit where*, and answers with a graded typology demonstrated on five
  large corporations.
- The unit is the coordination *form*, not the person (the readability move: a readability score is
  a property of the text, not the reader).
- The headline: the score tracks the **structure** of how parties reach each other, not the
  **seat** of the mediator. A securities exchange scores like Uber; a staffing firm scores like
  Upwork — same structure, different seat, same score.
- The gap (one paragraph): the algorithmic-management literature frames the platform as a dyadic
  control actor and folds structure into the technology's affordances; no one scores a triadic
  W–S–C form by structural irreducibility so that human and algorithmic mediators of like structure
  score identically.
- Preview the five cases and the two equal-Φ seat-contrast pairs.

## §2 The unit of analysis — the coordination form, not the person

- The readability analogy, stated and bounded (what is borrowed: a property-of-the-form score; what
  is not: a validated reader-outcome instrument — that is later work).
- Grounding in coordination theory: Malone & Crowston (dependencies between *activities*, not
  actors; substrate-independent across human/computational/biological) and Crowston's taxonomy.
- Grounding in brokerage theory: Burt (causation in the *intersection of relations*; the occupant —
  person or organization — is interchangeable); Halevy, Halali & Zlatev (brokerage-as-position vs.
  brokering-as-process; triadic configurations). These are the form-over-actor and structure-not-
  seat warrants from canonical sources.

## §3 The model and the family (the general application)

- Recap the W–S–C model and exact IIT-4.0 Φ from Paper 2 (briefly; cite Paper 2 for the instrument).
- The catalog: enumerate the complete family (4,144 distinct wirings), compute Φ for each; 44.1%
  reducible, seven discrete non-zero bands — the bands are a property of the family, not assigned
  (`catalog.py`/`analyze_catalog.py`).
- What drives Φ: strict mediation strongest (+0.54), parity (+0.27), edges (+0.24), R² = 0.20 — Φ is
  not a feature checklist. The Cerullo (2015) parity caution → read magnitude ordinally only.
- The graded typology: organizations placed on populated bands (`typology.py`), 0 / 0.50 / 0.83 /
  2.00 / 3.00. Tie to the graded-coordination-ladder precedent (Thompson; Van de Ven et al.).
- Typology-as-theory framing (Doty & Glick) — fill specifics from per-section research.

## §4 Methods for the case studies

- Register and aim: Yin theory-driven demonstration; calibrate the claim (demonstration + replication,
  not definitive test — Ridder's caution).
- Case selection: theoretical/diverse-case sampling (Seawright & Gerring); vary determination
  structure, control party count (Burnham et al.). The five cases and their replication roles.
- Replication logic: the two equal-Φ pairs are literal replication on Φ and theoretical contrast on
  seat; MTurk is higher-order theoretical replication.
- Modeling procedure: Paper 2's pre-registered individuation rule; pre-register each determination
  structure before computing; report Φ, band, MIP.
- Rigor as inferential reasoning (Harley & Cornelissen): the chain org → evidence → classifier inputs
  → Φ → coordination-form claim. Transparency (Pratt's four questions).
- Provisional-status disclosure: which inputs are public-documentation provisionals to be replaced
  with field data; honest flagging (no established convention — a transparency disclosure).

## §5 The five cases (within-case write-ups)

Each case follows the per-case anatomy (`research/case_study_methodology.md` §6): bounded unit/
context · data sources & chain of evidence (provisional-marked) · within-case description of how it
coordinates · the analytic operation (W–S–C model + Φ) · alternative explanations (rival codings).

- §5.1 Uber — transportation — strict mediation — Φ 2.00 — algorithmic.
- §5.2 NYSE / Nasdaq (securities exchange) — financial markets — strict mediation — Φ 2.00 — market
  institution. Twin of §5.1: same Φ, different seat.
- §5.3 Upwork — professional services — partial mediation — Φ 0.83 — algorithmic.
- §5.4 ManpowerGroup — staffing — partial mediation — Φ 0.83 — human-institutional. Twin of §5.3.
- §5.5 Amazon Mechanical Turk — crowdwork — higher-order strict mediation — Φ 3.00 (n=4) —
  algorithmic. The higher-order extension.

## §6 Cross-case synthesis

- The display matrix (Miles & Huberman): dimensions as rows, the five cases as columns ordered along
  the determination-structure spectrum (partial → strict → higher-order); read across for the
  predicted Φ pattern.
- The two equal-Φ pairs carry the structure-not-seat headline; state the equality is a modeling
  property (true once both are coded to the same structure), not an empirical discovery.
- The cases sit on populated bands of the §3 family — not cherry-picked.
- What the cases add beyond the model: that the tool does analytic work on real, documented
  coordination, and cuts against the industry-vocabulary sorting (a court-like exchange, a staffing
  firm, and a gig platform land by structure, not by sector or seat).

## §7 Discussion

- Structure, not the seat, sets the score — related to coordination theory (substrate-independence),
  brokerage (position over occupant), two-sided markets (structural criterion).
- Scope and the orthogonality move (preempt the Rahman objection): Φ measures structural
  irreducibility; opacity, power, and accountability are orthogonal contingencies layered on an
  identical structural score, not part of it. Continuity with Paper 2 §4.
- What the tool buys an analyst: a sector-blind, seat-blind placement of a coordination form on a
  graded scale, and a discipline against reading triadicity off the industry label.

## §8 Limitations

- Demonstration, not outcome-validation (Ridder); the cases illustrate and replicate, they do not
  statistically validate Φ against a coordination outcome — that remains the empirical program.
- The cases are provisional pending fieldwork; public-documentation inputs to be replaced.
- Magnitude ordinal only (Cerullo); cross-node (n=4) magnitudes not strictly comparable to the
  0–2.00 triad band.
- The equivalence claim is structural, bracketing normative/distributive consequences.
- Single modeling choices (the reads, the individuation rule) carried from Paper 2 §5 — declared,
  contestable, auditable.

## §9 Conclusion

- The graded structural typology plus the five-case demonstration: a sector- and seat-blind score of
  coordination structure that does analytic work on real corporations.
- Forward: outcome-validation (vary structure at fixed party count against an observed outcome) is
  the remaining empirical program; the matched person-level instrument is later work.

## Back matter

- Data and code availability (the `rebuild/` scripts).
- References (Crossref-verified; Paper 2's bib is the shared base).

## What the per-section deep research (Stage 2c) must deliver before the detailed outline

1. Per-organization coordination mechanisms for all five cases (the evidence base for §5).
2. Doty & Glick typology-as-theory criteria (for §3) and any precedent for a graded structural score.
3. Any org-theory precedent for importing a formal/information-theoretic measure (for §3/§7; Paper 2
   carries the borrowing discipline).
