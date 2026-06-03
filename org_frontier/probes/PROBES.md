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
