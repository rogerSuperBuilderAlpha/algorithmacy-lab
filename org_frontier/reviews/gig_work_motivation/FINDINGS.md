# Findings — gig/platform-work reviews motivate themselves by gap-spotting, nine times in ten

Across 49 review, agenda-setting, and bibliometric-review articles on gig and platform work, 44 (90%)
justify themselves by gap-spotting — naming an under-studied topic, a fragmented literature, or a
missing framework. Four (8%) problematize: they build the contribution on challenging an assumption the
field takes for granted. One is neither. The gap-spotting default that Sandberg and Alvesson (2011)
describe for management reviews holds, sharply, in this literature.

## Intercoder reliability
| variable | Fleiss' κ | agreement | interpretation |
|---|---|---|---|
| motivation_mode | 0.721 | 93.2% | substantial |
| assumption_targeted | 0.916 | 98.6% | almost perfect |

Three independent agent coders, blind to one another, coded each source from title + abstract. The κ
discharges the single-coder objection: the 90/8/2 split is not one reader's idiosyncratic reading. The
gap-spotting vs. problematization call is the harder one (κ = 0.72), which is expected — the two shade
into each other when a review both maps gaps and complicates a framing.

## Results
| # | Hypothesis | Verdict | Statistic |
|---|---|---|---|
| H1 | Gap-spotting dominates | **Supported** | gap_spotting 44/49 = 90%; problematization 4/49 = 8% |
| H2 | Problematization rises over time | **Challenged** | early (<2024) 13% -> late (>=2024) 6% problematization |
| H3 | Problematizers cited more per year | **Supported (fragile)** | median cites/yr 28.6 vs 3.7; Mann-Whitney U=27, z=-2.29, p=0.022 |

## What the data revise

**H2 runs backward.** The prediction was a modest rise in problematization as the field matures.
Instead the problematization share falls: 2 of 15 early reviews (13%) vs 2 of 34 recent reviews (6%).
The mechanism is visible in the corpus. The recent surge in gig-work reviews is dominated by
bibliometric and PRISMA systematic reviews — a genre whose entire method is gap-spotting: count the
literature, cluster it, list the gaps, call for future work. As the review count grew after 2023, the
mix tilted further toward gap-spotting, not away from it. Maturity brought more cataloguing, not more
contesting.

**H3 holds but rests on four cases.** Problematizing reviews are cited far more per year (median 28.6
vs 3.7; means 41.3 vs 8.2), and the Mann-Whitney test clears p < 0.05. But there are only four
problematizers, and the result is carried by two prominent agenda pieces — Duggan et al. (2019), which
disputes the "problematic aggregation" of gig work (~104 cites/yr), and Keegan & Meijerink (2025), an
Annual Review chapter challenging the clean employment/freelance boundary (~37 cites/yr). Read this as a
real association consistent with Sandberg and Alvesson's claim that problematization is the
higher-impact move, not as a powered test. The direction is clear; the estimate is not.

## Limitations
- **Agent, not human, coders.** Three LLM agents applied the codebook. κ is high, but they may share
  systematic reading biases a panel of trained humans would not.
- **Title + abstract only.** Motivation was coded from the abstract, which compresses the framing a
  full introduction carries. A review can problematize in its introduction while its abstract reads as
  gap-spotting; such cases are undercounted, always in the direction of inflating gap-spotting.
- **Connector-bounded corpus.** Discovery ran through two semantic-search connectors; a source outside
  their index is outside the corpus. DOIs were not uniformly resolved for connector-sourced items.
- **Citation snapshot, small problematizer cell.** Citations are a single July-2026 snapshot,
  uncorrected for field. The H3 cell for problematization is n = 4; two old, highly cited pieces
  dominate it.
- **Genre confound in H2.** The rising share of bibliometric/PRISMA reviews mechanically raises
  gap-spotting; H2's reversal is partly a shift in review genre, not only in scholarly posture.

## Reproduce
```bash
cd /Users/ludwitt/iit-playground/pyphi-experiments
python3 -m org_frontier.reviews.lib.reliability \
    org_frontier/reviews/gig_work_motivation/coding \
    --categorical motivation_mode,assumption_targeted \
    --out org_frontier/reviews/gig_work_motivation/results/frozen.json
python3 -m org_frontier.reviews.gig_work_motivation.run
```
Registered numbers: N=49; kappa(motivation_mode)=0.721, kappa(assumption_targeted)=0.916; gap_spotting
90%; H3 Mann-Whitney p=0.022. See `results/summary.json`.
