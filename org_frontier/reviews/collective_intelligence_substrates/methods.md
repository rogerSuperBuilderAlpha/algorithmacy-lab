# Methods — substrates of collective-intelligence research

## Corpus boundary (explicate)
- **Substantive:** sources whose object is a *collective* that is claimed to compute, decide, or know
  something no member holds — human teams, human crowds, animal or robotic swarms, artificial
  multi-agent systems, information/prediction markets, or human-machine hybrids. A source is in scope
  iff its title + abstract name a collective-intelligence / collective-behavior construct AND a
  substrate cue (group, team, crowd, swarm, agent, market, colony, flock). Front-matter and clearly
  off-topic hits returned by semantic search are screened out.
- **Procedural:** English-language journal articles and conference papers indexed by the Scholar
  Gateway (Wiley) academic corpus, no fixed date window (the harvested set runs 2008–2026). Gray
  literature is out except where the index surfaces a preprint with a DOI. Databases: Scholar Gateway
  semantic search as the primary channel; Consensus (Semantic Scholar / PubMed / Scopus / arXiv) as a
  supplementary recall check.
- A source is included iff the boundary rule above resolves to true on its title + abstract, decided
  by `build_corpus.py`.

## Search and harvest (execute)
- Seed set: fourteen Scholar Gateway semantic-search queries, one to three per substrate — human
  groups/teams, swarms/social insects/robotics, crowds/crowdsourcing, multi-agent AI/LLM agents,
  prediction markets, human-AI hybrids, stigmergy/self-organization, plus general-theory and
  organization/citizen-science queries. Candidates deduplicated by DOI then normalized title.
- Snowball: `lib/harvest.py` over `seeds.json` → each seed's backward references and forward citers
  from Semantic Scholar. Publishers elide references for many papers, so the inbound citer channel
  carries the H1 test.
- Stopping rule: the fourteen queries were run; after screening, marginal new queries returned
  mostly duplicates or out-of-boundary hits (yield below Booth's five-per-hundred heuristic), so the
  search terminated at 48 in-boundary sources.
- Final corpus: 48 sources (`literature/corpus.jsonl`), all with DOIs.

## Coding (encode)
- Codebook: `coding_protocol.md`. Variables: `substrate` (human_team | crowd | swarm | ai_multiagent
  | market | hybrid | na), `method` (empirical | model | conceptual), `spans_multiple` (yes | no).
- Coders: three independent LLM agents, blind to one another, each → `coding/coder{A,B,C}.jsonl`.
  Agent coders are a limitation, not trained human raters; the reliability figure bounds it.
- Reliability: `lib/reliability.py` → Fleiss' κ per categorical variable and a majority-vote
  adjudicated dataset → `results/frozen.json`.

## Analysis (evaluate)
- Content-coding tests: the `substrate` frequency distribution (H2), the proportion of
  `spans_multiple = yes` (H3), the `method` distribution as context.
- Bibliometric test: `lib/bibliometrics.py` cluster matrix over `clusters.json` (slug → adjudicated
  substrate) — within-substrate versus cross-substrate citation links among the corpus seeds (H1).
- Statistics: distributions with counts and proportions; the citation matrix as a within/cross split.
  If the harvest is rate-limited, H1 is reported partial from whatever edges resolved and H2/H3 stand
  on the coded corpus.
