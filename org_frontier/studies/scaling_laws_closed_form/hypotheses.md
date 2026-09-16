# Scaling laws closed-form — claims (fixed before proving)

**Question (RESEARCH_AGENDA_50_V2 #47).** Prove the scaling laws
closed-form: conjunctive Φ = n−1, pool Φ = n(n−1), parity Φ = 2^(2−n)
(#116, #132, #115) — derive them from the MIP rather than reading
them off numerics.

**Already known (cited, not reopened).**
- Probe #116: conjunctive (AND-all) hub at Φ = n−1, full core, n=4..7.
- Probe #132: zoo — hub linear, pool super-linear n(n−1), parity decay.
- Probe #115: parity (XOR) hub Φ trajectory vs conjunctive; decay
  2^(2−n) is the zoo reading of that sequence.
- Stoch–temporal / estimation / construct / omit stay closed except as
  empirical pointers to these laws.

**What is proved here vs verified.** Analytic derivation from the
IIT-4.0 Φ_MIP / GID apparatus on the lab’s PyPhi pin. Small-n exact Φ
checks verify; they are not the proof. Steps are tagged **Theorem** or
**Conjecture** (or **Lemma**) in `PROOFS.md`.

## Instrument (fixed)

- **Φ** = major-complex `sia.phi` (system φ_s), not `big_phi`.
- φ_s = min(φ_cause, φ_effect) on the MIP.
- Repertoire distance: `GENERALIZED_INTRINSIC_DIFFERENCE`
  (PyPhi 1.2.1.dev1470+gb78d0e342):
  φ = selectivity × log₂(forward / partitioned_forward).
- System partitions: `SET_UNI/BI`. MIP minimizes
  `(normalized_φ, −φ)` — lowest normalized φ, then highest raw φ.
- Exact binary Boolean TPMs; in-silico. No Hegel / Substack.

## Forms (exact Boolean)

Labels `n0..n_{n-1}`; node 0 is the hub when the form has one.

| law | builder | update |
|---|---|---|
| conjunctive Φ = n−1 | `single_hub` (#103/#116) | S′ = ∧_{i≥1} X_i ; X_i′ = S |
| pool Φ = n(n−1) | `pool` (#104/#132) | X_i′ = ∧_{j≠i} X_j |
| parity Φ = 2^(2−n) | `parity_hub` (#115) | S′ = ⊕_{i≥1} X_i ; X_i′ = S |

Evaluation state for the closed forms: the all-1s state (reachable and
φ-maximizing on the verified range).

## Claims

### C1 — conjunctive hub

For every n ≥ 3, major-complex Φ(`single_hub(n)`) = n − 1, with the
full node set as the complex.

### C2 — pool

For every n ≥ 3, major-complex Φ(`pool(n)`) = n(n − 1), full core.

### C3 — parity hub

For every n ≥ 3, major-complex Φ(`parity_hub(n)`) = 2^(2−n), full core.

## Status targets (filled in FINDINGS)

Each claim: **proved** / **partial** (named gap) / **blocked**.

## Best next (among #48–#50)

Fixed after #47 lands; see FINDINGS.
