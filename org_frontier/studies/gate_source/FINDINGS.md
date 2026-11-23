# A switch the group can reach rejoins the whole; an OR gate keeps it out either way

Exact IIT 4.0 Φ (PyPhi pin `b78d0e342`), every reachable subset in every reachable state. Hypotheses
pushed in `93c512f7` before computation. Control passed: and_self reproduces `relay_flips` gated_1
(whole Φ = 0, top φ = 2.0).

## Setup

P' = R1 ∧ R2, R1' = P, R2' = C1. AND gate: C1' = P ∧ G; OR gate: C1' = P ∨ G. G' = G (self), P, R1 or C1.

| form | reachable states | whole Φ | states with whole φ > 0 | top φ | states at top | full group bound | pooled top ties |
|---|---:|---:|---:|---:|---:|---|---|
| and_self | 16 | 0.000000 | 0 | 2.000000 | 5 | no | PR1, PR2C1, PR1R2C1 |
| and_from_P | 12 | 2.000000 | 2 | 2.000000 | 4 | yes | PR1, PR2C1, PR2C1G, PR1R2C1, PR1R2C1G |
| and_from_R1 | 18 | 2.000000 | 4 | 2.000000 | 6 | yes | PR1, PR2C1, PR1R2C1, PR1R2C1G |
| and_from_C1 | 12 | 2.000000 | 1 | 2.000000 | 5 | yes | C1G, PR1, PR2C1, PR2C1G, PR1R2C1, PR1R2C1G |
| or_self | 16 | 0.000000 | 0 | 2.000000 | 5 | no | PR1, PR2C1, PR1R2C1 |
| or_from_P | 12 | 0.000000 | 0 | 2.000000 | 3 | no | PR1 |

Full data: [results/results.json](results/results.json).

## Scores

- **H1 SUPPORTED.** and_from_P whole Φ = 2.000000.
- **H2 SUPPORTED.** and_from_R1 whole Φ = 2.000000.
- **H3 SUPPORTED.** and_from_C1 whole Φ = 2.000000.
- **H4 SUPPORTED.** or_self whole Φ = 0.
- **H5 REFUTED.** or_from_P whole Φ = 0.
- **H6 SUPPORTED.** In all three forms with whole Φ > 0, G is in a pooled top tie (the full group
  PR1R2C1G in each; also PR2C1G for and_from_P and and_from_C1, and C1G for and_from_C1).

## Reading

With an AND gate, it does not matter which group member drives the switch (the platform, the reader R1,
or the relayer itself): each restores the whole to Φ = 2.0, the same value as the ungated loop, and the
switch joins the tightest-bound groups. A self-held switch is reached by nothing in the system, and the
whole stays at 0. The OR gate does not follow this pattern. Driving the switch from P (so the relayer
passes on "P now or P one step ago") still leaves whole Φ at 0, and the relayed loop PR2C1 drops out of
the top tie set; only the direct loop PR1 reaches φ = 2.0. We did not test why.

## What it means

A go-between who waits on an outside switch splits the group only if nothing in the group drives the
switch. Once a group member drives it, the switch is bound in with them. This holds for the "pass it on
only if the switch is on" rule. For a "pass it on if either says so" rule, wiring the switch to the
platform did not bring the group back together in this test.

## Limits

Binary, deterministic, synchronous; one platform rule (AND); n = 5; one OR form driven from inside. Ties
at 1e-9.

## Reproduce

```sh
python org_frontier/studies/gate_source/run.py --quick   # CI subset, ~6 s
python org_frontier/studies/gate_source/run.py --write   # full run, ~18 s
```

An AI assistant working as the open harness around IIT 4.0/PyPhi wrote the script and this report; every
number is printed by `run.py` or stored in `results/results.json`. No human review is claimed.
