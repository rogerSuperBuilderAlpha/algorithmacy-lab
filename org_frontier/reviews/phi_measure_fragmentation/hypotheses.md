# Hypotheses — do the proposed measures of integrated information validate against a ground truth, and do the measure-families connect?

*Committed before any corpus is harvested or coded. The question: the literature has proposed many
measures of integrated information, complexity, and synergy — exact IIT Φ, practical proxies such as
Φ*, causal emergence, integrated information decomposition, total correlation, geometric measures. Are
these measures validated against a ground truth (an exact or reference Φ), or asserted to capture
integration? And do the measure-families cite one another, or fragment on the citation graph? Each
hypothesis names the knowledge claim it tests (in the knowledge-weaving typology), its
operationalization, and the outcome that would support versus challenge it.*

This review mirrors the foundations arm at the level of the literature. The foundations experiments
asked, on exactly-computable systems, *what tracks exact Φ*, and found that no single cheap number is
integrated information. This review asks the analogous question of the published record: when authors
propose a measure of integration, do they check it against a ground truth, or do they assume it? The
foundations arm audits measures on data; this arm audits the literature that proposes them.

## H1 — Many distinct measure families
- **Knowledge claim (stylized fact):** the literature does not converge on one measure of integrated
  information; it proposes many distinct families — exact IIT Φ, practical proxies (Φ*, geometric,
  whole-minus-parts), causal emergence, integrated information decomposition / synergy, total
  correlation and other information-theoretic complexity measures.
- **Operationalization:** the `measure_family` code over the screened corpus; count the families that
  each attract a non-trivial share of sources (≥ 3).
- **Predicts:** at least five families each carry ≥ 3 sources; no single family holds a majority.
- **Challenged if:** one or two families account for nearly all sources.

## H2 — Asserted, not validated against a ground truth
- **Knowledge claim (key assumption):** that a proposed measure captures integration is taken as
  given; few sources validate the measure against an exact or reference Φ, or against any external
  ground truth.
- **Operationalization:** the `validation` code — `ground_truth` (validated against exact IIT Φ, a
  reference measure, or an external criterion) vs `internal` (self-consistency, axioms, or
  toy-example sanity checks only) vs `none/conceptual` (asserted, proposed, or argued, no validation) vs
  `na`. Report the share `ground_truth`.
- **Predicts:** `ground_truth` is a small minority; `none/conceptual` plus `internal` dominate.
- **Challenged if:** `ground_truth` is a plurality or more.

## H3 — Fragmentation on the citation graph
- **Knowledge claim (enduring critique):** the measure-families develop in relative isolation; a
  family cites within itself more than across to rival families.
- **Operationalization:** the cluster-to-cluster citation matrix over the `measure_family` clusters,
  on the harvested graph (`lib/bibliometrics.py`); compare within-family to cross-family link counts.
- **Predicts:** within-family citation links exceed cross-family links (a block-diagonal tendency).
- **Challenged if:** the matrix is well-connected across families (cross ≥ within).

## Method fixed in advance
- Corpus boundary and search: `methods.md` (substantive + procedural gates; semantic-search seed +
  citation snowball).
- Coders: three independent agents, blind to one another, on `coding_protocol.md`.
- Reliability reported (Fleiss' κ per categorical variable). Any hypothesis the data contradict is
  reported as challenged. If the citation harvest is rate-limited, H1 and H2 are reported from the
  coding and H3 is marked partial.
