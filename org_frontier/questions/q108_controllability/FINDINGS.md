# Q108 findings — every party is a control node, but the mediator is dominant and the parties are knife-edge

All four hypotheses confirmed. Varying any single party's reads can steer the verdict, so every party is a
control node. But the granularity differs: the mediator has six of sixteen functions that keep the form
triadic, while each outer party has exactly one — its live read. The hub is the robust control point; the
parties hold the triad only on a knife-edge.

| party | triadic settings | total | control node |
|---|---|---|---|
| worker | 1 | 4 | yes |
| counterpart | 1 | 4 | yes |
| mediator | 6 | 16 | yes |

| H | Result | Verdict |
|---|--------|---------|
| H1 | the mediator is a control node | confirmed |
| H2 | each outer party is a control node | confirmed |
| H3 | the mediator is the dominant control node | confirmed (6 vs 1, 1) |
| H4 | the outer parties are knife-edge (exactly one triadic) | confirmed |

From `probe_controllability.py`.

## What it says

The verdict can be steered from any single party. Each party's sweep reaches both verdicts: setting the
worker's read, the counterpart's read, or the mediator's function can make the form triadic or dyadic while
the others stay fixed (H1, H2). There is no party that fixes the verdict regardless of its read; the
coordination is controllable from every position.

The mediator is the dominant control node. Six of its sixteen two-input functions keep the form triadic,
against one of four for each outer party (H3). The hub has the richest space of triad-preserving settings,
so a designer steering toward a triad has the most room at the mediator. This is the control reading of the
mediator's role: it is not only the party that binds the others, but the position from which the triad is
most robustly held and most flexibly reached.

The outer parties are knife-edge. Exactly one of each outer party's four reads keeps the triad — its live
read of the mediator — and the other three break it (H4). A party controls the verdict, but it holds the
triad on a single setting: any read but the live one drops the form to dyadic. This is Finding 3 read as a
control statement. Liveness is one condition, met by one read, so the party that supplies liveness cannot
vary its read without breaking the coordination. The hub tolerates many functions; the spoke tolerates one.

The asymmetry has a design and a security reading. To build or maintain a triad, a designer works most
freely at the mediator, where many settings hold. To break one, an adversary works most easily at a party,
where all but one setting breaks it. Control toward the triad concentrates at the hub; control toward the
dyad is available at every spoke. The coordination is robust to mediator variation and fragile to party
variation, which is why the wave's other results locate building at the parties (Q105) and find the parties
load-bearing (Q104).

## Caveats

- **Confirmatory.** All four predictions held; they follow from the law and Finding 3.
- **One base form.** Control is read from the read-recipient triad; a different starting form could shift
  the counts, though the live-read requirement for the parties is general.
- **Single-party control.** The sweep varies one party at a time; joint control by two parties is untested.
  In-silico, exact verdict.
