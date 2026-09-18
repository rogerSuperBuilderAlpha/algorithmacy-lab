# Agent tool core — findings

**Verdict: TOOL_LIKE_INFERENCE.** A tool joins the major complex the
same way an inference model does (#4, #9): unused / read-only stays
out; pure `A'=T` leaves T outside the major complex; blended
`A'=S∧T` puts T in as `{A,S,T}` and **displaces** C. Reciprocity is
neither necessary (blend joins without `T←A`) nor always sufficient
(`tool_call_blended` acts+reciprocates yet T stays out). COMMIT_READ
(tool in S’s determination) is a separate join path.

In-silico; candid N (designed Boolean panel). Hypotheses fixed in
`hypotheses.md`. Cited: #4/#9; #37 PROTOCOL_IS_COMMIT (pointer only).
Formal / stoch–temporal / estimation / construct-omit closed.

## Hypotheses

| H | result |
|---|---|
| H1 joins iff acts + reciprocity | **REFUTED** |
| H2 read-only tool never joins | **SUPPORTED** |
| H3 can join without reciprocity | **SUPPORTED** |

## Panel

| form | whole | Φ | core | T in | note |
|---|---|---:|---|:---:|---|
| tool_unused / exo_unused / sink | dyadic | 2 | {A,S,C} or {S,C} | no | H2 |
| tool_used_pure | triadic | 2 | {S,C} | no | act alone |
| tool_blended | triadic | 2 | {A,S,T} | **yes** | displaces C |
| tool_call_used | dyadic | 2 | {A,T} | **yes** | recip dyad |
| tool_call_blended | triadic | 2 | {S,C} | no | act+recip fails |
| tool_exo_used / blended | dyadic | 2 | ≤3 | no | exo act |
| tool_in_commit | triadic | 3 | {A,S,C,T} | **yes** | COMMIT_READ |
| inference_blended_WSCM | triadic | 2 | {W,S,M} | **yes** | ≅ blended |

## Minimal boundary edits

- Unused → blended (`A'=S` → `A'=S∧T`): T enters; C exits.
- Blended → pure (`A'=S∧T` → `A'=T`): T exits major complex.
- Add reciprocity alone (`T'=S` → `T'=A` with `A'=T`): dyadic `{A,T}`,
  triad collapses.
- Put T in S (`S'=A∧C` → `S'=A∧C∧T`, all read S): full four-node core
  without `A←T`.

## Reading

Calling a tool is not enough. The agent must keep the system signal
in the act (`A'=S∧T`) for the tool to join the coordination core the
way a folk model does — and that join displaces the counterpart.
Reciprocal tool calls can form a private `{A,T}` dyad that leaves the
counterpart–system pair as a separate complex. Feeding the tool into
the commit (COMMIT_READ) joins without that private loop. H1’s
acts+reciprocity iff is the wrong cut; the #4 blend/displacement cut
is the right one.

## Limits

Boolean abstractions of tool use; n=4; no live LLM/tool API; no
organization measured.

## Best next

**#39** — HITL rubber-stamp (human in core vs stamp). Alternate:
**#40** online-learning displacement.

## Reproduce

```
python org_frontier/studies/agent_tool_core/analyze_tools.py
```
(~5 s)
