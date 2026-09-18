# Correlated output noise (agenda #5)

True correlated party-output noise as a non-CI state-by-state TPM,
contrasted with #61 static shared input and state-by-node flip-noise.
Exact IIT-4.0 Φ on the CI projection.

## Run

```
python org_frontier/studies/correlated_output_noise/analyze_correlated.py
```

## Result in one line

**CORE_SHIFT_NO_FLIP** — correlated SBS is non-CI but Φ only sees its
CI projection (= indep dual-party flip); smooth decay; no interior
verdict flip vs #61; one-point n_core dip at p=0.40.
