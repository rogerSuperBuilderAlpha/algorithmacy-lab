# Partial observation / estimability (agenda #24)

How fast does the cheap mean-MI screen degrade when a node is hidden or
a party is observed only intermittently?

## Run

```
python org_frontier/studies/partial_observation_screen/analyze_partial_obs.py
```

## Result in one line

**HIDDEN_COLLAPSE_INTERMITTENT_CLIFF** — hide party: AUC 0.922→0.547;
δ≥0.10 holds, cliffs at δ=0; hide mediator ≈ full.

## Hypotheses

Fixed before computing in [`hypotheses.md`](hypotheses.md).

## Priors

`sample_complexity_screen/` (#23), `spectral_invariant/` (#21),
`ESTIMATION_ARC.md`. Exact binary IIT-4.0 Φ; in-silico.
