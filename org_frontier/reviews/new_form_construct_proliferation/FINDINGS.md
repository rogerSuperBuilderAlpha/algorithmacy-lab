# Findings — the new organizational form carries at least eighteen names, and the camps rarely read each other

Sixty-seven sources that theorize an alternative to the bureaucratic firm split across eight
well-populated construct labels plus a tail of roughly ten more. A majority define the form by a
positive coordinating mechanism, not by contrast with hierarchy or market. On the citation graph the
label-camps connect through a single meta-organization hub and are otherwise near-isolated: 7,082
external papers cite one camp, and only two cite four.

## Intercoder reliability
| variable | Fleiss' k | agreement | interpretation |
|---|---|---|---|
| label | 0.966 | 97.0% | almost perfect |
| differentia_mode | 0.791 | 90.0% | substantial |
| parent_form | 0.863 | 91.0% | almost perfect |
| claim_type | 0.738 | 81.6% | substantial |

Three independent agent coders applied the fixed codebook blind to one another. The label variable —
the count that H1 turns on — reached k = 0.966, so the proliferation result does not rest on one
reader's judgment.

## Results
| # | Hypothesis | Verdict | Statistic |
|---|---|---|---|
| H1 | The literature uses more than 8 distinct construct labels for overlapping "new form" phenomena | Supported | 8 closed-set labels in active use + a tail of ~10 more (about 18 distinct labels); 9 distinct code values |
| H2 | Most sources define the form by contrast to hierarchy/market rather than by a positive mechanism | Challenged | positive_mechanism 40/67 (60%); by_contrast 27/67 (40%) |
| H3 | Label-camps cite within-camp far more than across (block-diagonal graph) | Qualified | within-cluster 19, cross-cluster 20 links; assembly-spanning: 7,082 span-1 vs 32 span->=3 external citers |

## What the data show

**H1 — supported, and larger than predicted.** Eight of the nine closed-set labels are populated:
`meta_organization` (7), `community` (9), `open_collaboration` (8), `hybrid` (8),
`network_organization` (7), `ecosystem` (7), `platform` (5), `partial_organization` (2); only
`field_or_institution` drew no source. The `other` bin (14 sources) is not residue. It resolves on
inspection to at least ten further named forms: heterarchy, holacracy, adhocracy / non-traditional
organization, fractal social organization, prosocial cooperative, actor-oriented collaboration
architecture, corporate hub, the principle of distributed control, alternative enterprise, and dual
forms of organizing. Counting the closed set and the tail together, the field gives one recurring
object — coordination that is neither a market nor a bureaucratic hierarchy — on the order of eighteen
distinct construct labels. This is the jangle fallacy at the scale of a subfield.

**H2 — challenged.** The prediction was that the field defines the new form negatively. In the
majority it does not. Forty of sixty-seven sources (60%) establish the form by a positive coordinating
mechanism — modularity and design rules for platforms and ecosystems, membership and
organization-of-organizations for meta-organizations, combined institutional logics for hybrids, peer
and commons governance for open collaboration. Twenty-seven (40%) work by contrast to hierarchy,
market, or bureaucracy. The `parent_form` distribution corroborates the reversal: 32 of 67 sources
invoke no explicit hierarchy/market baseline at all (`none`), against 19 `hierarchy`, 12 `market`, 4
`network`. The "beyond markets and hierarchies" framing is common but not dominant.

**H3 — qualified.** The label-to-label seed matrix is not block-diagonal. Cross-camp links (20)
slightly exceed within-camp links (19), so isolation as stated fails. The connectivity is hub-and-spoke
rather than evenly woven. `meta_organization` is the hub: 10 within-camp links plus 15 out to
`ecosystem` (3), `platform` (4), and `other` (7). `platform` has zero within-camp seed links and
reaches the graph only through that hub. The periphery stays siloed: `community`,
`network_organization`, `open_collaboration`, `partial_organization`, and `hybrid` each show at most
one off-diagonal link. The assembly-spanning test reads the wider citing literature the same way —
7,082 external papers cite seeds from a single camp, 321 span two, 30 span three, and 2 span four. The
constructs almost never get assembled by anyone downstream. Proliferation-in-isolation holds for the
periphery and for the reading public; a small meta-organization core integrates a few adjacent labels.

## Limitations
Coders are LLM agents applying a fixed codebook, not trained human raters; k among agent passes is high
but does not substitute for human coding. The corpus is bounded by the Scholar Gateway semantic-search
connector and by English-language indexing; a different seed set would shift the label mix, though not
the fact of proliferation. Semantic Scholar elides outbound references for many publishers, so the
seed-to-seed matrix rests mostly on the inbound-citer channel and undercounts links; three seeds
resolved to error stubs and the two `partial_organization` seeds carried no matched links, so that
camp's isolation is partly a coverage artifact. The label count depends on the codebook's closed set
plus a judgment about what the `other` tail contains; a coarser codebook would report fewer camps and a
finer one more.

## Reproduce
```bash
python3 -m org_frontier.reviews.lib.reliability \
  org_frontier/reviews/new_form_construct_proliferation/coding \
  --categorical label,differentia_mode,parent_form,claim_type \
  --out org_frontier/reviews/new_form_construct_proliferation/results/frozen.json

python3 -m org_frontier.reviews.lib.harvest \
  org_frontier/reviews/new_form_construct_proliferation/seeds.json \
  --out org_frontier/reviews/new_form_construct_proliferation/edges/

python3 -m org_frontier.reviews.lib.bibliometrics \
  org_frontier/reviews/new_form_construct_proliferation/edges \
  --clusters org_frontier/reviews/new_form_construct_proliferation/clusters.json
```
Registered numbers: `ci/reproduce.json` (corpus_n, kappa, H2 split, H3 link counts and spanning).
