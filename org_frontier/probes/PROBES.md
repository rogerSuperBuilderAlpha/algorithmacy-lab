# Probes — an iterative hypothesis loop

Each probe states a hypothesis grounded in a dissertation concept, tests it with exact IIT-4.0 Φ via
PyPhi, and records the result. Later probes build on earlier ones. The verdict is read on the major
complex (spectator-robust) where a form may have idle nodes, otherwise whole-system Φ over the MIP.

Dissertation concepts in play: the algorithmacy construct's **dimensions** (inferential,
translational, temporal-tracking), its **scope conditions** (signal asymmetry, intent compression,
opaque mediation), and the triadic structure (worker–system–counterpart through a system that
interprets both and commits determinations neither controls).

| # | Concept | Hypothesis | Verdict | Result |
|---|---|---|---|---|
| 1 | Collective action in the triad | Counterpart coalition pulls the core to {C1,C2} and ejects the worker | **H1 supported** | With a direct C1↔C2 channel the major complex becomes {C1,C2} (Φ=2.0); the worker drops out and the whole system factors. Counterpart solidarity dissolves the worker's triadic bind. `probe_coalition.py` |

| 2 | Intent compression (translational) | Compression removes intent dimensions from the core | **H2 supported, refined** | An intent bit the determination drops leaves the core (compressed: W2 out). Redundant (OR) reading drops both bits; only a pivotal reading (XOR) keeps each in. Footprint = dimensions made *pivotal*, not merely read. `probe_compression.py` |

| 3 | Temporal-tracking (regime switch) | A switching rule pulls the regime node into the core | **H3 refuted** | A switching rule does NOT integrate the regime. An exogenous rule-clock stays a spectator (emit-only); an outcome-tracking regime *destabilizes* the core (Φ 2.0→0.28, worker drops out). Temporal-tracking is a worker competency, not a structural property of the form — consistent with the dissertation's worker-level framing. `probe_regime.py` |

| 4 | Inferential (folk-theory node) | A used inference joins the core | **H4 supported, striking** | An unused inference is a sink (out). A *blended* inference (W'=S∧M) joins the core as {W,S,M} and **displaces the actual counterpart C**. Acting purely on the model (W'=M) decouples the worker. The worker coordinates with its *model* of the other, not the other. `probe_inference.py` |
| 5 | Signal asymmetry (scope cond.) | Both parties need feedback; one-sided collapses it | **H5 supported** | Symmetric feedback → triadic {W,S,C}. One-sided feedback drops the no-feedback party (worker-only → {W,S}; counterpart-only → {S,C}). An emit-only party leaves the core. `probe_asymmetry.py` |
| 6 | Exit option (Hirschman) | An absorbing exit erodes the triad | **H6 partial** | An absorbing exit erodes the counterpart's core membership (core → {W,S} in exited states). The reversible-reentry form is **confounded** — it accidentally adds a W→C back-channel, so its collapse is not a clean exit result. Flagged, not claimed. `probe_exit.py` |

| 7 | "Determinations neither party controls" | One-party control collapses the triad | **H7 supported, refined** | S following one party alone (S=W or S=C) is dyadic — the ignored party drops. But *both* mutual-veto (AND) and either-forces (OR) are triadic. The criterion is "S genuinely reads both," not "requires both." `probe_control.py` |
| 8 | Coalition displacement, as a rate | Worker far less often in core under coalition | **H8 weak / tempers Probe 1** | Over all 256 counterpart-couplings: worker-in-core 20.8% with a coalition vs 31.2% without. Real direction, but a modest 10-pt effect — NOT the categorical ejection the 3 named forms in Probe 1 showed. The vivid forms were unrepresentative. `probe_coalition_sweep.py` |

