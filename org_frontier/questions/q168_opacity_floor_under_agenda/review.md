# q168 — review

## What the probe shows

H(out|W) for the interested mediator can exceed the 0.50-bit floor PP1 sets for a faithful hidden
counterpart, reaching 1.00 bits at approve k=1, and probing W removes none of the residual at any k. H1
SUPPORTED, H2 CONFIRMED.

## Strengths

- The control reproduces PP1's exact 0.50-bit floor and the canonical triadic Φ = 2.0, tying the surprise
  accounting to the existing predictive-processing line.
- The result is closed-form and exact. No RNG enters the numbers; the seeded generator is hygiene only.
  Output is byte-identical across three runs.
- The two helpers added to predictive_processing.py reuse PP1's accounting verbatim with the gate
  swapped, so the faithful and interested cases share one code path.

## Limits and adversarial points

- The mechanism of the rise is specific. The agenda raises the residual only when the override aliases the
  counterpart's variance into a W-value the faithful gate left determinate. Approve k=1 does this; deny
  never does, because it collapses output toward a constant. The rise is real but not generic across
  agendas, and the FINDINGS table makes that visible rather than averaging it away.
- H2 is a structural identity, not a contingent finding. Probing W learns P(out|W) and the residual is
  defined as H(out|W), so probing W removes none of it by construction. The probe confirms the framing is
  consistent rather than discovering a surprising fact. That should be read as the model being coherent,
  not as independent evidence.
- C uniform and binary is a modeling choice. A non-uniform or correlated counterpart would shift the
  numbers. The study fixes the uniform case PP1 uses, for comparability.

## Scope

Closed-form information theory on a 3-variable Boolean model. The empirical reading is on synthetic forms.
No worker is measured; the surprise floor is explored, not established for any real platform.
