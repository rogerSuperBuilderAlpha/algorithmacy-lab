# Paper pipeline — turning paper-less work into full-package research papers

All 74 `questions/q*` directories already carry a `paper.md`, and the foundations arc is a complete
manuscript (`foundations/paper/manuscript.md`). Several other bodies of work have real, reproducible
exact-Φ results but have **not** been through the full protocol — no Stage-2 deep research, no
pre-registered `hypotheses.md`, no `paper.md`. This document inventories that work, groups it into
six paper-sized categories, and gives each a research plan that produces the full package.

The full package per category means the six stages of `protocol/RESEARCH_PROTOCOL.md`: a cursory
review, a **deep-research literature pass** (the step every item below skipped), five hypotheses
**committed before any new computation**, methods, the runs (mostly already done — but
pre-registration must precede any *new* run), and a `paper.md` + `FINDINGS.md`. Each category lands
as either a `questions/qNN_*` entry or, for the multi-experiment ones, a `studies/*` or `field/*`
entry with a `paper.md`.

## The honest status line

The exact-Φ computations under every category below are real, instrument-validated, and CI-gated.
What they lack is scholarly grounding and pre-registration. In particular, the platform-position and
field categories (E, F) reach organizational claims — disintermediation, lock-in, outside options —
that overlap decades of platform-economics and transaction-cost scholarship the lab has not read. The
deep-research stage is there to find out whether each result is novel, a rediscovery, or wrong. Until
that stage runs, these are exploratory in-silico regularities, not findings.

## Sequencing

| # | Category | Evidence state | Deep-research load | Priority |
|---|----------|----------------|--------------------|----------|
| A | Structural law of core membership | synthesized (`STRUCTURAL_FINDINGS.md`), needs pre-registered re-run | medium (IIT complexes/exclusion) | 1 — foundational, others cite it |
| D | Coordination-logic atlas | complete (`studies/coordination_logic_atlas`) | medium (Boolean-network / canalization) | 2 — evidence done, self-contained |
| F | Structural theory of platform position | complete (two `field/threads`) | heavy (platform economics) | 3 — highest novelty risk |
| E | Field protocol & demonstration | complete (`field/PROTOCOL.md` + mocks) | medium (org methods, modeling) | 4 — methods paper, pairs with F |
| B | Discriminant boundaries vs neighbor constructs | partial (probes 19–23, 31) | heavy (HMC/CMC/AI-MC literatures) | 5 — needs new runs |
| C | Robustness & encoding-dependence | partial (probes 14–18, 27, 32, 34, 38) | light | 6 — may fold into A |

Do A first; it is the result the others lean on. D and F have all their numbers and are the fastest
to paper once the literature is in. B and C need new probes and are lower priority.

---

## Category A — The structural law of core membership

**Working title.** *Two conditions decide the irreducible core: bidirectional coupling and
pivotality in Boolean models of coordination.*

**Question.** Which parties of a coordination form belong to its IIT-4.0 major complex, and what
rule property decides membership?

**Existing evidence.** `STRUCTURAL_FINDINGS.md` (eight findings + the two-condition law); the early
probe loop (probes ~1–43); `q98_pivotality_bidirectionality`, `q74_verdict_vs_complex`,
`q75_spectator_robustness`; the conjunctive law (`probe_conjunctive_law`, Φ = n−1). Synthesized in
`essays/algorithmacy_outreach_paper.md` §"structural law and the eight findings" but never a
protocol paper.

**Stage 2 — deep research.** IIT-4.0 on complexes and the exclusion postulate (Albantakis et al.
2023; Marshall/Mayner on major complex and condensation); the cause-effect-structure literature on
which elements enter a complex; prior formal treatments of "who is essential to an integrated
whole." Goal: place the two-condition account against IIT's own theory of exclusion, and check
whether "bidirectional coupling + pivotality" is implied by, or additional to, existing results.

