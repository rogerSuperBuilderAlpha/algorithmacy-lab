# The strongest-part-to-whole ratio on noisy counting quorums follows a counting law

Exact IIT 4.0 Φ (PyPhi pin `b78d0e342`), every reachable subset in every reachable state, probe 464
independent input noise. Hypotheses pushed in `4f0fe759` before computation. The law was fitted to four
already-known ratios (disclosed in `hypotheses.md`); the four new cases are the test. Controls passed:
MAJ3 whole 0.036624 and 3of5 whole 0.004260 at e = 0.2.

## The law

R(n, q) = Σ_{k=0}^{m−1} C(n, k), with m = min(q, n − q + 1). m is the size of the smallest group of parties
that can settle the outcome on its own (q to force "yes", n − q + 1 to force "no"). R counts the groups
of parties, including the empty one, too small to settle it.

## Results

| form | e | whole Φ | top subset φ | top / whole | R(n, q) | ties | full group in top? |
|---|---:|---:|---:|---:|---:|---:|---|
| 2of3 (MAJ3), control | 0.2 | 0.036624 | 0.146495 | 4.000000 | 4 | 3 | no |
| 2of4, control | 0.2 | 0.035822 | 0.179110 | 5.000000 | 5 | 4 | no |
| 3of5, control | 0.2 | 0.004260 | 0.068160 | 16.000000 | 16 | 15 | no |
| **2of5** | 0.1 | 0.029993 | 0.179961 | 6.000000 | 6 | 15 | no |
| **2of5** | 0.2 | 0.032322 | 0.193930 | 6.000000 | 6 | 5 | no |
| **4of5** | 0.2 | 0.032322 | 0.193930 | 6.000000 | 6 | 5 | no |
| **1of4** | 0.2 | 1.110953 | 1.110953 | 1.000000 | 1 | 1 | yes |
| **1of5** | 0.2 | 1.110953 | 1.110953 | 1.000000 | 1 | 1 | yes |

Full data: [results/results.json](results/results.json).

## Scores

- **H1 SUPPORTED.** 2of5's ratio is 6 at e = 0.1 and 0.2, as R predicts, not 16 (3of5) and not 5 or 4.
- **H2 SUPPORTED.** 4of5 equals 2of5 at e = 0.2 (complement quotas, so this is a check, not a new case).
- **H3 SUPPORTED.** At e = 0.2, 2of5's top tie set is exactly the five pairs {S, Pi}.
- **H4 SUPPORTED.** At e = 0.2, the tie set has R − 1 members for MAJ3 (3), 2of4 (4), 3of5 (15) and
  2of5 (5).
- **H5 SUPPORTED.** The extreme rules 1of4 and 1of5 have ratio 1, with the full group the top subset.

Descriptive, not pre-registered:
- At e = 0.1, 2of5's tie set has 15 subsets (every pair and trio with S), not 5, while the ratio stays 6.
  So |ties| = R − 1 is a coincidence of particular rates, and the ratio is the robust quantity.
- 1of5 and 1of4 have the same whole Φ to 1e-12 at e = 0.2 (1.110953).

## What it means

On noisy counting quorums, how much weaker the whole is than its strongest part is set by the rule's
combinatorics: the number of party groups too small to settle the vote. A majority of three has 4 such
groups, 3-of-5 has 16. The extreme rules (any-yes, all-yes) have exactly one, the empty group, and their
whole group is as bound as any part. This turns an earlier "node count" reading, which `five_six_node_
quorum_ties` refuted, into a rule that predicted a new case. It is an observed law on eight cases; we have
not derived it.

## Limits

Counting quotas with equal weights only (weighted quota 3 on (1,1,2,2) gives 6 and is not covered by this
formula as stated); independent reading errors; parties copy S exactly; e = 0.1 and 0.2; up to five
parties. Ties at the 1e-9 cutoff.

## Reproduce

```sh
python org_frontier/studies/quorum_ratio_law/run.py --quick   # CI subset, ~14 s
python org_frontier/studies/quorum_ratio_law/run.py --write   # full run, ~100 s on 8 cores
```

An AI assistant working as the open harness around IIT 4.0/PyPhi wrote the script and this report; every
number is printed by `run.py` or stored in `results/results.json`. No human review is claimed.
