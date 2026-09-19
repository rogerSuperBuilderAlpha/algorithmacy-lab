# Research agenda v3 — questions only

V2’s science cells are closed on `contrib` (topology #15–#20, estimation
#21–#25 including #24 `HIDDEN_COLLAPSE_INTERMITTENT_CLIFF` on PR #749,
omit/construct #42, construct validity #43–#46, formal #47–#50, plus the
earlier beyond-binary / stoch-temporal / PE / AI lanes). This file lists
**new** questions only — residuals of those arcs, and motifs V2 never
named. No methods here. Numbered 1–16. Themes group them; each cites the
V2 finding it grows from.

Optional tooling leftover (M3 overlay subset-Φ fidelity on
`third_party/pyphi_iit4_mv`) is **not** a V3 science cell unless a cell
below is blocked without it.

## A. Missing templates and determination algebra

1. Beyond the five n=3 strict-mediation templates (relay / conjunctive /
   additive / free / parity from V2 #27 / `template_coverage_census`),
   does an **n=4 dual-mediator** census (series cascade, parallel
   mediators, mediator-of-mediators) force a **sixth** template, or do
   all triadic cores factor into products of the five?
   **Answered — FACTORS_INTO_FIVE.** No sixth template; closed triadic
   cores match the five; size-4 cores sit on known landmark Φ (0.5 / 2 /
   4=2+2 product). See `studies/dual_mediator_template_census/`.
2. Is **threshold / majority** determination at n≥4 a new template, or
   does it always collapse into the known redundancy-factors pattern
   (probes #10/#67) once pivotality is lost — even under topologies that
   restored triadicity for conjunctive hubs (V2 #15–#20)?
   **Answered — COLLAPSES_TO_REDUNDANCY.** Intermediate majority always
   factors; no new template — including on shared-mediator and recurrent
   carriers that restore triadicity under AND. See
   `studies/threshold_majority_template/`.
3. Do **mixed-algebra seats** (one seat parity, one conjunctive) on a
   single mediator produce a hybrid signature, or does the parity
   blind-spot (V2 #4 `BLINDSPOT_SURVIVES_RADIX`) dominate the whole form?
   **Answered — BLINDSPOT_DOMINATES.** Mixed seats never restore a
   conjunctive whole-form Φ; the form stays in the parity band or
   factors. See `studies/mixed_algebra_seats/`.

## B. Composed and hybrid topologies

4. When **local conjunctive triads are composed on a cycle** (a necklace:
   alternating hubs and shared parties), does the major complex merge
   globally (generalizing V2 #16 `WIN` shared-mediator merge), recover a
   known landmark (V2 #18 `DISCRETE_LANDMARKS` / #19
   `NO_INTERMEDIATE_LAW`), or invent a new Φ law?
   **Answered — COMPOSE_LANDMARK_OR_COLLAPSE.** Closed AND necklace recovers
   ring landmark Φ=4 (full core); OR/directed variants collapse; no new
   compose law. See `studies/local_triad_necklace/`.
5. Does a **ring-of-hubs** (hubs coupled as a ring, each hub serving a
   private leaf set) combine ring-cap with hub-growth where V2 #17
   `PICK_ONE` morphs failed, or does it also pick a landmark / collapse?
   **Answered — FACTORS_NO_COMBINE.** No ring–hub hybrid on the n=6 panel;
   cells factor (incomplete hub cores, often Φ=6 on hubs alone) or
   collapse. See `studies/ring_of_hubs/`.
6. Across **k>2 local triads sharing a single mediator** (the natural
   lift of V2 #16), does merge Φ scale as k, as 2k, or saturate — and
   does OR bridging still refuse merge?
   **Answered — SCALE_2K_OR_REFUSES.** AND merge Φ = 2k for k=1,2,3
   (Φ=2,4,6; full cores); OR refuses full merge at k=2 and k=3. See
   `studies/shared_mediator_k/`.
7. Is there a **hybrid feedforward+recurrent** seam (one recurrent cycle
   feeding a feedforward chain) whose locus violates V2 #15’s
   closure-decides-locus rule?
   **Answered — CLOSURE_HOLDS_HYBRID.** Hybrid AND seams keep the major
   complex inside the recurrent zone (FF tail excluded); V2 #15’s
   closure-decides-locus survives. OR relocates onto the FF pair alone.
   See `studies/hybrid_ff_recurrent_seam/`.

## C. Scale morphs past n=6

8. Does the omit cycle-type discriminant **morph again at n=7**, or does
   the n=5→n=6 singleton→band shift (V2 #42 `SCALE_MORPHS`) stabilize
   into a fixed band grammar?
   **Answered — BAND_GRAMMAR_HOLDS.** At n=7 (indeg (0,1,1,1,1,1,2)) the
   omit cycle-type law stays a class-pure two-band grammar (Φ=12 vs 14);
   no singleton return, continuum, or purity break. See
   `studies/omit_cycle_morph_n7/`.
9. Do the discrete Φ atoms of V2 #18 / `interior_ring_pool` at n≤6
   **sprout new interior atoms at n=7–8**, or only thicken existing
   landmark multiplicities?
   **Answered — SPROUTS_NEW_ATOMS.** Designed ring–pool interiors at n=7
   yield a new full-core atom Φ=10 outside L≤6 interiors {6,8,9,12}, while
   also recalling 6 and 12. See `studies/interior_atoms_n78/`.
10. Does the parity Φ = 2^(2−n) law (V2 #47/#115) remain exact under
    **n>6 hub embeddings**, or do topology residuals appear once exact
    enumeration is replaced by cut formulas alone?
   **Answered — LAW_HOLDS_NGT6.** Exact parity-hub Φ = 2^(2−n) at
   n∈{6,7} with full cores; named H-cut is the MIP and matches exact Φ
   (no cut-only residual). See `studies/parity_law_n_gt6/`.

## D. Graded × topology and noise × structure

11. On a **ring versus hub versus necklace** carrier, does graded commit
    (V2 #2 `SHARP_CLASS_GRADED_PATH`) keep sharp class labels while Φ
    grades, or does topology force class flips the fixed-hub panel
    never saw?
   **Answered — SHARP_HOLDS_ACROSS_TOPO.** Graded min-commit keeps
   discrete NULL→DYADIC→TRIADIC on hub, ring (n=3,4), and necklace while
   Φ grades; no topology-forced class flip. See
   `studies/graded_topo_carriers/`.
12. Does party-vs-mediator noise (V2 #7 `SAME_THRESHOLD_DIFF_CURVE`)
    still share p*=0.5 when the carrier is a **composed necklace** or
    **multi-hub span** rather than a single hub?
   **Answered — SAME_PSTAR_COMPOSED.** Party and mediator flip-noise
   still share p*=0.5 on AND necklace and shared-mediator span
   (shared_k2); V2 #7 coin-flip threshold survives composition. See
   `studies/noise_composed_carriers/`.

## E. Validation bridges left open by V2 #45

13. What is the **weakest Boolean render** of a real coordination log
    that still recovers the conjunctive Φ=n−1 signature V2 #45 found
    only under a forced hub — role counts alone, activity thresholds,
    or institutional elicits?
   **Answered — ROLE_COUNTS_HUB_WEAKEST.** Weakest recovering render is
   role-count cardinality → conjunctive hub template; activity
   thresholds/fits and institutional elicits miss the Φ=n−1 scaling
   bar. See `studies/weakest_boolean_render/`.
14. Can a **survey / Wageman-style instrument** (V2 #44) be paired with
    an in-silico form so that measured W predicts not only the verdict
    class but the **Φ landmark** (ring-4 vs hub-(n−1) vs pool)?

## F. Estimation residuals after V2 #24

15. Under V2 #24’s role-gated collapse (hide party kills MI screen; hide
    mediator does not), does a **topology-aware imputer** (ring vs hub
    prior) restore AUC, or is party absence a hard information cut no
    prior repairs?
16. Does the intermittent-observation **cliff at δ=0** soften under
    **correlated party duty cycles** (two parties observed on
    alternating slots), or does any zero-duty party recreate the
    cliff?

---

**First cells run on this agenda:** #4
(`studies/local_triad_necklace/` → `COMPOSE_LANDMARK_OR_COLLAPSE`); #5
(`studies/ring_of_hubs/` → `FACTORS_NO_COMBINE`); #6
(`studies/shared_mediator_k/` → `SCALE_2K_OR_REFUSES`); #7
(`studies/hybrid_ff_recurrent_seam/` → `CLOSURE_HOLDS_HYBRID`); #1
(`studies/dual_mediator_template_census/` → `FACTORS_INTO_FIVE`); #2
(`studies/threshold_majority_template/` → `COLLAPSES_TO_REDUNDANCY`); #3
(`studies/mixed_algebra_seats/` → `BLINDSPOT_DOMINATES`).
Lane note `COMPOSED_TOPOLOGY_ARC.md`.
