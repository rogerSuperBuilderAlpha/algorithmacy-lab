# Construct × scale ladder arc — working picture

A short synthesis of the literacy→algorithmacy encoding-ladder arm on
PR #739. Exact binary IIT-4.0 Φ; in-silico. Sibling arcs:
[`OMIT_ATOM_ARC.md`](OMIT_ATOM_ARC.md) (omit/motif),
[`ROLE_TARGET_GRAIN.md`](ROLE_TARGET_GRAIN.md) (role-target grain).
Residual / cascade / ternary noted only.

## Verdict in one line

**Across HMC / CMC / AI-MC and n∈{5,6}, literacy→algorithmacy flips at
last outer-party monotone full-commit with Φ=n−1; COMMIT_READ holds.
Non-monotone gates are a separate regime** (gate studies).

## Arc

| step | study | verdict | claim |
|---|---|---|---|
| 1 | [`hmc_algo_boundary/`](studies/hmc_algo_boundary/) | **COMMIT_READ_BOUNDARY** | party ∈ core iff in S’s determination and reads S; full ∧/∨-commit flips |
| 2 | [`encoding_ladder_n5/`](studies/encoding_ladder_n5/) | **FULL_JOINT_FLIP** | assist grows core; flip is last outer commit; Φ=4 (=n−1) |
| 3 | [`encoding_ladder_n6/`](studies/encoding_ladder_n6/) | **PHI_TRACKS_NM1** | same boundary form; flip Φ=5 (=n−1); no morph |
| 4 | [`encoding_ladder_gates/`](studies/encoding_ladder_gates/) | **GATE_SPLITS_LADDER** | AND/OR/NAND: Φ=n−1; XOR/XNOR: flip Φ≪n−1; MAJ/MIXED: no flip |
| 5 | [`ladder_gate_properties/`](studies/ladder_gate_properties/) | **MONO_EXTREMAL_VS_AFFINE** | A↔monotone∧wt∈{1,15}; B↔affine; else C |
| 6 | [`ladder_gate_panel/`](studies/ladder_gate_panel/) | **RULE_HOLDS_PANEL** | 448/448 stratified; rule survives |
| 7 | [`construct_ladders_n5/`](studies/construct_ladders_n5/) | **BOUNDARY_TRANSFERS** | CMC / AI-MC match HMC flip + COMMIT_READ at n=5 |
| 8 | [`construct_ladders_n6/`](studies/construct_ladders_n6/) | **PHI_TRACKS_NM1_ALL** | all three families track Φ=n−1 at n=6; no morph |
| 9 | [`construct_gates_n5/`](studies/construct_gates_n5/) | **GATE_REGIMES_TRANSFER** | CMC/AI-MC XOR→B, MAJ→C match HMC GATE_SPLITS |

## Working picture

1. **Membership law.** COMMIT_READ_BOUNDARY is the local membership
   rule: enter the major complex by joint determination∩read; leave by
   dropping from the determination even while still reading.

2. **Flip law (monotone).** On monotone extremal full-commit (AND / OR
   and their De Morgan duals), the literacy→algorithmacy boundary is
   the last outer party’s commit into the mediator. Assist alone never
   flips. Flip Φ tracks **n−1** for n∈{4,5,6} on the HMC ladder.

3. **Construct transfer.** Classical baselines keep construct signatures
   (HMC 2-core loop; CMC 1–2-core convey; AI-MC ≥3-core transform). The
   **boundary step does not**: CMC and AI-MC share
   `pre_AND → full_AND` with HMC at n=5 and again at n=6
   (BOUNDARY_TRANSFERS + PHI_TRACKS_NM1_ALL).

4. **Gate regime is orthogonal — and transfers.** Φ=n−1 is not “any
   joint bind.” It is the **monotone extremal** slice (Regime A).
   Affine full dependence (XOR / XNOR) still flips but collapses Φ
   (Regime B). Majority / mixed / mixed-polarity extremal stay dyadic
   (Regime C). CMC / AI-MC full-bind matches HMC on AND/XOR/MAJ
   ([`construct_gates_n5/`](studies/construct_gates_n5/)
   GATE_REGIMES_TRANSFER).

5. **Scope.** Exact binary IIT-4.0; designed ladders; in-silico. No
   organization measured. Omit-atom and role-target arms are separate
   motif threads — they do not revise the encoding-boundary claim.

## Best next

Optional: XNOR or mixed-polarity extremal on one CMC cell; or close
the arc. Skip another multi-role indeg. Residual / cascade / ternary
unless tooling lands.
