# Paper 3 — computed results: the Φ landscape of the W–S–C model family and the typology on it

Exact IIT-4.0 system Φ via `proxy_audit.exact_phi` (PyPhi `new_big_phi.sia`), over application-layer
systems built under Paper 2's pre-registered state-individuation rule. Everything here is **model-internal**:
it characterizes what the formal model of Paper 2 yields across its whole domain and where hand-modeled
organizations fall within it. The dissertation makes **no claim that these scores are validated against any
observed coordination outcome** — that is future work (see `exploratory/` for why the earlier rideshare
"anchor" was cut). Reproduce:
`~/iit-playground/venv-4.0/bin/python dissertation/paper3_baseline/catalog.py` then
`… analyze_catalog.py` (writes `results/catalog.csv`, `catalog_analysis.txt`, `catalog_landscape.png`).

## Stage 1: the model family — the complete space of W–S–C wirings

A three-node system in our modeling vocabulary is *any* way each node's next value can depend on the other
two: `W' = f_W(S,C)`, `S' = f_S(W,C)`, `C' = f_C(W,S)`. There are exactly 16 Boolean functions of two
inputs, so the complete family is **16³ = 4096 wirings** — we enumerate all of them (plus 48 higher-order
four-node wirings), with no curation, and compute exact Φ for each. **4,144 distinct wirings** result
(after deduplicating identical transition matrices).

**Read this correctly.** Most of these 4,096 wirings are *not* recognizable coordination forms; they are
simply every Boolean way three nodes can be coupled. The enumeration is a **coverage / null check**, not a
census of real coordination. Its value is twofold: it characterizes what the model does across its whole
domain, and it shows that the hand-modeled organizations of Stage 2 are not cherry-picked but fall on
populated, structurally meaningful bands of the family.

**The bands are a property of the family, not assigned.** Across all 4,096 three-node wirings, Φ takes only
a handful of values:

| Φ band | # wirings | reading |
|---|---|---|
| 0.00 | 1,808 (44.1%) | reducible — the wiring factors along the party lines |
| 0.42 | 856 | the most common nonzero level in the family |
| 0.50 | 24 | parity-coupled determination |
| 0.84 | 824 | partial-mediation band |
| 1.00 | 72 | |
| 1.50 | 8 | |
| 2.00 | 496 | strict-mediation band |
| 6.00 | 8 | a small tail of exotic high-Φ wirings |

Nearly half of all wirings are reducible (Φ = 0): most ways of coupling three nodes do *not* produce an
irreducible structure. The non-zero wirings collapse onto **seven discrete bands**, and the levels the
organization typology occupies below (0, 0.5, 0.84, 2.0) are *populated bands of this family* — they fall
out of the enumeration, they are not set by hand. (`catalog_landscape.png`.)

### What drives Φ within the family

Group means and an OLS of max Φ on structural features (all 4,096 triads):

| feature | effect | reading |
|---|---|---|
| **strict mediation** (parties read only a mediator that reads both) | meanΦ 0.90 vs 0.53; **partial coef +0.54** | the strongest single driver of the score |
| **parity** (an XOR/XNOR coupling present) | meanΦ 0.79 vs 0.40; coef +0.27 | parity couplings score higher than monotone ones |
| **edge density** | coef +0.24 per edge | more coupling, higher score |
| mediator reads both parties | meanΦ 0.60 vs 0.42 (confounded with edges) | necessary but not sufficient |
| back-channel present | negligible once controlled (coef −0.06) | a direct channel does not by itself lower the score |
| **model R²** | **0.196** | **Φ is not reducible to a feature checklist** |

The headline is that last line: simple structural flags explain only ~20% of the variance in Φ. Strict
mediation and parity raise the score, but Φ registers an irreducibility that a count of parties or edges
does not reproduce — which is exactly why the construct uses Φ and not a checklist.

**A caution we carry openly (Cerullo, 2015).** Among genuine two-party mediators, **XOR/XNOR (parity)
mediators score the highest Φ** (meanΦ 0.85) while the monotone ones (AND/OR/NAND/NOR/inhibition) sit at
0.535. This is the model-internal echo of a known critique: Cerullo showed that trivially regular XOR
structures can carry very high Φ, so **a high Φ does not certify sophisticated coordination.** We therefore
read positive Φ only *ordinally and within the model*, lean on the binary Φ = 0 / Φ > 0 distinction for the
dyad/triad question, and do not treat magnitude as a measure of how sophisticated a coordination is.

