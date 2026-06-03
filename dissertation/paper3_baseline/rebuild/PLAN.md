# Paper 3 rebuild — plan and scope

> **FROM-SCRATCH REWORK (author steer, superseding).** Paper 3 is being rethought and rebuilt
> from scratch with brand-new deep research and five real-organization case studies as the spine.
> The pipeline is: deep research (case-study methodology) -> foundational rework + deep research
> -> outline -> per-section deep research -> detailed outline -> write five provisional cases
> (all required sections/features) -> write the whole paper. The cases are written provisionally
> now; the author replaces provisional content with field data later.

## What stays vs. what is rebuilt

- **Stays (the computation).** `phi_core.py` (PyPhi-only, n-general), `catalog.py` +
  `analyze_catalog.py` (the 4,144-form family landscape), and `typology.py` are re-derived from
  scratch this session and verified to reproduce the recast numbers exactly. This is the model
  inherited from the ACCEPTed Paper 2; it is not re-derived again.
- **Rebuilt from scratch (the paper).** Framing, research base, architecture, and the case
  studies. The catalog and typology become supporting breadth; the five real-organization case
  studies become the spine.

## The five case studies (LOCKED slate; provisional content, field data later)

Designed to span industries and exercise the structural claim (score tracks determination
structure, not the mediator's seat) via two "same structure, different seat" twins plus a
higher-order extension. Hold party count fixed, vary structure (the cut-anchor lesson).

All five are large, publicly documented corporations. Cases use public information only (filings,
terms of service, reporting) — no insider or personal knowledge. The author replaces provisional
content with field data later.

| # | Organization | Industry | Structure | Φ band | Seat |
|---|---|---|---|---|---|
| 1 | Uber Technologies | transportation / ride-hailing | strict mediation | 2.00 | algorithmic |
| 2 | NYSE / Nasdaq (securities exchange) | financial markets | strict mediation | 2.00 | market institution (twin of #1) |
| 3 | Upwork Inc. | online labor / professional services | partial mediation | 0.83 | algorithmic |
| 4 | ManpowerGroup | staffing & workforce solutions | partial mediation | 0.83 | human-institutional (twin of #3) |
| 5 | Amazon Mechanical Turk | crowdwork / digital labor | higher-order strict | 3.00 (n=4) | algorithmic |

Replication design (per `research/case_study_methodology.md`): the two equal-Φ pairs (1≈2 at 2.00;
3≈4 at 0.83) are each a literal replication on Φ and a theoretical contrast on the mediator's seat,
carrying the structure-not-seat headline; #5 is the higher-order theoretical replication.

## Stage status

- Stage 1 (case-study methodology deep research): DONE -> `research/case_study_methodology.md`.
- Stage 2a (foundational rework deep research): DONE -> `research/framing_and_positioning.md`.
- Outline (architectural): DONE -> `OUTLINE.md`.
- Stage 2c (per-section / per-organization mechanism research): DONE ->
  `research/organization_mechanisms.md`. All five mechanisms confirmed; `cases.py` computes the
  five case models (Upwork=ManpowerGroup=0.83; Uber=NYSE/Nasdaq=2.00; MTurk=3.00).
- Computation: `phi_core.py` (PyPhi-only, n-general, passes Paper 2 controls), `catalog.py` +
  `analyze_catalog.py` (4,144-form landscape reproduces the recast exactly), `typology.py`,
  `cases.py` — all re-derived from scratch and verified.
- NEXT: detailed outline -> five provisional cases -> full paper -> Stage 4 adversarial review.
- Open framing items to handle at draft time from existing knowledge + Crossref: Doty & Glick
  typology-as-theory criteria (§3); any org-theory precedent for a graded structural score.

## Scope (what Paper 3 does)

1. **Applies the tool generally.** Enumerate the whole W–S–C model family, compute Φ for every
   wiring, show the scores fall onto a few discrete bands, and place a typology of organization
   types on the populated bands. The headline is model-internal: the score tracks the *structure*
   of how parties reach each other, not the *technology* in the middle.
2. **Runs case studies on five real organizations.** Model each from how it actually coordinates
   its parties, compute Φ, read the case. The case studies are the paper's contact with the
   world — grounded analytic applications, not a statistical outcome-calibration (the cut-anchor
   lesson below). Provisional now; field data later.

## Process (locked, same as Paper 2)

- **Full from-scratch rebuild** in `rebuild/`, depending only on PyPhi. No import of prior
  project code. `phi_core.py` re-derives the measure n-generally and reproduces Paper 2's
  controls exactly at n=3 (0.000 / 0.830 / 2.000).
- **Compute, don't assert.** Every Φ is computed and reproducible from a `rebuild/` script.
- **Nagel style** (CLAUDE.md) for the draft. ORM register.
- **Stage 4 adversarial review** to close — three hostile reviewers, reproduce every number,
  iterate to ACCEPT, as Paper 2 did.

## The cut-anchor lesson (carries into the case-study design)

The earlier rideshare "anchor" was cut because, in the pooling model, Φ = k + 1 for a pool of
k riders, so Φ was a linear function of party count. Correlating it with pooling friction only
validated the party-count axis — the one axis you do not need Φ to see. The novel content of
the scale is that determination *structure* separates forms at a *fixed* party count (parity
0.50 vs partial 0.83 vs strict 2.00 at n=3). So the case studies must hold party count fixed
and vary structure, or they repeat the cut anchor's mistake. The cut scripts live in
`../exploratory/` and their numbers are cited nowhere.

## Stages and status

- **Stage 0 — scaffolding + foundation.** DONE. `rebuild/` created; `phi_core.py` (PyPhi-only,
  n-general) passes the Paper 2 control self-check.
- **Stage 1 — general application (catalog + typology).** IN PROGRESS.
  - `catalog.py` re-derived (PyPhi-only via `phi_core`); full run reproduces the recast
    landscape (target: ~44% reducible, seven non-zero bands, strict mediation the strongest
    driver, R² ≈ 0.20, parity caution). `analyze_catalog.py` reports the bands, the OLS, and
    the Cerullo caution.
  - `typology.py` re-derived; reproduces the recast placements exactly (0 / 0.50 / 0.83 / 2.00
    / 3.00; court = Uber = ATS at 2.00; staffing = broker = Upwork at 0.83).
- **Stage 2 — live-organization case studies.** TO DO. The new contribution. Design below.
- **Stage 3 — draft.** TO DO. Nagel style; intro -> unit -> model + general application ->
  case studies -> discussion -> limits. Every number from the rebuild scripts.
- **Stage 4 — adversarial review.** TO DO.

## Stage 2 design — live-organization case studies (to refine with author)

Goal: a handful of case studies on real, named organizations where the tool does analytic work,
built to exercise the *structure* axis (fixed party count, varied determination), not party
count. Candidate shape, to confirm:

- **Pick real organizations with documented coordination**, not toy archetypes. Model each from
  public evidence of how it actually routes its parties (terms of service, how a match/dispatch
  is committed, whether the parties can reach each other off-platform). Pre-register the
  determination structure before computing, as the typology does.
- **Exercise the structure axis at fixed n.** Contrast organizations that have the same party
  count but different determination structure — e.g. a strict-mediation platform vs a
  partial-mediation marketplace in the same sector — so the case shows Φ separating them by
  structure, the scale's novel content.
- **Exercise the human-vs-algorithmic contrast on real instances**, not only by construction.
  The healthcare staffing agency is a strong candidate (insider knowledge available) against an
  algorithmic platform of the same partial-mediation shape.
- **Read each case for where structure cuts against appearance** — a form that looks dyadic but
  is strict (Paper 2's false dyad), or looks triadic but factors (the exhibit), if a real
  instance can be documented.
- **Honesty bounds:** the case studies are grounded analytic applications, not outcome
  validation. State plainly that no Φ here is regressed against an observed coordination
  outcome; that remains future work. Magnitude read ordinally only (Cerullo).

Open questions for the author:
- Which real organizations to study, and how many.
- How much to lean on the author's own healthcare-staffing access as a deep case vs documented
  public platforms as breadth.
- Whether any case can responsibly claim a structure-cuts-against-appearance reading on a real
  named org, or whether that stays a modeled illustration.

## Paper 2 coherence note (act on after Paper 3 claims are settled)

Paper 2 (ACCEPTed) says "Calibration against coordination outcomes is Paper 3" (abstract, §4,
§10, §11). Paper 3 does case-study application, not statistical outcome-calibration. Once
Paper 3's claims are fixed, soften Paper 2's forward-promise to match — e.g. "applying and
case-studying the instrument is Paper 3; outcome-calibration is the empirical program it opens."
Flag, do not touch Paper 2 yet.
