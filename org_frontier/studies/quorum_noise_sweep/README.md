# Quorum input-noise sweep (O01)

Does the noisy-majority counterexample of probe 464 have a noise threshold, and does any interior
quorum ever bind the full group under input noise? Seven counting quorums (3 and 4 parties) at ten
error rates, exact IIT 4.0 Φ.

## Run

```
python org_frontier/studies/quorum_noise_sweep/sweep.py --quick   # CI subset, ~35 s
python org_frontier/studies/quorum_noise_sweep/sweep.py --write   # full panel, ~9 min
```

## Result in one line

**NO_THRESHOLD_MEMBERSHIP_HOLDS** — interior quorums have positive whole Φ at every noise rate in
(0, 0.5) on the grid (MAJ3 peak 0.036624 at η = 0.2) yet never take the full group as major complex;
extremes keep the full group except a tie at η = 0.4 in the four-party forms.

Files: [hypotheses.md](hypotheses.md) (pre-registered), [FINDINGS.md](FINDINGS.md),
[results/sweep.csv](results/sweep.csv), [results/results.json](results/results.json),
[BACKLOG.md](BACKLOG.md) (next experiments).
