# When does a weighted quorum behave like a counting quorum under noise?

Fixed before this study's computation.

## Gap

`quorum_ratio_law` found that on equal-weight counting quotas under independent input noise, largest
subset φ = R × whole Φ, where R counts the groups of parties too small to settle the outcome alone.
`weighted_ratio_law` found the law fails on weights (1,1,1,2) at quotas 2–4 (ratios drift with noise,
e.g. 24.54–25.46 at quota 3, predicted 8), while it holds on (1,1,2,2) quota 3 (ratio 6). Item 1 of
`weighted_ratio_law/BACKLOG.md` asks where the boundary is. Values already seen: those in the two
studies above. Nothing on (1,2,2,2) or (1,1,2,3) has been computed.

## Working idea (stated before computing)

A weighted rule should follow the law when, after dropping dummy parties (parties never pivotal),
the rule is a counting rule on the remaining parties; R is then computed on that reduced game.
Otherwise the ratio drifts with noise. On (1,2,2,2): quota 3 is exactly "2 of 4" (same Boolean
function); quota 4 is "2 of 3" among the heavy parties with P1 a dummy; quota 2 is "1 of 3" among the
heavy parties with P1 a dummy. (1,1,2,3) has no dummy at any quota and is not a counting rule at quotas
2–6.

## Model

Probe 464 `input_tpm` (mediator misreads each party independently with probability e; parties copy S).
Every reachable subset in every reachable state. Ratio = largest subset φ over states / largest
full-group φ over states. Cases: (1,2,2,2) quotas 2 and 4 at e ∈ {0.05, 0.1, 0.2}, quota 3 at 0.2;
(1,1,2,3) quotas 1–4 at e ∈ {0.05, 0.1, 0.2}, quotas 5–7 at 0.2.

Control: (1,2,2,2) quota 3 equals equal-weight 2of4 at e = 0.2 (whole 0.035822, top 0.179110; 1e-6).

## Outcomes (relative tolerance 1e-6)

- H1: (1,2,2,2) quota 4 has ratio 4 (MAJ3's value) at every rate, not the raw count 8.
- H2: (1,2,2,2) quota 2: the full group is not the top subset; the top tie set is {S,P2,P3,P4} (dummy
  P1 left out) at every rate.
- H3: (1,1,2,3) quotas 2, 3 and 4 each have a ratio that is not constant across the three rates
  (spread > 1%).
- H4: (1,1,2,3) quotas 5 and 6 equal quotas 3 and 2 (whole and top) at e = 0.2 (complements).
- H5: (1,1,2,3) quotas 1 and 7 have ratio 1 with the full group on top at e = 0.2.
