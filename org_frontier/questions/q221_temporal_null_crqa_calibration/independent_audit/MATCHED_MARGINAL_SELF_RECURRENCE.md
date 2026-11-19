# Self-recurrence falsification of the marginal-matched candidate

Independent exact finite-state calculation, 2026-10-15. Candidate A=`nsi(6,3,3)`, B=`aff(6,9,5)`, using the search's committed truth tables, independent node flips p=0.08, stationary initial law, all lags 0..20.

All three channel marginals are exactly 0.5 in both models; six ordered **cross-channel** match profiles agree within floating precision (max absolute error 3.33e-16). However, **within-channel** profiles differ: X lag-1 self-match A=0.74893568, B=0.5, maximum within-channel profile difference over tested lags=0.24893568. Y and H lag-1 self-match both equal 0.5.

Therefore the marginal-matched candidate is not observationally equivalent even at the level of all channel auto- and cross-match profiles. This is a useful **falsification**, not a failure to be hidden. It still demonstrates insufficiency of the restricted population cross-channel profile representation.

**Next candidate filter:** match both within-channel and cross-channel lag profiles, ideally as exact rational quantities, and then verify the nondegenerate IIT target differences and finite-sample feature distributions. Do not present marginal matching alone as sufficient.

These are exploratory results; no new confirmatory decision or IIT-specific theorem is asserted.
