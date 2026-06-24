# q183 — A Φ-spread bridge for two divergent party accounts of one coordination

Two parties to a coordination can describe it differently. One says the mediator binds both
sides; the other says the mediator just tracks one side. Qualitative research treats that
disagreement as data. This study builds an instrument that scores the disagreement when each
account is written as a small rule set, and validates the instrument on controls.

The bridge module `org_frontier/qualitative/disagreement_phi.py` takes two accounts of the same
coordination, each a list of per-party Boolean rules over shared labels, runs each through the
exact IIT-4.0 Φ classifier, and returns a spread tuple:

- `verdict_agreement` records whether the two accounts read the same structure (both dyadic or
  both triadic).
- `phi_gap` is the absolute difference of the two whole-system max Φ_MIP values.
- `core_jaccard` is the Jaccard overlap of the two major-complex cores.

A useful divergence metric anchors at zero. When the two accounts agree exactly, the score must
report no spread. The identity control checks this: feeding the same rule set as both accounts
returns verdict_agreement = 1, phi_gap = 0.0, core_jaccard = 1.0. H1 holds.

A useful divergence metric also depends on the disagreement, not on which party happens to be
listed first. The label-swap control checks this on a pair that actually diverges: the faithful
worker-system-counterpart triad `[x1, x0&x2, x1]` against a dyadic rewrite `[x1, x0, x1]` in
which the mediator copies the worker and drops the counterpart. The two accounts split on the
verdict (triadic vs dyadic), carry a phi_gap of 2.0, and overlap two-thirds on the core. Swapping
which account is A and which is B leaves all three components fixed. H2 holds.

The accounts here are synthetic rule sets, not measured worker states. The instrument scores
divergence between two stated accounts of a coordination. The gap between a coded account and an
observed coordination remains open, and later studies in this line apply the bridge across
settings rather than closing that gap. The contribution of this study is the validated
instrument: a zero-anchored, party-symmetric spread that a later analysis can read off two
coder-supplied accounts.
