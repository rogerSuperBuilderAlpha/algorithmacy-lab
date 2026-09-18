# Hybrid feedforward+recurrent seam (V3 #7)

Does a recurrent cycle feeding a feedforward chain keep V2 #15’s
closure-decides-locus rule, or violate it?

## Run

```
python org_frontier/studies/hybrid_ff_recurrent_seam/analyze_hybrid_seam.py
```

## Result in one line

**CLOSURE_HOLDS_HYBRID** — hybrid AND seams keep the major complex in the
recurrent zone; FF tail excluded (V2 #15 rule survives).
