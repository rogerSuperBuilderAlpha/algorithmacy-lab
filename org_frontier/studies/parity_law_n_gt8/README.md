# Parity-hub law for n>8 (agenda V4 #9)

Does V3 #10’s parity-hub law Φ=2^(2−n) remain exact for n>8 hub
embeddings — via the named H-cut and/or feasible exact SIA — or do
topology residuals appear?

## Run

```
python org_frontier/studies/parity_law_n_gt8/analyze_parity_n_gt8.py
```

## Result in one line

**LAW_HOLDS_NGT8** — H-cut φ = 2^(2−n) at n∈{8,9,10}; full SIA at n=8
keeps H as MIP with φ = law; no residual in the lean window.

## Scope

Lean panel: V3 #10 controls n≤7 + named H-cut n∈{8,9,10} + full SIA at
n=8. Major-complex census stays at n≤7 (cut/SIA regime for n≥8).

## Hypotheses

Fixed before computing in [`hypotheses.md`](hypotheses.md).

## Priors

V3 #10 `LAW_HOLDS_NGT6`; V2 #47/#49. Exact binary IIT-4.0 where feasible.
