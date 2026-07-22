# Methods — construct proliferation in the "new organizational form"

## Corpus boundary (explicate)
- **Substantive:** sources that propose, adopt, or theorize an alternative to the bureaucratic /
  hierarchical firm as a distinct organizational *form* — platform, ecosystem, meta-organization,
  community, network organization, partial organization, open collaboration / peer production, hybrid,
  field-as-form, and named variants (holacracy, heterarchy, adhocracy, post-bureaucratic form). A
  source is in if its title or abstract treats one of these as a form of organizing worth naming and
  theorizing. Pure firm-strategy papers that use "platform" only as a product feature, and papers on
  organizational *change* with no form construct, are out.
- **Procedural:** English-language; indexed by the academic semantic-search connectors (Scholar
  Gateway, Consensus) over Semantic Scholar / Scopus / PubMed / ArXiv; organization-theory and
  management venues; no hard date floor, but the "new form" framing concentrates post-1990.
- A source is included iff its title or abstract names and theorizes one of the alternative forms.

## Search and harvest (execute)
- **Seed set:** semantic search over queries pairing "new organizational form" with each candidate
  label — "platform as a new organizational form," "meta-organization theory," "organizational
  ecosystems as a form," "partial organization theory," "community forms of organizing," "network
  organization form," "open collaboration peer production organizing." The union, deduplicated and
  screened against the boundary rule, is the corpus (`literature/corpus.jsonl`).
- **Snowball:** `lib/harvest.py` over `seeds.json` (the screened seeds' DOIs) pulls backward references
  and forward citers for the H3 citation graph. References are elided by some publishers, so the
  inbound-citer channel carries most of the signal.
- **Stopping rule:** search terms are exhausted when new label-queries return no new in-boundary
  sources; the screened-out count is logged so coverage is auditable.

## Coding (encode)
- Codebook: `coding_protocol.md`. Variables: `label`, `differentia_mode`, `parent_form`, `claim_type`.
- Coders: three independent agents, blind to one another, each → `coding/coder<X>.jsonl`, coding from
  the title + abstract in `literature/corpus.jsonl`.
- Reliability: `lib/reliability.py` → Fleiss' κ per categorical variable, majority-vote adjudicated
  dataset → `results/frozen.json`.

## Analysis (evaluate)
- **H1** — the count of distinct `label` values in the adjudicated dataset; the label-frequency table.
- **H2** — the `differentia_mode` distribution (share `by_contrast`).
- **H3** — `lib/bibliometrics.py` cluster matrix using the coded `label` as the cluster key
  (`clusters.json` maps each seed slug to its adjudicated label); within- versus cross-label links.
- Report each hypothesis with its statistic and a supported / qualified / challenged verdict, with the
  reliability figure attached. State limitations: elided references, small per-label clusters, agent
  coders, a connector-bounded corpus. If the harvest is rate-limited, H1/H2 are reported from coding
  and H3 is marked partial.
