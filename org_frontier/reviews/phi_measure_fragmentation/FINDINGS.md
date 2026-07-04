# Findings — the integration-measure literature proposes six families and validates one source in five against a ground truth

The corpus holds 68 sources whose central object is a measure of integrated information, integration,
complexity, or synergy. Three independent coders sorted each into a measure family and graded how it
establishes that the measure captures integration. The families are many and the validation is thin:
six distinct families each carry at least three sources, no family holds a majority, and only 13 of 68
sources (19%) validate their measure against a ground truth. Most propose or axiomatize a measure and
demonstrate it on a system of their own choosing.

## Intercoder reliability
| variable | Fleiss' κ | agreement | interpretation |
|---|---|---|---|
| measure_family | 0.963 | 97.1% | almost perfect |
| validation | 0.905 | 96.1% | almost perfect |
| substrate | 0.985 | 99.0% | almost perfect |

Three agent coders applied the fixed codebook blind to one another. κ above 0.90 on all three variables
discharges the single-coder objection: the family assignments and the validation grades are not one
reader's impression.

## Results
| # | Hypothesis | Verdict | Statistic |
|---|---|---|---|
| H1 | The literature proposes many distinct measure families | Supported | 6 families with >=3 sources; largest family 31%, no majority |
| H2 | Few sources validate against a ground truth; most assert or assume | Supported | ground_truth 13/68 (19%); internal-or-none 55/68 (81%) |
| H3 | Measure-families cite within-family more than across (fragmentation) | Partial | citation harvest rate-limited (shared S2 API); see below |

### H1 — six families, no convergence
| measure family | sources | share |
|---|---|---|
| integrated information decomposition / synergy (PID, PhiID) | 21 | 31% |
| causal emergence / effective information | 16 | 24% |
| practical Phi proxy (Phi*, Phi_AR, Phi_G, compression) | 10 | 15% |
| total correlation / multi-information | 8 | 12% |
| exact IIT Phi | 7 | 10% |
| geometric / neural (TSE) complexity | 6 | 9% |

Six families each clear the three-source bar and the largest holds under a third of the corpus. The
literature has not converged on one measure of integration; it maintains a standing plurality of them.

### H2 — validation is mostly internal
| measure family | ground_truth | internal | none/conceptual | total |
|---|---|---|---|---|
| exact IIT Phi | 1 | 4 | 2 | 7 |
| practical Phi proxy | 4 | 6 | 0 | 10 |
| causal emergence | 1 | 11 | 4 | 16 |
| iid / synergy | 2 | 19 | 0 | 21 |
| total correlation | 4 | 4 | 0 | 8 |
| geometric / TSE complexity | 1 | 5 | 0 | 6 |
| total | 13 | 49 | 6 | 68 |

Internal validation — axioms, desiderata, or a demonstration on a system the author picked — is the
norm (49/68, 72%). Scoring the measure against a ground truth (exact Phi, a reference criterion, a known
generative structure) is the exception (13/68, 19%). The families divide on this. Practical proxies
have the highest ground-truth rate (4/10, 40%), because a proxy exists to approximate exact Phi and can
be checked against it. The decomposition / synergy family is almost entirely internal (19/21), its
measures established by lattice axioms rather than by recovering a known quantity.

### H3 — fragmentation (partial)
The citation harvest (`lib/harvest.py`, title-resolved seeds on the unauthenticated Semantic Scholar
API) ran against a rate limit shared with several concurrent reviews and did not complete in the run
window. The cluster-to-cluster citation matrix over the six family clusters is therefore not reported
here. H1 and H2 stand on the coded corpus; H3 is left partial. The reproduce command below completes
the matrix when the harvest finishes (edge files are checkpointed, so a restart resumes).

## What the data show
The coding answers the review's question. The proposed measures of integration are many, not one: the
codebook's six families are all populated and none dominates. And the field mostly does not check its
measures against a ground truth — four in five sources rest on axioms or a self-chosen demonstration.
This mirrors the foundations arm at the level of the literature. Where the foundations experiments
found, on exactly-computable systems, that no single cheap number is exact Phi, this review finds that
the literature proposing those numbers rarely tests them against exact Phi at all. The validation gap
the foundations arm closes with computation is, in the published record, mostly open.

## Limitations
The coders are LLM agents applying a fixed codebook, not trained human raters; kappa among agent passes
is high but is not a substitute for independent human coding. The corpus is bounded by the
semantic-search connectors' coverage and by English-language indexing, and it is deliberately
measure-centric — application papers that use a fixed measure without engaging it are out of boundary,
so the corpus speaks to how measures are proposed and validated, not to how often they are used. The
`validation` grade is coded from the abstract; a paper that validates against a ground truth in its
body but does not say so in the abstract is undercounted, which biases the ground-truth rate downward.
H3 is partial: the citation matrix was not computed, so the fragmentation claim is neither supported
nor challenged here.

## Reproduce
```bash
python -m org_frontier.reviews.phi_measure_fragmentation.build_corpus
python -m org_frontier.reviews.lib.harvest \
    org_frontier/reviews/phi_measure_fragmentation/seeds.json \
    --out org_frontier/reviews/phi_measure_fragmentation/edges/
python -m org_frontier.reviews.lib.reliability \
    org_frontier/reviews/phi_measure_fragmentation/coding \
    --categorical measure_family,validation,substrate \
    --out org_frontier/reviews/phi_measure_fragmentation/results/frozen.json
python -m org_frontier.reviews.phi_measure_fragmentation.run
```
Registered numbers: N = 68; families >=3 = 6; largest family share = 0.31; ground_truth rate = 0.19;
kappa = measure_family 0.963, validation 0.905, substrate 0.985.
