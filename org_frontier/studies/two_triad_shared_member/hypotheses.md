# two_triad_shared_member — hypotheses (fixed before computing)

**Question (agenda #16).** When two separately-triadic groups share one member, under what
couplings do they merge into a single major complex versus stay two cores?

**Already known (cited, not reopened).**
- **q210:** shared *counterpart* + bridge none/AND/OR — **never merges**; AND makes whole-system
  Φ_MIP=2.0 but core stays a local pair/triad at Φ=2.0.
- **q211:** *no* shared member; direct mediator↔mediator channel — **AND merges** (spans both,
  core Φ=3.0); OR spans mediators at Φ=2.0.
- **q212:** channel *location* — only mediator–mediator placement merges; worker–worker and
  counterpart–counterpart stay local (leaf symmetry).

**Gap.** q210 fixed the shared role as counterpart. This census varies the shared role
(worker / mediator / counterpart) under the same bridge family, asking whether merger depends
on *which* role is shared — the natural completion of #16 after q210–q212.

**Universe.** Exact IIT-4.0 Φ, conjunctive leaves, n=5. Three architectures × three bridges
(none / AND / OR). Residual/cascade arc cited only as closed tooling context
(`foundations/RESIDUAL_AND_CASCADE.md`); not reopened.

## Architectures

1. **Shared counterpart C** (q210 replicate) — labels `(W1,S1,W2,S2,C)`;
   `S1'=W1∧C`, `S2'=W2∧C`, `W*'=S*`, `C'=bridge(S1,S2)`.
2. **Shared mediator S** — labels `(W1,C1,W2,C2,S)`; leaves `W*'=S`, `C*'=S`;
   `S'=bridge(W1∧C1, W2∧C2)`.
3. **Shared worker W** — labels `(S1,C1,S2,C2,W)`; `S*'=W∧C*`, `C*'=S*`,
   `W'=bridge(S1,S2)`.

**Bridge:** none = first side only; AND = both sides; OR = either side.
**Span:** major complex intersects both exclusive pairs of the architecture
(shared-C: `{W1,S1}` and `{W2,S2}`; shared-S: `{W1,C1}` and `{W2,C2}`;
shared-W: `{S1,C1}` and `{S2,C2}`).

## H1 — instrument + q210 replicate

Single triad F0 is triadic Φ_MIP=2.0. Shared-counterpart / none matches q210:
whole-system dyadic (Φ_MIP=0), core Φ=2.0, does not span.

## H2 — shared counterpart AND does not merge (q210)

Under shared-C / AND, `spans_both` is false (replicates q210 H2 REFUTED).

## H3 — shared mediator AND merges

Under shared-S / AND, `spans_both` is true.

## H4 — shared-mediator AND is super-additive

Under shared-S / AND, core Φ > 2.0.

## H5 — shared worker mirrors shared counterpart (leaf symmetry)

Under shared-W / AND, `spans_both` is false — same qualitative non-merge as shared-C / AND
(q212 leaf symmetry extended to shared-member architectures).

## H6 — shared role decides merger under AND

Among the three AND cells, at least one merges (expected: mediator) and at least one of
{worker, counterpart} does not. Null: all three AND cells merge, or none merge.
