# Fielded W × Φ landmark — findings

**Verdict: LANDMARK_COLLAPSES_VERDICT_HOLDS.** Clean CM-echo (W,n)
still predicts HUB / RING4 / POOL (acc=1.000), but a **fielded rater-
noise** instrument (Gaussian σ=0.20 on Wageman subscales) drops
landmark accuracy to **0.802** while **verdict-class AUC stays 0.997**.
Missing a subscale alone does not collapse this symmetric panel.

In-silico; exact binary IIT-4.0. Hypotheses fixed in `hypotheses.md`.
Answers RESEARCH_AGENDA_V4 #6. Extends V3 #14 `W_N_PREDICTS_LANDMARK`
and V2 #44 `WAGEMAN_PREDICTS_VERDICT`.

**Validation gap.** “Fielded” here is synthetic subscale / rater noise
on designed Boolean forms, not a real questionnaire or scored teams.
Missing-subscale redundancy is panel-specific (hub/ring/pool CMs have
equal subscales).

## Already known

| prior | result |
|---|---|
| V3 #14 | W_N_PREDICTS_LANDMARK — clean W+n predicts landmarks; W alone fails cross-n |
| V2 #44 | WAGEMAN_PREDICTS_VERDICT — W separates dyadic/triadic |
| V4 #5 | MATCHED_RETAINS_COPY_RANKS (separate imputer lane) |

## Panels

| regime | metric | value |
|---|---|---:|
| clean | N4 hub < ring < pool (gaps ≥0.05) | **YES** |
| clean | (W,n) landmark acc | **1.000** |
| clean | W-alone cross-n acc | 0.700 |
| clean | verdict AUC | **1.000** |
| fielded σ=0.20 | (W,n) landmark acc (40-trial mean) | **0.802** |
| fielded σ=0.20 | verdict AUC (40-trial mean) | **0.997** |
| drop any subscale | (W,n) acc | **1.000** |
| reciprocity-only | N4 order+gaps | **YES** |

Landmark hold bar: acc ≥ 0.85. Verdict hold bar: AUC ≥ 0.85.
Prototypes = clean CM W; query W = fielded.

## Hypotheses

| H | result |
|---|---|
| H1 clean #14 replicate | **SUPPORTED** |
| H2 rater noise collapses landmark | **SUPPORTED** |
| H3 verdict holds under same noise | **SUPPORTED** |
| H4 missing subscale keeps landmark | **SUPPORTED** |
| H5 recip-only keeps N4 order | **SUPPORTED** |

## Reading

The V3 #14 pairing is **instrument-sensitive**. When W is the clean CM
echo, (W,n) recovers landmarks. When the same three subscales are
read with moderate rater noise — a minimal model of a fielded survey —
nearest-clean-prototype landmark prediction falls below the hold bar,
while the coarser dyadic/triadic verdict screen remains nearly
perfect. Dropping one subscale does not matter here because hub /
ring / pool connectivity makes the three subscales identical; the
failure mode is noise, not item loss. Practice: do not treat a clean
W+n landmark chart as field-ready without an instrument-noise check;
verdict-class use of W is more robust under the same degradation.

## Best next (V4)

**#7** — on logged collaboration graphs (or a public OSS role graph),
does anti-correlated party duty predict failure of a cheap integration
screen the way V3 #16 predicts in silico?

## Reproduce

```
python org_frontier/studies/fielded_w_landmark/analyze_fielded.py
```
