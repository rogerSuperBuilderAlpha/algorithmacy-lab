# q192 — methods

## The account space

An account is a triple of per-node rules over labels `(W, S, C)`, evaluated on the little-endian
current-state tuple `x = (W, S, C)`. Each node's rule is one of a fixed catalog of six building
blocks:

    x0, x1, x2, x0&x2, x0|x2, 0

These span tracking another party, an AND coupling, an OR coupling, and a constant off. The
account space is the product, `6^3 = 216` accounts. A single-rule edit replaces one node's
catalog entry with a different one, so each account has `3 * (6 − 1) = 15` neighbours.

Each account carries a signature: its `(structure, major-complex core)` under the exact IIT-4.0 Φ
classifier. The probe precomputes the signature of all 216 accounts by running each through
`verdict()` and `major_complex()` from `org_frontier.probes.lib`. Φ is not reimplemented.

## The reconcile routine

`reconcile(A, B, sigs)` runs breadth-first single-rule edits from account A over the catalog,
stopping at the first account whose signature equals account B's signature, and returns the edit
count. The target is B's signature class, not B's exact rules: A reconciles to B's verdict and
core, possibly through a different rule set that reads the same. `all_shortest_lengths(A, B, sigs)`
enumerates the BFS layers and returns the set of lengths at which B's signature is first reached,
which is a single value when the distance is well-defined.

## The bridge

The Φ spread of each pair comes from `spread(A, B, labels)` in
`org_frontier.qualitative.disagreement_phi`, built and validated in q183. It returns
verdict_agreement, phi_gap (absolute difference of the two whole-system max Φ_MIP values), and
core_jaccard (Jaccard overlap of the two major-complex cores). The spread magnitude used to order
pairs is `phi_gap + (1 − core_jaccard)`.

## Controls

**Instrument control.** The faithful triad `[x1, x0&x2, x1]` with labels `(W, S, C)` reads
`triadic` with max Φ_MIP = 2.0. The probe aborts on failure.

**Reconcile controls.** The identity pair (an account against itself) must give distance 0. A
one-rule-apart pair (a catalog neighbour with a different signature) must give distance 1. Both
anchor the routine before the panel is scored.

## The panel

A fixed panel of eight account-A indices is paired against account B = the faithful triad
`[x1, x0&x2, x1]` (triadic, core {W, S, C}). The panel is sorted so the run order is fixed. For
each pair the probe records verdict_agreement, phi_gap, core_jaccard, core divergence, spread
magnitude, and edit distance.

## Decision rules

- H1 supported iff the Spearman rank correlation between spread magnitude and edit distance
  exceeds 0.5, the edit distance is non-decreasing across the spread-sorted panel, and every
  zero-spread pair sits at distance 0.
- H2 supported iff every pair at distance ≥ 1 has a single shortest-path length equal to its
  distance, and the directed distance is symmetric (A→B equals B→A) for every pair.

## Determinism

The probe seeds `numpy.random.default_rng(0)`. The signature map, the BFS, and the spread are
exact reads over enumerated reachable states, so the output is byte-identical on re-run. This was
confirmed across three runs.

## Scope

The accounts are synthetic, coder-supplied rule sets, not measured worker states. The construct is
divergence between two stated accounts of one coordination, and the reconciliation cost is defined
over a coder-chosen catalog. The empirical arms are on synthetic data. The catalog-to-observation
gap is not closed here.
