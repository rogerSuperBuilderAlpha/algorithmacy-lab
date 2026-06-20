# The bridge demonstration: Φ and CRQA on one model

[`bridge_demo.py`](bridge_demo.py) runs one Boolean coordination model through both instruments. Φ
comes from the model's transition matrix by the lab's exact classifier; CRQA comes from a stochastic
trajectory of the same model, 600 steps after warmup, flip noise 0.08, seed 7. The numbers below
reproduce on that seed.

## Panel A — Φ and CRQA partition the coupling regimes

Three two-party wirings. A persists; the relay makes B copy A's prior state; the mutual wiring swaps
the two.

| wiring | Φ | RR | DET | peak lag | prominence |
|---|---|---|---|---|---|
| independent | 0.000 | 0.498 | 0.976 | none | 0.018 |
| one-way relay A→B | 0.000 | 0.504 | 0.895 | +1 | 0.305 |
| mutual A↔B | 2.000 | 0.503 | 0.639 | +1 | 0.416 |

Two instruments, two different cuts. Φ marks the mutual wiring as irreducible at 2.0 and reads the
relay as no different from the independent pair, both at zero, because a feedforward chain splits.
CRQA reads the relay's direction off the profile: a peak at lag +1 with prominence 0.305, A leading
B by one step, the trace of B's rule reading A's prior state. The independent pair gives a flat
profile, prominence 0.018, no preferred lag. The recurrence rate stays near 0.5 across all three,
the binary chance floor, so it carries no signal here, and determinism runs high wherever both series
are sticky. The peak lag and its prominence are what separate directed coupling from chance.

The complementarity is the result. Φ resolves the mutual-versus-relay distinction that CRQA's lag
blurs, since both show a peak at +1. CRQA resolves the relay-versus-independent distinction that Φ
collapses to zero. Neither instrument partitions the three regimes alone. Together they do.

## Panel B — the committing triad, read off behavior

The triad has P and T each reading the apparatus S, and S reading both. Whole-form Φ is 2.0 and the
classifier calls it triadic. The CRQA readings of the trajectory:

| pair | RR | DET | Lmax | peak lag |
|---|---|---|---|---|
| P, S | 0.553 | 0.719 | 71 | −1 |
| T, S | 0.552 | 0.712 | 71 | −1 |
| P, T | 0.544 | 0.721 | 32 | 0 |

Each party tracks the apparatus in long sustained episodes, a longest diagonal of 71 steps, at a lag
of −1 that has the apparatus leading its readers, which is what P and T reading S's prior state
produces. The two parties track each other in much shorter episodes, a longest diagonal of 32, at lag
zero, with no direct lead-lag because their coupling runs through the common hub instead of between
them. The structural reading and the behavioral reading agree on the same shape: the apparatus is the
hub the parties reach each other through, the veto player of the disintermediation result, now
visible in the recurrence of a run where the model alone left it implicit.

## What this establishes and what it does not

The demonstration shows the bridge is real. One model yields a Φ verdict and a CRQA reading, the two
readings are distinct and informative, and on the committing triad they converge on the disintermediation
structure. It does not yet show how often structure and behavior agree across the corpus, nor how
reliably the profile lag reconstructs a connectivity matrix at scale. Those are the first two items on
the agenda in [README.md](README.md). The trajectory generator adds noise to keep the run exploring,
so the numbers depend on the flip rate and the seed; the qualitative pattern, a directed peak for the
relay, a flat profile for the independent pair, hub-tracking for the triad, holds across seeds, while
the exact rates move.
