# Q58 — findings

## Hypothesis verdicts

| Hypothesis | Verdict | Key result |
|---|---|---|
| H1 — severed-connection ratio | confirmed | 16/16 cut_ones tied/excl ratio 2.0 (4 vs 2); spread 0. |
| H2 — normalization factor ratio | confirmed | 16/16 norm_factor excl/tied ratio 2.0 (0.5 vs 0.25); spread 0. |
| H3 — equal unnormalized phi | confirmed | 16/16 phi tied/excl ratio 1.0 (both 2.0 at system Phi). |
| H4 — complete cut geometry | confirmed | 16/16 complete matches recipient cut_ones=4 and norm_factor=0.25. |
| H5 — inverse cut-size law | confirmed | 16/16 norm_phi ratio equals cut_ones ratio (2.0). |

## Reading

Q57 #187 documented the fixed two-to-one normalized_phi ratio without identifying the normalization
denominator. The ratio is a direct consequence of IIT-4.0 `NUM_CONNECTIONS_CUT` normalization on the
min-norm at-system-Phi partition representatives. Both outer cuts carry unnormalized phi=2.0. The recipient
singleton severs four cut-matrix connections; the non-recipient severs two. Normalized_phi is 0.5 on the
recipient and 1.0 on the non-recipient. Complete co-enters the tie set because its min-norm representative
shares the recipient's four-connection cut geometry.

## Validation gap

Deterministic n=3 Boolean models at finest grain with synchronous update. PyPhi implements the
normalization rule; analytic cross-check against Albantakis et al. for these partition representatives
remains open.

## Reproduce

```bash
python -m org_frontier.questions.q58_normalization_cut_geometry.probe_severed_edge_ratio
python -m org_frontier.questions.q58_normalization_cut_geometry.probe_norm_factor_ratio
python -m org_frontier.questions.q58_normalization_cut_geometry.probe_equal_phi_baseline
python -m org_frontier.questions.q58_normalization_cut_geometry.probe_complete_cut_match
python -m org_frontier.questions.q58_normalization_cut_geometry.probe_inverse_cut_law
```
