# q166 methods

## The form

The triad is W (worker), S (system, the held position), C (counterpart, the referent), with
W'=S, C'=C, and S' the gate over the two parties. The counterpart self-loops, which is the
phantom-addressee structure the theory-of-mind battery uses: C is read by S but is not driven
by anything, so the whole three-node system factors (structure verdict "dyadic") while the
major complex over states is the {W, S} subsystem with positive Φ.

The interested version keeps W'=S and C'=C and replaces the faithful gate W∧C with Q126's
`mediator(agenda, k)`: it outputs the agenda a on the k input states where the parties least
warrant a, and commits the faithful AND elsewhere. k=0 is the faithful gate (the battery's T1
control); k=4 ignores the parties. Approve (a=1) overrides first where the fewest parties are
on; deny (a=0) overrides first where the most are on.

The forms come from the shared bridge `org_frontier/cognition/interested_mediator_forms.py`
(`phantom_rules`, `phantom_set_rules`), which extends the theory-of-mind battery to interested
mediators.

## Readers

For each agenda and each k the probe reads:

- the major complex and its Φ, via the mediation-boundary `probe` (the major complex over
  reachable states), reported as `core` and `coreΦ`;
- the whole-system structure verdict, via `org_frontier.probes.lib.verdict`;
- the address connectivity cm[0,1] (S depends on W) and cm[2,0] (W depends on C), via the
  classifier's flip-test `cm_from_rules`, where cm[i,j]=1 iff node j's rule depends on node i.

All readers are exact. No reader is sampled, so the run is deterministic; the RNG is seeded
(`numpy.random.default_rng(0)`) regardless.

## Instrument control

The control validates two known cases before the study runs. The canonical faithful committing
triad `[lambda x:x[1], lambda x:x[0]&x[2], lambda x:x[1]]` reads structure "triadic" with max
Φ 2.0. The faithful phantom form (k=0) reproduces the battery's T1: major complex {W,S}, core
Φ 2.0, S reads W (cm[0,1]=1), the worker never reads C (cm[2,0]=0). Both must hold or the run
stops.

## Robustness

An order-averaged sweep means the major-complex Φ over every choice of which k states the
agenda overrides (C(4,k) sets per level), so the decay is not an artifact of the
least-warrant override order.

## Run

```
python -m org_frontier.questions.q166_phantom_addressee_displaced.probe_phantom_addressee_displaced
```
