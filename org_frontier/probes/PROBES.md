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

### Literature-inspired batch (from the Φ-on-social-systems dossier)

| 44 | Group-size transition (Niizato 2020) | A Niizato-style size discontinuity appears | **H44 partial** | The all-required pool's Φ rises with size (2,2,3,4 for n=2–5); the random triadic rate collapses (9.4%→2.3%→0%). Size strongly governs irreducibility, but the sharp 3→4 discontinuity Niizato found in fish-school Φ distributions is dynamics-specific, not reproduced here. `probe_group_size.py` |
| 45 | Φ vs MI / transfer entropy (Niizato contrast) | Φ separates what MI/TE miss | **H45 confirmed** | MI(W;C) ranges overlap across classes (triadic 0.006–0.281 vs dyadic 0.001–0.119); transfer entropy is worse — a dyadic back-channel form has the HIGHEST TE (0.54) of all. MI/TE measure dependence, not integration. Replicates Niizato's contrast on coordination forms (and this repo's proxy results). `probe_phi_vs_mi_te.py` |
| 46 | O-information (Rosas 2019) | Triadic = synergy-dominated | **H46 weak** | Means lean the right way (triadic O=−0.004, dyadic O=+0.012) but individual forms are mixed and near-zero — a dyadic back-channel form is strongly synergistic, a dyadic relay strongly redundant. O-information on the present-state joint does not cleanly separate the verdict. `probe_o_information.py` |
| 47 | ΦID atoms on a coordination series (white-space) | Triadic = more persistent synergy | **H47 supported, directional** | First application of ΦID to a coordination series (a gap the dossier flags). Triadic forms carry more persistent synergy (mean sts −0.072 vs −0.009 for dyadic). Directionally clean; not a perfect separator (estimated-measure degradation, cf. proxy_bridge). `probe_phiid_social.py` |
| 48 | Φ vs performance (Engel & Malone 2018) | Higher Φ → better coordination | **H48 null** | Spearman ρ(Φ, success-proxy) = +0.00; triadic and dyadic forms have identical mean success (0.50). Φ is orthogonal to the match-reaching proxy — being triadic is about the *kind* of coordination, not the *level* of success. Contrasts Engel-Malone's performance correlation; aligns with the dissertation (the triad demands a competency, it is not itself success) and with Probe 29. `probe_phi_performance.py` |
| 49 | Causal emergence (Hoel / Klein) | Triadic = more emergence, higher EI | **H49 nuanced** | Triadic forms show MORE causal emergence (0.16 vs 0.04) but LOWER raw effective information (1.93 vs 2.33). Emergence leans triadic; EI does not — a non-trivial relationship, partly contrasting emergence_vs_phi's random-net orthogonality. `probe_emergence.py` |
| 50 | Adversarial / anti-coordination | Irreducibility is valence-free | **H50 mostly confirmed** | Adversarial determinations (W⊕C, ¬(W∧C)) are triadic just like cooperative (W∧C); only the one-sided W∧¬C factors. Whether the parties' interests align does not bear on irreducibility — structure does. `probe_adversarial.py` |
| 51 | Team's irreducible subset (Watson) | The core is a proper subset of the team | **H51 confirmed** | A homogeneous pool integrates over all members; a heterogeneous team (tight triad + peripherals) integrates only over its tight subset {W,S,C1} — the core is a proper subset of the roster, matching Watson's subset-Φ. `probe_team_core.py` |
| 52 | Group vs members (List 2018) | Group Φ exceeds any member's | **H52 nuanced, refines List** | The 4-party pool's whole Φ (3.0) exceeds its best pair (2.0) — genuine group-level integration absent in the parts. But the 3-node triad's whole (2.0) equals its best pair (2.0) — no surplus. Group integration beyond members emerges at n≥4, not at the minimal triad. A precise answer to the List/Kramer debate. `probe_group_vs_members.py` |
| 53 | Dimension composition (integration claim) | Both dimensions individually necessary | **H53 confirmed** | The worker is bound (in the core, triadic) only with BOTH inference (reads S) and translation (intent reaches S); removing either drops her out. The construct is the composition of its dimensions, not either alone — the dissertation's integration claim, structurally. `probe_dimension_composition.py` |

### Program Wave 1 — formal core (agenda #44, #46, #47, #12, #13)

