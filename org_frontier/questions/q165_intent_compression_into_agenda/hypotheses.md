# q165 — hypotheses (fixed before computing)

battery_embodiment models the worker's intent as something the system compresses when the parties read
the system at reduced fidelity q. The mediator there is faithful: S commits the joint determination
S = W ∧ C, committing only when both parties warrant it. q165 gives the mediator an agenda. It holds a
preferred output a (approve a = 1, deny a = 0) and imposes it on the k input states where the parties
least warrant a, committing the faithful AND elsewhere — Q126's mediator(agenda, k). The question is how
self-interest changes the way compression sheds the worker's meaning.

- **H1.** The compression curve Φ(q) for an interested mediator (k ≥ 1) lies strictly below the faithful
  curve at every fidelity q < 1, so self-interest steepens the embodiment loss.
  - **Null.** The interested and faithful Φ(q) curves coincide — interest does not change how
    compression sheds meaning.

- **H2.** A nuance bit N that the faithful mediator carries into the core (the reads_n form, S = W ∧ C ∧ N)
  is dropped from the core once the mediator imposes its agenda on the state where N would have mattered,
  so interest evicts nuance independently of read-fidelity.
  - **Null.** N stays in the core under the interested mediator exactly as under the faithful one.

Two agendas run for each arm (approve, deny). H1 sweeps a fixed descending fidelity grid; H2 is read at
full fidelity (q = 1) so the eviction it reports cannot be attributed to read-noise.

The labels name output values and a worker input bit, not measured intent: "agenda", "approve", "deny",
and "nuance" describe what the mediator commits and which worker bit it reads. The result is exact Φ on
small Boolean models, evidence about the construct and the instrument. The empirical arm of this line
runs on synthetic data.
