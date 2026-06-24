# q155 — A coupling-centrality threshold recovers major-complex membership only weakly, and fails on reciprocal coupling

Major-complex membership is a structural fact: exact IIT-4.0 Φ names which nodes belong to the
maximal complex and which are excluded as spectators. This study asks whether a behavioral
quantity, coupling_centrality read from a sampled trajectory, recovers that membership as a per-node
binary, and where the recovery breaks.

The corpus is 89 synthetic Boolean coordination forms: 9 named multiparty forms and 80 random forms
of 3 to 5 nodes. Each node gets a structural label from the complex's node_indices and a behavioral
score from its summed prominent coupling. All 361 nodes are pooled and the score threshold is swept
to trace the ROC.

The pooled ROC-AUC is 0.649, against a label-shuffled null of 0.494. Centrality tracks membership
above chance, and the gap from the null is clear. The signal does not clear the pre-registered bar
of 0.65, so the first hypothesis is refuted on its own terms. The recovery is real and modest.

The breakdown by topology locates the strength and the weakness. Star and mediator forms give the
cleanest recovery, with within-class AUC around 0.73: a hub or an articulation node out-couples the
parties it serves, and the structure includes it. Reciprocal forms are the weak class. They are the
bulk of the corpus, their within-class AUC is 0.561, and they supply the most false positives per
node, 0.244. Mutually coupled spectators score high on a symmetric centrality even when the structure
leaves them out, so the threshold admits them.

The second hypothesis predicted the opposite failure. Chain and relay forms were expected to be the
systematic false-positive class, on the reasoning that a tightly-coupled relay node excluded from the
core would look central. That did not happen. Chain forms produce zero false positives per node. A
relay in these forms is excluded from the core and also scores low on coupling centrality, because
its prominent links are few. The relay is correctly called a spectator. The systematic failure is
reciprocal coupling, not chain relays.

The result is a bounded negative. A single behavioral threshold is too blunt to recover structural
membership across topologies. Where the coordination has a clear hub or mediator, centrality and
structure agree; where coupling is symmetric and mutual, a scalar centrality cannot tell a member
from a well-connected spectator. This marks a limit on reading membership from behavior alone and
points to features that separate directed asymmetric coupling from mutual coupling as the next step.

The corpus is synthetic. Every number is an in-silico reading of how a behavioral centrality tracks
exact-Φ membership on Boolean coordination models. No field organization is measured, and the gap
between these forms and any real coordination is open.
