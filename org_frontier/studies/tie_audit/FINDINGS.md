# PyPhi's arbitrary tie-breaking does not move any verdict in the lab's main panels

Ties between equally maximal cause or effect states are everywhere (3,984 of 4,096 three-node forms have
at least one), but re-scoring under every tied choice changes no verdict and no max Φ in any panel audited.
Exact IIT 4.0 Φ (PyPhi pin `b78d0e342`). Hypotheses pushed in `92b1cc26` before computation. Controls
passed: PyPhi's default choice reproduces 2,288/4,096 and 24/256 triadic, and the atlas's whole-system Φ
for all 47 forms with at most five nodes.

## Setup

`new_big_phi.system_intrinsic_information` returns one cause state and one effect state and notes "State
ties are arbitrarily broken (for now)"; the ties are kept on the result. For every reachable state we ran
`new_big_phi.sia` once for each tied (cause, effect) pair and kept the minimum and maximum Φ. A form is
tie-dependent if its max-over-states Φ is positive under some choice and zero under another.

| panel | forms | triadic (PyPhi default) | triadic under some tie | triadic under every tie | tie-dependent | forms with tied states |
|---|---:|---:|---:|---:|---:|---:|
| three-node family (every node reads the other two) | 4,096 | 2,288 | 2,288 | 2,288 | 0 | 3,984 |
| strict-mediation slice | 256 | 24 | 24 | 24 | 0 | 256 |
| named forms (classifier 5, Q215 10) | 15 | 7 | 7 | 7 | 0 | 12 |
| coordination-logic atlas, ≤ 5 nodes | 47 | 24 | 24 | 24 | 0 | 44 |

The max Φ itself also did not change: in every form of every panel, the minimum and maximum over tie
choices agree (difference ≤ 1e-9).

Full data: [results/results.json](results/results.json).

## Scores

- **H1 SUPPORTED.** No strict-mediation form is tie-dependent.
- **H2 SUPPORTED.** No named form is tie-dependent.
- **H3 SUPPORTED.** 0 of 4,096 three-node forms are tie-dependent (threshold was under 205).
- **H4 SUPPORTED.** No atlas verdict (47 forms, ≤ 5 nodes) is tie-dependent.

## What it means

The tie problem found in `consensus_pivotality` is real but local. It appeared in four-node forms where
three parties copy the same mediator. It does not reach the three-node panels the lab's central claims
rest on, the named forms the manuscripts cite, or the atlas. Those verdicts can be reported as they are.
New studies with several interchangeable parties should report the tie range, since that is where ties
did change answers.

## Limits

Ties are enumerated for the whole system's cause and effect states only, not for ties inside the
partition search or among mechanisms. Atlas forms with six nodes were skipped for run time. The audit
covers max-over-states Φ; per-state values at non-maximal states were not compared.

## Reproduce

```sh
python org_frontier/studies/tie_audit/run.py --quick   # CI subset, ~2 s
python org_frontier/studies/tie_audit/run.py --write   # full run, ~2.3 min on 4 cores
```

An AI assistant working as the open harness around IIT 4.0/PyPhi wrote the script and this report; every
number is printed by `run.py` or stored in `results/results.json`. No human review is claimed.
