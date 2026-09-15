# Coleman — Stage 4 methods

## Shared infrastructure

- Forms are expression specs (label → expression over other labels with `and`, `or`, `not`); a deleted
  party's variable is read as 0. Rules → TPM via `classifier.tpm_from_rules`; verdict via
  `probes.lib.verdict`; major complex via `probes.lib.major_complex`. Attractors and basins from the
  deterministic TPM.
- Burt's broker forms are imported unchanged from `org_frontier.thinkers.burt.forms` (`h1_forms`) and
  evaluated with that module's `evaluate`, so H2 compares Coleman's prediction against the Burt paper's own
  numbers.
- Run from the repo root on `~/iit-playground/venv-4.0/bin/python`.

## Instrument control (run first, in every probe)

The conjunctive triad by rules: Φ = 2.000000, core {A, M, B}.

## Forms

| form | rules |
|---|---|
| norm_open | A' = B ∧ C; B' = ¬A; C' = ¬A |
| norm_closed | A' = B ∧ C; B' = ¬A ∨ C; C' = ¬A ∨ B |
| info_open / info_closed | Burt: E' = X ∧ Y; X' = E [∨ Y]; Y' = E [∨ X] |
| control_open / control_closed | Burt: E' = X ∨ Y; X' = E [∨ Y]; Y' = E [∨ X] |
| parents_open | K1' = P1 ∧ K2; K2' = P2 ∧ K1; P1' = K1; P2' = K2 |
| parents_closed | K1' = P1 ∧ K2; K2' = P2 ∧ K1; P1' = K1 ∨ P2; P2' = K2 ∨ P1 |
| ring4 | A' = D; B' = A; C' = B; D' = C |
| two_dyads | A' = B; B' = A; C' = D; D' = C |

## Decision rules

- **H1** CONFIRMED iff (1,1,1) is a fixed point of norm_closed and not of norm_open, and B, C ∈ core of
  norm_closed. PARTIAL iff the fixed-point clause holds alone. REFUTED otherwise.
- **H2** CONFIRMED iff for both brokers coreΦ_closed ≥ coreΦ_open − 1e-6 and advantage_closed <
  advantage_open − 1e-6. PARTIAL iff both hold for one broker, or one clause holds for both. REFUTED
  otherwise.
- **H3** CONFIRMED iff closed core = {P1, P2, K1, K2}, open core ≠ that, and basin(1111)_closed >
  basin(1111)_open. PARTIAL iff two of three. REFUTED otherwise.
- **H4** CONFIRMED iff ring4 core = {A, B, C, D} with Φ > 0 and all four V equal and > 0, and two_dyads has
  no complex of more than two. PARTIAL iff the ring clause holds alone. REFUTED otherwise.
- **H5** CONFIRMED iff gain > 1e-6 and (V_B,closed − V_B,open)/gain < 1 − 1e-6. PARTIAL iff gain > 0 and B
  captures ≥ 1. REFUTED iff gain ≤ 0.

## Reporting

Each probe prints the control, one line per form, and one verdict. Results in `results/<probe>.json`.