## Stage 2: hand-modeled organizations placed in the family

Each of 13 organizations is modeled as a W–S–C system (a fourth node for higher-order forms), its
determination structure fixed *before* computing in `typology_phi.py`, derived from how it actually
coordinates its parties — not chosen for a target Φ. Each lands on a populated band of the family:

| Φ (max) | Organization | Class | Modeled structure |
|---|---|---|---|
| **0.00** | Direct exchange (no mediator) | dyadic baseline | parties deal directly; mediator inert |
| **0.00** | Chat with a language model | dyadic baseline | two-party loop; nothing couples a third |
| **0.50** | Complementary skill matching | algorithmic platform | parity determination (S′ = W ⊕ C) |
| **0.83** | Freelance marketplace (Upwork) | algorithmic platform | partial mediation (parties also coordinate directly) |
| **0.83** | Healthcare staffing agency | **human-mediated** | partial mediation |
| **0.83** | Real-estate broker | **human-mediated** | partial mediation |
| **2.00** | Rideshare, solo (Uber/Lyft) | algorithmic platform | strict mediation (S′ = W ∧ C) |
| **2.00** | Food delivery | algorithmic platform | strict mediation |
| **2.00** | Hiring / applicant-tracking system | algorithmic-institutional | strict mediation |
| **2.00** | Content moderation | algorithmic-institutional | strict mediation |
| **2.00** | Court (judge between parties) | **human-mediated** | strict mediation |
| **3.00** | Rideshare, POOLED (driver + 2 riders) | higher-order (n=4) | S′ = W ∧ C ∧ D |
| **3.00** | Crowdwork (requester + 2 workers) | higher-order (n=4) | S′ = W ∧ C ∧ D |

### The headline: structure sets the score, not the seat of the mediator

The human-mediated contrast class illustrates that the model responds to *triadic structure* and not to
*algorithms* — but read this as a modeling property, not an empirical discovery. The court and the platform
get the same Φ **because they are coded with the same strict-mediation structure**; the equality is true by
construction. It shows the model is indifferent to the mediator's seat once the structure is fixed (the
property we want), not that a court and a platform are observed to be structurally identical — that would
need independent inter-rater coding (see `typology_sensitivity.py` for how placements move under alternative
codings). With that reading:

- **A court is modeled at Φ = 2.00 — the same as Uber, the ATS, and content moderation.** A judge between two
  parties who reach each other only through rulings is, in the model, the same strict mediator as the
  dispatch algorithm. The human in the seat does not change the modeled score.
- **A staffing agency and a real-estate broker are modeled at Φ = 0.83 — the same as Upwork.** All three
  match the parties but leave them a direct channel; partial mediation lands at the same level whether the
  matcher is an algorithm or a person.

The human-mediated forms interleave with the algorithmic ones at every level, sorted by structure — and the
Stage-1 family shows these are not 13 special cases but populated bands of the whole model family.

## Notes and honest bounds

- **Everything here is model-internal.** The catalog and the typology characterize the model; neither shows
  that Φ tracks an observed coordination outcome. The dissertation makes no validation claim. The earlier
  rideshare "anchor" was cut because, in the pooling model, Φ = k + 1, so it validated only the party-count
  axis — the one axis Φ is not needed for (see `exploratory/README.md`). Outcome-validation, with a dataset
  that varies determination structure at a *fixed* party count, is named as future work.
- **The 3-node scale (0 → 2.0) is comparable; cross-node is not.** The higher-order cases are 4-node
  systems, so their Φ (3.0 in the typology; up to 12.0 in the family's HO wirings) is partly a function of
  system size. They show the score extends upward when a determination binds more parties, but cross-node
  magnitudes are not strictly comparable and we say so. A size-normalized companion is a candidate.
- **Many wirings share a score** (496 distinct triads at Φ = 2.0). This is a finding, not a defect: forms
  the model couples the same way receive the same score, regardless of industry vocabulary.
- **Φ is not a feature count.** The R² = 0.20 of the structural model is the evidence; and Cerullo's
  XOR-grid result is the reason we never read magnitude as sophistication.
