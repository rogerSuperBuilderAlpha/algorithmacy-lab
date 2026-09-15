# Serres — Stage 4 methods

## Shared infrastructure

- Deterministic forms: rules → TPM via `classifier.tpm_from_rules`; verdict via `probes.lib.verdict`; major
  complex via `probes.lib.major_complex`.
- Exogenous noise: the TPM column for N is 0.5 in every state; Φ and the major complex on the stochastic TPM
  via the Granovetter machinery (`granovetter.forms.phi_mip`, `major_complex_tpm`), max over reachable
  states.
- Constants: a producer is a constant 1, a stopped token a constant per node; orphaned terms in deletion
  become constants 0.
- Run from the repo root on `~/iit-playground/venv-4.0/bin/python`.

## Instrument control (run first, in every probe)

The conjunctive triad by rules: Φ = 2.000000, core {A, M, B}. In the probe using the stochastic path, the
same triad through that path must also give 2.000000.

## Forms

`∧` AND, `¬` NOT, `⊕` XOR.

| form | rules |
|---|---|
| arrow | F = 1; P' = F |
| exchange | A' = B; B' = A |
| chain | F = 1; T' = F; R' = T |
| chain_noise | F = 1; T' = F; R' = T ∧ ¬N; N' = R |
| cascade | F = 1; T' = F ∧ ¬R; R' = T ∧ ¬N; N' = R |
| dyad | A' = B; B' = A |
| dyad_exo | A' = B; B' = A ⊕ N; N' = coin (P = 0.5) |
| dyad_endo | A' = B; B' = A ⊕ N; N' = A ∧ B |
| passing | A' = C; B' = A; C' = B |
| stopped | A = 1; B = 0; C = 0 |

## Decision rules

- **H1** CONFIRMED iff the arrow has a complex containing F and P with Φ > 0. REFUTED otherwise.
- **H2** CONFIRMED iff chain has no complex, chain_noise has one, N is in it, and F and T are not. PARTIAL
  iff a complex appears with N but F or T in it. REFUTED otherwise.
- **H3** CONFIRMED iff dyad_exo core = {A, B} with core Φ < 2 − 1e-6, and dyad_endo core ∋ N. PARTIAL iff
  one clause. REFUTED iff neither.
- **H4** CONFIRMED iff cascade core ⊇ {R, N}, excludes F and T, share(N) ≥ share(R), share(T) = 0. PARTIAL
  iff the core is at the last position but the share ordering fails, or the reverse. REFUTED otherwise.
- **H5** CONFIRMED iff passing core = {A, B, C} with Φ > 0 and stopped has no complex. PARTIAL iff one
  clause. REFUTED iff neither.

## Reporting

Each probe prints the control, one line per form, share lines where computed, and one verdict. Results in
`results/<probe>.json`.
