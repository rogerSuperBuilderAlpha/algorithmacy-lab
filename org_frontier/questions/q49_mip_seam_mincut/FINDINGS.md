# Q49 — findings

Probes #140–#144. Exact IIT-4.0 Φ via PyPhi, n=3 deterministic Boolean forms, seam read from the MIP tie
set (`sia.ties`) at the max-Φ reachable state.

| hypothesis | verdict | key numbers |
|---|---|---|
| H1 — canonical seam is a tie | confirmed | Canonical triad (S=W∧C): system Φ=2.0, 4 tied MIPs — `{W,SC}`, `{WS,C}`, and the complete `{W,S,C}` twice. Seam set `{W,C}`; `{S,WC}` absent. |
| H2 — no worker-unique seam | confirmed | All 24 triadic n=3 strict-mediation forms have (W in seam) == (C in seam); 0 worker-unique-seam violations. 16 conjunctive forms seam `{W,C}` (Φ=2.0), 8 parity forms empty seam (Φ=0.5, complete-partition MIP). |
| H3 — back-channel breaks the tie | refuted | Worker-side back-channel W'=S∧C stays triadic but at Φ=1.0 (down from 2.0); seam set stays `{W,C}`. The one-sided wiring asymmetry does not break the seam tie. |
| H4 — broken seam follows read direction | refuted | Worker-side channel seam `{W,C}`; counterpart-side channel seam `{W,C}`; symmetric two-sided channel Φ=6.0 with empty seam (complete partition). None matches the predicted `{C}`/`{W}`/`{W,C}`. The read direction does not move the seam. |
| H5 — seam ≠ connectivity min-cut | confirmed | Φ-seam and graph min-cut disagree on 8/11 forms. Conjunctive and one-sided forms agree (`{W,C}`); all 8 parity forms have empty Φ-seam (complete-partition MIP) vs min-cut `{W,C}`. No graph min-cut law for the seam. |

**Through-line.** The worker is never the unique weakest seam. For every triadic strict-mediation form the
MIP tie set severs the worker and the counterpart on equal terms, so the worker-as-weakest-seam reading of
#26 and #33 is a labeling convention over a degenerate tie. The 67% of forms #33 counted as cutting
`{W,SC}` are the 16 conjunctive forms, each of which ties `{W,SC}` with `{WS,C}`; the remaining 8 are
parity forms whose MIP is the complete partition with no singleton seam. The seam symmetry is more robust
than the wiring graph: a one-sided back-channel that makes the connectivity asymmetric still leaves the
seam tied, because the seam tracks the determination's symmetry in the two parties (balanced in every
triadic form, #16), not the edge graph. A graph min-cut accidentally matches the seam on conjunctive forms
but fails on every parity form, so agenda Q49's min-cut theorem does not hold.

**Caveats.** n=3 only; strict-mediation family plus three n=3 back-channel forms. The seam is read at the
max-Φ reachable state with synchronous update; the verdict's grain- and schedule-relativity (#32, #62,
#112) applies. The back-channel form (W'=S∧C) is one verdict-preserving asymmetry, not the only one; other
asymmetries (asymmetric reliability, self-loops) were not tested.

**Reproduce.**
```
python -m org_frontier.questions.q49_mip_seam_mincut.probe_seam_tie
python -m org_frontier.questions.q49_mip_seam_mincut.probe_seam_family
python -m org_frontier.questions.q49_mip_seam_mincut.probe_seam_break
python -m org_frontier.questions.q49_mip_seam_mincut.probe_seam_direction
python -m org_frontier.questions.q49_mip_seam_mincut.probe_seam_mincut
```
