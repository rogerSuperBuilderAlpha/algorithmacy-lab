# Agent tool core — hypotheses (fixed before computing)

**Question (RESEARCH_AGENDA_50_V2 #38).** Does a tool an agent calls
join the core when the agent acts on its output, like the inference
model (#4, #9)?

**Already known (cited, not reopened).**
- Probe #4: unused inference M is a sink (out). Pure act `W'=M` leaves
  M out of the major complex (core `{S,C}`). Blended `W'=S∧M` puts M
  in as `{W,S,M}` and **displaces** C.
- Probe #9: over 64 forms, C and M never coexist in the core —
  displacement is categorical.
- #37 PROTOCOL_IS_COMMIT: protocol joins iff joint commit + read
  (COMMIT_READ). Pointer only — conceptual bridge for “node joins
  when acted into the determination,” not reopened.
- Formal / stoch–temporal / estimation / construct-omit closed.

**Universe.** Exact binary IIT-4.0 Φ. Nodes `(A, S, C, T)` = agent,
system commit, counterpart, tool — the #4 `(W,S,C,M)` panel under
relabeling. In-silico Boolean abstractions of tool use; not live LLM
API calls.

**Definitions (fixed).**
- **T in core:** `"T" ∈ major_complex`.
- **acts on tool:** A’s update depends on T (`A'=T` or `A'=S∧T`).
- **reciprocal dependence:** T’s update depends on A (`T'=A` or a
  gate of A), not only on S/C/self.
- **read-only / unused:** T updates from the world but A ignores T
  (`A'=S` or exogenous; no A←T edge in the rule).

## Panel (designed)

| id | sketch | role |
|---|---|---|
| tool_unused | T'=S; A'=S | unused sink |
| tool_exo_unused | T'=T; A'=S | exogenous unused |
| tool_sink_from_A | T'=A; A'=S | write-only sink |
| tool_used_pure | A'=T; T'=S | act, no reciprocity |
| tool_blended | A'=S∧T; T'=S | act, no reciprocity |
| tool_call_used | A'=T; T'=A | act + reciprocity |
| tool_call_blended | A'=S∧T; T'=A | act + reciprocity |
| tool_exo_used / blended | A acts; T self-loop | exo act |
| tool_in_commit | S'=A∧C∧T; all ←S | COMMIT_READ contrast |
| inference_blended_WSCM | W'=S∧M; M'=S | #4 isomorphism check |

## H1 — joins iff acts + reciprocity

T is in the major complex if and only if the agent acts on T **and**
T reciprocally depends on A. Null: a form with act+reciprocity leaves
T out, or a form without reciprocity puts T in.

## H2 — read-only tool never joins

Every unused / exogenous-unused / write-only-sink form has T outside
the major complex. Null: any such form puts T in.

## H3 — tool can join without reciprocity

At least one panel form puts T in the core while T does **not**
depend on A (T tracks S or self only). Null: every T-in-core form is
reciprocal.
