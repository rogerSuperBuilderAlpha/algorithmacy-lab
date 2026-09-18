# Omit-atom arc — working picture

A short synthesis of the fixed_k omit / discrete-Φ thread on PR #739.
Exact binary IIT-4.0 Φ; in-silico. Residual / cascade / ternary noted only.

## Verdict in one line

**Discrete motif-ruled Φ.** Size **morphs the rule form once** (singleton →
band at n=5→n=6; derangement rung → cycle-type split). From n=6→n=7 the
**band grammar holds** (#8 BAND_GRAMMAR_HOLDS). It does **not** open a
continuum, and it does **not** blur into within-class mixing (#42
SCALE_MORPHS).

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
| 8 | [`omit_cycle_morph_n7/`](studies/omit_cycle_morph_n7/) | BAND_GRAMMAR_HOLDS (#8) | n=7 indeg (0,1,1,1,1,1,2): Φ=12 vs 14 bands; grammar stabilizes |

## Working picture

1. **Atoms are motif-ruled.** Nearby Φ values (5 vs 6; 8 vs 9; 12 vs 14)
   track omit digraph features — cycle type, and for derangements the
   partition type — once indegree signature is fixed.

2. **Size morphs the rule once, then holds.** At n=5 the incomplete-core
   separator is a **singleton** 3-cycle motif. At n=6 it is a **multi-class
   band** of cycle types. At n=7 the same band grammar persists (Φ=12 vs
   14). Derangements likewise go from one rung (Φ=9) to a **cycle-type
   split** (12 vs 14). The Φ spectrum stays discrete relative to designed
   landmarks; Φ=14 is a new atom, not a spray.

3. **Purity survives scale.** Within a (cycles, recip) class, uniformity
   samples do not mix Φ as n grows (#42, #8). Softness is across classes
   (coarser bands), not inside them.

4. **Scope.** Conjunctive AND; fixed_k omit (k=n−2); n∈{5,6,7}. Band purity is
   **fingerprint-dependent**: indeg (0,1,1,1,1,2) was pure under cycle type;
   indeg (0,0,1,1,2,2) mixed until **role-target grain**
   ([`indeg_002122_grain/`](studies/indeg_002122_grain/) ROLE_TARGETS_LAW:
   t_targets=(1,1)→Φ=12; (3,)+z_targets=(2,2)→Φ=8). Construct arm:
   [`hmc_algo_boundary/`](studies/hmc_algo_boundary/) COMMIT_READ_BOUNDARY;
   [`encoding_ladder_n5/`](studies/encoding_ladder_n5/) FULL_JOINT_FLIP;
   [`encoding_ladder_n6/`](studies/encoding_ladder_n6/) PHI_TRACKS_NM1
   (same boundary; flip Φ = n−1 for n∈{4,5,6});
   [`encoding_ladder_gates/`](studies/encoding_ladder_gates/) GATE_SPLITS_LADDER
   (AND/OR/NAND only; XOR/XNOR Φ≪n−1; MAJ/MIXED no flip);
   [`ladder_gate_properties/`](studies/ladder_gate_properties/)
   MONO_EXTREMAL_VS_AFFINE (A↔monotone∧wt∈{1,15}; B↔affine; else C);
   [`ladder_gate_panel/`](studies/ladder_gate_panel/) RULE_HOLDS_PANEL
   (448/448 stratified stress-test);
   [`indeg_001113_grain/`](studies/indeg_001113_grain/) Z_TARGETS_LAW
   (role-target grain generalizes; z_targets splits (2,) on (0,0,1,1,1,3));
   [`indeg_000123_grain/`](studies/indeg_000123_grain/) JOINT_TZ_LAW
   (both t and z vary on (0,0,0,1,2,3); joint grain; z-cut sufficient).
   Role-target synthesis: [`ROLE_TARGET_GRAIN.md`](ROLE_TARGET_GRAIN.md).

## Best next

Omit scale lane: **V3 #9** (interior atoms at n=7–8) is the natural
companion now that #8 closed the band-grammar question. Graded×topo
**V3 #11** if switching lanes. Construct/gate arc already sealed
([`CONSTRUCT_LADDER_ARC.md`](CONSTRUCT_LADDER_ARC.md)). Role-target:
[`ROLE_TARGET_GRAIN.md`](ROLE_TARGET_GRAIN.md). Skip another multi-role
indeg on the same family. Residual / cascade / ternary unless tooling
lands.
