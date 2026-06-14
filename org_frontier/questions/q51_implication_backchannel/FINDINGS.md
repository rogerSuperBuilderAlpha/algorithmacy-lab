# Q51 — findings

Probes #155–#159. Exact IIT-4.0 Φ via PyPhi, n=3 deterministic Boolean forms, strict-mediation family plus
minimal back-channel transforms. Grows from Q50 probe #154.

| hypothesis | verdict | key numbers |
|---|---|---|
| H1 — matched implication binds at Φ=2.0 with worker back-channel | partial | 0/8 at Φ=2.0; 6/8 triadic below ceiling (max 0.830075 on W1_S2_C1 and W2_S13_C2). |
| H2 — worker back-channel enables triadic binding for most matched forms | confirmed | 6/8 matched-read implication forms triadic with worker-side back-channel W'=f_W(S)∧C. |
| H3 — strict mediation control | confirmed | 0/8 matched-read implication forms triadic under strict mediation (all Φ=0). |
| H4 — back-channel preserves complementary implication at Φ=2.0 | partial | 8/8 complementary forms stay triadic with back-channel but all drop below ceiling (0.830075 or 0.415037; strict baseline Φ=2.0). |
| H5 — symmetric two-sided back-channel unifies matched binding | confirmed | 8/8 matched-read implication forms triadic at uniform max_phi=0.830075 with six edges. |

**Through-line.** Q50 (#154) required complementary party reads for implication commits at the four-edge
Φ=2.0 ceiling. A minimal worker-side back-channel does not swap that rule for matched reads at the ceiling:
zero of eight matched forms reach Φ=2.0 (H1 partial). The back-channel does restore irreducible binding for
most matched forms at lower Φ — six of eight read triadic, with magnitudes 0.830075 or 0.415037 depending on
commit index (H2 confirmed). The strict-mediation control confirms all eight matched forms stay dyadic without
the extra edge (H3). The same back-channel grades every complementary-read implication form down from Φ=2.0
while keeping them triadic (H4 partial). A symmetric two-sided back-channel (W'=f_W(S)∧C, C'=f_C(S)∧W)
lifts all eight matched forms to triadic at a single shared Φ=0.830075 (H5).

**Caveats.** n=3 deterministic Boolean; synchronous update; back-channel defined as conjunctive gate on the
existing party read. Results describe coordination forms, not empirical organizations.

**Reproduce.**
```
python -m org_frontier.questions.q51_implication_backchannel.probe_impl_phi2_matched
python -m org_frontier.questions.q51_implication_backchannel.probe_impl_triadic_matched
python -m org_frontier.questions.q51_implication_backchannel.probe_impl_strict_control
python -m org_frontier.questions.q51_implication_backchannel.probe_impl_complementary_preserve
python -m org_frontier.questions.q51_implication_backchannel.probe_impl_symmetric_unify
```
