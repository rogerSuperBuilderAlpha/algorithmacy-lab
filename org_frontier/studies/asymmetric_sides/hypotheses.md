# Asymmetric sides: which side does a two-sided platform bind?

Fixed before this study's computation.

## Gap

`two_sided_platform` found that every side-aware rule on a 2 + 2 platform (match, fixed pairs, one per
side, one full side) has φ = 0 for every subset when parties just copy the platform, while all-or-none
rules give Φ = 4.0. Two open items from its BACKLOG: (a) a rule that is strict on one side and loose on the
other, and (b) parties that also read their own side, not only the platform.

## Model

Platform P, buyers B1, B2 (and B3 when n = 6), sellers S1, S2. Binary, deterministic, synchronous.

Panel A (parties copy P):

- **strict_buyers**: P' = (B1 ∧ B2) ∧ (S1 ∨ S2)
- **strict_sellers**: P' = (B1 ∨ B2) ∧ (S1 ∧ S2) (mirror of strict_buyers)
- **strict_buyers_3**: n = 6, P' = (B1 ∧ B2 ∧ B3) ∧ (S1 ∨ S2)
- **loose_or_strict**: P' = (B1 ∧ B2) ∨ S1 ∨ S2

Panel B (side_match platform P' = (B1 ∨ B2) ∧ (S1 ∨ S2); parties also read their side partner):

- **side_link_and**: Bi' = P ∧ Bj, Si' = P ∧ Sj (j the other member of the same side)
- **side_link_or**: Bi' = P ∨ Bj, Si' = P ∨ Sj

Exact IIT 4.0 φ of every reachable subset in every reachable state (`new_big_phi.reachable_subsystems`).
Whole Φ = largest full-group φ over states; top = largest subset φ over states; top ties within 1e-9.

Controls: conjunctive triad Φ = 2.0; `two_sided_platform` side_match with copying parties gives top 0.

## Outcomes (threshold 1e-9)

- H1: strict_buyers has a top subset φ > 1e-9 and every top tie contains both buyers and no seller
  (the platform binds the strict side only).
- H2: strict_sellers mirrors strict_buyers: same whole Φ and same top φ (within 1e-9).
- H3: strict_buyers_3 top φ is larger than strict_buyers top φ.
- H4: loose_or_strict whole Φ ≤ 1e-9.
- H5: side_link_and has whole Φ > 1e-9 (a side link restores integration to side_match).
- H6: side_link_or has whole Φ > 1e-9.
