# Methods — integrated information beyond consciousness

## Corpus boundary (explicate)
- **Substantive:** sources that apply, extend, or discuss applying integrated information theory (IIT)
  or its measure Φ to a system *other than* an individual brain/mind — organizations, teams, firms,
  markets, economies, social networks, animal groups/swarms, or engineered multi-agent systems — or
  that discuss the scope of such application. Pure neuroscience/consciousness IIT (Φ of a brain) is out
  of scope; a neural-*analogy* model explicitly transferred to a collective is in.
- **Procedural:** English-language; indexed in Semantic Scholar; 2004–present (Tononi's first IIT paper
  was 2004). Preprints included (the topic is nascent and partly on arXiv/bioRxiv), flagged in the
  `.bib`.
- A source is included iff its title or abstract asserts an IIT/Φ treatment of a non-individual-brain
  system, or a foundational discussion of that scope.

## Search and harvest (execute)
- **Seed set:** Semantic Scholar keyword search over combinations of {integrated information, IIT, phi,
  Φ} × {organization, firm, team, collective, social, economy, market, swarm, ant colony, group,
  multi-agent, society}. The union, deduplicated and screened against the boundary rule, is the seed
  corpus (`literature/corpus.jsonl`).
- **Snowball:** `lib/harvest.py` over `seeds.json` (the screened seeds' DOIs) pulls backward references
  and forward citers, for the H2/H4 citation graph. References are elided by some publishers, so the
  inbound-citer channel carries most of the signal.
- **Stopping rule:** search terms are exhausted when new terms return no new in-boundary sources; the
  screened-out count is logged so coverage is auditable.

## Coding (encode)
- Codebook: `coding_protocol.md`. Variables: `substrate`, `evidence`, `claim_type`, `cites_org_theory`.
- Coders: three independent agents, blind to one another, each → `coding/coder<X>.jsonl`, coding from
  the title + abstract in `literature/corpus.jsonl`.
- Reliability: `lib/reliability.py` → Fleiss' κ per categorical variable, majority-vote adjudicated
  dataset → `results/frozen.json`.

## Analysis (evaluate)
- **H1** — corpus size and year distribution from the adjudicated dataset / corpus metadata.
- **H2** — `lib/bibliometrics.py` cross-citation between the IIT-applied cluster and the fixed
  coordination-canon reference set (`clusters.json` assigns canon seeds a `coordination_canon` label);
  corroborated by the `cites_org_theory` coded proportion.
- **H3** — the `evidence` distribution (share `empirical`).
- **H4** — `lib/bibliometrics.py` cluster matrix over the `substrate` clusters.
- Report each hypothesis with its statistic and a supported / qualified / challenged verdict, with the
  reliability figure attached. State limitations: elided references, small clusters, agent coders, a
  Semantic-Scholar-bounded corpus.
