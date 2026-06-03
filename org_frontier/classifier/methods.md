# Methods — how the classifier computes a verdict

A reader should be able to reproduce the design without reading the code.

## The model of a coordination form

A coordination form is a discrete dynamical system of `n` parties. The first three are Worker (W),
System/mediator (S), Counterpart (C); more can be added. Each party is a binary element (active or
not at each step). Each party's next state is a fixed Boolean function of the current states of all
parties. The dynamics are encoded as a deterministic state-by-node transition matrix (TPM) of shape
`(2^n, n)`, with little-endian state indexing (bit 0 = W), matching PyPhi and the repo's
`proxy_audit.exact_phi` oracle.

The TPM is derived from the form's **actual coupling** — who depends on whom — never chosen to hit a
target Φ. The connectivity matrix is inferred from the rules by a flip-test (`cm[i,j] = 1` iff
flipping party i's state ever changes party j's next state).

## State individuation

States are the joint on/off configurations of the parties. The classifier evaluates every
**reachable** state (one with at least one predecessor under the dynamics); PyPhi refuses to analyze
unreachable states. This is the pre-registered state-individuation rule inherited from the
dissertation's Paper 2 instrument.

## The ground-truth computation

For each reachable state, exact IIT-4.0 system Φ is computed via `pyphi.new_big_phi.sia`, wrapped by
`proxy_audit.exact_phi.exact_big_phi`. `sia` returns Φ over the **minimum-information partition** —
the party-respecting cut the system resists least — together with that partition.

## The verdict rule

A form is **triadic** (demands **algorithmacy**) if Φ over the MIP exceeds `PHI_EPS = 1e-9` in at
least one reachable state. Otherwise it is **dyadic** (demands **literacy**). The system-level
verdict is read at the most-integrated reachable state, matching the instrument the dissertation
validated. The full Φ profile across states is retained in the `Verdict` object and written to the
results CSV.

### Why the MIP, not the complete cut

Φ over the complete `{W}{S}{C}` cut is positive even for coupled dyads, because that cut also severs
the genuine two-party `{W,S}` coupling a dyad has. It therefore over-calls every coupled dyad a
triad. The correct binary test is Φ_MIP = 0: a dyad factors along its own least-damaging cut
(`{W,S}|{C}`), which the MIP finds; a triad has no such factoring cut. The MIP is itself a
party-respecting partition, so the verdict is still about party-line factorization. Demonstrated in
`dissertation/paper2_construct/party_partition.py`.

## Controls (run before any verdict)

`validate.py` runs two controls and the regression suite:

1. **Factoring control** — `W'=S, S'=W, C'=C` (C decoupled). Must classify **dyadic** (Φ ≈ 0).
2. **Irreducible control** — `W'=S|C, S'=W&C, C'=W^S` (full coupling). Must classify **triadic**
   (Φ > 0).
3. **Regression suite** — every built-in form in `forms.py` must match its `EXPECTED` verdict.

A non-zero exit code means a control failed; verdicts are not to be trusted until it passes.

## Statistics and scope

This is a structural classifier, not a statistical estimator: each form has a definite TPM and a
definite Φ profile. There is no sampling and no noise at this layer. The statistical questions
(does a cheap proxy track this verdict on real interaction data; how do verdicts distribute across a
population of forms) belong to the next two sub-experiments (proxy bridge; coordination-form
library), per `../landscape/SURVEY_FINDINGS.md`.

## Reproducibility

```bash
~/iit-playground/venv-4.0/bin/python -m org_frontier.classifier.validate   # controls
~/iit-playground/venv-4.0/bin/python -m org_frontier.classifier.run        # library -> CSV
```

Built on the same PyPhi IIT-4.0 line as the rest of the repo (`requirements.txt`).
