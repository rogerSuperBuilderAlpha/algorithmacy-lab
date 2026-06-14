# Q70 — Stage 4 methods (fixed before computation)

Deterministic Boolean systems, synchronous update, classified by exact IIT-4.0 Φ over the
minimum-information partition (`classifier.classify_rules`) and read on the maximal complex
(`probes.lib.major_complex`) for H4. Instrument validated on a decoupled relay (dyadic) and a
fully-coupled triad (triadic) first. Run on `~/iit-playground/venv-4.0/bin/python`. Decision rules fixed
here.

Forms:
- **single** (E, M, C): E'=M, M'=E∧C, C'=M.
- **substitutable** (E, M1, M2, C): E'=M1∨M2, M1'=E∧C, M2'=E∧C, C'=M1∨M2.
- **required_both** (E, M1, M2, C): E'=M1∧M2, M1'=E∧C, M2'=E∧C, C'=M1∧M2.

## Test (`probe_agent_substitutability.py`)

- **Measure:** verdict and Φ_MIP for each form; the major complex for required_both.
- **Decision rules:**
  - H1 confirmed if single is triadic at Φ_MIP = 2.0.
  - H2 confirmed if substitutable is dyadic.
  - H3 confirmed if required_both is triadic.
  - H4 confirmed if the required_both major complex contains M1 and M2.
