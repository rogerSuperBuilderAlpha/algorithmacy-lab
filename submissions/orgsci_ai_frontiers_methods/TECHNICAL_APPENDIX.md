# Technical Appendix: An Exact Test for Triadic Coordination

[DRAFTED by Claude, 26 Oct 2026. Anonymous. Companion to the proposal. Every number below was re-run on 26 Oct 2026 from the anonymized repository, or is tied to a regression check named in A6.]

## A1. Encoding a coordination form

A coordination form with *n* parties is a deterministic Boolean network on *n* binary nodes. Node *i* holds party *i*'s state (acts or does not act, available or not, approves or does not), and a rule f_i maps the current state of the network to node *i*'s next state. The rules determine a state-by-node transition probability matrix (TPM) and a connectivity matrix. In the classifier's convention, node 0 is the worker, node 1 the system and node 2 the counterpart (little-endian state order).

Example: the strict-mediation triad.

| Party | Rule | Reading |
|---|---|---|
| Worker (0) | x0′ = x1 | the worker acts on the system's signal |
| System (1) | x1′ = x0 AND x2 | the system commits only when both parties are in |
| Counterpart (2) | x2′ = x1 | the counterpart responds to what the system shows |

The worker and counterpart have no direct edge. Each reads only the system.

## A2. The verdict

We compute system integrated information under IIT 4.0 (Albantakis et al., 2023) with PyPhi (Mayner et al., 2018). For a candidate system in state *s*, PyPhi evaluates every directional partition of the nodes and returns φ over the minimum-information partition (MIP), the partition that minimises normalised integrated information. The classifier takes the maximum over reachable states and returns:

| Φ over the MIP | Structure | Reading |
|---|---|---|
| Φ_MIP = 0 | dyadic | some party-respecting cut leaves the cause–effect structure intact |
| Φ_MIP > 0 | triadic | no cut does; the parties are bound through the mediator |

The test uses the MIP. Φ over the complete cut (every node separated) is positive for any coupled pair, so it over-calls every coupled dyad as a triad. The classifier also returns the *major complex*, the subset of nodes with maximal Φ, which names the parties bound into the irreducible structure. The major complex matters when a form has spectator nodes: a whole system can factor while a triad inside it stays irreducible.

Only the binary verdict is interpreted. Φ magnitude depends on the encoding (the number of states per party, the rule family) and is at most an ordinal hint.

## A3. Validation on the instrument's own controls

Every run first reproduces known controls and stops if any fails (`python -m org_frontier.classifier.validate`). The controls include:

| Control or form | Expected | Observed (re-run 26 Oct 2026) |
|---|---|---|
| Factoring control (counterpart decoupled) | dyadic | dyadic, Φ_MIP = 0.000 |
| Irreducible control (full coupling) | triadic | triadic, Φ_MIP = 0.830 |
| Chat dyad | dyadic | dyadic, Φ_MIP = 0.000 |
| Dyadic gig model | dyadic | dyadic, Φ_MIP = 0.000 |
| Strict-mediation triad (A1; résumé → applicant-tracking system → hiring manager) | triadic | triadic, Φ_MIP = 2.000 |
| Applicant-tracking form with factoring feedback | dyadic | dyadic, Φ_MIP = 0.000 |
| Gig "false dyad" (a worker alone with an app, bound to a hidden counterpart) | triadic | triadic, Φ_MIP = 2.000 |

## A4. Results cited in the proposal

**R1. Census of the strict-mediation family** (`python -m org_frontier.corpus.population`). With no worker–counterpart edge, the worker's rule is one of 4 one-input functions of the system, the counterpart's likewise, and the system's rule one of 16 two-input functions of worker and counterpart: 4 × 16 × 4 = 256 forms. Re-run 26 Oct 2026:

| Quantity | Value |
|---|---|
| Forms | 256 |
| Triadic (Φ > 0) | 24 (9.4%) |
| P(triadic \| mediator reads both parties) | 24/160 = 15.0% |
| P(triadic \| mediator does not read both) | 0/96 = 0.0% |

**R2. Time-series proxies** (`python -m org_frontier.proxy_bridge.run`). Eight curated forms (three triadic, five dyadic) × three noise levels (0.05, 0.10, 0.20) × three seeds, trajectories of 8,000 steps. Proxies: ΦID Φ_R with CCS redundancy, and uncorrected whole-minus-sum Φ_WMS. Ground truth: the exact verdict on the deterministic form. Re-run 26 Oct 2026:

