# Q53 — findings

Probes #165–#169. Exact IIT-4.0 Φ via PyPhi, n=3 deterministic Boolean forms, implication commits
{2,4,11,13} with matched party reads and extended back-channel topologies. Grows from Q51 probes #155,
#159 and Q52 probe #164.

| hypothesis | verdict | key numbers |
|---|---|---|
| H1 — counterpart-side AND restores Φ=2.0 | partial | 0/8 at ceiling; 6/8 triadic below (max 0.830075). |
| H2 — OR-graded worker-side restores Φ=2.0 | partial | 0/8 at ceiling; 6/8 triadic below (max 0.830075). |
| H3 — XOR gates exceed 0.830075 equilibrium | confirmed | 16/24 XOR pairs exceed 0.830075; symmetric_xor reaches 2.0 on all 8 matched forms. |
| H4 — no AND/OR/cross topology restores Φ=2.0 | confirmed | 0/64 pairs at ceiling across eight conjunctive-style topologies. |
| H5 — supremum is exactly 0.830075 | refuted | Global max = 2.0 via XOR; symmetric-AND panel uniform at 0.830075 (8/8, spread 0). |

**Through-line.** Q51–Q52 pinned 0.830075 as the symmetric-AND equilibrium for matched implication under
conjunctive back-channel gates. The broader sweep splits the answer by gate class. AND, OR, and mixed
cross topologies never restore Φ=2.0 (H4); their supremum is 0.830075, saturated by symmetric-AND on all
eight forms. XOR parity gates break the ceiling: symmetric_xor reaches Φ=2.0 on every matched form;
one-sided XOR reaches 2.0 on four of eight (the commit-class complement of the one-sided AND ladder).
Counterpart-AND mirrors the worker-AND ladder with W-centric and C-centric roles exchanged (H1 partial).
Worker-OR grades differently but still caps below 2.0 (H2 partial). The 0.830075 value is the absolute
maximum for conjunctive-style coupling only; parity coupling restores the strict-mediation ceiling.

**Caveats.** n=3 deterministic Boolean; synchronous update; finite gate panel {AND, OR, XOR}. Results
describe coordination forms, not empirical organizations.

**Reproduce.**
```
python -m org_frontier.questions.q53_impl_phi_ceiling.probe_counterpart_and_ceiling
python -m org_frontier.questions.q53_impl_phi_ceiling.probe_worker_or_ceiling
python -m org_frontier.questions.q53_impl_phi_ceiling.probe_xor_exceed_equilibrium
python -m org_frontier.questions.q53_impl_phi_ceiling.probe_topology_sweep_phi2
python -m org_frontier.questions.q53_impl_phi_ceiling.probe_supremum_characterization
```
