# Q57 — Stage 3 hypotheses (fixed before computation)

Five working hypotheses on why one-sided channel direction fixes which outer-party singleton cut achieves
minimum normalized_phi and co-enters the official MIP tie set with complete. Written and committed before any
test runs. Grows from Q56 probes #181 and #184.

## H1 — Back-channel recipient determines tied singleton seam
- **Claim:** On every aligned one-sided ceiling pair, the outer-party singleton cut in the official tie set
  isolates the back-channel recipient — the outer party whose update rule gains the extra incoming
  cross-edge from the other outer party. Worker topologies tie `{W,SC}`; counterpart topologies tie
  `{WS,C}`.
- **H0:** At least one one-sided ceiling pair ties the cut on the non-recipient outer party.
- **Predicted outcome:** Sixteen of sixteen pairs match the recipient→singleton mapping. H0 refuted only
  if the count is perfect.

## H2 — Dual at-system Phi with fixed normalized_phi split
- **Claim:** Every one-sided ceiling pair has both outer-party two-part cuts at system Phi; the tied cut
  has minimum normalized_phi 0.5 matching complete; the excluded cut has normalized_phi 1.0.
- **H0:** At least one pair lacks both outer cuts at system Phi, or the tied cut is not 0.5, or the excluded
  cut is not 1.0.
- **Predicted outcome:** Sixteen of sixteen with dual at-system outer cuts; sixteen of sixteen tied=0.5 and
  excluded=1.0. H0 refuted on any exception.

## H3 — Two-to-one normalized_phi ratio on outer cuts
- **Claim:** The excluded outer cut carries exactly twice the minimum normalized_phi of the tied outer cut
  on every one-sided ceiling pair (ratio 2.0, spread 0).
- **H0:** The excluded-to-tied normalized_phi ratio differs from 2.0 on at least one pair.
- **Predicted outcome:** Sixteen of sixteen pairs at ratio 2.0 within 1e−6 tolerance. H0 refuted on any
  deviation.

## H4 — Complete partition shares tied outer minimum normalized_phi
- **Claim:** The complete partition minimum normalized_phi equals the tied outer cut on all sixteen
  one-sided ceiling pairs, explaining co-entry of complete with the favored singleton seam.
- **H0:** Complete normalized_phi differs from the tied outer cut on at least one pair.
- **Predicted outcome:** Sixteen of sixteen pairs with complete norm equal to tied outer norm within 1e−6.
  H0 refuted on any mismatch.

## H5 — Gate-invariant direction rule under XOR and XNOR
- **Claim:** XOR and XNOR gate polarity preserve the recipient→singleton mapping: all worker topologies
  (worker_xor, worker_xnor) tie `{W,SC}`; all counterpart topologies (counterpart_xor, counterpart_xnor)
  tie `{WS,C}`.
- **H0:** At least one worker topology ties `{WS,C}` or at least one counterpart topology ties `{W,SC}`.
- **Predicted outcome:** Eight of eight worker pairs at `{W,SC}`; eight of eight counterpart pairs at
  `{WS,C}`. H0 refuted on any gate-direction violation.
