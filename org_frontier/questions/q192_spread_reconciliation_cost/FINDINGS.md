# q192 — findings

Two accounts of one coordination are reconciled by single-rule edits. The reconcile routine runs
breadth-first edits from account A until it reaches an account that reads the same structure and
core as account B, and returns the edit count. The study asks whether that count measures how far
the accounts diverge and tracks the q183 Φ spread. The results are on synthetic rule sets over a
fixed catalog.

## Instrument and reconcile controls

The faithful triad `[x1, x0&x2, x1]` reads `triadic` with max Φ_MIP = 2.000000. PASS. The identity
pair reconciles at distance 0; a one-rule-apart pair reconciles at distance 1. Both controls pass.
The signature map covers all 216 accounts.

## Panel

Account B = `[x1, x0&x2, x1]` (triadic, core {W, S, C}).

| account A              | vagree | phi_gap | core_J | core_div | spread | edit_dist |
|------------------------|--------|---------|--------|----------|--------|-----------|
| [x0, x1, x2]           | 0      | 2.0000  | 0.3333 | 0.6667   | 2.6667 | 3         |
| [x1, x0, x1]           | 0      | 2.0000  | 0.6667 | 0.3333   | 2.3333 | 1         |
| [x1, x1, x1]           | 0      | 2.0000  | 0.3333 | 0.6667   | 2.6667 | 1         |
| [x1, x0&x2, x1]        | 1      | 0.0000  | 1.0000 | 0.0000   | 0.0000 | 0         |
| [x1, x0\|x2, x1]       | 1      | 0.0000  | 1.0000 | 0.0000   | 0.0000 | 0         |
| [x2, x2, x2]           | 0      | 2.0000  | 0.3333 | 0.6667   | 2.6667 | 2         |
| [x0&x2, x0&x2, x0&x2]  | 0      | 2.0000  | 0.6667 | 0.3333   | 2.3333 | 2         |
| [0, 0, 0]              | 0      | 2.0000  | 0.0000 | 1.0000   | 3.0000 | 3         |

## Verdicts

- **H1 (edit distance rises with the spread): REFUTED.** The Spearman correlation between spread
  magnitude and edit distance is 0.8355, positive and strong, and zero-spread pairs sit at
  distance 0. But the edit distance is not non-decreasing across the spread-sorted panel: at the
  same spread of 2.6667, `[x1, x1, x1]` reconciles in 1 edit while `[x2, x2, x2]` needs 2 and
  `[x0, x1, x2]` needs 3. Edit distance correlates with the spread without being a monotone
  function of it, so the strict H1 fails.
- **H2 (reconciliation is a well-defined distance): NOT SUPPORTED.** Path-order invariance holds:
  every pair has a single shortest-path length equal to its distance. But the directed distance is
  not symmetric. Reconciling `[x0, x1, x2]` to B's signature costs 3 edits, and the reverse costs
  a different count, because reconciliation targets a signature class and those classes differ in
  size and reachability. A well-defined distance requires symmetry, so the combined H2 fails.

## What does hold

The reconcile routine is well-anchored: identity at 0, neighbours at 1, and every shortest path
between fixed endpoints has one length. Edit distance and Φ spread are strongly rank-correlated.
The two refutations are about strictness: distance is not a monotone function of spread, and it is
a directed quasi-distance, not a symmetric metric.

## Scope

The accounts are synthetic rule sets over a coder-chosen catalog. The reconciliation cost depends
on that catalog. The empirical arms are on synthetic data; no real coordination is measured.
