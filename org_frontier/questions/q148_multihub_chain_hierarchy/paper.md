# q148 — Hierarchy depth and the hub-seam: where a chain of hubs stops integrating

A coordination can be held together by a hub that gates every party. Stack such hubs into a hierarchy and the
question is whether integration survives the stacking. This study builds a chain of gating hubs and reads how
far the core reaches.

## The form

Each hub gates a party group. Hub 0 fires when its group is all on. Hub k fires when the upstream hub and its
own group are all on. Each party reads its hub. The hubs run one way, H0 -> H1 -> ... -> H{L-1}, which is the
directed version of the mutually-coupled two-hub. Group size is fixed at one party per hub, so the chains
tested are L = 2, 3, 4 at n = 4, 6, 8.

## What the core does

The major complex is the first hub and its party, at every depth. It holds one group and drops the rest. The
whole-system Φ at the all-ones state is zero: nothing past the first hub-and-party loop is irreducible. A
control built to span — one hub that ANDs all parties, every party reading it — binds all four nodes into one
complex at n = 4 (Φ = 3.000), so the chain's failure to span is the chain's, not the instrument's. The
all-spanning hub is fully integrated and its maximal complex grows costly fast, so the control is read at that
tractable size and not pushed to n = 6 or 8.

H1 said depth would cap the integrable group size, with terminal groups dropping at the weakest seam. The
data support the direction and sharpen it: the cap is not graded. The core never reaches past the first group,
even at L = 2. Hierarchy depth does not slowly erode the span; the first downstream seam already cuts it.

H2 said the break would fall at a hub seam rather than inside a group. Confirmed. The surviving core is a whole
group, hub and party together, and the break sits at the H0–H1 link. The hub-to-hub gate is the bottleneck.

## Why the seam cuts

A downstream hub computes an AND of the upstream hub and its own group. The AND gate fixes the upstream cause
from a downstream-on state but does not let the downstream side constrain the upstream side back. Irreducibility
needs a two-way constraint across the cut. The feedforward gate gives a one-way one. Only the first hub and its
own party constrain each other both ways, so only that group integrates.

## Scope

The result is in-silico: synthetic Boolean forms under exact IIT-4.0 Φ at group size one. The terms "core",
"span", and "seam" name graph-and-Φ quantities. No organization is measured, and whether real hierarchies
fragment this way is not established here. The Φ-to-organization bridge stays open. The reading on synthetic
data is that a one-way hierarchy of gates integrates only its top loop, and the place it stops is the hub seam.
