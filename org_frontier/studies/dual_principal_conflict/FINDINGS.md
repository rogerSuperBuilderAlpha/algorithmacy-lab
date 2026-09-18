# Dual principal conflict — findings

**Verdict: CONFLICT_ENCODING.** With two principals, whose core wins
is set by the **conflict encoding** — not a single universal winner.
Extractive asymmetry → one principal dominates (`{S,A}` / `{S,B}`).
Joint COMMIT_READ / joint principal commits → **stable shared core**
(both A and B in). Unresolved agenda conflict, majority, and
substitutable gates → **collapse** (neither principal in, or empty
complex). Extends single-principal bidirectionality (`principal/`).

In-silico; candid N (designed n=5 panel). Hypotheses fixed in
`hypotheses.md`. Cited: `principal/`; #74/#78; #37 pointer only.
Closed lanes stay closed.

## Hypotheses

| H | result |
|---|---|
| H1 one principal dominates | **SUPPORTED** (3 forms) |
| H2 stable shared/joint core | **SUPPORTED** (6 forms) |
| H3 collapse / both out | **SUPPORTED** (4 forms) |

## Panel (selected)

| form | Φ | core | reading |
|---|---:|---|---|
| single_gate_mon | 3 | {W,S,C,A} | single-P contrast |
| extract_A / B_wins | 2 | {S,A} / {S,B} | **dominate** |
| A_full_B_mon | 3 | {W,S,C,A} | asymmetric dominate |
| both_gate_AND | 4 | {W,S,C,A,B} | **shared** full |
| both_extract_AND / XOR / OR / NAND | 0.5–2 | {S,A,B} | **shared** principal pair |
| both_idle / both_gate_OR | 2 | {W,S,C} | principals out |
| agenda_conflict / maj_2of | 0 | — | **collapse** |

## Contrast to single-principal

Single gates+monitors joins as `{W,S,C,A}` (B idle). A second
principal does not automatically share that core: monitor-only B stays
out (`A_full_B_mon`); extractive S←A ejects parties and B
(`extract_A_wins`); only joint determination + read puts both in.

## Reading

Dual corporate authorship is encoding-sensitive. Conflict resolved by
one extractive commit hands the irreducible core to that principal.
Conflict resolved by joint commit+read builds a shared principal-bearing
complex. Conflict left as opposing agendas or majority factorization
destroys principal standing in the major complex. Same bidirectional
cut as the single-principal study, applied to two authors.

## Limits

Boolean n=5 designed panel; no organization measured; Φ magnitudes
ordinal across different cores.

## Best next

**#30** — endogenous coalition formation (alt **#32** rival platforms).

## Reproduce

```
python org_frontier/studies/dual_principal_conflict/analyze_dual.py
```
(~15 s)
