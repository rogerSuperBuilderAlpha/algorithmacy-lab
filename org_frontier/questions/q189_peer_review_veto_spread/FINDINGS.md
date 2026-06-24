# q189 — findings

The gate and conduit accounts read the same whole-system verdict (both triadic, max_phi = 2.0,
phi_gap = 0), so the spread does not separate them on Φ magnitude or on the structure label. The
disagreement surfaces instead in core membership and in the editor-pivotality flag. Under the
reviewers' gate account the editor is in the core; under the authors' conduit account the
integrated core runs reviewer-to-author and the editor drops out.

| quantity | gate account | conduit account |
|---|---|---|
| structure | triadic | triadic |
| max_phi | 2.000000 | 2.000000 |
| major complex | (R, E, A) | (R, A) |
| editor in core (pivotal) | True | False |

| spread component | value |
|---|---|
| verdict_agreement | 1 |
| phi_gap | 0.000000 |
| core_jaccard | 0.666667 |
| pivotality_agrees | 0 |

Control (no-editor two-reviewer pair): core (R1, R2), core_jaccard 1.000000, editor pivotality
False under both accounts, pivotality_agrees 1. Editor pivotality is vacuous and core membership
agrees trivially.

## Verdicts

- H1 gate/conduit spread puts editor core membership in dispute (core_jaccard < 1): SUPPORTED.
  The editor is core under the gate account and droppable under the conduit account; core_jaccard
  = 0.667.
- H2 added editor-pivotality flag disagrees across accounts (veto-player claim): CONFIRMED. The
  flag reads True under the gate account and False under the conduit account, so
  pivotality_agrees = 0.

## Note

A whole-system verdict that agrees (phi_gap = 0) can hide a membership dispute. Here the spread's
verdict_agreement and phi_gap components miss the disagreement; only core_jaccard and the added
pivotality flag register it. The editor-pivotality flag is the component that carries the
veto-player claim.

## Scope

Synthetic coder-supplied accounts, not measured worker states. The gate and conduit results are
on synthetic rule sets. The construct is divergence between two stated accounts, validated on the
control; it is not a measurement of a real editorial process.
