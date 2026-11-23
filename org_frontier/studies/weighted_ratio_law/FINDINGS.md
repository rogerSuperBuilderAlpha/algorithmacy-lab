# One heavy voter breaks the quorum ratio law

Exact IIT 4.0 Φ (PyPhi pin `b78d0e342`), every reachable subset in every reachable state, probe 464
independent input noise. Hypotheses pushed in `ba8ddb0d` before computation; values already seen on
weights (1,1,2,2) are disclosed there. Control passed: (1,1,2,2) quota 3 at e = 0.2 reproduces whole Φ
0.032470 and ratio 6 (= generalized R).

## Results, weights (1,1,1,2)

| quota | e | whole Φ | top subset φ | top / whole | generalized R | top tie set |
|---:|---:|---:|---:|---:|---:|---|
| 1 | 0.05 / 0.1 / 0.2 | 3.016929 / 2.225483 / 1.110953 | same | 1 | 1 | full group |
| 2 | 0.05 | 0.014973 | 0.873322 | 58.327969 | 4 | {S,P4} |
| 2 | 0.1 | 0.024283 | 0.741828 | 30.549829 | 4 | {S,P4} |
| 2 | 0.2 | 0.029299 | 0.486042 | 16.589044 | 4 | {S,P4} |
| 3 | 0.05 | 0.003897 | 0.095636 | 24.542139 | 8 | {S,P4} |
| 3 | 0.1 | 0.006615 | 0.165167 | 24.967040 | 8 | {S,P4} |
| 3 | 0.2 | 0.008897 | 0.226478 | 25.456563 | 8 | {S,P4} |
| 4 | all | = quota 2 | = quota 2 | = quota 2 | 4 | {S,P4} |
| 5 | all | = quota 1 | = quota 1 | 1 | 1 | full group |

Full data: [results/results.json](results/results.json).

## Scores

- **H1 REFUTED.** Quota 3 (a weighted majority, 3 of 5 weight) has ratio 24.54, 24.97 and 25.46, not 8,
  and not constant.
- **H2 SUPPORTED.** Quota 2's ratio falls from 58.33 to 16.59 as noise rises, as quota 2 on (1,1,2,2) did.
- **H3 SUPPORTED.** Quota 4 matches quota 2 exactly (complement quotas).
- **H4 SUPPORTED.** Quotas 1 and 5 have ratio 1 with the full group on top; their values equal the
  equal-weight 1of4 values (1.110953 at 0.2), since with q = 1 or 5 weights do not matter.
- **H5 SUPPORTED.** The full group is never in the top tie set for quotas 2–4.

## What it means

The counting law from `quorum_ratio_law` holds where voters are interchangeable, and also on (1,1,2,2)
quota 3, where the voters come in two interchangeable pairs. With a single heavy voter, the strongest part
is no longer a tie among many small groups: it is the mediator and the heavy voter alone, {S,P4}, and its
φ is not a fixed multiple of the whole. The whole stays weakly bound and is never the strongest part. Read
for organizations: when one party's reading counts more, the mediator's binding concentrates on that
party, and the three-way whole becomes thinner in a way no simple count of coalitions predicts.

## Limits

One weight vector; three rates; independent reading errors; parties copy S exactly. We have not found a
weighted formula; the ratio for quota 3 drifts slowly with e (24.5 → 25.5).

## Reproduce

```sh
python org_frontier/studies/weighted_ratio_law/run.py --quick   # CI subset, ~15 s
python org_frontier/studies/weighted_ratio_law/run.py --write   # full run, ~40 s on 8 cores
```

An AI assistant working as the open harness around IIT 4.0/PyPhi wrote the script and this report; every
number is printed by `run.py` or stored in `results/results.json`. No human review is claimed.
