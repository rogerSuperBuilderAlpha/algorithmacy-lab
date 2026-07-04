# Many measures of integration, little validation: a coded review of the integrated-information measure literature

## Research summary

Integrated information theory placed one number, Phi, at the center of a claim about consciousness, and
the difficulty of computing it launched a search for alternatives. That search has produced not one
measure but a plurality of them. This review treats the plurality as a dataset. It assembles 68 sources
whose central object is a measure of integrated information, integration, complexity, or synergy, and
codes each on two variables: which measure family it belongs to, and how it establishes that the
measure captures integration. Three independent coders agree almost perfectly (Fleiss' kappa 0.905 to
0.985). Six measure families are each populated by at least three sources and the largest holds under a
third of the corpus, so the literature has not converged. Only 13 of 68 sources (19%) validate their
measure against a ground truth such as exact Phi or a known generative structure; the other 81% rest on
axioms or on a demonstration using a system the author selected. The review is the literature-level
image of the lab's foundations program, which asks on computable systems what tracks exact Phi. The
field proposes many candidate numbers and rarely checks them against the quantity they approximate.

## Introduction

A measure that cannot be computed invites substitutes. Integrated information theory (IIT) defines Phi
as the information a system generates as a whole beyond the information its parts generate
independently, and identifies it with the quantity of consciousness (Tononi et al., 2003; Balduzzi &
Tononi, 2008). Computing Phi exactly requires enumerating a system's partitions and its cause-effect
structure, which becomes intractable past a dozen or so elements. The response was a wave of proposals:
tractable approximations for time-series data, decoding-based measures, geometric measures,
compression-based measures, and measures built to satisfy a chosen set of axioms. Alongside them grew
adjacent literatures that quantify related quantities — the balance of integration and segregation in a
neural system, the synergy and redundancy among interacting variables, the strength of causation at a
macroscale — each with its own measure and its own community.

The situation raises two empirical questions about the literature itself. The first is about
proliferation. How many distinct families of measure does the field actually maintain, and does any one
of them command the field, or does the plurality persist? A field with one dominant measure and a few
challengers differs from a field that sustains half a dozen families in parallel; the count is
diagnostic. The second question is about validation. When an author proposes a measure of integration,
what work does the paper do to show that the number means what it is claimed to mean? A measure can be
justified in three broad ways. It can be derived to satisfy axioms or desiderata and demonstrated on an
example — internal justification. It can be checked against a ground truth: scored against exact Phi, a
reference measure treated as a criterion, a known generative structure, or an external empirical
target. Or it can be proposed and argued for with no validation at all. The mix of these across the
literature is a fact about the field's evidentiary standards, and it can be measured.

Both questions matter to a research program that uses exact Phi as an instrument. The lab's foundations
arm establishes exact IIT-4.0 Phi as a ground-truth measure on small systems and asks which cheap
signals track it, finding that no single cheap number is integrated information. This review asks the
companion question of the published record rather than of simulated systems. If the measures the field
proposes are many and mostly unvalidated against a ground truth, then the foundations arm is supplying
something the literature is short of — a systematic check of proposed measures against the quantity
they claim to approximate. This paper measures whether that characterization of the literature holds.

## Framework

The review follows the systematicity pipeline for treating a body of scholarship as data (Simsek, Fox,
& Heavey, 2023) and draws its questions from the knowledge-weaving typology of a field's claims
(Simsek, Heavey, Fox, & Yu, 2022). Three hypotheses, registered before the corpus was built, render the
two questions falsifiable.

H1 states a stylized fact: the literature proposes many distinct measure families and has not converged
on one. Operationally, at least five families each attract three or more sources and no family holds a
majority.

H2 states a key assumption the field is charged with: that a proposed measure captures integration is
taken as motivating rather than demonstrated. Operationally, the share of sources that validate against
a ground truth is a minority, and internal-or-none justification dominates.

H3 states an enduring critique: the measure families develop in relative isolation and cite within
themselves more than across. Operationally, a cluster-to-cluster citation matrix over the family
clusters shows more within-family than cross-family links.

The knowledge-weaving frame names H1 a stylized fact to test, H2 an assumption to audit, and H3 a
fragmentation critique to check on the citation graph. The systematicity frame supplies the discipline
that makes each answerable: an explicit corpus boundary, three independent coders, and a reported
reliability coefficient.

## Method

**Corpus boundary.** A source is in scope when its central object is a quantitative measure of
integrated information, integration, complexity, or synergy — its definition, computation,
approximation, comparison, or critique. Exact IIT Phi, practical Phi proxies, causal emergence and
effective information, integrated information decomposition and partial information decomposition,
total correlation and multi-information, and neural (Tononi-Sporns-Edelman) complexity are all in
scope. A paper that uses a fixed off-the-shelf measure to study a substrate, without engaging the
measure itself, is out of scope, as are pure statistical dependence coefficients, quantum-correlation
measures, and machine-learning representation objectives. The corpus is English-language and indexed by
the academic semantic-search connectors, spanning 1994 (the Tononi-Sporns-Edelman complexity measure)
to 2026, and includes preprints, since much of this work appears on arXiv.

