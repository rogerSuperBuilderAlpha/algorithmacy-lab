# Q45 — findings

Probes #145–#149. Exact IIT-4.0 Φ via PyPhi, n=3 deterministic Boolean forms, strict-mediation family
(256 forms) and full 4096-wiring space for H5.

| hypothesis | verdict | key numbers |
|---|---|---|
| H1 — triadic forms sit at the edge floor | confirmed | All 24 triadic strict-mediation forms have exactly 4 edges (= 2(n−1)); 0 off-floor. |
| H2 — only AND reaches Φ = n−1 at the floor | refuted | 16 triadic forms at Φ = 2.0; only 2 use S-index 1 (AND). The other 14 use monotone non-AND commits (OR index 7, NOR 8, NAND 14, implication variants 2/4/11/13). |
| H3 — parity saturates its ceiling at the floor | confirmed | All 8 parity (XOR/XNOR) triadic forms: 4 edges, Φ = 0.5 = 2^(2−3); 0 off-ceiling. |
| H4 — OR does not bind in strict mediation | refuted | 2/16 OR-commit forms are triadic at Φ = 2.0 (W1_S7_C1, W2_S7_C2); 14 OR forms are dyadic. |
| H5 — global 4-edge max-Φ is AND-only | refuted | 312 triadic forms at 4 edges in the 4096 space; 192 reach Φ = 2.0; only 2 are strict-mediation AND; 190 counterexamples. |

**Through-line.** Every irreducible strict-mediation form sits at the lean four-edge floor (H1), confirming
#30. At that floor the Φ budget splits by commit *class*, not by AND alone: all eight parity forms saturate
their ceiling at Φ = 0.5 (H3), while sixteen monotone forms saturate at Φ = 2.0 — but only two of those
sixteen are AND (H2 refuted). OR binds triadically in strict mediation for two of sixteen OR-labelled forms
(H4 refuted), so the conjunctive hub is not the only commit that achieves irreducibility at the floor, and
OR is not categorically excluded. In the full wiring space, 192 triadic forms at four edges reach Φ = 2.0,
and almost all lie outside strict-mediation AND (H5 refuted). Agenda #48's uniqueness claim holds only at
the coarse monotone-versus-parity split: monotone commits share the high ceiling, parity commits share the
low one, and the edge floor is shared by both.

**Caveats.** n=3 only; edge count from the connectivity matrix; synchronous update. "Conjunctive" in #113
means monotone (non-parity), not AND specifically — this study's H2 tested AND index 1 explicitly. H5 used
strict-mediation plus AND truth table as the counterexample filter; relabeled equivalents were not exhaustively
quotiented.

**Reproduce.**
```
python -m org_frontier.questions.q45_edge_floor_uniqueness.probe_edge_floor
python -m org_frontier.questions.q45_edge_floor_uniqueness.probe_conjunctive_max
python -m org_frontier.questions.q45_edge_floor_uniqueness.probe_parity_floor
python -m org_frontier.questions.q45_edge_floor_uniqueness.probe_or_strict
python -m org_frontier.questions.q45_edge_floor_uniqueness.probe_global_floor
```
