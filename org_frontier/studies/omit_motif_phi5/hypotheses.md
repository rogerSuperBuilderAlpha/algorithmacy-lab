# omit_motif_phi5 — hypotheses (fixed before computing)

**Question.** What omit motif discriminates non-derangement fixed_k=3 forms
with Φ=5 from those with Φ=6 (and other non-derangement Φ) at n=5?

**Already known.**
- **`fixed_k_atoms_n5`:** NEW_RUNGS — Φ=9 = all 44 derangement omits; Φ=5
  recurs on non-derangement incomplete cores (6/48, always n_core=4).
- **Prior Φ=5 sample:** all had indeg signature (0,1,1,1,2), a single
  **3-cycle** in the omit digraph, recip=0, n_core=4.
- **Prior Φ=6 sample:** mixed; when same indeg, cycle structure differed
  (2-cycles, 4-cycles, double 2-cycles).
- Ternary / residual-cascade noted only.

**Universe.** Binary exact IIT-4.0. Conjunctive AND. n=5 fixed_k=3 ⇔ omit
function f with f(i)≠i. Non-derangements partition into finitely many classes
by (indeg_sig, cycle_lengths, recip). Each class is a single S5-orbit (checked
combinatorially). Evaluate orbit representatives + a uniformity sample of the
candidate Φ=5 motif.

**Motif M (candidate Φ=5 law).**
indeg_sig = (0,1,1,1,2) ∧ cycle_lengths = (3,) ∧ recip = 0
(one never-omitted node, one double-omitted node, omit digraph is a 3-cycle
with trees feeding in; no reciprocal omit pair).

## H1 — motif M yields Φ=5

A designed witness of motif M has core Φ = 5.0 and n_core = 4. A uniformity
sample of N≥8 distinct members of M (beyond the witness) all match Φ=5,
n_core=4. Null: any M member differs.

## H2 — no other non-derangement class yields Φ=5

Every other non-derangement omit class (orbit representative) has core Φ ≠ 5.
Null: some other class representative has Φ = 5.

## H3 — same-indeg siblings without the 3-cycle yield Φ=6

Orbit representatives of classes with indeg_sig=(0,1,1,1,2) but cycle_lengths
≠ (3,) have core Φ = 6.0 (not 5). Null: any such sibling has Φ=5 or Φ∉{5,6}.

## H4 — Φ=5 is exactly motif M among non-derangements

H1 ∧ H2: the structural discriminant for Φ=5 vs other non-derangement Φ is
membership in motif M. Null: H1 or H2 fails.

## H5 — designed witness, not noise

Motif M is nonempty with known size 120 (!); Φ=5 is a **designed** omit law,
not a rare random near-miss of a landmark.
