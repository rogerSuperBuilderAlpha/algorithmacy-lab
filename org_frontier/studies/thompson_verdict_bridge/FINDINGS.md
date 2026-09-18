# Thompson verdict bridge — findings

**Verdict: PARTIAL_ALIGNMENT.** Thompson’s interdependence types track the
dyadic/triadic verdict loosely, not as a clean map. Canonical
pooled_indep→dyadic and recip_cyclic→triadic hold; the sequential chain
ties reciprocal at Φ=2 (not low); alternate encodings flip the verdict.

In-silico. Exact binary IIT-4.0. N=3 AND family. Hypotheses fixed in
`hypotheses.md`. Prior: `questions/q43_thompson_interdependence/`
(pointer only).

## Type → verdict / Φ / core

| type | form | role | structure | Φ | core | vs H1 |
|---|---|---|---|---|---|---|
| pooled | indep relay | canonical | dyadic | 0.0 | {W,S} | OK |
| pooled | all-required | alternate | triadic | 2.0 | {W,S,C1} | **MISMATCH** |
| sequential | pass-through chain | canonical | triadic | 2.0 | {W,S,C} | chain OK; **not low** |
| sequential | acyclic hand-off | alternate | dyadic | 0.0 | {C} | **MISMATCH** |
| reciprocal | cyclic triad | canonical | triadic | 2.0 | {W,S,C} | OK |
| reciprocal | labels, no cycle | alternate | dyadic | 0.0 | {W,S} | **MISMATCH** |

Alignment score: **0.429** (3/6 structure + 0/1 sequential-low).

Under the AND family the canonical chain and cyclic reciprocal share the
same rules, so the top Thompson step cannot separate them.

## Hypotheses

| H | result |
|---|---|
| H1 clean type→verdict map | **REFUTED** |
| H2 mismatches | **SUPPORTED** |
| H3 partial alignment only | **SUPPORTED** |

## Reading

The typology names structures the lab already knows (#25/#40/#57/#116/#39).
What decides the verdict is joint determination and a feedback cycle, not
the Thompson label — same through-line as q43. Construct-validity bridge
opens here; it does not close the map.

## Best next

**#44** Wageman-style measured task interdependence → modeled verdict.

## Reproduce

```
python org_frontier/studies/thompson_verdict_bridge/analyze_thompson.py
```
