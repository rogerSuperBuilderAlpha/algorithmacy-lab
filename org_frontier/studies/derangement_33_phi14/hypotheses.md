# derangement_33_phi14 — hypotheses (fixed before computing)

**Question.** Among n=6 fixed_k=4 omit-derangements (!6=265), is **Φ=14
exactly the cycle-type 3+3 class**, or do other !6 types / non-derangements
also hit 14?

**Already known (`omit_lift_n6` LAWS_MORPH).**
- Designed witnesses: cycle types 6, 4+2, 2+2+2 → Φ=12; **3+3 → Φ=14**
  (two designed forms, both full-core).
- Class sizes: (6,)=120, (2,4)=90, (3,3)=40, (2,2,2)=15.
- Each cycle type is a single S6-conjugacy class; Φ is relabeling-invariant,
  so dense uniformity samples test the law without full 265×~45s enum.
- Ternary / residual-cascade / #42 noted only.

**Universe.** Binary exact IIT-4.0. Conjunctive AND. n=6, fixed_k=4.
Dense sample: N_33 of type 3+3; N_other per remaining type; thin non-derangement
fixed_k=4 for Φ=14 contamination. Candid: not full !6 enum.

## H1 — Φ=14 ⟺ 3+3 among tested derangements

Every tested 3+3 derangement has core Φ=14 (full n_core=6), and every tested
non-3+3 derangement has core Φ ≠ 14. Null: some 3+3 ≠ 14, or some other type = 14.

## H2 — other !6 cycle types also hit 14

At least one tested derangement with cycle type in {(6,), (2,4), (2,2,2)} has
core Φ=14. Null: none do. (Adversarial to the exclusive law.)

## H3 — non-derangements can hit 14

At least one tested non-derangement fixed_k=4 omit form has core Φ=14.
Null: none in the thin sample.

## H4 — 3+3 class size and conjugacy

!6 partitions as (6,)=120, (2,4)=90, (3,3)=40, (2,2,2)=15, and all 3+3
perms share one conjugacy class (structural check, pre-Φ).

## H5 — 3+3 uniformity

All tested 3+3 forms share Φ=14 with full six-node core (dense sample, not
one-off).