**Search.** The corpus was assembled by semantic search over the measure vocabulary — measures of
integrated information, practical approximations to Phi, integrated information decomposition and
synergy, causal emergence measures, neural complexity and integration-segregation, whole-minus-parts
and total correlation — via the Scholar Gateway and Consensus connectors, which draw on Semantic
Scholar, PubMed, Scopus, and arXiv. The union was deduplicated and screened against the boundary rule.
Off-boundary hits returned by the connectors (statistical-methods papers, domain applications, quantum
and machine-learning uses) were dropped. The screened corpus holds 68 sources.

**Coding.** The codebook fixes three categorical variables. `measure_family` sorts a source into one of
six named families or `other`/`na`. `validation` grades the source `ground_truth`, `internal`, or
`none/conceptual`. `substrate` records whether the measure is demonstrated on a neural, simulated,
abstract, or other system. Three coders, realized as independent LLM agents blind to one another,
applied the codebook to the title and abstract of each source and wrote to separate files. Fleiss'
kappa and a majority-vote adjudicated dataset were computed with the arm's reliability tool. Coding the
source's own argument from its abstract, rather than the reviewer's expectation, is what keeps the
grade honest; the three passes and their kappa are what answer the single-coder objection.

**Analysis.** H1 and H2 are read from the adjudicated dataset: the family distribution and the
validation distribution. H3 requires the citation graph, harvested by resolving each seed on Semantic
Scholar and pulling its backward references and forward citers, then forming the family-to-family
citation matrix.

## Results

**Reliability.** The three coders agreed almost perfectly. Fleiss' kappa was 0.963 for
`measure_family`, 0.905 for `validation`, and 0.985 for `substrate`, with pairwise agreement above 96%
on all three. The family assignments and validation grades below are not one reader's judgment.

**H1 — the plurality persists.** Six measure families each carry at least three sources, and the largest
holds 31% of the corpus (Table 1). Integrated information decomposition and synergy is the most
populated family, followed by causal emergence, then the practical Phi proxies; exact IIT Phi itself is
a tenth of the corpus. No family approaches a majority. The literature sustains a standing plurality of
measures rather than converging on one, and H1 is supported.

**Table 1. Measure families (N = 68).**

| measure family | sources | share |
|---|---|---|
| integrated information decomposition / synergy | 21 | 31% |
| causal emergence / effective information | 16 | 24% |
| practical Phi proxy | 10 | 15% |
| total correlation / multi-information | 8 | 12% |
| exact IIT Phi | 7 | 10% |
| geometric / neural (TSE) complexity | 6 | 9% |

**H2 — validation is mostly internal.** Thirteen of 68 sources (19%) validate their measure against a
ground truth (Table 2). The remaining 81% justify the measure internally — by axioms, desiderata, or a
demonstration on a self-chosen system — or propose it without validation. Internal justification alone
accounts for 49 sources (72%). H2 is supported: the field mostly assumes that its measures capture
integration rather than showing it against an external criterion.

The families divide sharply on this. Practical proxies have the highest ground-truth rate, four of ten,
which follows from what a proxy is for: a measure built to approximate exact Phi can be scored against
exact Phi, and several proxy papers do exactly that. Total correlation measures also validate against
analytical or benchmark criteria at a comparable rate. The decomposition and synergy family sits at the
other end — nineteen of its twenty-one sources are internal, their measures fixed by lattice axioms and
demonstrated on canonical examples rather than scored against a known quantity. Causal emergence
concentrates in internal and conceptual grades: its measures are typically shown on toy Markov systems
where a macroscale beats a microscale, which demonstrates the phenomenon the measure was built to
detect rather than validating the measure against an independent target.

**Table 2. Validation by family.**

| measure family | ground_truth | internal | none/conceptual | total |
|---|---|---|---|---|
| exact IIT Phi | 1 | 4 | 2 | 7 |
| practical Phi proxy | 4 | 6 | 0 | 10 |
| causal emergence | 1 | 11 | 4 | 16 |
| iid / synergy | 2 | 19 | 0 | 21 |
| total correlation | 4 | 4 | 0 | 8 |
| geometric / TSE complexity | 1 | 5 | 0 | 6 |
| total | 13 | 49 | 6 | 68 |

The substrate coding adds context. Half the corpus is demonstrated on abstract or formal systems (34 of
68), a quarter on simulated systems (18), and a minority on neural data (8). The measures are, for the
most part, exhibited on systems chosen to display them, which is consistent with the low ground-truth
rate: a self-chosen demonstration substrate is the vehicle of internal validation.

