# Q81 findings — a learned surrogate recovers the verdict in-distribution, and fails to cross sizes

One hypothesis confirmed, three refuted. A random forest over ten size-invariant cheap features recovers
the outreach verdict perfectly within the size it trains on, and classifies larger forms worse than
chance. The exact-Φ size ceiling holds even for a learned student.

| Measure | Value |
|---|---|
| n=3 family | 256 forms (24 triadic, 232 dyadic; the 9.4% triadic census) |
| majority-class baseline | 0.906 |
| surrogate 5-fold CV accuracy | 1.000 |
| surrogate 5-fold CV ROC-AUC | 1.000 |
| held-out larger forms (n = 4, 5, 6) | 20 forms, majority baseline 0.600 |
| mean generalization accuracy | 0.250 |
| mean held-out dyadic recall | 0.250 |

| H | Result | Verdict |
|---|--------|---------|
| H1 | in-distribution CV ROC-AUC ≥ 0.85 (reached 1.000) | confirmed |
| H2 | CV accuracy ≥ majority + 0.10 | refuted |
| H3 | mean generalization accuracy ≥ 0.75 (reached 0.250) | refuted |
| H4 | mean held-out dyadic recall ≥ 0.50 (reached 0.250) | refuted |

From `probe_learned_surrogate.py`.

## What it says

A learned surrogate over cheap statistics recovers the dyadic/triadic verdict perfectly on the n=3
outreach family. Cross-validated accuracy and ROC-AUC are both 1.000, against a 0.906 majority baseline.
Within a fixed size, the verdict is fully readable from a combination of cheap trajectory features, which
is the in-distribution result probe #21 reported and this study sharpens to perfect separation.

The surrogate does not generalize past the size it trained on. Trained on the full n=3 family and applied
to outreach forms at n = 4, 5, and 6, it scores 0.250 accuracy — below the 0.600 held-out majority, and
below chance. The result is identical at three trajectory seeds, so it is the decision boundary that
fails, not estimation noise: the larger forms' intensive statistics fall in regions the n=3-trained model
labels with confidence and gets wrong. A surrogate that perfectly separates the verdict at one size places
most larger forms on the wrong side of the same boundary.

H2 is refuted by a ceiling, and the ceiling is itself the point. The n=3 family is 90.6% dyadic, so the
pre-registered rule — accuracy at least the majority baseline plus 0.10 — required 1.006, above the
maximum any classifier can reach. The surrogate reached perfect accuracy and still failed an unreachable
bar. The substantive in-distribution claim holds through H1 (AUC 1.000) and the perfect CV accuracy; the
H2 rule was set wrong and stays as written, marked refuted, because editing it after the fact would defeat
the audit.

The agenda asked whether a learned surrogate crosses the exact-Φ size ceiling. It does not. This sits with
`proxy_bridge`'s result rather than against it: cheap signals carry the verdict only where an exact label
was available to fit them, and the route past the ceiling does not hold. The finding strengthens the case
for exact computation, and costs little in practice, because coordination units are small enough to
classify exactly.

## Caveats

- **Mostly refutational.** Three of four hypotheses failed; only in-distribution recovery held.
- **In-silico.** Boolean models, evidence about the models. The verdict labels are exact; the surrogate
  sees only cheap trajectory statistics.
- **One held-out set.** Twenty larger forms from three families (breadth, chain/ring, market). A different
  held-out construction could shift the generalization number, but not above chance given how far below it
  the surrogate falls.
- **Class imbalance.** The n=3 family is 9.4% triadic, so accuracy is read alongside ROC-AUC and the
  generalization dyadic recall, not on its own.
