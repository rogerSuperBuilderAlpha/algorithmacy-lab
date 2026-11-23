# Relay flips: what if the person passing the message on changes it?

Fixed before this study's computation.

## Gap

`relay_length` found that a platform's loop closed through a chain of 0–3 relayers keeps whole Φ at exactly
2.0. Every relayer there copied the message. Its BACKLOG asked about relayers that do something else, and
about arms of unequal length. This study changes what the relayer does.

## Model

Platform P reads R1 and R2. R1 copies P (R1' = P). R2 gets P's decision through relayers.

- **copy_1** (control, = `relay_length` arm_1): P' = R1 ∧ R2, C1' = P, R2' = C1. n = 4.
- **flip_1**: as copy_1 but the relayer flips the message: C1' = ¬P.
- **flip_2**: two relayers that each flip: C1' = ¬P, C2' = ¬C1, R2' = C2. n = 5.
- **gated_1**: the relayer passes the message only if an outside gate G is on: C1' = P ∧ G, G' = G. n = 5.
- **xor_copy_1**: copy_1 with the platform rule P' = R1 ⊕ R2.
- **xor_flip_1**: flip_1 with the platform rule P' = R1 ⊕ R2.
- **unequal_1_2**: P' = R1 ∧ R2, R1 reached through one copying relayer, R2 through two. n = 6.

Exact IIT 4.0 φ of every reachable subset in every reachable state, as in `relay_length`. Whole Φ = largest
full-group φ over states; top = largest subset φ over states; full group "bound" if it is in the top tie set
at any state where top φ is reached (pooled).

Control: copy_1 whole Φ = 2.0 (reproduces `relay_length` arm_1).

## Outcomes (threshold 1e-9, equality within 1e-6)

- H1: flip_1 whole Φ equals copy_1 whole Φ (a flip only relabels the message).
- H2: flip_2 whole Φ equals copy_1 whole Φ (two flips cancel).
- H3: xor_flip_1 whole Φ equals xor_copy_1 whole Φ.
- H4: gated_1 whole Φ > 1e-9 and G is in at least one pooled top tie subset.
- H5: unequal_1_2 whole Φ = 2.0 and the full group is bound (pooled).
