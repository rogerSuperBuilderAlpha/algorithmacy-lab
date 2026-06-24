# q153 — Classifying the triadic-vs-dyadic Φ verdict from CRQA features

A coordination form has a structural verdict computed from exact IIT-4.0 Φ: its major complex
either binds three or more parties (triadic) or settles into a two-node core (dyadic). It also
has a behavioral signature read from a sampled run by cross-recurrence quantification analysis.
This study asks whether a few CRQA features recover the structural verdict.

## Setup

Four features describe each form. Two come from whole-system multidimensional recurrence:
determinism (DET) and recurrence rate (RR). One is the variance of the prominent pairwise
lead-lag lags. One is the prominence spread, the count of pairwise coupling links above a
prominence floor. The first two read the global behavioral pattern; the last two read the
pairwise coupling structure.

The corpus combines the curated 3-node `forms_library` with random 3-node and 4-node ensembles.
Each form is labeled by its major-complex core size. Triadic forms are rare among random wirings:
the raw pool ran 18 triadic against 77 dyadic. To keep accuracy meaningful, the corpus is
balanced to 1.5 dyadic per triadic with fixed seeds, giving n=45 and a majority-class baseline of
0.6000. A logistic regression on standardized features is scored by 5-fold stratified
cross-validation, with a label-shuffled control.

## Result

The classifier scores 0.5556 held-out accuracy against a 0.6000 baseline. The shuffled control
scores 0.5778. Neither beats the larger-class guess. The four CRQA features carry no held-out
signal about the structural verdict on this corpus.

The coefficient pattern is the more interesting half. Prominence spread holds the largest
standardized coefficient at 0.5440, ahead of lag variance (0.2211) and far ahead of DET
(0.0673). The model places what little weight it uses on coupling breadth, and almost none on
behavioral richness. Spread leads the field. It does not lead far enough to clear the baseline.

## What it means

The behavioral trajectory does not reconstruct the major-complex core size that exact Φ derives
from the transition matrix. A sampled run mixes the wiring with update noise, and the four
features tested do not separate the noise from the structure well enough to classify the verdict.
The negative result is informative: it marks a limit of the cheap behavioral readout against the
structural one, and it points at coupling breadth as the feature worth refining, since spread is
the only feature the model leans on.

The affirmative reading runs the other way. Exact Φ does the structural work the behavioral
features cannot. The CRQA side is a sampled proxy; the Φ side is the principled measurement. That
a four-feature proxy fails to recover the verdict is a statement about the proxy, not about the
tool it tries to approximate.

## Scope

Every number is exact IIT-4.0 Φ on synthetic Boolean coordination forms. This is an in-silico
study of the CRQA-to-Φ bridge. No field organization is measured. The accuracy is a property of
this balanced corpus and these four features. A richer feature set or a different ensemble could
read differently. The validation gap to coded field data stays open, and this study is the first
of the recurrence empirical line that uses the shared bridge module.
