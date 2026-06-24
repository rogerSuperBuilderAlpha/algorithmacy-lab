# q183 — findings

The bridge module `org_frontier/qualitative/disagreement_phi.py` reads two party accounts of one
coordination as two rule sets and returns a spread tuple. Both validation hypotheses hold on
synthetic controls.

## Instrument control

The faithful triad `[x1, x0&x2, x1]` reads `triadic` with max Φ_MIP = 2.000000. PASS.

## Spread on the controls

| control                  | verdict_agreement | phi_gap  | core_jaccard | both_verdicts      |
|--------------------------|-------------------|----------|--------------|--------------------|
| identity (A == B)        | 1                 | 0.000000 | 1.000000     | (triadic, triadic) |
| divergent A=triad B=dyad | 0                 | 2.000000 | 0.666667     | (triadic, dyadic)  |
| divergent A=dyad B=triad | 0                 | 2.000000 | 0.666667     | (dyadic, triadic)  |

The divergent pair genuinely diverges (verdict_agreement = 0, phi_gap = 2.0), so the symmetry
check is not vacuous. The core Jaccard of 0.666667 reflects that the triad core is {W,S,C} and
the dyad core drops C, leaving a two-of-three overlap.

## Verdicts

- **H1 (zero anchor): SUPPORTED.** Identical accounts return verdict_agreement = 1,
  phi_gap = 0.0, core_jaccard = 1.0.
- **H2 (symmetry): SUPPORTED.** Swapping account A and account B leaves all three spread
  components unchanged.

## Scope

The accounts are synthetic rule sets. The construct validated is divergence between two stated
accounts; no real coordination is measured. Results are on synthetic data.
