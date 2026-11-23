# Two-sided platform: two buyers and two sellers around one mediator

Fixed before this study's computation.

## Gap

Topology studies so far put one party per role around each mediator (`rival_platforms`,
`two_triad_shared_member`, `shared_mediator_k`) or used symmetric k-party hubs (`hub_floor_uniqueness`,
`quorum_*`). None splits the parties into two *sides* whose members are interchangeable within a side,
the way a marketplace has buyers on one side and sellers on the other. Here the mediator's rule
treats sides differently from individuals.

## Model

Five binary nodes: platform P, buyers B1, B2, sellers S1, S2. Every party copies P (next state = P).
The platform's rule varies:

- **all_four** (control): P' = B1 ∧ B2 ∧ S1 ∧ S2 (conjunctive 4-party hub).
- **any_one** (control): P' = B1 ∨ B2 ∨ S1 ∨ S2 (disjunctive 4-party hub).
- **side_match**: P' = (B1 ∨ B2) ∧ (S1 ∨ S2): a trade happens if at least one buyer and one seller show up.
- **fixed_pairs**: P' = (B1 ∧ S1) ∨ (B2 ∧ S2): only pre-assigned buyer–seller pairs can trade.
- **one_per_side**: P' = (B1 ⊕ B2) ∧ (S1 ⊕ S2): exactly one buyer and exactly one seller.
- **both_sides_full**: P' = (B1 ∧ B2) ∨ (S1 ∧ S2): either side fully present.

For each reachable state, exact IIT 4.0 φ of every reachable subset (`new_big_phi.reachable_subsystems`).
Whole Φ = largest full-group φ over states. Top = largest subset φ over all states; top tie set = subsets
within 1e-9 of top at the state where it occurs.

Controls: the 3-node conjunctive triad (W,S,C with S'=W∧C, parties copy S) gives Φ = 2.0.

## Outcomes (threshold 1e-9)

- H1: all_four and any_one each give whole Φ = 4.0 with the full five-node group in the top tie set
  (hub landmark Φ = n − 1).
- H2: side_match puts the full five-node group in its top tie set.
- H3: side_match whole Φ is strictly below 4.0.
- H4: fixed_pairs does not put the full group in its top tie set; its top ties are buyer–seller trios
  {P, Bi, Si}.
- H5: one_per_side whole Φ > 1e-9 and the full group is in its top tie set.
