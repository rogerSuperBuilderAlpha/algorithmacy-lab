# q168 — methods

Probe 322. The surprise accounting reuses predictive_processing's two helpers, with the output gate set to
Q126's interested mediator.

## Forms

The mediator is mediator(agenda, k) from q126: it outputs its agenda a on the k states where the parties
least warrant a, and commits the faithful joint determination W ∧ C elsewhere. k = 0 is the faithful AND
gate; k = 4 is the constant agenda. The two agendas are approve (a=1, overriding the least-warrant states
toward 1) and deny (a=0, overriding the most-warrant states toward 0). The sweep runs k = 0..4.

## Quantities

The worker sees W. The counterpart C is hidden and uniform, C ~ Bernoulli(0.5). For a gate g:

- residual_surprise_under_mediator(g) computes H(out|W) = mean over W of the binary entropy of
  P(out=1 | W=w), where P(out=1 | W=w) = 0.5 · [g(w,0) + g(w,1)]. This is the surprise the worker's best
  model from W alone cannot remove.
- probed_w_limit_under_mediator(g) returns the residual that survives the worker probing W. Probing W lets
  her learn P(out | W) exactly, removing epistemic uncertainty about her own channel. She cannot set or
  observe C, so the C-aliased part of the output remains. That surviving part is exactly H(out | W), so the
  function returns it. The difference H(out|W) − (probed limit) is the surprise probing W removes.

Both helpers live in org_frontier/cognition/predictive_processing.py, the module the predictive-processing
line reuses. For the faithful gate they reproduce PP1's 0.50-bit floor.

## Control

The instrument control checks that the faithful gate (k=0) reads H(out|W) = 0.50 bits, matching PP1, and
that the canonical faithful triad [x[1], x[0]&x[2], x[1]] reads structure 'triadic' with max_phi 2.0. The
probe stops on a failed control.

## Verdict rules

- H1 holds if some interested k (k>0) raises H(out|W) above 0.50 bits.
- H2 holds if probing W removes none of H(out|W) at any k, that is the W-probing limit equals H(out|W) for
  every k and agenda.

## Determinism

The surprise is closed-form binary entropy over a 4-state truth table; no RNG enters the result. A seeded
generator (numpy default_rng(0)) is fixed for reproducibility hygiene. Output is byte-identical across runs.

## Scope

Closed-form information theory on a 3-variable Boolean model. Evidence about the instrument and the
construct, not a measurement of a real platform. "Agenda", "approve", "deny", "interest" label output
values and rule structure, not measured intent. The empirical reading is on synthetic forms.
