# Q206 — Does a parity ring rewire differently from a conjunctive ring, and where does the verdict inflect? · Stage 1 review

**Question.** Under Watts-Strogatz rewiring of a six-node ring, does a parity (XOR) coupling decline and
factor the same way a conjunctive (AND) coupling does, and where exactly does the verdict turn dyadic?

**Agenda id.** Agenda Q17 (small-world rewiring), extending q146 with its two stated open edges.

## Prior probes that bear on this

| probe | finding | how it relates |
|---|---|---|
| q146 | Rewiring a conjunctive ring (n=6) lowers mean Φ monotonically (4.0→3.0→2.14→0.67→0.47); no small-world peak; verdict flips dyadic by p=0.5 | The baseline this extends; its caveats name both gaps this fills |
| #115 | The parity family scales differently from the conjunctive hub (parity Φ decays as 2^(2−n)) | Motivates testing whether the coupling family changes the rewiring response |
| #132 / q143 | Ring Φ is constant in n where a hub's is linear; ring verdict geometry is a balanced two-arc cut | Establishes the conjunctive ring as the integrated reference topology |

## The gap

q146 swept a conjunctive ring and found a clean monotone Φ decline with the verdict collapsing to dyadic
under rewiring, and it closed with two explicit caveats: the five-point p grid is coarse enough that
"a finer grid or larger n could in principle expose structure between the sampled points," and the
conjunctive coupling "is a fixed design choice — other couplings (parity, threshold) could behave
differently and are not swept." Both are open. The verdict first turns dyadic somewhere in p∈(0.25, 0.5),
but q146's grid cannot say where. And whether the monotone decline is a property of the AND coupling or of
rewiring in general is untested, even though #115 shows the parity family scales by a different law. This
question fills the grid in the unresolved interval to locate the inflection, and runs the same sweep on a
parity ring to test whether the coupling family changes the rewiring response.
