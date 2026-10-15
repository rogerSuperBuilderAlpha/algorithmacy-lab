# Audit of the q161 bottleneck target (mandate step 11)

**Evidence.**
- Results: `identifiability/results/target_audit.txt` and `identifiability/results/target_variants.txt`.
- Scripts: `identifiability/target_audit.py` and `identifiability/target_variants.py`.
- Run in the pinned PyPhi environment.

## What the target is

The q161 bottleneck set B is a **project-derived** quantity built on IIT 4.0. It is not an IIT 4.0 object.
`q161 bottleneck_set` computes it as follows:
1. Compute base Φ, the major-complex Φ maximised over reachable states of the deterministic TPM.
2. For each node k, replace k's rule with the constant 0 ("freeze"). Rebuild the TPM and connectivity matrix
   with `tpm_from_rules` / `cm_from_rules`.
3. Recompute the major-complex Φ of the modified **3-node** network over its own reachable states. This is the
   residual Φ.
4. Drop_k = base Φ − residual Φ. B = argmax of the drops, with ties within `TOL` = 1e-6. If the maximum drop is
   ≤ TOL, B = ∅.

The frozen node stays in the network. PyPhi still perturbs its state, and every other node still reads it,
because the connectivity matrix keeps its outgoing edges.

## Invariance checks on the lead pair

| check | P | Q |
|---|---|---|
| node-permutation equivariance (6 maps) | yes | yes |
| invariance under value relabelling (7 non-trivial flip masks) | yes | yes |
| ties | none: drops {2, 0, 2} | none: drops {1, 0, 2} |
| depends on node order | no (equivariant) | no |

## Mechanism of the difference

Freezing X:
- **In P**, the residual network has **no** complex, so the drop is 2.
- **In Q**, the residual network keeps the single-node complex {Y} with Φ = 1, so the drop is 1.

Y's rule (X⊕Y vs ¬(X⊕Y⊕H)) decides whether a residual complex survives on Y. Y lies outside the major complex
{X,H} of the intact system.

When the same networks are built with the frozen node's edges removed, the residual is {H} with Φ = 1 in both P
and Q. This check is `identifiability/edge_removal_check.py` (`results/edge_removal_check.txt`). It confirms that the q161 result depends on keeping the frozen
node as a perturbed element.

## Alternative operationalisation: IIT background condition

Here node k is held at a fixed value as a background condition of the **original** network. Residual Φ is taken
over subsystems that exclude k, at states reachable with x_k = v.

| survivor pair | q161 (freeze rule) | background condition (v = 0 or 1) |
|---|---|---|
| P vs Q | {X,H} vs {H}: **differ** | {X,H} vs {X,H}: **equal** |
| aff(9,6,10) vs aff(9,15,12) | {X,H} vs {H}: differ | {X,H} vs {X,Y,H}: the second has \|B\| = 3, so it is **ineligible** |
| aff(9,6,11) vs aff(9,14,10) | {X,H} vs {H}: differ | {X,H} vs {X,H}: **equal** |

## Assessment

The target difference in every survivor pair is an artefact of the q161 operationalisation:
- the frozen node is kept as a perturbed element, with rule := 0 and its edges retained;
- residual Φ can then be carried by a node outside the major complex.

Under a background-condition reading closer to IIT's treatment of fixed external elements, no surviving pair has
two eligible, different targets.

Major complex and Φ are identical within every pair (`rep_verify.txt`).

This makes **target B (the q161 structural target) survive only conditionally on the q161 convention. Target C
(an IIT quantity) does not differ.**

## Recommendation for the lab (not applied; q161 is untouched)

Any study that uses the q161 bottleneck as ground truth should:
- state the freeze convention it uses;
- report sensitivity to the background-condition alternative.
