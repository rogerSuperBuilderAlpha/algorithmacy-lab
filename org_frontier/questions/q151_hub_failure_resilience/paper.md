# q151 — Hub-failure resilience: redundant mediation protects the triadic verdict, but the cycle is not the reserve

A coordination can be held together by one hub that gates every party. Freeze that hub and the mediation it
supplied is gone. This study asks whether a topology with redundant mediation keeps a triadic verdict where a
single hub loses it, and whether the Φ that survives the freeze is bought by cycle redundancy through the
non-hub nodes.

## The forms

Three topologies at n = 6 share one designated spanning hub at node 0. single_hub gates all five parties
through that one hub. two_hub_backup adds a second independent spanning hub; each party reads either hub
through an OR, so the second hub is a backup that does not depend on the first. ring_hub wires the five
non-hub nodes into a directed copy-ring and lets the hub observe two opposite ring nodes, so the hub watches
the ring while the ring runs on its own. Ablation freezes node 0 to the constant 0.

## What ablation does

The single hub collapses. Intact it binds all six nodes at Φ = 5.0; frozen, every party reads a dead node,
the form factors, and no irreducible complex remains. The verdict falls from triadic to dyadic.

The two redundant forms keep the triadic verdict. The backup-hub form retains Φ = 0.879 after ablation, up
from a near-reducible 0.015 intact: the two interchangeable hubs make the intact form almost factor along the
hub-swap symmetry, and freezing one hub breaks that symmetry so the surviving hub mediates a cleaner triad.
The ring form retains Φ = 2.0 unchanged, because the copy-ring never read the hub.

H1 said redundant mediation would buy verdict resilience. The data support it: the single hub collapses to
dyadic while both redundant forms stay triadic.

H2 said retained Φ would scale with the number of independent cycles through non-hub nodes, naming cycle
redundancy as the reserve. The data reject it. two_hub_backup has zero non-hub cycles and still retains 0.879
Φ, as much resilience as the construction offers short of the ring. A non-hub cycle is not necessary for
retention. The backup form's reserve is the second hub, not a cycle. Retained Φ does not reduce to cycle
count because more than one structure supplies the reserve.

## Why the verdict survives two ways

A hub frozen to a constant stops constraining anything downstream of it. single_hub has nothing else
constraining the parties, so it factors. two_hub_backup keeps a live hub gating the parties through the OR.
ring_hub keeps a closed copy-ring that was never gated by the hub. A redundant mediator and a non-hub cycle
are two distinct reserves, and either one holds the triadic verdict through the loss of the spanning hub.

## Scope

The result is in-silico: synthetic Boolean forms under exact IIT-4.0 Φ at n = 6. "Hub", "backup", "ring",
and "resilience" name graph-and-Φ quantities. No organization is measured, and whether real coordination
gains resilience from redundant mediation this way is not established here. The Φ-to-organization bridge stays
open. The reading on synthetic data is that redundant mediation protects the triadic verdict and that the
protection has more than one source, so a single cycle-counting law does not capture it.
