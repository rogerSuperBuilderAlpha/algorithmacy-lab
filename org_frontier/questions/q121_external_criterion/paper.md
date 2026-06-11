# Q121 — The verdict is interventional: an external criterion where observation fails

## Question

The critical review's first defense question (T1) asks for a non-circular criterion on which triadic forms are
distinct, after the program's behavioral-difficulty checks failed (Probes 98, 107, 108). This tests the weak
form of the question, consilience with a formalism independent of IIT, and asks which kind of criterion
recovers the verdict where topology and observation both fail.

## Method

Two non-Φ criteria against the exact verdict, over the 256-form strict-mediation family and its 40 full-cycle
forms (the hard subset Q117 isolated, where the wiring is identical and the verdict splits 24/16). The
observational criterion is the total correlation of the next-state joint under a uniform current state. The
interventional criterion is Boolean-network damage spreading: flip one party, run the dynamics, and average the
Hamming divergence from the unperturbed trajectory. Neither calls Φ. Performance is rank-AUC against the
verdict.

## Results

On the hard subset, observation is at chance and intervention is perfect.

| scope | criterion | rank-AUC |
|---|---|---|
| full family | cycle indicator (topology) | 0.966 |
| full family | observational (total correlation) | 0.914 |
| full family | interventional (damage spreading) | 0.851 |
| hard subset (40 full-cycle forms) | observational | 0.500 |
| hard subset | interventional | 1.000 |

| | result |
|---|---|
| H1 the full-family AUC bar is trivial (cycle clears 0.9) | confirmed |
| H2 observation fails on the hard cases | confirmed |
| H3 intervention separates the hard cases | confirmed |
| H4 intervention alone underdetermines the verdict | confirmed |

## Interpretation

The full-family rank-AUC is a trap, and naming it is the first result. The classes are lopsided, 24 triadic
among 256, so a criterion that only detects the feedback cycle scores 0.966 on the full family. Both non-Φ
criteria clear 0.85 there, but on the easy 216 acyclic forms, which any connectivity-aware measure separates.
The defense agenda's literal ask, a non-Φ criterion above 0.5 on the family, is met without effort and shows
little. The test that matters is the 40 full-cycle forms, where Q117 proved the wiring cannot decide.

On those, observation reads nothing. The total correlation of the next-state distribution separates the
triadic from the dyadic full-cycle forms at rank-AUC 0.500, pure chance. A verdict that Q117 located in the
determination's logic rather than its output statistics is invisible to a measure of the output statistics,
and the program's earlier nulls for mutual information, transfer entropy, and O-information (Probes 45-47) were
the same fact seen from other angles. Watching the dynamics cannot separate the classes.

Intervention separates them perfectly. Damage spreading, a do-intervention probe from dynamical-systems theory
that flips a party and follows the perturbation, scores rank-AUC 1.000 on the same 40 forms, with disjoint
score ranges and a separation stable for any horizon of two or more steps. The dyadic forms absorb a
perturbation; the triadic ones carry it. The verdict turns out to be a fact about behavior under perturbation,
not about resting output, which is what IIT's interventional construction and Q117's logic-not-wiring result
together predict. The agreement is consilience: damage spreading is defined entirely within Boolean-network
theory (Kauffman; Derrida and Pomeau), with no reference to IIT, so its perfect match with the verdict is two
independent formalisms meeting, with neither restating the other.

The criterion is the sufficient half of a two-part test, short of a replacement for the verdict. Damage spreading
alone fails to classify the full family (0.851): some acyclic dyadic forms spread a perturbation without being
irreducible. Screened first by the cycle, which Q117 showed is necessary and admits no false negatives, and
then decided by damage spreading, the verdict has a non-Φ characterization in two parts, a topological screen
and an interventional test, the same shape as Q117's necessary cycle plus sufficient logical condition, now
read dynamically.

This answers T1 in its weak form and aims its strong form. A non-circular criterion on which triadic forms are
distinct exists, sharply: damage spreading, perfect on the hard cases. The result also explains why the
program's behavioral checks failed, since those measured coordination difficulty, which Probe 48 found
orthogonal to Φ, while the verdict is interventional. The strong form of T1, a criterion on real coordination
data, now has a concrete target: perturb a real coordination and measure how far the shock travels. The verdict
predicts that triadic coordinations propagate it and dyadic ones absorb it.

## Limitations

In-silico; the exact IIT-4.0 verdict is the ground truth. "Non-circular" means an independent formalism, not
behavioral or empirical-external data, so this is consilience, not the behavioral validation T1 ultimately
calls for. The criteria were prototyped and evaluated on one family (the 256 strict-mediation forms), with the
horizon fixed after a stability check; generalization to other topologies and to stochastic or larger systems
is untested. Damage spreading is an extrinsic dynamical measure, and its agreement with the intrinsic Φ is
consilience rather than derivation; the two could diverge on other families.
