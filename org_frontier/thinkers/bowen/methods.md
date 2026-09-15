# Bowen — Stage 4 methods

## Shared infrastructure

- Rules → deterministic TPM via `classifier.tpm_from_rules`; anxiety via flip noise per node,
  `T[:, j] = det[:, j] (1 − ε_j) + (1 − det[:, j]) ε_j` (the q71 convention).
- Whole-system Φ_MIP: max over all reachable states of exact IIT-4.0 system Φ (`forms.phi_mip`). Major
  complex: `forms.major_complex_tpm`, max over reachable states. Connectivity from the noiseless rules.
- Retained fraction: Φ(ε) / Φ(0) of the whole. Run from the repo root on `~/iit-playground/venv-4.0/bin/python`.

## Instrument control (run first, in every probe)

The conjunctive triad by rules: Φ = 2.000000, core {A, M, B}. Then the same triad through the noise path at
ε = 0: Φ = 2.000000. No comparison is read until both pass.

## Forms

Little-endian state tuples; `∧` is AND.

| form | parties | rules |
|---|---|---|
| dyad | A, B | A' = B; B' = A |
| calm | A, B, C | A' = B; B' = A; C' = A ∧ B |
| triangled | A, B, C | A' = B ∧ C; B' = A; C' = A ∧ B |
| interlocked | A, B, C, D | A' = B ∧ C ∧ D; B' = A; C' = A ∧ B; D' = A ∧ B |
| reactive third | A, B, C | A' = B ∧ C; B' = A ∧ C; C' = A ∧ B |
| neutral third | A, B, C | A' = B ∧ C; B' = A ∧ C; C' = C |

Anxiety levels: ε ∈ {0, 0.05, 0.1, 0.2, 0.3} uniform (H1, H4, H5); ε ∈ {0.1, 0.2} at one node (H3).

## Decision rules

- **H1** CONFIRMED iff at every ε > 0 the triangled form's retained fraction exceeds the dyad's and its major
  complex is {A, B, C}. PARTIAL iff the fraction ordering holds at some but not all ε, or holds while the
  complex shrinks. REFUTED iff the dyad retains at least as much at every ε.
- **H2** CONFIRMED iff calm core = {A, B} and triangled core = {A, B, C}. REFUTED otherwise.
- **H3** CONFIRMED iff at both ε the loss from anxiety at C is strictly the smallest of the three positions.
  PARTIAL iff at one ε. REFUTED iff at neither.
- **H4** CONFIRMED iff (a) the interlocked major complex has three parties and (b) its retained fraction
  exceeds the triangled form's at every ε > 0. PARTIAL iff one of (a), (b). REFUTED iff neither.
- **H5** CONFIRMED iff (a) the neutral third is outside the core and the reactive third inside, and (b) the
  neutral-third form's insiders retain a larger fraction than the dyad at every ε > 0 (fraction measured on
  the major complex's Φ relative to its ε = 0 value). PARTIAL iff one of (a), (b). REFUTED iff neither.

## Reporting

Each probe prints the two control lines, one line per form and ε (`form ε Φ_MIP fraction core coreΦ`),
and one verdict line. Results in `results/<probe>.json`.
