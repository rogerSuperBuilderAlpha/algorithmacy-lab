# q155 — Review

## Pre-registration

Both hypotheses and the 0.65 AUC bar were fixed in the probe docstring and hypotheses.md before the
numbers were read. The verdicts follow the computed AUC and false-positive rates with no adjustment
of the bar after the fact. H1 lands at 0.649, just under 0.65; the refutation is reported as it fell.

## Instrument control

The control validates the membership read (faithful triad, triadic, max_phi 2.0, full three-node
core), the AUC routine (1.0 separable, 0.5 tied), and a label-shuffled null near 0.5. The run prints
CONTROL ... PASS only when all hold. The control passed.

## Determinism

The random corpus is drawn from a fixed seed and trajectory seeds are fixed per form, with no use of
the non-deterministic builtin hash. Three runs, including one under PYTHONHASHSEED=99, produced
byte-identical output.

## Threats to validity

- Topology classes are coarse and assigned by a heuristic on the connectivity matrix. Reciprocal
  dominates the corpus (205 of 361 nodes), so the pooled AUC is largely the reciprocal AUC. A corpus
  balanced across topologies would report a higher pooled number; the per-topology table is the more
  informative read.
- coupling_centrality is symmetric in source and sink, so it cannot distinguish a directed member
  from a mutually coupled spectator. This is the mechanism behind the reciprocal failure and a target
  for a follow-up feature.
- The corpus is small at the named end (9 forms) and the random forms cap at 5 nodes. Larger forms
  are not tested.

## Scope

In-silico throughout. The study reads behavioral centrality against exact-Φ membership on synthetic
Boolean forms and makes no field measurement.
