# phi_measure_fragmentation — are the proposed integration measures validated and connected?

A quantitative archival review (Simsek, Fox & Heavey style) of the literature that proposes measures of
integrated information, complexity, and synergy. It treats the measures as a dataset: 68 sources coded
by three independent agents on measure family, validation target, and substrate.

**Question.** The field has proposed many measures of integration — exact IIT Phi, practical proxies
(Phi*, Phi_AR, geometric, compression), causal emergence, integrated information decomposition and
synergy, total correlation, neural (TSE) complexity. Are they validated against a ground truth, and do
the measure-families cite each other or fragment? This mirrors the foundations arm's "what tracks exact
Phi" question at the level of the literature.

**Verdicts.**
- **H1 (many families): supported.** Six families each carry >=3 sources; the largest holds 31%, no
  majority.
- **H2 (asserted, not validated): supported.** Only 13/68 (19%) validate against a ground truth; 81%
  are internal (axioms/desiderata/self-chosen demonstration) or conceptual.
- **H3 (citation fragmentation): partial.** The citation harvest was rate-limited on a shared Semantic
  Scholar API and did not finish; the family-to-family matrix is not reported. Checkpointed — restart
  the harvest to complete it.

Intercoder reliability (Fleiss' kappa): measure_family 0.963, validation 0.905, substrate 0.985.

See [`FINDINGS.md`](FINDINGS.md) for the verdicts and tables, [`paper.md`](paper.md) for the writeup,
[`hypotheses.md`](hypotheses.md) for the pre-registration, and [`coding_protocol.md`](coding_protocol.md)
for the codebook.

## Reproduce
```bash
python -m org_frontier.reviews.phi_measure_fragmentation.build_corpus
python -m org_frontier.reviews.lib.harvest phi_measure_fragmentation/seeds.json --out phi_measure_fragmentation/edges/
python -m org_frontier.reviews.lib.reliability phi_measure_fragmentation/coding --categorical measure_family,validation,substrate --out phi_measure_fragmentation/results/frozen.json
python -m org_frontier.reviews.phi_measure_fragmentation.run
```