| 9 | Inference displacement, as a rate | C and M trade off in the core | **H9 confirmed, categorical** | Over 64 forms, C and M **never coexist** in the core (0 forms). P(C in core \| M in)=0%; P(C in core \| M out)=91%. The inferred model *substitutes for* the real counterpart, never supplements it. The sweep confirms Probe 4 (vs Probe 8, which tempered Probe 1). `probe_inference_sweep.py` |
| 10 | Determination type vs multi-party core | Parity keeps all parties most robustly | **H10 refuted, surprising** | AND and OR keep all parties at Φ=3.0; parity keeps all but at Φ=0.25; **majority (2-of-3) factors entirely → dyadic**. Redundancy (no party pivotal) destroys irreducibility, extending Probe 2 to the determination level. `probe_parity_multiparty.py` |

| 11 | Pivotality as a predictor | Influence predicts core membership | **H11 validated** | Across 256 determinations × 3 parties: P(in core) rises monotonically with influence — 0% at influence 0 (never), 12.5%, 37.5%, then **100% at influence ≥ 0.75**. Rank-AUC = **0.891**. The discovered mechanism is quantitatively confirmed, not just illustrated. `probe_pivotality.py` |

## A validated two-condition account of core membership

The loop did not just illustrate a theory; Probe 11 validated it. Given the structural object (the
major complex of a small mediated system), **which parties are in the irreducible coordination is
governed by two conditions**:

1. **Bidirectional constraining coupling** (necessary; probes 3–5, principal): the party must both
   feed and be fed by the coordination. Emit-only sources and read-only sinks are out.
2. **Pivotality / influence** (graded predictor; probes 2, 7, 10, validated in 11): given coupling,
   P(in core) rises monotonically with the determination's Boolean sensitivity to the party — zero
   influence excludes (0/48), influence ≥ 0.75 guarantees inclusion (AUC 0.89).

This is the loop's headline result: a discovery (probes 1–7) → population rating (8–10) → mechanism
synthesis → quantitative validation (11) arc, all on exact IIT-4.0 Φ via PyPhi. It also re-grounds
the algorithmacy thesis: a coordination form binds a party into an irreducible triad exactly when
that party is both two-way coupled and pivotal to the determination — which is what "a system that
interprets both parties and commits determinations neither controls" means, made computable.

| 12 | Two-condition account on the full family | Coupling + pivotality predict core membership for arbitrary wirings | **H12 supported, generalizes** | Sample of the 4,096-wiring family: non-bidirectional nodes in core **0/435 (categorically necessary)**; among coupled nodes P(in core) rises 41%→63%→83%→89% with influence (AUC 0.695, lower than the controlled 0.89 — single-node influence misses higher-order effects). The account is not an artifact of the mediated setup. `probe_family_validation.py` |

