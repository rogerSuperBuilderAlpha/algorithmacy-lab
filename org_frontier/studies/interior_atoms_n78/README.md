# Interior atoms at n=7–8 (V3 #9)

Do the discrete Φ atoms of V2 #18 / `interior_ring_pool` at n≤6 sprout
new interior atoms at n=7–8, or only thicken existing landmark
multiplicities?

**Verdict: SPROUTS_NEW_ATOMS** — n=7 designed interiors yield new full-core
Φ=10 (plus prior 6, 12); atoms sprout, not only thicken.

## Run

```
python org_frontier/studies/interior_atoms_n78/analyze_atoms_n78.py
```

(default loads committed census; `--rebuild` recomputes exact Φ)

## Result in one line

At n=7, mh2 lands on Φ=10 outside L≤6 interiors {6,8,9,12}; prior atoms
6 and 12 also recur.
