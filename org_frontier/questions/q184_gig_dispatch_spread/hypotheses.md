# q184 — hypotheses

A gig driver and the platform give different accounts of one dispatch. The driver narrates it as
a one-way suggestion the driver may decline. The platform narrates it as committing the
driver-rider match. The q183 bridge reads each account as a rule set over labels (D, P, R) =
(Driver, Platform, Rider) and returns a spread tuple. Both hypotheses are fixed before the
computation.

**H1 (verdict split, gap = platform Φ).** The driver suggestion account scores a dyadic verdict
with Φ_MIP = 0, and the platform commit account a triadic verdict with Φ_MIP > 0. So
verdict_agreement = 0 and phi_gap equals the platform account's whole-system max Φ_MIP.

- H1-null: both accounts yield the same verdict and phi_gap = 0. The disagreement leaves no Φ
  trace.

**H2 (rider bound only under the platform account).** The rider node R sits in the major-complex
core under the platform commit account and is absent from the driver suggestion account's core,
so core_jaccard < 1.

- H2-null: core membership is identical across the two accounts. The disagreement is about
  magnitude, not about who is bound in.
