# Relay length: how long can the loop through other people be?

Fixed before this study's computation.

## Gap

`indirect_loops` found that a loop closed through one other person (P → A3 → A1 → P) binds the platform at
φ = 2.0, and two such relays make the whole group irreducible (Φ = 2.0). Its BACKLOG asked whether longer
relays keep this.

## Model

Platform P reads two parties R1, R2: P' = R1 ∧ R2. R1 copies P directly (R1' = P). R2 gets P's decision
through a chain of L relayers C1..CL: C1' = P, Ci' = C(i−1), R2' = CL (L = 0 means R2' = P).

- **arm_L** for L ∈ {0, 1, 2, 3} (n = 3 + L).
- **both_1**: both readers reached through one relayer each (= `indirect_loops` relay_both, n = 5).

Exact IIT 4.0 φ of every reachable subset in every reachable state. Whole Φ = largest full-group φ over
states; top = largest subset φ over states. Tie sets are recorded at every state; the full group counts as
"bound" if it is in the top tie set at *any* state where top φ is reached (pooled), per the
`indirect_loops` BACKLOG item 1.

Controls: arm_0 is the conjunctive triad (whole Φ = 2.0); both_1 reproduces `indirect_loops` relay_both
whole Φ = 2.0.

## Outcomes (threshold 1e-9)

- H1: whole Φ > 1e-9 for every arm_L, L = 0..3.
- H2: top φ = 2.0 (within 1e-6) for every arm_L.
- H3: the full group is bound (pooled) for every arm_L.
- H4: whole Φ is non-increasing in L over arm_0..arm_3.
