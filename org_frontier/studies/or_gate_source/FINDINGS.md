# The relayer's gate has to match the platform's rule

Exact IIT 4.0 Φ (PyPhi pin `b78d0e342`), every reachable subset in every reachable state. Hypotheses
pushed in `941f278b` before computation. Control passed: or_from_P reproduces `gate_source` (whole Φ = 0,
top φ = 2.0).

## Setup

P reads R1, R2; R1' = P; R2' = C1. AND platform P' = R1 ∧ R2 or OR platform P' = R1 ∨ R2. AND gate C1' =
P ∧ G or OR gate C1' = P ∨ G. G copies the named member.

| form | platform | gate | G copies | reachable states | whole Φ | states with whole φ > 0 | top φ | states at top | full bound | pooled top ties |
|---|---|---|---|---:|---:|---:|---:|---:|---|---|
| or_from_P | AND | OR | P | 12 | 0.000000 | 0 | 2.000000 | 3 | no | PR1 |
| or_from_R1 | AND | OR | R1 | 18 | 0.000000 | 0 | 2.000000 | 3 | no | PR1 |
| or_from_R2 | AND | OR | R2 | 18 | 0.000000 | 0 | 2.000000 | 12 | no | PR1, R2C1G |
| or_from_C1 | AND | OR | C1 | 12 | 0.000000 | 0 | 2.000000 | 7 | no | C1G, PR1 |
| and_from_R2 | AND | AND | R2 | 18 | 2.000000 | 1 | 2.000000 | 8 | yes | PR1, PR2C1, R2C1G, PR1R2C1, PR1R2C1G |
| orP_and_from_P | OR | AND | P | 12 | 0.000000 | 0 | 2.000000 | 3 | no | PR1 |
| orP_or_from_P | OR | OR | P | 12 | 2.000000 | 2 | 2.000000 | 4 | yes | PR1, PR2C1, PR2C1G, PR1R2C1, PR1R2C1G |

Full data: [results/results.json](results/results.json).

## Scores

- **H1 REFUTED.** or_from_R1 whole Φ = 0.
- **H2 REFUTED.** or_from_R2 whole Φ = 0.
- **H3 REFUTED.** or_from_C1 whole Φ = 0.
- **H4 SUPPORTED.** and_from_R2 whole Φ = 2.000000.
- **H5 REFUTED.** orP_and_from_P whole Φ = 0.
- **H6 SUPPORTED.** orP_or_from_P whole Φ = 2.000000.

## Reading

Across this study and `gate_source`, an inside-driven switch brings the whole group back (Φ = 2.0) in
every case where the gate's rule is the same as the platform's rule (AND with AND: switch driven by P, R1,
R2 or C1; OR with OR: driven by P). In every case where the two rules differ (AND platform with OR gate,
four drivers; OR platform with AND gate, one driver) whole Φ is 0. This matching pattern was noticed after
the run. It was not a pre-registered hypothesis, and it rests on ten inside-driven forms (five matched, five mismatched) with one
OR–OR case. In the mismatched AND-platform forms the relayed loop PR2C1 never reaches the top; with the
switch driven by R2 or C1, a gate-and-relayer pair (R2C1G, C1G) ties with PR1 at 2.0 instead.

## What it means

Whether a switch-dependent go-between stays bound with the platform depends on more than who works the
switch. In these models, it also depends on whether the go-between combines the platform's message with
the switch the same way the platform combines its inputs ("both" with "both", "either" with "either").

## Limits

Binary, deterministic, synchronous; n = 5; one OR–OR form; the matching pattern is post hoc. Ties at 1e-9.

## Reproduce

```sh
python org_frontier/studies/or_gate_source/run.py --quick   # CI subset, ~6 s
python org_frontier/studies/or_gate_source/run.py --write   # full run, ~16 s
```

An AI assistant working as the open harness around IIT 4.0/PyPhi wrote the script and this report; every
number is printed by `run.py` or stored in `results/results.json`. No human review is claimed.
