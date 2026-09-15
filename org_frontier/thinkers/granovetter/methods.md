# Granovetter — Stage 4 methods

## Shared infrastructure

- Ties → state-by-node TPM by expectation over read sets (`forms.tpm`); connectivity from ties (`forms.cm`).
- Whole-system Φ_MIP: max over all reachable states of exact IIT-4.0 system Φ on the probabilistic TPM
  (`forms.phi_mip`). Major complex: `forms.major_complex_tpm`, max over reachable states. Both mirror
  `org_frontier.probes.lib` for deterministic rules.
- Transmission: ordered pairs joined by a path of ties (`forms.reach_pairs`).
- Run from the repo root on `~/iit-playground/venv-4.0/bin/python`.

## Instrument control (run first, in every probe)

Two checks. The conjunctive triad by rules: Φ = 2.000000, core {A, M, B}. The same triad built from ties
(A–M, M–B strong; AND-of-read, hold when nothing read): Φ = 2.000000. No comparison is read until both pass.

## Disclosure

The tie machinery was smoke-tested before H2–H5 were fixed, on the dyad at p = 1, 0.75, 0.5, 0.25 and on the
two-dyad bridge at p = 0.5 and 1. Those numbers are the H1 and H3 results and are reported unchanged; the
hypotheses record what was seen.

## Forms

**H1** dyad (a, b), p ∈ {0.25, 0.5, 0.75, 1.0}.
**H2** triad (A, B, C): A–B, A–C strong; B–C ∈ {absent, weak, strong}.
**H3** (a1, a2, b1, b2): a1–a2, b1–b2 strong; a2–b1 ∈ {weak, strong}.
**H4** base = H3 weak bridge; `cut_bridge` removes a2–b1; `cut_strong` removes a1–a2.
**H5** (a1, a2, b1, b2, c1, c2): three strong dyads; `isolated`; `chain` a2~b1, b2~c1 weak; `ring` adds c2~a1
weak; `strong_ring` the same three ties strong.

## Decision rules

- **H1** CONFIRMED iff Φ strictly increases over the four p. REFUTED otherwise.
- **H2** CONFIRMED iff Φ(open) < Φ(weak) < Φ(strong) and all three in the core each time. PARTIAL iff the
  ordering holds but a member is out, or Φ(open) < Φ(strong) with the weak closure out of order. REFUTED iff
  Φ(open) ≥ Φ(strong).
- **H3** CONFIRMED iff transmission equal and the major complex spans both dyads under both bridges. PARTIAL
  iff it spans under the strong bridge only. REFUTED iff it spans under neither.
- **H4** CONFIRMED iff bridge removal loses more on both measures. PARTIAL iff on one. REFUTED iff on neither.
- **H5** CONFIRMED iff chain and ring both have a major complex spanning all three dyads. PARTIAL iff the ring
  only. REFUTED iff neither.

## Reporting

Each probe prints the two control lines, one line per form (`form  Φ_MIP  core  coreΦ  reach  seconds`), and
one verdict line. Results in `results/<probe>.json`.
