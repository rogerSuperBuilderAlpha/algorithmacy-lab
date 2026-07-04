# The Substrates of Collective Intelligence: One Question, Six Literatures, Almost No Traffic Between Them

## Research Summary

Collective-intelligence research asks whether a group can compute, decide, or know something that no
member holds alone. It asks this of many different kinds of group: human work teams, online crowds,
ant colonies and fish schools, swarm robots, artificial multi-agent systems, prediction markets, and
mixed human-machine collectives. This study treats that spread as a measurable object. It codes 48
collective-intelligence sources for the substrate each one studies, the method each uses, and whether
each reasons across more than one substrate, and it harvests the citation graph around the corpus to
see whether the substrates read each other. Three findings follow. The citation graph is fragmented:
of roughly 2,053 external papers that cite the corpus, six cite across two substrates and none across
three. Cross-substrate synthesis inside the corpus is rare and entirely conceptual: five of 48 sources
span two or more substrates, and none of the five reports data or a model. The field's mass sits where
the pre-registration did not expect it — swarm and collective-animal research is the single largest
substrate at 35%, and the human substrates together reach only 46%, a plurality rather than the
predicted majority. Intercoder reliability is almost perfect across all three coded variables (Fleiss'
κ of 0.96, 0.92, and 1.00). The picture is a field that runs the same experiment in six enclosures and
rarely opens the doors between them.

## Introduction

A group of people, a colony of ants, a market, and a population of learning agents have little in
common as physical systems. Researchers study all four with one question: does the collective, as a
unit, do something its parts cannot? The wisdom-of-crowds tradition asks it of aggregated human
judgments. The collective-intelligence-factor line asks it of small human teams. Swarm biology asks it
of insects and fish. Swarm robotics and multi-agent learning ask it of machines. Prediction markets
ask it of prices. The question travels; the answer is supposed to be a general property of collectives.

If the question is general, the literatures that ask it should talk to each other. A swarm result
about quorum sensing should inform a claim about how a jury reaches consensus; a crowd-aggregation
theorem should bear on multi-agent voting. Whether that traffic exists is a fact about the field's
structure, and a citation graph can measure it. This review runs that measurement. It is a
descriptive-integrative review in the systematicity sense (Simsek, Fox & Heavey, 2023): it sorts a
field's sources by the kind of collective they study and asks whether those sorts form one conversation
or several.

The exercise matters beyond bibliometric curiosity. A research program that proposes a
substrate-independent lens on coordination — one that would read a firm, a swarm, and an agent
population with the same instrument — needs to know whether the collective-intelligence field is
already integrated across substrates or is waiting to be. An integrated field needs no new bridge. A
fragmented one names the gap the bridge would fill. The pre-registration, committed before any coding,
took three positions: the field fragments by substrate (H1), human teams and crowds carry its mass
(H2), and cross-substrate synthesis is rare (H3). The data support two of the three and overturn the
one about where the field's weight sits.

## Framework

The review draws its questions from knowledge weaving (Simsek, Heavey, Fox & Yu, 2022), which sorts a
field's knowledge claims into stylized facts, key assumptions, enduring critiques, and substantive
omissions, and its procedure from systematicity (Simsek, Fox & Heavey, 2023), which fixes the stages —
envision, explicate, execute, encode, evaluate, exposit — and the disciplines that make a review
auditable: an explicit corpus boundary, a stopping rule, independent coders, and a reported reliability
figure.

Three knowledge claims about the collective-intelligence field become three hypotheses. The first is a
substantive omission cast as structure. If the substrates developed in isolation, the citation graph is
block-diagonal by substrate: sources cite within their own kind of collective and ignore the others.
The bibliometric test is the assembly-spanning count — how many external papers cite corpus sources
from two or more substrates. A field that reads across substrates produces many spanning citers; a
fragmented one produces almost none.

The second is a stylized fact about the field's center of gravity. Management and psychology treat
human teams and crowds as the paradigm cases of collective intelligence, so the pre-registration
predicted those two substrates would form a majority of the corpus, with swarm and multi-agent AI as
smaller, newer literatures. The test is the substrate frequency distribution.

The third is a substantive omission at the level of the individual source. Even without a citation
graph, one can ask how many sources themselves reason across substrates — compare a swarm to a human
team, transfer a crowd-aggregation mechanism to a set of agents. The prediction was that such sources
are rare. The test is the proportion coded `spans_multiple = yes`.

