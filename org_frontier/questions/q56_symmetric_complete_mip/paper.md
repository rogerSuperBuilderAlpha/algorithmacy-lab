# Q56 — symmetric complete MIP geometry

## Question

Why do the sixteen symmetric bijective parity pairs that reach Phi=2.0 uniformly adopt the complete
three-part MIP {W,S,C} rather than the outer-party singleton seams seen on the aligned one-sided ceiling
pairs?

## Grounding

Q55 probe #178 reported the ceiling MIP split: sixteen symmetric pairs at complete `{W,S,C}`, sixteen
aligned one-sided pairs at outer-party singleton seams (`{W,SC}` or `{WS,C}`). The present study tests
five structural explanations on the thirty-two bijective parity ceiling pairs.

## Instrument

Exact IIT-4.0 Phi via PyPhi on n=3 deterministic Boolean coordination forms with labels (W, S, C). The
canonical triad W'=S, S'=W AND C, C'=S reads triadic at max_phi=2.0 with MIP `2 parts: {W,SC}`. Every
probe asserts this control before comparison. Official tie sets are read from `sia.ties`; partition
landscapes from `evaluate_partition` at the max-Phi reachable state.

## Ensemble

Thirty-two bijective parity ceiling pairs: sixteen symmetric (symmetric_xor, symmetric_xnor on eight
matched implication forms) and sixteen aligned one-sided (worker_xor, counterpart_xor, worker_xnor,
counterpart_xnor at Phi=2.0 per Q55 #175).

## Results

### H1 — Complete-only official tie set on symmetric pairs

All sixteen symmetric ceiling pairs have official tie set exactly `3 parts: {W,S,C}`. Zero include a
two-part outer-party partition. **Verdict: confirmed.**

### H2 — One outer-party tie plus complete on one-sided pairs

All sixteen aligned one-sided ceiling pairs have official tie set of size two: exactly one outer-party
two-part partition (`{W,SC}` or `{WS,C}`) together with the complete partition. **Verdict: confirmed.**

### H3 — Directional coupling symmetry

All sixteen symmetric ceiling pairs restore directional symmetry (in-degree equals out-degree per party,
W mirrors C). Zero of sixteen one-sided ceiling pairs are directionally symmetric. **Verdict: confirmed.**

### H4 — Dual outer-party at system Phi, excluded from official ties

All sixteen symmetric ceiling pairs have both `{W,SC}` and `{WS,C}` achieving system Phi at the max-Phi
state. Zero have an outer-party partition in the official tie set. **Verdict: confirmed.**

### H5 — Minimum normalized-phi tie-break rule

The predicted tie set from minimum normalized_phi among at-system-Phi partitions matches the official
tie set on all thirty-two ceiling pairs. On symmetric pairs only complete achieves the minimum; on
one-sided pairs one outer-party cut plus complete achieve it. **Verdict: confirmed.**

## Synthesis

Symmetric bijective parity coupling restores bilateral directional symmetry on the outer parties. Both
outer-party two-part cuts reach system Phi, but their normalized_phi stays above the complete partition
minimum. IIT-4.0 tie-break therefore admits only the complete partition into the official tie set. One-sided
aligned coupling breaks W/C directional symmetry; the favored outer-party cut shares the minimum
normalized_phi with complete and co-enters the tie set. The printed MIP first line is a representative from
that tie set, which is why symmetric pairs read complete-only while one-sided pairs read an outer-party
singleton seam.

## Validation gap

These results hold for n=3 deterministic Boolean models at synchronous update. Partition evaluation uses
PyPhi at the max-Phi reachable state. No claim extends to empirical organizations, coarser update
schedules, or n>3 systems.

## Reproduce

```
python -m org_frontier.questions.q56_symmetric_complete_mip.probe_complete_only_tie
python -m org_frontier.questions.q56_symmetric_complete_mip.probe_one_sided_outer_tie
python -m org_frontier.questions.q56_symmetric_complete_mip.probe_directional_symmetry
python -m org_frontier.questions.q56_symmetric_complete_mip.probe_dual_outer_excluded
python -m org_frontier.questions.q56_symmetric_complete_mip.probe_min_norm_tiebreak
```
