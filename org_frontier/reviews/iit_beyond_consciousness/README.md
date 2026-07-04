# Integrated information beyond consciousness

**Question (descriptive).** Has integrated information theory (IIT / Φ) been applied beyond
consciousness — to organizations, teams, economies, markets, and collective/social systems — and what
does that literature claim?

**Status.** In progress. Result slot: <headline once computed>.

Why the lab cares: its whole program applies exact IIT-4.0 Φ to organizational coordination. This
review measures whether that application is an open gap (small, disconnected, mostly conceptual) or a
crowded field. The four falsifiable claims are in [`hypotheses.md`](hypotheses.md), committed before
any result. Corpus boundary, search, and coder design in [`methods.md`](methods.md); codebook in
[`coding_protocol.md`](coding_protocol.md); findings in [`FINDINGS.md`](FINDINGS.md).

## Reproduce

```bash
python -m org_frontier.reviews.lib.harvest org_frontier/reviews/iit_beyond_consciousness/seeds.json \
    --out org_frontier/reviews/iit_beyond_consciousness/edges/
python -m org_frontier.reviews.lib.reliability org_frontier/reviews/iit_beyond_consciousness/coding \
    --categorical substrate,evidence,claim_type,cites_org_theory \
    --out org_frontier/reviews/iit_beyond_consciousness/results/frozen.json
python -m org_frontier.reviews.iit_beyond_consciousness.run
```
