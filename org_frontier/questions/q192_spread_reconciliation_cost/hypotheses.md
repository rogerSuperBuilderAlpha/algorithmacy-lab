# q192 — hypotheses

Two parties give disagreeing accounts of one coordination. Each account is a rule set over labels
(W, S, C) = (Worker, System, Counterpart), drawn from a fixed catalog of per-node rules. A
single-rule edit replaces one node's rule with another from the catalog. A reconciliation path is
a sequence of single-rule edits that takes account A's verdict-and-core to match account B's. This
study asks whether the length of the shortest such path measures how far the two accounts diverge,
and whether that length tracks the Φ spread the q183 bridge reports. Both hypotheses are fixed
before the computation.

**H1 (edit distance rises with the spread).** The minimum number of single-rule edits to make
account A's signature (its structure and major-complex core) match account B's is monotone
increasing in the noiseless Φ spread of the original pair, where the spread is phi_gap plus core
divergence (1 − core_jaccard). Larger spread costs more edits to reconcile.

- H1-null: edit distance is uncorrelated with the spread magnitude. Reconciliation cost is not a
  function of how far the accounts diverge.

**H2 (reconciliation is a well-defined distance).** Reconciliation is path-order-invariant. Every
minimal edit sequence between two accounts has the same length, regardless of which intermediate
account it passes through, and the distance is symmetric. So edit distance is a well-defined
distance on the account space.

- H2-null: minimal-edit length depends on the path, or the directed distance from A to B differs
  from B to A. Reconciliation cost is not a well-defined distance.
