# Findings — collective-intelligence research splits by substrate, and the split is swarm-led, not human-led

Collective-intelligence research asks one question — does a group compute something no member holds —
across human teams, human crowds, animal and robotic swarms, artificial multi-agent systems, markets,
and human-machine hybrids. This review coded 48 sources for the substrate each studies and harvested
the citation graph around them. The field is fragmented: of roughly 2,053 external papers that cite the
corpus, 6 cite sources from two substrates and none from three or more. The field is also not shaped
the way the pre-registration assumed. Swarm work is the single largest substrate (35%), the human
substrates fall short of a majority (46% combined), and artificial multi-agent AI is absent from the
corpus this search returned.

## Intercoder reliability
| variable | Fleiss' κ | agreement | interpretation |
|---|---|---|---|
| substrate | 0.963 | 97.2% | almost perfect |
| method | 0.916 | 95.8% | almost perfect |
| spans_multiple | 1.000 | 100.0% | almost perfect |

Three independent agent coders, blind to one another, applied the codebook to title + abstract. The κ
figures answer the single-coder objection: the substrate calls are not one reader's idiosyncrasy.

## Results
| # | Hypothesis | Verdict | Statistic |
|---|---|---|---|
| H1 | Fragmented by substrate (block-diagonal citation) | Supported | 6 of ~2,053 external citers span two substrates; 0 span three or more; 0 cross-substrate links among seeds |
| H2 | Human teams and crowds dominate; swarm and AI smaller | Challenged | swarm 35% (largest); human_team + crowd 46% (not a majority); ai_multiagent 0% |
| H3 | Cross-substrate synthesis is rare | Supported | 5 of 48 sources (10%) span ≥ 2 substrates; all 5 are conceptual |

Substrate distribution (adjudicated, N = 48): swarm 17, crowd 13, human_team 9, na 7, hybrid 2,
market 0, ai_multiagent 0. Method mix: conceptual 31, empirical 13, model 4.

## What the data revise

**H2 was wrong about which substrate leads.** The pre-registration assumed human teams and crowds carry
the field's mass. In this corpus they do not. Swarm research — social insects, collective animal
behavior, swarm robotics, stigmergy — is the single largest substrate at 35%, larger than crowd (27%)
or human teams (19%) alone. Human teams and crowds together reach 46%, a plurality but not the predicted
majority. The likely reason is the substrate's age and breadth: collective-animal-behavior work is an
older, biology-anchored literature the semantic search reaches easily. The prediction was calibrated to
management and psychology, where the Woolley collective-intelligence-factor line is prominent; the field
as a whole is wider and older than that line.

**Artificial multi-agent AI is absent, and that is partly the corpus boundary.** Zero sources coded
`ai_multiagent`, despite a dedicated multi-agent / LLM-agent query. The Scholar Gateway index
(Wiley-anchored) under-covers the CS and AI venues (NeurIPS, AAMAS, arXiv) where multi-agent
reinforcement learning and LLM-agent collectives publish. The absence is a fact about this corpus, not
a proven fact about the field; a CS-indexed search would recover that substrate. Reported as measured,
flagged as bounded.

**H1 holds on the spanning test, not the seed matrix.** The 48 seeds barely cite one another (one
within-swarm link, zero cross-substrate), because 48 sources are a thin sample of five large
literatures — the seed-to-seed matrix is underpowered. The informative statistic is the assembly-spanning
count over the full citer neighborhood: 2,047 external papers cite the corpus from within a single
substrate, 6 reach across two, and none reach across three. Fewer than one citer in three hundred bridges
substrates. The five conceptual sources that themselves reason across substrates are the exception H3
names, and the citation graph shows even those bridges are read within one substrate at a time.

## Limitations
- **Agent coders, not trained humans.** The three coders are LLM agents. The κ is high (0.92–1.00), but
  agent agreement can reflect shared model priors as much as construct clarity. A human-rater replication
  would strengthen the substrate call.
- **Corpus boundary shapes the substrate distribution.** The Scholar Gateway (Wiley) index under-covers
  CS/AI and economics venues. The absence of `ai_multiagent` and the collapse of `market` to none are
  partly artifacts of where the search looked. The swarm-led shape would likely soften, and AI would
  appear, under a CS-inclusive search. N = 48 is modest.
- **Partial reference channel.** 47 of 48 seeds resolved (1 error stub). Semantic Scholar elides outbound
  references for most publishers, so H1 rests on the inbound citer channel. The spanning count is robust
  to this; the seed matrix is thin.
- **Title + abstract coding.** Substrate and method were coded from title + abstract, not full text. A
  source that spans substrates only in its body would be undercounted as `spans_multiple = no`.

## Reproduce
```bash
python3 -m org_frontier.reviews.collective_intelligence_substrates.build_corpus
python3 -m org_frontier.reviews.lib.harvest \
    org_frontier/reviews/collective_intelligence_substrates/seeds.json \
    --out org_frontier/reviews/collective_intelligence_substrates/edges/
python3 -m org_frontier.reviews.lib.reliability \
    org_frontier/reviews/collective_intelligence_substrates/coding \
    --categorical substrate,method,spans_multiple \
    --out org_frontier/reviews/collective_intelligence_substrates/results/frozen.json
python3 -m org_frontier.reviews.collective_intelligence_substrates.run
```
Registered numbers: substrate κ = 0.963; N = 48; swarm = 17 (35%); human_team + crowd = 22 (46%);
spans_multiple = yes 5 (10%); external citers spanning ≥ 2 substrates = 6 of ~2,053.
