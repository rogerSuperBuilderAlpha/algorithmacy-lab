# AI / multi-agent arc — #37–#41 synthesis

Exact binary IIT-4.0 Φ; in-silico Boolean / tabular proxies (not live
LLM calls, not deep MARL unless noted). Formal / stoch–temporal /
estimation / construct-omit stay closed except as pointers
(COMMIT_READ, #69, #98/#107).

## Lane status: **CLOSABLE**

| # | study | verdict | one line |
|---|---|---|---|
| 37 | [`agent_protocol_triad/`](studies/agent_protocol_triad/) | **PROTOCOL_IS_COMMIT** | Protocol joins iff joint commit + read; no human required |
| 38 | [`agent_tool_core/`](studies/agent_tool_core/) | **TOOL_LIKE_INFERENCE** | Tool joins like #4/#9 blend; unused out; displaces C |
| 39 | [`hitl_rubber_stamp/`](studies/hitl_rubber_stamp/) | **HUMAN_COMMIT_READ** | HITL human in iff COMMIT_READ; stamps out |
| 40 | [`ai_fidelity_displace/`](studies/ai_fidelity_displace/) | **SHARP_FULL_DISPLACE** | Policy-model displaces C only at full fidelity |
| 41 | [`marl_emergent_learn/`](studies/marl_emergent_learn/) | **EMERGENT_NULL** | Emergent verdict ̸↔ learnability; extends #98/#107 |

## What the lane shows

1. **Membership cuts transfer.** Protocol nodes, tools, and HITL
   humans enter the major complex by the same bidirectional
   constraining pattern (commit/act + read), not by label. Rubber
   stamps, unused tools, and conveyors stay out.
2. **Displacement is sharp.** Learned / inferred stand-ins for the
   counterpart join and eject C at a discrete fidelity threshold, not
   by a smooth Φ glide (#40 / #69).
3. **Structure ≠ learnability.** Neither the designed form’s verdict
   (#98/#107) nor the **emergent** post-learning verdict (#41)
   predicts whether tabular agents solve the commit. Successful
   learners often induce open-loop factored policies.

## Exact limits

- In-silico Boolean abstractions and a **tabular** stateful Q-learning
  proxy — not production multi-agent RL, not field orgs, not
  consciousness claims.
- #41 association only; no causal identification.
- One precise optional gap **outside** this lane’s close: whether
  *deep* MARL (value factorization, continuous obs) recovers a
  structure–learnability link the tabular proxy nulls. Not required
  to close #37–#41.

## Reproduce

```
python org_frontier/studies/agent_protocol_triad/analyze_protocols.py
python org_frontier/studies/agent_tool_core/analyze_tools.py
python org_frontier/studies/hitl_rubber_stamp/analyze_hitl.py
python org_frontier/studies/ai_fidelity_displace/analyze_fidelity.py
python org_frontier/studies/marl_emergent_learn/analyze_marl.py
```
