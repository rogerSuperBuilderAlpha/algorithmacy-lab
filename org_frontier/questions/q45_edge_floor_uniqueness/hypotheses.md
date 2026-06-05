# Q45 — Stage 3 hypotheses (fixed before computation)

Five working hypotheses on whether the conjunctive (AND) commit uniquely saturates the maximum integrated
information available at the 2(n−1) edge floor of strict mediation, and whether other commit classes or
wiring spaces reach competing ceilings at the same lean budget. Written and committed before any test runs.
Prior probes (#30, #56, #113, #115, #116, #94, #7) supply the structural priors each null rests on.

## H1 — Every triadic strict-mediation form sits at the edge floor
- **Claim:** All 24 triadic forms of the n=3 strict-mediation family carry exactly 4 causal edges, the
  2(n−1) floor reported by #30. No triadic form in the family is above or below that count.
- **H0:** At least one triadic strict-mediation form has an edge count other than 4.
- **Predicted outcome:** Edge count is 4 for all 24 triadic forms; min = max = 4 among triadic rows.
  H0 is refuted.

## H2 — Only AND commits reach Φ = n−1 at the floor
- **Claim:** Among triadic strict-mediation forms at the 4-edge floor, every form with Φ = 2.0 (= n−1 at
  n=3) uses an AND commit on the mediator (S-function index 1). No other commit class matches conjunctive
  Φ at the floor.
- **H0:** At least one triadic form at 4 edges with Φ = 2.0 uses a non-AND commit (OR, XOR, or other).
- **Predicted outcome:** The 16 forms at Φ = 2.0 all have S-index 1 (AND); zero counterexamples. H0 is
  refuted.

## H3 — Parity commits saturate their own ceiling at the same floor
- **Claim:** The 8 parity (XOR/XNOR) triadic forms sit at the same 4-edge floor but achieve Φ = 0.5 =
  2^(2−n), the parity scaling-law ceiling from #115. Parity is not sub-floor; it fully saturates its
  class budget at the lean wiring.
- **H0:** At least one parity triadic form has Φ ≠ 0.5 or an edge count ≠ 4.
- **Predicted outcome:** All 8 parity forms: 4 edges, Φ = 0.5 exactly. H0 is refuted; parity uniqueness
  is class-relative, not a failure to reach a ceiling.

## H4 — OR commits do not bind triadically in strict mediation
- **Claim:** No OR-commit form (S-function index 7) in the 256 strict-mediation family is triadic. OR
  cannot achieve even parity-level irreducibility at the strict-mediation topology, despite matching AND
  at larger n in the all-required hub (#116).
- **H0:** At least one OR-commit strict-mediation form is triadic.
- **Predicted outcome:** Zero OR forms among the 24 triadic rows; all 64 OR-labelled forms (4 W' × 16
  S × 1 C' pattern with S-index 7) are dyadic. H0 is refuted.

## H5 — Global 4-edge triadic maximum is conjunctive-only
- **Claim:** Across all 4096 arbitrary n=3 wirings, every triadic form at exactly 4 edges with Φ = 2.0
  is strict-mediation with an AND commit. No back-channel or exotic wiring reaches max Φ at the global
  4-edge minimum.
- **H0:** At least one triadic wiring with 4 edges and Φ = 2.0 is not strict-mediation AND.
- **Predicted outcome:** The set of max-Φ 4-edge triadic forms equals the 16 conjunctive strict-mediation
  forms (possibly relabeled). H0 is refuted; the conjunctive hub is the unique max-Φ achiever at the
  global 4-edge floor.
