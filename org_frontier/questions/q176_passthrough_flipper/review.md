# q176 — Review

## Claim

The pass-through flip (commit S = D & R to relay S = D) does not universally collapse the
triadic verdict; 11 of 15 in-scope accounts stay triadic under pure relay (flip rate
0.267). The system's commit-vs-convey bit carries the entire CI sensitivity to coder
disagreement (median system share 1.000).

## Checks

The instrument control passes: faithful triad triadic at Phi 2.0, decoupled relay dyadic,
committed account triadic with a zero-width CI. Output is byte-identical across three
runs; every bootstrap seeds `numpy.random.default_rng(0)`.

H1 is an honest refutation. The prediction of a 100% flip rate was fixed before computing
and the data give 0.267. The survivors have a clear mechanism: the worker reads off the
counterpart, closing a cycle that skips the system, so relay leaves the structure
irreducible.

H2 is strong and clean. The zero width on the worker and counterpart parties is not a
coding artifact: under a committing system, an exhaustive check finds no worker reading
over the source basis that changes the verdict, so the system bit genuinely carries the
sensitivity.

## Limits

The basis family is small and discrete (five worker and five counterpart forms). The flip
rate 0.267 is specific to this basis, not a general constant; a different basis would give
a different number. The claim that survives is qualitative: relay does not guarantee a
pipe.

The H2 decomposition holds the non-tested parties at consensus, so it measures one-party
sensitivity, not interaction. A coder panel disagreeing on two parties at once is not
covered. The median share of 1.000 is for one account family; a family whose worker or
counterpart ambiguities could swing the verdict would lower it, though the search above
suggests that is hard to arrange while the system commits.

All inputs are synthetic. The study tests instrument behaviour, not a measured
coordination.

## Verdict

H1 REFUTED (null holds), H2 SUPPORTED. Both reported as computed. The two together give a
usable coding rule: the system bit is necessary but not sufficient for a literacy pipe.
