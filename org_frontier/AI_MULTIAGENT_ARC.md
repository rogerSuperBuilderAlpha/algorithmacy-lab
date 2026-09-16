# AI / multi-agent arc — #37–#41 working picture

Short spine for the AI lane on `RESEARCH_AGENDA_50_V2` (PR #739).
Exact binary IIT-4.0 Φ; in-silico Boolean abstractions (not live LLM
calls). Formal / stoch–temporal / estimation / construct-omit stay
closed except as pointers (commit laws, COMMIT_READ, encoding ladders).

## #37 status

[`studies/agent_protocol_triad/`](studies/agent_protocol_triad/)
→ **PROTOCOL_IS_COMMIT**

Protocol design sets dyadic vs triadic by the same joint-commit /
COMMIT_READ cut as human mediation (#88). Negotiation **can** be
triadic with only (A,P,B) — no human required. Relay/broadcast stay
dyadic; joint AND/OR/NAND/XOR are protocol-triadic.

## #38 status

[`studies/agent_tool_core/`](studies/agent_tool_core/)
→ **TOOL_LIKE_INFERENCE**

A called tool joins like the inference model (#4/#9): unused out;
pure act out of major complex; blended act joins and displaces C.
Reciprocity is neither necessary nor always sufficient. COMMIT_READ
(tool in S) is a separate join path. H1 acts+reciprocity iff
**REFUTED**; H2/H3 hold.

## #39 status

[`studies/hitl_rubber_stamp/`](studies/hitl_rubber_stamp/)
→ **HUMAN_COMMIT_READ**

HITL human joins iff in S’s determination and reads S (COMMIT_READ /
#76). Rubber stamps stay out. Partial cells (veto-only,
read-without-commit) are the boundary. Override → dyadic `{H,S}`.

## Best next

**#40** online-learning displacement (alt **#41** MARL).

## Reproduce

```
python org_frontier/studies/agent_protocol_triad/analyze_protocols.py
python org_frontier/studies/agent_tool_core/analyze_tools.py
python org_frontier/studies/hitl_rubber_stamp/analyze_hitl.py
```
