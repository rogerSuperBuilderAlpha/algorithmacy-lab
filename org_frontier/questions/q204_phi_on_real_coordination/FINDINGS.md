# Q204 findings — exact Φ on a real coordination, decided by the coding

This computes exact IIT-4.0 Φ on a real interpersonal coordination for the first time in the lab. Two people
— a narrator describing a scene and a listener — have their gaze region recorded over 2000 time points (the
`eyemovement` dyad from the crqa package, Richardson & Dale 2005). Each person's gaze is binarized into one
unit, the joint two-unit transition matrix is estimated from the real sequence, and exact Φ is read with a
bootstrap confidence interval over the estimated matrix.

## Instrument control

A synthetic two-unit system with a known coupling — each unit reads the other (swap dynamics) — reads
Φ_s = 0.79. PASS. The instrument detects integration when it is present.

## The real dyad, three codings

| coding | Φ_s | 95% bootstrap CI | verdict |
|---|---|---|---|
| per-person mode-region | 0.0004 | [−0.0088, +0.0038] | reducible (CI includes 0) |
| per-person lower-half | 0.0095 | [−0.0013, +0.0212] | reducible (CI includes 0) |
| folded joint (same region) | 0.5256 | [+0.5154, +0.5334] | integrated (CI excludes 0) |

## Verdicts

- **H1 (exact Φ computed on real coordination; control reads integration): SUPPORTED.** The method runs on
  real data and the control reads Φ = 0.79.
- **H2 (the integration verdict is coder-dependent): SUPPORTED.** Both honest per-person codings give a Φ
  whose confidence interval includes 0; the folded coding gives Φ = 0.53 with a CI well clear of 0.

## What it says

Exact Φ can be computed on a real coordination. The method runs, and the control confirms it reads
integration when integration is there.

Under honest per-person codings — each person's gaze binarized on their own regions — the two gaze streams
factorize. The estimated transition matrix is near-diagonal in each person's own state: each person's next
gaze is driven mostly by their own current gaze, not the other's, so the joint dynamics decompose into two
independent processes and Φ sits at zero. This does not mean the two are uncoordinated. Richardson and Dale's
result is that the listener's gaze follows the narrator's at a lag of about two seconds; a one-step Φ at the
recording grain cannot see a coupling that lives several steps back. The coordination is real and lagged, and
the one-step exact Φ misses it.

The folded coding tells the cautionary half of the story. Coding both units as "the two are looking at the
same region" puts the joint relation inside each unit, and exact Φ then reads 0.53 with a tight interval
clear of zero. The same raw gaze data reads as strongly integrated. The integration came from the coding, not
from the data.

So the integration verdict on a real coordination is decided by the coding choice. The synthetic field
studies found this with bit-thresholds (q178) and unit splits (q180); here it holds on real data, and the
folded coding is a concrete way a coding can manufacture an integration verdict the honest codings deny.

## Scope

A single real dyad, a one-step transition matrix at the recording grain. The lagged coupling Richardson and
Dale report is exactly what the one-step Φ does not capture, so the right reading of the low per-person Φ is
"not integrated at the one-step grain," not "uncoordinated"; a study that builds the system at the coupling
lag is the next step. The binarizations are stated and the data is committed at `data/eyemovement.csv`,
refetchable from CRAN package `crqa`, `data(eyemovement)`. The companion real-data study
[q203](../q203_real_coordination_coupling/FINDINGS.md) reads the same kind of coordination with the
behavioral coupling measures; together they say the fine-grained instantaneous reading is weak while the
coordination lives at a lag.