**H3 — fragmentation (partial).** The citation harvest ran against a Semantic Scholar rate limit shared
with several concurrent reviews and did not complete within the run window. The family-to-family
citation matrix is therefore not reported. H3 is left partial; the harvest is checkpointed and the
matrix completes on a restart. Two features of the corpus bear on the eventual result without settling
it. The families are of different ages — neural complexity dates to 1994, exact Phi to 2003-2008,
causal emergence and the decomposition family largely to the 2010s — which gives older families more
time to be cited across. And several sources already sit on family boundaries in a way that predicts
some cross-citation: the integrated information decomposition family was built by fusing partial
information decomposition with integrated information, and one causal-emergence result argues that
emergence appears across a dozen independently developed causal measures. Whether that cross-talk is
enough to overturn a within-family tendency is exactly what the matrix will decide.

## Discussion

The literature on measuring integration is plural and lightly validated. Six families coexist with no
convergence, and four sources in five establish their measure by axiom or by a demonstration of the
author's choosing rather than by a check against a ground truth. Neither finding is a charge of bad
faith. A field early in its life proposes measures faster than it validates them, and internal
justification — proving a measure satisfies the properties integration ought to have — is a legitimate
and necessary mode of work. The finding is about where the literature's effort has gone. It has gone
into constructing measures and establishing their formal credentials, and much less into scoring them
against the quantity they are meant to capture.

The division among families sharpens the point. The practical-proxy family, whose reason for existing
is to approximate exact Phi, is the family most often checked against exact Phi. The decomposition and
synergy family, whose measures are defined by which axioms they satisfy on a redundancy lattice, is
almost never checked against an external quantity, because its standard of success is internal by
construction. These are different research cultures sharing a subject. A reader who wants to know
whether a given measure tracks integration will find the question answered for some families and left
open, by design, for others.

This is the literature-level counterpart of the lab's foundations program. That program takes exact
IIT-4.0 Phi as a ground-truth instrument on systems small enough to compute it, and asks which cheap
measures track it — a ground-truth validation carried out by computation. The review shows that this is
the validation the literature mostly does not perform. The proxies that have been scored against exact
Phi are a minority even within their own family, and the other families are scored against exact Phi
almost not at all. The foundations arm is therefore not duplicating an established practice; it is
supplying one that the coded record shows to be scarce. That is the contribution the review points to:
not that the many measures are wrong, but that whether they track integration is, for most of them, an
open empirical question that a ground-truth study can close.

## Limitations

The coders are LLM agents applying a fixed codebook, not trained human raters. Agreement among the
three passes is almost perfect, but high agreement among agent coders is not a substitute for
independent human coding, and the reliability figure should be read with that in mind. The corpus is
bounded by the semantic-search connectors' coverage and by English-language indexing, and it is
deliberately measure-centric: application papers that use a fixed measure without engaging it are out
of boundary, so the corpus describes how measures are proposed and validated, not how widely they are
used. The `validation` grade is read from the abstract, so a paper that scores its measure against a
ground truth in its body but does not say so in its abstract is graded down; this biases the
ground-truth rate downward and makes 19% a floor rather than a point estimate. Finally, H3 is partial.
The fragmentation hypothesis is neither supported nor challenged here, because the citation matrix was
not computed within the run window; the reproduce command completes it.

## References

Balduzzi, D., & Tononi, G. (2008). Integrated information in discrete dynamical systems: Motivation and
theoretical framework. *PLoS Computational Biology, 4*(6), e1000091.

Barrett, A. B., & Seth, A. K. (2011). Practical measures of integrated information for time-series data.
*PLoS Computational Biology, 7*(1), e1001052.

Hoel, E. P., Albantakis, L., & Tononi, G. (2013). Quantifying causal emergence shows that macro can beat
micro. *Proceedings of the National Academy of Sciences, 110*(49), 19790-19795.

Mediano, P. A. M., Seth, A. K., & Barrett, A. B. (2019). Measuring integrated information: Comparison of
candidate measures in theory and simulation. *Entropy, 21*(1), 17.

Oizumi, M., Amari, S., Yanagawa, T., Fujii, N., & Tsuchiya, N. (2016). Measuring integrated information
from the decoding perspective. *PLoS Computational Biology, 12*(1), e1004654.

Simsek, Z., Fox, B. C., & Heavey, C. (2023). Systematicity in organizational research literature
reviews: A framework and assessment. *Organizational Research Methods, 26*(2), 292-321.

Simsek, Z., Heavey, C., Fox, B. C., & Yu, T. (2022). Compelling questions in research: Seeing what
everybody has seen and thinking what nobody has thought. *Journal of Management*.

Tegmark, M. (2016). Improved measures of integrated information. *PLoS Computational Biology, 12*(11),
e1005123.

Tononi, G., & Sporns, O. (2003). Measuring information integration. *BMC Neuroscience, 4*, 31.

Tononi, G., Sporns, O., & Edelman, G. M. (1994). A measure for brain complexity: Relating functional
segregation and integration in the nervous system. *Proceedings of the National Academy of Sciences,
91*(11), 5033-5037.

Williams, P. L., & Beer, R. D. (2010). Nonnegative decomposition of multivariate information. *arXiv
preprint arXiv:1004.2515*.

*The full 68-source corpus, the coder files, the adjudicated dataset, and the reproduce commands are in
the review directory. The complete reference list is in `literature/references.bib`.*
