# Q121 findings — the verdict has an interventional correlate where observation fails

All four hypotheses confirmed. On the hard cases that the verdict's own definition makes hard, the 40
full-cycle forms where topology splits 24 triadic from 16 dyadic, an observational non-Φ criterion is at
chance (rank-AUC 0.500) while an interventional one separates the verdict perfectly (rank-AUC 1.000). The
construct that resisted observational and behavioral-difficulty validation has a clean interventional
correlate: damage spreading, a do-intervention probe from Boolean-network theory that calls no Φ.

| scope | criterion | rank-AUC |
|---|---|---|
| full family (24/256 triadic) | cycle indicator (topology, Q117) | 0.966 |
| full family | observational (total correlation) | 0.914 |
| full family | interventional (damage spreading) | 0.851 |
| hard subset (40 full-cycle forms) | observational (total correlation) | **0.500** |
| hard subset | interventional (damage spreading) | **1.000** |

| H | Result | Verdict |
|---|--------|---------|
| H1 | the full-family AUC bar is trivial (cycle alone clears 0.9) | confirmed (0.966) |
| H2 | an observational criterion fails on the hard cases | confirmed (0.500) |
| H3 | an interventional criterion separates the hard cases | confirmed (1.000) |
| H4 | the interventional criterion alone underdetermines the verdict | confirmed (full 0.851) |

From `probe_external_criterion.py`.

## What it says

The headline rank-AUC on the family is a trap, and naming it is the first result. With 24 triadic forms among
256, the classes are lopsided, and a criterion that merely detects the feedback cycle scores 0.966 on the full
family (H1). The observational criterion's 0.914 and the interventional criterion's 0.851 on the full family
are likewise mostly the easy 216 acyclic forms, which any connectivity-aware measure separates. So "a non-Φ
criterion clears AUC well above 0.5 on the family", the literal ask of the defense agenda, is met trivially
and means little. The severe test is the 40 full-cycle forms, where Q117 showed the wiring is identical and the
verdict splits.

There, observation is exactly at chance. The total correlation of the next-state distribution, a standard
statistical-dependence measure, separates the 24 triadic from the 16 dyadic full-cycle forms at rank-AUC 0.500
(H2): no signal at all. This is the expected fate of an observational measure faced with a verdict that Q117
located in the determination's logic over its output statistics, and it matches the program's earlier nulls for
mutual information, transfer entropy, and O-information (Probes 45-47). Watching the dynamics' output cannot
tell the two classes apart.

Intervention separates them perfectly. Damage spreading, which flips one party and measures how far the
perturbation travels over the following steps, scores rank-AUC 1.000 on the same 40 forms (H3), with the
triadic and dyadic score ranges disjoint and the separation stable for any horizon of two steps or more. The
dyadic full-cycle forms dissipate a perturbation; the triadic ones sustain or amplify it. A do-intervention
probe recovers the verdict exactly where observation reads nothing, which is the signature predicted by IIT's
own interventional character and by Q117: the verdict is a fact about what the system does under perturbation,
not about what its outputs look like at rest.

The criterion is a sufficiency test, short of a replacement for the verdict. Damage spreading alone fails to
classify the full family (full-family AUC 0.851, H4): some acyclic dyadic forms also spread a perturbation
without being irreducible. Paired with the cycle screen of Q117, which is necessary and admits no false
negatives, the picture is a two-part non-Φ characterization that mirrors Q117's own structure: a topological
screen for the candidates, then an interventional test that decides them. The interventional test is the
sufficient half, read dynamically where Q117 read it logically.

This answers the first defense question in its weak form and sharpens its strong form. T1 asked for a
non-circular criterion on which triadic forms are distinct. In the weak sense, a criterion from a formalism
independent of IIT, the answer is now yes and sharp: damage spreading, perfect on the hard cases. It also
explains the program's prior failures: the behavioral checks (Probes 98, 107) were observational difficulty
measures, and Probe 48 found Φ orthogonal to coordination success, so the construct was being tested against
the wrong kind of criterion. The right kind is interventional. That points the strong form of T1 at a concrete
target: a real coordination that can be perturbed, with the spread of the perturbation measured. The verdict
predicts that triadic coordinations propagate a shock and dyadic ones absorb it.

## Caveats

- **Confirmatory, but the risky claim was real.** H3 could have failed exactly as H2 did; an interventional
  criterion was not guaranteed to separate the hard cases. It did, perfectly. H1 and H4 are framing and
  scoping results, not discoveries.
- **In-silico consilience, not behavioral validation.** "Non-circular" here means an independent formalism
  (statistical multi-information; Boolean-network damage spreading) computed from the same dynamical system. It
  is not behavioral or empirical-external data. The strong form of T1, a non-circular criterion on real
  coordination, remains open; this study identifies the criterion-type it should use.
- **One family, calibrated on it.** The criteria were prototyped on the 256-form strict-mediation family and
  evaluated on it; the horizon was fixed after checking stability. Generalization to other topologies and to
  larger or stochastic systems is untested, and is the natural successor study.
- **Damage spreading is a dynamical, not an intrinsic, measure.** Its agreement with Φ on this family is
  consilience between an extrinsic dynamical probe and an intrinsic information measure, not a derivation; the
  two could part on other families.
- **Exact verdict throughout.** The ground truth is the exact IIT-4.0 verdict over the MIP. In-silico.
