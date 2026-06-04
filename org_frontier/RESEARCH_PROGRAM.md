# Research Program: an executable design for the 50-question agenda

This operationalizes [`RESEARCH_AGENDA.md`](RESEARCH_AGENDA.md) into a program that runs continuously,
wave by wave, without per-project check-ins. Each of the 50 questions becomes a project with a
concrete method, the reusable infrastructure it uses, an expected artifact, and a feasibility lane.
Projects that cannot run autonomously (external data, human subjects, unavailable tooling) are routed
to a parking lane so the loop never stalls on them.

## How to run it continuously

**The loop, per project.** Write a probe script `probes/probe_<slug>.py` (or a sub-experiment folder
for larger studies) → run it on `~/iit-playground/venv-4.0/bin/python -m org_frontier...` → append one
row to the status table below and a result block to `probes/PROBES.md` (continuing the numbering past
53) → after a wave of ~5, make one commit of `org_frontier/`, fast-forward `main`, push, leave the
`dissertation/` working-tree edits untouched. Report once per wave, not per project.

**Definition of done (per project).** A committed script, a result with exact numbers, and a log entry
stating question / hypothesis / method / result, honest about nulls and refutations. Apply the
rate-it discipline: a vivid named-form result is an existence proof; rate it against a population
before stating it as general.

**Cadence.** ~5 projects per wave (the established batch size). Continue wave after wave until the
runnable set (Lane R) is exhausted; background the heavy ones (Lane X); document and skip the parked
lanes (T, D, H). Heavy/background runs use `run_in_background`; the loop proceeds to the next project
while they compute.

**Stop conditions.** Only three: a project is blocked (route to its parking lane and continue, do not
stall), a hard tool failure that cannot be worked around, or all Lane-R/Lane-X projects are done.

## Feasibility lanes

- **R — runnable now.** Uses existing infrastructure; foreground or quick. The bulk of the program.
- **X — heavy compute.** Full or large-sample enumerations / per-form CES or emergence; run in the
  background or by sampling, and log what was sampled vs censused.
