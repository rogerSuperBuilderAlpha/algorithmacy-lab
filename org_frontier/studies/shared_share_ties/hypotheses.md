# Shared-error share sweep and tie enumeration: hypotheses and methods

Fixed before the study's computation. Disclosure: one API smoke test was run first to confirm that
`pyphi.Subsystem` + `new_big_phi.sia` returns per-subset φ: MAJ3, independent errors, e = 0.2, state
(0,0,0,0). It showed the three {S,Pi} pairs at φ = 0.146494864, the three {S,Pi,Pj} triples at
0.096570797 and the full group at 0.036623716. H4 and H5 below are scored on all cases, including that
one; readers can discount it.

## Gap

`quorum_correlated_noise/` showed MAJ3 has Φ = 0 under fully shared reading errors and Φ > 0 under a
half-shared mixture. Its backlog item 4 asks how Φ moves as the shared share of the error grows. Item 2
(carried from `quorum_noise_sweep/`) asks whether the single core `maximal_complex` returns ({S,P3},
{S,P4}, …) hides a symmetric tie, and whether the full group ever ties for the maximum.

## Part A: shared-share sweep

Three-party OR3 and MAJ3 (same construction as the two earlier studies). Each reading's flip is a shared
flip (probability a, same for all three readings) XOR an independent flip (probability b), with a = s·e
and b = (e − a)/(1 − 2a), so the marginal error per reading is e. s = 0 is the independent model, s = 1
the fully shared model. Grid: e ∈ {0.1, 0.2}, s ∈ {0, 0.25, 0.5, 0.75, 0.9, 1}. 24 cases.

Controls: marginal error equals e; s = 0 TPM equals probe 464's `input_tpm`; s = 1 TPM equals
`quorum_correlated_noise` `common` TPM (both entrywise, 1e-12).

- H1: at each e, MAJ3 whole Φ strictly decreases as s increases across the grid.
- H2: MAJ3 whole Φ > 1e-9 at every s < 1, and ≤ 1e-9 at s = 1.
- H3: at each e, OR3 whole Φ strictly increases as s increases across the grid.

## Part B: tie enumeration

Independent errors. MAJ3 at e ∈ {0.05, 0.1, 0.2}; 2of4 (four parties, quota 2) at e ∈ {0.1, 0.2}. For
every reachable state, compute system φ (`new_big_phi.sia`) of every nonempty node subset.

- H4: in every state, the subsets attaining the maximum φ (within 1e-9) are exactly one full symmetry
  class: all subsets of one size k smaller than the full group that contain S (e.g. all three {S,Pi}),
  and nothing else.
- H5: in every state the full group's φ is below the maximum by more than 1e-9.

Descriptive: the size of the maximizing class at each case.
