# Research program v2 — expanding the completed probe loop

The first program closed at Probe 98: all 50 agenda projects computed or designed. This second program
expands it. Every project here builds on a specific completed probe and opens territory the first
program left at a clean edge — the estimation results (Waves 7–8), the scaling collapse (Wave 9), the
function-content residual (#94), and two honest nulls (#98 ABM, #48/#80 Φ-vs-success).

Numbering continues the logbook: v2 probes start at 99. Each runs the same loop — write a script citing
reusable infra, run on the IIT-4.0 venv, log to `probes/PROBES.md`, update the status table below, commit
to main, push, report once per wave.

Lanes: **R** runnable now · **X** runnable but heavy · **T** tooling-absent · **H** human/data.

## A. The estimation frontier

The verdict is recoverable from time series (Φ_AR 0.925 at #84, random forest 1.0 at #85, CES counts
1.0 at #93) while Φ_R fails at any length or noise (#86, #87). The open questions are sharper than what
was answered.

- **A1 — surrogate-transfer** `[R]` — H: a cheap feature model trained on n=3 predicts the verdict at
  n=4/5 where exact Φ is costly. M: compute size-invariant aggregate features (mean/max over nodes,
  pairs) on noisy trajectories; train a random forest on the n=3 corpus; test on n=4 and n=5 samples.
  Builds on #85, #95. Out: `probe_surrogate_transfer.py`.
- **A2 — minimal-features** `[R]` — H: two or three features carry the perfect recovery #85 got with
  thirteen. M: per-feature AUC and greedy forward selection to the smallest set reaching AUC ≈ 1.0.
  Builds on #85, #90. Out: `probe_minimal_features.py`.
- **A3 — phi-ar-failure** `[R]` — H: the forms Φ_AR misranks are the parity / pure-higher-order forms a
  linear AR model cannot see. M: from the cached consilience panel, find Φ_AR's worst-ranked triadic
  forms and cross-tab against Φ_exact = 0.5 (the parity forms, #56). Builds on #84, #89, #56. Out:
  `probe_phi_ar_failure.py`.
- **A4 — exact-ces-predicate** `[X]` — H: a single CES count threshold is an exact verdict equivalent.
  M: compute the CES suite over the 256 corpus; test candidate predicates (n_relations ≥ k,
  frac_higher_order > 0, max_order ≥ 2) for zero error against the verdict. Builds on #93, #36. Out:
  `probe_ces_predicate.py`.

## B. Scaling and topology

Triadicity through a single mediator vanishes by n=6 (#97), always at the 2(n−1) floor (#95, #96). But
chains (#57) and trees (#58) preserve Φ=2.0, and all-required pools grow Φ with size (#65). Topology, not
size, is the live variable.

- **B1 — distributed-mediators** `[X]` — H: distributed mediation sustains triadicity at sizes a single
  hub cannot. M: build modular topologies (two mediators each binding a subset, linked) at n=6,7 and
  compare the verdict to the single-hub collapse. Builds on #97, #57. Out: `probe_distributed_mediators.py`.
- **B2 — topology-map** `[X]` — H: which topology classes keep the verdict and which grow Φ with size.
  M: classify representative chain, tree, single-hub, multi-hub, and pool forms at fixed n=5; chart
  survives? / Φ-grows?. Builds on #57, #58, #65, #97. Out: `probe_topology_map.py`.
- **B3 — lean-n6-existence** `[X]` — H: a lean triadic n=6 form exists even though random sampling found
  none. M: test the specific conjunctive (all-required) strict-mediation n=6 form directly rather than
  by random fill. Builds on #96, #97, #65. Out: `probe_lean_n6.py`.

## C. Finishing the N&S theorem

Probe 94 found connectivity decides 93% of the n=3 verdict; the last 7% turns on the Boolean function
content. Parity / XOR determinations are special everywhere (#10, #28, #43, #56).

- **C1 — nonseparability-ns** `[R]` — H: "all three nodes bidirectionally coupled AND the determination
  is non-separable" is the exact N&S condition. M: over the 4096 n=3 wirings, add a non-separability
  feature per node's function; test whether it closes #94's residual to zero error. Builds on #94, #56.
  Out: `probe_nonseparability.py`.

## D. The behavioral gap

Independent selfish learners do not find triadic forms harder (#98), and Φ is orthogonal to match-success
(#48, #80). The question is whether the right agent or the right outcome measure recovers a link.

- **D1 — tom-agents** `[R]` — H: agents that must model the partner show the difficulty gap independent
  bandits did not. M: re-run the coordination game with joint-action / partner-modeling learners; correlate
  learning difficulty with the verdict. Builds on #98, #88. Out: `probe_tom_agents.py`.
- **D2 — resilience** `[R]` — H: Φ tracks resilience (recovery from perturbation) even though it does not
  track success. M: perturb each form's state, measure recovery time to attractor, correlate with the
  verdict. Builds on #48, #27, #38. Out: `probe_resilience.py`.
- **D3 — hysteresis** `[R]` — H: rebinding an ejected party is path-dependent. M: drive a mediator with a
  sticky coupling memory up then down in party-reliance; compare the Φ paths. Builds on #79, #43. Out:
  `probe_hysteresis.py`.

## E. Political economy, continued

Extractive commits eject parties → {S,P} (#78); toothless oversight is a sink (#76).

- **E1 — ejection-order** `[R]` — H: as a commit tilts toward the owner, parties drop in a fixed order.
  M: sweep the tilt continuously; record the core at each step and the drop sequence. Builds on #78. Out:
  `probe_ejection_order.py`.
- **E2 — regulator-coalition** `[R]` — H: two weak (observe-only) regulators jointly bind where one does
  not. M: two regulators each reading the commit without an individual veto; test joint core membership.
  Builds on #76, #66. Out: `probe_regulator_coalition.py`.

## F. Hardening the instrument

The verdict is grain-relative (#32, #60) and schedule-relative (#62).

- **F1 — invariant-verdict** `[X]` — H: a verdict aggregated over grains and schedules is more robust for
  empirical use. M: compute the verdict across grains 1–3 and both update schedules; define and test an
  aggregate rule. Builds on #60, #62. Out: `probe_invariant_verdict.py`.

## Waves and status

Probe numbering continues from 98.

| Wave | Projects | Lane | Status |
|------|----------|------|--------|
| V1 | A1 A2 A3 A4 | R/X | **done** (probes 99–102; A1/A2 confirmed, A3 partial, A4 refuted-clean) |
| V2 | B1 B2 B3 | X | pending |
| V3 | C1 D1 D2 D3 | R | pending |
| V4 | E1 E2 F1 | R/X | pending |

Definition of done (per project): a committed script, a result with exact numbers, and a log entry in
`probes/PROBES.md` continuing the numbering. Stop rule: all Lane-R/X projects done.
