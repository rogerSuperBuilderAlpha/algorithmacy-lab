# Q132 — hypotheses (fixed before computing)

Q131 found that an interested mediator on the AND baseline destroys value — the total Φ falls and the
mediator's two-thirds share falls with it. Q127 found the baseline governs what self-interest does: balanced
baselines (XNOR, XOR) start weakly irreducible (Φ = 0.5) and a dose of self-interest re-integrates them,
raising Φ. Q132 reads the Shapley value of integration across all four baselines and asks whether, where the
value grows, the mediator captures the gain or the parties share it.

A methodological correction is forced first. Q111's value function reads subsystem Φ at the all-ones
background state, which is where the AND mediator integrates but not necessarily the others. The value must
be read where the form integrates — the verdict's max-Φ state.

- **H1.** The all-ones value reading agrees with the verdict only on the AND baseline; elsewhere it is
  degenerate, because all-ones is not those mediators' integrating state.
- **H2.** Under the verdict-aligned reading, destruction-versus-extraction is baseline-relative, mirroring
  Q127: on a sparse baseline self-interest destroys value and the mediator's rent; on a balanced baseline
  that re-integrates (XOR under the approve agenda) the mediator captures the re-integrated value as the same
  concentrated two-thirds rent — extraction, not sharing.
- **Null.** The value trajectory and the mediator's share are the same across baselines.

Method: the Q127 interested mediator at level k for four baselines (AND, OR, XNOR, XOR), approve agenda. At
each k, the verdict and its integrating state, then the Shapley value of subsystem Φ at that state and, for
comparison, at all-ones. As recorded in [`FINDINGS.md`](FINDINGS.md), H1 as stated was refuted — the all-ones
reading agrees with the verdict on more than AND but fails wherever the integrating state is not all-ones —
while H2 held.
