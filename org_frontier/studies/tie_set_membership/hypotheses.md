# Re-scoring quorum membership on tie sets instead of the single returned core

Fixed before this study's computation.

## Gap

`quorum_noise_sweep` scored membership by the one major complex `maximal_complex` returns. Later studies
(`shared_share_ties`, `five_six_node_quorum_ties`, `quorum_ratio_law`) found the top subset is usually a
tie among several subsets, so the returned core reflects tie-breaking. Its reported core shrinkage
(MAJ3 {S,P2,P3} → {S,P3}; 2of4 down to {S,P4}) and the ANY4/ALL4 exception at η = 0.4 (two states tie at
0.009264, one returning the full group) may be tie-breaking artefacts. Item 1 of
`weighted_equivalence/BACKLOG.md`.

Values already seen (disclosed): all of `quorum_noise_sweep/FINDINGS.md`; MAJ3 top tie set = three pairs
{S,Pi} at η = 0.2 and six subsets at 0.05; 2of4 = four pairs at 0.2.

## Model

The seven `quorum_noise_sweep` forms (OR3, MAJ3, AND3, ANY4, 2of4, 3of4, ALL4) under probe 464 input
noise at its eight noisy rates η ∈ {0.01, 0.02, 0.05, 0.1, 0.2, 0.3, 0.4, 0.45}. For each reachable state,
φ of every reachable subset; the top tie set is every subset within 1e-9 of the largest φ over all states
(pooled across the states where the maximum occurs).

Control: MAJ3 whole Φ 0.036624 at η = 0.2 and ANY4 maximum core φ 0.009264 at η = 0.4 (1e-6).

## Outcomes

- H1: for MAJ3, 2of4 and 3of4, the full group is never in the top tie set at any noisy rate.
- H2: for MAJ3, 2of4 and 3of4, every party appears in at least one top-tied subset at every noisy rate
  (no party is singled out once ties are counted).
- H3: for ANY4 and ALL4 at η = 0.4, the full group is in the top tie set.
- H4: for OR3 and AND3, the full group is the only member of the top tie set at every noisy rate.
- H5: for ANY4 and ALL4, the full group is in the top tie set at every noisy rate.
