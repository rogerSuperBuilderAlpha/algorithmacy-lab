# q143 — review

## Reproduce

source /tmp/rvenv/bin/activate && export PYPHI_WELCOME_OFF=yes && \
python -m org_frontier.questions.q143_ring_verdict_geometry.probe_ring_verdict_geometry

Captured stdout is in results/output.txt. Two runs give byte-identical output.

## Checks

- Instrument control: the faithful triad reads triadic at Φ=2.0 and the probe prints
  "CONTROL faithful-triad reads triadic at Φ=2.0: PASS". A failure exits non-zero before any
  ring result is reported.
- Anchors: chain(5) reads triadic with a two-node core (sheds nodes); pool(5) carries a full
  five-node core. These confirm the core-membership read discriminates shedding from holding.
- Determinism: numpy.random.default_rng(0) is seeded; exact Φ over reachable states is
  deterministic; diff of two runs is empty.

## Reading the verdicts

- H1 is REFUTED on its own pre-registered terms, and the refutation is informative. The two-arc,
  constant-Φ regime holds for n=4..7 exactly as rotational symmetry suggests. The n=3 ring breaks
  it: the cheapest partition is the complete three-way split at Φ=6.0, not a two-arc cut at 4.0.
  Reporting H1 as supported would require dropping n=3 from the claim after seeing the data, which
  the pre-registration forbids.
- H2 is SUPPORTED. The core is full at every n. This is a clean contrast to hub topologies that
  shed parties at intermediate sizes.

## Limits

Synthetic Boolean forms only. The range stops at n=7 because exact Φ over 2^n reachable states
grows fast. Whether the Φ=4.0 plateau and the full core persist past n=7 is open. The empirical
arm of this line is separate and is not touched here.
