# Q58 — normalization cut geometry

## Question

Why does isolating the back-channel recipient as the outer singleton yield normalized_phi exactly half that
of the non-recipient singleton on aligned one-sided ceiling pairs, and which IIT-4.0 partition repertoire
or cut-size asymmetry produces the fixed 2.0 ratio with zero spread across all sixteen forms?

## Grounding

Q57 probe #187 reported excluded/tied normalized_phi ratio 2.0 with spread 0 on sixteen aligned one-sided
ceiling pairs. Q57 probe #186 gave the absolute values (tied 0.5, excluded 1.0) without decomposing phi
from the normalization factor. The present study inspects PyPhi's IIT-4.0 normalization term on the
min-norm at-system-Phi partition representatives.

## Instrument

Exact IIT-4.0 Phi via PyPhi on n=3 deterministic Boolean coordination forms with labels (W, S, C). The
canonical triad W'=S, S'=W AND C, C'=S reads triadic at max_phi=2.0 with MIP `2 parts: {W,SC}`. Every
probe asserts this control before comparison. Normalization uses PyPhi's default `NUM_CONNECTIONS_CUT` rule:
`normalized_phi = phi × normalization_factor` with `normalization_factor = 1 / sum(cut_matrix)` for
`GeneralKCut` partitions.

## Ensemble

Sixteen aligned one-sided bijective parity ceiling pairs from Q55–Q57: worker_xor, counterpart_xor,
worker_xnor, counterpart_xnor on eight matched implication forms at Phi=2.0.

## Results

### H1 — Severed-connection count ratio

On min-norm at-system-Phi partitions, the recipient singleton severs cut_ones=4; the non-recipient
singleton severs cut_ones=2. The tied/excluded ratio is 2.0 on 16/16 pairs with spread 0. **Verdict:
confirmed.**

### H2 — Normalization factor ratio

The excluded min-norm partition carries normalization_factor=0.5; the tied partition carries 0.25. The
excluded/tied ratio is 2.0 on 16/16 pairs with spread 0. **Verdict: confirmed.**

### H3 — Equal unnormalized phi baseline

Both outer cuts reach unnormalized phi=2.0 at system level on every pair. The phi tied/excluded ratio is
1.0 on 16/16. The 2.0 normalized_phi split is not driven by phi asymmetry. **Verdict: confirmed.**

### H4 — Complete shares recipient cut geometry

The complete partition min-norm representative shares cut_ones=4 and normalization_factor=0.25 with the
recipient singleton on 16/16 pairs. **Verdict: confirmed.**

### H5 — Inverse cut-size law

The normalized_phi ratio (excl/tied = 2.0) equals the cut_ones ratio (tied/excl = 2.0) on 16/16 pairs,
confirming `NUM_CONNECTIONS_CUT` as the sole source of the fixed split when phi is held constant.
**Verdict: confirmed.**

## Mechanistic summary

The two-to-one normalized_phi ratio from Q57 #187 follows directly from IIT-4.0 cut-size normalization.
Both outer cuts reach identical unnormalized phi=2.0. The recipient singleton's min-norm partition severs
four cut-matrix connections; the non-recipient severs two. With `normalization_factor = 1 / cut_ones`,
normalized_phi is 0.5 on the recipient (2.0 × 0.25) and 1.0 on the non-recipient (2.0 × 0.5). The complete
partition co-enters the tie set because its min-norm representative shares the recipient's four-connection
cut geometry.

## Validation gap

Results apply to deterministic n=3 Boolean models at finest grain with synchronous update. The normalization
mechanism is PyPhi's IIT-4.0 implementation; independent verification against the Albantakis et al.
analytic normalization for these specific partition representatives is not yet shown.

## Reproduce

```bash
python -m org_frontier.questions.q58_normalization_cut_geometry.probe_severed_edge_ratio
python -m org_frontier.questions.q58_normalization_cut_geometry.probe_norm_factor_ratio
python -m org_frontier.questions.q58_normalization_cut_geometry.probe_equal_phi_baseline
python -m org_frontier.questions.q58_normalization_cut_geometry.probe_complete_cut_match
python -m org_frontier.questions.q58_normalization_cut_geometry.probe_inverse_cut_law
```
