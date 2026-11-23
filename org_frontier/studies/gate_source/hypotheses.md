# Gate source: does the switch rejoin the group if the group can reach it?

Fixed before this study's computation.

## Gap

`relay_flips` found that a relayer gated by an outside switch G (C1' = P ∧ G, G' = G) makes the whole
five-member group reducible (Φ = 0 in all 16 states), and G never joins a top tie. Its BACKLOG asked
whether the whole comes back when the switch itself is driven by someone inside the group.

## Model

P' = R1 ∧ R2, R1' = P, R2' = C1 (as `relay_flips` gated_1). The relayer is gated: C1' = P ∧ G (AND gate)
or C1' = P ∨ G (OR gate). The gate's own input varies:

- **and_self** (control, = `relay_flips` gated_1): G' = G.
- **and_from_P**: G' = P.
- **and_from_R1**: G' = R1.
- **and_from_C1**: G' = C1.
- **or_self**: C1' = P ∨ G, G' = G.
- **or_from_P**: C1' = P ∨ G, G' = P.

n = 5 each. Exact IIT 4.0 φ of every reachable subset in every reachable state; whole Φ = largest
full-group φ over states; top tie sets pooled over all states where top φ is reached.

Control: and_self whole Φ = 0 and top φ = 2.0 (reproduces `relay_flips` gated_1).

## Outcomes (threshold 1e-9)

- H1: and_from_P whole Φ > 1e-9.
- H2: and_from_R1 whole Φ > 1e-9.
- H3: and_from_C1 whole Φ > 1e-9.
- H4: or_self whole Φ ≤ 1e-9.
- H5: or_from_P whole Φ > 1e-9.
- H6: in every form with whole Φ > 1e-9, G is in at least one pooled top tie subset.
