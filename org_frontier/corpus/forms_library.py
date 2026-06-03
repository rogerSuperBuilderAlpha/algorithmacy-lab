"""A curated, reusable library of small coordination forms with exact IIT-4.0 Φ.

Each form is a named application-layer system given as per-party Boolean rules (little-endian:
0 = Worker, 1 = System/mediator, 2 = Counterpart). Every form carries a one-line rationale for
its coupling — the TPM is derived from the form's actual who-reads-whom, never tuned to a target
Φ — and a set of structural tags so the analysis can ask which feature moves the verdict.

This is the curated companion to the dissertation's complete 4,096-wiring enumeration
(`dissertation/paper3_baseline/catalog.py`): that one is a coverage/null check over every Boolean
way three nodes can couple; this one is a small set of *recognizable* coordination forms, each
documented, meant to be reused and extended. Five forms are validated in the dissertation's
Paper 2; the rest are first-pass models, flagged as such.

Structural tags (computed by the form, not assigned to fit Φ):
  strict_mediation : True iff there is no direct W<->C edge (parties meet only through S).
  mediator_reads_both : True iff S's update depends on BOTH W and C.
  back_channel : True iff a direct W<->C edge exists.
"""

from dataclasses import dataclass
from typing import Callable, List


@dataclass
class Form:
    key: str
    title: str
    rules: List[Callable]
    rationale: str
    validated: bool            # True if validated in the dissertation Paper 2
    expected: str              # "dyadic" or "triadic" (the documented/known verdict, "?" if open)


# --------------------------------------------------------------------------------------
# Validated forms (dissertation Paper 2)
# --------------------------------------------------------------------------------------

FORMS = [
    Form(
        key="chat_dyad",
        title="Chat with a language model (dyadic limit)",
        rules=[lambda x: x[1], lambda x: x[0], lambda x: x[2]],
        rationale="Worker and system form a two-party loop; no third human party (C decoupled).",
        validated=True, expected="dyadic",
    ),
    Form(
        key="gig_dyadic_model",
        title="Rideshare, modeled dyadically (rider dropped from dispatch)",
        rules=[lambda x: 1 - x[1], lambda x: x[0], lambda x: x[2] & (1 - x[1])],
        rationale="Analyst sees only the driver<->app channel; the dispatch reads the driver alone.",
        validated=True, expected="dyadic",
    ),
    Form(
        key="ats_strict_bottleneck",
        title="Resume -> ATS -> hiring manager (strict bottleneck)",
        rules=[lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]],
        rationale="S forwards iff resume-signal AND manager-profile; W,C each read only S.",
        validated=True, expected="triadic",
    ),
    Form(
        key="ats_feedback_factors",
        title="Resume -> ATS -> hiring manager (realistic feedback — yet factors)",
        rules=[lambda x: 1 - x[1], lambda x: x[0] & x[2], lambda x: x[1] | x[2]],
        rationale="Strict mediator topology, but the reads do not keep each party live to S's commit.",
        validated=True, expected="dyadic",
    ),
    Form(
        key="gig_false_dyad",
        title="Rideshare driver -> platform -> rider (rider constitutive: the false dyad)",
        rules=[lambda x: 1 - x[1], lambda x: x[0] & x[2], lambda x: x[2] & (1 - x[1])],
        rationale="Presents as a driver<->app dyad, but dispatch reads the unseen rider (S' = W AND C).",
        validated=True, expected="triadic",
    ),

    # ----------------------------------------------------------------------------------
    # First-pass forms (NOT yet dissertation-validated) — defensible couplings, flagged.
    # ----------------------------------------------------------------------------------
    Form(
        key="pure_relay",
        title="Pure relay / broadcast (S copies W to C)",
        rules=[lambda x: x[0], lambda x: x[0], lambda x: x[1]],
        rationale="S relays W to C with no joint determination (S reads only W). Should factor.",
        validated=False, expected="dyadic",
    ),
    Form(
        key="two_sided_match",
        title="Two-sided match (both parties act on the system's joint commit)",
        rules=[lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]],
        rationale="S commits iff both sides present (W AND C); both W and C track the commit. "
                  "(Identical coupling to the ATS bottleneck — the canonical match triad.)",
        validated=False, expected="triadic",
    ),
    Form(
        key="hierarchy_backchannel",
        title="Hierarchy with a direct back-channel (W<->C edge present)",
        rules=[lambda x: x[2], lambda x: x[0] & x[2], lambda x: x[0]],
        rationale="Same joint commit S' = W AND C, but W and C also read each other directly. "
                  "Restoring the direct channel should collapse the triad.",
        validated=False, expected="dyadic",
    ),
]

FORMS_BY_KEY = {f.key: f for f in FORMS}


# --------------------------------------------------------------------------------------
# Structural tags from the coupling (computed, not assigned)
# --------------------------------------------------------------------------------------

def structural_tags(rules):
    """Return dict of structural features inferred from the connectivity matrix.
    Node order 0=W, 1=S, 2=C."""
    from org_frontier.classifier.classifier import cm_from_rules
    cm = cm_from_rules(rules)
    # cm[i, j] = 1 iff node j's rule depends on node i.
    s_reads_w = cm[0, 1] == 1
    s_reads_c = cm[2, 1] == 1
    w_reads_c = cm[2, 0] == 1
    c_reads_w = cm[0, 2] == 1
    back_channel = bool(w_reads_c or c_reads_w)
    return {
        "strict_mediation": not back_channel,
        "mediator_reads_both": bool(s_reads_w and s_reads_c),
        "back_channel": back_channel,
    }
