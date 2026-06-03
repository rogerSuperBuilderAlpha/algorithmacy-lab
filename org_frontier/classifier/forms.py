"""Built-in library of canonical coordination forms.

Each form is a small application-layer system rendered as per-party Boolean rules
(little-endian: index 0 = W, 1 = S, 2 = C). The TPMs are derived from each case's actual
coupling — who depends on whom — not chosen for a target Φ. These are the forms validated in
the dissertation's Paper 2 (``dissertation/paper2_construct/worked_examples.py``); they double
as the classifier's demo set and its regression suite (see ``EXPECTED``).

Drop in your own form by writing three (or n) rules and calling ``classifier.classify_rules``.
A reusable library of broader forms — broadcast, market, hierarchy — is the next sub-experiment
(see ``../landscape/SURVEY_FINDINGS.md``); stubs are marked TODO below.
"""

# --------------------------------------------------------------------------------------
# Dyadic limit — expect LITERACY (Φ_MIP ≈ 0)
# --------------------------------------------------------------------------------------

def chat_dyad():
    """Chat with a language model. W and S form a two-party loop; no third human party, so C
    is decoupled. The model commits determinations but none couples a C.
        W' = S,  S' = W,  C' = C."""
    return [lambda x: x[1], lambda x: x[0], lambda x: x[2]]


def gig_dyadic_model():
    """Rideshare as a DYADIC construct models it: the analyst sees only the driver<->app
    channel and drops the (invisible) rider from the dispatch determination.
        W' = NOT S,  S' = W,  C' = C AND NOT S.
    Exactly one dependency removed vs the false dyad (S no longer reads C)."""
    return [lambda x: 1 - x[1], lambda x: x[0], lambda x: x[2] & (1 - x[1])]


# --------------------------------------------------------------------------------------
# Irreducible triads — expect ALGORITHMACY (Φ_MIP > 0)
# --------------------------------------------------------------------------------------

def ats_triad_mediator():
    """Résumé -> applicant-tracking-system -> hiring manager, strict bottleneck.
        S' = W AND C,  W' = S,  C' = S.   No direct W-C edge."""
    return [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]


def ats_feedback_factors():
    """ATS with realistic feedback, strict mediator topology (W, C each couple only to S) — yet
    it FACTORS. Instructive case: triadic topology is necessary but not sufficient. The read
    functions here do not keep each party a live function of the mediator's commit, so the form
    factors and Φ_MIP = 0. The verdict turns on the reads, not just the wiring.
        W' = NOT S,  S' = W AND C,  C' = S OR C.   (dissertation Paper 2, §4: Φ = 0.0)"""
    return [lambda x: 1 - x[1], lambda x: x[0] & x[2], lambda x: x[1] | x[2]]


def gig_false_dyad():
    """Rideshare driver -> platform -> rider, with the rider CONSTITUTIVE of dispatch. Presents
    as a driver<->app dyad, but the determination reads the unseen third party.
        W' = NOT S,  S' = W AND C,  C' = C AND NOT S.   No direct W-C edge."""
    return [lambda x: 1 - x[1], lambda x: x[0] & x[2], lambda x: x[2] & (1 - x[1])]


# --------------------------------------------------------------------------------------
# Registry + expected verdicts (regression suite)
# --------------------------------------------------------------------------------------

FORMS = {
    "chat_dyad": chat_dyad,
    "gig_dyadic_model": gig_dyadic_model,
    "ats_triad_mediator": ats_triad_mediator,
    "ats_feedback_factors": ats_feedback_factors,
    "gig_false_dyad": gig_false_dyad,
}

# Expected structural verdict per form, matching the dissertation's Paper 2 results exactly:
# the dyad and dyadic-model forms factor (literacy); the strict bottleneck and the
# rider-constitutive false dyad do not (algorithmacy); and the "realistic feedback" form
# FACTORS despite triadic topology (Φ = 0.0, §4) — the read functions, not the wiring, decide.
EXPECTED = {
    "chat_dyad": "dyadic",
    "gig_dyadic_model": "dyadic",
    "ats_triad_mediator": "triadic",
    "ats_feedback_factors": "dyadic",
    "gig_false_dyad": "triadic",
}

# TODO (sub-experiment: coordination-form TPM library): broadcast, two-sided market,
# hierarchy, commons. Each needs a defensible application-layer coupling before inclusion.
