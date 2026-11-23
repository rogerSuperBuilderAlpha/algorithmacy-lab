# Does the quorum ratio law extend to weighted votes?

Fixed before this study's computation.

## Gap

`quorum_ratio_law` found, on equal-weight counting quotas under independent input noise, that the
largest subset φ is R × whole Φ, where R counts the groups of parties (including the empty one) too
small to settle the outcome alone. A group settles "yes" if its weight is at least q and settles "no" if
its weight is at least W − q + 1 (W = total weight).

## Values already seen (disclosed)

On weights (1,1,2,2) from `five_six_node_quorum_ties`: quota 3 (and 4) gives ratio 6 at e = 0.05, 0.2,
0.4; the generalized R for quota 3 is also 6 ({}, four singles, {P1,P2}). Quota 2 (and 5) gives 168.8,
36.7 and 5.28 at those rates, where R would be 3. So the generalized law already fits one weighted quota
and fails another. Nothing on weights (1,1,1,2) has been computed.

## Model

Four parties with weights (1,1,1,2), W = 5, quotas q = 1…5; probe 464 `input_tpm` at e ∈ {0.05, 0.1, 0.2};
parties copy S exactly. Every reachable subset in every reachable state. Ratio = largest subset φ over
states / largest full-group φ over states.

Generalized R for (1,1,1,2): q = 1 → 1; q = 2 → 4 ({}, P1, P2, P3); q = 3 → 8 ({}, P1, P2, P3, P4, and the
three pairs of weight-1 parties); q = 4 → 4; q = 5 → 1.

## Outcomes (relative tolerance 1e-6)

- H1: q = 3 has ratio 8 at all three rates.
- H2: q = 2 has a ratio that is not constant across rates (spread > 1%), like quota 2 on (1,1,2,2),
  because a single heavy party can settle "yes" alone while "no" needs W − q + 1 = 4.
- H3: q = 4 gives exactly q = 2's whole Φ and top φ at every rate (complement quotas).
- H4: q = 1 and q = 5 have ratio 1 with the full group in the top tie set at every rate.
- H5: for q = 2, 3, 4 the full group is never in the top tie set.
