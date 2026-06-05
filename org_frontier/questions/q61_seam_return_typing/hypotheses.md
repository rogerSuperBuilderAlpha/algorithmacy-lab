# Q61 — Stage 3 hypotheses (fixed before computation)

Five working hypotheses cross-tabulating official MIP singleton seam against Q43 return-path
sequential/reciprocal typing on the sixteen aligned one-sided ceiling pairs. Written and committed before
any test runs.

## H1 — Seam tracks return-path type bijection
- **Claim:** Official singleton seam and return-path type correspond perfectly on every pair: W singleton
  ({W,SC}) iff sequential, C singleton ({WS,C}) iff reciprocal.
- **H0:** At least one pair's seam disagrees with its return-path type.
- **Predicted outcome:** 16/16 seam–type matches; 0 mismatches.

## H2 — Co-extensive partitions
- **Claim:** Seam and return-path type induce the same two-way partition of the panel (eight sequential
  and eight reciprocal cells identical under both labels).
- **H0:** Seam and type partitions differ on at least one pair assignment.
- **Predicted outcome:** Partition equality 16/16; both labels yield 8+8 split with perfect correspondence.

## H3 — Seam not finer than type
- **Claim:** No pair shares a return-path type with another pair of different singleton seam — seam is not a
  strict refinement of type.
- **H0:** At least one return-path type class contains both W and C singleton seams.
- **Predicted outcome:** 0 within-type seam heterogeneity; sequential class all W seam, reciprocal class all
  C seam.

## H4 — Seam not coarser than type
- **Claim:** No pair shares a singleton seam with another pair of different return-path type — seam is not a
  strict coarsening of type.
- **H0:** At least one singleton seam class contains both sequential and reciprocal types.
- **Predicted outcome:** 0 within-seam type heterogeneity; W seam class all sequential, C seam class all
  reciprocal.

## H5 — Seam recovers verdict-lost discrimination
- **Claim:** While max_phi is uniform at 2.0 across the panel (#204), official singleton seam splits the
  panel into the same sequential/reciprocal halves return-path typing names.
- **H0:** Seam subpanels disagree with return-path subpanels on at least one pair.
- **Predicted outcome:** W-seam subpanel = sequential subpanel (8/8); C-seam subpanel = reciprocal subpanel
  (8/8); max_phi spread 0 across all four named subpanels.
