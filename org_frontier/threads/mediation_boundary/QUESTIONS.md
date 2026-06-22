# Ten research questions from the mediated-or-irreducible paper, ranked

The paper [`essays/mediated_or_irreducible.md`](../../essays/mediated_or_irreducible.md) gives the
conditions under which a mediated triad is irreducible rather than a conduit. Each condition and each
modulating law leaves a sharper question open. Ten are stated below, then ranked, and the top one is
taken twenty steps deep in [`DEEP_DIVE.md`](DEEP_DIVE.md).

## The questions

- **Q1 — parity at scale.** The result that parity determinations generate irreducibility more robustly
  than monotone gates is shown at three nodes. Does it hold at four and five?
- **Q2 — the weakest commit.** What is the most degenerate determination by which a mediator still makes
  a strict-mediated triad irreducible, and how thin is the margin there?
- **Q3 — the structure of the boundary.** Starting from a committing triad, which single-feature
  perturbations preserve irreducibility, which destroy it, and does the boundary have a characterizable
  shape — sharp thresholds, asymmetries, invariants?
- **Q4 — distance to dyad.** Does the Φ value act as a margin, a measure of how far an irreducible triad
  sits from factoring, and what raises or lowers it?
- **Q5 — depth for every function.** Mediation depth preserves irreducibility for one chain. Does it
  preserve it under every determination function, or only some?
- **Q6 — the back-channel threshold.** As a direct worker–counterpart back-channel is strengthened from
  none to full, does irreducibility collapse at a threshold or erode gradually?
- **Q7 — partial substitutability.** Does substitutability collapse irreducibility only at full
  interchangeability, or does a partly-substitutable party already reduce it?
- **Q8 — the excluded proposer.** Under what conditions does the proposing party drop out of the major
  complex while the gates stay in it, the pattern v10 found under heavy review?
- **Q9 — asymmetric reads.** Some functions that read both parties (implication-like) fail to generate
  irreducibility while AND, OR, and parity succeed. What feature of a function's dependence on its inputs
  decides this?
- **Q10 — behavioral discriminability.** Can cross-recurrence separate a conveying mediator from a
  committing one across the corpus, and which measure does it best?

## The ranking

Four criteria, each scored 1–3: **centrality** to the paper's thesis, **tractability** with exact Φ at
small n, **depth** (how richly the question branches for a sequential investigation), and **novelty**
against what the eight structural findings already settle.

| Rank | Q | Centrality | Tractability | Depth | Novelty | Total |
|---|---|---|---|---|---|---|
| 1 | Q3 structure of the boundary | 3 | 3 | 3 | 3 | **12** |
| 2 | Q9 asymmetric reads | 3 | 3 | 3 | 2 | 11 |
| 3 | Q2 the weakest commit | 3 | 3 | 2 | 2 | 10 |
| 4 | Q6 back-channel threshold | 2 | 3 | 2 | 2 | 9 |
| 5 | Q7 partial substitutability | 2 | 3 | 2 | 2 | 9 |
| 6 | Q4 distance to dyad ([taken deep](../margin_to_dyad/THREAD.md)) | 2 | 3 | 2 | 1 | 8 |
| 7 | Q1 parity at scale | 2 | 2 | 1 | 2 | 7 |
| 8 | Q5 depth for every function | 2 | 2 | 1 | 2 | 7 |
| 9 | Q8 the excluded proposer | 2 | 2 | 2 | 1 | 7 |
| 10 | Q10 behavioral discriminability ([taken deep](../behavioral_discriminant/THREAD.md)) | 2 | 2 | 1 | 1 | 6 |

## The choice

**Q3, the structure of the boundary, is taken twenty steps deep.** It is the most central — it is the
paper's own question made operational — and it is the richest for a sequential investigation, because
each perturbation's result chooses the next probe rather than following a fixed list. Walking the
boundary also passes through the territory of Q2, Q6, Q7, and Q9, so the deep dive answers parts of
several questions at once. The chain is in [`DEEP_DIVE.md`](DEEP_DIVE.md), each step's question drawn
from the previous step's result.
