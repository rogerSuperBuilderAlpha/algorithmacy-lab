# Q93 findings — two notions of robustness come apart

Two hypotheses confirmed, two refuted. Every triadic form sits one structural edit from collapse, and the
mediator's function fixes both its structural and its dynamical robustness — but in opposite directions. A
cheap structural margin does not predict noise survival; it inversely tracks it.

| Measure | Value |
|---|---|
| triadic forms | 24 of 256 (the 9.4% census) |
| sit on a structural edge (≥1 collapsing single-bit flip) | 24/24 |
| robustness fraction | two values only: 0.125 (16 forms) and 0.250 (8 forms) |
| noise-Φ (noise 0.1) | two values only: 1.155 (16 forms) and 0.377 (8 forms) |
| parity-mediator robustness vs monotone | 0.250 vs 0.125 |

The forms split cleanly into two classes:

| mediator | count | structural robustness | noise-Φ |
|---|---|---|---|
| monotone (AND/OR/NAND/NOR) and other | 16 | 0.125 (fragile) | 1.155 (high) |
| parity (XOR/XNOR) | 8 | 0.250 (sturdier) | 0.377 (low) |

| H | Result | Verdict |
|---|--------|---------|
| H1 | majority sit on a structural edge | confirmed (24/24) |
| H2 | the margin varies (range ≥ 0.25) | refuted (range 0.125) |
| H3 | margin predicts noise survival (rank-AUC ≥ 0.60) | refuted |
| H4 | parity mediators more robust than monotone | confirmed (0.250 vs 0.125) |

From `probe_fragility_margin.py`.

## What it says

Every triadic form in the family is one bit from collapse. All 24 have at least one single-bit truth-table
flip that turns them dyadic, so the verdict sits on a structural edge throughout. This confirms in one
measure the corpus's recurring observation that a single edge or read toggles the verdict.

The margin is nearly binary, and it is set by the mediator's function. The robustness fraction takes only
two values across all 24 forms: 0.125 for the sixteen monotone-and-other forms, 0.250 for the eight parity
forms. There is no rich gradient at n = 3, so H2 fails. Parity mediators give the structurally sturdier
triads, twice as robust to single-bit edits, which extends Finding 4 from how often parity yields a triad
to how firmly it holds one.

The structural margin does not predict noise survival, and the reason is sharper than a null. Noise-Φ also
takes exactly two values, and they line up with the margin in the opposite order: the eight parity forms
are the structurally sturdiest (robustness 0.250) and the dynamically weakest (noise-Φ 0.377), while the
sixteen monotone-and-other forms are structurally fragile (0.125) and dynamically strong (1.155). The two
notions of robustness (distance in rule space and Φ retained under output noise) anti-align through the
mediator function. The pre-registered rank-AUC was undefined here because noise-Φ is constant within each
class and the median split left one side empty; the descriptive cross-tab is the honest reading, and it
points against H3 rather than merely failing to support it.

The lesson is that a form's structural sturdiness and its dynamical sturdiness are different quantities
that a parity determination drives apart. Parity binds the triad firmly against rewiring and weakly against
noise; monotone determinations do the reverse. A cheap structural margin cannot stand in for the noise
robustness Q71 measured.

## Caveats

- **Mixed result.** H1 and H4 confirmed; H2 and H3 refuted, the latter with an inverse relationship the
  pre-registered metric could not capture (noise-Φ is constant within each class, so the rank-AUC was
  undefined).
- **n = 3 only.** The margin is near-binary on the three-node family; a richer gradient could appear at
  larger n, where more single-edit neighbours exist. Untested here.
- **In-silico.** Boolean models, exact verdicts and exact Φ. The noise model is the repo's output-noise
  mix at a single level (0.1); other noise levels are not swept.
- **One perturbation class.** Single-bit truth-table flips; multi-bit and edge-deletion perturbations are
  not measured.
