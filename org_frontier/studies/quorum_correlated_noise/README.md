# Correlated input noise on quorum hubs

Does the noisy-majority effect of `quorum_noise_sweep/` survive when the mediator's reading errors are
shared across parties? Three three-party hubs (OR, 2-of-3 majority, AND) under independent, fully
shared and half-shared errors at eight rates, exact IIT 4.0 Φ.

## Run

```
python org_frontier/studies/quorum_correlated_noise/correlated.py --quick   # CI subset, ~6 s
python org_frontier/studies/quorum_correlated_noise/correlated.py --write   # full panel, ~90 s
```

## Result in one line

**SHARED_ERROR_KEEPS_MAJORITY_ZERO** — fully shared errors leave the majority at Φ = 0 at every rate;
half-shared errors make it positive at every rate (peak 0.022542 at e = 0.3); the majority never binds
the full group; core φ = 4 × whole Φ in all 14 positive majority cases.

Files: [hypotheses.md](hypotheses.md), [FINDINGS.md](FINDINGS.md), [results/](results/),
[BACKLOG.md](BACKLOG.md).
