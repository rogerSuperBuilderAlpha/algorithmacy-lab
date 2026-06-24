# q154 — Behavioral centrality misses the structural articulation point

A bottleneck form has one node that holds the others together. Exact IIT-4.0 Φ names that node. Freeze
each node to a constant in turn and recompute the maximal complex; the freezing that drops major-complex
Φ the most marks the articulation point, the node whose removal collapses the integration the rest
sustain. The question this study asks is whether a behavioral reading of a sampled trajectory finds the
same node. Two pickers are on offer: CRQA coupling centrality, the node with the most prominent
lead-lag coupling to the others, and transfer-entropy throughput, the node with the most directed
information flowing through it.

Three named bottleneck forms carry the test, with the articulation node placed at a different index in
each so a recovery is not a positional accident. The strict ATS mediator `[x1, x0 & x2, x1]` is the
canonical case. A joint bottleneck puts a hub between one party and a redundant pair, so the pair's
internal redundancy keeps the form integrated when a pair member is frozen but not when the hub is. A
degree bottleneck puts a high-degree connector between two parties with a back-up read. For each form, 30
seeded trajectories of 400 steps give 30 behavioral picks per picker, and a pick counts as a recovery
when it lands in the structural argmax-drop set.

Coupling centrality does not recover the articulation point. On the two forms with a single articulation
node it lands on the right node 28.3% of the time, a hair above the 25% chance rate and far below the 70%
the hypothesis fixed. Transfer-entropy throughput reaches 66.7% on the same forms. The cheaper directed
measure beats the centrality measure the recurrence program leans on.

The two forms split for a reason worth stating. On the degree bottleneck the load-bearing node is also
the one the trajectory couples to most, so coupling centrality half-recovers it, 17 of 30. On the joint
bottleneck the load-bearing hub is quiet: its behavioral coupling is weak next to the redundant cluster
it gates, and coupling centrality never finds it, 0 of 30, while throughput finds it 24 of 30. Structural
load and behavioral prominence come apart when the node that holds the form together is not the node that
talks the most.

The control rules out the cheap explanation. A degree-matched XOR-ring spreads equal Φ load over every
node, so it has no articulation point. The behavioral picks spread across all four nodes, with no node
taking more than 37% against a 25% chance floor. The pickers do not manufacture a bottleneck where the
structure has none; they fail to find one where the structure has one.

The reading for the recurrence program is narrow and negative. Coupling centrality tracks whole-complex
membership in earlier studies, but membership and articulation are different questions, and a behavioral
centrality that ranks who is in the complex does not thereby rank who holds it together. A node can be
central to the talk and not be the structural pivot. Exact Φ separates the two; the sampled-trajectory
centrality used here does not.

The ats_strict_bottleneck form contributes no recovery test. Its AND mediator dies whenever any input is
frozen, so all three nodes tie for the largest drop and each is an articulation point. The tied set makes
recovery automatic and uninformative, and the verdict rests on the two single-articulation forms.

## Scope

Exact IIT-4.0 Φ on small Boolean coordination forms. The bottleneck, the freezing ablation, and the
centrality and throughput readings are graph-and-Φ quantities, not measured organizations. The CRQA and
transfer-entropy arms run on synthetic trajectories, so every recovery rate is a baseline on synthetic
data. The Φ-to-organization bridge is open. The result bounds a claim about a behavioral instrument; it
does not reach a real coordination.
