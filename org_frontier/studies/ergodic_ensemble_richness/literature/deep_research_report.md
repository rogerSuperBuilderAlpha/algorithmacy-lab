# Literature — B5, written before the census run

The quantity this cell correlates is system integrated information in the
IIT 4.0 sense: Φ over the minimum-information partition of a discrete
system in a state (Albantakis et al. 2023). The software that evaluates
it on a small binary network is PyPhi (Mayner et al. 2018). The 2018
paper documents the IIT 3.0 toolbox. This lab pins the later IIT-4.0
line, which follows the 2023 formulation. The cell uses that line
through `classify_rules`.

On a finite deterministic map, the ergodic decomposition Birkhoff's
theorem guarantees for a measure-preserving transformation sits on the
invariant sets (Birkhoff 1931). For the synchronous Boolean maps in this
lab those sets are the attractors, and the basins are the states that
reach them. The track's working definition is that one, recorded in
`ergodicity/_boolean_ergo.py`. Peters (2019) is the reason the track
cares: when a time average and an ensemble average part, a population
summary mis-describes the trajectory a single party lives. B5 asks
whether that parting, read as basin entropy and attractor count, travels
with Φ_MIP inside one fully enumerated family.

The association statistic is Spearman's rank correlation (Spearman 1904),
with a permutation null so the p-value does not depend on a bivariate
normal assumption the Boolean census will not meet.

What the outside literature does not contain is this census. No paper
located for this note reports Spearman ρ between exact IIT-4.0 Φ and
basin entropy on the 256-form strict-mediation family. The lab's own
designed panel of nine forms refuted a mean-count link and left the
population correlation open. That is the gap. The sources above
underwrite the two quantities and the correlation. They do not underwrite
a sign.
