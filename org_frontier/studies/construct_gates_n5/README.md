# Construct gate transfer at n=5 — CMC / AI-MC

Do XOR (Regime B) and MAJ (Regime C) full-bind regimes transfer from
HMC to CMC / AI-MC?

## Run

```
python org_frontier/studies/construct_gates_n5/analyze_gates.py
```

## Result in one line

**GATE_REGIMES_TRANSFER** — CMC/AI-MC: XOR→B (Φ=0.125), MAJ→C (no
flip), AND→A; matches HMC GATE_SPLITS.
