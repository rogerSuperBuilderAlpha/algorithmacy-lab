# With five identical parties, every one-sided verdict depends on PyPhi's arbitrary tie-break

Exact IIT 4.0 Φ (PyPhi pin `b78d0e342`), max over reachable states, threshold 1e-9. Hypotheses pushed in
`058b5923` before computation.

## Setup

Six nodes P1..P5, S. Every party copies S; S' = h(P1..P5). Sample: all 62 non-constant symmetric rules and
128 one-sided rules (every party pivotal at exactly one consensus state; seed 0, same procedure as
`four_party_ties`). Each scored by default and under every tied (cause, effect) state choice.

## Results

| group | n | triadic, default | triadic, some tie choice | triadic, every tie choice | rule R | tie-dependent |
|---|---:|---:|---:|---:|---:|---:|
| symmetric | 62 | 42 | 48 | 34 | 48 | 14 |
| one-sided | 128 | 75 | 128 | 0 | 128 | 128 |

- Rule R mismatches against "triadic under some tie choice": 0 of 190.
- Tie-dependent share of one-sided rules by group size: 3 parties 24/56 = 0.43, 4 parties 116/128 = 0.906,
  5 parties 128/128 = 1.0. No one-sided rule is triadic under every tie choice; the largest one-sided Φ
  under any choice is 0.25.
- Tie-dependent symmetric rules (output by number of parties on, 0-5): 000110, 001101, 001110, 010011,
  011000, 011001, 011100, 100011, 100110, 100111, 101100, 110001, 110010, 111001. Share 14/62 = 0.226,
  against 4/30 = 0.133 with four parties and 0 with three.
- Four more symmetric rules keep their verdict but change value with the tie choice: 010001, 011101,
  100010, 101110 (each between 0.299560 and 0.402506).
- AND5 and its relabelings (100000, 011111, 111110): 5.0. Profiles 011110 and 100001: 2.0.
- 34 distinct default triadic Φ values, from 0.028451 to 5.0.

| hypothesis | verdict |
|---|---|
| H1: rule R exact when ties are counted | SUPPORTED (0 mismatches) |
| H2: one-sided tie share above 0.906 | SUPPORTED (1.0) |
| H3: symmetric tie share above 0.133 | SUPPORTED (0.226) |
| H4: AND5 Φ = 5.0 | SUPPORTED |

## Reading

The trend from `four_party_ties` continues. With five identical parties, the default PyPhi verdict for
every sampled one-sided rule is set by the arbitrary tie-break: each one is triadic under some tie choice
and under none of them under every choice. Rule R stays exact when ties are counted. Any count of binding
forms for groups of this size should be reported as a range over tie choices.

Full data: [results/results.json](results/results.json).
