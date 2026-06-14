# Q59 — findings

## Hypothesis verdicts

| Hypothesis | Verdict | Key result |
|---|---|---|
| H1 — cross-edge shared severance | confirmed | 16/16 cross-edge in both tied and excluded severed sets; 0 exclusive. |
| H2 — symmetric-difference size | confirmed | 16/16 at |only_tied|=3, |only_excl|=1, symdiff=4. |
| H3 — cross-edge subtraction equalizes | refuted | 0/16 equal after cross subtraction; adj 3 vs 1 on all pairs. |
| H4 — mediator edges in recipient-only diff | confirmed | 16/16 with 2 mediator edges in only_tied; adj ratio 3.0, spread 0. |
| H5 — recipient-template gate invariance | confirmed | 8/8 worker and 8/8 counterpart match fixed edge templates. |

## Reading

Q58 #190 counted severed connections without naming directed edges. The back-channel cross-edge appears in
both the recipient and non-recipient min-norm severed sets on every pair (195). The symmetric difference is
exactly four directed edges: three only in the recipient cut, one only in the non-recipient cut (196).
Subtracting the shared cross-edge leaves a 3-versus-1 gap on all sixteen pairs (197 refuted). Exactly two
mediator-incident edges sit in the recipient-only difference, fixing the adjusted ratio at 3.0 (198).
Worker-recipient pairs use template {S→W, W→C, W→S} vs {C→S}; counterpart pairs use {C→S, C→W, S→C} vs
{W→S}; XOR and XNOR preserve these templates (199). The 4-versus-2 severed-connection split is not
accounted for by cross-edge placement alone; mediator-edge severance in the recipient-only difference is
the residual source of asymmetry.

## Validation gap

Deterministic n=3 Boolean models at finest grain with synchronous update. Directed-edge labels follow
PyPhi cut-matrix indexing on the three-node connectivity matrix.

## Reproduce

```bash
python -m org_frontier.questions.q59_directed_cut_edges.probe_cross_edge_shared
python -m org_frontier.questions.q59_directed_cut_edges.probe_symdiff_size
python -m org_frontier.questions.q59_directed_cut_edges.probe_cross_subtract_equal
python -m org_frontier.questions.q59_directed_cut_edges.probe_mediator_only_diff
python -m org_frontier.questions.q59_directed_cut_edges.probe_recipient_template
```