## Method

**Corpus.** The substantive boundary admits a source if its title and abstract name a
collective-intelligence or collective-behavior construct and a substrate cue — group, team, crowd,
swarm, agent, market, colony, flock. The procedural boundary is the Scholar Gateway academic index,
queried by semantic search, with Consensus as a supplementary recall check; no date window was fixed,
and the harvested set runs 2008 to 2026. Fourteen semantic-search queries seeded the corpus, one to
three per substrate, plus general-theory and organization queries. Candidates were deduplicated by DOI
then by normalized title, and a small stoplist removed front-matter and clearly off-topic hits that
semantic search returns. Screening left 48 in-boundary sources, all with DOIs. The search stopped when
additional queries returned mostly duplicates or out-of-boundary hits, below Booth's five-relevant-per-
hundred heuristic.

**Coding.** A fixed codebook defined three variables. `substrate` takes one of seven values —
`human_team`, `crowd`, `swarm`, `ai_multiagent`, `market`, `hybrid`, or `na` — assigned to the one kind
of collective a source foregrounds. `method` is `empirical`, `model`, or `conceptual`. `spans_multiple`
is `yes` only when a source substantively develops two or more substrates, not on a passing mention.
Three coders applied the codebook to title and abstract, blind to one another, each writing to its own
file. The coders are LLM agents; this is a limitation the reliability figure bounds and the discussion
returns to.

**Analysis.** `reliability.py` computed Fleiss' κ per variable and a majority-vote adjudicated dataset.
`harvest.py` pulled each seed's backward references and forward citers from Semantic Scholar;
`bibliometrics.py` computed the substrate-to-substrate citation matrix and the assembly-spanning count
over the adjudicated substrate labels. Semantic Scholar elides outbound references for most publishers,
so the inbound citer channel carries the H1 test.

## Results

**Reliability.** Agreement was almost perfect on every variable: substrate κ = 0.963 (97.2%
agreement), method κ = 0.916 (95.8%), spans_multiple κ = 1.000 (100%). The substrate distinction, the
one the whole review rests on, is not one reader's judgment.

**Substrate distribution (H2).** Swarm is the largest substrate, and the human substrates fall short of
a majority.

| substrate | sources | share |
|---|---|---|
| swarm | 17 | 35% |
| crowd | 13 | 27% |
| human_team | 9 | 19% |
| na | 7 | 15% |
| hybrid | 2 | 4% |
| market | 0 | 0% |
| ai_multiagent | 0 | 0% |

Human teams and crowds together account for 22 of 48 sources, 46%. The prediction that they would form
a majority fails, and it fails because swarm and collective-animal research is larger and older than
the management-and-psychology framing assumed. Two substrates the pre-registration expected to find —
markets and artificial multi-agent AI — do not appear at all. The market absence reflects a thin,
economics-indexed literature the search reached poorly; the multi-agent-AI absence reflects the index
itself, which under-covers the computer-science venues where that work publishes. Both zeros are facts
about this corpus, not proven facts about the field. On method, the corpus is conceptual-heavy: 31
conceptual, 13 empirical, 4 model.

**Cross-substrate citation (H1).** The substrate-to-substrate matrix among the 48 seeds is nearly
empty — one within-swarm link, zero cross-substrate links — because 48 sources are a thin sample of
five large literatures and rarely cite one another directly. The assembly-spanning count over the full
citer neighborhood carries the finding.

| citers spanning | count |
|---|---|
| 1 substrate | 2,047 |
| 2 substrates | 6 |
| 3+ substrates | 0 |

Of roughly 2,053 external papers that cite the corpus, 2,047 cite it from within a single substrate,
six reach across two, and none reaches across three. Fewer than one citer in three hundred bridges two
substrates. Whatever integration the field's rhetoric claims, its citation behavior does not show it:
readers of swarm work cite swarm work, readers of crowd work cite crowd work, and the two audiences
barely overlap.