- **T — needs tooling not on this branch.** Multi-valued PyPhi (#5), an IIT-3.0 config/install (#8).
  Attempt the install once; if blocked, document and park.
- **D — needs external data.** Real organizational logs (#24). Stage a protocol and a synthetic
  stand-in; do not fabricate data.
- **H — needs humans.** A lab experiment (#41), inter-rater coding (#42). Produce the design and
  pre-registration only; cannot be run autonomously.

## Reusable infrastructure (cite these in each script)

- `classifier/classifier.py`: `classify_rules`, `classify`, `tpm_from_rules`, `cm_from_rules`,
  `Verdict`, `PHI_EPS`.
- `probes/lib.py`: `verdict`, `major_complex`, `max_phi_float` (exact Φ on stochastic TPMs);
  `probes/_info.py`: `entropy`, `mutual_information`, `transfer_entropy`, `o_information`.
- `proxy_audit/exact_phi.py`: `exact_big_phi`, `reachable_states`, `network_phi`, `simulate_trajectory`.
- `proxy_bridge/bridge.py`: `add_noise`. `phyid.calculate.calc_PhiID`.
- `emergence_vs_phi/emergence.py`: `effective_information`, `macro_tpm`, `causal_emergence`.
- `corpus/population.py`: `enumerate_family` (256 strict-mediation n=3 forms); `corpus/forms_library.py`.
- `multiparty/scaling.py`: `sample_form(n)`. `structure_suite/suite.py`: `extract_suite`
  (distinctions/relations). `probes/probe_variance.py`: `success_rate`.

---

## The projects

Format: **#agenda-id slug** — H: hypothesis. M: method (infra). Out: artifact. `[lane · cost]`.

### A. Hardening the two-condition account

- **#1 higher-order-influence** — H: a pairwise/synergy influence term lifts the family AUC toward
  0.89. M: extend `probe_pivotality`/`probe_family_validation` with a PID-style joint-influence feature
  over `enumerate_family`; compare AUC. Out: `probe_joint_influence_v2.py`. `[R · cheap]`
- **#2 ces-predicts-verdict** — H: relation/distinction counts predict triadicity where per-node
  influence cannot. M: `extract_suite` over the 256 family; logistic/threshold on relation count vs
  verdict. Out: `probe_ces_predictor.py`. `[X · per-form CES, background]`
- **#3 minimal-edge-n5n6** — H: the 2(n−1) edge floor is tight at n=5,6. M: sample `sample_form(5)`,
  `sample_form(6)`; min edges among triadic. Out: `probe_min_triad_n56.py`. `[X · n=6 costly, sample]`
- **#4 full-n4-rate** — H: the complete n=4 family triadic rate and edge distribution. M: enumerate or
  large-sample the n=4 family; classify. Out: `probe_n4_census.py`. `[X · 16k forms, background/sample]`
- **#5 multivalued-pivotality** — H: ternary parties obey the same law. M: needs PyPhi multi-valued
  (Gomez 2021), absent on the IIT-4.0 branch. `[T · attempt install, else park]`

### B. Verdict robustness and scope

- **#6 individuation-invariance** — H: verdict invariant under state coarse-grainings. M: apply
  coarse-grainings to corpus TPMs, reclassify. Out: `probe_individuation.py`. `[R · cheap]`
- **#7 grain-threshold** — H: a sampling rate below which the triad is always detectable. M: compose
  k-step maps (k=1..) on corpus forms; find the flip threshold vs attractor period. Out:
  `probe_grain_threshold.py`. `[R · cheap]`
- **#8 iit3-vs-iit4** — H: 3.0 and 4.0 agree on the verdict. M: needs an IIT-3.0 config/install.
  `[T · attempt, else park]`
- **#9 correlated-noise** — H: structured noise can flip the verdict, not just the magnitude. M: build
  correlated-noise TPMs; `max_phi_float`. Out: `probe_correlated_noise.py`. `[R · cheap]`
- **#10 async-update** — H: verdict stable under asynchronous update. M: asynchronous TPM analogue
  (random-order updates → effective TPM); classify. Out: `probe_async.py`. `[R · modeling]`

### C. Multi-party scaling and structure

- **#11 rate-past-n5** — H: the triadic rate floors or hits zero past n=5. M: `sample_form(6)` sample.
  Out: `probe_scale_n6.py`. `[X · background]`
- **#12 chain-theorem** — H: chain Φ = 2.0 is exact at all depths. M: compute chains to n=7; attempt a
  short proof sketch from the MIP structure. Out: `probe_chain_theorem.py` + note. `[R/X · cheap-ish]`
- **#13 tree-topology** — H: branching mediation dilutes like breadth or preserves like depth. M: build
  balanced/unbalanced trees; classify + major complex. Out: `probe_trees.py`. `[R · cheap]`
- **#14 team-core-from-graph** — H: a graph rule names the major complex without computing Φ. M: sample
  heterogeneous teams; fit a connectivity rule to `major_complex`. Out: `probe_team_core_rule.py`.
  `[R · moderate]`
- **#15 group-surplus-boundary** — H: group-beyond-members integration generalizes past the pool at
  n≥4. M: `subset_phi` sweep across forms and sizes. Out: `probe_group_surplus.py`. `[R · moderate]`

### D. Dynamics and time

- **#16 lifted-regime** — H: a switching rule binds its regime when the regime is lifted into the
  state. M: lift the regime node, recompute the verdict/core. Out: `probe_lifted_regime.py`. `[R]`
- **#17 adaptive-mediator** — H: a learning mediator's verdict trajectory differs from a fixed one.
  M: epoch the determination by a simple update; classify per epoch. Out: `probe_adaptive.py`. `[R]`
- **#18 phi-vs-success-over-learning** — H: Φ and success decouple as the form is trained. M: a
  learning loop over worker policy; track `success_rate` and Φ. Out: `probe_learning.py`. `[R]`
- **#19 criticality-peak** — H: some form has an interior Φ maximum vs a coupling parameter. M: sweep
  coupling/order parameters with `max_phi_float`; look for a peak. Out: `probe_criticality.py`. `[R]`

### E. Estimation and the data bridge

- **#20 phi-ar-proxy** — H: Barrett–Seth Φ_AR recovers the verdict better than Φ_R/Φ_WMS. M: implement
  the autoregressive Φ_AR estimator; run the proxy-bridge comparison. Out: `probe_phi_ar.py`. `[R ·
  implement estimator]`
- **#21 learned-surrogate-coord** — H: a feature-combining model recovers the binary verdict. M: reuse
  the `learned_surrogate` random-forest pipeline on corpus/family cheap features. Out:
  `probe_learned_surrogate.py`. `[R · moderate]`
- **#22 phiid-trajectory-length** — H: longer trajectories never recover the missed verdict. M: sweep
  trajectory length in the proxy bridge. Out: `probe_phiid_length.py`. `[R]`
- **#23 phiid-redundancy-noise** — H: MMI vs CCS or higher noise changes ΦID separation. M: sweep both
  in `probe_phiid_social`. Out: `probe_phiid_sweep.py`. `[R]`
- **#24 real-org-logs** — H: the verdict is estimable from interaction logs. M: needs a dataset; stage
  a validation protocol and a synthetic-log stand-in. `[D · stage protocol, park]`

### F. The construct's dimensions and neighbors

- **#25 model-fidelity-displacement** — H: a better model displaces the counterpart more. M: sweep the
  inference node's fidelity; measure C-out rate. Out: `probe_model_fidelity.py`. `[R]`
- **#26 aimc-boundary** — H: a timescale or boundary criterion recovers the AI-MC/algorithmacy
  distinction. M: vary the AI node's update speed; test whether the verdict separates. Out:
  `probe_aimc_boundary.py`. `[R]`
- **#27 second-order-tom** — H: nested theory-of-mind adds to the core or stays a sink. M: add a
  second model node; major complex. Out: `probe_second_order_tom.py`. `[R]`
- **#28 sensemaking-family** — H: sensemaking is dyadic across a family, like the literacies. M: build a
  family of internal-process forms; classify. Out: `probe_sensemaking.py`. `[R]`
- **#29 multi-role-agent** — H: a two-platform agent's two cores are independent. M: model an agent that
  is worker on one platform and counterpart on another; read both cores. Out: `probe_multirole.py`. `[R]`

### G. Platform features and political economy

- **#30 generic-SP-core** — H: a coupling regime makes {S,P} the generic core. M: extend the principal
  sweep; rate {S,P} occurrence. Out: `probe_principal_regime.py`. `[R]`
- **#31 value-capture** — H: irreducibility predicts who captures surplus. M: define a payoff
  functional over the determination; relate to Φ and the core. Out: `probe_value_capture.py`.
  `[R · modeling]`
- **#32 regulator-node** — H: effective oversight must join the core. M: add a regulator that can
  override S; classify + major complex across coupling. Out: `probe_regulator.py`. `[R]`
- **#33 coalition-size** — H: a larger counterpart coalition always wins vs the principal. M: scale the
  coalition in `probe_interaction`. Out: `probe_coalition_size.py`. `[R]`
- **#34 platform-info-asymmetry** — H: the platform observing more than either party has a distinct
  signature. M: model partial observability per party; compare. Out: `probe_info_asymmetry.py`. `[R]`
- **#35 fairness-signature** — H: a non-extractive determination has a different Φ signature. M:
  parametrize principal weighting; relate fairness to influence-balance (Probe 16). Out:
  `probe_fairness.py`. `[R]`

### H. Adjacent measures and consilience

- **#36 consilience-map** — H: the adjacent measures agree with exact Φ on some forms and diverge on
  others, mappably. M: over the 256 family, compute exact Φ, O-information, ΦID synergy, EI, and causal
  emergence; cross-tabulate verdict agreement. Out: `probe_consilience.py` + table. `[X · 256 ×
  several measures, background]`
- **#37 cheap-measure-search** — H: no cheap measure cleanly separates the verdict. M: rank every
  cheap measure by AUC against the verdict over the family. Out: `probe_cheap_search.py`. `[X ·
  background]`
- **#38 o-info-on-transitions** — H: O-information on the transition structure separates better than on
  the present-state joint. M: compute O-information over the TPM-induced transition distribution. Out:
  `probe_o_info_transitions.py`. `[R]`
- **#39 ei-vs-phi-family** — H: the EI-vs-Φ relationship from Probe 49 generalizes. M:
  `effective_information` + `causal_emergence` over the 256 family. Out: `probe_ei_family.py`. `[X ·
  background]`

### I. Validation and ground truth

- **#40 abm-difficulty-corpus** — H: the verdict tracks an agent-based coordination-difficulty measure
  across the corpus. M: a small ABM (Q-learning agents) per corpus form; correlate learned difficulty
  with the verdict. Out: `probe_abm_difficulty.py`. `[R · moderate compute]`
- **#41 human-subjects** — H: humans coordinating through triadic vs dyadic interfaces show the
  difficulty gap. M: experiment design + pre-registration only. `[H · design only, park]`
- **#42 inter-rater-coding** — H: coders agree on real organizations' coordination structures. M: a
  coding protocol + reliability plan only. `[H · design only, park]`
- **#43 non-collapsing-niizato** — H: a size-4 discontinuity appears in a richer-dynamics family. M:
  design non-collapsing dynamics; compute Φ across sizes; look for a discontinuity. Out:
  `probe_niizato_rich.py`. `[R · moderate]`

### J. Theory and formal characterization

- **#44 phi-free-test** — H: a graph predicate (non-separable determination hypergraph + feedback
  cycle) matches the verdict, giving a Φ-free test. M: define the predicate; validate against all 256
  verdicts. Out: `probe_phi_free_test.py`. `[R · cheap]`
- **#45 ns-theorem-n3** — H: a necessary-and-sufficient structural condition for n=3 triadicity. M:
  exhaustive over 4096 wirings; mine the structural features that perfectly separate the verdict. Out:
  `probe_ns_theorem.py` + note. `[X · 4096, background]`
- **#46 role-symmetry-automorphism** — H: worker↔counterpart relabeling is an exact verdict
  automorphism. M: test the relabel over the family for any flip. Out: `probe_role_symmetry.py`. `[R]`
- **#47 pure-higher-order-form** — H: a form is triadic with no individually pivotal party. M: search
  the family for triadic forms where every node's influence is below the inclusion threshold. Out:
  `probe_pure_higher_order.py`. `[R]`

### K. New application domains

- **#48 market-clearinghouse** — H: a clearinghouse matching many buyers and sellers is triadic. M:
  model a small market form (buyers, sellers, clearing mechanism); classify + major complex. Out:
  `probe_market.py`. `[R]`
- **#49 voting-aggregation** — H: which aggregation rules yield triadic governance. M: classify
  plurality, majority, supermajority, veto, ranked aggregation forms (extends Probe 10). Out:
  `probe_voting.py`. `[R]`
- **#50 multi-agent-ai** — H: an AI-agent protocol is dyadic (conveyor) or triadic (committing third
  party). M: model agents coordinating via a shared protocol node; classify. Out: `probe_mas.py`. `[R]`

---

## Execution waves

Ordered so cheap and foundational projects run first, heavy ones go to the background, and parked
lanes are documented without stalling the loop. ~5 per wave.

1. **Formal core (cheap, foundational):** #44, #46, #47, #12, #13.
2. **Robustness:** #6, #7, #9, #10, #16.
3. **Structure & aggregation:** #14, #15, #33, #49, #48.
4. **Dimensions & neighbors:** #25, #26, #27, #28, #29.
5. **Political economy:** #30, #31, #32, #34, #35.
6. **Dynamics:** #17, #18, #19, #43, #38.
7. **Estimation:** #20, #21, #22, #23, #50.
8. **Consilience & scaling (background-heavy):** #36, #37, #39, #2, #1.
9. **Heavy enumerations (background):** #45, #4, #3, #11, #40.
10. **Parked lanes (document/design only):** #5 (T), #8 (T), #24 (D), #41 (H), #42 (H).

## Status tracker

Update on each run: `pending → running → done` (or `blocked`). Probe numbering continues from 54.

| Wave | Projects | Lane | Status |
|---|---|---|---|
| 1 | #44 #46 #47 #12 #13 | R | **done** (probes 54–58; #44 partial, #46/#47/#12 confirmed, #13 refuted) |
| 2 | #6 #7 #9 #10 #16 | R | **done** (probes 59–63; #6/#7/#10 confirmed, #16 refuted, #9 modeling-limited) |
| 3 | #14 #15 #33 #49 #48 | R | **done** (probes 64–68; #15/#33/#49/#48 confirmed, #14 partial) |
| 4 | #25 #26 #27 #28 #29 | R | **done** (probes 69–73; #25/#27/#28/#29 confirmed, #26 clarifying refutation) |
| 5 | #30 #31 #32 #34 #35 | R | **done** (probes 74–78; #32/#35 confirmed, #30/#34/#31 partial-or-refined) |
| 6 | #17 #18 #19 #43 #38 | R | pending |
| 7 | #20 #21 #22 #23 #50 | R | pending |
| 8 | #36 #37 #39 #2 #1 | X | pending |
| 9 | #45 #4 #3 #11 #40 | X | pending |
| 10 | #5 #8 #24 #41 #42 | T/D/H | pending (parked: document only) |

## Conventions (carried from the lab)

- House style in all prose (`CLAUDE.md`): no first person; short blunt claims; one em-dash per
  paragraph; no "Crucially/Importantly", no "not X but Y", no breathless adjectives.
- Validate any new instrument on its own controls before trusting a verdict (the playbook's rule).
- Read the verdict on the major complex when a form may have spectator nodes; otherwise on
  whole-system Φ over the MIP.
- Commit per wave; ff `main`; push; stage `org_frontier/` only, leaving the `dissertation/` edits
  untouched. Log every project in `probes/PROBES.md` with question/hypothesis/method/result.
- Report honestly: refutations and nulls are first-class results and are logged as such.
