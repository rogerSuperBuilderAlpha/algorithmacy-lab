# Q104 findings — the integration concentrates in the binding distinction, and every edge bears load

All four hypotheses confirmed. The read-recipient triad's integration sits in the binding distinction,
which carries φ_d equal to the system Φ, while each party individually carries a quarter of it. And the
triad has no redundancy: removing any one of its four reads collapses the verdict. The cause-effect
structure names what holds the coordination together, and the structure hangs on every edge.

| distinction | φ_d |
|---|---|
| {M} → {E, R} (spanning) | 2.0 |
| {E, R} → {M} (joint) | 2.0 |
| {E} → {M} | 0.5 |
| {R} → {M} | 0.5 |

System Φ = 2.0. Edge knockouts (drop M reads R, M reads E, E reads M, or R reads M) all give dyadic Φ = 0.

| H | Result | Verdict |
|---|--------|---------|
| H1 | the load-bearing distinction is binding, with φ_d = Φ | confirmed |
| H2 | the singleton distinctions carry less than Φ | confirmed |
| H3 | knocking the mediator's read collapses the verdict | confirmed |
| H4 | every edge is load-bearing (no redundancy) | confirmed |

From `probe_load_bearing.py`.

## What it says

The integration concentrates in the binding distinction. The spanning distinction {M} → {E, R} and the
joint distinction {E, R} → {M} each carry φ_d = 2.0, equal to the system Φ, while the singleton
distinctions {E} → {M} and {R} → {M} each carry 0.5 (H1, H2). The binding mechanism — the mediator
distinguishing the parties jointly, and the parties jointly distinguishing the mediator — is the
load-bearing element of the structure. The parties individually account for a quarter of the integration
each; together, as a joint mechanism, they account for all of it. The whole is not the sum of the parts,
and the structure says by how much: 2.0 against 0.5 and 0.5.

The triad has no redundancy. Removing the edge that enables the binding distinction, the mediator's read
of a party, collapses the verdict to dyadic (H3), and so does removing any other read, including the
downstream reads by which the parties see the mediator (H4). Every one of the four edges is load-bearing.
This sharpens Q93, which found the triad one edit from collapse: not one edit but every edit collapses it.
The minimal coordination is a tight loop in which each read is necessary, and there is no edge whose loss
the others absorb.

The two results together give the structure of fragility. The integration is concentrated — it lives in one
binding mechanism, not spread across the parts, and it is unredundant: every edge that builds that
mechanism is required. A coordination that concentrates its integration in a single binding distinction and
hangs that distinction on every edge is maximally fragile, which is the structural reason the verdict toggles
under a single perturbation.

## Caveats

- **Confirmatory.** All four predictions held; they follow from Q99 and Q93.
- **One form.** The read-recipient triad, the minimal mediated coordination. Larger triads with redundant
  paths (a ring, a market) would not have every edge load-bearing, and the no-redundancy result is specific
  to the minimal form. Untested here.
- **Targeted knockouts.** Four named edge removals, recomputing the verdict; a full structural-margin sweep
  is Q93's. In-silico.
