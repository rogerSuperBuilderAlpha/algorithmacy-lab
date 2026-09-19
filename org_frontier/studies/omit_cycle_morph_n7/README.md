# Omit cycle-type morph at n=7 (V3 #8)

Does the omit cycle-type discriminant morph again at n=7, or does the
n=5→n=6 singleton→band shift stabilize into a fixed band grammar?

**Verdict: BAND_GRAMMAR_HOLDS** — class-pure Φ=12 vs Φ=14 bands at n=7;
grammar stabilizes (no morph-again).

## Run

```
python org_frontier/studies/omit_cycle_morph_n7/analyze_morph_n7.py
```

(default loads committed census; `--rebuild` ~90 min for 12 exact-Φ cells)

## Result in one line

At n=7, indeg (0,1,1,1,1,1,2) keeps a pure two-band cycle-type law
(Φ=12 vs 14); the V2 #42 singleton→band shift does not morph again.
