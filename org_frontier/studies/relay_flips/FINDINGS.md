# Flipping the message costs nothing; gating it from outside splits the whole

Exact IIT 4.0 Φ (PyPhi pin `b78d0e342`), every reachable subset in every reachable state. Hypotheses
pushed in `0a088f3f` before computation. Control passed: copy_1 reproduces `relay_length` arm_1 (whole Φ =
2.000000).

## Setup

P reads R1, R2; R1' = P. AND platform: P' = R1 ∧ R2; XOR platform: P' = R1 ⊕ R2.
copy_1: C1' = P, R2' = C1. flip_1: C1' = ¬P. flip_2: C1' = ¬P, C2' = ¬C1, R2' = C2.
gated_1: C1' = P ∧ G, G' = G. unequal_1_2: R1 via one copying relayer A1, R2 via two (B1, B2).

| form | n | reachable states | whole Φ | top φ | states at top | full group bound | pooled top ties |
|---|---:|---:|---:|---:|---:|---|---|
| copy_1 | 4 | 8 | 2.000000 | 2.000000 | 3 | yes | PR1, PR2C1, PR1R2C1 |
| flip_1 | 4 | 8 | 2.000000 | 2.000000 | 3 | yes | PR1, PR2C1, PR1R2C1 |
| flip_2 | 5 | 16 | 2.000000 | 2.000000 | 6 | yes | PR1, PR2C1C2, PR1R2C1C2 |
| gated_1 | 5 | 16 | 0.000000 | 2.000000 | 5 | no | PR1, PR2C1, PR1R2C1 |
| xor_copy_1 | 4 | 8 | 0.500000 | 0.500000 | 8 | yes | PR1R2C1 |
| xor_flip_1 | 4 | 8 | 0.500000 | 0.500000 | 8 | yes | PR1R2C1 |
| unequal_1_2 | 6 | 32 | 2.000000 | 2.000000 | 12 | yes | PR1A1, PR2B1B2, PR1R2A1B1B2 |

gated_1 by state: the gate G alone is the top unit (φ = 1.0, its self-loop) in 11 of 16 states. Top φ =
2.0 is reached in the other 5. The gated loop PR2C1 and the four-member group PR1R2C1 reach it only when
G = 1 (PR2C1 in 2 states, PR1R2C1 in 1). G is never in a φ = 2.0 tie, and the full five-member group has
φ = 0 in every state.

Full data: [results/results.json](results/results.json).

## Scores

- **H1 SUPPORTED.** flip_1 whole Φ = copy_1 whole Φ = 2.000000.
- **H2 SUPPORTED.** flip_2 whole Φ = 2.000000.
- **H3 SUPPORTED.** xor_flip_1 whole Φ = xor_copy_1 whole Φ = 0.500000.
- **H4 REFUTED.** gated_1 whole Φ = 0, and G is in no pooled top tie.
- **H5 SUPPORTED.** unequal_1_2 whole Φ = 2.000000 and the full group is bound.

## Reading

A relayer that inverts the message is, for Φ, the same as one that copies it: the values, tie sets and
state counts are identical for one flip, two flips, and under both the AND and the XOR platform rule. One
reading (not tested separately) is that the relayer's state is still fully set by the platform's. A gate breaks that. G reads
only itself, so nothing in the system affects it, and cutting the system's influence on G costs nothing:
the five-member whole is reducible in every state. The loop G gates still binds at 2.0 when G is on, but
as a part that leaves G out. Unequal arm lengths (one relayer on one side, two on the other) change
nothing: whole Φ stays 2.0.

## What it means

How a go-between passes a platform's decision along (straight or reversed) does not change how tightly
the platform and its people are bound. A go-between who also answers to an outside switch that nothing
inside the system touches makes the whole group come apart. The loop still holds when the switch is on,
but the switch itself is not part of the bound unit.

## Limits

Binary, deterministic, synchronous; one gate type (AND with a self-looping source); n ≤ 6. Ties at 1e-9.

## Reproduce

```sh
python org_frontier/studies/relay_flips/run.py --quick   # CI subset, ~4 s
python org_frontier/studies/relay_flips/run.py --write   # full run, ~85 s
```

An AI assistant working as the open harness around IIT 4.0/PyPhi wrote the script and this report; every
number is printed by `run.py` or stored in `results/results.json`. No human review is claimed.
