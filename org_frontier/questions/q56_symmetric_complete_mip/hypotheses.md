# Q56 — Stage 3 hypotheses (fixed before computation)

Five working hypotheses on why symmetric bijective parity ceiling pairs adopt complete MIP {W,S,C} while
aligned one-sided ceiling pairs adopt outer-party singleton seams. Written and committed before any test
runs. Grows from Q55 probe #178.

## H1 — Complete-only official tie set on symmetric ceiling pairs
- **Claim:** Every one of the sixteen symmetric bijective ceiling pairs (symmetric_xor and symmetric_xnor on
  eight matched implication forms) has an official MIP tie set containing only `3 parts: {W,S,C}` — no
  two-part outer-party partition appears in `sia.ties`.
- **H0:** At least one symmetric ceiling pair includes a two-part outer-party partition (`{W,SC}` or
  `{WS,C}`) in the official tie set.
- **Predicted outcome:** Sixteen of sixteen symmetric ceiling pairs with tie set exactly `{W,S,C}`; zero with
  any two-part outer-party tie. H0 refuted only if the count is perfect.

## H2 — One outer-party tie plus complete on aligned one-sided ceiling pairs
- **Claim:** Every one of the sixteen aligned one-sided bijective ceiling pairs has an official tie set
  containing exactly one outer-party two-part partition (`{W,SC}` or `{WS,C}`) together with the complete
  partition `3 parts: {W,S,C}`.
- **H0:** At least one aligned one-sided ceiling pair has zero or two outer-party partitions in the official
  tie set, or lacks the complete partition in the tie set.
- **Predicted outcome:** Sixteen of sixteen one-sided ceiling pairs with tie-set size two: one outer-party
  two-part plus complete. H0 refuted on any exception.

## H3 — Directional coupling symmetry distinguishes topology classes
- **Claim:** Symmetric ceiling pairs restore full directional coupling symmetry (in-degree equals out-degree
  for each party, and W mirrors C); aligned one-sided ceiling pairs break that symmetry on the outer parties.
- **H0:** At least one symmetric ceiling pair lacks directional symmetry, or at least one one-sided ceiling
  pair has full W/C directional symmetry.
- **Predicted outcome:** Sixteen of sixteen symmetric ceiling pairs directionally symmetric; zero of sixteen
  one-sided ceiling pairs directionally symmetric. H0 refuted on any crossover.

## H4 — Dual outer-party cuts at system Phi but excluded from official ties on symmetric pairs
- **Claim:** On every symmetric ceiling pair, both outer-party two-part partitions `{W,SC}` and `{WS,C}`
  achieve system Phi at the max-Phi state, yet neither appears in the official tie set — IIT-4.0 tie-break
  filters both when they tie at equal normalized existence.
- **H0:** At least one symmetric ceiling pair fails to have both outer-party cuts at system Phi, or has at
  least one outer-party cut in the official tie set.
- **Predicted outcome:** Sixteen of sixteen symmetric pairs with both outer-party types at system Phi and
  zero outer-party entries in official ties. H0 refuted on any violation.

## H5 — Minimum normalized-phi rule predicts official tie set on all ceiling pairs
- **Claim:** The official MIP tie set equals the set of partition types achieving the minimum normalized_phi
  among all partitions at system Phi — on symmetric pairs only complete qualifies; on one-sided pairs one
  outer-party cut plus complete qualify.
- **H0:** The minimum-normalized-phi rule disagrees with the official tie set on at least one of the
  thirty-two ceiling pairs.
- **Predicted outcome:** Thirty-two of thirty-two ceiling pairs match the predicted tie set from the
  minimum-normalized-phi rule. H0 refuted on any mismatch.
