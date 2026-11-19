# Q221 maintainer decision proposal — preserve history, disambiguate interventions

**2026-10-15 — editorial/architecture recommendation only, not a new scientific result.** Q221 remains a draft. This note does not modify q161, q220, or their historical outputs. The authoritative empirical and computational evidence is in `TARGET_AUDIT.md`, `identifiability/results/target_variants.txt`, `GATES.md`, and `confirmatory_4node/RESULTS.md`.

## Decision requested

Should the lab's word **bottleneck** refer to:

1. **Rule freeze (existing q161):** set the frozen node's update rule to zero but keep its state available for IIT perturbations, and retain its outgoing dependencies. Re-evaluate system-integrated information in the modified network.
2. **Background condition:** treat the selected node as fixed external context, evaluate the residual subsystems excluding it, at the specified constant state.
3. **Rule freeze plus edge removal:** a different perturbation that changes both a node rule and its contribution to the connectivity model.

These are **different interventions and estimands**, not competing numerical implementations of one universally defined IIT quantity. It is therefore a mistake to silently replace one with another or to designate either result an implementation bug solely because the targets disagree.

## Evidence relevant to this choice

- In Q221's three surviving three-node classes, the historical q161 rule-freeze target differs between recurrence-equivalent pairs. The pinned IIT runs have the same intact major complex and same intact Phi within each pair.
- Under the examined background-condition variant, no surviving pair retains two distinct eligible target sets; in one class an eligibility rule itself changes. The rule-freeze target difference therefore does **not** establish a formalism-independent IIT property.
- The original q161/q220 studies were conducted with the historical rule-freeze definition. Their outputs are valid *as results of that declared algorithm*, subject to the existing methodological limitations, and must not be silently rewritten in place.
- Independently, Target A (non-injectivity of population pairwise recurrence summaries for the transition law) is a mathematical statement **independent of how a bottleneck target is defined**. The preregistered four-node study and follow-up likewise concern that statistical target, not q161 leave-one-out bottlenecks.

## Recommended disposition

**Preserve the existing q161 rule-freeze convention as the historically named operational score, but rename or explicitly label it wherever ambiguity would mislead readers.** Suggested public name: `rule-freeze Φ-drop articulation set`. Describe that the frozen node remains a perturbed element and its outgoing edges are kept.

Do **not** assert that this is the unique IIT-consistent operationalization of "removing a node." If the lab wants a background-conditioned removal target, add a **separately named**, versioned target with its own state-selection, held-value, subsystem, eligibility, and tie-handling definitions. Report the two measurements side by side in future new analyses, never by retroactively substituting one into past q161/q220 outputs.

For a prospective empirical study, choose the target based on the actual intervention represented by the domain question, then preregister that target and keep separate its predictive loss: exact maximizing **set** versus selecting **a member** of the set. Q221's lead example permits a shared correct node even when full sets differ.

## Choices and consequences

| Maintainer choice | Historical studies | Q221 valid headline | Further work |
|---|---|---|---|
| Keep historical rule freeze | Keep unchanged | Mathematical recurrence-to-transition limit; **conditional** set-target example | Label intervention and target precisely |
| Adopt background condition for future studies | Keep unchanged and add separate target | Mathematical recurrence-to-transition limit; no surviving eligible distinct background-condition bottleneck target in current screen | New prospective q220 target study, not a reinterpretation of old results |
| Claim either target measures "true node deletion" or a universal IIT bottleneck | Unsupported | Would overstate the evidence | Formalize the intervention semantics first |

## Merge/review recommendation

The exact mathematical Target-A work and bounded empirical synthetic studies are independently assessable without resolving the q161 vocabulary. The maintainer can review the PR as a **statistical methods contribution** while leaving the IIT-derived Target-B definition explicitly conditional, provided the draft keeps its current caveat and does not claim an intrinsic IIT theorem.

This memo is a proposal for a human maintainer's scientific decision; it does **not** approve merging, change the PR's draft status, or modify any historical data.
