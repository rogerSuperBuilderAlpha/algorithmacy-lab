# Technical Appendix: An Oracle-Adjudicated Research Loop for Organization Theory

[DRAFTED by Claude, 26 Oct 2026, v2. Anonymous. Companion to the proposal. Part A specifies the loop, Part B the oracle, and Part C the record and the audit. Every count was re-run on 26 Oct 2026 from the anonymized repository.]

## Part A. The loop

### A1. Division of labour

| Role | Who | What it may do | What it may not do |
|---|---|---|---|
| Director | human researcher | chooses questions, reads each stage's output, accepts or rejects results, commissions audits | (no restriction) |
| Generator | AI agents | review, literature search, hypotheses, test design, code, paper | decide whether a hypothesis holds |
| Oracle | deterministic exact computation | return a verdict on a formal model, after reproducing its controls | be influenced by the generator |
| Ledger | append-only file of results | hold every prior result, refutations included | be renumbered or edited |

### A2. Stages and their contracts

The orchestration script (`org_frontier/protocol/question_pipeline.js`) runs each stage as an agent call. Stages 3 to 5 return JSON that must validate against a fixed schema.

| Stage | Input | Output (artifact) | Schema or gate |
|---|---|---|---|
| 1. Review | the question; the ledger (`probes/PROBES.md`); the synthesis of findings | `review.md`: related prior probes, cited by number, and the gap | stops if a prior result answers the question |
| 2. Literature | the question | `literature/deep_research_report.md`, `references.bib` | 15–30 sources with DOIs or arXiv IDs; an explicit open-gap statement |
| 3. Hypotheses | the review and literature | `hypotheses.md` | exactly 5 items, each {name, claim, null, predicted, slug}; committed before any computation |
| 4. Methods | the hypotheses | `methods.md` | exactly 5 items, each {hypothesis, slug, spec}; the spec gives the model or ensemble, the measure, the controls and the decision rule |
| 5. Run (in parallel, one agent per test) | one spec | `probe_<slug>.py`, `results/` | the probe asserts a known control before testing; returns {verdict ∈ {confirmed, partial, refuted}, numbers, probe_file, probes_row} |
| 5b. Log | the five result rows | rows appended to the ledger, continuing the numbering | existing rows are never renumbered |
| 6. Paper | the results | `paper.md`, `FINDINGS.md` | every number traces to `results/` or the ledger; refutations are reported as refutations |

A manual template (`org_frontier/protocol/template/`) reproduces each stage by hand when the automated run fails.

### A3. Regression

The lab's regression suite holds 542 commands with the output each must print. It re-runs the code behind reported numbers and fails on any change. It checks determinism, not correctness: a check passes if the code still prints what it printed before.

## Part B. The oracle

### B1. Encoding

A coordination form with *n* parties is a deterministic Boolean network on *n* nodes. Node *i* holds party *i*'s state, and a rule sets node *i*'s next state from the current state of the network. The strict-mediation triad:

| Party | Rule | Reading |
|---|---|---|
| Worker | W′ = S | acts on the system's signal |
| System | S′ = W AND C | commits only when both parties are in |
| Counterpart | C′ = S | responds to what the system shows |

### B2. Verdict

PyPhi (Mayner et al., 2018) computes IIT-4.0 system integrated information (Albantakis et al., 2023) over the minimum-information partition (MIP), the directional cut that minimises normalised integrated information. The verdict is dyadic when Φ_MIP = 0 and triadic when Φ_MIP > 0. The oracle also returns the *major complex*, the subset of parties bound into the irreducible structure. Only the binary verdict and the complex are read. Φ magnitude depends on the encoding and is treated as ordinal at most.

### B3. Controls (re-run 26 Oct 2026; `python -m org_frontier.classifier.validate`)

| Control or form | Expected | Observed |
|---|---|---|
| Factoring control (counterpart decoupled) | dyadic | dyadic, Φ_MIP = 0.000 |
| Irreducible control (full coupling) | triadic | triadic, Φ_MIP = 0.830 |
| Strict-mediation triad (B1) | triadic | triadic, Φ_MIP = 2.000 |
| Chat dyad; dyadic gig model; tracking form with factoring feedback | dyadic | dyadic, Φ_MIP = 0.000 each |
| Gig "false dyad" (a worker alone with an app, bound to a hidden counterpart) | triadic | triadic, Φ_MIP = 2.000 |

### B4. Two reference results the oracle settles

