# Weighted quorums under noise: the Boolean rule decides, and a dummy party unbinds the whole

Exact IIT 4.0 Φ (PyPhi pin `b78d0e342`), every reachable subset in every reachable state, probe 464
independent input noise. Hypotheses pushed in `9a305ba1` before computation. Control passed: (1,2,2,2)
quota 3 equals equal-weight 2of4 at e = 0.2 (whole 0.035822, top 0.179110, ratio 5).

## Results

| weights, quota | e | whole Φ | top subset φ | top / whole | top tie set |
|---|---:|---:|---:|---:|---|
| (1,2,2,2) q2 | 0.05 / 0.1 / 0.2 | 0 / 0 / 0 | 2.381786 / 1.854569 / 1.041518 | – | {S,P2,P3,P4} |
| (1,2,2,2) q3 | 0.2 | 0.035822 | 0.179110 | 5.000000 | the four {S,Pi} |
| (1,2,2,2) q4 | 0.05 | 0 | 0.063043 | – | {S,Pi}, {S,Pi,Pj} over P2–P4 (6) |
| (1,2,2,2) q4 | 0.1 / 0.2 | 0 / 0 | 0.107922 / 0.146495 | – | {S,P2}, {S,P3}, {S,P4} |
| (1,1,2,3) q1, q7 | 0.2 | 1.110953 | 1.110953 | 1 | full group |
| (1,1,2,3) q2 (= q6) | 0.05 / 0.1 / 0.2 | 0.009877 / 0.015905 / 0.022686 | 1.667250 / 1.360017 / 0.833215 | 168.80 / 85.51 / 36.73 | {S,P3,P4} |
| (1,1,2,3) q3 (= q5) | 0.05 / 0.1 / 0.2 | 0.009093 / 0.014974 / 0.018807 | 0.875411 / 0.748696 / 0.503401 | 96.28 / 50.00 / 26.77 | {S,P4} |
| (1,1,2,3) q4 | 0.05 / 0.1 / 0.2 | 0.003897 / 0.006615 / 0.008897 | 0.095636 / 0.165167 / 0.226478 | 24.54 / 24.97 / 25.46 | {S,P4} |

Full data: [results/results.json](results/results.json).

## Scores

- **H1 REFUTED.** (1,2,2,2) quota 4 has no ratio at all: the whole group's Φ is exactly 0 at every rate.
  What the working idea got right: the strongest parts are exactly MAJ3's (0.146495 at e = 0.2, the three
  pairs {S,Pi} over the heavy parties), so the rule on the non-dummy parties is reproduced exactly. The zero is expected in IIT terms: S ignores
  P1, so P1 has no effect on anything in the system, and a cut that isolates P1's outputs costs nothing.
- **H2 SUPPORTED.** (1,2,2,2) quota 2: the top subset is {S,P2,P3,P4} alone at every rate, with exactly
  OR3's values (1.041518 at 0.2). The dummy P1 is left out, and the full group's Φ is 0.
- **H3 SUPPORTED.** (1,1,2,3) quotas 2, 3 and 4 all drift with noise (e.g. quota 3: 96.28 → 26.77).
- **H4 SUPPORTED.** Quotas 5 and 6 equal quotas 3 and 2 at e = 0.2.
- **H5 SUPPORTED.** Quotas 1 and 7 have ratio 1 with the full group on top.

Descriptive, after scoring: (1,1,2,3) quota 2 gives exactly the values of (1,1,2,2) quota 2 from
`five_six_node_quorum_ties` (168.8 at e = 0.05), and (1,1,2,3) quota 4 gives exactly (1,1,1,2) quota 3
from `weighted_ratio_law` (24.54 at 0.05). In both pairs the yes/no rule is the same up to relabeling the
parties (e.g. quota 4 on (1,1,2,3) and quota 3 on (1,1,1,2) are both "the heavy party plus anyone, or all
three others"). Weights matter only through the rule they compute.

## What it means

Under input noise, what a weighted vote does to integration is fixed by its yes/no rule, not by its
weights. If that rule is a counting rule, the counting law holds. If one party can never change the
outcome, the mediator still binds the others exactly as the smaller counting rule would, but the whole
group, which includes the party nobody needs, is exactly reducible. If one party is strictly stronger
than the rest, the binding concentrates on that party and the mediator, and the ratio to the whole drifts
with the error rate.

## Limits

Two weight vectors, four parties, three rates; independent reading errors; parties copy S exactly. The
claim "same rule, same values" is shown on three pairs, not proven; it follows from the TPM depending only
on the rule, which the control and the two descriptive pairs confirm numerically.

## Reproduce

```sh
python org_frontier/studies/weighted_equivalence/run.py --quick   # CI subset, ~15 s
python org_frontier/studies/weighted_equivalence/run.py --write   # full run, ~30 s on 8 cores
```

An AI assistant working as the open harness around IIT 4.0/PyPhi wrote the script and this report; every
number is printed by `run.py` or stored in `results/results.json`. No human review is claimed.
