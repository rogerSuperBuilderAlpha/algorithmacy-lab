# A platform that matches sides factors completely; only all-or-none platforms hold together

Exact IIT 4.0 Φ (PyPhi pin `b78d0e342`), every reachable subset in every reachable state. Hypotheses
pushed in `1e35d61b` before computation. Control passed: the conjunctive triad (S' = W ∧ C, parties copy S)
gives whole Φ = 2.000000.

## Setup

Five binary nodes: platform P, buyers B1, B2, sellers S1, S2. Every party copies P. Because the parties
copy P, only 4 states are reachable (P free, all four parties equal). "Top" is the largest subset φ over
those states; ties are subsets within 1e-9 of it.

| platform rule | P' | whole Φ | top subset φ | full group in top |
|---|---|---:|---:|---|
| all_four (control) | B1 ∧ B2 ∧ S1 ∧ S2 | 4.000000 | 4.000000 | yes (only tie) |
| any_one (control) | B1 ∨ B2 ∨ S1 ∨ S2 | 4.000000 | 4.000000 | yes (only tie) |
| side_match | (B1 ∨ B2) ∧ (S1 ∨ S2) | 0 | 0 | no |
| fixed_pairs | (B1 ∧ S1) ∨ (B2 ∧ S2) | 0 | 0 | no |
| one_per_side | (B1 ⊕ B2) ∧ (S1 ⊕ S2) | 0 | 0 | no |
| both_sides_full | (B1 ∧ B2) ∨ (S1 ∧ S2) | 0 | 0 | no |

Full data: [results/results.json](results/results.json).

## Scores

- **H1 SUPPORTED.** Both controls reach the hub landmark Φ = n − 1 = 4.0 with the full five-node group as
  the only top subset.
- **H2 REFUTED.** side_match does not bind the full group; no subset is irreducible at all.
- **H3 SUPPORTED** (trivially): side_match whole Φ is 0, below 4.0.
- **H4 REFUTED.** fixed_pairs does not form buyer–seller trios {P, Bi, Si}; every subset has φ = 0.
- **H5 REFUTED.** one_per_side has whole Φ = 0.

## Why every subset is zero

In a reachable state all four parties hold the same value. Under each side-aware rule, that common value
fixes P's next state no matter what any single party does (e.g. side_match with everyone at 1 gives P' = 1
even if one buyer drops to 0; with everyone at 0, P' = 0 even if one buyer rises to 1). So no part of the
system makes a difference to another part from the states the system actually visits, and every cut costs
nothing. The all-or-none rules are the exceptions: under AND (everyone at 1) or OR (everyone at 0), each
single party is pivotal. This is the same pattern as the 2-of-3 majority (`threshold_majority_template`,
#10/#67/#117), extended from vote-counting rules to rules built from sides and pairs.

## What it means

A marketplace rule that only needs "some buyer and some seller" has slack: no single participant is ever
decisive from the states this system reaches, so in this model the platform and its users do not form an
irreducible whole. The rules that do hold together are the ones where every participant can be decisive.
For algorithmacy, a binding third party integrates the people it coordinates only where each of them can
change its verdict; the side structure of a two-sided market, by itself, does not create that.

## Limits

Deterministic, synchronous, binary; parties only copy the platform (so 4 reachable states); one size (2+2).
Earlier studies show mediator-side misreading can make a 2-of-3 majority slightly integrated
(`quorum_noise_sweep`); that was not tested here.

## Reproduce

```sh
python org_frontier/studies/two_sided_platform/run.py --quick   # CI subset, ~5 s
python org_frontier/studies/two_sided_platform/run.py --write   # full run, ~10 s
```

An AI assistant working as the open harness around IIT 4.0/PyPhi wrote the script and this report; every
number is printed by `run.py` or stored in `results/results.json`. No human review is claimed.
