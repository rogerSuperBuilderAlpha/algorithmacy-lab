# A loop through a chain of up to three people binds exactly as tightly as a direct loop

Exact IIT 4.0 Φ (PyPhi pin `b78d0e342`), every reachable subset in every reachable state. Hypotheses
pushed in `eb7a3d60` before computation. Controls passed: arm_0 is the conjunctive triad (whole Φ =
2.000000); both_1 reproduces `indirect_loops` relay_both (whole Φ = 2.000000).

## Setup

P' = R1 ∧ R2; R1' = P; C1' = P, Ci' = C(i−1), R2' = CL (R2' = P when L = 0). Tie sets are pooled over
every state where the top φ is reached, as proposed in the `indirect_loops` BACKLOG.

| form | n | reachable states | whole Φ | top φ | states at top | full group bound | pooled top ties |
|---|---:|---:|---:|---:|---:|---|---|
| arm_0 (L = 0) | 3 | 4 | 2.000000 | 2.000000 | 1 | yes | PR1, PR2, PR1R2 |
| arm_1 (L = 1) | 4 | 8 | 2.000000 | 2.000000 | 3 | yes | PR1, PR2C1, PR1R2C1 |
| arm_2 (L = 2) | 5 | 16 | 2.000000 | 2.000000 | 6 | yes | PR1, PR2C1C2, PR1R2C1C2 |
| arm_3 (L = 3) | 6 | 32 | 2.000000 | 2.000000 | 12 | yes | PR1, PR2C1C2C3, PR1R2C1C2C3 |
| both_1 | 5 | 16 | 2.000000 | 2.000000 | 6 | yes | PR1C1, PR2C2, PR1R2C1C2 |

Full data: [results/results.json](results/results.json).

## Scores

- **H1 SUPPORTED.** Whole Φ > 0 at every relay length.
- **H2 SUPPORTED.** Top φ = 2.0 at every relay length.
- **H3 SUPPORTED.** The full group is in the pooled top tie set at every relay length.
- **H4 SUPPORTED** (flat): whole Φ is 2.000000 at L = 0, 1, 2, 3.

## Reading

Lengthening the path by which the platform's decision reaches one of its readers does not weaken the
binding at all in this model: whole Φ stays at the conjunctive-triad value 2.0, and the top tie set keeps
the same shape (the direct loop {P, R1}, the relayed loop {P, R2, C1..CL}, and the whole) with the relay
chain absorbed into the relayed loop. The number of reachable states doubles with each relayer
(4, 8, 16, 32) and the number of states at the top grows (1, 3, 6, 12), but the values do not change.

## What it means

A platform's decision can pass through several people before it comes back to shape the platform's
input, and the platform and all of them still form one irreducible whole, as tightly as when the loop is
direct. For algorithmacy, the people who carry a platform's decisions along a chain are bound with it,
however long the chain is, at least up to three relayers.

## Limits

Binary, deterministic, synchronous copies; one relay arm (plus the both_1 check); L ≤ 3 (n ≤ 6). Relayers
copy without error or delay beyond one step each. Ties at the 1e-9 cutoff.

## Reproduce

```sh
python org_frontier/studies/relay_length/run.py --quick   # CI subset, ~6 s
python org_frontier/studies/relay_length/run.py --write   # full run, ~100 s
```

An AI assistant working as the open harness around IIT 4.0/PyPhi wrote the script and this report; every
number is printed by `run.py` or stored in `results/results.json`. No human review is claimed.
