# ring_of_hubs — hypotheses (fixed before computing)

**Question (RESEARCH_AGENDA_V3 #5).** Does a **ring-of-hubs** (hubs coupled as
a ring, each hub serving a private leaf set) **combine** the ring’s
size-independent Φ=4 cap with hub growth (Φ=n−1), where V2 #17 `PICK_ONE`
morphs failed — or does it also pick a landmark / collapse?

**Already known (cited, not reopened).**
- **V2 #17 / `small_world_vs_hierarchy`:** `PICK_ONE` — interiors collapse;
  only pure ring / pure hub recover family laws.
- **V2 #18 / #19:** discrete landmarks; no log/√n intermediate law.
- **V3 #4 / `local_triad_necklace`:** `COMPOSE_LANDMARK_OR_COLLAPSE` —
  composed local triads on a cycle recover ring Φ=4 or collapse.
- **#132 ring:** Φ=4 for n≥4. **single_hub:** Φ=n−1.
- Probe 103 two-hub: distributed mediation at scale (cited only).
- Ternary / residual-cascade / M3 noted only.

**Gap.** #17 morphs a *single* ring toward a *single* hub. #4 composes
*shared-party* local triads. Neither tests hubs arranged in a **ring**, each
with **private** leaves — the natural candidate for “combine ring geometry
with hub growth.”

**Universe.** Binary exact IIT-4.0. Primary n=6 (where hub Φ=5 > ring Φ=4).

## Architectures

| cell | construction |
|---|---|
| triad | faithful W–S–C AND control |
| ring6 | conjunctive ring (landmark Φ=4) |
| hub6 | single hub (landmark Φ=5) |
| roh_leaf_ring | 3 hubs + 3 private leaves: H_i′=P_i∧H_{i−1}∧H_{i+1}; P_i′=H_i |
| roh_hubs_ring | 3 hubs + 3 leaves: H_i′=H_{i−1}∧H_{i+1}; P_i′=H_i (leaves hang off) |
| roh_2h2p | 2 hubs × 2 private leaves each: H_a′=H_b∧L_a0∧L_a1 (and sym); leaves copy hub |
| roh_OR_leaf | like roh_leaf_ring but hubs OR neighbors/leaf |
| roh_directed | H_i′=P_i∧H_{i−1} only (broken ring symmetry) |

**Combine** = full-core triadic with core Φ strictly between ring6 (4) and
hub6 (5), *or* full-core Φ > hub6 while remaining a ring-of-hubs (not pool).
**Landmark** = full-core Φ ∈ {4, 5} (or other #18 atom) matching a named
control. **Collapse** = dyadic whole or incomplete core with Φ ≤ 2.

## H1 — instrument + landmarks

Faithful triad triadic Φ=2.0. ring6 full-core Φ=4.0. hub6 full-core Φ=5.0.

## H2 — no combine on the ring-of-hubs panel

No roh_* cell is full-core triadic with core Φ ∈ (4, 5), and none exceeds
hub6 Φ=5 with a full core under a ring-of-hubs wiring (pool excluded by
construction). Null: some roh cell combines.

## H3 — each roh cell is landmark, collapse, or factor

Every roh_* cell is a landmark, a collapse, **or a factor** (incomplete
core with Φ>2 — hub subsystem integrates, private leaves drop out).
Pre-registered exclusive landmark|collapse was the tight claim; factoring
is the residual non-combine mode allowed under H2.

## H4 — panel verdict

H2 holds and every roh cell is landmark | collapse | factor.
If any cell factors → **FACTORS_NO_COMBINE**. If none factor and H3’s
landmark|collapse holds → **NO_COMBINE**. Combine anywhere →
**COMBINE_RING_HUB**.
