# Findings: a "level of consciousness" radically underdetermines the mind

**Premise.** *Assume IIT is true* — a system's Φ-structure **is** what it is like
to be it. We built a bestiary of ten small systems spanning low→high Φ and
different structural characters, computed each one's exact IIT-4.0 Φ-structure,
and asked how the *level* of consciousness (scalar Φ) relates to its *character*
(the structure). They come apart — completely.

## The bestiary (ordered by Φ)

| creature | Φ | #distinctions | composition (order:count) | #relations |
|----------|--:|--:|--|--:|
| feedforward | 0.000 | 1 | 1:1 | 0 |
| dense_no_subject | 0.000 | 6 | 1:3, 2:3 | 63 |
| dim_busy | 0.305 | 9 | 1:4, 2:3, 3:1, 4:1 | 318 |
| dim_simple | 0.318 | 3 | 1:2, 4:1 | 5 |
| **twin_minimal** | **0.415** | 6 | 1:4, 2:1, 4:1 | **59** |
| **twin_rich** | **0.415** | 11 | 1:4, 2:4, 3:2, 4:1 | **2 044** |
| **twin_baroque** | **0.415** | 15 | 1:4, 2:6, 3:4, 4:1 | **32 764** |
| synergic | 1.500 | 4 | 2:3, 3:1 | 15 |
| canonical | 2.000 | 4 | 1:2, 2:1, 3:1 | 10 |
| grid | 4.000 | 6 | 1:4, 2:2 | 14 |

## 1. Same level, radically different minds (the twins)

Three systems have **identical Φ = 0.415** — by IIT's scalar, the *same level of
consciousness*. Yet their cause-effect structures span **59 to 32 764
relations** — a **555× range** in the very thing that, under IIT, *is* the
experience. Equal Φ, utterly unequal minds.

## 2. "More conscious" ≠ "richer experience"

Across the subjects (Φ > 0), Φ and structural richness are **anti-correlated**
(Pearson r = −0.46 on log-relations). The starkest case:

- `grid` has the **highest Φ (4.0)** — the "most conscious" mind here — yet only
  **14 relations**.
- `twin_baroque` has a **low Φ (0.415)** yet **32 764 relations**.

So the system IIT ranks as *most* conscious has one of the *structurally
sparsest* experiences, while a "dim" mind has a vast one. A one-dimensional
consciousness scale does not even order minds by the richness of their
experience.

## 3. The *kind* of experience differs too (composition)

Beyond level and richness, the **composition** differs qualitatively:

- `synergic` has **no first-order distinctions at all** (2:3, 3:1) — its
  experience is built entirely from higher-order, irreducibly-joint concepts.
- `grid` is **first-order dominated** (1:4, 2:2) — an experience of many simple
  parts.
- `canonical` is a graded mix (1:2, 2:1, 3:1).

Under IIT these are not just different *amounts* of experience but different
*kinds* — and Φ is blind to the distinction.

## 4. Structure without a subject

`dense_no_subject` has **Φ = 0** (IIT says it is *not* a subject) yet a rich
structure — 6 distinctions, 63 relations. `feedforward` is the genuine null: one
distinction, no relations. So "has a cause-effect structure" and "is a conscious
subject" are separate facts.

## Interpretation

Granting IIT's own identity claim, **"level of consciousness" (scalar Φ)
radically underdetermines the conscious mind.** Two systems IIT calls equally
conscious can have experiences differing 500-fold in richness; the "most
conscious" system can have a sparser experience than a "dimmer" one; and systems
of equal Φ can be built from entirely different *kinds* of concept. This is a
constructive, by-example case for the field's own move away from a single Φ
toward the full Φ-structure (cf. Barrett et al.'s multi-dimensional proposal, and
the IIT phenomenology program that reads experience off the structure, not the
scalar). A clinical or AI "consciousness meter" reporting one number is, on IIT's
own terms, discarding almost everything that makes a mind what it is.

## Caveats

- This is an **existence demonstration on a hand-curated bestiary**, not a
  statistical claim — but existence is all the argument needs ("equal Φ *can*
  mean unequal minds").
- The "twins" were found by search at Φ = 0.415 (a value many small systems
  share) and frozen as fixed TPMs (`results/bestiary.pkl`); the analysis is fully
  reproducible.
- Relation counts carry the same congruence caveat as `structure_suite`
  (Φ = 0 / no-system-state cases may inflate counts); distinction-level facts are
  exact, and the twins all have Φ > 0.
- "Experience" talk is *under the IIT-is-true assumption* — the point is internal
  to IIT, not an independent claim about consciousness.

## Reproduce

`python -m consciousness_range.explore` (loads the frozen `results/bestiary.pkl`).
