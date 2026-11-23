# With four identical parties, most one-sided verdicts depend on PyPhi's arbitrary tie-break

Exact IIT 4.0 Φ (PyPhi pin `b78d0e342`), max over reachable states, threshold 1e-9. Hypotheses pushed in
`cbedad80` before computation. Control passed: AND4 Φ = 4.0.

## Setup

Five nodes P1..P4, S. Every party copies S; S' = h(P1..P4). Sample of 222 rules: all 30 non-constant
symmetric rules; 128 one-sided rules (every party pivotal at exactly one of the two consensus states;
seed 0); 64 uniform draws from all 65,536 rules (seed 1). Each scored by default and under every tied
(cause, effect) state choice.

## Results

| group | n | triadic, default | triadic, some tie choice | triadic, every tie choice | rule R | tie-dependent |
|---|---:|---:|---:|---:|---:|---:|
| symmetric | 30 | 22 | 24 | 20 | 24 | 4 |
| one-sided | 128 | 79 | 128 | 12 | 128 | 116 |
| uniform | 64 | 4 | 9 | 2 | 9 | 7 |

- Rule R mismatches against "triadic under some tie choice": 0 of 222.
- One-sided tie-dependent share: 116/128 = 0.9062, against 24/56 = 0.4286 with three parties.
- The tie-dependent symmetric rules are profiles 00110, 01100, 10011, 11001 (output by number of parties on,
  0-4). Each ranges over [0, 0.235840]. Under the default, 01100 and 10011 score 0.235840 and 00110 and
  11001 score 0, though 01100 is 00110 with the order of counts reversed (and so for the other pair).
- Interior thresholds (profiles 00011, 00111, 11000, 11100) and 00100, 11011 score 0 under every tie choice.
- AND4, OR4, NAND4, NOR4: 4.0. 01110 and 10001: 1.5. Parity (01010, 10101): 0.125.
- 18 distinct default triadic Φ values, from 0.084759 to 4.0.

| hypothesis | verdict |
|---|---|
| H1: rule R exact when ties are counted | SUPPORTED (0 mismatches) |
| H2: no symmetric rule tie-dependent | REFUTED (4 of 30) |
| H3: one-sided tie share above 0.43 | SUPPORTED (0.906) |

## Reading

As the number of identical parties grows, more cause and effect states tie, and the default verdict leans
more on PyPhi's arbitrary choice: 0 tie-dependent forms with two parties, 24 of 256 with three, 116 of 128
sampled one-sided rules with four. Rule R, scored over all tied choices, stays exact. Counts made under the
default for groups of four or more identical parties should be reported as a range over tie choices.

Full data: [results/results.json](results/results.json).
