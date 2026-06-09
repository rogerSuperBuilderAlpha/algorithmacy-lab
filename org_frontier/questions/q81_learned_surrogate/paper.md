# Q81 — A learned surrogate for the outreach verdict, and the size ceiling

## Question

Exact integrated information is intractable past roughly ten to twelve elements. The agenda's estimation
frontier asks whether a learned surrogate escapes that ceiling for the dyadic/triadic outreach verdict:
train a cheap model on small forms an exact computation can label, then predict the verdict on forms too
large to label exactly. Probe #21 found that a forest over many cheap features recovers the verdict
in-distribution on the 256-form family, where no single proxy does. That probe used a feature panel whose
length grows with the number of nodes, so it cannot be applied at a size it did not train on. This study
fixes a size-invariant feature panel and asks the generalization question directly.

## Method

The ground truth is the exact IIT-4.0 verdict on each form's Boolean rules. The surrogate sees only cheap
statistics estimated from a noisy trajectory of the form. The in-distribution corpus is the 256
strict-mediation outreach forms at n = 3 (sender intent, mediator, recipient). The held-out corpus is 20
outreach forms at n = 4, 5, 6 — the breadth, chain/ring, and market forms of Q64, Q66, and Q85, in both
classes — each larger than anything in training and labelled by its own exact verdict.

Each form's trajectory yields ten size-invariant features: the mean, max, min, and spread of per-node
entropy; the mean, max, and min of pairwise mutual information; the mean and max of transfer entropy; and
the per-node O-information. Every feature is an aggregate over nodes or pairs, so the vector has length 10
at any size, and none encodes the number of parties. The model is a random forest, evaluated
in-distribution by stratified 5-fold cross-validation and tested out-of-distribution by training on the
full n = 3 family and predicting the held-out larger forms at three trajectory seeds.

## Results

In-distribution, the surrogate recovers the verdict perfectly: 5-fold CV accuracy and ROC-AUC are both
1.000, against a 0.906 majority baseline. The combination of cheap features carries the verdict fully
within a fixed size.

Out of distribution, it fails. Trained on n = 3 and applied to the larger forms, mean accuracy is 0.250,
below the 0.600 held-out majority and below chance. The number is identical at all three seeds, so the
failure is in the decision boundary, not in estimation noise. The larger forms' intensive statistics land
in regions the n = 3 model labels confidently and wrongly: the same boundary that separates the verdict
perfectly at one size mislabels most forms at the next.

The pre-registered H2 is refuted by a ceiling that is itself informative. With the family 90.6% dyadic,
the rule "accuracy at least the majority baseline plus 0.10" demanded 1.006, which no classifier can
reach. The surrogate reached perfect accuracy and still failed an unreachable bar. The rule is left as
written and marked refuted; the in-distribution claim stands through H1 and the perfect CV accuracy.

| | result |
|---|---|
| H1 in-distribution CV ROC-AUC ≥ 0.85 | confirmed (1.000) |
| H2 CV accuracy ≥ majority + 0.10 | refuted (rule exceeded 1.0) |
| H3 generalization accuracy ≥ 0.75 | refuted (0.250) |
| H4 held-out dyadic recall ≥ 0.50 | refuted (0.250) |

## Interpretation

A learned student does not cross the exact-Φ size ceiling for this verdict. Cheap features carry the
verdict only where an exact label was available to fit them; extrapolated to larger forms, the fitted
boundary is worse than guessing. This agrees with `proxy_bridge`, where single cheap proxies failed to
preserve the verdict, and extends it: even a model that combines many cheap features and separates the
verdict perfectly in-distribution does not transfer across sizes. The estimation route past the ceiling
does not hold for the outreach verdict.

The consequence is mild in practice and sharp in principle. In practice, coordination units are small, so
the exact classifier runs well under the ceiling and no surrogate is needed. In principle, the verdict is
a structural property that a cheap statistical summary captures only locally in size: the result is one
more reason to compute the verdict exactly rather than estimate it.

## Limitations

In-silico throughout; the labels are exact and the surrogate's inputs are cheap statistics on Boolean
models. The held-out set is 20 forms from three families; a different construction could move the
generalization number, but not above chance given how far below it the surrogate sits. Class imbalance
(9.4% triadic) means accuracy is read with ROC-AUC and dyadic recall, not alone. The conclusion is a
refutation of generalization, reported as such.
