# q158 — review

## What the probe shows

Whole-system md_recurrence DET does not predict the magnitude of exact major-complex Φ. The
Spearman correlation is -0.19, below the preregistered 0.4 threshold and negative in sign. The
recurrence rate is more strongly negative at -0.40. Both hypotheses are refuted, and the refutation
is reported as found.

## Strengths

The result is a clean negative with a mechanism. High DET marks a form that locks onto a few global
states, which is the behavioral mark of a tight limit cycle, and a tight limit cycle is weakly
integrated. The negative sign is what the dynamics predict once the question moves from the binary
verdict to the continuous scale. The control on H2 distinguishes the two ways a positive high-Φ
residual can arise: a saturating rise would let a monotone increasing fit beat the line, and it does
not, so the residual is the negative trend rather than saturation.

## Limits

One behavioral feature against one structural magnitude. A multivariate fit on the full CRQA feature
set, or a feature designed for state-space novelty rather than recurrence, might recover a positive
predictor; this probe does not test that. The Φ ceiling at 2.0 compresses the top of the corpus, so
the high-Φ quartile is a narrow band. The pool mixes 3- and 4-node forms with different Φ ranges,
and a per-n analysis is not reported here.

## Scope

Synthetic Boolean forms, exact IIT-4.0 Φ, in-silico. No field organization is measured. The finding
constrains the CRQA-to-Φ bridge on this corpus and does not transfer to real coordination data
without the validation step that line still owes.

## Reproducibility

Deterministic. All RNG is seeded, trajectory sampling is seeded per form, and exact Φ is
deterministic. Three runs produce byte-identical output. The captured stdout is in results/output.txt.