**Stage 3 — hypotheses to pre-register** (re-run after committing): (H1) a node enters the major
complex only if it both reads and is read by the determination; emit-only and read-only nodes are
excluded. (H2) membership probability rises monotonically with the determination's Boolean
sensitivity to the node (pivotality). (H3) the two conditions are jointly sufficient at the corners
and trade off additively in the interior (q98's refined result). (H4) triadic forms are rare in the
random 3-node population (≈9–10%). (H5) a conjunctive all-required mediator gives Φ = n−1 with the
full party set in the core.

**Stage 4–5 — methods.** Reuse the classifier and `major_complex`; re-run the membership battery and
the conjunctive-law sweep under committed hypotheses; register the headline numbers.

**Stage 6 — paper.** Instrument → the two conditions → the eight findings as evidence → the law they
reduce to → rarity of triadicity → limits. Lands as `questions/` capstone or `studies/core_membership`.

---

## Category D — The coordination-logic atlas

**Working title.** *A coordination-logic atlas: which Boolean determination rules make a coordination
form irreducible.*

**Question.** Across quorum thresholds, four-node topologies, redundancy, inhibition, and
heterogeneity, which determination logics yield a triadic verdict, and what laws govern them?

**Existing evidence.** `studies/coordination_logic_atlas/` — 50 experiments, `hypotheses.md`,
`methods.md`, `FINDINGS.md`, CI-gated (`coordination-logic-atlas`). Headline: a k-of-n quorum
mediator is irreducible only at the extremes (k=1, k=n), dyadic at every interior threshold.

**Stage 2 — deep research.** Boolean-network theory (Kauffman; canalizing functions and criticality);
the threshold/quorum-sensing literature; the IIT work on parity vs monotone gates (the lab's own
q54 plus external). Goal: connect the extremes-only quorum law and the rotation-is-irreducible result
to known Boolean-dynamics structure; check whether the interior-quorum collapse is novel.

**Stage 3 — hypotheses (already stated in the study's `hypotheses.md`; pre-registration is in place
for the existing run).** The paper's job is the literature framing, not new pre-registration — the
study already committed predictions before computing. If new experiments are added (weighted/noisy
quorums), pre-register those.

**Stage 4–6.** Reuse the existing run and CSV; add a literature-framed discussion; write `paper.md`
into the existing study directory. Optional new runs: weighted quorums, larger n, noisy thresholds to
test whether extremes-only survives perturbation.

---

## Category F — A structural theory of platform position

**Working title.** *Bottleneck, enricher, capture, bypassed: a structural theory of when a mediating
platform belongs to a coordination, and the outside-option law.*

**Question.** When is a mediating system part of the irreducible coordination, and what governs the
transition between being indispensable, value-adding, capturing, and bypassed?

**Existing evidence.** `field/threads/THREAD.md` (the trichotomy, disintermediation) and
`THREAD_enricher.md` (capture dominates, enrichment rare/fragile, the outside-option core law),
both CI-gated (`field-mediator-in-core`, `field-enricher-regime`). Core law verified 60/60: a
platform's core is itself plus the parties with no outside option.

**Stage 2 — deep research (heaviest, highest-stakes).** Platform economics and two-sided markets
(Rochet–Tirole, Armstrong); disintermediation and multi-homing; lock-in and switching costs (Farrell
–Klemperer); transaction-cost economics and the make-vs-buy mediator; the bargaining-power /
outside-option literature (Nash bargaining, hold-up). Goal: determine whether the outside-option core
law is a from-scratch rediscovery of standard results, a novel structural restatement, or in tension
with them. This is the category most likely to be already known; the deep-research pass is decisive.

**Stage 3 — hypotheses to pre-register** (re-run after committing): (H1) a mediator is in the major
complex iff the whole out-integrates every party-only coalition. (H2) the in-core regime splits into
bottleneck / enricher / capture by the parties' outside options. (H3) the major complex equals the
mediator plus exactly the parties with no outside option. (H4) genuine enrichment is rare and
perturbs into capture (fragility). (H5) asymmetric outside options produce capture of the dependent
party; symmetric options produce bypass.

**Stage 4–6.** Reuse the two threads' scripts; re-run under committed hypotheses; write a single
`paper.md` (the two threads are one theory). Lands as `field/threads/paper.md` or a `questions/`
entry. Flag the validation gap hard: stipulated models, organizational claims unconfirmed.

---

## Category E — The field protocol and its demonstration

**Working title.** *Reading a real coordination arrangement with exact Φ: a field protocol and ten
worked models.*

**Question.** How does one take a real coordination arrangement to an explicit, falsifiable
dyadic/triadic model, and what does the verdict claim?

**Existing evidence.** `field/PROTOCOL.md` (the nine-step protocol) and `field/` mocks (`FINDINGS.md`,
CI-gated `field-mocks`): a system in the middle is not enough; the verdict turns on the encoding;
read the major complex.

**Stage 2 — deep research.** Organizational research methods (formal modeling in org theory;
computational/agent-based organization studies); construct operationalization and the
internal-vs-external validity literature; prior attempts to apply formal dynamical models to
coordination (organizational ecology, transaction-cost operationalization). Goal: position the
protocol as a methods contribution and borrow established standards for rule elicitation and
inter-rater reliability the protocol currently lacks.

**Stage 3 — hypotheses / claims.** A methods paper carries claims, not five predictions: the protocol
produces falsifiable models; the mock demonstration shows the four judgment points (system-vs-conduit,
substitutability, gate-vs-store, read-the-complex); the sensitivity step is load-bearing. Pre-register
any new mock battery.

**Stage 4–6.** Reuse the mocks; add the literature-grounded methods discussion and an explicit
elicitation procedure as the contribution; write `field/paper.md`. Pairs with Category F (F is the
theory, E is the method).

---

## Category B — Discriminant boundaries vs neighbor constructs

**Working title.** *What algorithmacy is not: structurally distinguishing the mediated triad from
human-machine communication, computer-mediated communication, and AI-mediated communication.*

**Question.** Do the neighbouring constructs (HMC, CMC, AI-MC, sensemaking) produce the same triadic
signature as algorithmacy, or does the verdict separate them?

**Existing evidence.** Probes 19–23, 31 (CMC, AI-MC boundary, contestability, worker competition,
system memory). Paper-less, and the thinnest evidence base — needs new runs.

**Stage 2 — deep research (heavy).** The HMC literature (Guzman, Lewis); CMC theory; AI-mediated
communication (Hancock et al.); sensemaking (Weick). Goal: define each neighbour construct precisely
enough to model it as a Boolean form and state what would distinguish it from algorithmacy.

**Stage 3 — hypotheses.** Pre-register, per construct, whether its canonical form reads dyadic or
triadic and why, before modeling. Likely H: CMC (transparent channel) reads dyadic; AI-MC where the
system commits a determination reads triadic; the distinction is the determination, not the medium.

**Stage 4–6.** This category needs a fresh probe battery (one form per construct, with sensitivity).
Build it, then paper. Lower priority because the evidence does not yet exist.

---

## Category C — Robustness and encoding-dependence of the verdict

**Working title.** *How robust is the dyadic/triadic verdict to modeling choices?*

**Question.** Does the verdict survive changes in encoding, grain, update schedule, and noise?

**Existing evidence.** Probes 14–18, 27, 32, 34, 38; partially covered already by
`q123_reproducibility` and `q124_aggregation_robustness` (which have papers). The paper-less remainder
is the encoding/grain robustness cluster.

**Stage 2 — deep research (light).** Robustness/sensitivity-analysis methodology; the IIT
grain/coarse-graining literature.

**Decision.** Because q123/q124 already paper the reproducibility and aggregation angles, this
category is the most likely to be **folded into Category A** as a robustness section rather than a
standalone paper. Keep it separate only if the encoding/grain probes prove rich enough on their own;
otherwise merge.

---

## Process note

For each category: branch, run the `deep-research` skill on the Stage-2 scope above and commit
`literature/deep_research_report.md` + `references.bib`, **then** commit `hypotheses.md` before any new
computation, then methods, then re-run/extend, then `paper.md` + `FINDINGS.md`, register numbers in
`ci/reproduce.json`, regenerate the README directory, and open a PR. The categories with complete
evidence (A re-run, D, E, F) can reach a paper without new experiments; B needs a new battery first.
