# q166 findings — the addressee becomes the agenda, and the worker drops to referent

Both hypotheses hold. Under a faithful gate the worker binds the held position S: the major
complex is {W, S} with core Φ 2.0, and S reads the worker. As the mediator serves its agenda,
the worker leaves the core and leaves S's read in the same step, and a positive-Φ bind
survives around the agenda's invariant. The held position the worker was binding has become
the agenda itself, and the worker is pushed outside as the referent.

## The ladder (least-warrant override order)

| k | approve: core / coreΦ / S<-W / W in core | deny: core / coreΦ / S<-W / W in core |
|---|---|---|
| 0 | WS / 2.000 / 1 / True  | WS / 2.000 / 1 / True  |
| 1 | WS / 2.000 / 1 / True  | C  / 1.000 / 0 / False |
| 2 | WS / 2.000 / 1 / True  | C  / 1.000 / 0 / False |
| 3 | C  / 1.000 / 0 / False | C  / 1.000 / 0 / False |
| 4 | C  / 1.000 / 0 / False | C  / 1.000 / 0 / False |

cm[2,0] (W reads C) is 0 at every k for both agendas: the worker never reads the counterpart,
so the address into the worker stays one-way throughout.

The transition is a single step. The core flips from {W, S} (worker binds the held position,
Φ 2.0) to {C} (the agenda's self-looping invariant carries the lone surviving bind, Φ 1.0),
and at that same step cm[0,1] drops from 1 to 0. A denying mediator flips at the first
override (k=1), because deny overrides the parties' point of agreement first. An approving
mediator holds the worker-bind through k=2 and flips at k=3.

## Order-averaged decay (mean major-complex Φ over every override set)

| k | sets | mean coreΦ (approve) | mean coreΦ (deny) |
|---|---|---|---|
| 0 | 1 | 2.000 | 2.000 |
| 1 | 4 | 1.750 | 1.750 |
| 2 | 6 | 1.833 | 1.500 |
| 3 | 4 | 1.750 | 1.250 |
| 4 | 1 | 1.000 | 1.000 |

The major-complex Φ never reaches 0: a positive bind survives at every level, ending at 1.0
when the agenda is constant. Deny decays monotonically; approve dips and recovers, the same
parity-pocket pattern Q126 found, because some approve-override sets rebuild a gate that reads
both parties.

## Verdicts

| H | Result | Verdict |
|---|--------|---------|
| H1 | the addressee inverts: W exits the core for an agenda-governed bind as k rises | SUPPORTED |
| H2 | the interested mediator stops reading the worker while a bind survives | SUPPORTED |

## Reading

The worker's "held position" is a property of faithful mediation. A faithful S commits the
joint determination, reads the worker, and binds her into a {W, S} complex with the counterpart
as the read-but-excluded referent. An interested S commits its agenda. It stops reading the
worker, the worker leaves the core, and the surviving bind is carried by the agenda's invariant
(the self-looping C-channel). The theory-of-mind picture inverts: the worker is now the
referent the bound whole reads past, while the agenda is the addressee.

## Limitations

Exact Φ on a three-node Boolean model; evidence about the construct and the instrument, not a
measurement of a real platform. The empirical reading is on synthetic data. "Agenda",
"approve", "deny", and "address" label output values and connectivity, not measured intent. The
counterpart self-loop is the battery's stylization of a referent; a counterpart driven by the
system is a separate model. The faithful baseline is AND; an OR baseline relabels which states
the agendas override and is the natural robustness extension.
