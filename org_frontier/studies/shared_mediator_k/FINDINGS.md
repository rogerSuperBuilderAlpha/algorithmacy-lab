# Shared-mediator k-lift — findings

**Verdict: SCALE_2K_OR_REFUSES.** k conjunctive triads sharing one mediator
merge under AND with **Φ = 2k** (k=1,2,3 → Φ=2,4,6; full cores). OR
bridging **refuses** full merge at k=2 and k=3. Lift of V2 #16 WIN; no
saturation on this range.

In-silico; binary exact IIT-4.0; n=2k+1 ≤ 7. Hypotheses fixed in
`hypotheses.md` before computing. Grows from V3 #6 / V2 #16. Ternary /
residual-cascade / M3 noted only.

## Already known

| prior | result |
|---|---|
| V2 #16 shared-mediator AND | k=2 merges; five-node core Φ=4.0 |
| V2 #16 shared-mediator OR | does not merge |
| single triad | Φ=2.0 |

## Panel

| cell | n | structure | core Φ | full core |
|---|---:|---|---:|---|
| triad (k=1) | 3 | triadic | **2.0** | yes |
| k=2 AND | 5 | triadic | **4.0** | yes |
| k=2 OR | 5 | dyadic | — | no |
| k=3 AND | 7 | triadic | **6.0** | yes |
| k=3 OR | 7 | dyadic | — | no |

## Hypotheses

| hypothesis | result |
|---|---|
| H1 triad + k=2 AND Φ=4 + k=2 OR refuse | **SUPPORTED** |
| H2 k=3 OR refuses full merge | **SUPPORTED** |
| H3 AND Φ scaling named (scale_2k) | **SUPPORTED** |
| H4 panel closed | **SUPPORTED** |

## Reading

Shared-mediator merge does not saturate at k=2. Each added triad under AND
adds **+2** to core Φ while keeping the whole system in one major complex.
OR remains a refuse bridge — the #16 OR null lifts. Scale beyond k=3 is
open (n=9 exact Φ costly).

Validation gap: Boolean models, not organizations.

## Best next (V3)

V3 #7 (hybrid feedforward+recurrent seam) or V3 #1 (n=4 dual-mediator
template census).

## Reproduce

```
python org_frontier/studies/shared_mediator_k/analyze_shared_k.py
```
