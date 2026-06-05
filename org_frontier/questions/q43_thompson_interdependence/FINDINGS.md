# Q43 findings

Thompson's interdependence types (pooled, sequential, reciprocal) against the IIT-4.0 dyadic/triadic verdict. Matched triple at n=3, AND family. Instrument control (pass-through triad #57) passed in every probe: triadic, Φ=2.000000, MIP `2 parts: {W,SC}`.

| hypothesis | verdict | key numbers |
|---|---|---|
| H1 naive ordering | confirmed | pooled dyadic Φ=0.0; sequential triadic Φ=2.0; reciprocal triadic Φ=2.0. Pooled is strict Φ-min; sequential strictly-between=False (2.0 ties 2.0); monotone-in-Thompson-order=False. Top step collapses. |
| H2 "pooled" ambiguous | confirmed | independent-contribution pool n=3 dyadic Φ=0.0, MIP (factors), major complex {W,S}=2.0; all-required pool #116 n=3 triadic Φ=2.0 (surplus +0.0), n=4 triadic Φ=3.0 (surplus +1.0). Φ≈n−1. Opposite verdicts at fixed n=3; switch = joint determination. |
| H3 "sequential" ambiguous | confirmed | propagating chain triadic Φ=2.0 MIP {W,SC}; acyclic hand-off (`C'=C`) dyadic Φ=0.0 (factors). Switch = the return edge. |
| H4 reciprocal needs a cycle | confirmed | cyclic `[x[1],x[0]&x[2],x[1]]` triadic Φ=2.0 MIP {W,SC}, MC {W,S,C}, CM W→S,S→W,S→C,C→S (loop); bidirectional-acyclic `[x[1],x[0]&x[2],x[2]]` dyadic Φ=0.0, CM has `C'=C` self-loop, no cycle. The cycle decides; arrow count is silent. |
| H5 two-primitive replacement | refuted | claim (a) holds: pooled and sequential each span {dyadic, triadic}. Claim (b) fails: 4 forms share (joint-det=T, cycle=T), 3 with identical CM, yet cyclic=triadic Φ=2.0 vs bidirectional-acyclic=dyadic Φ=0.0; cycle predicate also fires on the dyadic independent-contribution pool. Primitive pair leaves verdict undetermined. |

**Through-line.** Thompson's labels track the verdict loosely. The ordering breaks at the top step (sequential ties reciprocal at Φ=2.0, pooled alone is dyadic), and two of the three types take both verdicts: pooled and sequential each flip verdict on a single edge (joint determination; the return edge). The obvious repair, reading the verdict off the primitive pair {joint determination, feedback cycle}, is refuted, because four forms share the pair (three with identical connectivity matrices) and still split, and the connectivity-matrix cycle predicate fires on a form that factors. A directed cycle in the connectivity matrix is a different object from a closed loop in the cause-effect structure IIT integrates over. The verdict turns on closed causal loops finer than the Thompson label and finer than the coarse primitive pair.

**Caveats.** n=3 throughout (one n=4 pool); deterministic Boolean rules, AND family only; verdict read at the most-integrated reachable state, `PHI_EPS=1e-9`, Φ an ordinal hint and no coordination-cost scale. Primitive coding in H5 is one operationalization, and a finer cause-effect predicate stays possible. The result holds about the model, with real organizations still beyond reach.

**Reproduce.** `~/iit-playground/venv-4.0/bin/python -m org_frontier.questions.q43_thompson_interdependence.probe_thompson_ordering` (also `probe_thompson_pooled`, `probe_thompson_sequential`, `probe_thompson_reciprocal`, `probe_thompson_primitives`).
