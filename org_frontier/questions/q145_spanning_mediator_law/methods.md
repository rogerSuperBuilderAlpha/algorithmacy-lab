# q145 — methods

## Form

`single_hub(n, f)` builds an n-node Boolean coordination form. Node 0 is the hub (mediator);
nodes 1..n-1 are the parties. The hub spans the first k = round(f·(n-1)) parties: it fires on
the conjunction of those parties, and each spanned party reads the hub back. Each unspanned
party is an isolated self-loop, so it neither reads nor is read by the hub. The parties never
read each other, so without the hub the set is unconnected.

This is the conjunctive analogue of the worker-system-counterpart triad, scaled to one hub
and many parties. At k = n-1 the hub spans every party (f = 1). At k = 0 the hub reads
nothing and every party is isolated (f = 0).

## Measurement

`major_complex(rules, labels)` returns the core (the node set of the maximal complex) and its
Φ, taken over reachable states at the integrating state. The sweep runs n = 4, 5, 6 and, for
each n, every integer span k from 0 to n-1, recording core size, Φ, and which parties land in
the core.

## Controls

The instrument control is the faithful triad `[x1, x0&x2, x1]` with labels (W, S, C). It reads
structure `triadic`, max Φ_MIP 2.0, core (W, S, C), Φ 2.0. The probe asserts this before the
sweep and prints `CONTROL ... PASS`. The two endpoints of the sweep serve as design controls:
full span (f = 1) and disconnected parties (f = 0).

## Determinism

RNG is seeded with `numpy.random.default_rng(0)`. The major-complex search is otherwise
deterministic. Output is byte-identical across repeated runs.

## Verdict rule

H1 is read from four computed checks: full span gives core size n; Φ at full span equals n-1;
partial span gives core size k+1 holding exactly the hub and its spanned parties; partial span
excludes every unspanned party. H2 is read from whether Φ at a shared fraction (f = 1, sampled
at all three n; f = 0 likewise) takes one value across n.

## Scope

Synthetic forms only. The result describes the model's behavior under one design parameter and
does not claim that any measured coordination form has this topology.
