# Integrated Information Beyond Consciousness: A Quantitative Archival Review of a Nascent, Method-Bound Literature

## Research Summary

Integrated information theory (IIT) and its measure Φ were built to quantify consciousness in brains.
A scattered body of work now carries the same measure to other systems: fish schools, work groups,
inter-organizational networks, evolved robots, and abstract dynamical systems. This review treats that
body of work as data. It bounds the literature, harvests its citation graph, and codes every source
three times to test four pre-registered claims about it. The corpus is 40 sources, 92% of them
published in 2015 or later, and it does not touch organizational coordination theory: 8% of sources
engage that theory and the citation graph shows zero links between the corpus and a six-work
coordination canon. Φ is computed on real data in 15% of sources, and almost all of those computations
are on animal collectives rather than organizations. The one hypothesis the data reject is the
expectation that substrates form isolated silos; instead the substrate clusters cite across their
boundaries more than within them, bound together by shared IIT machinery. Intercoder reliability is in
the "almost perfect" band on all four variables (Fleiss' κ from 0.87 to 1.00). The review is
reproducible end to end and states the limitation that its coders are language-model agents.

**Keywords:** integrated information theory, systematic review, intercoder reliability, bibliometrics,
coordination, research methods

## Introduction

Organization theory imports formal models from other fields. Population biology gave it organizational
ecology; microeconomics gave it transaction-cost economics; network mathematics gave it a language for
interorganizational structure. A more recent candidate for import is integrated information theory,
developed in neuroscience to measure the degree to which a system's parts specify a joint state that
none of the parts specifies alone. Its measure, Φ, is a single number that grows with a system's
irreducibility. A research program that read organizational coordination as a form of irreducible
integration would find IIT an obvious tool.

Before a field imports a construct, it should know the shape of the literature it is joining. Is
applying Φ beyond the brain an established science with mature empirical methods, or a young and
speculative activity? Does that literature already talk to organization theory, or would the bridge be
new? Is Φ computed on real systems, or invoked as an analogy? Do its various applications form one
conversation or several disconnected ones? These are not rhetorical questions. Each has an answer that
a coded corpus and a citation graph can supply, and the answers bear directly on whether importing IIT
into organizational research fills a gap or enters a crowded room.

This review answers them. It is an evaluative review in the systematicity typology (Simsek, Fox, &
Heavey, 2023): it assesses the developmental status of a body of knowledge claims rather than
synthesizing findings into a new theory. The unit of analysis is the source, and the method treats the
literature the way that framework's authors treated a sample of review articles — as a dataset to be
coded and measured. Four claims about the literature were fixed in a pre-registered hypotheses file
committed before any source was harvested or coded, following the review's two governing rules: fix the
hypotheses before computing, and measure rather than assert.

## Framework

The review joins two methodological sources. From systematicity (Simsek, Fox, & Heavey, 2023) it takes
its pipeline: envision the orienting question, explicate the corpus boundary, execute a search with an
explicit stopping rule, encode with a fixed codebook and independent coders, evaluate against the
claims, and exposit the result with a reliability figure attached. From knowledge weaving (Simsek,
Heavey, Fox, & Yu, 2022) it takes its source of hypotheses: a literature's knowledge claims sort into
stylized facts, key assumptions, enduring critiques, and substantive omissions, and each type that a
number can check becomes a testable hypothesis.

Four claims follow.

H1 (stylized fact): applying IIT beyond neural substrates is nascent, not established. Operationalized
as corpus size and year distribution. Supported by a corpus in the tens concentrated after 2015;
challenged by a corpus in the hundreds or an even spread reaching well before 2010.

H2 (substantive omission): the IIT-beyond-consciousness literature and organizational coordination
theory do not cite each other. Operationalized as cross-citation between the corpus and a fixed
coordination canon, plus a coded measure of whether each source engages organization theory. Supported
by near-zero cross-citation; challenged by a substantial share engaging the canon.

H3 (key assumption): that Φ indexes collective or organizational integration is taken as motivating
rather than demonstrated. Operationalized as the share of sources that compute Φ on real social or
organizational data. Supported if empirical work is a small minority; challenged if it is a plurality.

H4 (enduring critique): applications fragment by substrate with little cross-talk. Operationalized as
the cluster-to-cluster citation matrix over substrate clusters. Supported by a block-diagonal matrix;
challenged by a well-connected one.

## Method

**Corpus boundary.** A source is in-boundary if its title or abstract applies, extends, or discusses
applying IIT or Φ to a system other than an individual brain — organizations, teams, firms, markets,
economies, social networks, animal groups or swarms, or engineered multi-agent systems — or discusses
the scope of such application. Pure clinical or brain-consciousness IIT is out. The canonical
consciousness formulations (IIT 3.0, IIT 4.0, and the "physical substrate" statement) are out as
core-brain theory. Unrelated "integrated information systems" in enterprise IT are out. English
language, indexed in Semantic Scholar, 2004 to present; preprints are admitted and flagged, because the
topic is young and partly on preprint servers.

**Search.** Candidates were gathered with two academic connectors — a semantic scholarly-search gateway
and a peer-reviewed-literature search engine — run over natural-language queries crossing IIT and Φ with
non-brain substrates: organizations and teams, animal collectives and swarms, economies and markets,
collective intelligence and group interaction, and the scope-of-IIT and panpsychism debates. The union
was deduplicated and screened by hand against the boundary rule. The connectors returned many
out-of-boundary hits — clinical and brain-only IIT, the canonical consciousness formulations,
enterprise "integrated information systems," and complex-systems or finance papers that use the word
"integration" without any IIT content — which were logged and dropped. Searching stopped when new query
framings returned no new in-boundary sources. The economy-and-market queries are illustrative: they
returned financial-integration and complex-systems papers, none of which computes or invokes Φ, so no
economy substrate cluster forms in the corpus.

**Coding.** The codebook fixes four categorical variables. Substrate records the system Φ is applied to
(neural, swarm, social_org, artificial, philosophical, or na). Evidence records how the source treats Φ
(conceptual argument, formal model on a toy or simulated system, empirical computation on real data, or
na). Claim_type records the knowledge-weaving type of the central claim (stylized_fact, assumption,
critique, omission, or na). Cites_org_theory records whether the source engages coordination or
organization theory. Three coders applied the codebook independently and blind to one another, each
coding from the title and abstract, none consulting another's output. The coders are language-model
agents run in parallel on the same codebook — a design choice whose consequences the Limitations section
states.

**Analysis.** Reliability is Fleiss' κ per variable with mean pairwise agreement, and a majority-vote
adjudicated dataset. H1 reads the size and year distribution off the adjudicated corpus. H3 reads the
evidence distribution. H2 reads the coded engagement measure and, on the harvested citation graph, the
cross-citation between the corpus and the coordination canon. H4 reads the cluster-to-cluster citation
matrix over substrate clusters. The graph was harvested by resolving each seed to a Semantic Scholar
paperId and pulling its inbound citers and outbound references; the coordination canon (Thompson 1967,
Williamson, Powell 1990, Galbraith 1973, Malone & Crowston 1994, Puranam et al. 2014) was harvested as
an additional seed set. The pipeline is reproducible from `build_corpus.py`, `lib/harvest.py`,
`lib/reliability.py`, and `run.py`.

## Results

**Reliability.** Agreement is high on all four variables (Table 1). Substrate and evidence drew
identical labels from all three coders on all 40 sources. Claim_type and cites_org_theory each carried a
few split calls but remain in the "almost perfect" band by the Landis and Koch thresholds.

Table 1. Intercoder reliability (three coders, 40 sources).

| Variable | Fleiss' κ | Mean pairwise agreement | Interpretation |
|---|---|---|---|
| substrate | 1.000 | 100.0% | almost perfect |
| evidence | 1.000 | 100.0% | almost perfect |
| claim_type | 0.874 | 93.3% | almost perfect |
| cites_org_theory | 0.866 | 98.3% | almost perfect |

**H1.** The corpus is 40 sources spanning 2008 to 2026, median year 2022. Thirty-seven (92%) date from
2015 or later and 25 fall in 2020–2024. The three earliest are the theory's formal groundwork. The
literature is nascent and recent. H1 is supported.

**H2.** Three of 40 sources (8%) engage organization or coordination theory; 37 do not. On the citation
graph the coordination canon draws zero links to or from the corpus (Table 2, final row and column).
Three of the six canon anchors resolved on Semantic Scholar and carry 2,535 harvested citers between
them, Malone and Crowston's coordination theory contributing 1,000; none of those citers is a corpus
source and no corpus source cites the canon. Both measures agree. H2 is supported.

**H3.** Evidence splits into conceptual (19; 48%), formal model (15; 38%), and empirical (6; 15%).
Empirical computation on real data is a small minority and conceptual argument is the largest single
category, as predicted, so H3 is supported. The qualification matters for the importing program: of the
six empirical sources, four are the Niizato group's fish-school studies computing IIT 3.0 on real
animal-collective trajectories, and the remaining two apply Φ or an integration proxy to real human
groups and to real interorganizational networks. None computes Φ on firm-, market-, or team-level
organizational data. Φ has been measured on collectives, but almost not at all on organizations.

**H4.** Coders sort the corpus into four substrate clusters: artificial or abstract systems (16),
philosophical or scope work (15), animal-collective "swarm" systems (5), and social-organizational
systems (4). No economy cluster forms. The topics fragment by substrate, but the citation matrix is not
block-diagonal (Table 2). Within-cluster seed-to-seed links total 24; cross-cluster links total 27. The
artificial and philosophical clusters are hubs, linked 11 times to each other and, for artificial, 7
times to swarm. The substrates cite across their boundaries more than within them because they share
the same Φ measures and tooling. Assembly from the outside, by contrast, is thin: of 3,932 external
papers citing the corpus, 3,837 touch a single substrate cluster, 80 span two, 13 span three, and 2
span all four. Insiders cross-cite; outsiders have not unified the substrates. The prediction of
isolated silos is rejected. H4 is challenged.

Table 2. Cluster-to-cluster citation links (undirected, deduplicated seed pairs). Rows and columns are
substrate clusters plus the coordination canon.

| | artificial | canon | philosophical | social_org | swarm |
|---|---|---|---|---|---|
| artificial | 14 | 0 | 11 | 2 | 7 |
| canon | 0 | 0 | 0 | 0 | 0 |
| philosophical | 11 | 0 | 8 | 2 | 2 |
| social_org | 2 | 0 | 2 | 1 | 3 |
| swarm | 7 | 0 | 2 | 3 | 1 |

**An unhypothesized split.** Claim_type divides almost evenly between sources asserting that Φ indexes
integration in a non-brain substrate (stylized_fact, 20) and sources disputing or bounding that
application (critique, 19), with one assumption. Half of the literature that carries IIT beyond the
brain is skeptical of the carry.

## Discussion

The four results give a coherent picture. Applying Φ beyond the brain is a young activity of a few dozen
papers (H1), disconnected from organizational coordination theory (H2), rarely grounded in real
organizational data (H3), and — against expectation — internally connected across its application
targets rather than fragmented (H4). For a research program that reads organizational coordination
through IIT, the first three results describe an open gap and the fourth describes the kind of
literature that gap sits in.

The gap is real on the terms that matter to organization theory. No corpus source computes Φ on
firm-, team-, or market-level data, and the coordination canon and the IIT corpus do not cite each
other in either direction. A program that computes exact Φ on organizational coordination structures is
not entering a crowded field; it is building a bridge that the citation graph shows to be unbuilt. That
is the affirmative reading of H2 and H3 together.

The fourth result refines rather than deflates that reading. The beyond-consciousness literature is not
four disconnected pockets that a newcomer would have to unify; it is one method-bound conversation with
several application targets. A fish-school study, an animat study, and a social-ontology paper cite the
same formal Φ measures and the same tooling. An organizational application would join that conversation
through its method, and it would inherit the conversation's live dispute — the near-even split between
sources that assert Φ indexes integration and sources that bound or reject the application. The
panpsychism debate, the strong-versus-weak-IIT distinction, and the argument that Φ has never been
computed on a real physical system are all inside the literature an importer joins. Naming that dispute
is part of importing the tool honestly; it does not diminish the tool's value as a principled lens on
irreducibility.

The review also demonstrates a method. Treating a target literature as a coded dataset, fixing the
hypotheses before computing, and reporting a reliability figure turns claims about a field — "it is
nascent," "no one has connected these," "it is all analogy" — into measured findings with verdicts,
challenges included. The rejected H4 is worth as much as the three supported hypotheses: it corrects a
plausible prior about how the literature is organized.

## Limitations

The coders are language-model agents applying a fixed codebook, where a conventional review would use trained human raters. The high κ shows
consistent application of the codebook; it does not certify that the codebook captures the constructs a
domain expert would draw, and claim_type — the variable with the most interpretive load — is where a
human panel would most likely diverge. Forty sources is a small corpus, so the thin clusters
(social_org = 4, swarm = 5) would move under a few reclassifications, and the decision to exclude the
canonical IIT formulations as core-brain theory shapes the size of the philosophical cluster. Search ran
through two academic connectors and hand screening, so recall is bounded by what those connectors
surface. Semantic Scholar returns citers far more completely than references, and three of six
canon anchors and several preprint seeds did not resolve; the graph tests therefore lean on the
inbound-citer channel. The zero canon cross-citation is robust to this, holding on the three anchors
that resolved, including coordination theory itself, but the cross-cluster link counts are a floor
rather than a full census. The pipeline and its inputs are committed, so each of these bounds is
auditable and each number is reproducible.

## References

Balduzzi, D., & Tononi, G. (2008). Integrated information in discrete dynamical systems: Motivation and
theoretical framework. *PLoS Computational Biology, 4*(6), e1000091.

Christensen, B. (2024). Beyond individualism and holism: Integrated information theory as formal
framework for the gradation of social structure. *Erkenntnis.*

Edlund, J. A., Chaumont, N., Hintze, A., Koch, C., Tononi, G., & Adami, C. (2011). Integrated
information increases with fitness in the evolution of animats. *PLoS Computational Biology, 7*(10),
e1002236.

Engel, D., & Malone, T. W. (2018). Integrated information as a metric for group interaction. *PLoS ONE,
13*(10), e0205335.

Lajaunie, C., et al. (2019). Organizational consciousness versus artificial consciousness. In *Law,
Governance and Technology Series.*

Mediano, P. A. M., Rosas, F. E., Carhart-Harris, R. L., Seth, A. K., & Barrett, A. B. (2021). Towards an
extended taxonomy of information dynamics via integrated information decomposition. *arXiv:2109.13186.*

Niizato, T., Sakamoto, K., Mototake, Y., Murakami, H., Gunji, Y.-P., Tomaru, T., & Kojima, T. (2020).
Finding continuity and discontinuity in fish schools via integrated information theory. *PLoS ONE,
15*(2), e0229573.

Simsek, Z., Fox, B. C., & Heavey, C. (2023). Systematicity in organizational research literature
reviews: A framework and assessment. *Organizational Research Methods, 26*(2), 292–321.

Simsek, Z., Heavey, C., Fox, B. C., & Yu, T. (2022). Compelling questions in research: Seeing what
everybody has seen and thinking what nobody has thought. *Journal of Management.*

Tononi, G., & Koch, C. (2015). Consciousness: Here, there and everywhere? *Philosophical Transactions of
the Royal Society B, 370*(1668), 20140167.

*The full 40-source corpus with DOIs is in `literature/references.bib`; the coded data, reliability
output, and citation-graph results are in `results/`.*
