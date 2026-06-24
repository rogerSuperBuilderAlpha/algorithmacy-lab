# q181 — Two flippers at once: redundancy, not interaction

A coded account of a worker-system-counterpart coordination names a Boolean determination
rule for each party. Two coding choices each flip a triadic verdict to dyadic on their own.
The substitutability flipper re-reads the single irreplaceable worker as one slot in an
interchangeable pool, so the worker decision becomes a disjunction over pool members. The
pass-through flipper switches the system from commit (S = W & R, the system acts only when
the worker decision and the counterpart request both hold) to relay (S = W, the system
passes the worker decision through and ignores the counterpart). This study asks what
happens when a coder applies both at once: whether the verdict effects compose additively,
or whether one flipper masks the other in the Φ confidence interval.

## Method

The study reuses the field bridge `org_frontier/field/rule_to_phi.py`. `rule_to_phi`
encodes the per-party rules into a TPM and reads the exact IIT-4.0 Φ verdict; `phi_ci`
propagates coder disagreement into a bootstrap-t Φ interval; `major_complex` reads the
maximal complex. Φ is not reimplemented.

A single account carries one knob per flipper. Pool size k sets the substitutability flip
(k = 1 specific, k >= 2 pooled); system mode sets the pass-through flip (commit or relay).
The grid over {specific, pooled} x {commit, relay} gives the no-flipper baseline, each
single flipper, and the double flipper. H1 reads the verdict of every cell. For H2, a panel
of 24 coders each decides independently whether to apply each flipper, with contested flips
drawn from the [0.3, 0.7] split band; each coder's Φ is the verdict their two decisions
select. The single-flipper panels contest one flip; the joint panel contests both. The test
compares the joint CI width to the union of the single-flipper CIs.

## Results

The no-flipper baseline reads triadic at Φ = 2.0. Substitutability alone, pass-through
alone, and both together all read dyadic at Φ = 0.0. No combined account re-reads triadic,
so H1 is supported: the flippers do not interact to restore irreducibility. The double
flipper reaches the same verdict as either single flipper, which is masking rather than
addition. Each flip already drives Φ to its floor, so the second flip has nothing to
remove.

In the contested case the joint CI width is 0.806 against a union width of 1.386, a gap of
-41.8%. The joint interval is narrower than the union, not within 10% of it and not more
than 25% above it. H2 is not supported, and the cause is contraction, not amplification.
Contesting both redundant flips concentrates the panel on Φ = 0, because a coder reads
triadic only by declining both flips. Two redundant disagreements carry less verdict
uncertainty than one.

The spectator-only control fixes the mechanism. A node that reads the system and feeds
nothing back leaves the major complex at the triad (W, S, C) with Φ = 2.0, while dropping
the whole-system verdict because the spectator itself is reducible. A coded choice changes
the verdict by touching the cycle, not by adding another observer.

## Scope and validation gap

The result is structural and holds for synthetic coded rule sets with known structure. No
worker is measured. The empirical arms report results on synthetic data. Whether a coded
account matches an observed coordination, and whether real coders split on these flips the
way the synthetic panels do, are open questions this study does not settle.
