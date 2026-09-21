# interior_atoms_n78 — hypotheses (fixed before computing)

**Question (RESEARCH_AGENDA_V3 #9).** Do the discrete Φ atoms of V2 #18 /
`interior_ring_pool` at n≤6 **sprout new interior atoms at n=7–8**, or only
**thicken existing landmark multiplicities**?

**Already known (cited, not reopened).**
- **`interior_ring_pool` (#19):** NO_INTERMEDIATE_LAW — designed interiors
  sit on discrete full-core steps; at n=6: **4 → 6 → 8 → 9 → 12 → 30**.
  No log/√n law.
- **`random_coupling_ensemble` (#18):** DISCRETE_LANDMARKS — random AND
  couplings land on those atoms (n=4 all on {2,4,6,12}; n=5 mostly on
  L5 with rare new 5/9 outside designed ring–pool families).
- Ring Φ=4 for n≥4; pool Φ=n(n−1).
- V3 #8 BAND_GRAMMAR_HOLDS — omit cycle-type band grammar stabilizes at
  n=7 (separate omit lane; cited only).

**Gap.** Whether lifting the **same designed families** (multihub, chordal
ring, k-regular, lattice strip) to n=7–8 yields **new** full-core Φ values
strictly between ring and pool that are absent from the n≤6 landmark set,
or only **recalls** known interior atoms (multiplicity thickens with n).

**Universe.** Binary exact IIT-4.0. Conjunctive AND. Designed interiors
only (not random ensembles). n ∈ {7, 8}.

## Landmark prior (n≤6 designed full-core)

From `interior_ring_pool` census:

| atom | role |
|---|---|
| 4 | ring pole |
| 6, 8, 9, 12 | **interior landmarks** |
| 12 / 20 / 30 | pool poles at n=4/5/6 |

**L_interior_prior** = {6, 8, 9, 12}.

A full-core triadic cell at n∈{7,8} with ring < core Φ < pool is:
- **prior atom** if core Φ ∈ L_interior_prior (within PHI_EPS);
- **new atom** otherwise.

Pool poles n(n−1) at n=7,8 (42, 56) are expected n-dependent poles, not
interior atoms.

## H1 — anchors hold at n=7

ring(7)=4.0 and pool(7)=42. (Lean n=8 ring lift is optional; ring Φ=4 for
n≥4 is already established.) Null: n=7 anchor fails.

## H2 — full-core interiors exist at n=7 or n=8

At least one designed cell (multihub / chordal / k-regular / strip) is
full-core triadic with ring < Φ < pool. Null: only poles or collapses.

## H3 — new interior atoms sprout

At least one full-core interior cell has core Φ ∉ L_interior_prior.
Null: every full-core interior lands on {6, 8, 9, 12}.

## H4 — panel verdict

- H1 ∧ H2 ∧ H3 → `SPROUTS_NEW_ATOMS`
- H1 ∧ H2 ∧ ¬H3 → `THICKENS_LANDMARKS`
- H1 ∧ ¬H2 → `COLLAPSES_ONLY`
- else → `CONTROLS_FAIL`
