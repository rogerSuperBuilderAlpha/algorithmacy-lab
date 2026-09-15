# Serres — findings

Serres's one-way arrow is not a relation the instrument can see: a parasite reading a producer who does not
read back forms no complex (H1 refuted, as the lab predicted; exchange binds at Φ = 2). His theorem holds:
the chain farmer → tax farmer → rat has no complex, and the noise the feast provokes and that stops the feast
creates one — {R, N} at 2.000, with the producer and the tax farmer outside it (H2 confirmed). The
quasi-object holds: the token passing round three players makes them one complex at 2.000, and stopped it
makes none (H5 confirmed). Two refutations carry the paper's findings. The excluded third (H3): noise from a
coin does not lower the pair's Φ — it annihilates the pair, at every noise rate including zero, because
IIT 4.0's cause side infers a background input's past from the present and a coin's past leaves no trace;
and the system's own noise (N' = A ∧ B) is not a member of the complex, which stays {A, B} at 2.000. The
last position (H4): in the cascade where every level ejects the one above, the complex is {T, R, N} — the
whole cascade except the producer — and the shares invert Serres: the producer F, outside the complex,
costs 2.000 to delete; the noise N at the last position, inside it, costs nothing. In the single-level form
every term costs 2.000. Membership and indispensability come apart, and the one who is excluded and
indispensable is not the noise but the one who produces.

## Verdicts

| H | claim | verdict | key numbers |
|---|---|---|---|
| H1 | the one-way arrow is the atom of relation | **REFUTED** | arrow: no complex, Φ 0; exchange 2.000 |
| H2 | noise gives rise to a new system | **CONFIRMED** | chain: none; chain + noise: {R, N} 2.000, F and T out |
| H3 | the excluded third, included | **REFUTED** | coin noise: no complex at ε = 0, .05, .1, .25, .4, .5 (post-hoc sweep); own noise: core {A, B} 2.000, N out |
| H4 | the last position wins | **REFUTED** | cascade core {T, R, N} 2.000; shares F 2.000, T 2.000, R 2.000, N 0 |
| H5 | the quasi-object weaves the "we" | **CONFIRMED** | passing ring {A, B, C} 2.000; stopped: none |

Instrument control passed in all five probes (Φ = 2.000000, core {A, M, B}; stochastic path 2.000000 in H3).

## Caveats

- H3's exogenous result is a property of the instrument's cause side (PyPhi's backward TPM weights a
  background unit's past states by their probability given the present). A channel that an outside unit
  *could* flip carries no cause information about its sender, whether or not the flip ever happens. This
  is reported as found; it is not a lowering of Φ and it does not depend on ε.
- One rendering of each claim. Producers are constants; a held producer would be a one-node complex.
- "The cascade collapses when P1 = P4" was not tested; the ring of H5 is the closed chain, and it binds.
- In-silico; two- to four-node forms. No fable, feast, or channel is measured.

## Reproduce

```
~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.serres.probe_serres_arrow
~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.serres.probe_serres_theorem
~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.serres.probe_serres_third
~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.serres.probe_serres_cascade
~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.serres.probe_serres_quasiobject
```

Post-hoc (noise sweep, chain_noise shares): `results/posthoc_noise_sweep.json`.
