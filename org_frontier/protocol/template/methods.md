# Q<NN> — Stage 4 methods

For each hypothesis: the form or ensemble (exact rules/parameters), the measure, the controls, and the
decision rule fixed before the run. A reader should reproduce every test from this file alone.

## Shared infrastructure
- Verdict / Φ / major complex: `classifier.classifier` (`classify_rules`, `tpm_from_rules`,
  `cm_from_rules`), `probes/lib.py` (`verdict`, `major_complex`, `max_phi_float`).
- Information measures: `probes/_info.py` (entropy, mutual_information, transfer_entropy, o_information).
- Exact Φ / trajectories: `proxy_audit/exact_phi.py`.
- Python: `~/iit-playground/venv-4.0/bin/python`.

## Instrument control (run first)
<the known form whose verdict is already established, and the value it must reproduce before any
comparison number is trusted>

## H1 test
- **Form / ensemble:** <exact rules or sampling parameters>
- **Measure:** <verdict / Φ / core / named info measure>
- **Controls:** <baseline / positive control>
- **Decision rule:** <what value confirms vs refutes H1>
- **Script:** `probe_<slug>.py`

## H2 … H5 test
<same structure>
</content>
