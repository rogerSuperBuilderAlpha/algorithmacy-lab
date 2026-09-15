# Girard — Stage 4 methods

## Shared infrastructure

- Deterministic forms: rules → TPM via `classifier.tpm_from_rules`; verdict via `probes.lib.verdict`; major
  complex via `probes.lib.major_complex`.
- Distance sweep: the TPM column for M is p·(copy of S) + (1 − p)·(hold); Φ and the major complex on the
  stochastic TPM via the Granovetter machinery (`granovetter.forms.phi_mip`, `major_complex_tpm`), max over
  reachable states.
- Shares: deletion cost on the core's Φ; an orphaned term (no inputs left) becomes a constant 0 — this avoids
  the self-holding one-node complex the Hegel paper met. A form with no complex counts as 0.
- Run from the repo root on `~/iit-playground/venv-4.0/bin/python`.

## Instrument control (run first, in every probe)

The conjunctive triad by rules: Φ = 2.000000, core {A, M, B}. For the sweep probe, the same triad through
the stochastic path at p = 1 must also give 2.000000.

## Forms

Little-endian (S, M, O); `∧` is AND.

| form | rules |
|---|---|
| spontaneous | S' = O; O' = S (no M) |
| external | S' = M; M' = M; O' = M ∧ S |
| internal | S' = M; M' = S ∧ O; O' = M ∧ S |
| double | S' = M; M' = S; O' = M ∧ S |
| dyad | S' = M; M' = S (no O) |
| distance(p) | S' = M; M' = S w.p. p else M; O' = M ∧ S |

## Decision rules

- **H1** CONFIRMED iff internal core ⊇ {S, O} and, with M deleted, no complex contains both S and O. REFUTED
  otherwise.
- **H2** CONFIRMED iff external: M in no complex and no complex ⊇ {S, O}; internal core = {S, M, O}. PARTIAL
  iff one half. REFUTED iff neither.
- **H3** CONFIRMED iff double core = {S, M} and |Φ(double core) − Φ(dyad)| < 1e-6. PARTIAL iff core = {S, M}
  and Φ differs. REFUTED iff O in the core.
- **H4** CONFIRMED iff core Φ strictly increases over p = 0.25, 0.5, 0.75, 1 (p = 0 is external, Φ of the
  S–O part) and O is in the core at no p > 0. PARTIAL iff one of the two. REFUTED iff neither.
- **H5** CONFIRMED iff double shares S = M > 0, O = 0, and internal shares S ≠ M. PARTIAL iff one of the two.
  REFUTED iff neither.

## Reporting

Each probe prints the control, one line per form, share lines where computed, and one verdict. Results in
`results/<probe>.json`.
