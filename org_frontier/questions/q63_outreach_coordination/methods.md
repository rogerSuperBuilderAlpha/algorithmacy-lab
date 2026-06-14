# Q63 — Stage 4 methods (fixed before computation)

All forms are deterministic Boolean systems with synchronous update, classified by exact IIT-4.0 Φ over
the minimum-information partition via `classifier.classify_rules` (whole-system verdict) and
`probes.lib.major_complex` (the maximal complex, for forms with spectator nodes). State tuples are indexed
in label order. Each probe validates the instrument on a known control before its comparison: a
fully-coupled control triad (forms.py TRIADIC_CONTROL) reads triadic at Φ=0.83, and a decoupled relay
reads dyadic. Run on `~/iit-playground/venv-4.0/bin/python`.

The decision rule for each hypothesis is fixed here.

## H1 test — broadcast versus read-the-recipient

- **Forms (n=3, labels E, M, R):**
  - `read_recipient`: E'=M, M'=E∧R, R'=M.
  - `broadcast`: E'=M, M'=E, R'=M.
- **Measure:** verdict and Φ_MIP from `classify_rules`.
- **Control:** the fully-coupled control triad reads triadic at Φ=0.83 before the comparison.
- **Decision rule:** H1 confirmed if `read_recipient` is triadic (Φ_MIP > 0) and `broadcast` is dyadic
  (Φ_MIP = 0). Refuted if `read_recipient` is dyadic or `broadcast` is triadic.

## H2 test — substitutable recipients

- **Forms (n=4, labels E, M, R1, R2):**
  - `all_required`: E'=M, M'=E∧R1∧R2, R1'=M, R2'=M.
  - `substitutable`: E'=M, M'=E∧(R1∨R2), R1'=M, R2'=M.
- **Measure:** verdict and Φ_MIP from `classify_rules`.
- **Control:** the fully-coupled control triad reads triadic before the comparison.
- **Decision rule:** H2 confirmed if `all_required` is triadic and `substitutable` is dyadic. Refuted if
  `substitutable` is triadic or `all_required` is dyadic.

## H3 test — disclosure is a label

- **Form (n=4, labels E, M, R, D):** `disclosed`: E'=M, M'=E∧R, R'=M, D'=M. No commit reads D.
- **Measure:** `major_complex` — the core label set and its Φ — compared to the H1 `read_recipient` triad.
- **Control:** the fully-coupled control triad reads triadic at Φ=0.83 before the comparison.
- **Decision rule:** H3 confirmed if the major complex is exactly {E, M, R}, D is excluded, and its Φ
  equals the H1 `read_recipient` Φ (within 1e-6). Refuted if D enters the core, or the core or its Φ
  differs from the H1 triad.

## H4 test — cost proxy does not recover the verdict

- **Forms:** the four forms above (`read_recipient`, `broadcast`, `all_required`, `substitutable`).
- **Measure:** the cost proxy is the mediator's in-degree, `cm[:, M].sum()` from `cm_from_rules`, i.e. the
  number of sources M's commit reads. Paired with each form's verdict.
- **Control:** the H1 and H2 verdicts (themselves validated) supply the ground truth.
- **Decision rule:** H4 confirmed if the proxy is non-monotone in the verdict — at least one dyadic form
  has mediator in-degree greater than or equal to a triadic form's. Refuted if every triadic form has
  strictly higher mediator in-degree than every dyadic form.

## H5 test — liveness carries the verdict

- **Forms (n=3, labels E, M, R):**
  - `conversation`: E'=M, M'=E∧R, R'=M (recipient stays live to the commit).
  - `one_shot`: E'=M, M'=E∧R, R'=R (recipient frozen; M reads R but R does not read M).
- **Measure:** verdict and Φ_MIP from `classify_rules`.
- **Control:** the fully-coupled control triad reads triadic at Φ=0.83 before the comparison.
- **Decision rule:** H5 confirmed if `conversation` is triadic and `one_shot` is dyadic. Refuted if
  `one_shot` is triadic.
