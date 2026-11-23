# Findings: switch loop member

Hypotheses fixed in [hypotheses.md](hypotheses.md) before computing. All numbers from
`run.py --write` (results/results.json), PyPhi IIT 4.0, PHI_EPS = 1e-9.

## Control (PASS)

AND gate under the AND platform gives whole 2.0 with G' = R2 and with G' = C1.

## Whole Φ

| form | G' = P (gate_census) | G' = R1 (gate_census_r1) | G' = R2 | G' = C1 |
|---|---:|---:|---:|---:|
| AND platform, AND gate (8) | 2.000000 | 2.000000 | 2.000000 | 2.000000 |
| AND platform, P ∧ ¬G (4) | 0.415037 | 0.830075 | 0.000000 | 0.000000 |
| XOR platform, AND gate (8) | 0.500000 | 2.000000 | 1.000000 | 0.500000 |

Top φ is 2.0 in all six new forms. The whole group is in the pooled top ties only for the AND gate under the
AND platform.

## Hypotheses

- H1 (AND_g04 = 0.830075 for R2 and C1): **REFUTED** (0 and 0).
- H2 (XOR_g08 = 2.0 for R2 and C1): **REFUTED** (1.0 and 0.5).
- Loop-member reading: **REFUTED**.

## Other observations (post hoc)

- Driving the switch from R2 or C1 creates a second loop that does not pass through P: G → C1 → R2 → G
  (from_R2) or G ↔ C1 (from_C1). Those small groups show up as top units: R2C1G ties for top in every
  from_R2 form, and C1G in every from_C1 form; under the XOR platform C1G is the only top unit with
  G' = C1.
- R1 is different: it only copies P and feeds nothing but P and G, so it adds no loop that skips P.
- Taken with `switch_delay`, the gain seen with G' = R1 is not explained by delay or by loop membership
  alone. What R1 has that the others lack is left open.
