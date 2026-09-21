# Parity law under n>6 hub embeddings (V3 #10)

Does Φ = 2^(2−n) remain exact for the parity hub past n=6, or do
topology residuals appear when cut formulas replace exact enumeration?

**Verdict: LAW_HOLDS_NGT6** — exact Φ matches 2^(2−n) at n=6 and n=7;
named H-cut is the MIP with no residual.

## Run

```
python org_frontier/studies/parity_law_n_gt6/analyze_parity_n_gt6.py
```

(default loads committed census; `--rebuild` ~10 min)

## Result in one line

Parity hub Φ = 2^(2−n) holds exactly through n=7; H-cut formula matches MIP.
