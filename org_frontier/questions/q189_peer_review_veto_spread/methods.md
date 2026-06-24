# q189 — methods

## Machinery

The probe reuses the exact-Φ classifier (`org_frontier.classifier.classifier`) and the probe
library (`org_frontier.probes.lib`) through the disagreement-Φ bridge built in q183
(`org_frontier.qualitative.disagreement_phi`). Φ is not reimplemented. The bridge's
`pivotality_spread` extends the q183 `spread` with an editor-membership flag; `node_pivotal`
reports whether a named party sits in the major complex.

## Parties and accounts

Three labelled parties: Reviewer verdict R, Editor E, Author-facing outcome A. Rules are
per-node Boolean lambdas over the little-endian current-state tuple x.

- GATE (reviewers' account): `[x1, x0&x2, x1]`. The editor reads both R and A; R and A read E.
  The editor gates every integrating coalition. This is the faithful strict-mediation triad.
- CONDUIT (authors' account): `[x2, x0, x0&x1]`. The editor forwards the reviewer verdict
  (E = R); the author reads the reviewers directly (A = R AND E); the reviewers read the author
  (R = A). The triad still integrates, but its core runs R<->A and the editor drops out.

## Pivotality

Editor pivotality is membership in the major complex. A party in the integrated core is in every
integrating coalition, so its removal takes it out of the structure that carries Φ; a party
outside the core is droppable. This is the pivotal/veto-player reading of membership (Probe 11).

## Control

A no-editor two-reviewer pair `[x1, x0]` over labels (R1, R2). With no editor node, editor
pivotality is vacuous and core membership agrees trivially: the pair compared with itself has
core_jaccard = 1 and pivotality_agrees = 1. The probe asserts this before reporting verdicts.

## Instrument control

The probe first reads the faithful triad and checks it returns structure 'triadic' with
max_phi = 2.0, printing `CONTROL ... PASS`.

## Determinism

All RNG is seeded with `numpy.random.default_rng(0)`. The spread is exact, so output is
byte-identical across reruns; this was confirmed on three runs.

## Scope

The accounts are coder-supplied rule sets, not measured worker states. The construct scored is
divergence between two stated accounts of one coordination, validated on the control. Results on
the gate and conduit arms are on synthetic data and do not measure a real editorial process.
