# q161 — Which structural verdict survives update-noise misspecification

A CRQA reading of a coordination form is taken from a stochastic run. The run's update noise, the
per-node flip rate, is set by the analyst. It need not match the regime the form would settle into
on its own. When the flip rate is wrong, which of the structural verdicts read from the run still
matches the exact-Phi ground truth?

Three verdicts are tested against a fixed exact IIT-4.0 Phi ground truth on sixteen synthetic
Boolean forms: the triadic/dyadic label (core size three or more vs two), per-node membership
(in-core vs spectator), and the bottleneck node (the structural articulation point). The flip rate
is swept from 0.02 to 0.30. The ground truth is computed once and does not move with flip; only the
CRQA reading moves.

## Result

The ranking is the reverse of the prior. Bottleneck recovery is the most robust verdict, holding
between 0.75 and 0.84 agreement across the whole flip range and rising, not falling, with more
noise. The triadic/dyadic label is the most fragile: it is correct at every swept flip for only 5
of 16 forms, and away from its low-flip sweet spot it sits near chance. Membership lands between
the two.

H1 predicted the opposite: that the triadic/dyadic verdict would be robust for over 80% of forms
while bottleneck recovery degraded by more than 20 points. Both halves fail. The triadic/dyadic
robust fraction is 0.31, and bottleneck recovery degrades by only 9 points and in the wrong
direction. H1 is refuted.

H2 predicted that each form's optimal flip would track its intrinsic update entropy. The optima do
vary across forms, so no single flip is best for all. But the optimum does not track entropy: the
Spearman correlation is -0.148, weak and the wrong sign. H2 is not supported.

## Why the bottleneck wins

The bottleneck pick is an argmax of coupling centrality, a rank statistic. Update noise shifts
every centrality value, but the node that leads stays the leader across a wide noise band, so the
pick survives. The triadic/dyadic label reads a prominence-spread count against a threshold
calibrated at one flip. The count moves with flip, so the threshold drifts off calibration and the
label flips. Robustness here is set by how the verdict is decoded from the trajectory, not by how
much irreducibility the form carries.

## Scope

Every number is exact IIT-4.0 Phi on small synthetic Boolean coordination forms paired with CRQA
readings of their sampled trajectories. "Verdict", "membership", "bottleneck", and "update noise"
name graph-and-Phi quantities. The agreement rates are baselines on synthetic data. The
Phi-to-organization bridge is open, so the lesson is for the CRQA decoding step: a rank-based pick
of one node tolerates a misspecified flip rate where a threshold-based label does not.
