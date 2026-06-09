# Q85 — Stage 4 methods (fixed before computation)

Deterministic Boolean systems, classified by exact IIT-4.0 Φ over the minimum-information partition
(`classifier.classify_rules`) and read on the maximal complex (`probes.lib.major_complex`) for H3. Worker
E, agents M1..MN, counterpart C; each agent reads E and C (Mi'=E∧C). Run on
`~/iit-playground/venv-4.0/bin/python`.

Forms (for N = 2, 3, 4; n = N + 2):
- **substitutable**: E'=M1∨…∨MN, C'=M1∨…∨MN (E and C coordinate through any one agent).
- **all_required**: E'=M1∧…∧MN, C'=M1∧…∧MN (all agents required).
- **mixed** (N=3): E'=C'= M1 ∧ (M2 ∨ M3) (one substitutable pair among required agents).

## Test (`probe_agent_market.py`)

- **Measure:** the verdict and Φ_MIP for substitutable and all_required at N=2,3,4; the major complex of
  all_required at N=3; the verdict of the mixed form.
- **Decision rules:**
  - H1 confirmed if substitutable is dyadic at every N.
  - H2 confirmed if all_required is triadic at every N with Φ increasing in N.
  - H3 confirmed if the all_required major complex is the full party set.
  - H4 confirmed if the mixed form is dyadic.
