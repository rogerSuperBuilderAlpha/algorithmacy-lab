# algorithmacy-lab

An open computational lab that applies **exact integrated information** (Φ, from IIT 4.0, computed with
[PyPhi](https://github.com/wmayner/pyphi)) to **organizational coordination theory**, and runs an
**AI-assisted research protocol** that takes a question to a finished quantitative paper.

> **New here? Start with [`OVERVIEW.md`](OVERVIEW.md)** — a five-minute, honest review of what the lab
> argues, where it actually stands (including what is recovered from other fields and what is genuinely
> new), and where you could contribute. The directory below is the map; the overview is the orientation.
>
> **Exploring with an AI assistant (Cursor, Claude Code)?** Ask it *"what is this and where do I start?"* —
> it follows [`START_HERE.md`](START_HERE.md), a guided onboarding that gets you to your first computed
> Φ verdict and your own research question in about fifteen minutes.

The thesis it tests: a coordination form is **dyadic** when its cause-effect structure factors into
independent pieces (it demands *literacy*), and **triadic** when the structure stays irreducible across
the worker–system–counterpart partition (it demands *algorithmacy*). On systems small enough to compute
exact Φ, that verdict is exact, not a proxy.

> **Scope, stated up front.** The core results are *in-silico*: exact Φ on small Boolean dynamical models
> of coordination. They are evidence about the models. A validation gap separates them from empirical
> claims about real organizations (cross-model agreement is internal validity, not external validity).
> This is a research program and a proof-of-method, not peer-reviewed findings about real firms. The
> recurrence program has begun reading real coordination data (the empirical ask below has the detail),
> on a methodological side, away from the core thesis.

## The empirical ask — bring the lab real data

Every result here is in-silico or pre-fieldwork, and the validation gap is the program's largest open
need. Closing it is community work: each of the four empirical arms below is waiting on a different kind of
real data, and the highest-value contribution available is to go get one piece of it. Bring it through a
pull request into `contrib` (see [`CONTRIBUTING.md`](CONTRIBUTING.md)); the lab is reproducibility-first
and fixes its claims before computing, so a contributor commits the questions before the data.

- **Field — one real arrangement, modeled to a Φ verdict.** No real worker, platform, or message
  has been measured. The [field protocol](org_frontier/field/PROTOCOL.md) needs one real coordination — a
  team, the system that mediates it, the counterpart — with the determination rules (what each party's
  next action depends on, who reads whom) elicited from interviews, observation, or system documentation,
  and a second coder's agreement on the encoding. That turns a real arrangement into a Boolean model and
  an exact-Φ verdict. This is the deepest gap.
- **Qualitative — one worked study, run as fieldwork.** The studies under
  [`org_frontier/qualitative/`](org_frontier/qualitative/) are designs awaiting data: a neonatal bedside,
  a content-moderation team, a clinical handoff, a brokered market, each read against a named prior. Each
  needs access to the setting and the interviews, observation hours, and documents to read it. Run one,
  hold the prior open, and report where the real setting departs from the catalog's expectation.
- **Recurrence — one recorded series the lab has not touched.** The behavioral instrument has read
  open-source merge graphs ([v8–v10](org_frontier/recurrence/)) and wants more, ideally where the
  determination actor is recorded so both Φ and cross-recurrence can run: a bot-merged project, a dispatch
  or handoff log with a named gatekeeper, or a physiological series such as the infant vitals the neonatal
  study describes.
- **Survey — field the instrument with a real cohort.** The
  [survey arm](org_frontier/survey/) measures the competence directly: self-report from people inside a
  real coordination arrangement, on a fixed schedule, the questions committed before the answers. The
  pre-registered panel needs a cohort and the access to run it; any workforce coordinating through a
  system beyond its control is a candidate.

Each ask now has a ready-to-run **handoff packet** — a front-door README, the pre-registration discipline,
and a runnable scaffold that takes a real input to a verdict. The five are indexed in
[`org_frontier/HANDOFF_PACKETS.md`](org_frontier/HANDOFF_PACKETS.md). Each program README carries the
specifics, and the [overview](OVERVIEW.md) lists the open contributions in order of value. Dig as deep as
you like from there.

## The programs

The lab runs a computational program and five arms that carry it onto real coordination and into cognitive
theory. Each is a different lens on the same coordination arrangement.

- **The computational program** in [`org_frontier/`](org_frontier/) computes exact Φ on Boolean
  models through a fixed six-stage protocol — review → deep research → five hypotheses fixed before
  computing → methods → run against the exact-Φ instrument → paper. Its corpus of threads, studies,
  and questions stands as a catalog of pre-disclosed priors: the structural reading of what a
  coordination form is.
- **The field program** in [`org_frontier/field/`](org_frontier/field/) takes one real coordination
  arrangement through a nine-step protocol to a dyadic or triadic verdict on an explicit model of it. It is
  the bridge from the in-silico priors to a real case, where the determination rules are elicited from
  interviews, observation, and documents.
- **The qualitative program** in [`org_frontier/qualitative/`](org_frontier/qualitative/) reads real
  coordination settings against those priors, on the questions of process and meaning that fieldwork
  answers and a model cannot. It holds each prior open, and builds its contribution where a real
  setting departs from the catalog's expectation.
- **The recurrence program** in [`org_frontier/recurrence/`](org_frontier/recurrence/) pairs Φ with
  cross-recurrence quantification, the behavioral reading of how the parties' states track each other
  over time. Φ says whether a coordination is irreducible; cross-recurrence says how its signal
  moves, and which party leads.
- **The survey program** in [`org_frontier/survey/`](org_frontier/survey/) measures the competence in
  people: a human-subjects arm that reads algorithmacy as a lived skill through self-report from workers
  inside a real coordination arrangement, the measurement side of the validation gap the structural arms
  cannot reach.
- **The cognition program** in [`org_frontier/cognition/`](org_frontier/cognition/) is the formal bridge to
  the cognitive theories of coordination. Each theory of mind models a channel between two parties and has
  nowhere to put an opaque, interested third; the major complex holds that third as a member of the
  irreducible core, and each failure point becomes a computable Φ prediction.

Four readings meet on one arrangement: structure, fieldwork, behavior, and measurement. The field protocol
turns real evidence into the structural reading, and the cognition program ties that structure back to the
theories of mind it answers. Φ is the structural instrument the field, qualitative, and recurrence arms are
built around, and the survey arm measures the competence the structure is meant to demand. The
measure-validation arc in [`foundations/`](foundations/) established exact Φ first. The directory below is a
live map of the lab, regenerated from the content on every merge, so it is always current.

<!-- BEGIN GENERATED DIRECTORY (tools/build_index.py) -->
## Directory

*A map of the lab, regenerated by `tools/build_index.py`. Do not edit this section by hand — edits are overwritten on the next build.*

### Reviews & articles

Cross-program essays and reviews — the best places to start window-shopping.

- [Reading coordination with a consciousness measure: a structural law for agent-mediated outreach](org_frontier/essays/algorithmacy_outreach_paper.md)
- [Committee panel review — "Committed determination: one axis across six exact-Φ studies"](org_frontier/essays/committed_determination_committee_review.md)
- [Committed determination: one axis across six exact-Φ studies of Boolean coordination models](org_frontier/essays/committed_determination_synthesis.md)
- [Committee panel review — "Integrated information as a cooperative game"](org_frontier/essays/cooperative_game_committee_review.md)
- [The seam carries what the scalar drops: a review of the floor-to-seam program (Q45–Q62)](org_frontier/essays/floor_to_seam_review.md)
- [What integrated information adds to the theories of coordinating minds](org_frontier/essays/integrated_information_and_coordinating_minds.md)
- [Literacy or Algorithmacy? Borrowing a Consciousness Measure to Read an Org Chart](org_frontier/essays/literacy_or_algorithmacy.md)
- [Market structure, regulation, and time in interested mediation](org_frontier/essays/market_structure_of_interested_mediation.md)
- [Mediated, or Irreducible? When the Third Party Is Constitutive and When It Is a Conduit](org_frontier/essays/mediated_or_irreducible.md)
- [Integrated information as a cooperative game](org_frontier/essays/phi_as_a_cooperative_game.md)
- [The political economy of interested mediation: when the platform's rent survives its self-interest](org_frontier/essays/political_economy_of_interested_mediation.md)
- [What Exact Φ Can Do for Organization Theory: A Complete Experiment Catalog](org_frontier/essays/pyphi_org_theory_catalog.md)
- [How this lab studies algorithmacy](org_frontier/essays/studying_algorithmacy.md)
- [The interested third party: how a self-interested mediator changes the irreducibility of coordination](org_frontier/essays/the_interested_third_party.md)
- [The Boolean corpus is a pre-disclosed prior catalog](org_frontier/essays/the_prior_catalog.md)
- [What the six research lines found](org_frontier/essays/what_the_six_lines_found.md)

### Programs, syntheses & the open agenda

- [Research program v7 — the qualitative and recurrence wave](org_frontier/RESEARCH_PROGRAM_V7.md) — the current research program
- [Research narrative: how the program has progressed, and a path forward](org_frontier/RESEARCH_NARRATIVE.md) — the narrative arc across questions
- [Structural findings: what makes a coordination form irreducible](org_frontier/STRUCTURAL_FINDINGS.md) — the standing structural findings
- [Critical review: the political-economy and structural-law waves (Q111–Q117)](org_frontier/CRITICAL_REVIEW_Q111_Q117.md) — a critical self-review
- [Paper pipeline — turning paper-less work into full-package research papers](org_frontier/PAPER_PIPELINE.md) — the plan to turn paper-less work into full papers
- [50 new research questions (v2 agenda)](org_frontier/RESEARCH_AGENDA_50_V2.md) — the open agenda — questions waiting for a contributor

### Handoff packets — pick one up and run it

The five empirical and bridge arms, each packaged so a researcher can take a real input to a verdict: a front-door README, the pre-registration discipline, and a runnable scaffold.

- **[Handoff packets — pick one up and run it](org_frontier/HANDOFF_PACKETS.md)** — The lab's empirical and bridge arms are each packaged so a researcher can pick one up and take it from a
  - [Survey](org_frontier/survey/cohort_algorithmacy/README.md) · [Field](org_frontier/field/packets/gig_dispatch/README.md) · [Recurrence](org_frontier/recurrence/packets/template/README.md) · [Cognition](org_frontier/cognition/packets/template/README.md) · [Qualitative](org_frontier/qualitative/template/README.md)

### Research monitoring — a standing literature watch

A live bibliography and review for each program, decomposed into ten topics and refreshed daily so new work is caught as it appears.

- **[Research monitoring — a standing literature watch for each program](org_frontier/research/README.md)** — A live bibliography and literature review for each of the lab's six programs, refreshed daily so new work is
  - [Master index](org_frontier/research/INDEX.md) · [Changelog](org_frontier/research/CHANGELOG.md) · [Daily playbook](org_frontier/research/DAILY_REFRESH.md)
  - programs: [computational](org_frontier/research/computational/README.md) · [field](org_frontier/research/field/README.md) · [qualitative](org_frontier/research/qualitative/README.md) · [recurrence](org_frontier/research/recurrence/README.md) · [survey](org_frontier/research/survey/README.md) · [cognition](org_frontier/research/cognition/README.md)

### Field — reading real organizations

Bridging the in-silico work to real coordination arrangements: a field protocol and a worked demonstration.

- **[Field — reading real organizations with exact Φ](org_frontier/field/README.md)** — The lab's verdicts are in-silico: exact Φ on small Boolean models, evidence about the models, with a
  - [Protocol](org_frontier/field/PROTOCOL.md) · [Findings](org_frontier/field/FINDINGS.md)

### Qualitative research

The empirical arm: reading real coordination against the pre-disclosed priors, with methods and an open topic agenda for qualitative contributors.

- **[Qualitative research — reading real coordination against the priors](org_frontier/qualitative/README.md)** — The lab's in-silico work builds a catalog of priors: Boolean coordination forms carried to an exact Φ
  - [Methods](org_frontier/qualitative/METHODS.md) · [Topics](org_frontier/qualitative/TOPICS.md) · [Publishing](org_frontier/qualitative/PUBLISHING.md)
- [Whose Reach Is It: When a Worker Goes to Market Through an Agent, Who Becomes the Central Party](org_frontier/qualitative/broker_delegation/STUDY.md) — A worker who reaches a market through an agent hands the work of dealing to a party who stands between the worker and the platform
- [The Record as a Third Party: How Clinicians Coordinate Care Across the Shift Boundary Through a Handoff Tool](org_frontier/qualitative/clinical_handoff/STUDY.md) — Care continuity at shift change runs through a record. An outgoing clinician writes the patient into a handoff tool, an incoming clinician reads it, and the care…
- [Who Holds the Decision: How a Poster, an Automated Moderator, and a Trust-and-Safety Team Settle a Takedown](org_frontier/qualitative/moderation_memory/STUDY.md) — A takedown decision is settled by three parties: a poster who writes, an automated system that flags and acts, and a policy team that sets the rules and hears…
- [The Third in the Room: How Neonatal Nurses Coordinate Care Between Parents and an Infant Who Cannot](org_frontier/qualitative/neonatal_third/STUDY.md) — Coordination is increasingly accomplished through a third party that stands between two others, and the case that most demands explanation, coordination through an…
- [Who Decides the Manuscript: How Authors, Editors, and Reviewers Locate the Editorial Verdict](org_frontier/qualitative/peer_review_gate/STUDY.md) — An editorial decision on a manuscript passes through three parties and a software system: an author who submits, reviewers who advise, and an editor who decides…
- [Watching the Queue: Whether a Triage Supervisor Is a Member of Service Coordination or Only Its Spectator](org_frontier/qualitative/triage_spectator/STUDY.md) — Customer-service triage routes a contact through an automated classifier to a human agent, with a supervisor watching the queue from a dashboard

### Survey — measuring algorithmacy in real workers

The first human-subjects arm: self-report from people inside a real coordination arrangement, with the instrument and hypotheses committed before the data.

- **[Survey — measuring algorithmacy in real workers](org_frontier/survey/README.md)** — The lab's instrument is exact and its results reproduce, and every one of them is in-silico. No real
- [Learning to Read the Machine: A Three-Wave Panel of Algorithmacy in a Developer Cohort](org_frontier/survey/cohort_algorithmacy/STUDY.md) — A three-wave panel of a sixteen-week developer cohort that coordinates through platforms it builds and a peer-review gate, developing a scale for algorithmacy as a…

### Recurrence — coordination read off behavior

Pairing exact Φ with cross-recurrence quantification: the structural measure on the model and the behavioral measure on a run of it.

- **[Recurrence — reading coordination off behavior, paired with Φ](org_frontier/recurrence/README.md)** — A coordination arrangement can be read two ways. Its structure says whether the parties form a
  - [Concepts](org_frontier/recurrence/CONCEPTS.md) · [Bridge](org_frontier/recurrence/FINDINGS.md) · [Sweep](org_frontier/recurrence/SWEEP.md) · [Φ experiments](org_frontier/recurrence/IIT_EXPERIMENTS.md) · [CRQA experiments](org_frontier/recurrence/CRQA_EXPERIMENTS.md) · [Four-party](org_frontier/recurrence/BRIDGE_FOUR.md)

### Cognition — the formal bridge to cognitive science

Where the formal apparatus meets the cognitive theories of coordination: the third party that two-party theories cannot represent, held as a member of the irreducible core.

- **[Cognition — the formal bridge to the cognitive theories of coordination](org_frontier/cognition/README.md)** — A coordination through an opaque, interested third party is something the standard theories of mind
  - [Paper](org_frontier/cognition/coordinating_through_the_opaque_third.md) · [Findings](org_frontier/cognition/FINDINGS.md) · [Theory batteries](org_frontier/cognition/THEORIES.md) · [Predictive processing](org_frontier/cognition/PREDICTIVE_PROCESSING.md) · [Survey bridge](org_frontier/cognition/survey_bridge.md)

### Threads

Deep single-question dives, each driven by its own results.

- [Thread — the back-edge commits; forward-only mediators convey](org_frontier/threads/back_edge/THREAD.md) — The designed-mediator thread wired one architecture, a bidirectional star where the mediator reads the outer
- [The behavioral discriminant: can cross-recurrence tell a committing mediator from a conveying one](org_frontier/threads/behavioral_discriminant/THREAD.md) — The third deep dive from the [mediated-or-irreducible paper](../../essays/mediated_or_irreducible.md),
- [Thread — co-bottlenecks share equally only when interchangeable](org_frontier/threads/bottleneck_symmetry/THREAD.md) — The joint-bottleneck thread reported that the two members of a veto pair share the credit roughly evenly, a
- [Thread — the named coordination forms, read through the cooperative game](org_frontier/threads/canonical_reference/THREAD.md) — A reference for the catalog. The catalog's priors are drawn from random forms; this thread grounds them in
- [Thread — the major complex as a coalition structure](org_frontier/threads/coalition_structure/THREAD.md) — The Shapley thread closed on a residual it called structural. Major-complex membership tracks the exact
- [Thread — a genuine substitute loosens a platform's hold](org_frontier/threads/competing_platforms/THREAD.md) — A prior for the catalog. Two platforms connect the same two parties. When the platforms are identical, a
- [Thread — conflict integrates like cooperation; only disengagement breaks it](org_frontier/threads/conflict/THREAD.md) — A prior for the catalog. Does it matter whether the two parties agree or conflict in how they respond to the
- [Core membership: who is in the irreducible whole, and who drops out](org_frontier/threads/core_membership/THREAD.md) — The fourth deep dive from the [mediated-or-irreducible paper](../../essays/mediated_or_irreducible.md),
- [Thread — the integration credit has no stable split](org_frontier/threads/core_stability/THREAD.md) — The subadditivity thread showed φ_s does not aggregate: a tight pair often out-values the whole that
- [Thread — a coordination needs a threshold of coupling, and commits more readily as it densifies](org_frontier/threads/coupling_density/THREAD.md) — A prior for the catalog. The cyclic thread found a sparse coordination has no bottleneck and a dense one
- [Thread — the mediator takes the credit, the excluded party owes it](org_frontier/threads/credit_concentration/THREAD.md) — The veto thread showed the mediator carries the largest Shapley value. This thread measures how much
- [Thread — cyclic coordination has no bottleneck and shares the credit](org_frontier/threads/cyclic/THREAD.md) — A prior for the catalog. The engagement thread found that closing a feedback cycle raises commitment. This
- [Thread — degree predicts the bottleneck but does not determine it](org_frontier/threads/degree_bottleneck/THREAD.md) — A prior for the catalog. Is a coordination's bottleneck simply the most-connected party? Almost, and not
- [Thread — delegation moves standing from the worker to its agent](org_frontier/threads/delegation/THREAD.md) — A prior for the catalog. A worker reaches the platform through an agent, a chain of worker, agent, platform
- [Thread — a designed mediator: position is wired, power is earned](org_frontier/threads/designed_mediator/THREAD.md) — The committee that reviewed the cooperative-game synthesis pressed one objection hardest. Every form in the
- [Thread — disintermediation needs a symmetric channel; a one-way channel entrenches the mediator](org_frontier/threads/disintermediation/THREAD.md) — A prior for the catalog. The designed-mediator and back-edge threads built a mediator and asked what makes it
- [Thread — a party is bound by coupling, not by heeding the mediator](org_frontier/threads/engagement/THREAD.md) — A prior for the catalog. The back-edge thread asked what makes a mediator commit and answered the return
- [Thread — the irreducible moments are engagement-blind](org_frontier/threads/engagement_blind/THREAD.md) — A prior for the catalog, extending the momentary thread. A triad is irreducible at only a minority of its
- [Thread — the cooperative-game laws at four parties](org_frontier/threads/four_party/THREAD.md) — Seven threads read integrated information as a cooperative game, and all of them ran on three-party forms
- [Thread — fragility tracks coordination logic: monotone has one point of failure, parity has three](org_frontier/threads/fragility/THREAD.md) — A prior for the catalog. The gate-logic thread found that a parity mediator binds all three parties equally
- [Thread — a parity mediator binds twice as readily and shares the credit](org_frontier/threads/gate_logic/THREAD.md) — A prior for the catalog. The cyclic thread found that topology decides whether a coordination has a
- [Thread — commitment scales with the mediator's information throughput](org_frontier/threads/gate_sensitivity/THREAD.md) — A prior for the catalog. The gate-logic thread found a parity mediator binds more readily than a monotone
- [Thread — the architecture of scale: twenty questions on coordination beyond one mediator](org_frontier/threads/hierarchy/THREAD.md) — A deep line for the catalog. The scale thread found one mediator cannot bind a large coordination, and the
- [Thread — influence is universal and does not determine membership](org_frontier/threads/influence_membership/THREAD.md) — A prior for the catalog. A party can shape what the others do without being part of the coordination's
- [Thread — only reciprocal interdependence binds; pooled and sequential carry no integration](org_frontier/threads/interdependence/THREAD.md) — A prior for the catalog. Thompson's typology of interdependence — pooled, sequential, reciprocal — read
- [Thread — inside a joint bottleneck the credit is shared](org_frontier/threads/joint_bottleneck/THREAD.md) — The four-party thread found a structure three parties cannot show: a bottleneck that is a set of parties,
- [Distance to the dyad: the Φ margin as a continuous measure of mediation](org_frontier/threads/margin_to_dyad/THREAD.md) — The second deep dive from the [mediated-or-irreducible paper](../../essays/mediated_or_irreducible.md),
- [The mediation boundary: when a committing mediator binds, and the co-monotonicity law](org_frontier/threads/mediation_boundary/THREAD.md) — A deep dive into the structure of the irreducibility boundary, derived from the
- [Thread — a mediator that remembers takes more of the credit](org_frontier/threads/memory/THREAD.md) — A prior for the catalog. The gate-logic thread varied what the mediator computes. This one varies whether it
- [Thread — coordination is momentary: a triad is irreducible at a minority of its states](org_frontier/threads/momentary/THREAD.md) — A prior for the catalog, and the one that qualifies the rest. Being a triadic coordination does not mean
- [Thread — a mediated triad degrades gracefully under noise, and parity degrades slower](org_frontier/threads/noise/THREAD.md) — A prior for the catalog. Real coordination is noisy. This thread perturbs a mediated triad — each node's
- [Thread — normalizing Φ collapses the core to one party](org_frontier/threads/normalization/THREAD.md) — A standing objection to integrated information is that Φ rises with system size, so it should be normalized
- [Thread — an observer is never in the core; a member must act, not only watch](org_frontier/threads/observer/THREAD.md) — A prior for the catalog. A coordination often has an audience — a party that watches but is not watched,
- [Thread — oversight joins the top; it does not break the bottleneck or reach the parties](org_frontier/threads/oversight/THREAD.md) — A prior for the catalog. Place a principal over the mediator — a regulator, an owner, a board — coupled to
- [Thread — integration is quantized: triads land on a short ladder of Phi values](org_frontier/threads/phi_ladder/THREAD.md) — A prior for the catalog. Integration does not take a continuum of values. Across random three-party
- [Thread — memory pays at the center, not at the periphery](org_frontier/threads/position_of_memory/THREAD.md) — A prior for the catalog. The memory thread found that a self-loop on the mediator raised its share of the
- [Thread — a quorum coordination binds only at the extremes, never at a majority](org_frontier/threads/quorum/THREAD.md) — A prior for the catalog. A quorum mediator fires when at least k of its parties are active. This thread asks
- [Thread — one mediator has a size limit: commitment collapses as the coordination grows](org_frontier/threads/scale/THREAD.md) — A prior for the catalog. How large a coordination can a single mediator hold together? Not large. A
- [Thread — does major-complex membership track Shapley pivotality?](org_frontier/threads/shapley_membership/THREAD.md) — A deep dive into the program's one genuinely novel claim, and the one the committee pressed hardest
- [Thread — the empty core is a property of the random sample, not of coordination](org_frontier/threads/structured_forms/THREAD.md) — The committee that reviewed the cooperative-game synthesis pressed one objection above the rest. Every
- [Thread — integration does not aggregate](org_frontier/threads/subadditivity/THREAD.md) — "The whole is more than the sum of its parts" is the slogan integrated information is supposed to make
- [Thread — substitutability is the enemy of integration: a pool never binds, a team binds both](org_frontier/threads/substitutability/THREAD.md) — A prior for the catalog. A platform connects two workers to a counterpart. Whether the workers are a team or
- [Thread — topology sets the credit distribution at four parties too](org_frontier/threads/topology_four/THREAD.md) — A prior for the catalog. The cyclic thread found, at three parties, that a symmetric ring shares the credit
- [Thread — a second hub beats the size limit one mediator hits](org_frontier/threads/two_hubs/THREAD.md) — A prior for the catalog, and the opening of the scale-and-hierarchy line. The scale thread found a single hub
- [Thread — the mediator is a veto player](org_frontier/threads/veto_player/THREAD.md) — The Shapley thread showed the mediator carries the largest Shapley value over the game v(S) = φ_s(S) and

### Studies

Multi-experiment batteries on one theme.

- **[Coordination-logic atlas](org_frontier/studies/coordination_logic_atlas/README.md)** — Fifty coordination forms, classified by exact IIT-4.0 Φ. Thirty-six verdicts matched the
- **[The core-membership law](org_frontier/studies/core_membership_law/README.md)** — A pre-registered confirmatory run of the two-condition account of major-complex membership. The
- **[Discriminant boundaries — what algorithmacy is not](org_frontier/studies/discriminant_boundaries/README.md)** — A pre-registered discriminant battery: faithful Boolean models of algorithmacy's neighbour constructs,

### Foundations — what tracks Φ

The measure-validation arc that established exact Φ as the instrument.

- [`candidate_audit`](foundations/candidate_audit) — which candidate Φ measures track exact IIT‑4.0 Φ?
- [`cbh_complexity`](foundations/cbh_complexity) — the entropy–content conundrum is resolvable on exactly-computable systems
- [`consciousness_range`](foundations/consciousness_range) — a "level of consciousness" radically underdetermines the mind
- [`emergence_vs_phi`](foundations/emergence_vs_phi) — causal emergence and IIT Φ are nearly orthogonal
- [`learned_surrogate`](foundations/learned_surrogate) — combining cheap features predicts Φ far better than any single one
- [`phiid_vs_phi`](foundations/phiid_vs_phi) — estimating Φ from data (via ΦID) roughly halves how well it tracks exact Φ
- [`proxy_audit`](foundations/proxy_audit) — cheap proxies do not track exact IIT‑4.0 Φ
- [`psi_vs_phi`](foundations/psi_vs_phi) — maximum-caliber information ψ does not track exact IIT-4.0 Φ
- [`structure_suite`](foundations/structure_suite) — scalar Φ is nearly orthogonal to the structure it summarizes

### Questions — the logbook (154)

Each question fixes five hypotheses, runs them against the exact-Φ instrument, and writes a paper. The full per-probe log is [`org_frontier/probes/PROBES.md`](org_frontier/probes/PROBES.md).

<details>
<summary>Browse all 154 questions</summary>

| # | Question | Finding |
|---|----------|---------|
| [Q6](org_frontier/questions/q6_noise_phase_transition/paper.md) | Commit noise on a mediated triad: smooth Φ decay with a step verdict, no interior critical point | Commit noise: phase transition or smooth decay? |
| [Q7](org_frontier/questions/q7_party_vs_mediator_noise/paper.md) | Party noise versus mediator noise: which seat carries the flip changes the Φ curve | party noise vs mediator noise findings |
| [Q8](org_frontier/questions/q8_parity_vs_conjunctive_noise/paper.md) | Parity hub versus conjunctive hub under flip-noise | parity hub vs conjunctive hub under flip-noise findings |
| [Q9](org_frontier/questions/q9_timescale_separation/paper.md) | A slow mediator over fast parties flips the coordination verdict | Timescale separation: findings |
| [Q10](org_frontier/questions/q10_commit_delay/paper.md) | Commit-response delay: graded Φ, stable verdict | commit→response transport delay findings |
| [Q11](org_frontier/questions/q11_oscillatory_scaling/paper.md) | Oscillatory coordination forms: a constant ring law, a period term, no triadic guarantee | oscillatory Φ scaling law findings |
| [Q43](org_frontier/questions/q43_thompson_interdependence/paper.md) | Thompson's interdependence types against the dyadic/triadic verdict | Thompson's interdependence types (pooled, sequential, reciprocal) against the IIT-4.0 dyadic/triadic verdict. Matched triple at n=3, AND family |
| [Q45](org_frontier/questions/q45_edge_floor_uniqueness/paper.md) | Conjunctive uniqueness at the edge floor |  |
| [Q49](org_frontier/questions/q49_mip_seam_mincut/paper.md) | The weakest seam is a tie |  |
| [Q50](org_frontier/questions/q50_or_triadic_seam/paper.md) | Party-read structure for OR triadic binding at the edge floor |  |
| [Q51](org_frontier/questions/q51_implication_backchannel/paper.md) | implication back-channel |  |
| [Q52](org_frontier/questions/q52_phi_ladder_mechanism/paper.md) | phi-ladder mechanism |  |
| [Q53](org_frontier/questions/q53_impl_phi_ceiling/paper.md) | implication Phi ceiling |  |
| [Q54](org_frontier/questions/q54_xor_parity_mechanism/paper.md) | XOR parity back-channel mechanism |  |
| [Q55](org_frontier/questions/q55_bijective_discriminator/paper.md) | bijective parity below-vs-ceiling discriminator |  |
| [Q56](org_frontier/questions/q56_symmetric_complete_mip/paper.md) | symmetric complete MIP geometry |  |
| [Q57](org_frontier/questions/q57_channel_direction_mip/paper.md) | channel direction MIP seam |  |
| [Q58](org_frontier/questions/q58_normalization_cut_geometry/paper.md) | normalization cut geometry | Q57 #187 documented the fixed two-to-one normalized_phi ratio without identifying the normalization |
| [Q59](org_frontier/questions/q59_directed_cut_edges/paper.md) | directed cut edges | Q58 #190 counted severed connections without naming directed edges. The back-channel cross-edge appears in |
| [Q60](org_frontier/questions/q60_thompson_backchannel/paper.md) | Thompson back-channel typing | Thompson sequential/reciprocal interdependence against the Q59 back-channel mediator-severance templates |
| [Q61](org_frontier/questions/q61_seam_return_typing/paper.md) | MIP seam vs return-path typing | Official MIP singleton seam against Q43 return-path sequential/reciprocal typing on the back-channel panel |
| [Q62](org_frontier/questions/q62_excluded_cut_signal/paper.md) | Excluded outer cut signal | Excluded outer singleton cut against Q43 return-path typing on the back-channel panel after Q61 established |
| [Q63](org_frontier/questions/q63_outreach_coordination/paper.md) | Is agent-mediated outreach triadic? An exact-Φ reading of the sender–agent–recipient form | outreach as a coordination form |
| [Q64](org_frontier/questions/q64_outreach_breadth_scaling/paper.md) | Outreach breadth scaling: an all-binding campaign stays triadic at Φ = n−1 | outreach breadth scaling |
| [Q65](org_frontier/questions/q65_agent_chain_outreach/paper.md) | Agent-to-agent outreach: depth preserves the triad, but localises the core to an end pair | agent-to-agent outreach (depth) |
| [Q66](org_frontier/questions/q66_chain_core_boundary/paper.md) | The core of an agent chain is a symmetric end pair; closing the loop binds the whole | where the core sits in an agent chain |
| [Q67](org_frontier/questions/q67_reciprocity_gradient/paper.md) | The reciprocity gradient: partial feedback seeds a core, full coupling binds the exchange | the reciprocity gradient |
| [Q68](org_frontier/questions/q68_triage_gating/paper.md) | A recipient-side triage agent joins the coordination only when bidirectionally coupled, and displaces the sender | a recipient-side triage agent |
| [Q69](org_frontier/questions/q69_two_sided_agents/paper.md) | When both sides delegate, the irreducible coordination is the two agents | the two-sided agent exchange |
| [Q70](org_frontier/questions/q70_agent_substitutability/paper.md) | Multi-homing across interchangeable agents collapses the coordination | agent substitutability |
| [Q71](org_frontier/questions/q71_noise_robustness/paper.md) | The outreach verdict is robust to noise: it degrades gracefully and never manufactures a triad | noise robustness of the outreach verdict |
| [Q72](org_frontier/questions/q72_cost_proxy_frontier/paper.md) | The cost/proxy frontier: cheap structural proxies cannot recover the outreach verdict | the cost/proxy frontier |
| [Q73](org_frontier/questions/q73_outreach_law/paper.md) | The outreach-coordination law: when agent-mediated outreach demands algorithmacy | the outreach-coordination law |
| [Q74](org_frontier/questions/q74_verdict_vs_complex/paper.md) | Whole-system verdict versus the maximal complex: a rule for which to report | whole-system verdict versus the maximal complex |
| [Q75](org_frontier/questions/q75_spectator_robustness/paper.md) | Spectator robustness: the triadic core is stable under added non-participating parties | spectator robustness of the core |
| [Q79](org_frontier/questions/q79_stochastic_threshold/paper.md) | Stochastic emergence: the triad accumulates with the probability of reading the recipient | stochastic emergence of the triad |
| [Q80](org_frontier/questions/q80_async_update/paper.md) | Asynchronous update: the verdict survives, the magnitude falls | asynchronous update |
| [Q81](org_frontier/questions/q81_learned_surrogate/paper.md) | A learned surrogate for the outreach verdict, and the size ceiling | a learned surrogate recovers the verdict in-distribution, and fails to cross sizes |
| [Q82](org_frontier/questions/q82_surrogate_vs_proxy/paper.md) | The learned surrogate against the proxies that failed | the surrogate beats every single proxy, and one structural proxy is stronger than expected |
| [Q83](org_frontier/questions/q83_agent_coalition/paper.md) | A recipient-side gating coalition keeps a size-three core; only one of two required agents enters | a recipient-side gating coalition |
| [Q84](org_frontier/questions/q84_adversarial_agent/paper.md) | Influence requires membership: an agent outside the core cannot flip the verdict | influence versus membership |
| [Q85](org_frontier/questions/q85_agent_market/paper.md) | A market of interchangeable agents is a broadcast: interchangeability collapses outreach at every size | a market of interchangeable agents |
| [Q89](org_frontier/questions/q89_heterogeneous_market/paper.md) | Which heterogeneous agents enter the core of a market? | heterogeneous membership is a property of the joint determination, not the agent |
| [Q90](org_frontier/questions/q90_membership_law_scaling/paper.md) | Does the core-membership law generalize past three nodes? | the membership law generalizes in kind, at moderate strength |
| [Q91](org_frontier/questions/q91_lossy_channel/paper.md) | A lossy read degrades the triad gracefully | the triad degrades gracefully under a lossy read |
| [Q92](org_frontier/questions/q92_stateful_mediator/paper.md) | Does a mediator's memory substitute for a live read? | a tracking memory substitutes for a live read, and reorganizes the core |
| [Q93](org_frontier/questions/q93_fragility_margin/paper.md) | A margin-to-dyadic metric, and two notions of robustness that diverge | two notions of robustness come apart |
| [Q94](org_frontier/questions/q94_multiple_complexes/paper.md) | Multiple coexisting complexes, and why coupling does not fuse them | coordination holds multiple cores, and coupling does not fuse them |
| [Q95](org_frontier/questions/q95_composition_of_triads/paper.md) | Composing two triads: fragmentation, not unification | composing two triads fragments rather than unifies |
| [Q96](org_frontier/questions/q96_contingent_membership/paper.md) | State-contingent participation: a factored whole with a local core | contingent participation factors the whole, but keeps a local core |
| [Q97](org_frontier/questions/q97_coordinated_adversary/paper.md) | The coordinated adversary: no influence without membership, but a mediator capture | a coalition gains no influence without membership, but can capture the mediator |
| [Q98](org_frontier/questions/q98_pivotality_bidirectionality/paper.md) | Reading and influence: a hard gate at the corners, a soft one inside | the membership gate is hard at the corners, soft inside |
| [Q99](org_frontier/questions/q99_binding_distinction/paper.md) | The cause-effect structure of a triad: a joint mechanism, and a taxonomy of binders | the integration lives in a joint mechanism, but the binder is not always one party |
| [Q100](org_frontier/questions/q100_structure_fingerprint/paper.md) | The cause-effect structure fingerprints the kind, and is orthogonal to the verdict | the structure fingerprints the kind, and its richness is not the scalar |
| [Q101](org_frontier/questions/q101_what_it_distinguishes/paper.md) | What a coordination distinguishes: the joint-success state | coordination distinguishes the all-present, determination-firing state |
| [Q102](org_frontier/questions/q102_relation_skeleton/paper.md) | The relation skeleton: a hub in mediated coordination, a spread in symmetric | mediated coordination relates through a hub; the breadth count is combinatorial |
| [Q103](org_frontier/questions/q103_structure_under_operations/paper.md) | The cause-effect structure under the operations | the whole-system structure collapses under substitution but diverges from membership |
| [Q104](org_frontier/questions/q104_load_bearing/paper.md) | The load-bearing distinction: where the integration sits and what it hangs on | the integration concentrates in the binding distinction, and every edge bears load |
| [Q105](org_frontier/questions/q105_construction_distance/paper.md) | Construction distance: building a triad is restoring liveness at a party | the boundary is thin from the build side, and triads are built at the parties, not the mediator |
| [Q106](org_frontier/questions/q106_design_operations/paper.md) | The design operations: the law's conditions as reversible levers | the design vocabulary is the law's three conditions, read as moves |
| [Q107](org_frontier/questions/q107_repair/paper.md) | Repair is lever-specific: no routing around the damage | repair is lever-specific: the broken condition must be the one restored |
| [Q108](org_frontier/questions/q108_controllability/paper.md) | Controllability: the hub steers robustly, the spokes on a knife-edge | every party is a control node, but the mediator is dominant and the parties are knife-edge |
| [Q110](org_frontier/questions/q110_reversibility/paper.md) | Reversibility: the boundary is cheap toward the dyad, dear toward the triad | the dyad/triad boundary is asymmetric: easy to break, harder to build |
| [Q111](org_frontier/questions/q111_shapley_value/paper.md) | The Shapley value of integration: the mediator captures the rent | the mediator captures two-thirds of the value; an outsider captures less than nothing |
| [Q112](org_frontier/questions/q112_veto_power/paper.md) | Veto power: everyone can break it, only the mediator captures it | destruction is democratic, value is concentrated |
| [Q113](org_frontier/questions/q113_substitutability_value/paper.md) | Substitutability destroys value; a required set shares it | substitutability destroys all value; a required set shares it equally |
| [Q114](org_frontier/questions/q114_principal_rent/paper.md) | The principal captures value by creating it | a principal captures value only by creating it; ownership alone captures nothing |
| [Q115](org_frontier/questions/q115_market_value/paper.md) | Scale pays the scarce, not the required | a growing required market commoditizes its agents and pays the scarce parties |
| [Q116](org_frontier/questions/q116_value_against_structure/paper.md) | Strategic value is structural depth, smoothed | strategic value and structural depth rank the parties alike, and coincide only in the small |
| [Q117](org_frontier/questions/q117_phi_free_test/paper.md) | Triadicity has a Φ-free test, and it reads the logic | triadicity has a Φ-free test, but it reads the logic, not the wiring |
| [Q120](org_frontier/questions/q120_higher_order_binding/paper.md) | No pure higher-order bind: every party in a triadic form is pivotal | no pure higher-order bind: every party in a triadic form is pivotal |
| [Q121](org_frontier/questions/q121_external_criterion/paper.md) | The verdict is interventional: an external criterion where observation fails | the verdict has an interventional correlate where observation fails |
| [Q122](org_frontier/questions/q122_game_validity/paper.md) | Is the value function a valid cooperative game? A split verdict | the game is valid where the wave used it, and the critique holds where it bites |
| [Q123](org_frontier/questions/q123_reproducibility/paper.md) | The verdict is reproducible within IIT-4.0, and version-bound | the verdict is reproducible within IIT-4.0, and the SYSTEM_CUTS charge is misdirected |
| [Q124](org_frontier/questions/q124_aggregation_robustness/paper.md) | The verdict is a robust capacity reading, not an artifact of the maximum | the verdict survives every reasonable aggregation; only the strict every-state rule flips it |
| [Q125](org_frontier/questions/q125_four_party_higher_order/paper.md) | No pure higher-order bind at four parties: redundancy keeps every party pivotal | no pure higher-order bind at four parties either: redundancy does not free the bind |
| [Q126](org_frontier/questions/q126_interested_mediator/paper.md) | The interested mediator: self-interest erodes coordination irreducibility | self-interest disintegrates the coordination, and a gatekeeping agenda corrodes it fastest |
| [Q127](org_frontier/questions/q127_interest_baselines/paper.md) | Denial is not special: self-interest collapse depends on the mediator's rare output | denial is not special: the collapse agenda flips with the baseline, and balanced mediators re-integrate |
| [Q128](org_frontier/questions/q128_adaptive_mediator/paper.md) | The adaptive mediator: self-interest and irreducible coordination can coexist | adaptation re-integrates a predatory mediator, but only if its objective reads both parties |
| [Q129](org_frontier/questions/q129_mediator_interpolation/paper.md) | Faithful to predatory: an adaptive objective re-integrates the system by displacing a party | two readings of coordination survival diverge: adaptation re-integrates the system by displacing a party |
| [Q130](org_frontier/questions/q130_pivotal_excluded/paper.md) | Pivotal but excluded: a coordination can depend on a party its core does not contain | necessity is broader than membership: a party can be pivotal yet outside the core |
| [Q131](org_frontier/questions/q131_value_capture/paper.md) | Value capture under an interested mediator: destruction, not extraction | interested mediation is value destruction, not rent extraction |
| [Q132](org_frontier/questions/q132_value_baselines/paper.md) | Destruction or extraction: value capture under an interested mediator is baseline-relative | destruction or extraction is baseline-relative, and value must be read at the integrating state |
| [Q133](org_frontier/questions/q133_deny_symmetry/paper.md) | Agenda symmetry of value capture: deny extracts on XNOR as approve extracts on XOR | the destruction-vs-extraction split is symmetric in the agenda |
| [Q134](org_frontier/questions/q134_rent_scaling/paper.md) | The mediator's rent dilutes: two-thirds is a three-party number | the mediator's rent dilutes as the coordination grows |
| [Q135](org_frontier/questions/q135_objective_rent/paper.md) | The objective's rent: the system's agenda is a co-owner of the coordination | the system's agenda is a rentier on a par with the system |
| [Q136](org_frontier/questions/q136_competing_mediators/paper.md) | Two competing mediators: competition destroys the coordination or stacks another toll | competition does not return the rent: substitutes destroy the value, complements split it |
| [Q137](org_frontier/questions/q137_interested_worker/paper.md) | The interested worker: gaming the system breaks the coordination, it does not reclaim value | the worker cannot reclaim value by gaming; resistance breaks the coordination |
| [Q138](org_frontier/questions/q138_faithful_fraction/paper.md) | The minimum faithful fraction: reviving the coordination, and who pays for it | reviving the coordination takes three-quarters faithfulness, and the rent is the last quarter |
| [Q139](org_frontier/questions/q139_value_veto/paper.md) | Value and veto: Q112's decoupling is the integration | veto is always universal; the value-veto gap is the integration |
| [Q140](org_frontier/questions/q140_coalition_stability/paper.md) | The core inverts the rent: faithful mediation monopolizes, interest frees the value | faithful mediation monopolizes the core; interest frees it |
| [Q141](org_frontier/questions/q141_lagging_objective/paper.md) | The lagging objective: slow learning keeps the worker in the coordination | a lagging objective rescues the worker that immediate adaptation displaces |
| [Q143](org_frontier/questions/q143_ring_verdict_geometry/paper.md) | The Ring's Verdict and Where Its MIP Cut Falls | The conjunctive ring reads triadic at every size from n=3 to n=7. The core is the full node set |
| [Q144](org_frontier/questions/q144_mediator_hierarchy_depth/paper.md) | Mediator hierarchy: does Φ track depth like a chain or breadth like a pool? | depth holds Φ at the chain constant; breadth grows it linearly |
| [Q145](org_frontier/questions/q145_spanning_mediator_law/paper.md) | The spanning-mediator law | A single mediator that spans every party binds the whole set into the core, and Φ rises one |
| [Q146](org_frontier/questions/q146_smallworld_rewire_phi/paper.md) | Rewiring a conjunctive ring lowers Phi; there is no small-world peak | rewiring lowers Φ monotonically; no small-world peak |
| [Q147](org_frontier/questions/q147_random_boolean_topology/paper.md) | Which graph statistic predicts a triadic verdict, and how large Φ is | short cycles predict a triadic verdict; core in-degree does not predict Φ |
| [Q148](org_frontier/questions/q148_multihub_chain_hierarchy/paper.md) | Hierarchy depth and the hub-seam: where a chain of hubs stops integrating | A feedforward chain of gating hubs does not hold a core that spans its groups. At every tested depth the |
| [Q149](org_frontier/questions/q149_topology_shapley_split/paper.md) | The Shapley split of subsystem Φ across topologies | The mediator rent does not spread out as mediation is carried by more hubs. It concentrates. The |
| [Q150](org_frontier/questions/q150_ring_chord_integration/paper.md) | Adding one chord to a conjunctive ring: where the integration goes | A single chord across a conjunctive ring leaves the whole-system Φ flat but moves the cut and |
| [Q151](org_frontier/questions/q151_hub_failure_resilience/paper.md) | Hub-failure resilience: redundant mediation protects the triadic verdict, but the cycle is not the reserve | A single hub loses the triadic verdict when it is frozen. A backup hub and a non-hub ring each keep it. The |
| [Q152](org_frontier/questions/q152_verdict_vs_complex_topology/paper.md) | The whole-system verdict and the major complex are not interchangeable diagnostics | The whole-system verdict and major-complex membership disagree on the studied catalog |
| [Q153](org_frontier/questions/q153_triadic_dyadic_classifier/paper.md) | Classifying the triadic-vs-dyadic Φ verdict from CRQA features | CRQA features read from sampled runs do not recover the triadic-vs-dyadic exact-Φ verdict above |
| [Q154](org_frontier/questions/q154_bottleneck_node_recovery/paper.md) | Behavioral centrality misses the structural articulation point | Coupling centrality does not recover the node exact-Φ marks as the form's articulation point. On the |
| [Q155](org_frontier/questions/q155_mc_membership_threshold/paper.md) | A coupling-centrality threshold recovers major-complex membership only weakly, and fails on reciprocal coupling | Coupling centrality carries a real but weak signal for major-complex membership. Pooled over 361 |
| [Q156](org_frontier/questions/q156_interested_mediator_signature/paper.md) | A CRQA signature for the interested mediator | Interested and faithful mediators that share a wiring graph and a full {W, S, C} Φ-core do not |
| [Q157](org_frontier/questions/q157_te_vs_dcrp_direction/paper.md) | Transfer entropy reads directed read edges better than the recurrence peak lag | Pairwise transfer entropy recovers the true orientation of a directed read edge far more often |
| [Q158](org_frontier/questions/q158_phi_magnitude_regression/paper.md) | Whole-system recurrence does not track the magnitude of major-complex Φ | Whole-system CRQA measures do not predict the magnitude of exact major-complex Φ across the |
| [Q159](org_frontier/questions/q159_length_to_verdict_curve/paper.md) | How Long a Run a Stable CRQA Verdict Needs | The CRQA triadic/dyadic verdict settles fast. Convergence length does not track Φ magnitude in this |
| [Q160](org_frontier/questions/q160_five_node_complex_recovery/paper.md) | Coupling-centrality recovery of the major complex at five parties | q160 |
| [Q161](org_frontier/questions/q161_noise_robust_verdict/paper.md) | Which structural verdict survives update-noise misspecification | Both hypotheses were fixed before computing. Both fail, and the way they fail reverses the |
| [Q162](org_frontier/questions/q162_feature_ablation_minimal/paper.md) | The minimal CRQA feature set for the joint structural verdict | The minimal CRQA feature set for the joint structural verdict keeps whole-system recurrence. On a |
| [Q163](org_frontier/questions/q163_computationalism_under_agenda/paper.md) | Computationalism under an agenda: the interested mediator as a third object |  |
| [Q164](org_frontier/questions/q164_perceivable_agenda_fraction/paper.md) | The perceivable agenda: an imposed rule is louder in outcomes than a hidden one | An imposed agenda is more perceivable from outcomes than a merely hidden rule, and it adds marginal- |
| [Q165](org_frontier/questions/q165_intent_compression_into_agenda/paper.md) | Intent compression into an agenda: self-interest steepens embodiment loss | the agenda crowds out the channel for the worker's meaning |
| [Q166](org_frontier/questions/q166_phantom_addressee_displaced/paper.md) | The phantom addressee displaced: when the mediator's agenda becomes the addressee | the addressee becomes the agenda, and the worker drops to referent |
| [Q167](org_frontier/questions/q167_capture_meets_agenda/paper.md) | Capture meets the agenda: interest does not lower the worker's displacement threshold | interest does not simply lower the capture threshold |
| [Q168](org_frontier/questions/q168_opacity_floor_under_agenda/paper.md) | The opacity floor under an agenda: does interest raise the worker's surprise floor? |  |
| [Q169](org_frontier/questions/q169_lagging_objective_prediction_lag/paper.md) | A Lagging Objective Lets the Displaced Worker's Model Track the Platform | the lagging objective lets the worker's model track the platform better |
| [Q170](org_frontier/questions/q170_extracting_platform_tracking/paper.md) | Does the worker's generative model track an extracting platform? | the worker tracks an extractor worse, and worst where extraction equalizes |
| [Q171](org_frontier/questions/q171_drift_binding_with_agenda/paper.md) | Drift Binding with an Agenda: Whether the Two Opacities Stack | The two opacities do not stack. Both hypotheses about how drift and interest combine were fixed before |
| [Q172](org_frontier/questions/q172_facet_difficulty_under_interest/paper.md) | Where interest concentrates: a facet signature, not a uniform tax | Interest does not tax every facet equally, and it does not tax the facets the survey scale names |
| [Q173](org_frontier/questions/q173_build_rule_to_phi/paper.md) | A rule-to-Φ field bridge with a coder-disagreement confidence interval | The field bridge `org_frontier/field/rule_to_phi.py` encodes per-party coded determination rules |
| [Q174](org_frontier/questions/q174_alpha_phi_width/paper.md) | Propagated Φ confidence-interval width as a read of coder disagreement | CI width tracks coder agreement, and a stable agreement floor turns the verdict indeterminate |
| [Q175](org_frontier/questions/q175_substitutability_flipper/paper.md) | The substitutability flipper: coding a worker as interchangeable dissolves the triad | Coding the worker as one slot in an interchangeable pool flips the exact-Φ verdict from triadic to |
| [Q176](org_frontier/questions/q176_passthrough_flipper/paper.md) | The pass-through flip and the rule the verdict is most sensitive to | The pass-through flip does not universally collapse the verdict, and the system's |
| [Q177](org_frontier/questions/q177_spectator_complex/paper.md) | Idle spectators sink whole-system Φ; the major complex keeps the triadic core | an idle spectator sinks whole-system Φ but leaves the major complex untouched |
| [Q178](org_frontier/questions/q178_bit_grain_sensitivity/paper.md) | The Bit Cut on a Graded Action Is Verdict-Bearing | Collapsing a graded coded action to one bit at different cut points changes the structural Φ |
| [Q179](org_frontier/questions/q179_time_grain_sensitivity/paper.md) | The update time-grain is a coding choice that moves the Φ verdict | the update time-grain changes the verdict, and the flip is predictable |
| [Q180](org_frontier/questions/q180_individuation_boundary/paper.md) | Individuation and the Party Boundary | Where the coder draws the party boundary moves the Phi verdict. Splitting a coded party flips the |
| [Q181](org_frontier/questions/q181_flipper_interaction/paper.md) | Two flippers at once: redundancy, not interaction | The two flippers do not interact to restore irreducibility, and their coding |
| [Q182](org_frontier/questions/q182_adversarial_coding/paper.md) | Adversarial coding against the agreement-weighted Φ confidence interval | An adversary restricted to evidence-permitted readings forces the point verdict at will, and the |
| [Q183](org_frontier/questions/q183_build_disagreement_bridge/paper.md) | A Φ-spread bridge for two divergent party accounts of one coordination | The bridge module `org_frontier/qualitative/disagreement_phi.py` reads two party accounts of one |
| [Q184](org_frontier/questions/q184_gig_dispatch_spread/paper.md) | Φ spread between a driver's suggestion and a platform's commit account of dispatch | The driver and the platform give two accounts of one dispatch. The driver's suggestion account |
| [Q185](org_frontier/questions/q185_ats_commit_convey_spread/paper.md) | Commit and convey on one wiring diagram: a disagreement-Φ spread in algorithmic hiring | The disagreement-Φ spread separates the candidate's commit account from the manager's convey |
| [Q186](org_frontier/questions/q186_spread_decomposition_law/paper.md) | Three spread components vary independently across an account-pair census | The three spread components carry separate information across the synthetic census. They do not |
| [Q187](org_frontier/questions/q187_moderation_oversight_spread/paper.md) | Where Two Accounts of a Takedown Disagree: Localizing the Policy Team in the Phi Spread | Two accounts of one takedown coordination, differing only in the policy team's rule, were |
| [Q188](org_frontier/questions/q188_handoff_directionality_spread/paper.md) | Handoff Directionality Spread: When Narrated Reciprocity Moves the Phi Verdict | The two narrations of one handoff read as different structures. The outgoing clinician's one-way |
| [Q189](org_frontier/questions/q189_peer_review_veto_spread/paper.md) | The Editor's Core Membership in Dispute: A Gate/Conduit Spread | The gate and conduit accounts read the same whole-system verdict (both triadic, max_phi = 2.0, |
| [Q190](org_frontier/questions/q190_spread_robustness_noise/paper.md) | Is the disagreement-Φ spread robust to elicitation noise? | The disagreement-Φ spread survives synthetic elicitation noise. Under bounded Bernoulli jitter on |
| [Q191](org_frontier/questions/q191_triage_spectator_spread/paper.md) | Φ spread between an agent's party account and a system's spectator account of a triage | An agent and a system give two accounts of one triage. The agent counts a monitoring supervisor a |
| [Q192](org_frontier/questions/q192_spread_reconciliation_cost/paper.md) | Reconciliation cost: edit distance between two accounts and the Φ spread | Two accounts of one coordination are reconciled by single-rule edits. The reconcile routine runs |
| [Q193](org_frontier/questions/q193_phi_bridge_build/paper.md) | A per-worker Φ coordination measure for the algorithmacy panel | A per-worker Φ-based coordination measure can be derived from each simulated worker's coordination form, |
| [Q194](org_frontier/questions/q194_phi_facet_specificity/paper.md) | Facet specificity: a partition-restricted Φ for counterpart inference | The exact-Φ coordination measure predicts the three ACS facets differentially, and a |
| [Q195](org_frontier/questions/q195_phi_incremental_over_se/paper.md) | Discriminant validity of the Φ bridge: incremental association over self-efficacy and belonging | On the simulated cohort Φ_coord carries association with ACS-total that survives controlling for |
| [Q196](org_frontier/questions/q196_phi_commit_moderation/paper.md) | Φ_coord predicts algorithmacy more where the system commits | The Φ_coord-to-ACS association strengthens under perceived system commitment. In the commit cohort, |
| [Q197](org_frontier/questions/q197_phi_invariance_waves/paper.md) | Invariance of the Φ_coord-to-ACS bridge across panel waves | The Φ_coord-to-ACS bridge holds metric and scalar invariance across the three simulated panel waves. A |
| [Q198](org_frontier/questions/q198_phi_predicts_growth/paper.md) | Baseline Φ_coord predicts the algorithmacy growth slope in the simulated panel | On the simulated panel, a worker's baseline (W1) Φ_coord predicts the individual latent ACS-growth slope |
| [Q199](org_frontier/questions/q199_phi_growth_mechanism/paper.md) | Φ_coord moves with the construct within a person across waves | On the simulated panel, within-person change in Φ_coord tracks within-person change in algorithmacy. A |
| [Q200](org_frontier/questions/q200_phi_bifactor_loadings/paper.md) | Φ_coord loads on the general algorithmacy factor, not a specific facet | On the simulated W2 cohort, Φ_coord loads on the general algorithmacy factor, not on a specific facet |
| [Q201](org_frontier/questions/q201_phi_substitutability_capture/paper.md) | substitutability degrades Φ_coord and captures algorithmacy | Substitutability degrades Φ_coord, and the degraded Φ_coord captures the substitutability-to- |
| [Q202](org_frontier/questions/q202_phi_bridge_falsification/paper.md) | Does the Φ-bridge survive its own falsification battery? | The Φ-bridge survives the worker-form-shuffle null in both simulated cohorts, and exact Φ adds |
| [Q203](org_frontier/questions/q203_real_coordination_coupling/paper.md) | Reading a real coordination four ways | the lab's first real coordination, read four ways |
| [Q204](org_frontier/questions/q204_phi_on_real_coordination/paper.md) | Exact Φ on a real coordination, decided by the coding | exact Φ on a real coordination, decided by the coding |

</details>

<!-- END GENERATED DIRECTORY -->

## Setup

Requires Python ≥ 3.10 and PyPhi's IIT-4.0 line.

```bash
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
```

Run an org_frontier probe, or a foundations experiment, from the repo root:

```bash
python -m org_frontier.probes.probe_conjunctive_law          # a lab probe
python -m foundations.proxy_audit.run 15 1 && python -m foundations.proxy_audit.analyze
```

**New here and want to contribute an experiment?** [`GETTING_STARTED.md`](GETTING_STARTED.md)
walks the whole path by hand — environment, the instrument-validation gate, the model in one
paragraph, scaffolding a new question with `python -m org_frontier.protocol.new_question`,
registering numbers for CI, and opening the pull request.

## Repository note

This working tree also contains a separate, private dissertation repository nested at `dissertation/`,
gitignored and invisible to this repo. Where you run git from decides which remote you touch. See
[`REPO_LAYOUT.md`](REPO_LAYOUT.md) before committing.

## License and citation

MIT — see [LICENSE](LICENSE). To cite, see [CITATION.cff](CITATION.cff).

## Contributing and publishing

Contributions are welcome, and the record is meant to grow by them. [`PUBLISHING.md`](PUBLISHING.md)
describes how to publish an essay or a study here: fork, open a pull request into the `contrib` branch,
pass a reproducibility-first public review, and get merged. Both `contrib` and `main` are branch-protected;
every change is a pull request, the `reproduce-the-numbers` workflow re-derives each registered number,
and a merge needs one approving review. The aspiration is a community of maintainers who sign off on
submissions in a peer review that is reproducible by construction. To join that review board — the
reviewers and editors — apply through the `maintainer-applications` branch; see
[`MAINTAINERS.md`](MAINTAINERS.md). Code and probe conventions are in [`CONTRIBUTING.md`](CONTRIBUTING.md).

## For AI agents and LLM tools

Three files serve agents, by purpose:

- **[`AGENTS.md`](AGENTS.md)** — the operating manual for an agent working *in* the repo: the map, the
  run and verify commands, the two-repo git rule, the land flow, and the definition-of-done checklist.
  Nested `AGENTS.md` files cover the subtrees with their own workflow.
- **[`MAP.md`](MAP.md)** — a generated one-screen index of the entry documents, programs, machinery, and
  live counts. Load it instead of crawling the tree.
- **[`llms.txt`](llms.txt)** — a token-light brief for *describing* the project to outside users: a
  canonical summary safe to copy into memory, framing rules, and links to the key documents.
