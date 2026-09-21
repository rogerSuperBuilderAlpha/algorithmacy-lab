# Dual-mediator template census — findings

**Verdict: FACTORS_INTO_FIVE.** An n=4 dual-mediator census (series
cascade, parallel mediators, mediator-of-mediators) does **not** force a
sixth template. Every closed triadic core matches one of the five n=3
strict-mediation templates (relay / conjunctive / additive / free /
parity). Size-4 major complexes sit on known landmark Φ — parity atom
0.5, or the 2+2 product Φ=4 — not a new atom.

In-silico; binary exact IIT-4.0; n≤4. Hypotheses fixed in `hypotheses.md`
before computing. Grows from V3 #1 / V2 #27. Ternary / residual-cascade /
M3 noted only.

## Already known

| prior | result |
|---|---|
| V2 #27 template coverage | five templates; parity is the fifth |
| conjunctive triad | Φ=2.0 |
| parity triad | Φ=0.5 |
| V3 #4–#7 | composed topology closed; no template reopen |

## Panel (abbrev.)

| cell | structure | core | core Φ | closed-triad templates |
|---|---|---|---:|---|
| triad_and | triadic | W\|S\|C | **2.0** | conjunctive |
| triad_xor | triadic | W\|S\|C | **0.5** | parity |
| series_AA / AX / XX / chain | triadic | size-2 | 2.0 | (no closed triad) |
| par_AA_s1 | dyadic | W\|C\|S1 | **2.0** | conjunctive |
| par_XX_s1 | dyadic | W\|C\|S1 | **0.5** | parity |
| par_AA_and | triadic | full n=4 | **4.0** | (product 2+2) |
| mom_copy / gate / two_mid | triadic | size-3 open | 2.0 | (open; pin→relay) |
| mom_xor | triadic | full n=4 | **0.5** | parity landmark |

## Hypotheses

| hypothesis | result |
|---|---|
| H1 AND Φ=2 + XOR Φ=0.5 anchors | **SUPPORTED** |
| H2 no sixth among closed triadic cores | **SUPPORTED** |
| H3 size-4 cores are known-phi products | **SUPPORTED** |
| H4 panel closed | **SUPPORTED** |

## Reading

Dual-mediator wiring at n=4 rearranges seats; it does not invent a new
determination algebra. Parallel AND–AND with both seats required yields
Φ=4 — the sum of two conjunctive atoms — a product, not a sixth template.
Series cascades collapse to dyadic cores. MoM forms either open-condition
to known templates or carry the parity landmark through a size-4 core.
The five-template inventory survives the dual-mediator lift.

Validation gap: Boolean models, not organizations.

## Best next (V3)

V3 #2 (threshold / majority at n≥4) or V3 #3 (mixed-algebra seats).

## Reproduce

```
python org_frontier/studies/dual_mediator_template_census/analyze_dual_mediator.py
```
