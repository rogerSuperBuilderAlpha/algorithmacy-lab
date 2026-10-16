# Follow-up orbit-pair unit and seed-independence audit

**2026-10-15 — post-hoc study-design verification, not a new confirmatory test or an amendment to the registered analyses.**

## Population and statistical unit

The 600-pair follow-up preregistered a simple random sample **without replacement** from the finite population of 1,832 untested recurrence-equal, non-isomorphic **orbit pairs**. The primary estimand is the proportion of these orbit pairs separated by each specified within-pair classifier at T=600, not the proportion of distinct individual network orbits nor the accuracy of a classifier transferred to wholly unseen networks.

The sampled 600 pair records contain **782 distinct orbit identifiers**. Of the 600 pairs, **413 share at least one orbit** with another sampled pair; the largest degree of an orbit within the sampled pair graph is 7, and there are 279 connected components. These facts do not mean the same *orbit pair* was tested twice: the 600 unordered pair identifiers are unique, all are disjoint from the original 40 pair records, and source-controlled tests already check this.

The overlap does matter when interpreting the study as evidence about a hypothetical superpopulation of **independently sampled network forms**. Orbit pairs sharing a system can share structural difficulty, and the 600 records should not be described as 1,200 independent model forms.

## Stochastic evaluation is independent per sampled pair

The preregistered trajectory seed formula is base 5,220,000 + 1,000*q + 500*member + r for pair index q=0..599, member=0/1 and run r=0..299. Its per-pair seed block is [5,220,000+1,000*q, 5,220,799+1,000*q]. Blocks for distinct pair indices are disjoint by at least 201 integer seeds. The sampling of orbit-pair identities uses a separate seed 5,210,002.

Thus, under the pseudorandom-generator model, every recorded pair gets independent trajectory draws even when a network orbit reappears in another pair. The experiment estimates a **pair-specific** decision event using fresh simulations and the fixed per-pair classifier, not an edge in a graph conditioned on one reused physical time series.

## Interpretation of registered Wilson intervals

The protocol applies Wilson intervals across 600 sampled **orbit-pair decision events** and two-classifier Bonferroni adjustment. Pair sampling is without replacement from a finite population, and each observed decision also has Monte Carlo simulation variation. A textbook iid Bernoulli Wilson interval is therefore an **approximation**, not an exact design-based confidence procedure. Applying a naive finite-population correction to the *entire observed Bernoulli variance* would be unjustified because conditional simulation noise is not reduced by sampling without replacement. Conversely, treating shared orbit identities alone as proof of positive sampling correlation would ignore the without-replacement design and independent per-pair simulation streams.

The original preregistered C2/C4 counts and Wilson decision rules must remain unchanged. An orbit-cluster superpopulation analysis could be worthwhile in a different, prospectively defined study; a post-hoc connected-component bootstrap is not a replacement for the registered finite orbit-pair estimand.

## Reproducible counts and safeguard

The new focused test in test_confirmatory_4node.py recomputes distinct-orbit and shared-orbit counts from the committed followup_pairs.json and verifies disjoint trajectory seed blocks across q. This is input-integrity QA and does not inspect classifier outcomes.

**Disposition:** No change to the registered C2/C4 verdicts from this audit. The scope remains the specified finite family of orbit pairs, candidate sampling rule and fresh within-pair trajectories. Generalization to unseen model families and new network sizes is not established.
