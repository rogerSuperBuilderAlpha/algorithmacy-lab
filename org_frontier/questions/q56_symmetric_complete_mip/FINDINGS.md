# Q56 — findings

Probes #180–#184. Exact IIT-4.0 Phi via PyPhi, n=3 deterministic Boolean forms, thirty-two bijective parity
ceiling pairs from Q55. Grows from Q55 probe #178.

| hypothesis | verdict | key numbers |
|---|---|---|
| H1 — complete-only tie set | confirmed | 16/16 symmetric ceiling pairs with official tie set exactly `{W,S,C}`; 0/16 with outer-party in ties. |
| H2 — one-sided dual tie | confirmed | 16/16 one-sided ceiling pairs with exactly one outer-party two-part plus complete in official ties. |
| H3 — directional symmetry | confirmed | 16/16 symmetric directionally symmetric; 0/16 one-sided directionally symmetric. |
| H4 — dual outer excluded | confirmed | 16/16 symmetric with both `{W,SC}` and `{WS,C}` at system Phi; 0/16 with outer-party in official ties. |
| H5 — min normalized-phi rule | confirmed | 32/32 ceiling pairs match predicted tie set from minimum normalized_phi; 0 mismatches. |

**Through-line.** Q55 (#178) documented the MIP split without naming the mechanism. Symmetric bijective
parity coupling restores full directional W/C symmetry. Both outer-party two-part cuts achieve system Phi
on every symmetric pair, but IIT-4.0 tie-break excludes them: only the complete partition achieves the
minimum normalized_phi. One-sided aligned pairs break directional symmetry; one outer-party cut shares the
minimum normalized_phi with complete and enters the official tie set. The printed MIP first line follows
the tie set: complete-only on symmetric pairs, one outer-party singleton plus complete on one-sided pairs.

**Caveats.** n=3 deterministic Boolean; synchronous update; partition scan uses PyPhi `evaluate_partition`
at the max-Phi reachable state. Results describe coordination forms, not empirical organizations.

**Reproduce.**
```
python -m org_frontier.questions.q56_symmetric_complete_mip.probe_complete_only_tie
python -m org_frontier.questions.q56_symmetric_complete_mip.probe_one_sided_outer_tie
python -m org_frontier.questions.q56_symmetric_complete_mip.probe_directional_symmetry
python -m org_frontier.questions.q56_symmetric_complete_mip.probe_dual_outer_excluded
python -m org_frontier.questions.q56_symmetric_complete_mip.probe_min_norm_tiebreak
```
