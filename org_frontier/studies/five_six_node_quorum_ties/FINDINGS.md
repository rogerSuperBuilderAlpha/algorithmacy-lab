# Bigger and weighted quorums under noise: heavy pairs survive, and the "node count" pattern breaks

Exact IIT 4.0 Φ (PyPhi pin `b78d0e342`), every reachable subset in every reachable state. Backlog items
1 and 3 of `shared_share_ties/`. Hypotheses pushed in `3915c606` before computation (one disclosed timing
value aside). Probe 464 control reproduced (weights (1,1,2,2), quotas 2 and 5, e = 0.1: whole Φ 0.015905).

## Results

"Top" is the largest subset φ over states; "ties" is every subset within 1e-9 of it at that state.

| form | e | whole Φ | top subset φ | top / whole | top tie set |
|---|---:|---:|---:|---:|---|
| w2 (1,1,2,2; quota 2) | 0 | 0 | 2.000000 | – | {S,P3}, {S,P4}, {S,P3,P4} |
| w2 | 0.05 | 0.009877 | 1.667250 | 168.8 | {S,P3,P4} |
| w2 | 0.2 | 0.022686 | 0.833215 | 36.7 | {S,P3,P4} |
| w2 | 0.4 | 0.007095 | 0.037470 | 5.28 | {S,P3}, {S,P4}, {S,P3,P4} |
| w3 (quota 3) | 0 | 0 | 0 | – | none |
| w3 | 0.05 | 0.015393 | 0.092357 | 6 | {S,P3}, {S,P4}, {S,P1,P2}, {S,P3,P4} |
| w3 | 0.2 | 0.032470 | 0.194822 | 6 | {S,P3}, {S,P4} |
| w3 | 0.4 | 0.013370 | 0.080218 | 6 | {S,P3}, {S,P4} |
| 3of5 | 0.1 | 0.001770 | 0.028325 | 16 | 15 subsets: all {S,Pi} and all {S,Pi,Pj} |
| 3of5 | 0.2 | 0.004260 | 0.068160 | 16 | same 15 subsets |

Quota 5 gives exactly quota 2's values and quota 4 gives quota 3's at every rate (complement pairs, not
independent replications). Full per-state data: [results/results.json](results/results.json).

## Scores

- **H1 SUPPORTED.** For quotas 2 and 5 the heavy pair with the mediator, {S,P3,P4}, is in the top tie set
  at every noisy rate (alone at e = 0.05 and 0.2; tied with {S,P3} and {S,P4} at 0.4).
- **H2 SUPPORTED.** All four weighted quotas have positive whole Φ at every noisy rate, including quotas 3
  and 4, which have no irreducible subset at all at e = 0.
- **H3 REFUTED.** For 3of5 the top subset φ is 16 × whole Φ at both rates (0.068160 vs 0.004260), not 6.
  So the earlier "node count" reading (4 for three parties, 5 for four) does not extend to five parties;
  weighted quotas 3 and 4 give 6, and quotas 2 and 5 give no fixed ratio.
- **H4 REFUTED.** 3of5's top tie set is 15 subsets, every pair and every trio that contains S, at all four
  reachable states, not only the five pairs.
- **H5 SUPPORTED.** At no noisy rate is the full group in the top tie set, weighted or five-party.

## What it means

The membership result now holds on 5- and 6-node quorums too: under input noise the whole group is never
among the most tightly bound subsets where binding is strongest. Weighted rules keep their structure: a
quota that makes the two heavy parties decisive keeps them bound to the mediator as noise grows. The
size of the whole-system value relative to the strongest part is not a simple function of node count;
the earlier regularity was a three- and four-party coincidence or depends on the rule, and should not be
cited as a law.

## Limits

Independent reading errors only; parties never err; synchronous update. One weight vector, one
five-party rule, three or two rates. Ties at the 1e-9 cutoff. The full run takes 5 min 8 s (3of5 dominates).

## Reproduce

```sh
python org_frontier/studies/five_six_node_quorum_ties/run.py --quick   # CI: w2 at e = 0.2, ~12 s
python org_frontier/studies/five_six_node_quorum_ties/run.py --write   # full run, ~5 min
```

An AI assistant working as the open harness around IIT 4.0/PyPhi wrote the script and this report; every
number is printed by `run.py` or stored in `results/results.json`. No human review is claimed.
