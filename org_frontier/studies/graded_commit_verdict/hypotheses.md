# Graded commit verdict — hypotheses (fixed before computing)

**Question (RESEARCH_AGENDA_50_V2 #2).** Does a graded commit — the
mediator outputs a level, not a bit — keep a sharp dyadic/triadic
verdict, or does the verdict itself become graded?

**Instrument.** Exact IIT-4.0 Φ via `third_party/pyphi_iit4_mv`
(MultivaluedSubsystem / maximal_complex). Stock pin unused for ternary.
N=3; alphabet k=3 on (W,S,C); CM bidirectional triad. In-silico.

**Universe.** Faithful graded commit: `S'=min(W,C)`, `W'=S`, `C'=S`.
Commit level on the diagonal is `L` in state `(L,L,L)` for `L∈{0,1,2}`.
Structure class from major-complex size: NULL (no irreducible complex),
DYADIC (n_core=2), TRIADIC (n_core=3).

**Binary control.** All-binary AND triad at `(1,1,1)`: structure TRIADIC,
Φ=2 (stock / overlay regression).

**Cited.** Agenda #1 `ternary_pivotality/` (TWO_CONDITION_STATE_DEPENDENT);
probes #11–#12; M2 overlay notes.

## H1 — structure class stays sharp

At each designed state, the major-complex structure is one of
{NULL, DYADIC, TRIADIC} — a discrete class, not a fractional verdict.
Null: instrument yields ambiguous / non-classifiable cores.

## H2 — Φ grades with commit level

On the faithful diagonal `(L,L,L)`, Φ is monotone non-decreasing in L
and not constant across {0,1,2}. Null: Φ flat in L.

## H3 — core membership grades with commit level

On the faithful diagonal, either `n_core` or the core label-set changes
with L (membership is not fixed for all L). Null: same core at every L
with Φ>0.

## Reading keys

- **SHARP_CLASS_GRADED_PATH:** H1∧H2∧H3 — discrete structure labels;
  Φ and membership track L.
- **SHARP_THRESHOLD:** H1; H2/H3 fail — single jump, flat otherwise.
- **GRADED_PHI_ONLY:** H1∧H2; H3 fails — Φ moves, core fixed.
