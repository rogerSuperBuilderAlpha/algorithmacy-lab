# Q58 — Stage 2 deep research

## Question

Why does the back-channel recipient singleton carry normalized_phi exactly half the non-recipient singleton
on aligned one-sided ceiling pairs, and which IIT-4.0 cut-size asymmetry fixes the 2.0 ratio with zero
spread?

## IIT-4.0 normalization definition

IIT 4.0 defines system integrated information relative to a partition-specific normalization factor equal to
the maximal possible phi across that partition for arbitrary TPMs of the same dimensions
(`albantakis2023iit4`). The MIP minimizes normalized integrated information so that fault lines with fewer
severed pairwise interactions are not automatically favored over bridge cuts. PyPhi implements this as
`normalized_phi = phi × normalization_factor`, with `DISTINCTION_PHI_NORMALIZATION = NUM_CONNECTIONS_CUT`
and `normalization_factor = 1 / num_connections_cut()` for general k-cuts (`mayner2018pyphi`; PyPhi
`models/cuts.py` `GeneralKCut.normalization_factor`).

## Prior lab context

Q57 (#187) documented the excluded/tied normalized_phi ratio of 2.0 with zero spread but did not decompose
phi from normalization factor or count severed cut-matrix entries. Q56 (#184) showed minimum normalized_phi
predicts the official tie set. The present study tests whether the fixed ratio is a direct consequence of
the IIT-4.0 `NUM_CONNECTIONS_CUT` rule on the min-norm at-system-Phi partition representatives.

## Mechanistic prediction

If both outer cuts reach identical unnormalized phi at system level, any normalized_phi ratio must come
entirely from differing `normalization_factor` values. Under `NUM_CONNECTIONS_CUT`,
`normalization_factor = 1 / cut_ones`, so a 2:1 normalized_phi ratio implies a 2:1 inverse cut-ones ratio
(recipient severs twice as many connections in the min-norm representative). Complete partition
co-entry (#188) should share the recipient's cut geometry if the tie is normalization-driven.

## Validation gap

Results apply to deterministic n=3 Boolean models at finest grain with synchronous update. The normalization
mechanism is PyPhi's IIT-4.0 implementation, not independently verified against the Albantakis et al.
analytic normalization for these specific partition representatives.
