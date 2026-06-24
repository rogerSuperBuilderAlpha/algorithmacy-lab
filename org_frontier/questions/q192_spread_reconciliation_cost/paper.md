# q192 — Reconciliation cost: edit distance between two accounts and the Φ spread

Two parties give different accounts of one coordination. A way to measure how far apart they sit is
to count the edits needed to bring one account into line with the other. This study defines an
account as a triple of per-node rules over labels `(W, S, C)` = (Worker, System, Counterpart),
drawn from a fixed catalog. A single-rule edit replaces one node's rule. The reconcile routine runs
breadth-first edits from account A until it reaches an account that reads the same structure and
core as account B, and returns the edit count. The question is whether that count tracks the q183 Φ
spread between the original pair. The work is on synthetic rule sets.

The routine anchors cleanly. An account reconciled with itself costs zero edits. A catalog
neighbour with a different signature costs one. The signature map covers all 216 accounts in the
`6^3` catalog space, each scored once by the exact-Φ classifier.

A panel of eight account-A indices is paired against account B = the faithful triad `[x1, x0&x2,
x1]` (triadic, core {W, S, C}). The spread magnitude of each pair is phi_gap plus core divergence.
Edit distance and spread are strongly rank-correlated: the Spearman coefficient is 0.84, and every
zero-spread pair sits at distance 0. The reconciliation cost rises, on the whole, with the Φ
spread.

H1 asked for more than correlation. It fixed, before the computation, that edit distance is a
monotone increasing function of the spread. The panel breaks that. Three accounts share a spread of
2.6667 against B, and they reconcile at distances 1, 2, and 3. `[x1, x1, x1]` reaches B's signature
in one edit; `[x0, x1, x2]` needs three. Equal spread, unequal cost. The Φ spread fixes the
verdict-and-core gap between two accounts, but it does not fix how many rule changes bridge that
gap, because the catalog geometry between two signatures varies. H1 is refuted: edit distance
correlates with the spread without being a function of it.

H2 asked whether reconciliation is a well-defined distance. Two properties were tested. Path-order
invariance holds: for every pair, all shortest edit paths between the fixed endpoints have one
length, so the BFS distance is unambiguous along any route. Symmetry fails. The directed distance
from `[x0, x1, x2]` to B's signature is not the distance back. Reconciliation targets a signature
class, and signature classes differ in how many accounts they contain and how the catalog reaches
them, so the nearest member of B's class from A need not match the nearest member of A's class from
B. A distance must be symmetric, so the combined H2 is not supported.

The two refutations sharpen the construct rather than sink it. Reconciliation cost is a directed
quasi-distance with unique shortest-path lengths, strongly rank-correlated with the Φ spread, and
anchored at zero for agreeing accounts. It falls short of a symmetric metric, and it tracks the
spread without reading it off monotonically. Reporting both negatives keeps the construct honest: the count
measures reconciliation effort in a chosen edit space, and that effort is related to the spread but
is a separate quantity.

The accounts are synthetic rule sets over a coder-chosen catalog, not measured worker states. The
reconciliation cost depends on the catalog: a different set of building blocks would change the
neighbour structure and the distances. The empirical arms are on synthetic data; no real
coordination is measured. Later studies in this line vary the catalog and the endpoints to test how
stable the rank correlation and the asymmetry are.
