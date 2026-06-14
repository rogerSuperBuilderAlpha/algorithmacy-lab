# Q64 — Stage 4 methods (fixed before computation)

All forms are deterministic Boolean systems with synchronous update, classified by exact IIT-4.0 Φ over
the minimum-information partition with `classifier.classify_rules`, and read on the maximal complex with
`probes.lib.major_complex` where the hypothesis concerns core membership. State tuples are indexed in
label order (E, M, R1, …, Rk). Every probe validates the instrument first: a decoupled relay reads dyadic
(Φ = 0) and a fully-coupled triad reads triadic (Φ = 0.83). Run on `~/iit-playground/venv-4.0/bin/python`.
Decision rules are fixed here.

## H1 test — all-required campaign scaling

- **Forms:** for k = 1..4, the all-required campaign on n = k + 2 elements: E'=M, M'=E∧R1∧…∧Rk, Ri'=M.
- **Measure:** verdict and Φ_MIP from `classify_rules`.
- **Control:** the fully-coupled control triad reads triadic at Φ = 0.83.
- **Decision rule:** H1 confirmed if every k is triadic and Φ_MIP = n − 1 (within 1e-6 of 2, 3, 4, 5).
  Refuted if any k is dyadic or any Φ_MIP departs from n − 1.

## H2 test — substitutable campaign

- **Forms:** for k = 2, 3, 4, the substitutable campaign: E'=M, M'=E∧(R1∨…∨Rk), Ri'=M.
- **Measure:** verdict and Φ_MIP.
- **Decision rule:** H2 confirmed if every k is dyadic (Φ_MIP = 0). Refuted if any k is triadic.

## H3 test — pooled broadcast

- **Forms:** for k = 2, 3, 4, the pooled broadcast: E'=M, M'=E, Ri'=M (the agent reads no recipient).
- **Measure:** verdict and Φ_MIP.
- **Decision rule:** H3 confirmed if every k is dyadic (Φ_MIP = 0). Refuted if any k is triadic.

## H4 test — one substitutable recipient

- **Forms (n = 5, k = 3):** `mixed` = E'=M, M'=E∧R1∧(R2∨R3), Ri'=M; `all_required` = E'=M,
  M'=E∧R1∧R2∧R3, Ri'=M.
- **Measure:** verdict and Φ_MIP.
- **Decision rule:** H4 confirmed if `mixed` is dyadic and `all_required` is triadic. Refuted if `mixed`
  is triadic.

## H5 test — core membership

- **Forms:** the all-required campaign at k = 2 (n = 4) and k = 3 (n = 5).
- **Measure:** the major complex (`major_complex`) — the core label set.
- **Decision rule:** H5 confirmed if the core is the full set {E, M, R1, R2} at k = 2 and
  {E, M, R1, R2, R3} at k = 3. Refuted if any recipient is excluded.
