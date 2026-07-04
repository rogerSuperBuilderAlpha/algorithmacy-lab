# One Object, Eighteen Names: Construct Proliferation in the Literature on the New Organizational Form

## Research Summary

Organization theory has spent three decades naming an alternative to the bureaucratic firm. This study
treats that naming as data. It codes 67 sources that theorize a form of organizing other than the
market or the hierarchy, and asks three questions a number can answer: how many distinct construct
labels the literature uses, whether it defines the form negatively or by a positive mechanism, and
whether the label-camps cite one another. Three independent coders reach almost-perfect agreement on
the construct label (Fleiss' k = 0.966). Eight closed-set labels are in active use, and a residual bin
resolves to roughly ten more, so the field gives one recurring object on the order of eighteen names.
A majority of sources (60%) define the form by a positive coordinating mechanism rather than by
contrast with hierarchy or market, reversing a common assumption about the literature. On the citation
graph the camps connect through a single meta-organization hub and are otherwise near-isolated: 7,082
external papers cite one camp and only two cite four. The pattern is a jangle fallacy at the scale of a
subfield, with a small integrating core.

## Introduction

The jangle fallacy is the error of treating one thing under two names as two things. Psychometricians
named it a century ago to explain why a field can accumulate constructs faster than it accumulates
knowledge. Organization theory is a candidate for the fallacy at scale. Since Powell's account of
network forms and the wave of post-bureaucratic writing that followed, the field has produced a steady
supply of labels for coordination that does not run through a chain of command or a price. Platform,
ecosystem, meta-organization, community, network organization, partial organization, open
collaboration, hybrid: each label carries its own review essays, its own special issues, its own
canonical citations. Whether these are distinct phenomena or one phenomenon seen from several angles is
rarely asked, because asking it requires stepping outside any single label's literature.

A construct proliferates without penalty when three conditions hold. The labels multiply. Each is
defined loosely enough to overlap its neighbors. And the camps do not read each other, so no one is
positioned to notice the redundancy. Those three conditions are measurable. The first is a count of
labels. The second is a coding of how each source establishes what its form is. The third is a
property of the citation graph. This study measures all three against a screened corpus, following the
systematicity pipeline of Simsek, Fox, and Heavey (2023) and drawing its questions from the
knowledge-weaving typology of Simsek, Heavey, Fox, and Yu (2022): a field's stylized facts, its
assumptions, and its omissions are the claims a review can test.

The question matters beyond bookkeeping. A subfield that cannot see its own redundancy keeps
rediscovering the same mechanism and calling the rediscovery novelty. It also raises the bar for any
genuinely new construct, which now has to be distinguished from a dozen incumbents rather than two.
Measuring the proliferation is the first step toward disciplining it.

## Framework

Three knowledge claims about this literature become three hypotheses.

The first is a stylized fact the field half-acknowledges: it uses many names. Rendered as a number, the
claim is that more than eight distinct construct labels are in active use for overlapping "new form"
phenomena (H1). The operationalization is a count of the labels coded across the corpus, drawn from a
closed set of nine plus an `other` category for anything outside it.

The second is a key assumption, usually stated as a compliment to the field's lineage: the new form is
"neither market nor hierarchy," defined against the two classical modes. If that framing dominates,
most sources should establish the form by contrast rather than by a positive coordinating mechanism
(H2). The operationalization codes each source's `differentia_mode` as `by_contrast` or
`positive_mechanism`, with a `parent_form` variable recording which baseline, if any, the source
invokes.

The third is a substantive omission: the camps proliferate in isolation. If so, the citation graph
built from the corpus should be block-diagonal by label — sources cite within their own camp and
ignore the others (H3). The operationalization uses the coded label as a cluster key and measures
within-label against cross-label citation links, plus an assembly-spanning count of how many camps any
external citing paper reaches.

The hypotheses were fixed and committed before any source was harvested or coded. A hypothesis the data
contradict is reported as a finding, not repaired.

## Method

**Corpus boundary.** A source is in scope if its title or abstract proposes, adopts, or theorizes an
alternative to the bureaucratic firm as a distinct organizational form. Product platforms used only as
a feature, firm-strategy papers that borrow "ecosystem" as a metaphor, and organizational-change papers
with no form construct are out. The corpus is English-language and indexed by the Scholar Gateway
semantic-search connector over Semantic Scholar, Scopus, PubMed, and ArXiv.

**Search.** Nine semantic queries paired "new organizational form" with each candidate label —
platform, meta-organization, ecosystem, partial organization, community, network organization, open
collaboration, post-bureaucratic and self-organizing forms, and hybrid organization. The union
returned 108 unique sources. Screening against the boundary rule dropped 41 (review essays, HR and
personality studies, policy analyses, product-development and firm-strategy papers, and other
off-boundary items, each logged with a reason in `literature/screened_out.jsonl`), leaving 67.

**Coding.** A fixed codebook assigns four categorical variables to each source from its title and
abstract: `label` (the construct the source foregrounds, closed set plus `other`), `differentia_mode`,
`parent_form`, and `claim_type` (the knowledge-weaving type of the central claim). Three independent
coders applied the codebook blind to one another. Reliability is Fleiss' k per variable, with a
majority-vote adjudicated dataset used for all downstream analysis.

**Citation graph.** For each of the 67 seeds, backward references and forward citers were harvested
from the Semantic Scholar Graph API. The adjudicated label is the cluster key. The
cluster-to-cluster matrix, the within-versus-cross link counts, and the assembly-spanning distribution
follow from the harvested edges.

## Results

**Reliability.** Agreement was high on all four variables and near-perfect on the one the headline
depends on. The label variable reached k = 0.966 (97.0% pairwise agreement); `parent_form` k = 0.863;
`differentia_mode` k = 0.791; `claim_type` k = 0.738. The count of construct labels is not an artifact
of a single reader.

**H1 — supported.** The corpus spreads across eight of the nine closed-set labels, with a large
residual tail.

| label | n |
|---|---|
| other | 14 |
| community | 9 |
| open_collaboration | 8 |
| hybrid | 8 |
| meta_organization | 7 |
| ecosystem | 7 |
| network_organization | 7 |
| platform | 5 |
| partial_organization | 2 |
| field_or_institution | 0 |

The `other` bin is not noise. Reading its 14 sources, it holds at least ten further named forms:
heterarchy, holacracy, adhocracy and the non-traditional organization, the fractal social
organization, the prosocial cooperative, the actor-oriented architecture of collaboration, the
corporate hub, the principle of distributed control, the alternative enterprise, and dual forms of
organizing. Combined with the eight populated closed-set labels, the literature gives one object —
coordination that is neither a price system nor a command hierarchy — on the order of eighteen distinct
construct labels. The prediction of more than eight is met with room to spare.

**H2 — challenged.** The field does not, in the majority, define the new form by what it is not. Forty
of 67 sources (60%) establish the form by a positive coordinating mechanism; 27 (40%) work by contrast
to hierarchy, market, or bureaucracy. The mechanisms are specific to each camp: modularity and design
rules for platforms and ecosystems, membership and the organization-of-organizations for
meta-organizations, combined institutional logics for hybrids, peer and commons governance for open
collaboration. The `parent_form` distribution corroborates the reversal. Thirty-two sources invoke no
explicit market-or-hierarchy baseline at all, against 19 that position against hierarchy, 12 against
market, and 4 against network. The "neither market nor hierarchy" slogan is present in the literature
but does not describe how most of it actually defines its object.

**H3 — qualified.** The label-to-label citation matrix, built on deduplicated seed pairs, is not
block-diagonal.

| | comm | eco | hyb | meta | net | open | other | part | plat |
|---|---|---|---|---|---|---|---|---|---|
| community | 1 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 |
| ecosystem | 0 | 2 | 0 | 3 | 0 | 0 | 0 | 0 | 1 |
| hybrid | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 |
| meta_organization | 1 | 3 | 0 | 10 | 0 | 0 | 7 | 0 | 4 |
| network_organization | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 |
| open_collaboration | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 |
| other | 1 | 0 | 0 | 7 | 1 | 0 | 3 | 0 | 2 |
| partial_organization | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| platform | 0 | 1 | 0 | 4 | 0 | 0 | 2 | 0 | 0 |

Within-camp links total 19 and cross-camp links total 20, so the isolation predicted by H3 does not
hold in aggregate. What holds instead is a hub-and-spoke structure. Meta-organization is the hub: 10
links inside its own camp and 15 out to ecosystem, platform, and the `other` tail. Platform reaches the
graph only through that hub, with no within-camp seed links of its own. The periphery is siloed as
predicted — community, network organization, open collaboration, partial organization, and hybrid each
show at most one off-diagonal link, and hybrid's two links are entirely internal.

The assembly-spanning test reads the wider literature the same way. Of the external papers that cite
any seed, 7,082 cite seeds from a single camp, 321 span two camps, 30 span three, and only 2 span four.
The redundancy across labels is almost never assembled by anyone downstream. The verdict is qualified
rather than challenged: proliferation-in-isolation is real for the periphery and for the reading
public, while a small meta-organization core integrates a handful of adjacent constructs.

**Claim types.** The knowledge-weaving coding sharpens the picture. Twenty-seven of 67 sources treat
their form as an assumption — a coherent object taken for granted to build other analysis on — and 21
assert it as a stylized fact. Fourteen frame the form as filling an omission, a call for the new label.
Only five sources code as critique. A subfield that produces eighteen construct labels and mounts five
critiques of them is one that adds names far faster than it examines them. The scarcity of critique is
the mechanism by which the proliferation persists: nothing in the literature's own output pushes back
on the supply of new terms.

## Discussion

The three measurements compose a coherent picture of how a subfield proliferates constructs. It
generates many labels (H1). It defines most of them by a positive mechanism, which makes each look like
a self-standing discovery rather than a variation on "not a hierarchy" (H2). And apart from one hub, it
does not cite across the labels, so the redundancy is invisible from inside any one of them (H3). The
positive-mechanism finding is the connective tissue. A field that defined every alternative form
negatively would at least share a common frame — the market-hierarchy contrast — that invites
comparison. Defining each form by its own mechanism removes even that shared reference point, and the
citation graph shows the consequence: camps that share almost no vocabulary and cite almost none of the
same work.

Meta-organization's position deserves attention. It is the one construct that links the others, sitting
between platform, ecosystem, and the heterodox tail. Kretschmer, Leiponen, Schilling, and Vasudeva
(2020) conceptualize platform ecosystems as meta-organizations; Gawer (2014) reads technological
platforms as evolving meta-organizations; Chen and colleagues (2021) treat the digital platform as a
distinct organizational form governed like a meta-organization. The construct works as a partial
lingua franca. Its centrality is also a caution: it shows that integration across these labels is
possible and has begun, which makes the isolation of the periphery a choice the field could reverse
rather than a fact about the phenomena.

The reversal on H2 also revises how the literature should be described to newcomers. The textbook
gloss — "new forms are neither market nor hierarchy" — captures a minority of the corpus and misreads
the rest. Most sources are past the contrast and into mechanism: they specify how their form
coordinates, in terms of modular interfaces, membership rules, or blended logics. That is progress at
the level of the individual construct and, at the same time, the engine of proliferation across
constructs, because a mechanism stated in a camp's private vocabulary reads as a discovery rather than
a restatement. The jangle fallacy here is not sloppiness. It is the byproduct of each camp doing
careful mechanism-level work in isolation from the others.

For a research program that would add another construct to this space, the measurements set the terms.
The label count specifies the work an entrant must do. Coining a new name adds an eighteenth to a
crowded list. The work worth doing is to state a coordinating mechanism precise enough to distinguish
the form from its incumbents and to cite across the camps those incumbents ignore. A new construct here
earns its place by what it integrates. The same discipline
applies to any measure that claims to grade a form's irreducibility across these camps: its worth is
the cross-label comparison it makes possible, which the citation graph shows the field has not yet
made for itself.

## Limitations

The coders are LLM agents applying a fixed codebook, not trained human raters. Agreement among the
agent passes is high, and near-perfect on the label variable, but it is not a substitute for
independent human coding, and the same codebook read by human raters could shift the boundary cases.
The corpus is bounded by one semantic-search connector and by English-language indexing; a different
seed set would change the label mix, though the fact of proliferation is robust to reasonable changes
in the search. Semantic Scholar elides outbound references for many publishers, so the seed-to-seed
matrix leans on the inbound-citer channel and undercounts links, which biases the within-versus-cross
comparison toward whichever camps happen to have complete citer records. Three seeds resolved to error
stubs, and the two partial-organization seeds matched no links, so that camp's apparent isolation is
partly a coverage artifact rather than a finding. Finally, the label count depends on the codebook's
closed set and on a judgment about the contents of the `other` tail; a coarser codebook would report
fewer camps and a finer one more. The direction of the result does not depend on that choice, but the
exact figure of eighteen does.

## References

Chen, L., Tong, T. W., Tang, S., & Han, N. (2021). Governance and design of digital platforms: A
review and future research directions on a meta-organization. *Journal of Management*, 48(1),
147-184. https://doi.org/10.1177/01492063211045023

Cennamo, C., Ozalp, H., & Kretschmer, T. (2019). Generativity tension and value creation in platform
ecosystems. *Organization Science*, 30(6), 1121-1394. https://doi.org/10.1287/orsc.2018.1270

Ciborra, C. U. (1996). The platform organization: Recombining strategies, structures, and surprises.
*Organization Science*, 7(2), 103-118. https://doi.org/10.1287/orsc.7.2.103

Gawer, A. (2014). Bridging differing perspectives on technological platforms: Toward an integrative
framework. *Research Policy*, 43(7), 1239-1249. https://doi.org/10.1016/j.respol.2014.03.006

Gawer, A. (2021). Digital platforms and ecosystems: Remarks on the dominant organizational forms of
the digital age. *Innovation: Organization & Management*, 24(1), 110-124.
https://doi.org/10.1080/14479338.2021.1965888

Kretschmer, T., Leiponen, A., Schilling, M., & Vasudeva, G. (2020). Platform ecosystems as
meta-organizations: Implications for platform strategies. *Strategic Management Journal*, 43(3),
405-424. https://doi.org/10.1002/smj.3250

McIntyre, D., Srinivasan, A., Afuah, A., Gawer, A., & Kretschmer, T. (2020). Multi-sided platforms as
new organizational forms. *Academy of Management Perspectives*, 35(4), 566-583.
https://doi.org/10.5465/amp.2018.0018

Simsek, Z., Fox, B. C., & Heavey, C. (2023). Systematicity in organizational research literature
reviews: A framework and assessment. *Organizational Research Methods*, 26(2), 292-321.
https://doi.org/10.1177/10944281211008652

Simsek, Z., Heavey, C., Fox, B. C., & Yu, T. (2022). Compelling questions in research: Seeing what
everybody has seen and thinking what nobody has thought. *Journal of Management*.
https://doi.org/10.1177/01492063211073068

The full 67-source corpus, with DOIs, is in `literature/corpus.jsonl` and `literature/references.bib`.
