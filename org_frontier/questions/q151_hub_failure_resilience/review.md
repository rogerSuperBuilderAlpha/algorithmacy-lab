# q151 — Review

Claim. Ablating the spanning hub collapses a single-hub topology to dyadic, while a backup-hub form and a
ring-backed form of the same n keep the triadic verdict. The Φ that survives does not track the number of
cycles through non-hub nodes.

Strengths.
- Exact IIT-4.0 Φ throughout; no reimplementation. The instrument control on the faithful triad passes
  (triadic, max Φ 2.0, spanning core).
- A built-in control checks that every unablated form reads triadic, so the resilience contrast is defined
  before it is read.
- H2 is reported as a clean null. The probe's decision rule requires the non-hub cycle to be necessary for
  retention, and the backup-hub form (zero non-hub cycles, retained Φ 0.879) rejects it. The result is not
  forced onto the original framing.
- Deterministic: seeds fixed, two re-runs byte-identical.

Limits and threats.
- Three topologies, one n. The H1 contrast rests on one collapsing form against two surviving forms; it is a
  demonstration of resilience, not a survey of when redundancy fails. A two-hub form whose second hub depends
  on the first does collapse (seen in the distributed-mediator probe), so "backup" must mean an independent
  hub, which is a modeling choice.
- The backup-hub form is near-reducible intact (Φ 0.015), and ablation raises its Φ. That a perturbation
  raises Φ is a real effect here, but it makes "retained Φ" an awkward scalar: the form retains more than it
  had. The verdict (triadic before and after) is the robust reading; the magnitude is encoding-dependent and
  should be read as ordinal at most.
- The ring's hub is a passive observer intact: it watches the ring but is not in the major complex, so its
  ablation changes nothing. This is honest about the ring case but means the ring arm tests "does the cycle
  carry the verdict on its own" rather than "does the cycle rescue a hub-dependent form." Both readings are
  stated.
- H2's cycle count is a static graph quantity (cyclomatic number on the non-hub subgraph). It does not see
  that the backup hub creates a dynamical hub-party loop after ablation. A cycle measure that counted all
  surviving loops, not only non-hub ones, might track retained Φ better; that is left open.
- Synthetic scope. No organization is measured. "Hub", "backup", "ring", "resilience" are Φ-and-graph
  quantities. The Φ-to-organization bridge is open, so the empirical reading is a baseline on synthetic data,
  not a field result.

Verdict. The synthetic claim holds within scope. H1 supported, H2 not supported. Worth extending to more
topologies and larger n by an approximation that keeps exact Φ tractable, and to a cycle measure that counts
the loops a backup hub leaves behind.
