# threshold_majority_template — hypotheses (fixed before computing)

**Question (RESEARCH_AGENDA_V3 #2).** Is **threshold / majority**
determination at n≥4 a new template, or does it always collapse into the
known redundancy-factors pattern (probes #10/#67/#117) once pivotality is
lost — even under topologies that restored triadicity for conjunctive hubs
(V2 #15–#20)?

**Already known (cited, not reopened).**
- **#10 / #67:** majority (2-of-3) factors → dyadic; no party pivotal.
- **#117:** on plain k-of-n hubs, only extremes (k=1 OR, k=all AND) keep
  the full core; every intermediate threshold factors.
- **V2 #15–#20 / V3 #4–#7:** shared-mediator AND merge, recurrent AND
  trees, necklace, spanning — restore or preserve triadicity / full cores
  under **conjunctive** determination. None tested majority on those
  carriers.
- Faithful conjunctive triad Φ=2.0. Five templates closed (V3 #1
  `FACTORS_INTO_FIVE`).

**Gap.** #117 shows the redundancy-factors pattern on the *plain hub*.
Whether a restored-triadicity *topology* rescues intermediate majority into
a new irreducible template is open.

**Universe.** Binary exact IIT-4.0. n≤5.

**Redundancy-factors pattern.** Intermediate threshold (1 < k < n_parties)
→ no full-core irreducible complex (dyadic / empty / incomplete). Extremes
keep full core at Φ = n−1.

**New majority template.** Some intermediate-threshold cell yields a
full-core triadic complex with a signature not explained as AND/OR extreme
or as a product of the five.

**Topologies tested.**
- Plain threshold hub (n=4,5) — #117 replicate.
- Shared-mediator AND merge (V2 #16 carrier) vs same carrier with majority
  of party bits.
- Recurrent breadth-3 AND tree (V2 #15 carrier) vs apex majority 2-of-3.

## H1 — instrument + plain-hub redundancy pattern

Faithful triad Φ=2.0. Plain hub n=4: k=1 and k=3 full-core Φ=3; k=2
factors. Plain hub n=5: an intermediate k factors; an extreme keeps full
core.

## H2 — restored-AND carriers still bind under conjunctive seats

Shared-mediator AND merge: full-core triadic. Recurrent AND b=3: full-core
triadic. (Topology controls that restore triadicity under AND.)

## H3 — majority on restored carriers does not rescue

Shared-mediator with majority-of-parties and recurrent apex-majority both
**factor** (no full-core triadic). Topology that restores triadicity under
AND does not mint a majority template.

## H4 — panel verdict

H1–H3 hold → `COLLAPSES_TO_REDUNDANCY`.
H3 fails (majority rescued to full-core triadic) → `MAJORITY_NEW_TEMPLATE`
  if the Φ signature is novel, else `TOPOLOGY_RESCUES_MAJ`.
H1 or H2 fails → `CONTROLS_FAIL`.
