# The shrinking cores in the noise sweep were tie-breaks; counted as ties, membership is symmetric

Exact IIT 4.0 Φ (PyPhi pin `b78d0e342`), every reachable subset in every reachable state, probe 464
input noise. Hypotheses pushed in `84542181` before computation; values already seen are listed there.
Controls passed: MAJ3 whole Φ 0.036624 at η = 0.2; ANY4 top φ 0.009264 at η = 0.4.

Top tie set = every subset within 1e-9 of the largest subset φ over all reachable states, pooled over the
states where that maximum occurs.

## Results (top tie set size; full group in it?)

| form | 0.01 | 0.02 | 0.05 | 0.1 | 0.2 | 0.3 | 0.4 | 0.45 |
|---|---|---|---|---|---|---|---|---|
| OR3, AND3 | 1 Y | 1 Y | 1 Y | 1 Y | 1 Y | 1 Y | 7 Y | 7 Y |
| MAJ3 | 6 N | 6 N | 6 N | 3 N | 3 N | 3 N | 3 N | 3 N |
| ANY4, ALL4 | 1 Y | 1 Y | 1 Y | 1 Y | 1 Y | 1 Y | 15 Y | 15 Y |
| 2of4, 3of4 | 14 N | 14 N | 10 N | 10 N | 4 N | 4 N | 4 N | 4 N |

MAJ3's six are the three pairs {S,Pi} and three trios {S,Pi,Pj}; its three are the pairs. 2of4's four are
the pairs {S,Pi}. At η = 0.4 and 0.45, OR3's seven and ANY4's fifteen are every subset containing S. Full
data: [results/results.json](results/results.json).

## Scores

- **H1 SUPPORTED.** No interior quorum has the full group in its top tie set at any noisy rate.
- **H2 SUPPORTED.** In every interior case every party is in at least one top-tied subset. The core
  shrinkage `quorum_noise_sweep` reported (MAJ3 to {S,P3}; 2of4 and 3of4 to {S,P4}) is which tied subset
  PyPhi happened to return, not a party dropping out.
- **H3 SUPPORTED.** ANY4 and ALL4 at η = 0.4 have the full group in the top tie set (15-way tie at
  0.009264, reached in states 01111 and 11111 for ANY4). The "fragile membership" exception in
  `quorum_noise_sweep` was a tie-break.
- **H4 REFUTED.** OR3 and AND3 have the full group as the unique top only up to η = 0.3. At 0.4 and 0.45
  the full group ties with all six smaller subsets containing S (0.023283 at 0.4).
- **H5 SUPPORTED.** ANY4 and ALL4 keep the full group in the top tie set at every noisy rate.

## What changes

The membership half of the quorum law, restated on ties: extreme rules always include the full group
among the most tightly bound units, and interior rules never do, at every rate tested. Interior rules
bind every party equally (each pair with the mediator ties), so no party is singled out. At high noise
the extreme rules stop singling out the full group too: every unit containing the mediator ties with it.
Claims in earlier studies that name a single shrinking core under noise should be read as tie-breaks.

## Limits

Counting quorums on three and four parties; independent reading errors; parties copy S exactly; ties at
the 1e-9 cutoff; pooled over top states.

## Reproduce

```sh
python org_frontier/studies/tie_set_membership/run.py --quick   # CI subset, ~8 s
python org_frontier/studies/tie_set_membership/run.py --write   # full run, ~46 s on 8 cores
```

An AI assistant working as the open harness around IIT 4.0/PyPhi wrote the script and this report; every
number is printed by `run.py` or stored in `results/results.json`. No human review is claimed.
