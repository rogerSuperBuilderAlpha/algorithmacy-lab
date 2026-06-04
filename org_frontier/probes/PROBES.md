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
