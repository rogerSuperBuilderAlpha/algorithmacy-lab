# Every two-input relayer rule, checked: the pre-registered rules hold on all 48 forms

Exact IIT 4.0 Φ (PyPhi pin `b78d0e342`), every reachable subset in every reachable state. Hypotheses
pushed in `5a8acf16` before computation. Controls passed: the AND gate gives whole Φ 2.000000 under the
AND platform and 0.500000 under the XOR platform.

## Setup

P reads R1, R2; R1' = P; R2' = C1; C1' = f(P, G); G' = P. Gate code: the output for input (P, G) is bit
2·P + G of the code (AND = 8, OR = 14, NAND = 7, NOR = 1, XOR = 6, XNOR = 9, G = 5, P = 12).

Whole Φ by platform and gate class:

| gate class (codes) | AND platform | OR platform | XOR platform |
|---|---|---|---|
| constant (0, 15) | 0, 0 | 0, 0 | 0, 0 |
| P-only (3 = ¬P, 12 = P) | 0, 0 | 0, 0 | 0, 0 |
| G-only (5 = G, 10 = ¬G) | 2.0, 2.0 | 2.0, 2.0 | 0.5, 0.5 |
| parity (6 = XOR, 9 = XNOR) | 2.0, 2.0 | 2.0, 2.0 | 0.5, 0.5 |
| single-odd, odd at P = 1, G = 1 (7, 8) | 2.0, 2.0 | 0, 0 | 0.5, 0.5 |
| single-odd, odd at P = 1, G = 0 (4, 11) | 0.415037, 0.415037 | 0, 0 | 0.5, 0.5 |
| single-odd, odd at P = 0, G = 1 (2, 13) | 0, 0 | 0.415037, 0.415037 | 0.5, 0.5 |
| single-odd, odd at P = 0, G = 0 (1, 14) | 0, 0 | 2.0, 2.0 | 0.5, 0.5 |

Whole Φ > 0 in 28 of 48 forms: 8 under AND, 8 under OR, 12 under XOR. Every form with whole Φ = 2.0 or 0.5
has the full group in the pooled top tie set. No form with whole Φ = 0.415037 does (there only PR1 reaches
the top φ of 2.0). Per-form tie sets and state counts are in [results/results.json](results/results.json)
and printed by `run.py`.

## Scores

- **H1 SUPPORTED.** P-value rule holds on all 16 single-odd AND/OR forms.
- **H2 SUPPORTED.** Constant and P-only gates: whole Φ = 0 on all 12 forms.
- **H3 SUPPORTED.** G-only gates: 2.0 under AND and OR, 0.5 under XOR.
- **H4 SUPPORTED.** All 8 single-odd gates under XOR: whole Φ = 0.5.
- **H5 SUPPORTED.** Parity gates: 2.0 under AND and OR, 0.5 under XOR.

## Reading

Output negation never changes a value: every gate and its negation (codes c and 15 − c) give identical
whole Φ, which generalizes `relay_flips` and `forcing_match` to all 16 rules. A relayer that ignores the
switch (P-only) gives whole Φ 0. The switch G then reads P but nothing reads G, so cutting it off costs
nothing. A relayer that ignores P (G-only) is just a second copying step and gives the full value (2.0, or
0.5 under XOR), as in `relay_length`. Parity gates also give the full value on every platform. For the
eight single-odd gates under AND and OR, the P-value rule from `odd_input` holds without exception. The
odd pattern on the diagonal ((1, 1) for AND, (0, 0) for OR) gives 2.0, and off the diagonal it gives
0.415037. Under XOR, every gate that uses both inputs or only G gives 0.5, and the rule type does not
matter.

## What it means

For a go-between who combines a platform's message with a switch the platform controls, this study covers
every possible two-input rule. The group stays irreducible when the go-between depends on the switch at
all (ignoring it splits the group). For "both" and "either" platforms, the go-between also has to treat
the platform's own message the way the platform listens for it. Whether it passes the result on straight
or reversed never matters.

## Limits

Binary, deterministic, synchronous; n = 5; the switch always copies P. Ties at 1e-9.

## Reproduce

```sh
python org_frontier/studies/gate_census/run.py --quick   # CI subset, ~15 s
python org_frontier/studies/gate_census/run.py --write   # full run, ~4.5 min
```

An AI assistant working as the open harness around IIT 4.0/PyPhi wrote the script and this report; every
number is printed by `run.py` or stored in `results/results.json`. No human review is claimed.
