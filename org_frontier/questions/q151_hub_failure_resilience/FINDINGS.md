# q151 — Findings

A single hub loses the triadic verdict when it is frozen. A backup hub and a non-hub ring each keep it. The
Φ that survives ablation does not track the non-hub cycle count: a backup hub with zero non-hub cycles
retains substantial Φ, so a redundant mediator supplies the reserve on its own.

## Result (synthetic, exact Φ; n = 6)

| topology | non-hub cycles | Φ intact | verdict | Φ ablated | verdict | Φ retained |
|---|---|---|---|---|---|---|
| single_hub | 0 | 5.000 | triadic | 0.000 | dyadic | 0.000 |
| two_hub_backup | 0 | 0.015 | triadic | 0.879 | triadic | 0.879 |
| ring_hub | 1 | 2.000 | triadic | 2.000 | triadic | 2.000 |

Control: every unablated topology reads triadic, so the resilience contrast is defined.

Cores. single_hub spans all six nodes intact and has no complex after ablation. two_hub_backup holds a small
core intact (one surviving hub and one party) and a larger one after ablation, as freezing one hub breaks the
hub-swap symmetry that made the intact form nearly reducible. ring_hub holds the five-node ring intact and
unchanged after ablation, because the ring never read the hub.

## Verdicts

- H1 (redundant mediation buys verdict resilience): SUPPORTED. The single hub collapses to dyadic on
  ablation while the backup-hub and ring forms stay triadic. The null — the single hub staying triadic, or
  the redundant forms collapsing equally — is rejected.
- H2 (retained Φ scales with non-hub cycle count): NOT SUPPORTED. two_hub_backup has zero non-hub cycles yet
  retains 0.879 Φ. A non-hub cycle is not necessary for retention. The reserve in the backup form is the
  second hub, not a cycle, so the cycle-count account does not hold.

## Why

Ablating the single hub leaves every party reading a dead node, so the whole form factors and Φ falls to
zero. The backup hub survives because the parties read (hub0 OR hub1): freezing hub0 leaves hub1 gating the
parties, and breaking the symmetry between the two interchangeable hubs raises Φ from 0.015 to 0.879. The
ring survives because the copy-ring is a closed cycle that never depended on the hub. Two different reserves,
a redundant mediator and a non-hub cycle, both protect the verdict, which is why retained Φ does not reduce
to cycle count.

## Scope

Synthetic Boolean forms under exact IIT-4.0 Φ at n = 6. "Hub", "backup", "ring", and "resilience" are
graph-and-Φ quantities, not measured organizations. Whether real coordination structures gain resilience
from redundant mediation this way is not shown here; the Φ-to-organization bridge is open. The reading on
synthetic data is that redundant mediation protects the triadic verdict, and more than one structure supplies
that protection.
