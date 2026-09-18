# Mixed-radix mediator — hypotheses (fixed before computing)

**Question (RESEARCH_AGENDA_50_V2 #3).** In a mixed-radix system
(binary parties, ternary mediator), where does the extra mediator
resolution go — into Φ magnitude or into core membership?

**Instrument.** Exact IIT-4.0 Φ via `third_party/pyphi_iit4_mv`.
N=3; alphabets `(W,S,C)=(2,3,2)`; CM bidirectional triad. In-silico.

**Universe.** Faithful mixed-radix commit `S'=W+C` (range {0,1,2}).
Two party-read variants:
- **full:** `W'=C'=[S==2]` (only max commit engages parties)
- **thresh:** `W'=C'=[S>=1]` (mid or max engages)

**Focal sweep.** Parties ON, mediator level varies: states `(1,S,1)` for
`S∈{0,1,2}`. The mid value `S=1` is the extra resolution binary AND
cannot express.

**Binary control.** All-binary AND triad `@ (1,1,1)`: TRIADIC Φ=2.

**Pointers.** #1 TWO_CONDITION_STATE_DEPENDENT; #2 SHARP_CLASS_GRADED_PATH
(all-ternary membership *does* grade with L — contrast case).

## H1 — extra resolution → Φ only

On at least one faithful mixed form, the `(1,S,1)` sweep keeps a
**fixed** core label-set for all S with a defined complex, while Φ is
**not** constant across those S. Null: Φ flat whenever core is fixed.

## H2 — extra resolution → core membership

On the same `(1,S,1)` sweep, core label-set or `n_core` **changes**
with S. Null: core fixed for all S in the sweep.

## H3 — both / neither / form-dependent

Across the two party-read forms (full, thresh), the H1/H2 pattern
differs (one form Φ-only, the other membership), or neither H1 nor H2
holds cleanly. Null: both forms agree on a single pattern.

## Reading keys

- **EXTRA_RESOLUTION_TO_PHI:** H1 ∧ ¬H2 (both forms agree Φ-only).
- **EXTRA_RESOLUTION_TO_CORE:** ¬H1 ∧ H2.
- **FORM_DEPENDENT:** H3 (forms disagree).
- **MIXED:** otherwise.
