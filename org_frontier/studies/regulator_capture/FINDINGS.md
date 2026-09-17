# Regulator capture — findings

**Verdict: SHARP_FULL_CAPTURE.** Oversight becomes capture at a **sharp
coupling cut**, not a smooth membership glide. Under mutual gate
`S'=W∧C∧R`, reading `R'=S` (or any proper subset of {W,S,C}) keeps
**oversight** `{W,S,C,R}` or a partial hollow. Only full
`R'=W∧S∧C` collapses the major complex to **capture** `{S,R}`.
Extractive `S←R` is the same capture core. No-gate controls keep R out
at every read set. Extends #76/#111 with the principal-style hollowing
cut.

In-silico; candid N (designed n=4 panel + 8+8 read sweep). Hypotheses
fixed in `hypotheses.md`. Cited: #76/#111; principal FINDINGS pointer;
#29–#32 pointers only. Closed lanes stay closed.

## Hypotheses

| H | result |
|---|---|
| H1 sharp capture threshold | **SUPPORTED** (n_reads 2→3) |
| H2 smooth membership shift | **REFUTED** |
| H3 stays out / always in | **REFUTED** |

## Boundary (gated `S'=W∧C∧R`)

| R reads | kind | Φ | core |
|---|---|---:|---|
| static | out | 2 | {W,S,C} |
| W or C alone | partial | 2 | {W,S,R} / {S,C,R} |
| S | **oversight** | 3 | {W,S,C,R} |
| any pair | **oversight** | 2 | {W,S,C,R} |
| W∧S∧C | **capture** | 2 | **{S,R}** |

No-gate `S'=W∧C`: R out on 8/8 cells — the gate is necessary.

## Named witnesses

| form | kind | core |
|---|---|---|
| #76 observer / veto_only | out | {W,S,C} |
| #76 veto_resp | oversight | {W,S,C,R} Φ=3 |
| extractive S'=R / S'=R∨(W∧C) | capture | {S,R} |
| full mutual R'=W∧S∧C | capture | {S,R} |
| #111 two joint-veto | oversight | {W,S,C,R1,R2} Φ=4 |

## Reading

A regulator that both gates and is gated is not yet captured. Capture
is the step where the platform **fully** determines the regulator —
every party plus the commit enters R’s update — and the irreducible
core contracts to system+regulator. Weaker mutual coupling (R tracks
S, or S plus one party) is still oversight in the #76 sense. Toothless
watchdogs stay out; fully platform-determined “regulators” are
structurally captured.

## Limits

Boolean n=4 designed sweep; AND over reads only; no organization
measured; Φ ordinal across different cores.

## Best next

**#34** — algorithmic transparency (**done** — OPEN_ACT_CUT; next **#35**).

## Reproduce

```
python org_frontier/studies/regulator_capture/analyze_capture.py
```
(~15 s)
