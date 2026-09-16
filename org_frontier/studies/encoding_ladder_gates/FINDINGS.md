# Encoding ladder gate family — findings

**Verdict: GATE_SPLITS_LADDER.** The literacy→algorithmacy flip and Φ=n−1
are **not** gate-robust. Three regimes at n=5:

1. **Monotone full-commit (AND / OR / NAND):** same ladder as before —
   assist grows multi-party core; full bind → whole triadic, Φ=4 (=n−1);
   COMMIT_READ holds.
2. **Parity (XOR / XNOR):** full bind **does** flip (n_core=5, whole
   triadic) but Φ collapses to **0.125** ≪ n−1; assist path breaks
   (idle-pad singleton is the major complex until full bind).
3. **Majority / mixed:** full bind stays **dyadic** (no multi-party
   major complex); no algorithmacy flip.

In-silico; binary exact IIT-4.0; designed n=5 per-gate ladders.
Hypotheses fixed in `hypotheses.md`. Extends `encoding_ladder_n5` /
`encoding_ladder_n6`. Ternary / residual / omit noted only.

## Per-gate summary

| gate | flip | Φ at flip | =n−1 | assist multiparty | COMMIT_READ |
|---|---|---:|---|---|---|
| AND | Y | 4 | Y | Y | HOLDS |
| OR | Y | 4 | Y | Y | HOLDS |
| NAND | Y | 4 | Y | Y | HOLDS |
| XOR | Y | 0.125 | N | N | HOLDS |
| XNOR | Y | 0.125 | N | N | HOLDS |
| MAJ (≥3/4) | N | — | N | Y† | HOLDS |
| MIXED (W1∧W2)∨(W3∧C) | N | — | N | Y† | HOLDS |

† Assist_W2 only (equals AND of two); later assist rungs do not grow the
AND-like core.

**Boundary step (AND/OR/NAND):** still `workers_*_Cidle → *_full`.  
**Parity:** flip at full bind only; Φ does not track n−1.  
**MAJ/MIXED:** no boundary — full bind is not algorithmacy.

## Hypotheses

| hypothesis | result |
|---|---|
| H1 flip + Φ=n−1 robust across gates | **REFUTED** |
| H2 some gates stay dyadic at full bind | **SUPPORTED** |
| H3 assist path changes with gate | **SUPPORTED** |

## Reading

PHI_TRACKS_NM1 is a **gate-family** result: it holds for AND, OR, and
NAND (monotone / De Morgan dual), not for parity or majority/mixed
commit encodings. COMMIT_READ_BOUNDARY still holds wherever membership
is testable — core membership tracks determination∩read even when Φ
collapses. Designed witnesses: AND_full (Φ=4), XOR_full (Φ=0.125),
MAJ_full (no flip).

## Limits

Designed n=5 ladders only; n=6 not repeated (cost). One MAJ threshold
(≥3/4) and one MIXED form. No organization measured.

## Best next experiment

Done: [`ladder_gate_panel/`](../ladder_gate_panel/) RULE_HOLDS_PANEL
(448/448). Next: role-target grain on another indeg. Skip residual /
cascade / ternary / omit-arc.

## Reproduce

```
python org_frontier/studies/encoding_ladder_gates/analyze_gates.py
```
(~1 min)
