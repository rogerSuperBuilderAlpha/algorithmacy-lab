# Q217 — Stage 3 hypotheses (fixed before computation)

Question: every mediator in the catalog is a fixed seat. What happens when the mediator role rotates: a
clock passes the "chair" among the parties, and whoever holds it aggregates the others (conjunctively) while
the others follow the chair? Forms (deterministic, exact IIT-4.0 via `classify_rules` / `major_complex`):

- F_fixed: A'=B∧C, B'=A, C'=A, plus an idle clock T'=¬T (n=4 baseline).
- F_rot2: clock T'=¬T; chair is A when T=0, B when T=1 (n=4).
- F_rot3: mod-3 clock on two bits; chair cycles A→B→C (n=5).

Written and committed before any test runs.

## H1 — Rotation preserves irreducibility
- **Claim:** F_rot2 and F_rot3 read triadic.
- **H0:** Rotating the chair factors the coordination (dyadic), as slow or intermittent mediators do (Q207, Q209).
- **Predicted outcome:** structure == triadic for both rotating forms.

## H2 — The clock is a member
- **Claim:** In the rotating forms the clock bit(s) belong to the major complex: the schedule is part of the coordination, not outside it.
- **H0:** The major complex excludes the clock.
- **Predicted outcome:** T (or T0/T1) appears in major_complex for F_rot2 and F_rot3; it does not for F_fixed.

## H3 — Rotation dissolves the single veto player
- **Claim:** Under a fixed chair the mediator is the sole party in every integrating coalition; under rotation no single party (A, B, or C) is.
- **H0:** Some party remains in every integrating coalition under rotation.
- **Predicted outcome:** veto_set over parties is {A} for F_fixed and empty of parties for F_rot2/F_rot3.

## H4 — Shared leadership integrates more
- **Claim:** Max Φ of a rotating form is at least the fixed form's.
- **H0:** max_phi(F_rot2) < max_phi(F_fixed).
- **Predicted outcome:** max_phi(F_rot2) ≥ max_phi(F_fixed).

## H5 — The core is the whole
- **Claim:** In F_rot3 the major complex contains all three parties.
- **H0:** Rotation localizes the core to a subset of parties (as agent chains do, Q65–Q66).
- **Predicted outcome:** {A,B,C} ⊆ major_complex(F_rot3).

Scope: in-silico, designed deterministic forms, conjunctive chairs only.
