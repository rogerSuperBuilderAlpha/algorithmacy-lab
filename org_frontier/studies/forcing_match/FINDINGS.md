# The forcing rule fails: negating the gate's output changes nothing

Exact IIT 4.0 Φ (PyPhi pin `b78d0e342`), every reachable subset in every reachable state. Hypotheses
pushed in `4b96e197` before computation. Control passed: andP_and reproduces `gate_source` and_from_P
(whole Φ = 2.000000).

## Setup

P reads R1, R2; R1' = P; R2' = C1; C1' = gate(P, G); G' = P.

| form | platform | gate | predicted | reachable states | whole Φ | states with whole φ > 0 | top φ | full bound | pooled top ties |
|---|---|---|---|---:|---:|---:|---:|---|---|
| andP_and | AND | AND | (control) | 12 | 2.000000 | 2 | 2.000000 | yes | PR1, PR2C1, PR2C1G, PR1R2C1, PR1R2C1G |
| andP_nor | AND | NOR | bound | 12 | 0.000000 | 0 | 2.000000 | no | PR1 |
| andP_nand | AND | NAND | not bound | 12 | 2.000000 | 2 | 2.000000 | yes | PR1, PR2C1, PR2C1G, PR1R2C1, PR1R2C1G |
| orP_nand | OR | NAND | bound | 12 | 0.000000 | 0 | 2.000000 | no | PR1 |
| orP_nor | OR | NOR | not bound | 12 | 2.000000 | 2 | 2.000000 | yes | PR1, PR2C1, PR2C1G, PR1R2C1, PR1R2C1G |
| xorP_or | XOR | OR | bound | 12 | 0.500000 | 4 | 0.500000 | yes | PR1R2C1, PR1R2C1G |

Full data: [results/results.json](results/results.json).

## Scores

- **H1 REFUTED.** andP_nor whole Φ = 0.
- **H2 REFUTED.** andP_nand whole Φ = 2.000000.
- **H3 REFUTED.** orP_nand whole Φ = 0.
- **H4 REFUTED.** orP_nor whole Φ = 2.000000.
- **H5 SUPPORTED.** xorP_or whole Φ = 0.500000.
- **Forcing-match rule REFUTED** (0 of 4).

## Reading

The proposed rule looked at the value the gate's output is forced to. The results show the output value
does not matter: a NAND gate gives exactly the same numbers as an AND gate (the tie sets match too), and
a NOR gate the same as an OR gate. That fits `relay_flips`, where a relayer that negates the message
changed nothing. What separates bound from unbound is how the gate combines P with the switch. "Both
needed" (AND/NAND) goes with the AND platform; "either suffices" (OR/NOR) goes with the OR platform. This
restores the simpler matching pattern from `or_gate_source` for AND/OR platforms, now with output
negation shown not to matter: 18 inside-driven AND/OR forms across four studies with no exception. This
reading was made after the run. The XOR platform stays bound at 0.5 with an OR gate as well, its third
gate type.

## What it means

The terms that need to line up between a platform and a switch-dependent go-between are about how each
combines its two inputs (both needed vs. either is enough). Whether the go-between then passes the result
on straight or reversed does not matter. For a platform that says "go" when exactly one input is on, they
do not need to line up at all in the cases tried.

## Limits

Binary, deterministic, synchronous; n = 5; switch driven by P only; one XOR form. Ties at 1e-9.

## Reproduce

```sh
python org_frontier/studies/forcing_match/run.py --quick   # CI subset, ~7 s
python org_frontier/studies/forcing_match/run.py --write   # full run, ~28 s
```

An AI assistant working as the open harness around IIT 4.0/PyPhi wrote the script and this report; every
number is printed by `run.py` or stored in `results/results.json`. No human review is claimed.
