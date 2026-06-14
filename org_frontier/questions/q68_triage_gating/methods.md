# Q68 — Stage 4 methods (fixed before computation)

Deterministic Boolean systems on four elements (E, M, R, T), synchronous update, read on the maximal
complex (`probes.lib.major_complex`) and classified by exact IIT-4.0 Φ (`classifier.classify_rules`). The
base outreach triad is E'=M, M'=E∧R, R'=M (Q63 read_recipient, triadic at Φ=2.0). The instrument is
validated on a decoupled relay (dyadic) and a fully-coupled triad (triadic) first. Run on
`~/iit-playground/venv-4.0/bin/python`. Decision rules fixed here. State tuple x = (E, M, R, T).

The three triage configurations:
- **monitoring_only:** E'=M, M'=E∧R, R'=M, T'=M. (T reads the message; gates nothing.)
- **gating_only:** E'=M, M'=E∧R, R'=M∧T, T'=T. (T gates delivery to R; reads nothing.)
- **bidirectional:** E'=M, M'=E∧R, R'=M∧T, T'=M. (T reads the message and gates delivery.)

## Test (`probe_triage_gating.py`)

- **Measure:** per configuration, the major complex (label set) and its Φ.
- **Decision rules:**
  - H1 confirmed if T is not in the monitoring_only major complex.
  - H2 confirmed if T is not in the gating_only major complex.
  - H3 confirmed if T is in the bidirectional major complex.
  - H4 confirmed if every configuration's major complex has Φ > 0 (triadic core present).