These results are not the contribution. They show the kind of claim the oracle decides, and why the verdict must be computed rather than read off a diagram.
- **Census** (`python -m org_frontier.corpus.population`). The strict-mediation family has no worker–counterpart edge. Each outer party's rule is one of 4 one-input functions of the system, and the system's rule is one of 16 two-input functions, giving 4 × 16 × 4 = 256 forms. Of these, 24 are triadic. The intuitive rule "the mediator reads both parties" holds for 160 forms, of which 24 are triadic. It fails for the other 96, and none of them is triadic.
- **Proxies** (`python -m org_frontier.proxy_bridge.run`). Two time-series proxies estimated from simulated trajectories, ΦID Φ_R and whole-minus-sum Φ, separate dyadic from triadic forms at rank-AUC 0.563 and 0.629, where 0.5 is chance.

## Part C. The record and the audit

### C1. Worked run: Thompson's interdependence types (`org_frontier/questions/q43_thompson_interdependence/`)

| Hypothesis (fixed before computing) | Verdict |
|---|---|
| H1: under one convention, the oracle does not reproduce pooled < sequential < reciprocal | confirmed: pooled Φ = 0.0, sequential Φ = 2.0, reciprocal Φ = 2.0 |
| H2: pooled is verdict-ambiguous | confirmed: dyadic with independent contributions, triadic when one node is jointly determined by all contributors |
| H3: sequential is verdict-ambiguous | confirmed: triadic with a return edge, dyadic when acyclic |
| H4: reciprocal needs a closed cycle | confirmed: bidirectional labels without a cycle read dyadic |
| H5: verdict = f(joint determination, feedback cycle) | refuted: four forms share (True, True), three of them with identical connectivity matrices, and they split across both verdicts |

### C2. Verdict tally (`python tools/tally_verdicts.py`)

The script reads each question's `FINDINGS.md`, takes each hypothesis's verdict from the findings table (or from an inline H*k* verdict where no table exists), and classifies it. It parses 163 of the 170 question records; the remaining 7 have no machine-readable verdicts.

| | Questions | Hypotheses | Confirmed | Refuted | Partial |
|---|---|---|---|---|---|
| All | 163 | 512 | 399 (77.9%) | 105 (20.5%) | 8 (1.6%) |
| Q1–Q117 (before the audit) | 65 | 275 | | 17.1% | |
| Q118 onward (after the audit) | 98 | 237 | | 24.5% | |

The parse is automated, and checking a random sample by hand is a development-stage task. The before/after difference is descriptive only: the later questions differ in topic and were not randomised.

### C3. The audit (`org_frontier/AUDIT_Q111_Q117.md`)

The adversarial review of Q111–Q117 read the wave through four lenses:
- the method's own assumptions;
- construct and external validity;
- formal and cooperative-game method;
- research process and integrity.

The reviewers re-checked their load-bearing claims against the code and the ledger, and the review corrects its own critics where they overreached. The table lists the failure modes it found and the mechanism the proposal assigns to each.

| Failure mode | Evidence in the wave | Proposed mechanism |
|---|---|---|
| Non-severe testing | 24 of 24 hypotheses confirmed; one hypothesis restated the Shapley efficiency axiom | a vetting agent flags identities; a per-wave severity alarm |
| Leaky pre-commitment | exploratory values computed before the hypotheses were fixed (Q115's sweep; Q117's predicate "found by inspecting the family") | hypotheses sealed to an external timestamp; oracle calls blocked until sealed |
| Self-administered gates | one agent in one session produced the review, hypotheses, code, results and paper | separate vetting and auditing agents; the auditor does not see the predictions |
| Vocabulary drift | Shapley shares of Φ described as "rent", "scarcity" and "value capture"; Φ magnitudes used cardinally | claim tracing: every finding sentence maps to a computed quantity, and unlicensed terms go to the director |
| Determinism mistaken for correctness | regression checks re-print numbers but do not validate what a form models | an independent human re-implementation of a sample (proposal, step 3) |

## Part D. Reproduction

- **Environment:** Python 3.12; PyPhi from its `feature/iit-4.0` branch; phyid; NumPy; pandas (`requirements.txt`).
- **Runtime:** the controls, census, proxy experiment and Thompson probes each finish in seconds on a laptop CPU. Exact Φ becomes impractical beyond about ten nodes.
- **The loop itself** runs today on a commercial model through a workflow runner. The stage prompts and schemas are in the script. The development stage adds an open-weight configuration.

## References

Albantakis, L., et al. (2023). Integrated information theory (IIT) 4.0: Formulating the properties of phenomenal existence in physical terms. *PLOS Computational Biology*, 19(10), e1011465. https://doi.org/10.1371/journal.pcbi.1011465

Mayner, W. G. P., Marshall, W., Albantakis, L., Findlay, G., Marchman, R., & Tononi, G. (2018). PyPhi: A toolbox for integrated information theory. *PLOS Computational Biology*, 14(7), e1006343. https://doi.org/10.1371/journal.pcbi.1006343
