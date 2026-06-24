# q175 — review

## Claim under review

Coding a worker as one of an interchangeable pool flips the exact-Φ verdict from triadic to dyadic,
and the coder-disagreement interval surfaces the flip when coders split on the reading.

## What holds

The flip is exact and reproducible. The specific reading reads triadic at max Φ_MIP = 2.0; pooled
readings at k = 2, 3, 4 read dyadic at max_phi = 0. The mechanism is transparent: an OR over the
pool makes every member redundant, and redundancy is the absence of the integration Φ measures. The
contested-reading interval spans [0, specific Φ] on 97.5% of contested panels, above the 0.90
threshold, and the unanimous-pool control collapses the bridge CI to [0, 0]. The probe is
deterministic and byte-identical across re-runs.

## Limits and stress points

The result is on synthetic accounts with known ground truth. No worker is measured, and the study
does not establish that any field coordination is dyadic or triadic. The flip is a property of the
coding choice.

H2 reads the flip from the percentile span of the coder readings, not from the bridge's bootstrap-t
mean-CI. The mean-CI is a confidence band on the average Φ, which for a 0/2 split lands near the mean
and excludes 0 most of the time; it answers a different question. The reading span is the right
instrument for a contested categorical reading, and the probe says so. A reviewer who wants the
bootstrap-t mean-CI to carry H2 will find it does not, and that is the honest reason the span is used.

The span fraction depends on the panel size and the contest band. At 12 coders and a [0.30, 0.70]
split band the span is robustly above 0.90; thinner panels or one-coder minorities can pull the 2.5
percentile off 0. The probe reports this: a barely-contested form fails the contest band, which is
fixed before computing.

The pool sizes run to k = 4 (system size n = 6), the exact-Φ ceiling for this machinery. The OR
mechanism makes larger pools behave identically, so the dyadic verdict is not expected to recover at
larger k, but that is an argument from the mechanism, not a computation.

## Disposition

Both hypotheses supported on synthetic data. The diagnostic is sound: it locates the substitutability
coding as the lever on the verdict and marks contested cases with an interval anchored at 0.
