# Integrated information beyond consciousness

**Question (descriptive).** Has integrated information theory (IIT / Φ) been applied beyond
consciousness — to organizations, teams, economies, markets, and collective/social systems — and what
does that literature claim?

**Status.** Complete. Result: a nascent, method-bound literature of 40 sources (92% since 2015) that
does not touch organizational coordination theory (0 citation links to a six-work coordination canon;
8% of sources engage it), computes Φ on real data in only 15% of cases and almost never on
organizations, and — against the pre-registered prediction — cross-cites across substrate clusters more
than within them (bound by shared IIT machinery, not fragmented into silos). Verdicts: H1 supported,
H2 supported, H3 supported (qualified), H4 challenged. Fleiss' κ 0.87–1.00 across four variables.

Why the lab cares: its whole program applies exact IIT-4.0 Φ to organizational coordination. This
review measures whether that application is an open gap (small, disconnected, mostly conceptual) or a
crowded field — and finds an open gap. The four falsifiable claims are in
[`hypotheses.md`](hypotheses.md), committed before any result. Corpus boundary, search, and coder
design in [`methods.md`](methods.md); codebook in [`coding_protocol.md`](coding_protocol.md);
per-hypothesis verdicts in [`FINDINGS.md`](FINDINGS.md); write-up in [`paper.md`](paper.md).

## Reproduce

```bash
# 1. rebuild the clean corpus (curated in-boundary set; resolves DOIs via Crossref)
python -m org_frontier.reviews.iit_beyond_consciousness.build_corpus
# 2. append the coordination-canon anchors to seeds before harvesting
python - <<'PY'
import json, os
d = "org_frontier/reviews/iit_beyond_consciousness"
seeds = json.load(open(f"{d}/seeds.json")); have = {s["slug"] for s in seeds}
seeds += [c for c in json.load(open(f"{d}/canon_seeds.json")) if c["slug"] not in have]
json.dump(seeds, open(f"{d}/seeds.json", "w"), indent=1)
PY
# 3. harvest the citation graph, 4. reliability + adjudication, 5. hypothesis tests
python -m org_frontier.reviews.lib.harvest org_frontier/reviews/iit_beyond_consciousness/seeds.json \
    --out org_frontier/reviews/iit_beyond_consciousness/edges/
python -m org_frontier.reviews.lib.reliability org_frontier/reviews/iit_beyond_consciousness/coding \
    --categorical substrate,evidence,claim_type,cites_org_theory \
    --out org_frontier/reviews/iit_beyond_consciousness/results/frozen.json
python -m org_frontier.reviews.iit_beyond_consciousness.run
```
