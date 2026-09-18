# Wageman TI → verdict — findings

**Verdict: WAGEMAN_PREDICTS_VERDICT.** A CM-only Wageman-style
interdependence index separates dyadic from triadic on the designed
panel (AUC=1.0, accuracy=1.0 at W≥0.472). It does **not** predict Φ
magnitude better than the verdict (H3 REFUTED): XOR and AND share W
while Φ is 0.5 vs 2.0.

In-silico. Exact binary IIT-4.0. N=3 (+ one N=4 pool). Hypotheses fixed
in `hypotheses.md`. #43 / CONSTRUCT_VALIDITY_ARC pointers only.

## Index

`W = (reciprocity + input + affect) / 3` from the connectivity matrix
(survey TI echo: mutual dependence, needing input, affecting others).
Not the #43 joint-AND / cycle primitives.

## Score vs verdict / Φ

| slug | W | TI_7 | structure | Φ |
|---|---|---|---|---|
| independent | 0.00 | 1.00 | dyadic | 0.0 |
| one_way_feed | 0.11 | 1.67 | dyadic | 0.0 |
| seq_handoff | 0.22 | 2.33 | dyadic | 0.0 |
| pooled_indep | 0.44 | 3.67 | dyadic | 0.0 |
| recip_acyclic | 0.44 | 3.67 | dyadic | 0.0 |
| pool_n4 | 0.50 | 4.00 | triadic | 3.0 |
| and_chain | 0.67 | 5.00 | triadic | 2.0 |
| xor_chain | 0.67 | 5.00 | triadic | 0.5 |
| or_chain | 0.67 | 5.00 | triadic | 2.0 |

## Prediction metrics

| metric | value |
|---|---|
| AUC(W→triadic) | **1.000** |
| best accuracy | **1.000** @ W≥0.472 |
| Spearman ρ(W, Φ) | 0.883 |
| r_pb(W, triadic) | 0.802 |
| mismatches @ thr | none |

## Hypotheses

| H | result |
|---|---|
| H1 W predicts dyadic/triadic | **SUPPORTED** |
| H2 weak/null | **REFUTED** |
| H3 Φ better than verdict | **REFUTED** (ρ − \|r_pb\| = 0.081 < 0.10) |

## Reading

On designed tasks, survey-style *intensity* of interdependence tracks
the structure class. Within one connectivity pattern the index is blind
to determination family (XOR vs AND), so Φ is not graded. This is a
stronger map than Thompson’s labels (#43), and still not a Φ calculator.
No worker was measured.

## Best next

**#45** Boolean render of a real coordination dataset (conjunctive law).

## Reproduce

```
python org_frontier/studies/wageman_ti_verdict/analyze_wageman.py
```
