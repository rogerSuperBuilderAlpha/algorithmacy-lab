# event_crqa — findings

The behavioral instrument run on the v9 PyPhi PR/review history (`../event_series/`), monthly bins,
138 months (2014-12 to 2026-05): 104 author opens, 33 reviews, 71 merges.

| hypothesis | verdict | key numbers |
|---|---|---|
| bH1 the gate is the behavioral hub | confirmed | merge centrality 0.241 (highest of the three); shuffle-null mean 0.035, p = 0.0005 |
| bH2 the gate does not lead | confirmed | author→merge peak lag +0 months, review→merge +1; neither party led by the gate |
| bH3 author–merge is the behavioral spine | refuted | highest determinism is review–merge (0.958), above author–review (0.892) and author–merge (0.856) |
| bH4 behavior agrees with structure | confirmed | the behaviorally most-central role is the merge gate, the same role v9's major complex includes |

## The structural gate is the behavioral hub

The merge role carries the most prominent month-to-month coupling of the three (centrality 0.241, against
0.182 for authoring and 0.059 for reviewing), and that prominence is far above a time-shuffle null
(mean 0.035, p = 0.0005). The veto player v9 identified from the merge-actor distribution is independently
the behaviorally most-coupled role. Two instruments — exact Φ on the elicited triad and cross-recurrence on
the activity series — name the same party (bH4). This is the paired reading the recurrence program is for:
structure says the gate is irreducible, behavior says it is the hub.

## The gate follows, and the grain cannot resolve the lead

The peak lag from authoring to merging is zero months and from reviewing to merging one month; the gate
never leads. This is consistent with v9's directed but time-compressed lifecycle — the median open-to-merge
latency is zero days, so the open→merge order lives below the monthly grain and the behavioral lead-lag is
unresolved here, as bH2 anticipated. The behavioral instrument confirms the gate's centrality without
recovering the direction the event order already establishes.

## The spine is review–merge, not author–merge

The pre-registered guess that author–merge would be the most sustained coupling is refuted: review–merge is
(determinism 0.958), and author–merge is the lowest of the three (0.856). The roles that track each other
most tightly month to month are reviewing and merging — the gate moves with the review process, not with
the broader stream of authoring. This fits v9's later-period finding that a heavier review process spreads
the merge gate, and it sharpens it: review activity is the behavioral company the gate keeps.

**Caveats.** The determinism values are high across all pairs (0.86–0.96) because the quantized monthly
series share long runs of co-inactive months, so the absolute level reflects sparsity; the finding is the
*ordering* of the three pairs, not the magnitudes. A single project (N=1), monthly resolution on a
time-compressed lifecycle, three role-activity series rather than individual actors. Evidence about the
behavioral instrument on one real coordination, paired with the structural reading, not a population.

**Reproduce.** `~/iit-playground/venv-4.0/bin/python org_frontier/recurrence/event_crqa/analyze_crqa.py`