**Cross-substrate synthesis (H3).** Five of 48 sources span two or more substrates, 10%, well under the
one-third threshold the prediction set. The composition of those five sharpens the point: all five are
conceptual. A broad "collective behavior" synthesis, an essay linking markets to the wisdom of crowds,
a piece transferring swarm mechanisms to human teams, an information-aggregation framework, and a
conservation-oriented programmatic review. Not one empirical study and not one formal model in the
corpus reasons across substrates. Synthesis, where it happens, is a matter of essays and framings, not
of shared data or shared models — and the H1 result shows even those essays are read within one
substrate at a time.

## Discussion

The three results cohere into one claim: collective-intelligence research is a set of parallel
literatures that ask the same question of different collectives and rarely cite across the divide. The
generality is in the question, not in the practice. A swarm biologist and a team-performance
psychologist both study whether the group exceeds its members, and both can state that shared aim, but
their reference lists come from different rooms.

The H2 reversal is the most instructive result, because it corrects the reviewer's own prior. Coming
from management and organizational research, the natural assumption is that human teams and crowds are
where collective intelligence lives, with the Woolley collective-intelligence-factor studies as the
paradigm. Measured across the field, that assumption is parochial. Swarm and collective-animal behavior
is the larger and older tradition, and it anchors much of the field's empirical and formal work. A
research program that wants to speak about collectives in general cannot take the human team as the
default case; the swarm has at least as strong a claim to being the paradigm, and the machine cases are
growing outside the reach of a humanities-and-social-science index.

For a substrate-independent lens on coordination, the fragmentation is the opening. If the field already
read fluidly across substrates, a new cross-substrate instrument would be redundant. It does not. The
six-in-two-thousand spanning rate says the bridges are missing, and the all-conceptual character of the
existing synthesis says the bridges that exist are rhetorical rather than methodological. An instrument
that measured the same property — say, the irreducibility of a coordinating whole — in a swarm, a team,
and an agent population with one procedure would supply exactly the connective tissue the citation graph
shows to be absent. This review does not build that instrument or claim it is necessary. It measures the
gap the instrument would address, and the gap is real.

The result also disciplines the claim. The absence of the market and multi-agent-AI substrates is partly
an artifact of where the search looked, and the fragmentation verdict must hold that artifact in view.
The field is more fragmented than any single-index corpus can show, because the
indexes themselves partition it: a Wiley-anchored search finds the biology and the psychology and misses
the computer science. That the substrates are hard to see together in one database is itself a mild form
of the fragmentation the review reports.

## Limitations

The coders are LLM agents, not trained human raters. The reliability is high, but agent agreement can
reflect shared model priors as much as a clean construct, and a human-rater replication would carry more
weight. The corpus is modest at 48 sources and bounded by a single index that under-covers computer
science and economics; the swarm-led distribution would soften, and the missing AI and market substrates
would appear, under a CS-inclusive search. Substrate and method were coded from title and abstract, so a
source that spans substrates only in its body is undercounted. Semantic Scholar elides outbound
references, so the citation test rests on inbound citers; the spanning count is robust to this, but the
seed-to-seed matrix is thin and underpowered. The verdicts should be read as bounded by these gates, and
the H1 and H3 findings, both of which survive the boundary effects, more firmly than the H2 distribution,
which the boundary partly shapes.

## References

Simsek, Z., Fox, B. C., & Heavey, C. (2023). Systematicity in organizational research literature
reviews: A framework and assessment. *Organizational Research Methods, 26*(2), 292–321.
https://doi.org/10.1177/10944281211008652

Simsek, Z., Heavey, C., Fox, B. C., & Yu, T. (2022). Compelling questions in research: Seeing what
everybody has seen and thinking what nobody has thought. *Journal of Management.*
https://doi.org/10.1177/01492063211073068

The 48 coded sources, with DOIs, are in `literature/references.bib`; the adjudicated codes are in
`results/frozen.json` and the citation-graph summary in `results/summary.json`. Representative sources
by substrate: swarm — collective decision-making in aquatic mammals; ant and termite collective
behavior; quorum response in animal collective motion; bacterial stigmergy. Crowd — integration of
social information by human groups; crowd-sourced seismic interpretation; open-innovation contests.
Human team — task structure as a boundary condition for collective intelligence; transactive memory and
collective identification. Hybrid — fostering collective intelligence in human–AI collaboration; the
COHUMAIN socio-cognitive architecture. Cross-substrate (conceptual) — a general "collective behavior"
synthesis; markets and the wisdom of crowds; swarm-to-human-team transfer; the rules of information
aggregation.
