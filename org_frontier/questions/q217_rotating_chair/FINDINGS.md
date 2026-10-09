# Q217 — Findings: the rotating chair

Probes 453 (three parties), 454 (four parties), 455 (chair logic and earned rotation), and 456 (per-state,
party-only audit). Hypotheses H1–H5 were committed before probe 453, H6 before 454, and H7–H8 before 455.
Probe 456 was run after independent review; its two observations are exploratory.

## Central result
In the tested conjunctive Boolean models, full rotation preserves peak party-core integration and its state
coverage, while moving the veto between successive chairs so that no party keeps it across states.

## Definitions
- **Peak core:** the maximal complex at the reachable state with the highest Φ (`probes/lib.py:major_complex`).
- **State coverage:** the share of distinct reachable states, counted uniformly, in which the party set is the
  maximal complex. It is not temporal persistence: it does not measure time spent in the core along a trajectory.
- **Party veto:** among party-only coalitions (size ≥ 2, φ_s > 0 at a state), the parties in every one. Reported
  per state and intersected across states. Clock nodes are excluded from coalitions.

## Results

| Form | Whole-system max Φ | Peak core (Φ) | State coverage | Per-state party veto | Cross-state party veto |
|---|---|---|---|---|---|
| F_fixed (chair A, idle clock) | 0 | A,B,C (2.0) | 2/8 | A | A |
| F_rot2 (A/B alternation) | 0 | A,B,C (2.0) | 2/8 | A,B | A,B |
| F_rot3 (A→B→C) | 0 | A,B,C (2.0) | 3/12 | current + previous chair | none |
| F4_fixed | 0 | A,B,C,D (3.0) | 4/16 | A | A |
| F4_rot (A→B→C→D) | 0 | A,B,C,D (3.0) | 4/16 | current + previous chair | none |
| F_rot3_OR | 0 | A,B,C (2.0) | 3/12 | a pair | none |
| F_earned3 (AND, earned gavel) | 0 | A,B,C (2.0) | 3/12 | a pair | none |
| F_rot3_XOR | 0 | T (1.0) | 0/12 | A,B,C | A,B,C |
| F_earned3_XOR | 0.5 (triadic, 7/12 states) | U (1.0) | 4/12 | A,B,C | A,B,C |

*Table note:* per-state veto entries apply only to states where integrating party coalitions exist; the
cross-state intersection excludes states with none (half of the evaluated states in the AND forms).

Clock nodes form the maximal complex in many non-peak states, in both fixed and rotating forms; F_earned3 has a
mixed B,C,U complex at one state and F_earned3_XOR has the whole five-node complex at two.

## Hypotheses
- **H1 (rotation reads triadic): refuted.** Whole-system max Φ is 0 for fixed and rotating AND forms.
- **H2 (clock joins the core): refuted for the peak core only.** Clock nodes do form maximal complexes at other states.
- **H3 (rotation dissolves the single veto): partial.** Full rotation leaves no cross-state party veto; two-seat
  alternation leaves both seats as veto players.
- **H4 (rotation integrates at least as much): holds as a tie on its stated measure,** whole-system max Φ 0 vs 0.
  Peak core Φ also ties (2 vs 2, 3 vs 3), a separate result.
- **H5 (core holds all parties): holds for the peak core.**
- **H6 (no cross-state veto at four parties): holds.**
- **H7 (not an AND artifact): holds for OR, refuted for XOR,** where under free rotation the party core is never the maximal complex (0/12), under earned rotation it is in
  4/12 states but not at the peak, and all
  three parties are party-only veto players.
- **H8 (earned rotation pulls the clock in and reads triadic): refuted for AND.** Earned XOR reads triadic at the
  whole-system level but its peak core is one clock bit and all parties hold the veto.

## Exploratory audit findings (probe 456)
1. **Moving veto.** Whenever party-only integrating coalitions exist (half the evaluated states), full
   rotation gives the veto to the current and previous chairs: all six eligible three-party states and all
   eight four-party states.
2. **Equal state coverage.** Fixed and fully rotating conjunctive models both have 25% state coverage. Clock-only
   cores occur in both controls; this does not show that any clock causes them.

## Limits
In-silico, designed deterministic forms, at most four parties, a clock that is external (free-running) except in the earned variants, where it is endogenous, three chair logics. Results
are per state, at the peak state, or intersected across states; none measure temporal persistence. Nothing here
concerns real organizations.
