# q202 — Does the Φ-bridge survive its own falsification battery?

The survey arm reads a per-worker Φ_coord from each simulated worker's W-S-C coordination form
with the exact IIT-4.0 instrument and reports its relation to the algorithmacy competence score
(ACS). Two cheap explanations could account for that relation without any role for irreducibility.
The first is a labelling artifact: pair any per-worker scalar with ACS by the same row index and a
correlation can appear. The second is a structural shortcut: the connectivity-matrix edge density
of a worker's form is a cheap non-Φ reading that might carry the whole relation. This study fixes
both as a pre-registered battery and asks whether the bridge survives.

## The two threats, as tests

H1 is a randomization test. Shuffle the worker-to-form mapping, recompute the Φ_coord-to-ACS
correlation, and ask whether the real correlation falls outside the shuffled null. A bridge that
rides on the index alone would sit inside the null.

H2 is an incremental-validity test. The edge-density proxy separates the two whole-system forms
exactly as Φ_coord does, so it is a fair competitor. The question is whether Φ_coord adds variance
the proxy misses once both predict ACS together.

## Result

The bridge survives H1 in both cohorts. Shuffling centers the correlation on zero (null means
-0.003 and -0.002) and the real effect sits far outside the null at p = .001. The relation does
not come from the row index.

H2 splits along the form space, and the split is the informative part. On the whole-system cohort
there are two forms, so edge density and Φ_coord are perfectly collinear (r = 1.000) and ΔR² is
zero: the cheap proxy ties Φ. A two-level structure offers nothing for the two measures to
disagree about. The facet cohort has four forms whose edge density and irreducibility rank them
differently. The counterpart-coupled form carries the most edges yet less Φ than the mediated
form. There Φ_coord adds ΔR² = +0.377 over the proxy, with a 95% CI of [+0.318, +0.439] that
excludes zero.

## Reading

A cheap structural proxy matches Φ on a two-form catalog and falls behind on a richer one. This is
the expected shape for an affirmative case. Edge density counts wires; Φ reads whether the wiring
makes the form irreducible. The two agree when there is only one structural step between the
forms, and they part once the catalog contains a form with more wires but less integration. The
exact-Φ instrument is what reads that difference, and the difference is where the construct
relation lives in the richer cohort.

## Scope

Both cohorts are simulated. The Φ_coord-to-ACS association is built into the synthetic data by
construction; the battery tests whether the bridge's reported relation is an index artifact and
whether Φ adds over a cheap proxy on that synthetic data. No worker is measured. The bridge to
real survey response data stays open, and the proxy comparison should be rerun on a real form
catalog once one exists.
