# Thread — the major complex as a coalition structure

The Shapley thread closed on a residual it called structural. Major-complex membership tracks the exact
Shapley value over the game v(S) = φ_s(S) at rank-AUC ≈ 0.87, not 1.0, and the thread attributed the gap
to a mismatch of objects: the major complex is the single argmax coalition, while the Shapley value
averages a party's marginal contribution over every coalition. The closing line named the next question.
Read the exclusion postulate itself as cooperative game theory — a coalition-formation solution concept
that selects the argmax coalition directly — and ask whether it fits where the averaged value left off.

It fits, and the reason rewrites the diagnosis. Reproduce with
`python org_frontier/threads/coalition_structure/coalition_structure.py` (seed 11, 150 three-node forms).

## Setup

A coalition structure is a partition of a form's parties; each block's worth is the integrated
information φ_s of that block. Two readings of the exclusion postulate fall straight out of IIT-4.0:

- **The major complex selects the maximally integrated coalition.** Among all subsets, exclusion keeps
  the one with the largest φ_s. That is argmax_S φ_s(S) — a winner-take-all coalition-formation rule.
- **Condensation generates a coalition structure.** Peel off the maximal complex, remove it, recurse on
  the rest. The output is a partition of the whole. Greedy, one block at a time.

The optimal coalition structure is the partition maximizing total worth across its blocks. The questions:
is the major complex the argmax coalition; is condensation the optimal structure; and where does the
Shapley thread's 0.87 actually come from.

## The arc

**The major complex is the argmax coalition — exactly.** At the state where the maximal complex attains
its largest φ, the complex is among the φ_s-argmax subsets in 149 of 149 usable forms, 100%. As a unique
winner it matches in 71%; the rest is ties, where several subsets reach the same φ_s at that state and the
argmax is a set of tied subsets. The exclusion postulate, restated in coalition language, says the maximally
integrated coalition wins. The value function v(S) = φ_s(S) reproduces it with nothing left over.

**The 0.87 ceiling was state aggregation, not irreducibility.** The Shapley thread scored every coalition
by its φ_s maximized across all reachable states, then asked a node-level marginal to recover membership,
and got AUC 0.87. The major complex lives at one state. Score the same node-level marginal — best
coalition containing the party minus best coalition without it — at that one state, and it predicts
membership at AUC 0.982. The residual the Shapley thread called structural was mostly the cost of mixing
states. A coalition that is worthless in the complex's state can be valuable in another, and maximizing
across states credits a party for worth that has nothing to do with the coalition that actually forms.

**The marginal at the right state is close to the membership question.** AUC 0.982 carries a caveat worth
stating. At the maximizing state, the best coalition containing a party is the global maximum exactly when
that party sits in an argmax coalition, so the marginal is nearly asking whether the party belongs to a
maximally integrated coalition — close to membership by construction. The empirical content sits in the
two facts that are not near-definitional: the Shapley thread's 0.87 across states, and the partition
result below.

**Condensation lands on the optimal structure most of the time.** Greedy peeling of the maximal complex matches the optimal
coalition structure in 131 of 149 forms, 88%. Exclusion's recursive condensation behaves like a greedy
coalition-structure generator that is right most of the time and myopic in about one form in eight, where
committing to the single best block first forecloses a better partition of the remainder.

## What the thread establishes

The exclusion postulate translates cleanly into cooperative game theory. The major complex is the
argmax of the coalition game v(S) = φ_s(S), the maximally integrated coalition, matched 100% up to ties.
Condensation is a greedy coalition-structure generator that lands on the optimal partition 88% of the
time. And the Shapley thread's AUC-0.87 ceiling is diagnosed: it is mostly state aggregation, since the
same node-level marginal recovers membership at AUC 0.98 once scored at the state where the complex forms.

## Limits, honestly

The argmax result is a translation, close to IIT's own definition of the major complex, so 100% is a
consistency check that v(S) = φ_s(S) faithfully encodes exclusion, not a discovery about organizations.
The AUC-0.98 marginal is near-definitional at the maximizing state and should not be read as a strong
predictive claim. The load-bearing empirical facts are the 88% greedy-versus-optimal gap and the
state-aggregation diagnosis. Everything is in-silico on three-node Boolean forms over a sampled
population, and the worth maximized across reachable states is one choice among several. This corrects
the Shapley thread's own account of its ceiling and should fold back into it as a footnote: the gap was
the price of mixing states, and the major complex is the coalition the postulate was always selecting.
