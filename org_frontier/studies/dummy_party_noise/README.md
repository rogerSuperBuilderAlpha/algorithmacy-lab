# Dummy party under noise: a never-pivotal party zeroes whole Φ in OR3 and AND3

Item 3 of `weighted_equivalence/BACKLOG.md`. OR3 and AND3 with a fourth party that never changes the outcome
(weights (1,2,2,2), quotas 2 and 6), under input noise η ∈ {0.05, 0.1, 0.2} and party-side noise
ε ∈ {0, 0.05, 0.1}, against plain OR3 and AND3.

```
python org_frontier/studies/dummy_party_noise/run.py --quick   # CI subset
python org_frontier/studies/dummy_party_noise/run.py --write   # full run, ~15 s on 8 cores
```

**Result: all three hypotheses supported.** With a dummy party, whole Φ is exactly 0 at every reachable
state in all 18 noisy cases. The top group is always {S,P2,P3,P4}, with φ equal to the plain three-party
form's whole Φ at the same noise (e.g. η = 0.2, ε = 0.1: 0.759267). OR3 and AND3 versions match exactly.

Files: [hypotheses.md](hypotheses.md), [FINDINGS.md](FINDINGS.md), [results/results.json](results/results.json),
[BACKLOG.md](BACKLOG.md).
