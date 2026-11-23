# Weighted swap symmetry: rules with a heavy voter are lopsided like the interior quorums

Item 3 of `swap_symmetry_panel/BACKLOG.md`. Weights (1,1,1,2) at quotas 2, 3 and 4 on a 3 × 3 grid of input
noise η and party-side noise ε, η, ε ∈ {0, 0.05, 0.2}.

```
python org_frontier/studies/weighted_swap_symmetry/run.py --quick   # CI subset
python org_frontier/studies/weighted_swap_symmetry/run.py --write   # full run, ~21 s on 8 cores
```

**Result: all three hypotheses supported.** None of the three rules is swap-symmetric; each has whole Φ 0
under party noise alone; and party noise of 0.2 lowers whole Φ by exactly 0.389% (1/257) at every η > 0.
After the run we found a formula that fits every interior and weighted case so far (60 points, error ≤ 2e-14):
Φ(η, ε) = Φ(η, 0) / (1 + (ε / (1 − ε))^n). It is post hoc and not yet tested on new cases.

Files: [hypotheses.md](hypotheses.md), [FINDINGS.md](FINDINGS.md), [results/results.json](results/results.json),
[BACKLOG.md](BACKLOG.md).
