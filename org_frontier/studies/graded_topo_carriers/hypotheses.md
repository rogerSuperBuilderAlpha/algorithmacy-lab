# graded_topo_carriers — hypotheses (fixed before computing)

**Question (RESEARCH_AGENDA_V3 #11).** On a **ring versus hub versus
necklace** carrier, does graded commit (V2 #2 `SHARP_CLASS_GRADED_PATH`)
keep sharp class labels while Φ grades, or does topology force class
flips the fixed-hub panel never saw?

**Already known (cited, not reopened).**
- V2 #2 `graded_commit_verdict/`: hub triad, faithful
  `S'=min(W,C)`, `W'=S`, `C'=S`, k=3 diagonal `(L,L,L)` →
  NULL → DYADIC → TRIADIC with Φ and membership grading
  (`SHARP_CLASS_GRADED_PATH`).
- V3 #4 `local_triad_necklace/`: binary AND necklace recovers ring
  landmark Φ=4 (or collapses under OR/directed) —
  `COMPOSE_LANDMARK_OR_COLLAPSE`.
- Binary ring: `i'=x_{i-1} ∧ x_{i+1}` (scaling zoo).

**Gap.** The graded path is known only on the fixed hub. #11 asks
whether ring or necklace carriers force a different class sequence
(or smear classes) once the same graded min-commit is ported.

**Instrument.** Exact IIT-4.0 via `third_party/pyphi_iit4_mv`
(`MultivaluedNetwork` / `maximal_complex`). Alphabet k=3. In-silico.
Binary AND triad control at `(1,1,1)`: TRIADIC Φ=2.

**Universe — graded min-commit on three carriers.**

| carrier | n | update |
|---|---:|---|
| hub | 3 | `S'=min(W,C)`, `W'=S`, `C'=S` (V2 #2) |
| ring | 3, 4 | `x_i' = min(x_{i-1}, x_{i+1})` |
| necklace | 6 | local-triad necklace with `min` for AND: `H_i'=min(P_i,P_{i+1})`, `P_i'=min(H_{i-1},H_i)` |

Diagonal state `(L,…,L)` for `L∈{0,1,2}`. Structure class from major
complex size: NULL / MONADIC / DYADIC / TRIADIC (`n_core≥3` → TRIADIC).

**Necklace search note.** Full `maximal_complex` on n=6, k=3 is
prohibitive (size-5/6 SIA). Class verdict for necklace uses exhaustive
SIA over all subsystems of size ≤4 (L=0,1,2), plus size-5 spot checks
at L=1 confirming Φ≪ dyad max. At L=2 a size-3 local triad already
ties the dyad Φ, so the class is TRIADIC under largest-first major
complex even if a larger subsystem matches Φ.

## H1 — classes stay sharp on every carrier

On each carrier diagonal, every L yields a discrete class in
{NULL, MONADIC, DYADIC, TRIADIC}. Null: unclassifiable / fractional.

## H2 — Φ grades with L on every carrier

On each carrier, Φ is monotone non-decreasing in L and not constant
across {0,1,2}. Null: flat or non-monotone Φ path on some carrier.

## H3 — class path matches the hub reference

Every carrier’s class sequence equals the hub reference
NULL → DYADIC → TRIADIC. Null: some carrier shows a different sequence
(a topology-forced flip relative to the fixed-hub panel).

## H4 — panel closed

Binary control passes and H1–H3 resolve to a panel verdict token.

## Reading keys

- **SHARP_HOLDS_ACROSS_TOPO:** H1 ∧ H2 ∧ H3 — sharp labels and Φ
  grades on all carriers; no topology-forced class flip.
- **TOPOLOGY_FORCES_FLIPS:** H1 ∧ H2 ∧ ¬H3 — some carrier’s class
  path leaves the hub sequence.
- **GRADED_BREAKS:** ¬H2 on some carrier (sharp or not).
- **CONTROLS_FAIL:** binary control fails or H1 fails.
