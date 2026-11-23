# Placement equality: when does party-side noise give the same Φ as mediator-side noise?

Fixed before this study's computation.

## Gap

`noise_placement` found that OR3's whole Φ under party-only noise equals its mediator-only value to six
decimals at r = 0.05, 0.1 and 0.2 (1.854569 at r = 0.1), but not at r = 0.4, and that MAJ3 under
party-only noise has whole Φ 0 at every rate. Item 1 of `noise_placement/BACKLOG.md` asks whether the
equality holds for other quorum rules and why. Values already seen before this file: all OR3 and MAJ3
numbers in `noise_placement/FINDINGS.md`. No AND3 or four-party party-side value has been computed.

## Model

Same as `noise_placement`: mediator S commits a counting quota over its readings of the parties; each
party copies S. Two placements at rate r ∈ {0.05, 0.1, 0.2, 0.4}:

- **mediator**: S misreads each party independently with probability r (probe 464 `input_tpm`).
- **party**: S reads exactly; each party flips its copy of S with probability r.

Forms: AND3 (3 parties, quota 3); 1of4, 2of4, 3of4, 4of4 (4 parties). OR3 and MAJ3 are rerun as controls
(must reproduce `noise_placement` to 1e-6). Whole Φ = largest full-group φ over reachable states; we also
record the state where it peaks.

## Outcomes (threshold 1e-9; equality tolerance 1e-6)

- H1: AND3 whole Φ equals OR3 whole Φ under each placement and rate (global bit-flip duality).
- H2: 1of4 party-only whole Φ equals its mediator-only whole Φ at r = 0.05 and 0.1.
- H3: 2of4 and 3of4 party-only whole Φ ≤ 1e-9 at every rate (the MAJ3 result extends to interior quotas).
- H4: for OR3 at r = 0.05, 0.1, 0.2, whole Φ peaks at the same state under both placements.
- H5: for 4of4 (AND4), party-only equals mediator-only at r = 0.05 and 0.1 (should match 1of4 by duality).
