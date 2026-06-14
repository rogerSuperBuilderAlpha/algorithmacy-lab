# Q57 — findings

Probes #185–#189. Exact IIT-4.0 Phi via PyPhi, n=3 deterministic Boolean forms, sixteen aligned one-sided
bijective parity ceiling pairs from Q56. Grows from Q56 probes #181 and #184.

| hypothesis | verdict | key numbers |
|---|---|---|
| H1 — recipient seam rule | confirmed | 16/16 one-sided ceiling pairs tie the cut isolating the back-channel recipient; worker→{W,SC}, counterpart→{WS,C}. |
| H2 — dual norm split | confirmed | 16/16 with both outer cuts at system Phi; tied outer norm 0.5, excluded outer norm 1.0. |
| H3 — two-to-one ratio | confirmed | 16/16 excluded/tied normalized_phi ratio 2.0; spread 0. |
| H4 — complete norm equality | confirmed | 16/16 complete partition min normalized_phi equals tied outer cut (0.5). |
| H5 — gate-invariant direction | confirmed | 8/8 worker topologies at {W,SC}; 8/8 counterpart at {WS,C} under XOR and XNOR. |

**Through-line.** Q56 (#181, #184) documented the one-sided dual tie and the minimum-normalized-phi rule
without naming the directional mechanism. The back-channel recipient — the outer party whose update rule
gains the extra incoming cross-edge — always determines which singleton seam co-enters the official tie
set with complete. Both outer-party cuts reach system Phi; the recipient-singleton cut carries minimum
normalized_phi 0.5, the non-recipient cut carries 1.0, and complete matches 0.5. XOR and XNOR preserve
the same recipient→singleton mapping.

**Caveats.** n=3 deterministic Boolean; synchronous update; partition scan at max-Phi reachable state.
Results describe coordination forms, not empirical organizations.

**Reproduce.**
```
python -m org_frontier.questions.q57_channel_direction_mip.probe_recipient_seam_rule
python -m org_frontier.questions.q57_channel_direction_mip.probe_dual_norm_split
python -m org_frontier.questions.q57_channel_direction_mip.probe_norm_ratio
python -m org_frontier.questions.q57_channel_direction_mip.probe_complete_norm_equal
python -m org_frontier.questions.q57_channel_direction_mip.probe_gate_invariant_direction
```