| 54 | Φ-free structural test (#44) | A graph predicate matches the verdict | **partial** | A connectivity predicate (S reads W and C; W and C read S) is NECESSARY (0 false negatives) but over-predicts (16 false positives), accuracy 0.938 over 256 forms. A purely connectivity-based Φ-free test is impossible; the function-level liveness Φ captures needs a pivotality term. `probe_phi_free_test.py` |
| 55 | Role-symmetry automorphism (#46) | W↔C swap preserves the verdict exactly | **confirmed** | 0/256 verdict flips and max |Φ−Φ_swapped| = 0.000000. Worker↔counterpart relabeling is an exact automorphism of the verdict, confirming Probe 22's behavioral symmetry as a structural identity. `probe_role_symmetry.py` |
| 56 | Pure higher-order binding (#47) | A triadic form can have no irreducible proper subset | **confirmed** | 8 of 24 triadic family forms are purely higher-order: whole Φ=0.5 with best-proper-subset Φ=0.0. These are the parity determinations — irreducibility appears only at the whole, with no lower-order seed. The 16 conjunctive forms are seeded (a pair already has Φ=2.0). `probe_pure_higher_order.py` |
| 57 | Mediator-chain invariance (#12) | Φ=2.0 at every chain depth, balanced MIP | **confirmed** | Chains k=1..4 (n=3..6) are all triadic with Φ exactly 2.0, the MIP a balanced two-part cut near the middle. Depth adds intermediaries but not integration; the chain has one irreducible bottleneck that lengthening neither factors nor raises. `probe_chain_theorem.py` |
| 58 | Tree (branching) mediation (#13) | Branching dilutes like breadth | **refuted** | Tree-mediation forms (a root joining two branch mediators) are triadic at Φ=2.0, like chains, not dyadic like breadth. Branching mediation PRESERVES the triad. What dilutes irreducibility is added *parties* with substitutability, not added mediator structure. `probe_trees.py` |

**Wave 1 reading.** Two formal results land: role-symmetry is an exact automorphism (#55), and pure
higher-order forms exist (#56) — the parity determinations bind synergistically with no irreducible
subset, the structural seed of the group-beyond-members result (Probe 52). #44 sharpens the
Φ-free-test question: connectivity is necessary but not sufficient, so an exact cheap test must encode
pivotality, not just edges. #58 refines the breadth/depth picture: mediator branching preserves the
triad (like depth); only substitutable parties dilute it.

### Program Wave 2 — robustness (agenda #6, #7, #9, #10, #16)

| 59 | Isomorphism invariance (#6) | Verdict invariant under the full relabeling group | **confirmed** | 0/384 verdict flips and 0 Φ difference across 8 forms × 6 node-permutations × 8 state-flips. The verdict is an exact invariant of the system up to relabeling; the state-individuation choice does not move it. (A first run had a relabeling bug, fixed.) `probe_individuation.py` |
| 60 | Temporal-grain threshold (#7) | A detectable band tied to the attractor period | **confirmed (short)** | The triadic corpus forms flip to dyadic at grain k=2, with attractor periods 1–2. For these short-period forms the detectable band is narrow; empirical sampling must be fine relative to the coordination's cycle (refines Probe 32). `probe_grain_threshold.py` |
| 61 | Shared exogenous shock (#9) | Correlated noise changes the verdict | **not shown (modeling limit)** | A static common source both parties read leaves the major complex the {W,S,C} triad (Φ=2.0) and stays out itself. A static shared input does not change the verdict. True correlated *output* noise needs a state-by-state TPM, which the state-by-node form cannot express; flagged. `probe_shared_shock.py` |
| 62 | Update scheduling (#10) | Verdict can depend on the update schedule | **confirmed, consequential** | Every triadic corpus form becomes DYADIC under sequential (one-node-at-a-time) update, for all 6 orders, while simultaneous update is triadic. The verdict is schedule-relative: within-step sequential composition lets information pass through in one step and collapses the joint determination. A modeling caveat alongside grain-relativity (Probe 32). `probe_async.py` |
| 63 | Bidirectionally-coupled regime (#16) | A two-way-coupled regime binds where the clock did not | **refuted** | A regime that switches the rule and is read into it does not join the core; the switching destabilizes the worker out (core {S,C}), as the outcome-tracking regime did in Probe 3. Temporal-tracking is not structural even with bidirectional coupling — the switch itself disrupts. `probe_lifted_regime.py` |

**Wave 2 reading.** The verdict is an exact relabeling invariant (#59) but **relative to two modeling
choices that must be stated**: the observation grain (#60, Probe 32) and the update schedule (#62,
new). Sequential update collapses the triad, so the synchronous-update assumption is load-bearing.
Temporal-tracking stays non-structural even when the regime is coupled both ways (#63), and structured
noise as a static shared source does not move the verdict (#61), with true correlated output noise
flagged as needing a state-by-state representation.

### Program Wave 3 — structure & aggregation (agenda #14, #15, #33, #49, #48)

| 64 | Core from the graph (#14) | A connectivity rule predicts the major complex | **partial** | Over 300 n=4 forms the bidirectional-coupling rule has recall 1.000 (never misses a core node — coupling is necessary, cf. Probe 12) but precision 0.543 (over-predicts), exact core-set match 33.3%. The core is not predictable graph-only; coupling gives a superset, and the rest is the holistic residual. `probe_team_core_rule.py` |
| 65 | Group surplus by size (#15) | Whole-Φ-beyond-members emerges with n | **confirmed, mapped** | All-required pool: surplus (whole Φ − best proper-subset Φ) is 0.0 at n=3, +1.0 at n=4, +1.0 at n=5. Group-level integration beyond the members appears at n≥4, not at the minimal triad (sharpens Probe 52). `probe_group_surplus.py` |
| 66 | Coalition size vs principal (#33) | A larger coalition still wins | **confirmed** | The counterpart coalition is the core at k=2 (n=5, core {C1,C2}) and k=3 (n=6, core {C1,C2,C3}, Φ=6.0), ejecting the active gating+monitoring principal both times. Solidarity dominates principal control regardless of coalition size (extends Probe 37). `probe_coalition_size.py` |
| 67 | Voting/aggregation rules (#49) | Which rules make a triadic collective decision | **clean, novel** | Unanimity (AND) and any-suffices (OR) bind all members (triadic, Φ=3.0); **majority (2-of-3) factors to dyadic** (no member pivotal); veto reduces to the vetoer (dyadic, core {W}); parity binds weakly (Φ=0.25). A majority-rule body is structurally not an irreducible collective. `probe_voting.py` |
| 68 | Market clearinghouse (#48) | A clearinghouse is triadic, a price-poster dyadic | **confirmed, new domain** | A clearinghouse jointly matching a buyer and seller is triadic (Φ=2.0, core {B,S,Se}); a one-way price-poster is a conveyor and factors (core {Se}); substitutable buyers (either clears) dilute to dyadic; an all-required two-buyer clear is triadic (Φ=3.0). The framework extends to markets. `probe_market.py` |

**Wave 3 reading.** The framework reaches two new domains with crisp verdicts. Governance (#67):
unanimity binds an irreducible collective, but **majority rule factors** — a majority body is not, by
this measure, a single irreducible decider. Markets (#68): a clearinghouse that jointly matches is
triadic, a price-poster is a conveyor, and substitutable buyers dilute, exactly as the
substitutability law predicts. Structurally, #65 maps the group-surplus onset to n≥4, #66 shows
solidarity beats the principal at every coalition size, and #64 confirms the core is a connectivity
*superset* but not graph-predictable (the holistic residual again).

### Program Wave 4 — dimensions & neighbors (agenda #25, #26, #27, #28, #29)

| 69 | Model fidelity vs displacement (#25) | A better model displaces the counterpart more | **confirmed** | With the worker acting on its model (W'=S∧M), the counterpart stays in the core at dead/static/lagged fidelity but is displaced at FULL fidelity (M'=S → core {W,S,M}, C out). Displacement strengthens with model fidelity (extends Probes 4/9). `probe_model_fidelity.py` |
| 70 | AI-MC boundary by timescale (#26) | A timescale criterion recovers the AI-MC distinction | **refuted, clarifying** | Absorbing the AI into the worker does NOT flip the Φ verdict: the 2-element W–C loop is still irreducible (Φ=2.0). The discriminator is the major-complex ELEMENT COUNT (2 vs 3), not Φ>0. "Triadic" in the construct must mean an irreducible complex with a genuine third party — sharpening Probe 20: AI-MC vs algorithmacy is a counting/boundary question the scalar verdict cannot settle. `probe_aimc_boundary.py` |
| 71 | Second-order theory of mind (#27) | A used second model joins the core | **confirmed** | The second-order model M2 stays a sink when unused (core {W,S,M1}, M2 out); it joins the core only when the worker acts on it (W reads M2 → core all five). Recursive mentalizing is structural only when used, else a worker burden — the acted-on/bidirectional principle again. `probe_second_order_tom.py` |
| 72 | Sensemaking family (#28) | Internal-process sensemaking is dyadic | **confirmed** | All three internal-process forms are dyadic. A process inside the worker that interprets the system, with no third party jointly committed, is dyadic across the family — sensemaking is a worker-side construct, not algorithmacy (extends Probe 31). `probe_sensemaking.py` |
| 73 | Multi-role agents (#29) | The two coordinations stay separate | **confirmed** | An agent who is worker on one platform and counterpart on another has a single triad as its major complex ({X,S1,C1}), not a merged five-element whole. Sharing one agent does not fuse two coordinations into one irreducible structure. `probe_multirole.py` |

### Program Wave 5 — political economy (agenda #30, #31, #32, #34, #35)

| 74 | Generic {S,P} core? (#30) | The platform-and-owner core is generic | **refuted (rare regime)** | Over the 16 principal-coupling forms, the core is {S,P} (both parties ejected) in only 1 (6%), at maximum coupling (S gates P, P reads all). The platform-and-owner core is a high-coupling regime, not the default. `probe_principal_regime.py` |
| 75 | Control, exposure, value capture (#31) | Structure predicts who captures surplus | **partial** | A Φ-free leverage proxy (control = the commit's sensitivity to a party; exposure = the party's sensitivity to the commit) is computable. In balanced triads every party is "captured" (exposure 1.0 > control 0.25–0.5), including a symmetric principal — differential capture needs an asymmetric/extractive commit (see #35). `probe_value_capture.py` |
| 76 | The regulator node (#32) | Effective oversight must join the core | **confirmed** | A read-only observer and a static veto stay out of the core; only a regulator that both vetoes the commit and responds to outcomes joins it. Toothless oversight (observe-only) is structurally outside the coordination it oversees — the acted-on/bidirectional principle for oversight. `probe_regulator.py` |
| 77 | Observability asymmetry (#34) | The asymmetry is necessary for the triad | **partial** | The Φ-maximal triad sits at S-reads-both / no-direct-channel (Φ=2.0). But a symmetric direct W↔C channel only grades Φ down (2.0→0.83) without collapsing, and S-reads-one + a channel is triadic at Φ=1.0. The asymmetry maximizes integration but is not strictly necessary; reading only one party is dyadic. `probe_info_asymmetry.py` |
| 78 | Fairness signature (#35) | Extractive commits carry a distinct signature | **confirmed** | A balanced commit keeps the parties in the core ({W,S,C}, P out); as the commit tilts toward the principal (P can force it) the parties are ejected and the core becomes {S,P}; a fully extractive commit (S follows P) leaves {S,P}. An extractive determination structurally excludes the parties from the irreducible coordination. `probe_fairness.py` |

### Program Wave 6 — dynamics (agenda #17, #18, #19, #43, #38)

| 79 | Adaptive mediator's verdict path (#17) | An adapting mediator traces a verdict path | **confirmed** | As the mediator's reliance on the counterpart degrades over epochs (r: 1.0→0.0), Φ falls 2.0→0.71→0.44→0.20→0.0 and the verdict crosses from triadic to dyadic at the final epoch. The form's kind is not fixed; it moves as the mediator adapts (a learning analogue of Probe 38). `probe_adaptive.py` |
| 80 | Φ vs success over learning (#18) | Training for success raises Φ | **refuted** | Across worker policies ordered by coordination success, Φ is non-monotone: a cautious policy at 0.12 success has Φ=2.0, while persistent/eager policies at 0.38 success have Φ=0. Climbing in success need not climb in Φ — success is the level, Φ is the kind (confirms Probe 48). `probe_learning.py` |
| 81 | Criticality / interior Φ peak (#19) | Φ peaks at intermediate coupling | **refuted (trough, not peak)** | Sweeping the parties' tracking phase p, Φ is symmetric: 2.0 at both deterministic extremes (in-phase p=1 and anti-phase p=0) and 0 at random tracking (p=0.5). Φ tracks coupling determinism, not phase sign; the interior point is a trough. No critical interior maximum (matches Probes 27, 38). `probe_criticality.py` |
| 82 | Non-collapsing Niizato size jump (#43) | A size-four Φ rise appears under richer dynamics | **refuted (opposite)** | Under all-to-all noisy majority coupling, max Φ peaks at n=3 (3.47) and falls — n=2:1.37, n=3:3.47, n=4:0.95, n=5:0.0. No Niizato-style rise at n=4; added members make the consensus more redundant and less integrated, so the size dependence runs the other way for this dynamics. `probe_noncollapse.py` |
| 83 | O-information on transitions (#38) | Transition O-info separates better than present-state | **partial** | Across 16 triadic and 16 dyadic corpus forms, present-state O-info gives no group gap (0.0). The present⊕next transition joint opens a gap of 0.25 (triadic 0.36 > dyadic 0.10, more redundancy-dominated). The transition structure carries discriminating synergy the static joint misses, but the gap is modest — a partial gain over Probe 46, not a clean separator. `probe_transition_oinfo.py` |

### Program Wave 7 — estimation and the data bridge (agenda #20, #21, #22, #23, #50)

| 84 | Barrett–Seth Φ_AR proxy (#20) | Φ_AR recovers the verdict better than Φ_R/Φ_WMS | **confirmed (recovers it)** | An autoregressive Φ_AR (min over bipartitions of summed-part minus whole residual entropy), fit to noisy trajectories, separates exact-triadic from exact-dyadic at rank-AUC 0.925 (triadic mean 0.60 vs dyadic 0.16). Where Φ_R/Φ_WMS failed, the AR proxy recovers most of the verdict from time series. `probe_phi_ar.py` |
| 85 | Learned surrogate over cheap features (#21) | A feature-combiner recovers the verdict | **confirmed (perfectly)** | A random forest over 13 cheap time-series features (per-node entropy, pairwise MI, transfer entropy, O-information) recovers the verdict at 5-fold CV accuracy 1.000 and ROC-AUC 1.000, against a 0.906 majority-class baseline. No single proxy works; the combination is a complete fingerprint. `probe_learned_surrogate.py` |
| 86 | Trajectory length (#22) | Longer trajectories never recover the missed Φ_R verdict | **confirmed** | Sweeping length 1k→64k, the triadic−dyadic Φ_R gap stays ~0.04–0.08 and never grows toward the exact gap (~2.0). Φ_R's failure is structural, not a finite-sample artifact — more data does not fix it. `probe_phiid_length.py` |
| 87 | Redundancy lattice and noise (#23) | MMI/CCS or noise changes ΦID separation | **confirmed (no rescue)** | Across MMI and CCS redundancy at noise 0.05/0.15, the Φ_R group gap stays small (0.04–0.07) in every cell and collapses toward zero at high noise. Neither the lattice nor the noise level is why ΦID misses the verdict — the limitation is the measure. `probe_phiid_sweep.py` |
| 88 | Multi-agent-AI protocol (#50) | An AI-agent protocol is dyadic or triadic by design | **confirmed** | A relay protocol (P forwards A1 to A2) and a broadcast protocol are dyadic (Φ=0); a joint-commit protocol whose state both agents determine and act on (P=A1∧A2, both read P) is triadic (Φ=2.0, core {A1,P,A2}). AI-agent coordination sits on the same conveyor-vs-committing-third-party cut as human coordination. `probe_mas.py` |

### Program Wave 8 — consilience of measures (agenda #36, #37, #39, #2, #1)

| 89 | Consilience map (#36) | Adjacent measures agree on clear cases, diverge mappably | **confirmed** | Over the 256 family (24 triadic), each measure's best single threshold agrees with the verdict only partly: EI and causal emergence default to all-dyadic (0.906), O-info catches 1/24, Φ_R catches 7/24 (2 false positives), Φ_AR catches 9/24 at 0 false positives (0.941). No scalar reproduces the verdict at one threshold; the divergence is structured (panel cached). `probe_consilience.py` |
| 90 | Cheap-measure search (#37) | No single cheap measure cleanly separates the verdict | **confirmed** | Ranking each measure by rank-AUC against the verdict: Φ_AR 0.959, causal emergence 0.661, EI 0.655, Φ_R 0.593, O-info 0.464. The autoregressive Φ_AR is the strongest single proxy but none reaches the perfect separation a learned feature combination gives (Probe 85). `probe_cheap_search.py` |
| 91 | EI / causal emergence across the family (#39) | The EI–Φ link from Probe 49 generalizes | **partial** | corr(EI, exact Φ) across the family is +0.164 — weakly positive. Triadic forms carry more effective information (mean EI 1.87 vs 1.50) and slightly more causal emergence (0.126 vs 0.074). EI tracks integration weakly across the whole family, less tightly than the few-form Probe 49 suggested. `probe_ei_family.py` |
| 92 | Joint-influence (synergy) term (#1) | A pairwise synergy feature lifts the family AUC toward 0.89 | **refuted** | Adding an explicit interaction/synergy feature to marginal out-influence gives a CV-AUC of 0.695 vs 0.690 for marginal alone — a +0.005 lift. The gap from ~0.69 to the controlled 0.89 is not closed by a pairwise synergy term (consistent with Probe 13's null). Marginal influence already carries what this feature would add. `probe_joint_influence_v2.py` |
| 93 | CES counts predict the verdict (#2) | Distinction/relation counts predict triadicity | **confirmed (perfectly)** | Cause-effect-structure counts from phi_structure separate the verdict: n_distinctions AUC 0.920, mean_order 0.897, n_relations 0.867, frac_higher_order 0.833; a combined logistic model reaches CV-AUC 1.000. The higher-order structure carries the verdict where per-node influence (#1, 0.69) cannot — an irreducible third party shows up as higher-order CES. `probe_ces_predictor.py` |

### Program Wave 9 — heavy enumerations and scaling (agenda #45, #4, #3, #11, #40)

| 94 | N&S structural condition for n=3 (#45) | Connectivity exactly decides triadicity | **refuted (almost)** | Over all 4096 arbitrary 3-node wirings (55.9% triadic), structural features (edge count, bidirectional-node count, strong connectivity) reach 92.97% — not 100%. The mined rule is essentially "all three nodes bidirectionally coupled"; that condition is necessary and ~93% sufficient. The ~7% residual is decided by the Boolean function content, so there is no purely-graph N&S condition — sharpening the two-condition account (coupling necessary, pivotality function-dependent). `probe_ns_theorem.py` |
| 95 | n=4 census (#4) | Low triadic rate, triadic forms near the edge floor | **confirmed** | Large-sampling the n=4 strict-mediation family (N=3000): triadic rate 2.4% (vs 9.4% at n=3). Every triadic form sits at exactly the 2(n−1)=6 edge floor (min=mean=6); dyadic forms average 4.3 edges. Irreducible n=4 coordination is sparse and maximally lean. `probe_n4_census.py` |
| 96 | Edge floor at n=5, n=6 (#3) | The 2(n−1) edge floor is tight as size grows | **confirmed (n=5)** | At n=5 the leanest triadic form has exactly 8 edges = 2(n−1) (2 triadic in 300, both at the floor). At n=6 no triadic form appeared in 150 samples, so the floor could not be bounded there. The bidirectional-coupling floor is tight at every size it can be measured. `probe_min_triad_n56.py` |
| 97 | Triadic rate past n=5 (#11) | The rate floors at a small positive value | **refuted (vanishes)** | The strict-mediation triadic rate falls 9.4% (n=3) → 2.4% (n=4) → 0.67% (n=5) → 0/300 ≈ 0% (n=6). It does not floor at a positive rate; irreducible coordination through a single mediator effectively disappears as the group grows. A single mediator cannot sustain triadicity at scale. `probe_scale_n6.py` |
| 98 | Agent-based difficulty (#40) | The verdict tracks independent-learner coordination difficulty | **refuted** | Two independent Q-learning bandits coordinating to hit each form's commit show no verdict signal: triadic mean difficulty 68.4 vs dyadic 76.8, rank-AUC 0.567. Coordination hardness for selfish learners and irreducibility of the form are different things — the structural verdict is not a behavioral-difficulty measure. `probe_abm_difficulty.py` |

### Program v2 Wave V1 — the estimation frontier (A1, A2, A3, A4)

| 99 | Surrogate transfer across scale (A1) | A cheap model trained on n=3 predicts the verdict at larger n | **confirmed** | Eight size-invariant aggregate features (mean/min/max over nodes and pairs of entropy, MI, TE, plus full-joint O-information), random forest trained on the 256 n=3 forms (CV-AUC 1.000), transfers to n=4 at AUC 0.984 (10 triadic in 400) and n=5 at 0.983 (2 triadic — noisy). A surrogate fit on cheap small forms ranks the verdict at sizes where exact Φ is costly. `probe_surrogate_transfer.py` |
| 100 | Minimal feature set (A2) | Two or three features carry the perfect recovery | **confirmed (one feature)** | Greedy forward selection reaches CV-AUC 1.000 with a single feature — one party's marginal entropy H[C] (H[W] equivalent by the role-symmetry automorphism #55). The verdict's cheap fingerprint on the corpus is essentially party liveness; single-feature rank-AUC was 0.81 (the RF uses a non-monotone band). Corpus-specific to strict mediation; the aggregate features transfer (#99). `probe_minimal_features.py` |
| 101 | Φ_AR failure mode (A3) | Φ_AR's misses are the parity / pure-higher-order forms | **partial** | The parity triadic forms (Φ=0.5) score lower under Φ_AR (mean 0.457, mean rank 41.5) than the conjunctive triadic forms (0.655, rank 10.8) but still above dyadic (0.136, rank 138.5). The linear-AR proxy partly sees the synergistic forms, so they are a partial blind spot, not a total one. `probe_phi_ar_failure.py` |
| 102 | Exact cheap-CES predicate (A4) | A single CES count is an exact verdict equivalent | **refuted (clean residual)** | No single-count threshold gives zero error. The best predicates (n_distinctions ≥ 3, frac_higher_order > 0, max_order ≥ 2) each have 8 errors, all false negatives, all on the same 8 parity / pure-higher-order forms (#56); no predicate ever produces a false positive. CES counts rank the verdict but do not define it — the parity forms have minimal cause-effect structure despite being triadic. `probe_ces_predicate.py` |

### Program v2 Wave V2 — topology and scaling (B1, B2, B3)

| 103 | Distributed vs single mediation at scale (B1) | Two linked mediators sustain a larger core than one hub | **refuted** | At n=6 and n=7 the single all-required hub holds the whole group in one core (Φ=5 core 6 at n=6; Φ=6 core 7 at n=7); the two-hub form keeps a smaller core (4, then 5) at lower Φ (3, 4) — one party-group drops out. Distributing the mediation fragments the coordination rather than scaling it. What scales a large irreducible group is one all-demanding commit, not splitting the mediator. **(Revised by #118: this fragmentation is an artifact of the asymmetric build; a symmetric two-hub keeps the full core at higher Φ.)** `probe_distributed_mediators.py` |
| 104 | Topology map (B2) | Topology classes differ in whether and how fast Φ grows | **confirmed** | At n=4→5, all four conjunctive topologies stay triadic but scale Φ differently: chain flat at 2.0 (fixed bottleneck, matches #57), single-hub and two-hub +1.0 per added member, all-to-all pool 12→20 (+8.0). Topology, not size, sets the scaling rate — serial mediation keeps one bottleneck while all-to-all coupling compounds. `probe_topology_map.py` |
| 105 | Lean triad at n=6 (B3) | A lean triadic n=6 form exists despite 0/300 random | **confirmed** | The conjunctive single-hub form is triadic at every size with the full node set as its core and Φ = n−1: n=4 Φ=3, n=5 Φ=4, n=6 Φ=5, each at the 2(n−1) edge floor. Probe 97's 0/300 means triadic n=6 forms are vanishingly rare under random function fills, not absent — the all-required commit is the surviving triadic structure at scale. `probe_lean_n6.py` |

### Program v2 Wave V3 — the N&S residual and the behavioral gap (C1, D1, D2, D3)

| 106 | Non-separability as the N&S residual (C1) | Connectivity + synergy is an exact condition | **refuted** | Over the 4096 wirings, connectivity+synergy reaches 92.97% — identical to connectivity alone; the per-function interaction term lifts nothing. The 7% the graph cannot decide is not a non-separability feature; it is genuinely holistic (per-node/per-function features have a ceiling, as Probe 13 found). No exact structural N&S condition for n=3 triadicity. `probe_nonseparability.py` |
| 107 | Partner-modeling agents (D1) | Theory-of-mind agents show the difficulty gap | **refuted** | Fictitious-play learners that best-respond to the partner's observed action distribution show rank-AUC 0.541 (triadic mean difficulty 66.6 vs dyadic 77.4) — no better than independent bandits (Probe 98, 0.567). The verdict is not a coordination-game-difficulty measure for any agent model tried; irreducibility and learning-to-coordinate are different things. `probe_tom_agents.py` |
| 108 | Resilience (D2) | Φ tracks recovery from perturbation | **partial (weak)** | Triadic forms take longer to recover from a flipped node (7.08 vs 5.17 steps) but rank-AUC is only 0.618 — a weak directional signal, not a clean tracker. Φ is closer to orthogonal here than to predictive; resilience leans the expected way but does not carry the verdict. `probe_resilience.py` |
| 109 | Hysteresis (D3) | Rebinding an ejected party is path-dependent | **confirmed** | A sticky mediator produces a hysteresis loop in coordination as the engagement drive is ramped up then down (loop area 0.071); a memoryless mediator does not (0.005, up and down legs coincide). With memory, a coordination latches and stays alive as engagement falls, so re-including a party is not the mirror of dropping it — the dynamical face of Probe 43. `probe_hysteresis.py` |

### Program v2 Wave V4 — political economy and instrument hardening (E1, E2, F1)

| 110 | Ejection order (E1) | Parties drop in a fixed order as the commit tilts | **confirmed, nuanced** | Sweeping the principal's weight in a threshold commit (S=1 iff W+C+w_P·P ≥ 2): w_P=0 gives the balanced core {W,S,C}; w_P=1 (the 2-of-3 majority) factors entirely — no irreducible core, the majority-rule null of #10/#67; w_P≥2 gives the extractive {S,P}. The worker and counterpart drop together (symmetric, #55) and the principal enters, but the path passes through a factored regime rather than an all-four core. `probe_ejection_order.py` |
| 111 | Regulator coalition (E2) | Two weak regulators jointly bind where one does not | **confirmed** | One observe-only regulator stays out (core {W,S,C}); a second observe-only regulator also stays out (still {W,S,C}); only when both regulators' approval gates the commit do they enter (core {W,S,C,R1,R2}, Φ=4.0). Number does not rescue observe-only oversight — a watchdog without a lever is a sink at any count; joint gating is the coalition analogue of veto+responsive (Probes 76, 66). `probe_regulator_coalition.py` |
| 112 | Modeling-invariant verdict (F1) | An aggregate verdict is robust to grain and schedule | **confirmed (no invariant)** | Of 24 canonically-triadic forms, grain-1 synchronous keeps all 24; grain-2 keeps 0; sequential update keeps 0; an across-condition majority keeps 0. Coarse grain (#32) and sequential update (#62) both call triadic forms dyadic, so aggregating destroys the verdict. There is no modeling-free invariant — the verdict must be reported at the finest grain with synchronous update, and that convention declared. Robustness is a declaration, not a result. `probe_invariant_verdict.py` |

**Wave V4 reading.** Two political-economy results sharpen Wave 5, and the instrument question resolves
cleanly. The tilt from a balanced to an extractive commit is not a smooth slide: it passes through a
factored regime at the 2-of-3 majority point before settling on the {S,P} extractive core, and the two
parties leave together by role symmetry (#110). Oversight does not scale by count — observe-only
regulators are sinks whether one or two; only joint gating binds them (#111), the coalition form of the
veto+responsive condition. And the verdict has no modeling-free invariant: grain and update schedule each
flip every triadic form to dyadic, so an aggregate vote calls them all dyadic (#112). The instrument is
exact, but only relative to a stated grain and a synchronous schedule — that convention is part of the
measurement, not a defect to average away.

### Program v3 Wave W1 — the parity blind spot (G1, G2, G3)

| 113 | What the parity forms are (G1) | The blind spot is exactly the XOR-family commits | **confirmed** | Among the 24 triadic corpus forms, the 8 with a parity (XOR/XNOR) commit all carry Φ=0.5 and the 16 with a conjunctive commit all carry Φ=2.0. The pure-higher-order forms (#56) that Φ_AR (#101) and every CES predicate (#102) miss are precisely the parity determinations. `probe_parity_characterization.py` |
| 114 | The parity detector (G2) | A cheap feature separates parity-triadic from dyadic | **confirmed** | Of the 13 cheap features, MI[W;C] ranks parity-triadic against dyadic at AUC 0.931, close to its 0.948 on conjunctive-triadic. Party coupling is the signal. The magnitude proxies miss parity because parity Φ is tiny; the coupling between the parties stays normal, which is how the learned surrogate (#85) recovers these forms. `probe_parity_detector.py` |
| 115 | How parity scales (G3) | The parity family scales differently from the conjunctive hub | **confirmed** | The XOR hub stays triadic with the full node set as its core at every size, while Φ halves each step: 0.5 at n=3, 0.25 at n=4, 0.125 at n=5 (Φ = 2^(2−n)). The conjunctive hub grows the other way, Φ = n−1. Two routes bind the whole group; one strengthens with size, one fades toward zero. `probe_parity_scaling.py` |

**Wave W1 reading.** The cheap-measure blind spot has a single identity. The eight forms that Φ_AR and
the CES counts miss are the XOR-family commits, the Φ=0.5 pure-higher-order forms (#113). Their Φ is tiny,
so any magnitude-based proxy under-ranks them, yet the mutual information between the two parties stays as
high as in the conjunctive forms (#114). That is why a learned model built on coupling features recovers
them while a magnitude proxy cannot, and it locates the blind spot precisely: it belongs to proxies that
track Φ size, and it disappears for features that track party coupling. The scaling result is the sharper
find (#115). Two commit families both hold the whole group in one irreducible core, and they scale in
opposite directions. The conjunctive hub grows stronger with size at Φ = n−1; the parity hub fades at
Φ = 2^(2−n), irreducible at every size and ever closer to nothing. Binding everyone through a shared
all-or-nothing demand compounds; binding everyone through a parity check thins out as the group grows.

### Program v3 Wave W2 — the all-required scaling law (H1, H2, H3)

| 116 | The conjunctive law (H1) | Φ = n−1 holds and OR scales like AND | **confirmed** | The AND-all hub holds the full node set as its core with Φ = n−1 at n=4,5,6,7 (Φ = 3,4,5,6); the OR-all hub matches exactly at n=4,5,6. The law is verified across four sizes (n=8 exact SIA does not finish in reasonable time, so the check stops at n=7). An all-required commit binds every member into one irreducible whole whose Φ grows one bit per added member. `probe_conjunctive_law.py` |
| 117 | Threshold commits (H2) | Only extreme thresholds keep the full core | **confirmed** | Across the k-of-n threshold commits at n=4 and n=5, the full core survives only at the extremes: OR (k=1) and AND (k=all), both at Φ = n−1. Every intermediate threshold (2-of-3, 2-of-4, 3-of-4) factors to a dyadic verdict with no irreducible core. Whole-group irreducibility needs an all-or-nothing commit; a genuine threshold leaves no member pivotal enough to stay bound (extends #10, #67). `probe_threshold_scaling.py` |
| 118 | Symmetric vs asymmetric multi-hub (H3) | The two-hub fragmentation was an asymmetry artifact | **confirmed (revises #103)** | A symmetric two-hub (both hubs read all parties and each other; each party reads both hubs) holds the full core at higher Φ than the single hub: Φ=8 vs 5 at n=6, Φ=10 vs 6 at n=7. The asymmetric two-hub of #103 dropped a party-group (core 4, 5). Distributed mediation scales integration above a single hub when symmetric; the earlier fragmentation came from the asymmetric build, where one group reached the rest through a longer path. `probe_symmetric_multihub.py` |

**Wave W2 reading.** The all-required commit is a scaling law with one strict condition, and distributed
mediation is rehabilitated. Φ = n−1 holds for the AND-all hub across every size checked, and OR-all
matches it (#116), so an all-or-nothing commit binds the whole group into one irreducible core whose
integration grows a bit per member. The condition is sharp: only the two extreme thresholds keep the full
core, and every majority-style threshold in between factors the group apart (#117). The Wave V2 reading
that splitting mediation fragments the coordination held only for the asymmetric build. A symmetric
two-hub keeps the full core at Φ above the single hub (#118), so multiple mediators integrate a large
group more when each sees everyone. The org-design picture sharpens accordingly: hold a whole group
together with an all-or-nothing demand, and add symmetric mediators to raise integration rather than to
shed it.

### Program v4 Wave X1 — the geometry of the scaling laws (J1, J3, L1)

| 119 | Multi-hub Φ law (J1) | Φ rises with mediator count toward the all-to-all pool | **confirmed, nuanced** | A symmetric m-hub at fixed n raises Φ as m grows: at n=6, Φ = 5, 8, 12, 20, 30 for m = 1..5, reaching the pool value when nearly every node is a mediator. Core membership is non-monotone, though: the full core holds at the extremes (single hub, near-pool) while intermediate hub counts (m=3,4 at n=6) raise Φ yet drop members. More mediators means more integration; keeping everyone in the core needs an extreme. `probe_multihub_law.py` |
| 120 | Parity dissolution size (J3) | The parity hub fades below any floor at a computable size | **confirmed** | Φ = 2^(2−n) holds exactly at n=3..7 (0.5, 0.25, 0.125, 0.0625, 0.03125). The law puts Φ below 1e−6 at n > 21.9, so the parity hub is numerically dyadic from n=22. XOR coordination is irreducible at every size in exact arithmetic and undetectable past about two dozen members. `probe_parity_dissolution.py` |
| 121 | Control structures by type (L1) | Everyday controls are conjunctive, parity controls are rare | **confirmed** | Dual authorization (W∧C) and escalation (W∨C) are conjunctive triads at Φ=2; allocate-to-exactly-one (XOR) and require-agreement (XNOR) are parity triads at Φ=0.5; a unilateral directive is dyadic. The familiar controls are the robust conjunctive kind that scales by the n−1 law (#116); the fragile parity kind (#115) is the exception, which is why the parity blind spot seldom bites real coordination. `probe_control_structures.py` |

**Wave X1 reading.** The two scaling laws acquire a geometry and a real-world reading. Spreading mediation
across more symmetric hubs raises Φ all the way to the all-to-all pool, so the most integrated arrangement
is one where nearly every node mediates (#119). That rise hides a non-monotone catch: intermediate hub
counts raise total Φ while dropping members from the core, so maximal integration and full membership are
distinct goals that coincide only at the extremes. The parity law gets a horizon: Φ = 2^(2−n) holds
exactly through n=7 and falls below any measurement floor near two dozen members (#120), so XOR
coordination cannot hold a large group in any detectable sense. The org reading lands the parity result
where it matters. The controls organizations actually run — dual authorization, escalation — are
conjunctive and scale robustly; the parity structures that fade are the exotic ones, allocate-to-one and
require-agreement (#121). The fragile family is rare in practice, and the robust family is the default.

### Program v4 Wave X2 — the cheap instrument, hardened (K1, K2, K3)

| 122 | Single coupling feature transfers (K1) | Mean pairwise MI transfers across size | **confirmed** | Mean pairwise mutual information alone ranks the verdict at AUC 0.942 at n=3, 0.947 at n=4, and 0.962 at n=5 (n=5 has one triadic, so its number is noisy). The cheap instrument reduces to one quantity — the mutual information between coordinating parties — and it carries across sizes the exact computation cannot reach, close to the eight-feature surrogate (#99). `probe_coupling_transfer.py` |
| 123 | Out-of-distribution generalization (K2) | The surrogate generalizes to new topology families | **refuted** | The n=3 strict-mediation surrogate scores 8/20 (40%) on families it never trained on. Hub-shaped forms that resemble the training family pass (single-hub, OR-hub); chains, pools, and multi-hub forms fail. The transfer of #99 holds across size within a topology family, and it does not hold across topology. The instrument must be trained on the structural class it is applied to. `probe_ood_surrogate.py` |
| 124 | Hybrid exact predicate (K3) | CES-or-coupling is an exact cheap test | **refuted** | The CES higher-order flag misses the 8 parity forms (fp=0, fn=8); adding an MI[W;C] threshold lowers nothing to zero — dyadic back-channel forms (#45, #46) carry high party coupling, so a hard MI cut false-positives them. MI ranks the verdict well (#122) yet does not separate it cleanly, so only a learned combination is exact (#85). The verdict resists an exact cheap definition (reaffirms #13, #106). `probe_hybrid_predicate.py` |

**Wave X2 reading.** The cheap instrument is powerful and bounded, and the boundary is now drawn. Within
the strict-mediation family it collapses to one number: mean pairwise mutual information ranks the verdict
at AUC ~0.95 and transfers across size (#122). Two limits hold it in. It does not transfer across topology
— a surrogate trained on strict mediation scores at chance on chains, pools, and multi-hub forms (#123),
so the instrument is family-specific and must be trained on the structural class it will read. And no hard
cheap threshold defines the verdict: coupling ranks it but dyadic back-channel forms carry high coupling
too, so an exact test needs the learned combination, not a single cut (#124). The practical shape of the
instrument follows: a coupling-based screen, trained on the topology it will face, read as a ranked
likelihood rather than a definition.

### Program v5 Wave Y1 — the holistic residual (M1, M2, M3)

| 125 | Residual characterization (M1) | The misclassified wirings share a dynamical signature | **confirmed** | Under the connectivity rule (n_bidir==3 ⇒ triadic), the residual is 288 forms, all false positives — 3-bidirectionally coupled yet dyadic, with zero false negatives. So all-three coupling is necessary and not sufficient. The residual forms collapse fast to a fixed point (mean max-period 1.08 vs 2.32 for the rest) and are never invertible. There is a dynamical signature connectivity does not see. `probe_residual_characterization.py` |
| 126 | Cheap-feature ceiling (M2) | No cheap panel reaches 100% | **confirmed** | A random forest on the full 10-feature panel (connectivity, synergy, global dynamics) reaches 95.2% 5-fold CV accuracy, short of perfect. Top features are n_bidir, strong connectivity, and reachable-set size. Even with dynamics added, the verdict is not defined by cheap features; about 5% stays irreducibly holistic, a property of the whole cause-effect structure (confirms #13, #106). `probe_residual_ceiling.py` |
| 127 | Dynamics ablation (M3) | Global dynamics adds nothing beyond connectivity and synergy | **refuted (it helps)** | Decision-tree accuracy is 0.9297 for connectivity, 0.9297 with synergy added (no lift, matching #106), and 0.9590 with global dynamics added (+0.029). Attractor structure — reachability and period — carries part of the residual that the graph and the function tables miss, closing roughly half of the 7% gap. The rest remains beyond cheap features. `probe_dynamics_ablation.py` |

**Wave Y1 reading.** The standing edge gives ground, partly. The residual is one-sided: every misclassified
wiring is a false positive, three-way coupled yet dyadic, so bidirectional coupling is a clean necessary
condition with no exceptions (#125). Those false-positive forms carry a dynamical tell — they collapse to a
fixed point in one step and never run an invertible map — and feeding global-dynamics features to the
classifier lifts accuracy by about three points where per-function synergy lifted nothing (#127). The win
stops there. The full cheap panel tops out near 95% (#126), so dynamics closes about half the 7% and the
rest stays holistic. The verdict's last few percent live in the whole cause-effect structure, reachable by
the exact partition and by no summary of the graph, the functions, or the coarse dynamics.

### Program v5 Wave Y2 — following v4's surprises (N1, N2)

| 128 | Intermediate-hub drop (N1) | The dropped members are the peripheral parties | **confirmed** | At the intermediate hub counts where the core is not full (#119), every hub stays in the core and the parties drop: n=6 m=3 gives core {H0,H1,H2,P2} with P0,P1 out; n=6 m=4 gives the four hubs plus one party. The hub cluster carries the integration once it is large enough and the peripheral parties lose their pivotal hold — a center-periphery effect, which explains why the core refills only at the symmetric extremes. `probe_intermediate_hub.py` |
| 129 | Mixed-topology surrogate (N2) | Diverse training fixes the family-specificity | **partial** | Training on strict mediation plus random arbitrary wirings lifts held-out archetype accuracy from 45% to 60%, but both sit below the 85% majority-triadic baseline. Mixing topologies broadens the signal without reaching cross-topology generalization; the cheap features carry a family-specific verdict signal that diverse data only partly widens. The screen stays family-bound (tempers, does not overturn, #123). `probe_mixed_topology_surrogate.py` |

**Wave Y2 reading.** Two v4 surprises resolve, one cleanly and one only partway. The non-monotone core of
the multi-hub law is a center-periphery effect: at intermediate mediator counts the hubs hold the core and
the parties fall out, so full membership returns only when the structure is symmetric at either extreme
(#128). The family-specificity of the cheap surrogate is softer than #123 made it look but not gone.
Feeding the surrogate random arbitrary wirings alongside strict mediation raises its accuracy on unseen
topology archetypes from 45% to 60%, yet both trail a trivial majority guess (#129). Diverse training
widens the signal; it does not make the cheap features carry a topology-general verdict. The screen
remains something to train on the structural class it will read.

**Wave V3 reading.** Both the structural and behavioral reductions fail, and the dynamics add memory. The
7% of the n=3 verdict the graph cannot decide is not a non-separability term — it is holistic, the same
ceiling per-node features hit at Probe 13 (#106). The verdict is not a coordination-game-difficulty
measure: neither independent learners (Probe 98) nor partner-modeling ones (#107) find triadic commits
harder, and triadic forms are if anything marginally easier to coordinate on. The one behavioral signal
is weak — triadic forms recover a little more slowly from a shock (#108), leaning the expected way but
far from a tracker. Dynamics, though, do matter once the mediator has memory: a sticky mediator makes
coordination path-dependent (#109), so dropping and re-binding a party are not symmetric. The verdict is
a structural fact; behavior reflects it only faintly, and the way to move it behaviorally is memory, not
agent sophistication.

**Wave V2 reading.** The all-required commit is what scales. A single conjunctive hub stays triadic with
the full group in its core and Φ = n−1 at every size from n=4 to n=7 (#105), so the n=6 collapse Probe 97
found was about random commits, not the structure itself. Splitting the mediation across two hubs does
not help — it shrinks the core and drops a party-group (#103). The growth rate is set by topology: a
serial chain keeps one fixed bottleneck (Φ=2.0), hub topologies grow Φ linearly, all-to-all coupling
compounds it (#104). The org-design reading is blunt. A large group is held in one irreducible
coordination by a commit that genuinely requires everyone, not by modularizing the mediator; modular
mediation buys separability at the cost of wholeness.

**Wave V1 reading.** The estimation frontier resolves into one payoff and one obstacle. The payoff: the
cheap surrogate generalizes. A random forest over eight size-invariant features, trained only on n=3,
ranks the verdict at n=4 (AUC 0.98) and n=5, so the dyadic/triadic call is estimable at scales the exact
computation cannot reach (#99), and the fingerprint is small — a single party-liveness feature suffices
on the corpus (#100). The obstacle: the 8 parity / pure-higher-order determinations (#56) are the
universal hard case. Φ_AR under-ranks them (#101) and every cheap CES predicate misses exactly them
(#102), never producing a false positive. Cheap measures fail in one direction only — they miss
synergistic binding that exists solely in the whole, the same forms the exact partition was built to
catch.

**Wave 9 reading.** Triadic coordination through a single mediator is rare, lean, and shrinking with
size. The rate falls from 9.4% at n=3 to effectively zero by n=6 (#97), and wherever triadic forms do
exist they sit exactly at the 2(n−1) edge floor — six edges at n=4, eight at n=5 (#95, #96). Two
reductions fail. There is no purely-structural necessary-and-sufficient condition for the verdict: across
all 4096 n=3 wirings, connectivity (all three nodes bidirectionally coupled) is necessary and 93%
sufficient, but the last 7% turn on the Boolean function content (#94). And the verdict is not a
behavioral-difficulty measure: independent learners do not find triadic commits harder to coordinate on
(#98). The structural kind stands on its own — not reducible to the wiring graph, not to selfish-learner
difficulty.

**Wave 8 reading.** Among measures computed without the exact system partition, two recover the verdict
fully and the rest only partly. A learned combination of cheap features (Probe 85) and the cause-effect-
structure counts (#93) both reach AUC 1.0. Single scalars max out below that: Φ_AR 0.96, causal emergence
and EI ~0.66, Φ_R 0.59, O-information at chance (#90). Per-node influence plateaus near 0.69 and a
pairwise synergy term does not lift it (#92), so the gap to the controlled 0.89 is not a missing
interaction feature. What separates the verdict cleanly is higher-order structure — the distinction and
relation counts of the cause-effect structure (#93) — which is the irreducibility the verdict measures
in the first place. EI tracks integration only weakly across the family (#39), and the measures' single-
threshold agreement is partial but structured, not random (#89).

**Wave 7 reading.** The verdict is estimable from time series, but not by every route. The ΦID-based
proxy Φ_R fails structurally: its triadic−dyadic gap stays near 0.06 no matter how long the trajectory
(#86) and no matter the redundancy lattice or noise (#87), never approaching the exact gap. Two other
routes succeed. The Barrett–Seth autoregressive Φ_AR separates the groups at AUC 0.925 (#84), and a
random forest over cheap features recovers the verdict outright, AUC 1.000 (#85). So an organization's
interaction logs do carry the dyadic/triadic signal — the earlier proxy-bridge nulls were a fact about
Φ_R, not about estimability. Probe 88 extends the cut to AI-agent protocols: a relay or broadcast
channel is a conveyor (dyadic), a jointly determined and acted-on protocol is a committing third party
(triadic). The estimation route that works is a learned combination of cheap features, not any single
information-theoretic Φ surrogate.

**Wave 6 reading.** Dynamics confirm that the verdict is a property of the form in motion, not a fixed
label. A mediator that adapts away from a party walks the form from triadic to dyadic (#79), and along
a path of rising coordination success Φ does not rise with it (#80) — the level and the kind stay
orthogonal under learning, as Probe 48 found statically. Two searches for richer structure came back
negative. There is no interior critical Φ peak: Φ tracks coupling determinism and is symmetric in phase,
so the random-tracking midpoint is a trough, not a peak (#81). A non-collapsing all-to-all pool shows no
Niizato-style size-four rise; under majority coupling Φ peaks at the triad and degrades as the group
grows (#82), the opposite dependence. One methodological gain: moving O-information from the present
state to the present⊕next transition opens a modest group gap where the static joint opens none (#83),
so transitions carry some discriminating synergy, though still well short of the exact verdict.

**Wave 5 reading.** A coherent political economy falls out. As a platform's determination tilts from
balanced toward the owner (#78), the worker and counterpart lose their place in the irreducible core
and it contracts to the platform-and-owner {S,P} — though that contraction is a specific extractive/
high-coupling regime, not the generic case (#74). Oversight is structurally inside the coordination
only when it both constrains and is fed by the commit (#76); a watchdog that only watches is a sink.
The leverage proxy (#75) is computable but shows balanced triads expose everyone symmetrically, so
differential value capture is a property of the *asymmetry* of the commit, the same axis #78 varies.
Observability asymmetry (#77) maximizes the triad's Φ rather than being strictly necessary.

**Wave 4 reading.** The dimensions and neighbors behave as the construct says, with one sharpening.
The worker's model displaces the counterpart as its fidelity rises (#69), and recursive mentalizing
binds only when acted on (#71) — the acted-on/bidirectional principle holds for inference too.
Sensemaking is dyadic across a family (#72), and one agent in two platforms keeps the two cores
separate (#73). The sharpening is #70: the scalar Φ>0 verdict conflates 2-party and 3-party
irreducibility, so the AI-MC/algorithmacy boundary is read on the major-complex *element count*, not
the verdict — which is exactly why Probe 20 found it a unit-of-analysis choice.

## Probes 49–53 — eighth batch (emergence, group agency, the integration claim)

More literature/dissertation engagement. Standouts:
- **Probe 52 gives a precise answer to the group-agency debate (List 2018 / Kramer 2021):** group
  integration that exceeds the members' emerges at n≥4 (the pool's Φ=3.0 > best pair 2.0), but not
  at the minimal triad (whole=pair=2.0). Whether a group has integration its members lack is a
  matter of size and binding, settled per-form by exact Φ.
- **Probe 51** confirms a heterogeneous team integrates over its tight subset, not the whole roster
  (Watson's subset-Φ picture).
- **Probe 53** closes the construct-validity loop: the worker's binding requires both competency
  dimensions (inference and translation), so the structural model reproduces the dissertation's core
  claim that algorithmacy is the *integration* of its dimensions, individually necessary.
- **Probe 49** is a non-trivial nuance: triadic forms show more causal emergence but lower raw
  effective information — Φ, emergence, and EI are three different things, as the repo's
  emergence_vs_phi already argued.
## Probes 44–48 — seventh batch (engaging the Φ-on-social-systems literature)

Grounded in the sourced dossier (Niizato et al. 2020 fish schools; Rosas et al. 2019 O-information;
Mediano–Rosas ΦID; Engel & Malone 2018). Three results matter:
- **Probe 45 replicates Niizato's headline contrast** on coordination forms: Φ separates dyadic from
  triadic where mutual information and transfer entropy do not — and transfer entropy is actively
  *fooled* by a back-channel (highest TE of all on a dyadic form). This is the fish-school result's
  methodological core, reproduced in the coordination domain.
- **Probe 47 fills a stated white-space**: ΦID has never been applied to a social/behavioral series;
  applied here it shows triadic coordination carries more persistent synergy than dyadic.
- **Probe 48 is a clean, important null**: exact Φ does NOT track a coordination-success proxy. The
  structural verdict is about the kind of coordination, not whether it succeeds — distinguishing this
  program's claim from Engel & Malone's performance correlation, and matching the dissertation's own
  position that the triad *demands* a competency rather than *being* good performance.
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
