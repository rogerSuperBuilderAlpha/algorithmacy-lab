# Argued, modeled, seldom measured: an archival review of the causal-emergence literature

## Research summary

Causal emergence names a specific claim: a macro-scale description of a system can carry causal power
that its micro-scale description lacks, and an explicit measure can detect the difference. This review
treats the literature that makes and disputes that claim as a dataset. Sixty sources, spanning the
information-theoretic effective-information program, its dynamical-systems and statistical relatives,
and the philosophy of downward causation, were coded by three independent raters on three variables:
what kind of evidence a source offers, what formal apparatus it uses, and which direction its central
claim runs. Intercoder reliability is high (Fleiss' kappa 0.85 to 1.00). Three results follow. The
literature is 93% conceptual argument and toy-model work; only four of sixty sources compute an
emergence quantity on real measured data, all of it neural. The reality claim has not converged: among
sources that take a side, 80% read emergence as real and 20% give a deflationary reading, an
asymmetric and unsettled split. The formal work fragments across three apparatuses, information theory
holding two-thirds of it and dynamical and statistical approaches the rest. For a research program
that reads a coordination form as a macro-scale whole doing irreducible causal work, the map is clear:
the nearest formal neighbor is an active, unsettled, and largely unmeasured field, not a closed one.

## Introduction

Whether a whole can do causal work its parts cannot is an old question in the philosophy of mind and
a newer one in complex-systems science. The philosophical version runs through Jaegwon Kim's exclusion
argument: if every physical effect has a sufficient physical cause at the micro level, a higher-level
cause seems either redundant or a violation of physical closure. The scientific version arrived with a
measure. Hoel, Albantakis, and Tononi (2013) defined effective information, showed that for certain
causal architectures it peaks at a coarse-grained macro scale, and called the gain causal emergence.
The measure turned a metaphysical dispute into something a model could exhibit and, in principle, data
could show.

A decade of work followed. Some of it extended the measure — integrated information across scales,
information decomposition, singular-value formulations, machine-learning methods that search for the
macro variable directly. Some of it disputed the measure, arguing that the emergence effective
information detects is epistemic, observer-relative, or an artifact of a maximum-entropy assumption.
Some of it never used a measure at all and argued about downward causation on metaphysical grounds.

This review asks three questions of that body of work, each phrased so a number can answer it. What
kind of evidence does the field rest on — argument, model, or measurement? Has its central claim
converged, or do the emergence-is-real and deflationary readings both persist? And does the formal
work proceed from one framework or several? The questions matter to a research program that borrows
this machinery. Reading a coordination form as a candidate for macro-scale irreducibility places that
program next to causal emergence. Knowing whether the neighbor is settled or open, measured or
modeled, unified or fragmented, tells the program what ground it stands on.

## Framework

The review follows the systematicity pipeline of Simsek, Fox, and Heavey (2023) and draws its
questions from the knowledge-weaving typology of Simsek, Heavey, Fox, and Yu (2022). Knowledge weaving
sorts a field's claims into stylized facts, key assumptions, enduring critiques, and substantive
omissions. Each type suggests a hypothesis a coded corpus or a citation graph can test.

The first hypothesis targets a stylized fact the field half-admits: that causal emergence has been
"found in real data across the sciences." H1 predicts the opposite balance — that conceptual and
formal-model work dominate and empirical demonstration on real systems is rare. The second targets an
enduring critique: the reality of macro-scale causation. H2 predicts the dispute is live, with
emergence-is-real and deflationary readings both well represented and no convergence. The third
targets a substantive omission: whether the formal approaches talk to one another. H3 predicts
fragmentation — several formalisms, each carrying a real share, developing with limited cross-citation.

The hypotheses were committed before any source was coded. Each names the coded variable that tests it
and the outcome that would challenge it. A challenged hypothesis is reported as a finding, not
smoothed away.

The three claims are visible in the corpus as distinct kinds of paper. The stylized fact behind H1
appears whenever a measure paper motivates itself by pointing at applications: the survey of Yuan and
colleagues (2024) frames identifying causal emergence from data as the field's second grand challenge,
which presumes the data work exists to be identified. The critique behind H2 is a standing exchange —
Hoel's map-better-than-territory argument and Eberhardt and Lee's reply that the map's distortions
obscure the territory sit in the same corpus, neither having closed the other out. The omission behind
H3 is structural: the information-theoretic, dynamical, and statistical treatments each carry their own
vocabulary — effective information, dynamical dependence, causal primitives — and a reader cannot
assume a citation runs from one to the next.

## Method

**Corpus boundary.** A source qualifies if its central concern is causal emergence, downward or
top-down causation, or macro-scale causation — whether and how a coarse-grained description carries
causal power the micro description lacks. Included: information-theoretic emergence measures,
dynamical-systems accounts of emergent macro-variables, statistical treatments of macro causation, and
the philosophy of downward causation's reality. Excluded: coarse-graining with no emergence claim,
such as molecular-dynamics model reduction for speed, and generic time-series causal discovery with no
macro-versus-micro question.

**Search.** Academic search ran through two backends, Scholar Gateway and Consensus, over queries
spanning the subtopics: causal emergence and effective information, downward causation and its formal
measures, macro causation and coarse-graining, information decomposition, dynamical independence and
computational mechanics, and the deflationary critiques. Scholar Gateway returned many tangential hits
that the boundary rule removed. The screened union is sixty sources.

**Coding.** Three variables. Evidence records how a source supports its claim: conceptual (argument,
no measure), formal_model (a measure computed on a toy, simulated, or abstract system), or empirical
(a measure computed on real measured data). Formalism records the apparatus: information_theoretic,
dynamical, statistical, other, or na. Claim_direction records where the source lands on the reality
question: emergence_real, deflationary, or neutral. Three agent coders applied the fixed codebook
blind to one another, coding each source from its title and abstract. Fleiss' kappa was computed per
variable and a majority-vote dataset adjudicated.

**Analysis.** H1 reads the evidence distribution. H2 reads the claim-direction split among
side-takers. H3 reads the formalism distribution and, on the harvested citation graph, the
formalism-to-formalism citation matrix.

## Results

**Reliability.** Agreement is high on all three variables, which is what licenses the single
adjudicated dataset the rest of the analysis uses.

| variable | Fleiss' kappa | mean agreement |
|---|---|---|
| evidence | 0.846 | 92.2% |
| formalism | 1.000 | 100.0% |
| claim_direction | 0.921 | 95.6% |

**Evidence (H1).** The distribution is lopsided toward argument and model.

| evidence | count | share |
|---|---|---|
| conceptual | 39 | 65% |
| formal_model | 17 | 28% |
| empirical | 4 | 7% |

Conceptual and formal-model work together make 93% of the corpus. The four empirical sources compute
an emergence quantity on real measured data, and every one of them uses neural recordings: fMRI during
movie viewing (Yang et al. 2023), electrocorticography (Rosas et al. 2020), differentiable estimators
on brain-activity datasets (McSharry et al. 2024), and neurophysiological time series via dynamical
independence (Barnett and Seth 2021). No source in the corpus computes an emergence measure on real
economic, social, or organizational data. The founding results run on Markov chains, Boolean networks,
Ising models, Conway's Game of Life, and flocking simulations. The demonstration that macro beats micro
lives in models; where it touches data, the data are from the brain.

What the four empirical sources do is worth stating precisely, because it bounds the field's contact
with data. Each takes a real neural recording, searches for or fixes a coarse-grained macro variable,
and computes an emergence quantity on it. None claims a controlled test of downward causation; each
reports that a macro variable, learned or specified, carries emergent structure the micro data do not
supply on their own. The measurement is real, and it is entirely within neuroscience. The pattern
matches the theory's origin — effective information and integrated information both grew from a theory
of consciousness — and it marks how far the empirical work has traveled from that origin, which is not
far.

**Claim direction (H2).** The reality question splits, but not evenly.

| claim_direction | count |
|---|---|
| emergence_real | 35 |
| neutral | 16 |
| deflationary | 9 |

Sixteen sources take no side — surveys, measure-development papers, and methods that stay agnostic.
Among the forty-four that do, thirty-five read macro-scale emergence or downward causation as real and
nine give a deflationary reading: the emergence is epistemic or observer-relative, downward causation
is incoherent or dispensable, the measure records a distortion rather than a scale. The
pre-registration set two lines: both readings above about a quarter of side-takers would mean a
balanced live dispute, and either below about a sixth would mean the question had settled. The
deflationary share falls between them at 20%. The dispute is live — the critiques of Dewhurst,
Eberhardt and Lee, Heil, Wong, and Leidenhag are specific and unanswered — but the field is not evenly
divided. Emergence-is-real leads four to one. The reality claim is unconverged and asymmetric.

**Formalism (H3).** The formal apparatus is not one thing.

| formalism | count (all) | count (formal + empirical only) |
|---|---|---|
| information_theoretic | 20 | 14 |
| dynamical | 6 | 4 |
| statistical | 5 | 3 |
| na | 29 | 0 |

Twenty-nine sources use no formal apparatus, the philosophy-of-downward-causation cluster. Among the
twenty-one that compute something, information theory holds fourteen, the dynamical approaches four,
and the statistical approaches three. Effective information and its relatives are the plurality, but a
third of the formal work runs on other machinery — dynamical independence and coarse-grained
state-space dynamics on one side, interventionist and causal-primitive accounts on the other. The
coded fragmentation supports H3.

The citation-matrix half of H3 is reported partial. The Semantic Scholar harvest is unauthenticated
and rate-limited; the resolved seeds (led by the Hoel papers, with 127 to 345 forward citers each)
confirm the graph is rich, but too few seeds resolved within the harvest window to freeze a
formalism-to-formalism matrix. The reproduce block below re-runs the harvest, which is checkpointed
and resumes where it stopped. The coded distribution stands on its own as evidence of fragmentation;
the cross-citation structure is left for the completed harvest.

## Discussion

Three facts about the neighbor emerge. It argues and models more than it measures. Its central claim
is live and unsettled, tilted toward realism but trailed by a specific, unanswered critique. Its
formal tools are plural. Each fact bears on a research program that treats a coordination form as a
macro-scale whole and reads an integrated-information measure as a lens on its irreducibility.

The empirical scarcity is the most consequential. Causal emergence is thirteen years old and its
demonstration on real systems remains confined to four neural datasets. Applying an emergence measure
to an organizational or economic system would not be a late entry into a crowded empirical field; it
would be among the first measurements outside the brain. The gap the founding papers point at — "found
in real data across the sciences" — is mostly still a promissory note.

The unconverged reality claim sets the altitude for any borrowing program. The deflationary readings
are not fringe. They argue, with care, that effective information's macro advantage can reflect a
maximum-entropy assumption extraneous to the system, or that the emergence it detects is epistemic. A
program that computes such a measure inherits the burden of saying which reading it endorses and why.
The honest stance treats a high measure as evidence to be interpreted, not as a settled fact of
macro-scale causation.

The fragmentation is an opportunity as much as a warning. Comolatti and Hoel's consilience result —
that a dozen independent causal measures all exhibit emergence because they share a few causal
primitives — suggests the formalisms may be closer than their citation patterns show. A program that
computes one measure can position it against the others rather than in isolation.

The neutral cluster deserves its own note. Sixteen sources take no side on the reality question, and
they are not evasions; they are the field's connective tissue — the Yuan survey, the measure-
development papers building the singular-value and neural-network formulations, the methods that
identify a macro variable without ruling on its metaphysics. A field with a large neutral cluster is
one still building tools, which fits the picture the other two results draw: much apparatus, active
argument, little settled. For a borrowing program, the practical reading is that the toolmaking is
open. The measures are still being formulated, their coarse-graining problem is still being attacked,
and a well-posed application on a new class of system is a contribution the field has room for rather
than a solved problem it has moved past.

## Limitations

The three coders are language-model agents, not trained human raters. Their agreement is high, but
shared priors could inflate it relative to independent humans; the codes are auditable against the
corpus abstracts. The corpus is the screened union of two search backends and numbers sixty sources —
a sample, not a census, and a different backend or query set could shift the mix. Coders saw abstracts,
not full texts, which biases the empirical count downward if a paper's data work sits past its
abstract; the 93/7 split is too wide for that to overturn. The citation channel is partial because
publishers elide references, and the rate-limited harvest left the H3 matrix incomplete. Twenty-six of
sixty sources carry verified DOIs; the rest resolve by title, which does not affect the coding-based
verdicts.

## References

Method papers:

- Simsek, Z., Fox, B. C., & Heavey, C. (2023). Systematicity in Organizational Research Literature
  Reviews: A Framework and Assessment. *Organizational Research Methods*, 26(2), 292-321.
  doi:10.1177/10944281211008652.
- Simsek, Z., Heavey, C., Fox, B. C., & Yu, T. (2022). Compelling Questions in Research: Seeing What
  Everybody Has Seen and Thinking What Nobody Has Thought. *Journal of Management*.
  doi:10.1177/01492063211073068.

Corpus (60 sources): full entries with DOIs in `literature/references.bib`; the coded corpus with
abstracts is `literature/corpus.jsonl`. Sources named in the text:

- Hoel, E. P., Albantakis, L., & Tononi, G. (2013). Quantifying causal emergence shows that macro can
  beat micro. *PNAS*. doi:10.1073/pnas.1314922110.
- Hoel, E. P. (2017). When the Map Is Better Than the Territory. *Entropy*. doi:10.3390/e19050188.
- Hoel, E. P., Albantakis, L., Marshall, W., & Tononi, G. (2016). Can the macro beat the micro?
  Integrated information across spatiotemporal scales. *Neuroscience of Consciousness*.
  doi:10.1093/nc/niw012.
- Rosas, F. E., et al. (2020). Reconciling emergences: An information-theoretic approach to identify
  causal emergence in multivariate data. *PLoS Computational Biology*. doi:10.1371/journal.pcbi.1008289.
- Comolatti, R., & Hoel, E. (2022). Causal emergence is widespread across measures of causation.
  *arXiv* preprint.
- Yang, M., et al. (2023). Finding emergence in data by maximizing effective information. *National
  Science Review*.
- McSharry, D., et al. (2024). Learning diverse causally emergent representations from time series
  data. *NeurIPS*.
- Barnett, L., & Seth, A. K. (2021). Dynamical independence: Discovering emergent macroscopic processes
  in complex dynamical systems. *Physical Review E*.
- Dewhurst, J. E. (2021). Causal emergence from effective information: Neither causal nor emergent?
  *Thought*. doi:10.1002/tht3.489.
- Eberhardt, F., & Lee, L. (2022). Causal Emergence: When Distortions in a Map Obscure the Territory.
  *Philosophies*. doi:10.3390/philosophies7020030.
