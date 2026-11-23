# A fitted formula for the drifting ratio when one party is strictly strongest

Fixed before this study's computation.

## Gap

On interchangeable counting rules, the largest subset φ is a fixed multiple of whole-group Φ: the
multiple is R, the number of party groups (including the empty one) too small to settle the vote
(`quorum_ratio_law`). A group settles "yes" if its weight is at least the quota q, and settles "no"
if its weight is at least W − q + 1 (W = total weight).

When one party is strictly strongest, that law fails and the ratio changes with the noise rate
(`weighted_ratio_law`, `one_heavy_voter`, `weighted_equivalence`). Item 4 of
`weighted_equivalence/BACKLOG.md` asks for a formula for that drifting ratio, fitted on (1,1,1,2)
quota 3 and (1,1,2,3) quota 3, then predicted on (1,1,1,3).

Those two named series belong to different families, so a single curve in the noise rate cannot
describe both. (1,1,2,3) quota 3 has a unique singleton-winning party (weight 3 meets the quota
alone) and the ratio *falls* as the rate rises. (1,1,1,2) quota 3 has a unique strictly strongest
party who cannot win alone (weight 2 is short of quota 3) and the ratio *rises* slowly. The
prediction target, (1,1,1,3) quota 3, is in the first family: the weight-3 party meets the quota
alone. The already-published singleton-winning series on (1,1,1,2) quota 2 (also unique-heavy, top
subset always {S, heavy}) is therefore used with (1,1,2,3) quota 3 to fit the formula. The
(1,1,1,2) quota 3 series is disclosed as the other family and is not used in the fit.

## Values already seen (disclosed)

Same protocol as this study (probe 464 `input_tpm`, parties copy S, every reachable subset in every
reachable state). Sources: `weighted_ratio_law` for (1,1,1,2); `weighted_equivalence` for (1,1,2,3).
Complement quotas that compute the same yes/no rule are listed only once.

Singleton-winning family (unique heavy party, top tie set {S, P4} at every rate):

| weights | q | R | e | whole Φ | top φ | ratio |
|---|---:|---:|---:|---:|---:|---:|
| (1,1,1,2) | 2 | 4 | 0.05 | 0.014972604668929156 | 0.8733216266331056 | 58.327969377659784 |
| (1,1,1,2) | 2 | 4 | 0.1 | 0.024282548019418235 | 0.7418276938542704 | 30.54982917200644 |
| (1,1,1,2) | 2 | 4 | 0.2 | 0.02929897282509204 | 0.4860419415847388 | 16.589043734955986 |
| (1,1,2,3) | 3 | 5 | 0.05 | 0.00909278667848543 | 0.8754109128212231 | 96.27531622319317 |
| (1,1,2,3) | 3 | 5 | 0.1 | 0.014973943530612347 | 0.7486964687973653 | 49.999952735680445 |
| (1,1,2,3) | 3 | 5 | 0.2 | 0.018806768429940404 | 0.5034005823556224 | 26.766989992507582 |

Other family, unique heavy who cannot win alone (top tie set also {S, P4}; not used in the fit):

| weights | q | R | e | whole Φ | top φ | ratio |
|---|---:|---:|---:|---:|---:|---:|
| (1,1,1,2) | 3 | 8 | 0.05 | 0.0038968042400468897 | 0.09563591084642234 | 24.542138879748183 |
| (1,1,1,2) | 3 | 8 | 0.1 | 0.0066154057587187445 | 0.1651671014019276 | 24.967040182568752 |
| (1,1,1,2) | 3 | 8 | 0.2 | 0.008896660359373351 | 0.22647839906045011 | 25.45656346449562 |

No committed input-noise whole Φ, top φ, or ratio exists for (1,1,1,3). (The party-side values in
`majority_factor_split` use a different noise model and are not used here.)

## Generalized R for the new rule

Weights (1,1,1,3), W = 6, quota 3. A group is too small to settle the vote when its weight is at
most 2 (it cannot force yes, and its complement still has at least the quota). Those groups are the
empty group, the three weight-1 parties, and the three pairs of weight-1 parties: R = 7. Quota 4 is
the complement of quota 3 (W − q + 1 = 4) and has the same R.

## Fitted formula

Write C(R, 2) = R(R − 1)/2. The candidate, fitted by least squares to the six singleton-winning
ratios in the first table and to nothing else, is

    ρ(e, R) = α · C(R, 2) / e + (R − β) + γ (R − 1) e

with the Python float64 coefficients obtained from `numpy.linalg.lstsq` on the six rows
[C(R, 2)/e, −1, (R − 1)e] against (ratio − R):

- α = 0.46208785675550357
- β = 1.07585180342645
- γ = −0.32856641898784006

The largest relative residual of this fit on those six published points is 4.864549e-5 (disclosed,
not a test). This is a three-parameter fit, not a derived identity.

Evaluated at R = 7, the formula gives the predicted ratios for (1,1,1,3) quota 3:

- e = 0.05: 199.9024781081887
- e = 0.1: 102.76545826383659
- e = 0.2: 54.04909345311601

A measured ratio *matches* the prediction if |measured − predicted| / predicted ≤ 1e-3 (and the
whole-group Φ is above 1e-9). That tolerance is about twenty times the largest in-sample residual,
so a clean extrapolation can still count as a match, while a miss of a few percent refutes the
formula.

## Model

Four parties with weights (1,1,1,3); probe 464 `input_tpm` at e ∈ {0.05, 0.1, 0.2}; parties copy S
exactly. Every reachable subset in every reachable state, as in `weighted_ratio_law`. Ratio =
largest subset φ over states / largest full-group φ over states. Tie set = subsets within 1e-9 of
the top φ. Quotas 3 and 4 are both measured. A harness control recomputes the already-published
(1,1,2,3) quota 3 case at e = 0.1 and must recover ratio 49.999952735680445 to relative tolerance
1e-6; that check is not a hypothesis test.

## Outcomes

- H1: at every rate e ∈ {0.05, 0.1, 0.2}, the measured ratio for (1,1,1,3) quota 3 matches the
  predicted value in the list above (relative error ≤ 1e-3).
- H2: at every such rate, the top tie set for (1,1,1,3) quota 3 is exactly {S, P4}.
- H3: (1,1,1,3) quota 4 gives the same whole Φ, top φ, and ratio as quota 3 at every rate
  (relative tolerance 1e-6). The top state may flip from all-0 to all-1, as in earlier complement
  pairs; the tie set is still {S, P4}.
