# q153 — findings

CRQA features read from sampled runs do not recover the triadic-vs-dyadic exact-Φ verdict above
chance on this corpus, but the one feature that carries any signal is coupling breadth, not
behavioral richness.

## The numbers

Balanced corpus: n=45 (18 triadic, 27 dyadic), majority-class baseline 0.6000.

| metric | value |
|---|---|
| 5-fold held-out accuracy (real) | 0.5556 |
| 5-fold held-out accuracy (shuffled control) | 0.5778 |
| majority-class baseline | 0.6000 |

Standardized logistic coefficients (full-corpus fit):

| feature | coef | abs |
|---|---|---|
| det | -0.0673 | 0.0673 |
| rr | 0.0459 | 0.0459 |
| lag_var | -0.2211 | 0.2211 |
| spread | 0.5440 | 0.5440 |

## Reading

The real classifier scores 0.5556, below the 0.6000 baseline. The shuffled control scores 0.5778,
also below the baseline. Neither beats guessing the larger class, so the four CRQA features carry
no held-out signal about the structural verdict on this corpus. The behavioral trajectory does not
reconstruct the major-complex core size that exact Φ computes from the transition matrix.

The coefficient pattern still separates the features. Prominence spread holds the largest
magnitude at 0.5440, more than double the next feature (lag_var at 0.2211) and far above DET
(0.0673). The little weight the model places anywhere goes on coupling breadth. DET, the
behavioral-richness feature, is nearly inert.

## Verdicts

H1 CRQA features beat the majority baseline: REFUTED. Held-out accuracy 0.5556 sits below the
0.6000 baseline, and the shuffled control sits below it too.

H2 prominence spread is the most predictive feature: CONFIRMED. Spread carries the largest-magnitude
standardized coefficient; DET does not.

The pair is consistent. The features cannot classify the verdict, and within that failure the only
feature with appreciable weight is coupling breadth.

## Scope

In-silico. The corpus is synthetic Boolean coordination forms scored by exact IIT-4.0 Φ. The
result describes the CRQA-to-Φ bridge on these models, not any field organization. The held-out
accuracy is a property of this balanced corpus and these four features; a richer feature set or a
different ensemble could read differently. The validation gap to coded field data is open.
