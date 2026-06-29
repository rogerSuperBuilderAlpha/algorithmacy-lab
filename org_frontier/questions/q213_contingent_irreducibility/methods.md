# Q213 — Stage 4 methods

For each hypothesis: the form, the measure, the controls, and the decision rule fixed before the run. A
reader should reproduce every test from this file alone.

## Shared infrastructure
- Verdict / Φ / major complex: `probes/lib.py` (`verdict`, `major_complex`), `classifier.classifier`
  (`PHI_EPS`).
- The classifier: `classifier/contingency.py` (`contingency_test`, `add_bypass`, `ContingencyResult`).
- Python: run from the repo root with the project venv (`venv-4.0`), `PYPHI_WELCOME_OFF` set.

## The instrument: the bypass-counterfactual
`contingency_test(rules, labels, party, downstream, upstream, mode)` computes the major complex of the
constrained system, restores the forbidden direct edge with `add_bypass`, recomputes, and classifies:
- `mode="replace"` — downstream reads upstream instead of its mediated source (disintermediation).
- `mode="add"` — downstream reads upstream in addition (a parallel back-channel), downstream' = original ∨ upstream.

`kind` is: reducible if the party is not in the constrained core; contingent if it is in the core but leaves
under the bypass; partial if it stays but whole-system Φ_MIP drops by more than PHI_EPS; intrinsic if it stays
with margin ≈ 0. `margin` = Φ_MIP(constrained) − Φ_MIP(bypass).

## Instrument control (run first)
The single conjunctive triad (W,S,C) with W'=S, S'=W∧C, C'=S. Must read triadic at Φ=2.000000 before any
classification is trusted.

## The four forms
| form | labels | rules | bypass |
|---|---|---|---|
| conjunctive clearinghouse | W,S,C | W'=S, S'=W∧C, C'=S | C reads W (replace) |
| car dealer | M,D,B | M'=B, D'=M, B'=D | B reads M (replace) |
| clearinghouse + back-channel | W,S,C | W'=S, S'=W∧C, C'=S | C'=S∨W (add) |
| free conduit | M,D,B | M'=B, D'=M, B'=M | B reads M (replace) |

## H1 test
- **Form:** conjunctive control. **Measure:** verdict. **Decision rule:** triadic, Φ=2.0.

## H2 test
- **Form:** constrained car dealer. **Measure:** verdict + `major_complex`. **Decision rule:** triadic, D in core.

## H3 test
- **Form:** car dealer, `contingency_test(party=D, downstream=B, upstream=M, mode=replace)`.
- **Decision rule:** kind="contingent"; D not in bypass core; margin = 2.0.

## H4 test
- **Form:** conjunctive clearinghouse, `contingency_test(party=S, downstream=C, upstream=W, mode=replace)`.
- **Decision rule:** kind="intrinsic"; S in bypass core; margin = 0.0.

## H5 test
- **Forms:** clearinghouse + back-channel, `contingency_test(party=S, downstream=C, upstream=W, mode=add)`;
  free conduit, `contingency_test(party=D, downstream=B, upstream=M, mode=replace)`.
- **Decision rule:** partial form kind="partial" with 0 < margin < 2.0; free conduit kind="reducible" with D
  not in core; margins order contingent ≥ partial > intrinsic ≈ reducible.