| 13 | Joint vs isolated influence | Context-sensitive influence closes the AUC gap | **H13 refuted** | Total context influence does *worse* (AUC 0.649) than isolated per-function influence (0.695). The full-family gap to 0.89 is NOT a missing per-node feature — it is genuinely holistic. Per-node pivotality has a prediction ceiling because the major complex is not a function of per-node features (as expected for an irreducibility measure). `probe_joint_influence.py` |
| 14 | Verdict robustness to encoding | Verdict stable under re-encoding; magnitude not | **H14 confirmed** | Isomorphism battery: 0 verdict flips across 8 forms × 8 state-relabelings, Φ-range exactly 0 (instrument well-defined). Re-encoding battery: AND/OR/NAND/NOR/XOR of the same inputs all triadic, Φ ranges 0.5–2.0 (CV 0.35). Exactly the dissertation's "verdict robust, magnitude soft" claim. `probe_robustness.py` |
| 15 | HMC vs algorithmacy (discriminant) | Verdict separates the two constructs | **H15 confirmed, clean** | All 4 HMC forms dyadic (core {W,S}); all 4 algorithmacy forms triadic. No overlap. The structural verdict is a clean discriminant between human–machine communication and algorithmacy — the dissertation's discriminant-validity claim, made structural. `probe_discriminant.py` |
| 16 | Power asymmetry ("neither controls") | Triadic requires balanced influence | **H16 confirmed, sharp** | Over 16 determinations: every triadic form has influence-asymmetry 0 (balanced); any asymmetry → dyadic (mean asymmetry 0.40 for dyadic, 0.00 for triadic). "Neither party controls" = equal influence, made quantitative. `probe_power.py` |
| 17 | What Φ magnitude tracks | Magnitude indexes structural quantities | **H17 supported** | Over the 256-form family, Φ magnitude correlates most with party feedback (ρ=+0.45, how many parties read S), then mediator arity (+0.24), then weakly parity (+0.18). Magnitude is not a readability scale but it does index feedback richness and arity. `probe_magnitude.py` |
| 18 | Φ vs coordination difficulty | Triadic ⇔ coordination-required | **H18 supported, caveated** | Verdict agrees with the analytic "coordination-required" proxy on 12/16 determinations (75%); bottleneck (no channel) Φ=2.0 vs open-channel Φ=0.83 — difficulty higher for the bottleneck, both triadic (a channel grades Φ down, not always to 0). **Circularity explicit**: both derive from the determination, so this is structural consistency, not independent validation. `probe_difficulty.py` |
| 19 | CMC (conveying medium) | A conveyor factors; only a joint determination is triadic | **H19 confirmed** | All conveying-medium forms (S relays/echoes/displays) are dyadic; only the joint determination is triadic. A system that conveys but does not commit is a wire. `probe_cmc.py` |
| 20 | AI-MC (AI in the worker's production) | AI-MC is not structurally triadic | **H20 refuted — a real limit** | The W→A→C loop is triadic (Φ=2.0, core {W,A,C}) just like external algorithmacy. The structural verdict CANNOT distinguish AI-MC from algorithmacy; the distinction depends on whether the AI is modeled as part of the worker (a unit-of-analysis choice), not on structure. Φ separates HMC/CMC cleanly (probes 15, 19) but not AI-MC. `probe_aimc.py` |
| 21 | Contestability / accountability | Contestability decouples the worker | **H21 confirmed, sharp** | An uncontestable determination (worker bound, W'=S) is triadic with W in core; ANY contestability (sticky, override, autonomous) drops the worker out → dyadic {S,C}. Accountability-vacancy is what binds the worker into the triad — and the effect is categorical, not graded. `probe_contestability.py` |
| 22 | Worker competition | Worker side mirrors counterpart side | **H22 confirmed** | Substitutable workers (platform matches either) factor → dyadic {S,C}; both-required is triadic {W1,S,C,W2}; a worker coalition relocates the core to {W1,W2}. Perfectly mirrors the counterpart results (probes 1, multi-homing) — the structure is symmetric in worker/counterpart roles. `probe_competition.py` |
| 23 | System memory / reputation | A reputation node joins the core | **H23 refuted** | As a sticky accumulator (M'=W∨M), the memory never enters the core; scoring purely on reputation (S reads M not present W) even decouples the present worker → core {S,C}. A reputation that is too inertial is non-pivotal. (Caveat: a more responsive memory might differ — sticky accumulation is what makes it non-pivotal, consistent with the pivotality principle.) `probe_memory.py` |
| 24 | Opaque mediation as a gradient | Transparency collapses the triad at a threshold | **H24 refuted, refined** | Blending a direct worker→counterpart observation channel (p: 0→1) leaves Φ at 2.0 and the verdict triadic at every level — even full transparency. Opacity is about the *binding pathway* (the counterpart reaching the worker only through the committed determination), not mutual visibility. The worker can see the counterpart and still be bound. `probe_opacity.py` |
| 25 | Joint vs decomposable determination | Only a genuine joint commit is triadic | **H25 confirmed** | A single joint determination is triadic; a split mediator with independent per-party channels factors to dyadic (two independent dyads); cross-coupled mediators that recombine are triadic again. The "joint" in joint determination is load-bearing. `probe_joint.py` |
| 26 | MIP as a structural fault line | The MIP isolates the weakest link | **H26 confirmed** | Every triadic corpus form cuts at {W,SC} — the worker is the most separable element; the system+counterpart cohere more tightly than the worker attaches. The MIP names the coordination's weakest seam: structurally, the worker is the most peripheral party. `probe_mip.py` |
| 27 | Mediator reliability | The triad degrades gracefully with unreliability | **H27 confirmed** | Φ falls smoothly with mediator unreliability (2.0 → 1.5 → 1.2 → 0.68 → 0.35 → 0.14) and the verdict holds triadic until reliability = 0.5 (random), where it collapses. Reliability is a genuine *continuous* Φ axis (unlike encoding). The triad tolerates a noisy system. `probe_reliability.py` |
| 28 | Information-richness asymmetry | The richer party occupies more of the core | **H28 partial** | A determination reading both worker bits jointly with the counterpart binds all four (Φ=3.0); reading one bit drops the other (compression, cf. Probe 2). But coupling the worker's bits to *each other* (XOR) binds the worker internally and *excludes* the counterpart. Richness helps the core only when channeled through a cross-party pivotal read. `probe_richness.py` |
| 29 | The variance puzzle (equifinality) | Same system, divergent outcomes | **H29 confirmed, nuanced** | Holding the system fixed and varying the worker's policy: success ranges 0.00–0.38 and the verdict itself varies — only a worker who stays live to the determination instantiates the triad; contrarian/withdrawn workers fail AND break it; eager workers succeed equally but dyadically. Triadicity is co-determined by worker engagement, and triadic ≠ higher success. The variance puzzle, structurally. `probe_variance.py` |
| 30 | Structural extremes of the triad | Minimal/maximal irreducible forms | **H30 confirmed, clean** | Every one of the 24 triadic strict-mediation forms has **exactly 4 edges** (joint determination S←W,S←C + both parties reading S); none has more or fewer. The triad has a fixed edge budget. Φ is 2.0 (16 forms) or 0.5 (8 parity forms). `probe_extremes.py` |
| 31 | Comprehensive discriminant map | Verdict maps the construct space | **H31 confirmed** | 6/6 neighbor constructs classify as expected: CMC, HMC, AI-literacy, sensemaking dyadic; algorithmacy and AI-MC triadic. One clean map, with AI-MC flagged as the lone structural boundary case (triadic by structure, dyadic-by-unit). `probe_discriminant_map.py` |
| 32 | Temporal grain (1-step vs 2-step) | Verdict is grain-relative | **H32 confirmed, consequential** | ALL three triadic corpus forms flip to **dyadic** under the 2-step composed map (Φ 2.0→0); dyadic forms stay dyadic. Observing the coordination too coarsely washes out the triad entirely. A real caveat for empirical sampling cadence. `probe_temporal_grain.py` |
| 33 | MIP fault line across the family | The worker is the weakest seam | **H33 refines Probe 26** | Over the 24 triadic family forms: 67% cut at {W,SC} (worker is the severed singleton), 33% cut at the complete {W,S,C} (the parity Φ=0.5 forms). Worker-as-weakest-seam is the dominant pattern, not universal. `probe_mip_population.py` |
| 34 | Graded contestability | Triad survives partial contestability | **H34 refines Probe 21** | Stochastic contestability q: Φ falls smoothly (2.0→0.86→0.62→0.42→0.19) but the verdict stays triadic until total autonomy (q=1). The triad tolerates *partial* contestability; only a worker who fully ignores the determination escapes it. Magnitude sensitive, verdict robust. `probe_graded_contestability.py` |
| 35 | Minimal-edge triad at n=4 | The edge budget rises with parties | **H35 confirmed** | Every triadic n=4 strict-mediation form has exactly **6 edges** (n=3 was 4). The minimal triad scales as 2(n−1): the joint determination reads all outer parties and they read back. A clean structural scaling law. `probe_min_triad_n4.py` |
| 36 | Cause-effect-structure richness | Triadic forms are structurally richer | **H36 confirmed** | Triadic forms carry more distinctions (4.0 vs 2.6) and far more **relations** (7.0 vs 2.8, ~2.5×) than dyadic. The irreducible coordination is richer in kind, not just higher in Φ — the relations gap is the bigger differentiator. `probe_ces_richness.py` |
| 37 | Feature interaction: principal × coalition | The two displacements compete | **H37 — coalition dominates** | A counterpart coalition relocates the core to {C1,C2} even when an active gating+monitoring principal is present, ejecting worker, system, AND principal. Counterpart solidarity trumps principal control over the irreducible coordination. `probe_interaction.py` |
| 38 | Asymmetric reliability | Degrading the system's read of the counterpart factors it | **H38 confirmed** | As the system's perception of the counterpart degrades (r_c: 1→0), Φ falls smoothly (2.0→0.88→0.44→0.20) and the verdict holds triadic until the counterpart is fully invisible (r_c=0). Graceful degradation, verdict robust until the extreme. `probe_asym_reliability.py` |
| 39 | Feedback cycle necessity | A cycle is needed for the triad | **H39 confirmed** | An acyclic joint determination (parties as sources, system as sink) is dyadic; one feedback edge is dyadic; only the full cycle (both parties read the system back) is triadic. Irreducible coordination requires recurrence through both parties. `probe_cycle.py` |
| 40 | Broadcast topology | Fan-out factors into dyads | **H40 confirmed** | A system that relays/broadcasts the worker to many counterparts without a joint determination over them is dyadic (core {W,S}); only a joint determination over the counterparts (the pool) is triadic. Broadcast ≠ triad. `probe_broadcast.py` |
| 41 | Dashboard vs determination | A decoupled dashboard factors the worker out | **H41 confirmed (transparency theater)** | When the worker reads a dashboard decoupled from the committing determination, the system *splits*: {W, dashboard} factors off from {commit, counterpart}. The worker is bound to the display, not the decision. A decoupled metric literally removes the worker from the irreducible coordination. `probe_dashboard.py` |
| 42 | Redundant determination paths | Duplicate mediators are reducible | **H42 refuted/nuanced** | Two mediators both committing W∧C, read *conjunctively*, RAISE Φ (2.0→4.0) and both join the core — requiring both makes each pivotal. Read *disjunctively* (either suffices) they factor. Redundancy is not monolithic: AND-duplication binds, OR-duplication collapses (cf. the pivotality principle). `probe_redundant.py` |
| 43 | Self-referential mediator | A self-loop on S shifts magnitude only | **H43 refuted/nuanced** | A *sticky* mediator (S'=(W∧C)∨S) COLLAPSES the triad to a self-absorbed core {S} — a system running on its own inertia stops being a live joint determination and factors the parties out. A parity-memory mediator (XOR) stays triadic. Mediator inertia can break the triad. `probe_self_ref.py` |

## Probes 39–43 — sixth batch (topology, transparency theater, mediator dynamics)

Three confirmations (39 cycle, 40 broadcast, 41 dashboard) and two instructive refutations (42, 43):
- **Probe 41 (transparency theater)** is the org-richest: a dashboard decoupled from the real
  determination splits the system into {worker, display} and {commit, counterpart} — the worker is
  bound to what she sees, not to what decides her. Showing a worker a metric that is not the
  determination structurally *removes* her from the coordination.
- **Probe 42** sharpens redundancy: conjunctive duplication (both required) raises Φ and binds both
  mediators; disjunctive duplication (either suffices) factors. Same pivotality logic as probes 2/10.
- **Probe 43** finds a new collapse mode: an inertial (sticky) mediator latches onto its own state
  and ejects the parties — a system coasting on momentum is not a live joint determination.
- **Probe 39** completes the structural necessity picture: feedback recurrence through both parties
  is required, alongside the joint determination (25), the 2(n−1) edge budget (35), and pivotality.
## Probes 34–38 — fifth batch (graded perturbations, structure, interaction)

A recurring theme sharpens across 34, 38 (and 27): **under stochastic perturbation Φ degrades
smoothly while the verdict is robust until the extreme** — the binary classification is the stable
object, magnitude the sensitive one, now confirmed under noise as well as encoding (Probe 14).
Standouts:
- **Probe 35 gives a scaling law:** the minimal strict-mediation triad needs 2(n−1) edges (4 at
  n=3, 6 at n=4). Irreducible coordination has a fixed, party-count-dependent structural cost.
- **Probe 36:** triadic coordination is structurally richer (≈2.5× the relations of dyadic), so the
  triad/dyad distinction is qualitative, not merely a Φ threshold.
- **Probe 37 is a genuine interaction result:** counterpart solidarity dominates principal control —
  an organized counterpart pair becomes the irreducible core and ejects even an active corporate
  principal. The most politically suggestive finding in the logbook.
## Probes 29–33 — fourth batch (the motivating puzzle, structure, grain)

Highlights:
- **Probe 29 grounds the dissertation's opening puzzle structurally:** one system, worker policy
  varied, outcomes diverge (0.00–0.38) — and triadicity is itself co-determined by whether the
  worker stays live to the determination. Being in the triad is not the same as succeeding; it is a
  different *kind* of coordination, exactly the construct's claim.
- **Probe 30 gives the triad a fixed cost:** in strict mediation, irreducibility requires exactly
  four edges — the lean joint determination both parties read back. There is no fat triad and no
  sub-4-edge triad.
- **Probe 32 is the most consequential caveat in the whole logbook:** the verdict is *grain-relative*
  — sampling the coordination every two steps washes the triad out completely. Any empirical use of
  this classifier must match the observation cadence to the coordination's own timescale.
## Probes 24–28 — third batch (scope conditions, robustness, structure)

Three confirmations (25 joint, 26 MIP, 27 reliability), one refined refutation (24 opacity), one
partial (28 richness). Highlights:
- **Probe 24 refines the opacity condition:** what binds the worker is not the absence of mutual
  visibility but the routing of the counterpart's influence through the committed determination. The
  worker can watch the counterpart and remain bound, as long as the counterpart reaches her only via
  the system's commit. This corrects a naive reading of "opaque mediation."
- **Probe 26 gives the triad an anatomy:** the worker is structurally the most separable element
  (MIP cut {W,SC}). The coordination's weak seam is the worker's attachment, not the system–
  counterpart bond.
- **Probe 27 finds a real continuous Φ axis:** mediator reliability degrades Φ smoothly, unlike the
  encoding-dependence that made magnitude unreliable elsewhere. The triad tolerates an unreliable
  system down to the random limit.
## Probes 19–23 — second batch (neighbor constructs + platform features)

Three confirmations (19 CMC, 21 contestability, 22 competition) and two informative refutations:
- **Probe 20 is the most important: a limit on the structural instrument.** The verdict cleanly
  separates HMC and CMC from algorithmacy (both dyadic), but it does **not** separate AI-MC — the
  W→A→C loop is structurally triadic. So the AI-MC/algorithmacy distinction is not a structural fact;
  it is a unit-of-analysis choice (is the AI inside the worker, or a third party?). This says exactly
  where the Φ-classifier can and cannot adjudicate a construct boundary.
- **Probe 21 sharpens accountability:** uncontestability is categorically what binds the worker —
  any contestability at all decouples her. This is the structural content of "accountability-vacant."
- **Probe 22 establishes a symmetry:** worker-side and counterpart-side behave identically
  (substitutability factors, coalition relocates the core). The triad is role-symmetric.
- **Probe 23** warns that not every added platform mechanism binds: an inertial reputation score is
  non-pivotal and stays out — consistent with the pivotality principle (probes 2, 7, 10, 11).
## Probes 14–18 — five independent experiments (batch)

Run as one continuous pass. Outcomes: **four clean confirmations** (14 robustness, 15 discriminant,
16 power, 17 magnitude) and **one supported-with-caveats** (18 difficulty, circularity flagged). Two
results are worth keeping in view:
- **The instrument is well-defined and the verdict is the hard invariant** (14): Φ is exactly
  relabel-invariant, the verdict survives determination re-encoding, and only magnitude moves — which
  is the precondition for trusting the binary classifier the whole program rests on.
- **The verdict cleanly separates HMC from algorithmacy** (15) and **tracks "neither party controls"
  as balanced influence** (16): two of the dissertation's construct-definition claims hold as exact
  structural facts, not just arguments.

## Bound on the pivotality account (from Probe 13)

The two-condition account is not a complete reduction. Coupling is categorically necessary, and
pivotality predicts membership monotonically, but no single-node influence measure — isolated or
context-sensitive — pushes the full-family AUC past ~0.70. The residual is holistic: which parties
form the irreducible core depends on the global cause-effect structure, not just each party's own
influence. This is the honest ceiling of a per-node account, and it is what an irreducibility
measure should do. The account explains *necessity* exactly and *gradation* partially; the rest is
irreducibly whole.

## A unifying thread: pivotality

Probes 2, 7, and 10 converge on one mechanism. **A party is in the irreducible core only if the
determination makes it pivotal** — its state must be able to change the outcome given the others.
Redundant readings (OR of two intent bits in #2; majority 2-of-3 in #10) make parties non-pivotal
and drop them, even to the point of collapsing the whole form (majority → dyadic). Reading a party
is necessary but not sufficient; the determination must let that party *matter*. This is the
function-level twin of the structural "reads all parties" condition.

## Reading across probes 1–8

Probe 8 is a methodological flag for this whole logbook: **named-form findings are existence proofs,
not rates.** Probe 1's "coalition ejects the worker" is true for the forms shown but is a 10-point
population effect, not a law. The same caution applies to probes 4 (inference displacement) and the
principal core-contraction — they demonstrate that a structure *can* occur, not how often it does. A
population sweep is the right follow-up before any of these is stated as a general claim.

## Reading across probes 1–6

Two principles now hold across every probe and the `principal/` study:
1. **A node is in the irreducible core only via constraining bidirectional coupling.** Emit-only
   sources (no-feedback parties, exogenous rule-clocks, static principals) and read-only sinks
   (unused inference, monitors) stay outside. Probes 3, 4, 5 and `principal/` all show this.
2. **Adding a tightly-coupled node often displaces another from the core (a tendency, not a law).**
   A counterpart coalition displaces the worker (1); a blended inference displaces the counterpart
   (4); a maximally-coupled principal contracts to {S,P} (`principal/`). But it is not a fixed
   budget — `gates_and_monitors` binds all four into one core. The tendency is real, the strict
   conservation claim is false (and the counterexample is logged so it is not overstated).

The worker-competency dimensions (temporal-tracking #3, inference #4-unused) correctly do NOT add
structural irreducibility; they are burdens on the worker, as the dissertation frames them. The
structural conditions (signal asymmetry #5, opaque mediation, joint determination) DO.

The major complex tracks *who is bound into the coordination*, and the probes move parties in and
out of it. A counterpart coalition (1) ejects the worker; intent compression (2) drops unread/
non-pivotal intent dimensions; a switching rule (3) does not bind the regime at all. The recurring
structural principle, also seen in `principal/`: a node enters the irreducible core only through
bidirectional coupling that *constrains* it — emit-only drivers (rule-clocks, static principals) and
read-only sinks stay outside, and some couplings (outcome-tracking regimes) even shrink the core.
The dimensions of algorithmacy that are *worker competencies* (temporal-tracking, inference) do not
show up as extra structural irreducibility — which is what the dissertation says they are.

## Probe 1 — counterpart coalition (detail)

Nodes W, S, C1, C2. Baseline all-required pool is triadic, core {W,S,C1,C2} Φ=3.0. Add a direct
channel between the counterparts (each reads the other, weak: C1'=S∨C2; strong: C1'=C2). In both,
the major complex collapses to **{C1,C2} Φ=2.0** — the counterpart pair is the irreducible core and
the worker is pushed out. Org reading: when the parties on one side organize among themselves, the
irreducible coordination becomes their coalition and the other party is structurally decoupled.
Caveat: read on the major complex; a coupling sweep would test robustness beyond these three forms.
