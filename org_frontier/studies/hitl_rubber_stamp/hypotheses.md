# HITL rubber stamp — hypotheses (fixed before computing)

**Question (RESEARCH_AGENDA_50_V2 #39).** Human-in-the-loop AI: with
human, AI, and counterpart, under what coupling is the human in the
core versus a rubber stamp?

**Already known (cited, not reopened).**
- #37 PROTOCOL_IS_COMMIT / #38 TOOL_LIKE_INFERENCE — pointers only.
- Probe #76: observer and static veto stay out; veto+responsive joins.
- Probe #21: contestability/override can drop a bound party.
- `hmc_algo_boundary` COMMIT_READ: party ∈ core iff in S’s
  determination **and** reads S. Conceptual pointer only — not a
  construct-omit reopen.
- AI-MC / HMC discriminants (#15, #20) — unit-of-analysis pointers;
  not re-run.

**Universe.** Exact binary IIT-4.0 Φ. Primary nodes `(H, AI, S, C)` =
human, AI proposer, system commit, counterpart. In-silico Boolean
abstractions of HITL coupling — not live LLM calls.

**Definitions (fixed).**
- **H in core:** `"H" ∈ major_complex`.
- **determinant:** H appears in S’s update rule.
- **reads:** H’s update depends on S (`H'=S`).
- **rubber stamp:** H mirrors or idles while **absent** from S’s
  determination (post-hoc approve, idle approve, sticky approve,
  observe-only).
- **override:** S follows H (alone or as a forcing gate), displacing
  the AI∧C joint.

## Panel (designed)

| id | sketch | role |
|---|---|---|
| stamp_posthoc / idle / sticky / observer | H not in S; may read | rubber stamp |
| veto_only | S'=H∧AI∧C; H'=H | partial (commit, no read) |
| nocommit_read | S'=AI∧C; H'=S | partial (read, no commit) |
| veto_responsive / full_joint | S'=H∧AI∧C; H'=S | COMMIT_READ |
| override_force / OR | S←H forcing | override |
| advice_into_AI / ignored | H→AI or unused | advice |
| H_or_AI_and_C | substitutable H∨AI | non-pivotal |
| classical_WSC | (W,S,C) joint | instrument contrast |

Plus the 2×2 commit×read boundary sweep on the primary wiring.

## H1 — human joins when determinant + read (or override)

Every COMMIT_READ form (H in S and H'=S) has H in the major complex;
at least one override form has H in the core. Null: COMMIT_READ leaves
H out, or no override puts H in.

## H2 — rubber stamp excluded

Every rubber-stamp form has H **outside** the major complex. Null: any
stamp puts H in.

## H3 — partial coupling is the boundary

On the 2×2 (commit × read), **only** commit∧read puts H in; commit
without read and read without commit leave H out. Null: a partial cell
puts H in, or the full cell leaves H out.
