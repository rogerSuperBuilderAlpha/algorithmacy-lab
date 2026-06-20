# The bridge at four parties and larger

Two parties give one lag. Four give several at once, and the new work is reading them together.
[`bridge_four.py`](bridge_four.py) carries the Φ-and-CRQA pairing to the lab's named multiparty forms
and a random four-node ensemble. Φ comes from `classify_rules` and the major complex from
`complex_over_states`, the same instruments the multiparty and hierarchy threads use. CRQA gains two
tools for more than two parties, both in [`crqa.py`](crqa.py): a pairwise lead-lag matrix across every
ordered pair, and a multidimensional whole-system recurrence on the full state vector. Numbers
reproduce at the seeds in the script.

## The bridge scales

Both instruments compute at four and five parties. Φ runs from zero on the dyadic forms to 4.0 on
`multihome_both`, where a worker routes through two platforms that both bind. The major complex
resolves cleanly: `pool_all_required` and `multihome_both` carry all four parties in the core, the
dyadic forms carry a two-node core, and two cases are worth marking. The mediator chain
W-S1-S2-C keeps its irreducible core on the tail pair S2-C, the end of the chain nearest the
counterpart. The five-node `deep_pool_all` keeps a four-node core that excludes the worker. The
whole-system recurrence sits between 0.71 and 0.83 determinism across the forms, a behavioral reading
of the whole that has no two-party analog.

## Reading several lags at once

The lead-lag matrix is the capability four parties demand. On a relay chain W to S1 to S2 to C, the
pairwise profile lag counts the hops:

| pair | lag | hops | prominence |
|---|---|---|---|
| W–S1 | +1 | 1 | 0.15 |
| S1–S2 | +1 | 1 | 0.22 |
| S2–C | +1 | 1 | 0.26 |
| W–S2 | +2 | 2 | 0.14 |
| S1–C | +2 | 2 | 0.19 |
| W–C | +3 | 3 | 0.12 |

Neighbors lead by one step, parties two apart by two, the ends of the chain by three. The matrix
recovers the order of the chain and the distance along it, all from behavior, which is the multiparty
form of the directional read-out. A star recovers differently: the parties each couple to the hub at
a short lag and to each other only through it, so the matrix locates the hub as the node every other
party leads or follows by one step.

## Structure and behavior stay distinct

The random four-node ensemble gives the rates. Whole-system irreducibility is rare, 9% of forms, in
line with the 5% at three nodes. The profile lag recovers 33% of directed read edges with an 11%
false-positive rate, a little below the 40% at three nodes: more parties bring more common-driver
paths, and a common driver couples two parties that share no edge. Coupling centrality, each node's
summed prominent coupling, ranks every major-complex member above every excluded party in 36% of
forms.

The 36% is the point, not a shortfall. The three-node experiments already found that the structural
core pair and the behavioral tight pair differ a third of the time, and that integrated information
and determinism dissociate. The four-node ensemble carries the same finding: behavior recovers the
structural core only partially, because the two instruments measure different things. A node can sit
in the irreducible core without being the most coupled in behavior, and a relay node can be tightly
coupled while belonging to no complex. The dissociation widens slightly with more parties, which is
the honest reading of the named forms too, where coupling centrality cleanly separated the core in
two of seven cases.

## What this establishes

The pairing holds at four and five parties. Φ resolves the major complex, including the cases where
the core is a chain's tail or excludes the worker, and CRQA's lead-lag matrix reads the several lags a
multiparty coordination carries, recovering chain order and hop distance and locating a hub. The two
instruments agree less as parties multiply, which keeps them complementary: the structure says which
parties form the irreducible whole, and the behavior says how the signal moves among them. The next
step on the agenda in [README.md](README.md) takes the behavioral instrument off synthetic
trajectories and onto a real recorded series through the field protocol.
