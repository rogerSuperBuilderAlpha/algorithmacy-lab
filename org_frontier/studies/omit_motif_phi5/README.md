# Omit-motif census: Φ=5 vs Φ=6 at n=5

What omit motif discriminates non-derangement fixed_k=3 forms with Φ=5 from
those with Φ=6?

## Run

```
python org_frontier/studies/omit_motif_phi5/analyze_motifs.py
```

## Result in one line

**MOTIF_DISCRIMINANT.** Φ=5 iff omit motif M (indeg (0,1,1,1,2) + 3-cycle +
recip=0); same-indeg siblings → Φ=6; \|M\|=120.
