# Findings — integrated information beyond consciousness

The corpus holds 40 in-boundary sources: work that applies, extends, or discusses applying integrated
information theory (IIT / Φ) to a system other than an individual brain, or that argues about the scope
of such application. Three agents coded every source from its title and abstract, blind to one another.
Intercoder reliability is high on all four variables, so the distributions below rest on agreement, not
on one reader's judgment.

## Reliability

| Variable | Fleiss' κ | Mean pairwise agreement | Landis & Koch |
|---|---|---|---|
| substrate | 1.000 | 100.0% | almost perfect |
| evidence | 1.000 | 100.0% | almost perfect |
| claim_type | 0.874 | 93.3% | almost perfect |
| cites_org_theory | 0.866 | 98.3% | almost perfect |

Substrate and evidence drew identical labels from all three coders on all 40 sources. The two lower
figures come from a handful of split calls on claim_type (whether a scope paper asserts the mapping or
disputes it) and on whether a source engages organization theory. All four sit in the "almost perfect"
band. Adjudication was majority vote; the frozen dataset is `results/frozen.json`.

## H1 — A corpus of 40, concentrated after 2015: supported

The boundary admits 40 sources spanning 2008 to 2026, with a median year of 2022. Thirty-seven of the
40 (92%) appeared in 2015 or later; 25 of them fall in 2020–2024 alone. The three pre-2015 sources are
the theory's own formal groundwork (Balduzzi & Tononi 2008 on Φ in discrete dynamical systems; Edlund
et al. 2011 on Φ in evolved animats). Applying IIT beyond the brain is a recent activity carried by
tens of papers, not an established literature of hundreds. The prediction holds.

## H2 — No bridge to coordination theory: supported

Two independent measures agree. In the coded data, 3 of 40 sources (8%) engage organization or
coordination theory at all; the other 37 do not. On the harvested citation graph, the six
coordination-canon anchors (Thompson 1967, Williamson, Powell 1990, Galbraith 1973, Malone & Crowston
1994, Puranam et al. 2014) draw zero citation links to or from the IIT corpus. Three of the six
canon anchors resolved on Semantic Scholar and together carry 2,535 harvested citers — Malone &
Crowston's coordination theory alone accounts for 1,000 — and not one of those citers is a corpus
source, nor does any corpus source cite them. The literature that applies Φ beyond the brain and the
literature on organizational coordination do not read each other.

## H3 — Rarely computed on real social data: supported, with a qualification

Coders split the 40 sources into conceptual (19, 48%), formal model (15, 38%), and empirical (6, 15%).
Empirical means Φ, or a declared proxy, computed on real behavioral, social, or organizational data.
The empirical share is a small minority and conceptual argument is the largest single category, as
predicted. The qualification: empirical is not zero. Four of the six empirical sources are the Niizato
group's fish-school studies, which compute IIT 3.0 on real *Plecoglossus altivelis* trajectories; the
other two apply Φ or an integration proxy to real human groups (Engel et al.'s work groups, Wikipedia
editors, and Internet traffic) and to real organizational networks (Lajaunie et al.'s Southeast Asian
inter-organizational networks). "Asserted, never measured" overstates it. "Measured on animal
collectives, almost never on organizations" is the accurate reading: of the six empirical computations,
none uses firm-, market-, or team-level organizational data of the kind the lab's own program targets.

## H4 — Substrate-diverse but citation-connected: challenged

The prediction was a block-diagonal citation matrix — substrates developing in isolation. The data
contradict it. Coders sort the corpus into four substrate clusters: artificial/abstract systems (16),
philosophical/scope work (15), animal-collective "swarm" systems (5, including plant meristems), and
social-organizational systems (4). No economy or market cluster forms at all; searches for Φ applied to
economies or financial markets returned papers that use the word "integration" without any IIT content,
and none entered the corpus. So the topics do fragment by substrate, and one predicted substrate is
essentially empty.

The citation graph, though, is not block-diagonal. Within-cluster seed-to-seed links total 24;
cross-cluster links total 27. The artificial and philosophical clusters are the hubs: artificial links
to philosophical 11 times and to swarm 7 times. The substrates cite across their boundaries more than
within them, because they draw on shared IIT machinery — the same formal Φ measures, the same PyPhi
tooling, the same Tononi-group foundations. This is one conversation with several application targets,
not four silos. Assembly-spanning confirms the ceiling from the other side: of 3,932 external papers
citing the corpus, 3,837 touch only one substrate cluster, 80 span two, 13 span three, and just 2 span
all four. Outsiders have not unified the substrates, but insiders already cross-cite. The hypothesis as
written is challenged; the corrected finding is that the beyond-consciousness literature is
substrate-diverse and internally connected, held together by method rather than by a shared object.

## A finding not in the hypotheses

The corpus divides almost evenly between claims that Φ does index integration in a non-brain substrate
(stylized_fact, 20) and claims that dispute or bound that application (critique, 19). Half of the
literature that applies IIT beyond the brain is skeptical of doing so — the panpsychism debate, the
strong-versus-weak-IIT distinction, the arguments that Φ has never been computed on a real physical
system. A program that carries Φ into a new substrate inherits an active, unsettled argument about
whether the carry is licensed.

## Limitations

- **Agent coders.** The three coders are language-model agents on a fixed codebook, not trained human
  raters. The high κ shows they applied the codebook consistently; it does not certify the codebook
  captures the constructs a domain expert would draw. Substrate and evidence were near-mechanical
  (κ = 1.00); claim_type carries more interpretive load.
- **Corpus boundary and size.** Forty sources is small, so cluster-level counts (social_org = 4,
  swarm = 5) are thin, and a few reclassifications would move the substrate proportions. The boundary
  excludes the canonical IIT 3.0/4.0/substrate consciousness formulations as core-brain theory; a
  reviewer who counted those as foundational scope work would enlarge the philosophical cluster.
- **Connector-sourced search.** Candidates came from two academic connectors (Scholar Gateway,
  Consensus) run over natural-language queries, then hand-screened, rather than from an exhaustive
  database export. Recall is not guaranteed; a paper indexed only under other terms could be missed.
- **Elided references and partial resolution.** Semantic Scholar returns citers far more completely
  than references (the corpus refs channel is largely empty), and 3 of 6 canon anchors plus several
  preprint seeds did not resolve to a paperId. The H2 and H4 graph tests therefore run mostly on the
  inbound-citer channel. The zero canon cross-citation is robust to this — it holds on the three anchors
  that did resolve, including coordination theory itself — but the cross-cluster counts are a floor, not
  a full census.
