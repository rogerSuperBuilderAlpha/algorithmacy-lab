# q165 — methods

## The model

The triad W (worker), S (system/mediator), C (counterpart). The parties read the system: W' and C'
take S. The system commits a gate over the two parties' inputs. The faithful gate is the joint
determination S = W ∧ C — the canonical strict-mediation actor (triadic, Φ = 2.0 at full fidelity), the
control. The interested gate is Q126's mediator(agenda, k): the system outputs its agenda a on the k
input states where the parties least warrant a, and commits the faithful AND elsewhere. k = 0 is
faithful; k = 1 imposes the agenda on one state.

## H1 — the read-fidelity compression curve

battery_embodiment's noisy() sweep degrades the parties' read of the system. At fidelity q the parties'
next state is q·S + (1−q)·0.5: at q = 1 they read S exactly, and as q falls their read mixes in a fair
coin. The system's commit gate is untouched. Φ is the maximum exact IIT-4.0 Φ over the system's states
(the lab's sphi3 reader). The curve Φ(q) is read on a fixed descending grid q ∈ {1.0, 0.9, 0.75, 0.6,
0.5} for three gates: the faithful AND (k = 0), an interested approve mediator (k = 1), and an interested
deny mediator (k = 1). H1 holds when each interested curve sits strictly below the faithful curve at
every q < 1.

## H2 — nuance eviction, at full fidelity

battery_embodiment's reads_n form adds a worker nuance bit N: the system commits S = W ∧ C ∧ N, so N
decides the output in the one state where both parties warrant a commit (W = C = 1). Under that form N
joins the major complex. The interested nuanced gate imposes the agenda on exactly that nuance-bearing
state — the state where N would otherwise have decided — and commits faithful AND ∧ N elsewhere. The
measure is major-complex membership of N (the irreducible core, max over reachable states) and whether
the system's rule still depends on N (connectivity-matrix flip test, cm[N, S]). Both are read at q = 1,
so any eviction is the agenda's doing and not the read-noise. Both agendas run.

## Reuse

The forms live in the shared bridge `org_frontier/cognition/interested_mediator_forms.py`: `fidelity_curve`
and `noisy_phi` wrap battery_embodiment's noisy() sweep around Q126's mediator(agenda, k); `reads_n_rules`,
`interested_n_rules`, and `reads_nuance` build the N-bit forms and the dependency test. Φ comes from
`org_frontier.probes.lib` (verdict, major_complex). No Φ is reimplemented.

## Reproduce

```
python -m org_frontier.questions.q165_intent_compression_into_agenda.probe_intent_compression_into_agenda
```

Output is saved in [`results/output.txt`](results/output.txt). The forms are deterministic Boolean gates
and any RNG is seeded with 0; three runs are byte-identical. The run takes a few seconds (three- and
four-node models).
