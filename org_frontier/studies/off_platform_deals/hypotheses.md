# Off-platform deals: buyer–seller links that bypass a two-sided platform

Fixed before this study's computation.

## Gap

`two_sided_platform` showed a side_match platform (P' = (B1 ∨ B2) ∧ (S1 ∨ S2)) with copying parties has
φ = 0 everywhere; `asymmetric_sides` showed same-side links (a buyer reads the other buyer) make the whole
integrated (Φ = 0.830075) but leave the sides as the tightest units. Its BACKLOG asked about *cross-side*
links, where a buyer reads a seller directly — a deal made partly off the platform — and whether the
strict-side law (top φ 2.0 → 3.0 for two → three strict buyers) continues to four.

## Model

Platform P, buyers B1, B2, sellers S1, S2 (n = 5). P' = (B1 ∨ B2) ∧ (S1 ∨ S2) unless noted.

- **cross_and**: B1' = P ∧ S1, S1' = P ∧ B1, B2' = P ∧ S2, S2' = P ∧ B2.
- **cross_or**: B1' = P ∨ S1, S1' = P ∨ B1, B2' = P ∨ S2, S2' = P ∨ B2.
- **one_pair_off**: B1' = S1, S1' = B1 (this pair ignores P entirely); B2, S2 copy P.
- **one_pair_and**: B1' = P ∧ S1, S1' = P ∧ B1; B2, S2 copy P.
- **strict_buyers_4** (n = 7): P' = (B1 ∧ B2 ∧ B3 ∧ B4) ∧ (S1 ∨ S2); parties copy P.

Exact IIT 4.0 φ of every reachable subset in every reachable state. Whole Φ = largest full-group φ over
states; top = largest subset φ over states; top ties within 1e-9.

Controls: conjunctive triad Φ = 2.0; `asymmetric_sides` side_link_and whole Φ = 0.830075.

## Outcomes (threshold 1e-9)

- H1: cross_and has whole Φ > 1e-9, and its top ties are the buyer–seller pairs {B1, S1}, {B2, S2}.
- H2: cross_or's top ties all contain P.
- H3: one_pair_off's top ties do not contain P, and {B1, S1} is among them.
- H4: one_pair_and has whole Φ > 1e-9.
- H5: strict_buyers_4 top φ = 4.0 (within 1e-6) with {P, B1, B2, B3, B4} as the only top tie.
