# q183 — methods

## The bridge module

`org_frontier/qualitative/disagreement_phi.py` exposes one function:

    spread(accountA_rules, accountB_rules, labels) ->
        {verdict_agreement, phi_gap, core_jaccard, both_verdicts}

Each account is a list of per-node Boolean rules over the same labels, evaluated on the
little-endian current-state tuple. The module runs each account through `verdict()` and
`major_complex()` from `org_frontier.probes.lib`, which wrap the exact IIT-4.0 Φ classifier. Φ
is not reimplemented.

The three spread components:

- `verdict_agreement` is 1 iff the two accounts read the same structure (both dyadic or both
  triadic), else 0.
- `phi_gap` is the absolute difference of the two whole-system max Φ_MIP values.
- `core_jaccard` is the Jaccard overlap of the two major-complex cores (the party sets of the
  maximal complex, taken at the max-Φ reachable state of each account). Two empty cores count
  as full agreement (1.0).

## Controls

**Instrument control.** The faithful worker-system-counterpart triad
`[x1, x0&x2, x1]` with labels `(W, S, C)` reads `triadic` with max Φ_MIP = 2.0. The probe
aborts on failure.

**H1 identity control.** `spread(TRIAD, TRIAD, labels)` with `TRIAD = [x1, x0&x2, x1]`. The
decision rule: H1 is supported iff verdict_agreement = 1, phi_gap < 1e-9, and
|core_jaccard - 1.0| < 1e-9.

**H2 label-swap control.** A divergent pair: `TRIAD` (triadic) against a dyadic rewrite
`DYAD = [x1, x0, x1]` in which S copies W only and drops C from the integrated core. The probe
computes `spread(TRIAD, DYAD)` and `spread(DYAD, TRIAD)`. H2 is supported iff all three
components match across the two orientations (within 1e-9) and the pair actually diverges
(verdict_agreement = 0 or phi_gap > 1e-9).

## Determinism

The probe seeds `numpy.random.default_rng(0)`. The spread itself is exact (it reads classifier
verdicts over enumerated reachable states), so the output is byte-identical on re-run; this was
confirmed across three runs.

## Scope

The accounts are synthetic, coder-supplied rule sets, not measured worker states. The construct
validated here is divergence between two stated accounts of a coordination. No claim is made
about a real coordination; the validation gap between coded accounts and observed behaviour is
not closed by this study.
