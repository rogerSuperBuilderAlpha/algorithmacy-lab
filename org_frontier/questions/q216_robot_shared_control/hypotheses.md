# Hypotheses — robot shared control

Fixed before any result was computed. This file is committed before the probe runs.

**Question.** Is human-autopilot shared control of a robot triadic or dyadic, and which link makes it so?

**Nodes.** Human operator `H` (x[0]), Autopilot / safety controller `P` (x[1]), Robot `R` (x[2]).
Deterministic Boolean rules, little-endian, scored with `org_frontier.probes.lib.verdict` and
`major_complex`.

| ID | Name | Rules |
|---|---|---|
| 1 | Teleoperation | R'=H, P'=R, H'=R |
| 2 | Full autonomy | R'=P, P'=R, H'=R |
| 3 | Shared control | R'=H∧P, P'=R, H'=R |
| 4 | Shared control, feedback to human cut | R'=H∧P, P'=R, H'=H |

**Predictions.**

- H1. (1) Teleoperation is dyadic. The autopilot only watches; the loop is human–robot.
- H2. (2) Full autonomy is dyadic. The human only watches; the loop is autopilot–robot.
- H3. (3) Shared control is triadic (Φ_MIP > 0). The robot moves only when the human command and the
  safety check agree, and both see the result.
- H4. (4) is dyadic. Cutting the robot-to-human feedback (H'=H) breaks the three-way loop, so the link
  that makes shared control triadic is the conjunctive gate together with feedback to both parties.

Only shared control (3) is predicted triadic.

**Nulls.** For each model the null is the opposite verdict. Any failed prediction is reported as a result.

**Decision rule.** Run `python -m org_frontier.classifier.validate` first; it must print
`Instrument validated`. A model is triadic iff `verdict(...).structure == "triadic"`
(Φ_MIP max > PHI_EPS = 1e-9), else dyadic. Numbers are recorded exactly as printed. A rule is changed
only if a model is degenerate, and any change is documented.

**Scope.** In-silico evidence about small Boolean models, not a measurement of any real robot.
