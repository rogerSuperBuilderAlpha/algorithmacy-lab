# encoding_ladder_gates — hypotheses (fixed before computing)

**Question.** Do the literacy→algorithmacy boundary and the Φ=n−1 flip
depend on the determination gate family, or are they gate-robust?

**Already known.**
- `encoding_ladder_n5` FULL_JOINT_FLIP / `encoding_ladder_n6` PHI_TRACKS_NM1
  under **AND** (OR checked only at the full-bind rung): boundary =
  `workers_*_Cidle → algo_full_*`; flip → whole triadic, Φ = n−1.
- `hmc_algo_boundary` COMMIT_READ_BOUNDARY: party ∈ core iff in S’s
  determination ∧ reads S.

**Universe.** Binary exact IIT-4.0. Labels `("W1","S","W2","W3","C")`
(n=5; candid — n=6 skipped as costly). Designed per-gate ladders:
reuse assist / workers_Cidle / full / drop / C_reads rungs; **swap only
S’s determination gate**. Families: AND (control), OR, NAND, XOR, XNOR,
MAJ (≥3 of 4), MIXED `(W1∧W2)∨(W3∧C)`.

## Competing claims

### H1 — flip + Φ = n−1 is gate-robust

For every tested gate, full joint bind (all outer parties in S’s rule,
all read S) yields whole **triadic**, n_core=5, core Φ = 4 (= n−1).
Null: at least one gate fails the flip or has Φ ≠ 4.

### H2 — some gates stay dyadic at full bind

At least one non-AND gate keeps the whole **dyadic** (or yields no
multi-party major complex) under full joint bind with all reading S.
Null: every tested gate flips to whole triadic.

### H3 — assist path changes with gate

Under AND/OR, progressive assist grows a multi-party core (n_core≥3)
while wholes stay dyadic. For at least one non-AND gate, the assist /
workers_Cidle rungs **do not** grow that multi-party core (e.g. major
complex collapses to an idle singleton). Null: every gate’s assist path
matches AND’s n_core sequence.
