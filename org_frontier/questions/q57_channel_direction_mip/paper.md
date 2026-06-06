# Q57 — channel direction MIP seam

## Question

Why does the one-sided channel direction fix which outer party — W under worker wiring, C under counterpart
wiring — achieves minimum normalized_phi and co-enters the official MIP tie set with the complete
partition, when both outer-party two-part cuts reach system Phi on every aligned ceiling pair?

## Grounding

Q56 probe #181 reported that aligned one-sided ceiling pairs tie one outer-party singleton seam with
complete: worker topologies favor {W,SC}, counterpart topologies favor {WS,C}. Q56 probe #184 confirmed
minimum normalized_phi as the tie-break rule. The present study tests five directional mechanisms on the
sixteen aligned one-sided bijective parity ceiling pairs.

## Instrument

Exact IIT-4.0 Phi via PyPhi on n=3 deterministic Boolean coordination forms with labels (W, S, C). The
canonical triad W'=S, S'=W AND C, C'=S reads triadic at max_phi=2.0 with MIP `2 parts: {W,SC}`. Every
probe asserts this control before comparison. Partition landscapes use `evaluate_partition` at the max-Phi
reachable state.

## Ensemble

Sixteen aligned one-sided bijective parity ceiling pairs: worker_xor, counterpart_xor, worker_xnor,
counterpart_xnor on eight matched implication forms at Phi=2.0 per Q55 #175 and Q56 #181.

## Results

### H1 — Back-channel recipient determines tied singleton seam

All sixteen pairs tie the outer-party singleton cut that isolates the back-channel recipient. Worker
topologies tie {W,SC}; counterpart topologies tie {WS,C}. **Verdict: confirmed.**

### H2 — Dual at-system Phi with fixed normalized_phi split

All sixteen pairs have both outer-party two-part cuts at system Phi. The tied cut carries minimum
normalized_phi 0.5; the excluded cut carries 1.0. **Verdict: confirmed.**

### H3 — Two-to-one normalized_phi ratio

The excluded-to-tied normalized_phi ratio is 2.0 on all sixteen pairs with spread 0. **Verdict: confirmed.**

### H4 — Complete partition shares tied outer minimum

Complete partition minimum normalized_phi equals the tied outer cut on all sixteen pairs (0.5). **Verdict:
confirmed.**

### H5 — Gate-invariant direction rule

All eight worker topologies tie {W,SC}; all eight counterpart topologies tie {WS,C}, under both XOR and
XNOR gate polarity. **Verdict: confirmed.**

## Synthesis

One-sided channel direction fixes the favored outer-party singleton through the back-channel recipient.
Worker wiring augments W's update with input from C; counterpart wiring augments C with input from W. The
official tie set isolates that recipient as the singleton seam. Both outer cuts achieve system Phi, but
only the recipient-singleton cut shares the complete partition's minimum normalized_phi (0.5). The
non-recipient cut carries normalized_phi 1.0, exactly twice as large, and is excluded from the official
tie set. Gate polarity (XOR vs XNOR) does not alter the mapping; direction alone selects the recipient and
therefore the tied singleton.

## Validation gap

These results hold for n=3 deterministic Boolean models at synchronous update. Partition evaluation uses
PyPhi at the max-Phi reachable state. No claim extends to empirical organizations, coarser update
schedules, or n>3 systems.

## Reproduce

```
python -m org_frontier.questions.q57_channel_direction_mip.probe_recipient_seam_rule
python -m org_frontier.questions.q57_channel_direction_mip.probe_dual_norm_split
python -m org_frontier.questions.q57_channel_direction_mip.probe_norm_ratio
python -m org_frontier.questions.q57_channel_direction_mip.probe_complete_norm_equal
python -m org_frontier.questions.q57_channel_direction_mip.probe_gate_invariant_direction
```
