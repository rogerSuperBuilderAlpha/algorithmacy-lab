# hybrid_ff_recurrent_seam — hypotheses (fixed before computing)

**Question (RESEARCH_AGENDA_V3 #7).** Is there a **hybrid feedforward+recurrent**
seam (one recurrent cycle feeding a feedforward chain) whose major-complex
locus **violates** V2 #15’s closure-decides-locus rule?

**Already known (cited, not reopened).**
- **V2 #15 / `mediator_hierarchy_census`:** recurrent AND trees — major complex
  spans every occupied level; feedforward hub chains — complex is **top-local**
  (H0,P0 only). **Closure decides the level locus** (H5 WIN).
- **V2 #16–#20 / V3 #4–#6:** shared-mediator merge, necklace landmark-or-collapse,
  ring-of-hubs factors, shared-mediator k-lift Φ=2k — none reopen the pure
  recurrent-vs-FF locus contrast.
- Faithful triad Φ=2.0. Ternary / residual-cascade / M3 noted only.

**Gap.** #15 separates pure recurrent from pure feedforward. The **hybrid** —
a recurrent cycle that feeds a feedforward AND (or OR) chain — was not on that
grid. Does the locus still truncate at the first FF seam, or does recurrent
closure pull the FF tail into the major complex?

**Universe.** Binary exact IIT-4.0. n≤6.

**Zones.** Each hybrid tags nodes as `recurrent` (cycle / tree with leaf↔apex
closure) or `ff` (downstream hub+party under a one-way AND/OR gate reading the
recurrent apex).

**Closure holds** = major complex ⊆ recurrent zone (FF tail excluded), and the
recurrent zone is non-empty in the core.
**Closure violated** = major complex intersects the FF zone (FF node in core).

## H1 — instrument + pure controls

Faithful triad: triadic, core Φ=2.0. Hub-chain L=2 (q148 / #15): core ⊆ {H0,P0}
(top-local; FF mid excluded).

## H2 — hybrid AND seams: locus vs closure rule

On each hybrid AND cell (triad→FF; recurrent tree d=1,b=2→FF), the major
complex either **holds** (core ⊆ recurrent zone) or **violates** (core meets FF
zone). Decision for the AND panel:
- all hold → AND_HOLDS;
- all violate → AND_VIOLATES;
- mixed → AND_MIXED.

## H3 — OR seam contrast (secondary)

Hybrid triad→FF with OR gate at the seam: report hold/violate the same way.
Does not alone decide the panel token; recorded for reading.

## H4 — panel verdict

H1 holds, and H2 names one of {AND_HOLDS, AND_VIOLATES, AND_MIXED} → token:
- `CLOSURE_HOLDS_HYBRID` if AND_HOLDS;
- `CLOSURE_VIOLATED_HYBRID` if AND_VIOLATES;
- `MIXED_SEAM_LOCUS` if AND_MIXED;
- `CONTROLS_FAIL` if H1 fails.
