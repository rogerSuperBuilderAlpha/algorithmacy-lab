# Q114 findings — a principal captures value only by creating it; ownership alone captures nothing

All four hypotheses confirmed. A principal bidirectionally coupled to the mediator captures positive value,
and it does so by enlarging the coordination, with nothing taken from the parties: the total Φ grows from 2
to 3 and every party's value rises. A principal that only monitors the mediator, without being read by it,
captures negative value. Value capture requires value creation, and pure ownership is worthless.

| party | base triad | bidirectional principal | monitor-only principal |
|---|---|---|---|
| worker (E) | 0.333 | 0.417 | 0.167 |
| mediator (M) | 1.333 | 1.750 | 0.500 |
| recipient (R) | 0.333 | 0.417 | 0.167 |
| principal (P) | — | 0.417 | −0.833 |
| total Φ | 2.0 | 3.0 | 0.0 |

| H | Result | Verdict |
|---|--------|---------|
| H1 | a bidirectional principal captures positive value | confirmed (+0.417) |
| H2 | a monitor-only principal captures non-positive value | confirmed (−0.833) |
| H3 | the principal adds value; the parties hold | confirmed |
| H4 | the principal grows the total value (Φ > 2) | confirmed |

From `probe_principal_rent.py`.

## What it says

The principal creates value. When a bidirectionally-coupled principal joins the core, the coordination's Φ
grows from 2 to 3, and every existing party is better off: the worker and the recipient rise from 0.333 to
0.417, the mediator from 1.333 to 1.750 (H3, H4). The principal captures 0.417, a share of a larger whole,
and it takes nothing from the parties, whose absolute values all rise. The cynical reading, that an owner
inserts itself to capture rent at the parties' expense, fails here:
the principal that joins the joint determination adds to it, and the pie it shares is bigger than the one
without it.

Ownership without productive coupling captures nothing, or less. The monitor-only principal, which reads the
mediator but is not read by it, has Shapley value −0.833 (H2). It is outside the core, and because a
read-only element factors the whole system (the Q74 effect), its marginal contribution is negative: adding
it drops the whole-system Φ to zero. A principal that owns the mediator but stays outside its determination
captures no value; it captures negative value, like the spectator of Q111. Participation is value; ownership
alone is empty.

The result refines the platform-power account. Q111 found the mediator captures two-thirds of the value, and
read that as platform power. Q114 locates the source of that power precisely: it is the mediator's
productive position in the joint determination, with ownership as such incidental. A principal who owns the
mediator captures value only by coupling into the determination, and when it does, it grows the value
instead of redistributing it. The rent in Q111 is the structural rent of the productive position, and any
party, principal or not, captures value only by occupying a productive position. Ownership that creates
nothing yields no value.

One redistribution does occur, though not at the parties' expense. The mediator's share falls from
two-thirds to 58% when the principal joins, even as its absolute value rises, because the principal dilutes
the concentration by adding a fourth productive party. The entry of a productive principal grows the total
and spreads the shares slightly toward equality, so the parties gain in both absolute value and relative
share while the mediator gains in absolute value and loses in share. Productive entry is positive-sum and
mildly equalizing.

## Caveats

- **Confirmatory.** All four predictions held; the rent-versus-creation discriminator resolved to creation.
- **One coupling.** The bidirectional principal couples symmetrically (read and read-by the mediator); a
  principal that dominates the mediator, contracting the core to {M, P}, is the displacement case of Finding
  8 and is untested here, and could redistribute instead of adding.
- **Coalition value as subsystem Φ.** As in Q111, the value is the subsystem Φ at the all-ones state. The
  monitor-only principal's negative value is the whole-system reading. In-silico, exact Φ.
