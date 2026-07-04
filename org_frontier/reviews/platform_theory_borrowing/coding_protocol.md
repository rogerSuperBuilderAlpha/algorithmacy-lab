# Coding protocol (codebook) — theory borrowing in platform-governance research

Code each source from its title + abstract. Code what the SOURCE does, not what this review predicts.
You are one of several independent coders; do not consult another coder's output. When unsure between
two values, pick the better fit — disagreement is expected and measured. Code every source in
`literature/corpus.jsonl`.

## Variables (one JSON object per source → your JSONL file)

- **slug** — the source id (copy from the corpus).
- **year** — the publication year (copy from the corpus).
- **parent_theory** — the *primary* established body of theory the source imports to explain the
  platform. Choose the one that most drives the source's argument (tests H1):
  - `tce` — transaction-cost economics: make-vs-buy, governance-form choice (market/hierarchy/hybrid),
    asset specificity, contracting hazards, boundary of the firm.
  - `two_sided_market` — two-/multi-sided-market economics: cross-side network effects, platform
    pricing structure, chicken-and-egg / getting-both-sides-on-board, envelopment, competition
    between platforms as markets.
  - `rdt` — resource-dependence theory: power/dependence between platform and participants, control
    over critical resources, dependence asymmetry, resource orchestration/control.
  - `network_embeddedness` — economic-sociology network and embeddedness theory: relational/structural
    embeddedness, network position/centrality, tie structure, social-network analysis of the platform.
  - `institutional` — institutional theory: legitimacy, institutional logics, isomorphism, regulation,
    norms, institutional work, sensemaking of the new form as institution.
  - `ecosystem` — ecosystem / business-ecosystem / complementor / generativity theory: platform as
    ecosystem, complementor participation and engagement, boundary resources, orchestration of an
    ecosystem, value co-creation among complementors, meta-organization.
  - `agency` — agency / control theory: principal-agent, monitoring and incentive alignment,
    algorithmic management and control as a control-theory problem, signalling.
  - `other` — a body of theory outside the seven above (e.g. labour-process theory, entrepreneurship,
    RBV, stakeholder theory, structuration, common-pool-resource/commons, dynamic capabilities), or a
    source with no identifiable single parent theory.
- **borrowing_mode** — how the source treats the parent theory (tests H2):
  - `apply` — imports the parent theory and applies it to the platform case; uses the theory as a
    ready lens, confirms or illustrates it. The default for most empirical and conceptual applications.
  - `extend` — develops or modifies the parent theory using the platform case: adds constructs,
    boundary conditions, or a new mechanism the parent theory did not have.
  - `critique` — disputes, bounds, or argues against the parent theory using the platform case; shows
    where the theory fails or misleads for platforms.
- **multi_theory** — does the source combine two or more identifiable parent theories in its core
  argument (tests H3): `yes` (draws on ≥2 of the parent-theory bodies above as load-bearing) | `no`
  (one parent theory carries the argument).

## Output

Write JSONL to `coding/coder<yourname>.jsonl`, one line per source, e.g.:
`{"slug":"platformenvelopment2011","parent_theory":"two_sided_market","borrowing_mode":"extend","multi_theory":"no","year":2011}`

Code every source in the corpus. If capacity runs low, code in list order and report how far you got.

## What the hypotheses predict (do NOT let this bias a call — code the source, not the prediction)

- H1 predicts economics theories (`tce`, `two_sided_market`) lead early and `institutional`/`ecosystem`
  rise later. Code the theory the source actually imports, whatever its year.
- H2 predicts `apply` dominates. A source that genuinely extends or critiques its parent theory is a
  real datum — record `extend` / `critique`.
- H3 predicts single-theory imports dominate. If a source truly braids two parent theories, code
  `multi_theory=yes`.
