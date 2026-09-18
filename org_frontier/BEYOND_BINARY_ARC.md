# Beyond-binary arc — #1–#4 working picture

Short spine for the beyond-binary lane on `RESEARCH_AGENDA_50_V2`
(PR #739). Prefer exact IIT-4.0 Φ. PE / AI / formal / stoch /
estimation / construct-omit stay closed except as pointers.

## Instrument status

| attempt | result |
|---|---|
| Stock `feature/iit-4.0` | rejects ternary SBS |
| Overlay M1 SBS ingest | **GREEN** (`third_party/pyphi_iit4_mv`) |
| Overlay M2 exact Φ | **GREEN** (binary regression Φ=2 match) |
| Path (B) embeddings | rejected |
| `pyphi@nonbinary` | rejected |

**CI-off is not a fix** (`int(log2)` trap). Overlay does not use it.

## #1 status

| study | verdict |
|---|---|
| `ternary_pivotality/` | **TWO_CONDITION_STATE_DEPENDENT** |

At `(2,2,2)` two-condition survives; at `(1,1,1)` faithful core shrinks.

## #2–#4

**Unblocked** on the overlay (instrument ready). Run next.

## Best next

**#2** graded commit verdict; **#3** mixed-radix mediator; expand
ternary state sweep.

## Reproduce

```
python third_party/pyphi_iit4_mv/smoke_m2.py
python org_frontier/studies/ternary_pivotality/analyze_pivot.py
```
