# Two-triad shared-member merger — findings

**Verdict: WIN — the shared role decides merger.** Under AND coupling, a **shared
mediator** merges two conjunctive triads into one major complex spanning both
exclusive leaf pairs (core = all five nodes, **Φ = 4.0**). A **shared counterpart**
or **shared worker** does **not** merge (cores stay local at Φ = 2.0), matching
q210 and extending q212's leaf symmetry to shared-member architectures.

In-silico; exact IIT-4.0 Φ; n=5. Hypotheses fixed in `hypotheses.md` before
computing. Extends q210–q212 (agenda #16). Residual/cascade arc closed
(`foundations/RESIDUAL_AND_CASCADE.md`); not reopened.

## Already known

| prior | result |
|---|---|
| q210 shared counterpart × none/AND/OR | never merges; AND whole Φ_MIP=2.0, core local Φ=2.0 |
| q211 direct S↔S channel (no shared member) | AND merges, core Φ=3.0 |
| q212 channel location | only mediator–mediator placement merges |

## Census (3 roles × 3 bridges)

| architecture | bridge | whole Φ_MIP | major complex | core Φ | spans both |
|---|---|---|---|---:|---|
| shared counterpart | none | 0.0 | (W1,S1,C) | 2.0 | no |
| shared counterpart | AND | 2.0 | (W2,S2) | 2.0 | **no** |
| shared counterpart | OR | 0.0 | (W1,S1,C) | 2.0 | no |
| shared mediator | none | 0.0 | (W1,C1,S) | 2.0 | no |
| **shared mediator** | **AND** | **4.0** | **(W1,C1,W2,C2,S)** | **4.0** | **yes** |
| shared mediator | OR | 0.0 | () | — | no |
| shared worker | none | 0.0 | (S1,C1,W) | 2.0 | no |
| shared worker | AND | 2.0 | (S2,C2) | 2.0 | **no** |
| shared worker | OR | 0.0 | (S1,C1,W) | 2.0 | no |

## Hypotheses

| hypothesis | result | detail |
|---|---|---|
| H1 control + q210 none replicate | **SUPPORTED** | |
| H2 shared-C/AND does not merge | **SUPPORTED** | replicates q210 |
| H3 shared-S/AND merges | **SUPPORTED** | full five-node core |
| H4 shared-S/AND core Φ > 2.0 | **SUPPORTED** | Φ=4.0 |
| H5 shared-W/AND does not merge | **SUPPORTED** | leaf symmetry with C |
| H6 role decides merger under AND | **SUPPORTED** | mediator yes; leaves no |

## Reading

Sharing a member is not enough. Merger under AND requires sharing the
**integrating** role — the mediator that reads both leaves. Sharing a leaf
(worker or counterpart) reproduces q210's non-merge: the whole system can be
irreducible (Φ_MIP=2.0) while the major complex stays inside one side. A shared
mediator under AND is stronger than q211's direct channel: the core is the
entire five-node system at Φ=4.0 (vs q211's four-node Φ=3.0 with two separate
mediators). Shared-mediator OR factors and yields no irreducible complex in
this construction — the combination rule still matters.

## Best next experiment

**Beyond-binary state** on the same shared-mediator AND architecture (or a
minimal conjunctive triad): does the merge / Φ=4.0 pattern survive when nodes
take ternary alphabets, or does multi-valued state split the complex? Agenda
structural queue alternative if compute-bound: hierarchy of mediators (#15).

## Reproduce

```
python org_frontier/studies/two_triad_shared_member/analyze_shared_member.py
```
