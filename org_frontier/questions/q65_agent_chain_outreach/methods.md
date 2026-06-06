# Q65 — Stage 4 methods (fixed before computation)

Deterministic Boolean systems, synchronous update, classified by exact IIT-4.0 Φ over the
minimum-information partition (`classifier.classify_rules`) and read on the maximal complex
(`probes.lib.major_complex`) for H4. The agent chain reuses the mediation-chain builder
`multiparty.chains.chain_rules`, relabelled E, A1..Ad, R. State tuples are indexed in label order. Every
probe validates the instrument first: a decoupled relay reads dyadic (Φ = 0) and a fully-coupled triad
reads triadic (Φ = 0.83). Run on `~/iit-playground/venv-4.0/bin/python`. Decision rules fixed here.

## H1 test — chain depth

- **Forms:** `chain_rules(d)` for d = 1..4 (n = d + 2): E'=A1, Aj'=A_{j-1}∧A_{j+1}, R'=Ad.
- **Measure:** verdict and Φ_MIP.
- **Control:** the canonical triad reads triadic at Φ = 2.0.
- **Decision rule:** H1 confirmed if every depth is triadic. Refuted if any depth is dyadic.

## H2 test — Φ constant across depth

- **Forms:** the same d = 1..4 chains.
- **Measure:** Φ_MIP per depth.
- **Decision rule:** H2 confirmed if Φ_MIP = 2.0 (within 1e-6) at every depth. Refuted if any Φ_MIP
  departs from 2.0.

## H3 test — relay-gap agent

- **Forms (d = 2, n = 4):** `intact` = chain_rules(2); `relay_gap` = chain_rules(2) with A1' = E (index
  rule x[0]) replacing A1' = E ∧ A2.
- **Measure:** verdict and Φ_MIP.
- **Decision rule:** H3 confirmed if `relay_gap` is dyadic and `intact` is triadic. Refuted if `relay_gap`
  is triadic.

## H4 test — core membership

- **Form:** the intact chain at d = 2 (n = 4), labels (E, A1, A2, R).
- **Measure:** the major complex (`major_complex`).
- **Decision rule:** H4 confirmed if the core is the full set {E, A1, A2, R}. Refuted if any element is
  excluded.

## H5 test — depth atop breadth

- **Form (n = 5, labels E, A1, M, R1, R2):** E'=A1, A1'=E∧M, M'=A1∧R1∧R2, R1'=M, R2'=M.
- **Measure:** verdict and Φ_MIP.
- **Decision rule:** H5 confirmed if the form is triadic (Φ_MIP > 0). Refuted if dyadic.
