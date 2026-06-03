# Findings — the literacy-or-algorithmacy classifier

Status: scaffolded and validated on its own controls. The numbers below are from the first run of
the built-in library (`results/verdicts.csv`), on the IIT-4.0 venv.

## Instrument validation (passes)

| Control | Rules | Verdict | Φ_MIP max | Expected |
|---|---|---|---|---|
| Factoring | W'=S, S'=W, C'=C (C decoupled) | dyadic | 0.0000 | dyadic ✓ |
| Irreducible | W'=S∨C, S'=W∧C, C'=W⊕S | triadic | 0.8301 | triadic ✓ |

## Built-in coordination forms

| Form | Structure | Competence | Φ_MIP max | MIP cut |
|---|---|---|---|---|
| chat_dyad | dyadic | literacy | 0.0000 | factors |
| gig_dyadic_model | dyadic | literacy | 0.0000 | factors |
| ats_triad_mediator | triadic | **algorithmacy** | 2.0000 | {W,SC} |
| ats_feedback_factors | dyadic | literacy | 0.0000 | factors |
| gig_false_dyad | triadic | **algorithmacy** | 2.0000 | {W,SC} |

## What the run shows

1. **The classifier reproduces the dissertation's Paper 2 binary result.** The strict bottleneck
   and the rider-constitutive false dyad are triadic (Φ = 2.0); the chat dyad and the dyadic gig
   model factor (Φ = 0). The verdict turns on one edge: does the mediator's determination read the
   unseen third party.

2. **Topology is necessary but not sufficient.** `ats_feedback_factors` has strict mediator
   topology — no direct worker–counterpart edge — yet it factors (Φ = 0). The read functions, not
   the wiring, decide. A form can look triadic and still demand only literacy. This is exactly why
   a surface read fails and the instrument is needed.

3. **The MIP, not the complete cut.** Triadic forms cut at {W, SC} — a 2-part party-respecting
   partition — not the complete {W}{S}{C} tripartition. The complete cut would over-call the dyads.

## Caveats (carried from the construct)

- **Binary, not graded.** Φ = 2.0 vs 0.8301 across triads is not a difficulty ranking; magnitude
  is encoding-dependent (dissertation withdrew the graded claim). Read the verdict.
- **Model-relative.** Verdicts depend on the application-layer coupling, the state-individuation
  rule, and the MIP reading. State the model.
- **Small only.** Exact Φ caps at ~10-12 parties. Fine for coordination units; the proxy bridge is
  the fallback for larger structures.

## Next

- Broaden `forms.py` into the coordination-form TPM library (broadcast, two-sided market,
  hierarchy, commons), each with a defensible application-layer coupling.
- Add the proxy bridge: estimate the verdict from interaction time-series (Φ_AR), reusing
  `proxy_audit/` and `phiid_vs_phi/` machinery, and test whether the cheap estimate preserves the
  binary verdict.
