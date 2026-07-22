# Substrates of collective intelligence — the question in one line

**Question.** Collective-intelligence research studies human teams, crowds, swarms, multi-agent AI,
markets, and hybrids. Does it cite across substrates or fragment into parallel literatures?
(descriptive-integrative)

**Status.** Complete. Result: the field fragments — 6 of ~2,053 external citers span two substrates,
none span three; swarm is the largest substrate (35%), not the human ones; cross-substrate synthesis
is rare (10%) and entirely conceptual. Substrate κ = 0.963.

Falsifiable claims: [`hypotheses.md`](hypotheses.md) (pre-registered). Corpus boundary and search:
[`methods.md`](methods.md). Codebook: [`coding_protocol.md`](coding_protocol.md). Findings:
[`FINDINGS.md`](FINDINGS.md). Manuscript: [`paper.md`](paper.md).

## Reproduce
```bash
python3 -m org_frontier.reviews.collective_intelligence_substrates.build_corpus
python3 -m org_frontier.reviews.lib.harvest \
    org_frontier/reviews/collective_intelligence_substrates/seeds.json \
    --out org_frontier/reviews/collective_intelligence_substrates/edges/
python3 -m org_frontier.reviews.collective_intelligence_substrates.run
```
