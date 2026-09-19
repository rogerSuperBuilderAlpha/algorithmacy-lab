# Graded × topology carriers (V3 #11)

On ring vs hub vs necklace, does graded min-commit keep sharp class
labels while Φ grades (V2 #2), or does topology force class flips?

**Verdict: SHARP_HOLDS_ACROSS_TOPO** — NULL→DYADIC→TRIADIC on all four
carrier cells; Φ grades; no topology-forced flip.

## Run

```
python org_frontier/studies/graded_topo_carriers/analyze_graded_topo.py
```

(default loads committed necklace census; `--rebuild-necklace` ~minutes)

## Result in one line

Graded commit’s sharp-class path survives ring and necklace carriers;
topology changes Φ magnitudes, not the label sequence.
