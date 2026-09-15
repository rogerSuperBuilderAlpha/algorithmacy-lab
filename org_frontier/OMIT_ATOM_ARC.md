# Omit-atom arc — working picture

A short synthesis of the fixed_k omit / discrete-Φ thread on PR #739.
Exact binary IIT-4.0 Φ; in-silico. Residual / cascade / ternary noted only.

## Verdict in one line

**Discrete motif-ruled Φ.** Size **morphs the rule form** (singleton → band;
derangement rung → cycle-type split). It does **not** open a continuum, and
it does **not** blur into within-class mixing (#42 SCALE_MORPHS).

## Arc

| step | study | verdict | claim |
|---|---|---|---|
| 1 | [`random_coupling_ensemble/`](studies/random_coupling_ensemble/) | PARTIAL_N5 | n=5 fixed_k hits new atoms 5 and 9 beside landmarks |
| 2 | [`fixed_k_atoms_n5/`](studies/fixed_k_atoms_n5/) | NEW_RUNGS | Φ=9 = all 44 derangement omits; Φ=5 recurs on non-derang 4-cores |
| 3 | [`omit_motif_phi5/`](studies/omit_motif_phi5/) | MOTIF_DISCRIMINANT | Φ=5 iff indeg (0,1,1,1,2) ∧ (3,) ∧ recip0; siblings → 6 |
| 4 | [`omit_lift_n6/`](studies/omit_lift_n6/) | LAWS_MORPH | n=5 laws morph at n=6: ders split 12/14; M3 incomplete persists; sibling uniqueness fails |
| 5 | [`derangement_33_phi14/`](studies/derangement_33_phi14/) | PHI14_IS_33 | among !6, Φ=14 iff cycle type 3+3; other types → 12 |
| 6 | [`same_indeg_band_n6/`](studies/same_indeg_band_n6/) | BAND_DISCRIMINANT | within indeg (0,1,1,1,1,2), Φ=9 iff {(5,),(2,3)}; else 8; classes pure |
| 7 | [`discriminant_scale_blur/`](studies/discriminant_scale_blur/) | SCALE_MORPHS (#42) | purity holds across n; law morphs singleton→band; not blur |

## Working picture

1. **Atoms are motif-ruled.** Nearby Φ values (5 vs 6; 8 vs 9; 12 vs 14)
   track omit digraph features — cycle type, and for derangements the
   partition type — once indegree signature is fixed.

2. **Size morphs the rule, not the discreteness.** At n=5 the incomplete-core
   separator is a **singleton** 3-cycle motif. At n=6 it is a **multi-class
   band** of cycle types. Derangements likewise go from one rung (Φ=9) to a
   **cycle-type split** (12 vs 14). The Φ spectrum stays discrete relative to
   designed landmarks (L5 / L6); Φ=14 is a new atom, not a spray.

3. **Purity survives scale.** Within a (cycles, recip) class, uniformity
   samples do not mix Φ as n grows (#42). Softness is across classes
   (coarser bands), not inside them.

4. **Scope.** Conjunctive AND; fixed_k omit (k=n−2); n∈{5,6}. One closed
   same-indeg family per n. No organization measured. HMC/CMC/AI-MC at n>3
   and other indeg signatures are parallel arms.

## Best next

Another indeg signature band; or HMC/CMC/AI-MC at n>3 (literal construct
reading of #42). Skip residual / cascade / ternary unless tooling lands.
