# Graded commit verdict — findings

**Verdict: SHARP_CLASS_GRADED_PATH.** A graded commit
(`S'=min(W,C)`, ternary) keeps **discrete** structure labels
(NULL / DYADIC / TRIADIC) while Φ and major-complex membership
**grade** with commit level L on the diagonal `(L,L,L)`.

In-silico. Exact IIT-4.0 via `pyphi_iit4_mv`. N=3, k=3. Hypotheses
fixed in `hypotheses.md`. Cited: agenda #1; probes #11–#12.

## Binary control

AND triad `@ (1,1,1)`: stock and overlay **TRIADIC Φ=2**, core {W,S,C}.

## Faithful diagonal

| L | state | structure | n_core | Φ | core |
|---|---|---|---|---|---|
| 0 | (0,0,0) | NULL | 0 | 0 | ∅ |
| 1 | (1,1,1) | DYADIC | 2 | 0.390 | {W,S} |
| 2 | (2,2,2) | TRIADIC | 3 | 3.170 | {W,S,C} |

## Hypotheses

| H | result |
|---|---|
| H1 structure class stays sharp | **SUPPORTED** |
| H2 Φ grades with L | **SUPPORTED** |
| H3 core membership grades with L | **SUPPORTED** |

## Reading

The dyadic/triadic *label* does not smear into a continuous verdict — each
state still gets one sharp class. What grades is the *path*: as commit
level rises, NULL → DYADIC → TRIADIC with Φ rising. Agenda #1’s
state-dependence is the L=1 vs L=2 slice of this path. Off-diagonal
spots show mediator level S and party min(W,C) can pull structure apart
(e.g. `(1,2,1)` TRIADIC vs `(2,1,2)` DYADIC).

## Best next

**#3** mixed-radix mediator (binary parties, ternary S).

## Reproduce

```
python org_frontier/studies/graded_commit_verdict/analyze_graded.py
```
