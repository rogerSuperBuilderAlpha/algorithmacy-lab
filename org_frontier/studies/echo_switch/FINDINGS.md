# Findings: echo switch

Hypotheses fixed in [hypotheses.md](hypotheses.md) before computing. All numbers from
`run.py --write` (results/results.json), PyPhi IIT 4.0, PHI_EPS = 1e-9.

## Whole Φ

| gate | G' = P | G' = R3 (echo the platform reads) |
|---|---:|---:|
| AND (8) | 1.000000 | 1.000000 |
| P ∧ ¬G (4) | 0.415037 | 0.415037 |

Reachable states: 12 (G' = P), 18 (G' = R3). Top φ is 2.0 in all four forms, and the whole six-node group
is never in the pooled top ties. With P ∧ ¬G the top units are PR1, PR3 and PR1R3 for both drivers.

## Hypotheses

- H1 (P ∧ ¬G: G' = R3 above G' = P): **REFUTED** (equal, 0.415037).
- H2 (AND gate: equal): **SUPPORTED** (1.0 and 1.0).
- Echo reading: **REFUTED**.

## Other observations (post hoc)

- With the three-way AND platform, even the AND gate gives whole Φ 1.0, not the 2.0 of the two-input AND
  platform, and the whole group never ties for top.
- The P ∧ ¬G value 0.415037 is the same number seen with G' = P on the two-input AND platform
  (`gate_census`).
- Together with `switch_delay` and `switch_loop_member`, three explanations of the R1 gain have now failed:
  delay, loop membership, and being an echo the platform reads. The gain may be specific to the
  two-reader platform.
