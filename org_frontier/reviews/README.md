# Reviews — experiments on the literature

Quantitative, systematic archival reviews. Where the rest of the lab computes on Boolean models, this
arm computes on a body of scholarship: it treats a literature as a dataset and tests falsifiable
claims *about* that literature. The unit of work is a review that states hypotheses about a field —
what it studies, how its parts connect, what it asserts versus tests — and answers them with a coded
corpus and its citation graph, reporting intercoder reliability.

**In one line:** a literature has structure that can be measured — which sub-literatures cite each
other, which questions are saturated and which are open, which claims are asserted and which are
established — and measuring it turns a reading into a result another researcher can reproduce.

The method comes from two sources in organizational research methods, summarized in
[`METHODS_FOUNDATIONS.md`](METHODS_FOUNDATIONS.md): Simsek, Fox & Heavey's (2023) framework for
*systematicity* in reviews, and Simsek, Heavey, Fox & Yu's (2022) *knowledge weaving* process for
interrogating a literature's knowledge claims. The reusable procedure is
[`RESEARCH_PLAYBOOK.md`](RESEARCH_PLAYBOOK.md); the local operating rules are
[`AGENTS.md`](AGENTS.md).

This is a different genre from the lab's integrative literature review (the dissertation's Paper 1),
which builds a construct by synthesis. A review here does not build a construct; it *measures a field*
and reports statistics with a reliability figure.

## Reviews

- [`iit_beyond_consciousness/`](iit_beyond_consciousness/) — has integrated information (Φ) been
  applied beyond consciousness, to organizations, teams, economies, and collective systems, and what
  does that literature claim? Four pre-registered hypotheses on the size, connectedness,
  empirical grounding, and clustering of that literature.
  [`iit_beyond_consciousness/FINDINGS.md`](iit_beyond_consciousness/FINDINGS.md).

## Tooling

Reusable, content-agnostic scripts under [`lib/`](lib/):

- [`lib/harvest.py`](lib/harvest.py) — build the citation graph around a seed set (Semantic Scholar;
  checkpointed, resumable).
- [`lib/reliability.py`](lib/reliability.py) — Fleiss' κ, pairwise agreement, and majority-vote
  adjudication across independent coders.
- [`lib/bibliometrics.py`](lib/bibliometrics.py) — cluster-to-cluster citation matrix,
  assembly-spanning counts, and mutual-citation density from the harvested graph.

## Starting a review

Copy [`template/`](template/) to `org_frontier/reviews/<slug>/` (`lower_snake_case`), then follow the
playbook: envision the question and its knowledge claims, explicate the corpus boundary, execute the
search and citation harvest, encode with at least three independent coders, evaluate the claims with
the coded data and the citation graph, and exposit a `FINDINGS.md`. Commit `hypotheses.md` before
computing any result.

## Running

From the repository root (note the `org_frontier.reviews.` prefix):

```bash
python -m org_frontier.reviews.lib.harvest <slug>/seeds.json --out <slug>/edges/
python -m org_frontier.reviews.lib.reliability <slug>/coding --categorical substrate,claim_type --set cells --out <slug>/results/frozen.json
python -m org_frontier.reviews.lib.bibliometrics <slug>/edges --clusters <slug>/clusters.json
```

Each review's `FINDINGS.md` holds the numbers, the reliability figure, and the exact reproduce
commands.
