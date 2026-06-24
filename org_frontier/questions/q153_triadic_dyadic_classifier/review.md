# q153 — review

## What the probe shows

A logistic classifier on four CRQA features does not separate triadic from dyadic forms above the
majority-class baseline on a balanced synthetic corpus. The real held-out accuracy is 0.5556, the
baseline is 0.6000, and the shuffled control is 0.5778. H1 is refuted. Within that failure,
prominence spread carries the largest standardized coefficient (0.5440 against 0.0673 for DET), so
H2 is confirmed.

## Strengths

The instrument control passes on the known triad before any new computation. The corpus, the
balancing, the trajectory seeds, the cross-validation split, and the label shuffle are all seeded;
three runs are byte-identical. The shuffled control sits near the baseline, which confirms the
cross-validation is not leaking. The feature extraction lives in a shared bridge module the rest
of the recurrence line can reuse.

## Weaknesses and threats

The balancing throws away most of the dyadic pool. A different dyadic sample could move the
accuracy; the 1.5 ratio and the seeds are fixed in advance, but the corpus is small (n=45), so the
5-fold accuracy is coarse-grained. The four features are a deliberately thin description of the
trajectory; a richer set could recover signal the thin set misses, and the negative result does
not rule that out. The triadic class is small in absolute terms (18 forms), which limits what the
classifier can learn.

## Reading the verdicts together

The two verdicts are consistent. The features do not classify the structural verdict, and the only
feature the model leans on is coupling breadth. Spread is the most predictive feature and still
fails to clear the baseline. The honest summary is a negative result on H1 with a clean
within-model ranking on H2.

## Scope

In-silico. Exact IIT-4.0 Φ on synthetic Boolean forms. The result describes the CRQA-to-Φ bridge
on these models. The validation gap to coded field data is open.
