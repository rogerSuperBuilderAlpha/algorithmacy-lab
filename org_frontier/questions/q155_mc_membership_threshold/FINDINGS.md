# q155 — Findings

Coupling centrality carries a real but weak signal for major-complex membership. Pooled over 361
nodes from 89 synthetic forms, the ROC-AUC is 0.649 against a label-shuffled null of 0.494. The
signal is above chance and below the pre-registered 0.65 bar, so H1 is refuted on its own terms.

The predicted failure class did not appear. Chain forms produce zero false positives per node:
their relay nodes are excluded from the core and also score low on centrality, so they are correctly
called spectators. The worst false-positive class is reciprocal forms, where mutually coupled
spectators score high enough to cross the threshold. H2 is not supported.

## Pooled and per-topology results

| scope        | nodes | core | spec | AUC   | FP/node |
|--------------|------:|-----:|-----:|------:|--------:|
| pooled       |   361 |  122 |  239 | 0.649 |       — |
| star         |    37 |   16 |   21 | 0.731 |   0.243 |
| chain        |    32 |    2 |   30 | 0.367 |   0.000 |
| reciprocal   |   205 |   85 |  120 | 0.561 |   0.244 |
| mediator     |    37 |    7 |   30 | 0.729 |   0.189 |
| other        |    50 |   12 |   38 | 0.604 |   0.060 |

Pooled best threshold (>=) 0.2281, balanced accuracy 0.638. Null AUC 0.494.

Star and mediator forms are where centrality recovers membership best (AUC ~0.73). Reciprocal forms
drag the pooled number down: they are the bulk of the corpus and their AUC is near chance.

## Verdicts

- H1 (pooled AUC > 0.65): REFUTED. AUC 0.649, null 0.494.
- H2 (chain is the systematic false-positive class): NOT SUPPORTED. Chain FP/node 0.000; reciprocal
  is the worst at 0.244.

## Scope

All forms are synthetic Boolean coordination models. The result is an in-silico reading and does not
measure any field organization.
