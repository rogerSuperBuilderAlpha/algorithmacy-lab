# Q63 — Stage 3 hypotheses (fixed before computation)

Five hypotheses on whether agent-mediated outreach is triadic, and on the four conditions the design
predicts move the verdict. Parties: sender intent (E), agent/mediator (M), recipient (R). The agent's
commit is M's update rule. Written and committed before any test runs.

## H1 — Reading the recipient makes outreach triadic; broadcast does not

- **Claim:** A read-the-recipient form, where M's commit jointly determines from E and R
  (E'=M, M'=E∧R, R'=M), is triadic (Φ_MIP > 0). A broadcast form, where M ignores R
  (E'=M, M'=E, R'=M), is dyadic (Φ_MIP = 0).
- **H0:** The read-the-recipient form is dyadic, or the broadcast form is triadic.
- **Predicted outcome:** read_recipient triadic at Φ_MIP = 2.0; broadcast dyadic at Φ_MIP = 0. H0 refuted.

## H2 — Substitutable recipients collapse the triad

- **Claim:** With two recipients, an all-required commit (M'=E∧R1∧R2) is triadic, while a substitutable
  commit (M'=E∧(R1∨R2)) is dyadic.
- **H0:** The substitutable form is triadic, or the all-required form is dyadic.
- **Predicted outcome:** all_required triadic (Φ_MIP > 0); substitutable dyadic (Φ_MIP = 0). H0 refuted.

## H3 — Disclosure is a label, not a read

- **Claim:** Adding a disclosure node D that announces the message (D'=M) but that no commit reads leaves
  the read-the-recipient triad's verdict unchanged: the major complex stays {E, M, R}, D stays out of it,
  and its Φ equals the H1 read_recipient value.
- **H0:** The major complex changes — D enters the core, or the core or its Φ differs from the H1 triad.
- **Predicted outcome:** core = {E, M, R}, D excluded, Φ equal to the H1 read_recipient Φ. H0 refuted.

## H4 — A cost proxy does not recover the verdict

- **Claim:** Mediator in-degree (the number of sources M's commit reads), a stand-in for the cost of
  tailoring, fails to separate dyadic from triadic: at least one dyadic form has in-degree greater than or
  equal to a triadic form's.
- **H0:** The proxy separates the classes — every triadic form has strictly higher mediator in-degree than
  every dyadic form.
- **Predicted outcome:** the substitutable form (dyadic, M reads E, R1, R2 → in-degree 3) has higher
  in-degree than read_recipient (triadic, in-degree 2). The proxy is non-monotone. H0 refuted.

## H5 — Liveness, not the mediator reading both, carries the verdict

- **Claim:** A one-shot form where M reads E and R but the recipient is frozen and not live to the commit
  (E'=M, M'=E∧R, R'=R) is dyadic. A conversation form where the recipient stays live (R'=M) is triadic.
- **H0:** The one-shot form is triadic — a mediator reading both sources suffices regardless of liveness.
- **Predicted outcome:** one_shot dyadic at Φ_MIP = 0; conversation triadic at Φ_MIP = 2.0. H0 refuted.
