# Formal vs informal cut — findings

**Verdict: CUTS_ACROSS.** The formal-vs-informal distinction does not
map onto dyadic/triadic. Formal spans both (commit gate vs
convey/handoff); informal spans both (lateral idle vs back-channel/ring).
Alignment 0.333.

In-silico. Exact binary IIT-4.0. N=3. Hypotheses fixed in
`hypotheses.md`. #43–#45 pointers only.

## Operationalization

- **Formal:** prescribed S-channel; no lateral W↔C in the rules.
- **Informal:** lateral W↔C mutual adjustment (back-channel, ring, or
  idle-S peer tie).

H1 predicted formal→triadic, informal→dyadic.

## Alignment table

| slug | class | structure | Φ | vs H1 |
|---|---|---|---|---|
| F_commit_gate | formal | triadic | 2.0 | OK |
| F_convey_gate | formal | dyadic | 0.0 | **MISMATCH** |
| F_hierarchy_handoff | formal | dyadic | 0.0 | **MISMATCH** |
| I_lateral_idle_S | informal | dyadic | 0.0 | OK |
| I_backchannel | informal | triadic | 1.0 | **MISMATCH** |
| I_copy_ring | informal | triadic | 2.0 | **MISMATCH** |

## Hypotheses

| H | result |
|---|---|
| H1 formal↔triadic / informal↔dyadic | **REFUTED** |
| H2 cuts across | **SUPPORTED** |
| H3 partial alignment only | **SUPPORTED** |

## Reading

A prescribed channel is irreducible only when it jointly commits; a
lateral tie is irreducible when it closes a cycle or back-channel bind.
The formal/informal label does not decide. Same through-line as #43
(Thompson labels) with a different org-theory carving.

## Best next

Outside CV — agenda **J #47** (scaling-law closed forms), or other open
lanes. Construct-validity arc **closable**.

## Reproduce

```
python org_frontier/studies/formal_informal_cut/analyze_cut.py
```
