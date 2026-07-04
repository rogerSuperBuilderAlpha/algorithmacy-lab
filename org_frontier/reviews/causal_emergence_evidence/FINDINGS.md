# Causal emergence is argued and modeled, not measured — and its reality claim has not converged

Sixty sources on causal emergence and downward causation, three blind coders, one adjudicated
dataset. The literature is overwhelmingly conceptual and formal-model work; measurement of an
emergence quantity on a real system is rare (4 of 60). Its central claim — that macro-scale causal
emergence is real — is not settled: a deflationary reading holds a persistent fifth of the sources
that take a side, though the field leans toward emergence-is-real. The formal work splits across
three formalisms, with information theory dominant but not alone.

## Intercoder reliability
| variable | Fleiss' kappa | mean agreement | interpretation |
|---|---|---|---|
| evidence | 0.846 | 92.2% | almost perfect |
| formalism | 1.000 | 100.0% | almost perfect |
| claim_direction | 0.921 | 95.6% | almost perfect |

Three independent agent coders, blind to one another, on a fixed codebook. All three variables clear
Landis & Koch's 0.80 "almost perfect" bar. The kappa answers the single-coder objection: these are not
one reader's judgment calls.

## Results
| # | Hypothesis | Verdict | Statistic |
|---|---|---|---|
| H1 | conceptual + formal dominate; empirical rare | **Supported** | conceptual+formal_model = 56/60 (93%); empirical = 4/60 (7%) |
| H2 | reality claim contested, no convergence | **Qualified** | side-takers 35 emergence_real / 9 deflationary (80% / 20%); 16 neutral |
| H3 | formal approaches fragment | **Supported (coding); citation matrix PARTIAL** | info-theoretic 20, dynamical 6, statistical 5 (na 29); among formal/empirical: IT 14, dynamical 4, statistical 3 |

## What the data show

**H1 — supported, and strongly.** The evidence distribution is 39 conceptual, 17 formal_model, 4
empirical. Conceptual argument and toy/simulated models together are 93% of the corpus. The four
empirical sources all compute an emergence quantity on real measured neural data
(`yang2023findingemergence` on fMRI, `rosas2020reconciling` on ECoG, `mcsharry2024learningemergent` on
brain-activity datasets, `barnett2021dynamicalindependence` on neurophysiological time series). No
source computes an emergence measure on real economic, social, or organizational data. The field
argues that macro can beat micro and models it on Markov chains, Boolean networks, Ising models, the
Game of Life, and flocking simulations; it rarely measures it in the wild, and never yet outside
neural data.

**H2 — qualified.** The reality claim has not converged, but the split is asymmetric. Among the 44
sources that take a side, 35 (80%) read macro-scale causal emergence or downward causation as real and
9 (20%) give a deflationary reading (emergence is epistemic, observer-relative, or a measure artifact;
downward causation is incoherent or dispensable); 16 sources are neutral (surveys, measure-development,
method). The pre-registration predicted both readings above ~25% (contested and balanced) and would
challenge the hypothesis if one fell below ~15% (effectively settled). The deflationary share sits
between those lines at 20%. The honest reading: the question is not settled — a real, named
deflationary critique persists (`dewhurst2020realpatterns`, `dewhurst2021neither`,
`eberhardt2022distortions`, `heil2021emergencedc`, `wong2020withoutvertical`,
`leidenhag2016panpsychism`, and others) — but the field is not evenly divided; the emergence-is-real
reading dominates four to one among side-takers. Contested, not balanced; unconverged, not open.

**H3 — supported on the coding; citation matrix partial.** The formal apparatus fragments. Restricting
to the 21 sources that compute something (formal_model + empirical), 14 are information-theoretic
(effective information, integrated information, information decomposition), 4 are dynamical
(dynamical independence, coarse-graining of state-space dynamics, renormalization), and 3 are
statistical (interventionist/Pearl-style causation, causal primitives). Information theory is the
plurality but holds only two-thirds of the formal work; two other formalisms carry real shares. The
citation-matrix test (whether these formalisms cite across the divide) is reported partial — see
Reproduce — because the unauthenticated Semantic Scholar harvest is rate-limited and slow; the coded
fragmentation stands on its own.

## Limitations
- **Agent coders.** The three coders are LLM agents applying a fixed codebook, not trained human
  raters. The kappa measures their mutual agreement, which is high, but shared model priors could
  inflate agreement relative to independent humans. The codes are auditable against the corpus
  abstracts.
- **Search-backend-bounded corpus.** The corpus is the screened union of Scholar Gateway and Consensus
  results. Scholar Gateway returned many tangential hits (molecular-dynamics coarse-graining, generic
  time-series causal discovery) that were screened out by the substantive rule; a different backend or
  query set could shift the mix. Sixty sources is a sample of a larger literature, not a census.
- **Abstract-only coding.** Coders saw title + abstract, not full text. A paper whose empirical work is
  buried past the abstract could be miscoded as formal; this biases the empirical count downward, but
  not enough to overturn the 93/7 split.
- **Elided references and a slow harvest.** The citation channel is partial (publishers elide
  references) and the harvest is rate-limited, so the H3 citation matrix is reported partial rather
  than as a finished block-diagonal test.
- **DOIs.** 26 of 60 sources carry verified DOIs; the rest resolve by title in the harvest. This does
  not affect the coding-based verdicts (H1, H2, H3-coding).

## Reproduce
```bash
# from the repo root: /Users/ludwitt/iit-playground/pyphi-experiments
python3 org_frontier/reviews/causal_emergence_evidence/build_corpus.py
python3 -m org_frontier.reviews.lib.reliability \
  org_frontier/reviews/causal_emergence_evidence/coding \
  --categorical evidence,formalism,claim_direction \
  --out org_frontier/reviews/causal_emergence_evidence/results/frozen.json
# H3 citation matrix (rate-limited; resume-safe, re-run until edges/ fills):
python3 -m org_frontier.reviews.lib.harvest \
  org_frontier/reviews/causal_emergence_evidence/seeds.json \
  --out org_frontier/reviews/causal_emergence_evidence/edges/
python3 -m org_frontier.reviews.lib.bibliometrics \
  org_frontier/reviews/causal_emergence_evidence/edges \
  --clusters org_frontier/reviews/causal_emergence_evidence/clusters.json
```
Headline numbers: corpus N = 60; kappa (evidence/formalism/claim_direction) = 0.846 / 1.000 / 0.921;
empirical 4/60; emergence_real vs deflationary among side-takers 35/9.
