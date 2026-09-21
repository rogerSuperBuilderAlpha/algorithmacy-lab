# Hybrid feedforward+recurrent seam — findings

**Verdict: CLOSURE_HOLDS_HYBRID.** A recurrent cycle feeding a feedforward
AND chain keeps the major complex **inside the recurrent zone**; the FF
tail is excluded. V2 #15’s closure-decides-locus rule **survives** the
hybrid AND seam. OR at the seam relocates the core onto the FF pair alone
(secondary; does not reopen the AND rule).

In-silico; binary exact IIT-4.0; n≤5. Hypotheses fixed in `hypotheses.md`
before computing. Grows from V3 #7 / V2 #15. Ternary / residual-cascade /
M3 noted only.

## Already known

| prior | result |
|---|---|
| V2 #15 recurrent trees | major complex spans occupied levels |
| V2 #15 hub chains | core top-local (H0,P0); FF mid excluded |
| V2 #15 H5 | closure decides level locus |

## Panel

| cell | n | structure | core | core Φ | locus |
|---|---:|---|---|---:|---|
| triad | 3 | triadic | W\|S\|C | **2.0** | holds (recurrent) |
| hub_L2 | 4 | dyadic | H0\|P0 | **2.0** | holds (top-local) |
| hy_triad_AND | 5 | dyadic | W\|S\|C | **2.0** | **holds** |
| hy_tree_AND | 5 | dyadic | S0\|L0\|L1 | **2.0** | **holds** |
| hy_triad_OR | 5 | dyadic | H1\|P1 | 2.0 | violates (FF-only) |

## Hypotheses

| hypothesis | result |
|---|---|
| H1 triad Φ=2 + hub_L2 top-local | **SUPPORTED** |
| H2 hybrid AND locus named (AND_HOLDS) | **SUPPORTED** |
| H3 OR seam locus reported | **SUPPORTED** |
| H4 panel closed | **SUPPORTED** |

## Reading

Under AND, attaching a feedforward hub+party to a recurrent triad or to a
d=1,b=2 recurrent tree does not enlarge the major complex past the
recurrent block. The FF seam behaves like the mid gate of a hub chain: the
complex stays where closure is. OR at the same seam drops the triad from
the core and leaves a local FF 2-cycle (Φ=2) — a relocate, not a recurrent
pull of the tail. The #15 rule is about AND-family locus; OR is a collapse
mode at the seam.

Validation gap: Boolean models, not organizations.

## Best next (V3)

V3 #1 (n=4 dual-mediator template census) or V3 #2 (threshold/majority at
n≥4). Composed-topology lane #4–#7 is closed.

## Reproduce

```
python org_frontier/studies/hybrid_ff_recurrent_seam/analyze_hybrid_seam.py
```
