# Q52 — findings

Probes #160–#164. Exact IIT-4.0 Φ via PyPhi, n=3 deterministic Boolean forms, implication commits
{2,4,11,13} with Q51 back-channel transforms. Grows from Q51 probes #156 and #159.

| hypothesis | verdict | key numbers |
|---|---|---|
| H1 — W-centric party-read polarity at (W=1,C=0) | confirmed | 4/4 W-centric matched forms classified by S'(1,0) ≠ (iw=2); zero mismatches. |
| H2 — C-centric mid plateau (matched) | confirmed | 4/4 C-centric matched forms triadic at 0.415037. |
| H3 — mid rung invariant across read pairing | confirmed | 8/8 forms with s∈{4,11} at 0.415037 (four matched, four complementary). |
| H4 — symmetric lift of dyadic W-centric forms | confirmed | W1_S13_C1 and W2_S2_C2: dyadic one-sided → triadic 0.830075 symmetric. |
| H5 — symmetric collapse to high-rung equilibrium | confirmed | 8/8 matched symmetric forms triadic at uniform 0.830075; spread 0. |

**Through-line.** Q51 (#156) left a three-rung ladder on matched-read implication forms under one-sided
worker back-channel wiring. The mechanism splits by commit class. W-centric commits {2,13} (distinguishing
state W=1,C=0) split by whether party-read polarity aligns with S'(1,0): high rung 0.830075 when
S'(1,0) ≠ (iw=2), dyadic when they match (H1). C-centric commits {4,11} (distinguishing state W=0,C=1)
plateau at 0.415037 regardless of party-read index or pairing (H2, H3). The two one-sided dyadic forms
lift to the high rung under symmetric two-sided coupling (H4). Symmetric coupling then unifies the full
matched panel at 0.830075 — the one-sided high-rung value — with zero spread (H5). Ladder collapse tracks
restored outer-party coupling balance: one-sided wiring leaves commit-class-specific partial integration;
two-sided wiring reaches the symmetric equilibrium probe #77 reported for conjunctive triads.

**Caveats.** n=3 deterministic Boolean; synchronous update; conjunctive back-channel gates only. Results
describe coordination forms, not empirical organizations.

**Reproduce.**
```
python -m org_frontier.questions.q52_phi_ladder_mechanism.probe_wcentric_polarity
python -m org_frontier.questions.q52_phi_ladder_mechanism.probe_ccentric_plateau
python -m org_frontier.questions.q52_phi_ladder_mechanism.probe_mid_invariant
python -m org_frontier.questions.q52_phi_ladder_mechanism.probe_symmetric_lift
python -m org_frontier.questions.q52_phi_ladder_mechanism.probe_symmetric_collapse
```
