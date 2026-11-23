# Findings: switch delay

Hypotheses fixed in [hypotheses.md](hypotheses.md) before computing. All numbers from
`run.py --write` (results/results.json), PyPhi IIT 4.0, PHI_EPS = 1e-9.

## Controls (PASS)

from_P and from_R1 reproduce `gate_census` and `gate_census_r1`.

## Whole Φ (largest full-group φ over reachable states)

| form | G' = P | G' = R1 | G' = D, D' = P |
|---|---:|---:|---:|
| AND platform, AND gate (code 8) | 2.000000 | 2.000000 | 1.000000 |
| AND platform, P ∧ ¬G (code 4) | 0.415037 | 0.830075 | 1.000000 |
| XOR platform, AND gate (code 8) | 0.500000 | 2.000000 | 0.500000 |

Reachable states: 12 / 18 (24 for XOR) / 24. Top φ is 2.0 in every AND-platform form and in from_R1 XOR;
0.5 in from_P XOR and via_D XOR.

## Hypotheses

- H1 (via_D AND_g04 = 0.830075): **REFUTED** (1.000000).
- H2 (via_D XOR_g08 = 2.0): **REFUTED** (0.500000, the from_P value).
- H3 (via_D AND_g08 = 2.0): **REFUTED** (1.000000).
- Delay explanation (H1 and H2): **REFUTED**.

## Other observations (post hoc)

- With the delay line, the two AND-platform forms give identical results: whole 1.0, 24 states, top 2.0
  in 7 states, pooled ties PR1, PR2C1, PR1R2C1, PR2C1GD. The whole six-node group is never in the top
  ties (full_bound N), whereas G' = P and G' = R1 with the AND gate both put the whole group in them.
- Under the XOR platform the delay line behaves like G' = P: whole 0.5, and the whole group ties for top
  (PR1R2C1, PR1R2C1GD).
- So the gain in `gate_census_r1` is not explained by the switch's copy of P being one step older. The
  extra node D is not equivalent to reusing R1, which is already in the platform's loop.
