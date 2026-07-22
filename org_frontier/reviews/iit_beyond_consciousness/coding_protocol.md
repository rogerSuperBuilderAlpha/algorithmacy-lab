# Coding protocol (codebook) — integrated information beyond consciousness

Code each source from its title + abstract (and note, where present). Code what the SOURCE does, not
what this review predicts. You are one of several independent coders; do not consult another coder's
output. Use `na` where a variable does not apply. When unsure between two values, pick the better fit —
disagreement is expected and measured.

## Variables (one JSON object per source → your JSONL file)

- **slug** — the source id.
- **substrate** — the system IIT/Φ is applied to (tests H4): `neural` (brain/neural-analogy models,
  including artificial neural nets) | `swarm` (animal groups, swarms, collective behavior, ant
  colonies) | `social_org` (organizations, teams, firms, markets, economies, institutions, social
  networks) | `artificial` (engineered/robotic/AI multi-agent systems, not framed socially) |
  `philosophical` (conceptual/foundational discussion of IIT's scope, no specific applied substrate) |
  `na` (not an IIT/Φ-beyond-consciousness source).
- **evidence** — how the source treats Φ (tests H3): `conceptual` (analogy or argument, no computed
  Φ) | `formal_model` (Φ or a declared Φ-proxy computed on a toy, simulated, or abstract system) |
  `empirical` (Φ or a declared proxy computed on real organizational / social / economic / behavioral
  data) | `na`.
- **claim_type** — the knowledge-weaving type of the source's central claim about applying Φ beyond
  consciousness: `stylized_fact` (asserts Φ does index integration in this substrate) | `assumption`
  (assumes the mapping to motivate other work) | `critique` (disputes or bounds the application) |
  `omission` (notes the application is missing / calls for it) | `na`.
- **cites_org_theory** — does the source engage organization / coordination theory at all (tests H2,
  as a coded cross-check on the citation graph): `yes` (cites or discusses coordination/organization
  theory) | `no` | `na`.

## Output

Write JSONL to `coding/coder<yourname>.jsonl`, one line per source:
`{"slug":"smith2020","substrate":"social_org","evidence":"conceptual","claim_type":"assumption","cites_org_theory":"no"}`

Code every source in the corpus (`literature/corpus.jsonl`). If capacity runs low, code in list order
and report how far you got.

## What the hypotheses predict (do NOT let this bias a call — code the source, not the prediction)

- H3 predicts `evidence=empirical` is rare. A source that genuinely computes Φ on real organizational
  data is a real disconfirming datum — record it as `empirical`.
- H4 predicts substrates fragment. Code the substrate the source actually uses, not the one the review
  is about.
