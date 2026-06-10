# Q116 — Stage 4 methods (fixed before computation)

Exact IIT-4.0. Two readings of each party's share of the coordination, compared across a panel. Run on
`~/iit-playground/venv-4.0/bin/python`; the panel computes in a few seconds.

## Measures (`forms.py`)

- **structural** — `structural_shares`: the φ_d of each party's own distinction (mechanism = {party}) in the
  cause-effect structure at the integrating state (Q99 `ces`), normalized to sum to one. Parties with no
  singleton distinction take zero.
- **strategic** — `strategic_shares`: each party's Shapley value of subsystem-Φ (Q111 `shapley`), normalized
  to sum to one.

## Panel (`panel`)

- **triad** — the read-recipient triad (E, M, R), the minimal symmetric case.
- **principal** — the bidirectional principal of Q114 (E, M, R, P), an asymmetric four-party form.
- **market2 / market3** — the all-required market of Q85 at N = 2 and N = 3 (E, M1..MN, C).

## Decision rules (`probe_value_against_structure.py`)

- H1 confirmed if the triad's largest structural-versus-strategic share gap is below 0.01.
- H2 confirmed if every form is concordant: for each party pair, the two measures never order it oppositely
  (Shapley ties within 0.01 ignored).
- H3 confirmed if the principal's largest share gap exceeds 0.05.
- H4 confirmed if, on the principal and the N = 3 market, the most strategically valuable party's structural
  share exceeds its strategic share.
