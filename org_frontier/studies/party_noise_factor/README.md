# The post-hoc party-noise factor, tested on new cases and refuted

Item 1 of `weighted_swap_symmetry/BACKLOG.md`. Pre-registered predictions of
Φ(η, ε) = Φ(η, 0) / (1 + (ε / (1 − ε))^n) at ε ∈ {0.3, 0.4}, on (1,1,1,2) at quotas 2–4, on
(1,1,2,2) at quota 3, and on the five-party interior rules 2-of-5, 3-of-5 and 4-of-5.

```
python org_frontier/studies/party_noise_factor/run.py --quick   # CI subset, ~11 s
python org_frontier/studies/party_noise_factor/run.py --write   # full run, ~2 min on 8 cores
```

**Result: both hypotheses refuted.** The formula missed 10 of 20 pre-registered cases. It held
exactly for (1,1,1,2) quota 3 and for 3-of-5 at every tested rate, and at ε = 0.3 for (1,1,2,2)
quota 3, 2-of-5 and 4-of-5. It failed for (1,1,1,2) quotas 2 and 4 at both new rates, and at
ε = 0.4 for the other three rules, where 2-of-5 and 4-of-5 whole Φ rose from 0.032322 to 0.075400
instead of falling to 0.028561.

Files: [hypotheses.md](hypotheses.md), [FINDINGS.md](FINDINGS.md), [results/results.json](results/results.json),
[BACKLOG.md](BACKLOG.md).
