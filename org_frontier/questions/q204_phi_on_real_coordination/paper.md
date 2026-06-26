# Q204 — Exact Φ on a real coordination, decided by the coding

## Abstract

The lab's exact-Φ studies all run on synthetic Boolean forms, and Barrett et al. (2026) note that exact Φ has
essentially never been computed on a real system. This study computes exact IIT-4.0 Φ on a real interpersonal
coordination — two people, a narrator and a listener, whose gaze is recorded over 2000 time points (the
`eyemovement` dyad, Richardson & Dale 2005). Each person's gaze is binarized into one unit, the joint
two-unit transition matrix is estimated from the real sequence, and Φ is read with a bootstrap interval.
Under honest per-person codings the gaze streams factorize (Φ ≈ 0, interval includes 0); a coding that folds
the joint state into both units manufactures integration (Φ = 0.53, interval clear of 0). The integration
verdict on real coordination is decided by the coding choice, the field bridge's coder-dependence (q178,
q180) outside synthetic data.

## Why this study

Every program in the lab names the same gap: the results are in-silico. The field program states the sharp
form — exact Φ has never been computed on a real coordination, and the rule-to-Φ verdict's dependence on
coding choices is shown only synthetically. This study computes exact Φ on real data and tests that
dependence there.

## The data

The `eyemovement` dyad distributed with the crqa R package: a narrator describing a scene to a listener,
each person's gaze region recorded over 2000 time points (Richardson & Dale 2005, the canonical
interpersonal-coordination eye-tracking study). Committed at `data/eyemovement.csv`.

## Method

Each person's categorical gaze is binarized into one unit; the joint two-unit transition matrix is estimated
from the empirical one-step transitions; exact Φ_s is computed with PyPhi at the most-visited state, with a
60-sample bootstrap interval over the estimated matrix. A synthetic two-unit coupled system (swap dynamics)
is the instrument control. Three binarizations are compared: each person's own most-frequent region, each
person's lower-half regions, and a folded coding that codes both units as "the two look at the same region."

## Result

Control Φ = 0.79 (PASS). Per-person codings give Φ ≈ 0 with intervals including 0; the folded coding gives
Φ = 0.53 with an interval clear of 0. H1 and H2 are both supported. The reading is in
[`FINDINGS.md`](FINDINGS.md).

## Limitations

One real dyad, a one-step transition matrix at the recording grain. Richardson & Dale's coupling is lagged
(~2 s), which a one-step Φ does not capture, so the low per-person Φ means "not integrated at the one-step
grain," not "uncoordinated." A system built at the coupling lag is the next step. The companion study
[q203](../q203_real_coordination_coupling/FINDINGS.md) reads the same coordination with behavioral coupling
measures.

## Reproduce

`python ci/reproduce.py q204-phi-on-real-coordination`
