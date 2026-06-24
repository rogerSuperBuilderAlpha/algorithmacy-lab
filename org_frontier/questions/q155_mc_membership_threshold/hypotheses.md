# q155 — Hypotheses

Both hypotheses were fixed before the numbers were computed.

## H1 — a single threshold recovers membership

A single coupling_centrality threshold separates in-core nodes from excluded spectators with
pooled ROC-AUC above 0.65 across the corpus of named multiparty forms and random forms.

Null: AUC at or below 0.5. Behavioral centrality then carries no membership signal.

## H2 — chain relays are the systematic failure

Recovery degrades on relay/chain forms where a tightly-coupled relay node is excluded from the
core. Chain forms contribute the most false positives per node.

Null: errors are uniform across topologies. Chain relays are then not a systematic failure mode.

## Verdicts

- H1: REFUTED. Pooled AUC is 0.649, just under the 0.65 line, against a label-shuffled null of
  0.494. The signal is real and above chance but does not clear the pre-registered bar.
- H2: NOT SUPPORTED. Chain forms produce zero false positives per node. Reciprocal forms are the
  worst false-positive class. The predicted failure mode did not appear; a different one did.
