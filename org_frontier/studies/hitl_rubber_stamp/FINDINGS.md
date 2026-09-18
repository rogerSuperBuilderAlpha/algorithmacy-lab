# HITL rubber stamp — findings

**Verdict: HUMAN_COMMIT_READ.** In a HITL loop (human, AI proposer,
system commit, counterpart), the human joins the major complex **iff**
in S’s determination and reads S — the same COMMIT_READ cut as
regulator #76 / encoding ladders. Rubber stamps stay out. Static veto
and read-without-commit are the partial boundary. Override puts H in a
dyadic `{H,S}`.

In-silico; candid N (designed Boolean panel + 2×2 sweep). Hypotheses
fixed in `hypotheses.md`. Cited: #76; COMMIT_READ pointer; #37/#38
pointers only. Formal / stoch–temporal / estimation / construct-omit
closed.

## Hypotheses

| H | result |
|---|---|
| H1 joins on COMMIT_READ / override | **SUPPORTED** |
| H2 rubber stamp excluded | **SUPPORTED** |
| H3 partial coupling is the boundary | **SUPPORTED** |

## Panel

| form | whole | Φ | core | H in |
|---|---|---:|---|:---:|
| stamp_posthoc / idle / sticky / observer | dyadic | 2 | {AI,S,C} or {S,C} | no |
| veto_only (commit, no read) | dyadic | 2 | {AI,S,C} | no |
| nocommit_read | dyadic | 2 | {AI,S,C} | no |
| veto_responsive / full_joint | triadic | 3 | {H,AI,S,C} | **yes** |
| override_force / OR | dyadic | 2 | {H,S} | **yes** |
| advice_into_AI / ignored | — | 2 | {S,C} | no |
| H∨AI ∧ C (non-pivotal) | dyadic | 2 | {S,C} | no |

## Boundary 2×2

| | read | no read |
|---|---|---|
| **in commit** | H in `{H,AI,S,C}` Φ=3 | H out |
| **not in commit** | H out | H out |

## Minimal edits / rubber-stamp witness

- **Stamp → in-core:** put H in S (`S'=AI∧C` → `S'=H∧AI∧C`) **and**
  keep `H'=S`. One-sided edits fail (veto_only, nocommit_read).
- **Rubber-stamp witness:** `stamp_posthoc` — H mirrors S after the
  fact; core `{AI,S,C}`; H outside.
- **Override:** `S'=H` ejects AI and C from the major complex.

## Reading

A HITL “approval” that does not gate the commit is a rubber stamp —
structurally outside the coordination it appears to authorize. The
human enters only through bidirectional constraining coupling with the
commit (COMMIT_READ), or by overriding it into a private `{H,S}` dyad.
Advice into the AI and substitutable H∨AI gates do not put H in.
Matches probe #76’s observer / static-veto / veto+responsive ladder.

## Limits

Boolean abstractions of HITL; n=4; no live LLM; no organization
measured.

## Best next

**#40** — online-learning displacement (does learned policy displace
C?). Alternate: **#41** MARL emergent structure vs learnability.

## Reproduce

```
python org_frontier/studies/hitl_rubber_stamp/analyze_hitl.py
```
(~5 s)
