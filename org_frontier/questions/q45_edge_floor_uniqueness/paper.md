# Conjunctive uniqueness at the edge floor

<code + data: org_frontier/questions/q45_edge_floor_uniqueness/ ; probes #145–#149 in probes/PROBES.md>

## Abstract

Probe #30 established that every irreducible strict-mediation form at n=3 sits at exactly four causal edges,
the 2(n−1) floor. Agenda question #48 asks whether the conjunctive (AND) hub is the unique form achieving
its integrated-information ceiling at that lean wiring. This study tests five pre-registered hypotheses on
the 256 strict-mediation family and the full 4096 n=3 wiring space. All 24 triadic family forms sit at the
four-edge floor (H1, confirmed). Sixteen monotone triadic forms reach Φ = 2.0 there, but only two use an
AND commit — the other fourteen use OR, NOR, NAND, or implication variants (H2, refuted). All eight parity
forms saturate their own ceiling at Φ = 0.5 on the same floor (H3, confirmed). OR binds triadically in two
of sixteen OR-labelled strict-mediation forms (H4, refuted). Across the full wiring space, 192 triadic
forms at four edges reach Φ = 2.0, and 190 are not strict-mediation AND (H5, refuted). Uniqueness at the
edge floor is a class property — monotone versus parity — not a property of the AND commit alone.

## Introduction

Irreducible coordination through a single mediator carries a fixed wiring cost. Probe #30 found that every
triadic form in the n=3 strict-mediation family uses exactly four causal edges: the joint determination
reads both parties and each party reads the determination back. Probes #115 and #116 established two scaling
laws — conjunctive Φ = n−1 and parity Φ = 2^(2−n) — and probe #113 mapped the sixteen high-Φ triadic
forms to monotone commits and the eight low-Φ forms to parity commits. Agenda question #48 asks a sharper
question: is the AND hub the *only* commit that achieves its ceiling at the 2(n−1) edge floor, or do other
determination types share or compete for that budget?

The IIT literature treats integrated information as irreducibility over the minimum information partition
(`balduzzi2008integrated`; `albantakis2023iit4`). Coordination theory motivates lean joint determination as
the structural minimum for binding multiple parties (`malone1994interdisciplinary`; `thompson1967organizations`).
This study connects the two: at the leanest wiring that supports irreducibility, which Boolean commits
saturate which Φ ceilings?

## Hypotheses

Five hypotheses were fixed before computation (`hypotheses.md`).

**H1.** Every triadic strict-mediation form has exactly four edges.

**H2.** Every triadic form at Φ = 2.0 uses an AND commit (S-index 1).

**H3.** Every parity triadic form has four edges and Φ = 0.5.

**H4.** No OR-commit form in strict mediation is triadic.

**H5.** Every triadic form in the 4096 wiring space with four edges and Φ = 2.0 is strict-mediation AND.

## Methods

Exact IIT-4.0 Φ via PyPhi on n=3 deterministic Boolean forms with synchronous update, labels (W, S, C).
Edge count from `cm_from_rules`. The strict-mediation family comes from `enumerate_family()` (256 forms).
The full space enumerates 16³ two-input truth-table triples. Each probe asserts the instrument control
(canonical triad: triadic, max_phi = 2.0, MIP `2 parts: {W,SC}`) before comparisons. Decision rules are
in `methods.md`.

## Results

### H1 — the edge floor binds all triadic family forms

All 24 triadic strict-mediation forms carry exactly four edges. Zero forms sit above or below the floor.
H1 is confirmed.

### H2 — max Φ at the floor is not AND-specific

Sixteen triadic forms reach Φ = 2.0. Only two — W1_S1_C1 and W2_S1_C2 — use S-index 1 (AND). The
remaining fourteen use monotone commits including OR (index 7), NOR (8), NAND (14), and implication
variants (indices 2, 4, 11, 13). Every max-Φ form is monotone non-parity, matching the #113 split, but
AND is not necessary. H2 is refuted.

### H3 — parity saturates its ceiling at the same floor

All eight XOR/XNOR triadic forms sit at four edges with Φ = 0.5 exactly, matching the parity scaling law
at n = 3. H3 is confirmed.

### H4 — OR can bind in strict mediation

Sixteen strict-mediation forms carry an OR commit. Two are triadic at Φ = 2.0 (W1_S7_C1, W2_S7_C2); the
other fourteen are dyadic. OR is not categorically excluded from irreducible strict mediation. H4 is refuted.

### H5 — the global four-edge maximum is widely shared

In the 4096 wiring space, 312 forms are triadic at exactly four edges. Of those, 192 reach Φ = 2.0. Only
two satisfy strict-mediation with an AND commit; 190 do not. The max-Φ achievers at the global four-edge
floor extend well beyond the canonical conjunctive hub. H5 is refuted.

## Discussion

The edge floor is real and universal within strict mediation (H1). What is not unique is which commit
achieves which ceiling. The floor hosts two saturated classes: monotone commits at Φ = 2.0 and parity
commits at Φ = 0.5 (H3). Within the monotone class, AND is one of several max-Φ commits (H2), and OR binds
in a subset of its labelled forms (H4). The full wiring space multiplies the diversity: back-channels and
alternate read patterns let many non-AND wirings reach Φ = 2.0 at four edges (H5).

Agenda #48 asked whether the conjunctive hub is the unique max-Φ form at the floor. The answer is no at
the commit level and yes at the class level: monotone versus parity partitions the floor's Φ budget, and
the AND hub is the best-known instance of the monotone class, not its sole member.

## Validation gap

These results concern Boolean models of coordination forms at n = 3 with synchronous update. Real
organizations may use richer state, asynchronous schedules, and non-Boolean commits. The edge count is a
connectivity proxy, not a literal count of contractual or informational ties.

## References

See `literature/references.bib`.
