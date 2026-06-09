# Parked designs (Q76, Q77, Q78, Q86)

Four agenda questions that need a tool, a dataset, or a written correspondence the lab does not yet have.
Each is stated as a runnable plan, so the work is ready when the anchor exists. The format follows the
earlier parked designs: the question, what is missing, the procedure once it exists, and the discriminator
that would settle it. These are the design-stage entries from `RESEARCH_AGENDA_Q74.md`; the computable
questions (Q74, Q75, Q79, Q80, Q83, Q84, Q85) are done and on the record.

## Q76 — Behavioural validation of the dyadic/triadic verdict

**Question.** Does the structural verdict predict a behavioural difference? When two people coordinate
through a form the instrument calls triadic, is their coordination measurably harder than through a form it
calls dyadic, after equal practice?

**What is missing.** The dissertation's agent-based coordination experiment, wired to the Q63 outreach
forms rather than its own. For human subjects, ethics approval. This is the program's first empirical
anchor and crosses the validation gap.

**Procedure once it exists.** Build the read-recipient triad and the broadcast as coordination tasks in
the behavioural harness, with the same surface and party count. Run matched pairs of subjects (or agents)
on each, holding everything fixed but the structural verdict. Measure the coordination-success gap after a
fixed number of rounds.

**Discriminator.** A difficulty gap that tracks the verdict and not the party count: the triadic form is
harder than the dyadic one even when both present the same number of parties and the same interface. If the
gap tracks party count instead, the structural verdict is not behaviourally load-bearing.

## Q77 — Cheap proxy against exact Φ on real interaction logs

**Question.** On real multi-party interaction logs, does any cheap proxy track the exact-Φ verdict computed
on the small coordination units, where Finding 7 and Q72 say it should not?

**What is missing.** A dataset of logged multi-party interactions with identifiable parties and units small
enough for exact Φ (worker, system, counterpart triples; agent-mediated exchanges). The logs must let a
coordination unit be extracted and its transition structure estimated.

**Procedure once it exists.** For each small unit, estimate the transition structure from the log, compute
the exact dyadic/triadic verdict, and compute several cheap proxies (mediator in-degree, whole-minus-sum,
transfer entropy). Score each proxy's agreement with the exact verdict across units.

**Discriminator.** Whether any cheap estimate recovers the exact verdict on real data. The in-silico result
(Finding 7, Q72) is that proxies fail near chance and collide across the verdict; a proxy that recovered it
on real logs would either contradict the in-silico finding or reveal that real units are easier than the
adversarial Boolean ones.

## Q78 — Multivalued outreach

**Question.** Does the dyadic/triadic verdict survive when parties have graded states — a worker idle,
engaged, or overcommitted; a counterpart with a graded position — rather than binary on/off?

**What is missing.** Multivalued integrated information. The installed PyPhi is the binary IIT-4.0 branch.
Multivalued IIT needs the k-valued extension, which is not on this branch and does not share the
`new_big_phi` API the classifier uses.

**Procedure once it exists.** Lift the classifier's `tpm_from_rules` to k-valued nodes (a node's update is
a function into {0,…,k−1} over a mixed-radix state space). Rebuild the read-recipient triad with ternary
parties and a ternary commit, recompute the verdict and the major complex, and generalise the influence
measure to the fraction of states where changing a node's value changes another's next value.

**Discriminator.** Whether the dyadic/triadic verdict reproduces on ternary parties. If it holds, the
binary result is robust to graded state. If graded states create partial irreducibility the binary cut
hides, the place to look is whether intermediate states open joint determinations the two-valued model
misses.

## Q86 — The organization-theory bridge

**Question.** How does the five-pillar outreach-coordination law map onto the literacy/algorithmacy
construct and onto the account of the platform as a third coordination mechanism alongside the market and
the hierarchy?

**What is missing.** The formal correspondence, written as a paper rather than computed. Each structural
pillar needs a stated organizational counterpart, and the law needs placing in the line of formal
borrowings organization theory has made from other fields.

**Procedure once it exists.** Write the correspondence pillar by pillar: joint determination as the
condition for a genuine third party; liveness and reciprocity as the demand that the coordination be a
two-way exchange; non-substitutability as the platform's hold; core localization and delegation as the
shift of coordination from people to systems; the structural-not-cheap pillar as why a structural
instrument is needed. Place the result against organizational ecology and transaction-cost theory as prior
borrowings.

**Discriminator.** A stated mapping from each structural pillar to an organizational construct, with the
boundary of the analogy marked. The borrowing is formal, not metaphysical: the claim is that Φ measures
irreducibility, the same property that separates a third coordination mechanism from a faster version of an
old one, and not that a platform is conscious.
