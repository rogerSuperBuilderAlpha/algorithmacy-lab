# q163 — findings

Probe 317. Exact Φ on the triad ('W','S','C') with W' = S, C' = S, and S' the mediator. The actor form
uses Q126's interested mediator; the channel form relays W with the same agenda. The channel is Φ = 0
at every k, so the actor surplus Φ(actor) − Φ(channel) equals the actor Φ.

## Order-averaged surplus (mean over all C(4,k) override sets)

| k | sets | surplus (approve) | surplus (deny) |
|---|------|-------------------|----------------|
| 0 | 1    | 2.0000            | 2.0000         |
| 1 | 4    | 0.6250            | 1.5000         |
| 2 | 6    | 0.4167            | 1.0000         |
| 3 | 4    | 0.5000            | 0.5000         |
| 4 | 1    | 0.0000            | 0.0000         |

The approve surplus dips to 0.4167 at k=2 and rises to 0.5000 at k=3 before collapsing at k=4. The deny
surplus falls monotonically.

## Ordered ladder (least-warrant states overridden first)

Approve: Φ = 2.000, 0.500, 0.000, 0.000, 0.000 for k = 0..4; S reads both W,C through k=2, then neither.
Deny: Φ = 2.000, 0.000, 0.000, 0.000, 0.000; S reads both at k=0, neither from k=1. At approve k=1 the
surplus is positive and at k=2 it is zero while S still depends on both parties.

## Verdicts

- H1 SUPPORTED. The approve surplus rises between k=2 and k=3 before collapsing to 0. A monotone
  channel-degradation cannot produce that bump, so the interested actor sits outside the channel/actor
  dichotomy. The deny agenda is monotone; one agenda showing the rise is enough.
- H2 REFUTED. On the ordered ladder S's rule still depends on both W and C (flip-test) while
  whole-system Φ has already dropped to 0 (approve k=2). Reading-the-agenda does not substitute for
  reading-the-parties before the bind collapses; the two do not dissociate on this connectivity test.

## Scope

Exact Φ on a 3-node Boolean model. Evidence about the instrument and the construct. The empirical
reading is on synthetic forms. Output is deterministic and byte-identical across runs.