| Proxy | Triadic mean | Dyadic mean | Rank-AUC | Best-threshold accuracy |
|---|---|---|---|---|
| Φ_R (CCS) | 0.139 | 0.091 | 0.563 | 0.736 |
| Φ_WMS | 0.122 | 0.043 | 0.629 | 0.778 |

Per form, mean Φ_R: hierarchy with back-channel (dyadic) 0.205; gig false dyad (triadic) 0.206; strict bottleneck (triadic) 0.106; two-sided match (triadic) 0.106; pure relay (dyadic) 0.136. The back-channel creates dependence that the proxy reads as integration.

**R3. Thompson's interdependence types** (`org_frontier/questions/q43_thompson_interdependence/`). Each type was built at n = 3 under one convention.

| Hypothesis | Result |
|---|---|
| H1: under one convention, the verdict does not reproduce pooled < sequential < reciprocal | Confirmed: pooled Φ = 0.0, sequential Φ = 2.0, reciprocal Φ = 2.0; the top step collapses |
| H2: pooled is verdict-ambiguous | Confirmed: dyadic with independent contributions, triadic when one node is jointly determined by all contributors |
| H3: sequential is verdict-ambiguous | Confirmed: triadic with a return edge, dyadic when acyclic |
| H4: reciprocal needs a closed cycle | Confirmed: bidirectional labels without a cycle read dyadic |
| H5: verdict = f(joint determination, feedback cycle) | Refuted: four forms share (True, True), three with identical connectivity matrices, and they split across both verdicts |

## A5. The research loop

| Stage | Artifact | Gate |
|---|---|---|
| 1. Review | `review.md`: the question against prior probes | names the related probes; stops if a prior probe answers the question |
| 2. Literature | `literature/deep_research_report.md`, `references.bib` | sourced references with DOIs; states whether the gap is open |
| 3. Hypotheses | `hypotheses.md`: H1–H5 with nulls and predicted outcomes | committed before any computation |
| 4. Methods | `methods.md`: form, measure, controls and decision rule per hypothesis | a reader can reproduce each test without the code |
| 5. Run | `probe_*.py`, `results/` | an instrument control passes first; refutations are logged as refutations |
| 6. Paper | `paper.md`, `FINDINGS.md` | every number traces to a results file or a logged probe |

The orchestration script (`protocol/question_pipeline.js`) runs the six stages as agent calls with JSON-schema outputs for hypotheses, methods and verdicts. A manual template reproduces each stage by hand. Status on 26 Oct 2026: 170 questions have fixed hypotheses and probes, and 168 have a written paper.

## A6. Reproducibility

- **Environment:** Python 3.12, PyPhi with IIT 4.0 support, phyid for the ΦID proxy, NumPy and pandas. The repository's `requirements.txt` lists the dependencies and pins PyPhi to its `feature/iit-4.0` branch.
- **Regression suite:** `ci/reproduce.json` lists 542 commands with expected output strings. Relevant checks include `instrument-controls` (A3), `q120-higher-order-binding` (24 of 256 strict-mediation forms triadic), `q43-thompson-ordering` and `q43-thompson-sequential` (R3), and `field-mocks` (nine of ten invented field cases matched the reading fixed before computing; ride-hail flips from triadic to dyadic under substitutable drivers). The R1 conditional rates and the R2 proxy statistics come from the module runs above and have no dedicated check yet.
- **Runtime:** the full three-party census runs in about one second on a laptop CPU, and the proxy experiment in about five seconds. Exact computation becomes impractical beyond about ten to twelve nodes.

## References

Albantakis, L., et al. (2023). Integrated information theory (IIT) 4.0: Formulating the properties of phenomenal existence in physical terms. *PLOS Computational Biology*, 19(10), e1011465. https://doi.org/10.1371/journal.pcbi.1011465

Mayner, W. G. P., Marshall, W., Albantakis, L., Findlay, G., Marchman, R., & Tononi, G. (2018). PyPhi: A toolbox for integrated information theory. *PLOS Computational Biology*, 14(7), e1006343. https://doi.org/10.1371/journal.pcbi.1006343
