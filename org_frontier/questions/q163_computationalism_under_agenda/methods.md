# q163 — methods

## Forms

The triad is ('W','S','C') with W' = S, C' = S, and S' the mediator of the two parties. The shared
module `org_frontier/cognition/interested_mediator_forms.py` builds two families at each interestedness
level k = 0..4 and each agenda a ∈ {1 = approve, 0 = deny}:

- Actor form: S' = mediator(a, k) from Q126. The agenda overrides the k states where the parties least
  warrant it; the faithful gate S = W ∧ C holds elsewhere. k = 0 is the faithful actor from
  battery_computationalism.
- Channel form: S relays W and imposes the same agenda on the W-values least warranting it, never
  reading C. This is the channel counterpart of the actor at the same level of interest. There are two
  W-states, so k caps at 2 for the channel.

## Measures

For each (agenda, k): `verdict().max_phi` for the actor form and the channel form; the actor surplus
Φ(actor) − Φ(channel); `parties_read_by_S(actor)`, the connectivity-matrix flip-test for whether S's
rule depends on W and on C; and `major_complex(actor)` for the core. Φ and the major complex come from
`org_frontier/probes/lib.py`; the verdict comes from the classifier.

Two ladder readings are reported. The ordered ladder follows Q126: the least-warrant states are
overridden first. The order-averaged ladder takes the mean actor Φ over all C(4,k) choices of which k
states the agenda overrides, the order-independent reading. The channel is Φ = 0 at every k, so the
actor surplus equals the actor Φ in both readings.

## Hypothesis tests

H1 holds when the order-averaged surplus rises at some step (a strict increase between consecutive k)
and ends at 0. A monotone-decreasing collapse has no strict increase and fails the test. A single
agenda showing the rise makes the interested actor a distinct object, so H1 is the disjunction over
the two agendas.

H2 holds when, at every k > 0 with actor Φ still positive, S already reads fewer than both parties on
the flip-test, and at least one such k exists. The null holds when S still depends on both W and C
while Φ has already reached 0.

## Determinism

The forms and exact Φ are deterministic. A `numpy.random.default_rng(0)` is fixed for reproducibility
hygiene though no random draw enters the computation. The instrument control checks that the faithful
actor reads triadic with Φ = 2.0 and that the matched channel reads Φ = 0. Output is byte-identical
across runs.

## Scope

Exact Φ on a 3-node Boolean model. The result is evidence about the instrument and the construct, not
a measurement of a platform. The empirical reading is on synthetic forms.
