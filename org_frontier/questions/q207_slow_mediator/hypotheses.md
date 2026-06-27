# Q207 — Stage 3 hypotheses (fixed before computation)

Five working hypotheses, each with its null and predicted outcome, committed before any test runs.

The reference form **F0** is the synchronous conjunctive triad `W'=S, S'=W∧C, C'=S` (triadic, Φ_MIP=2.0).
The slow-mediator form **F_slow** (n=4, labels W,S,C,K) adds a clock node K that toggles (`K'=¬K`) and
gates the mediator: `S' = (W∧C) if K else S` — the mediator recomputes its commitment only on K-ticks and
holds it otherwise — while the parties update every step (`W'=S, C'=S`). The control **F_held** (n=4) is
the zero-rate limit: the mediator never recomputes (`S'=S`), with the same clock and party rules.

## H1 — Instrument control
- **Claim:** F0 reads triadic with Φ_MIP = 2.0.
- **H0:** —
- **Predicted outcome:** triadic, max_phi = 2.000000. No comparison number is trusted unless this passes.

## H2 — The half-rate mediator still binds the triad
- **Claim:** F_slow stays irreducible: its major complex contains all three of W, S, C.
- **H0:** Slowing the mediator factors the coordination; the core loses at least one of W, S, C.
- **Predicted outcome:** {W, S, C} ⊆ `major_complex(F_slow).core`, and F_slow reads triadic.

## H3 — The gating clock is a spectator
- **Claim:** The clock K is not in F_slow's major complex — an exogenous rate clock emits without joining
  the irreducible core, matching Probe 3.
- **H0:** The clock joins the core.
- **Predicted outcome:** "K" ∉ `major_complex(F_slow).core`.

## H4 — Half-rate mediation lowers integration
- **Claim:** Gating the mediator to every second step lowers Φ below the synchronous triad: F_slow's core
  Φ < 2.0.
- **H0:** The slow mediator integrates as much as the synchronous one; core Φ = 2.0.
- **Predicted outcome:** `major_complex(F_slow).core_phi` < 2.0 − PHI_EPS.

## H5 — A never-committing mediator factors
- **Claim:** The zero-rate control F_held factors: a mediator that never recomputes cannot bind, so its
  core loses the triad (it reads dyadic, or the core drops a party). This shows the binding depends on the
  mediator actually committing, so the rate is the operative variable.
- **H0:** F_held is still triadic with the full triad in its core, so the mediator's rate does not matter.
- **Predicted outcome:** F_held reads dyadic, or {W, S, C} ⊄ `major_complex(F_held).core`.
