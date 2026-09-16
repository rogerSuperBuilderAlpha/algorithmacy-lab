# ladder_gate_properties — hypotheses (fixed before computing)

**Question.** Which Boolean properties of S’s determination gate predict
GATE_SPLITS_LADDER regimes A / B / C?

**Regimes (from `encoding_ladder_gates`).**
- **A:** flip + Φ = n−1; multiparty assist (AND / OR / NAND; NOR untested).
- **B:** flip + Φ ≪ n−1; broken assist (XOR / XNOR).
- **C:** no triadic flip (MAJ / MIXED).

**Universe.** Binary exact IIT-4.0. Labels `("W1","S","W2","W3","C")`
(n=5). Designed gates spanning property space; seven anchors included.
Primary measure: full joint bind (all outers in S, all read S). Assist_W2
recorded as secondary. Properties computed on the 4-input truth table:
weight, depends-on-all, monotone (all-inc or all-dec), unate, affine
(linear over GF(2)), canalizing.

**Proposed minimal rule (to test).**
```
if depends_on_all and affine:            → B
elif depends_on_all and monotone
     and wt ∈ {1, 15}:                   → A
else:                                    → C
```

## H1 — Regime A = monotone extremal

Among full-bind gates, regime A iff the gate is monotone (all-inc or
all-dec), depends on every input, and has Hamming weight ∈ {1, 2⁴−1}.
Null: some A gate violates this, or some non-A gate satisfies it.

## H2 — Regime B = affine full dependence

Regime B iff the gate is affine over GF(2) and depends on every input.
Null: mismatch either way.

## H3 — residual is Regime C

Every designed full-bind gate outside H1/H2 lands in Regime C (no
triadic n_core=5 flip). Null: a leftover gate flips with Φ=n−1 or
Φ≪n−1.

## H4 — weaker properties do not predict A

Canalizing alone, extremal weight alone, or unate∧canalizing∧extremal
weight **without** full monotonicity do **not** characterize A
(counterexample expected: AND with a negated literal). Null: those
weaker filters match A exactly.
