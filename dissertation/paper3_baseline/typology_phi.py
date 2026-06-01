"""Paper 3 — placing a typology of organization types on the triadic-demand scale.

Each organization is modelled as an application-layer system (Worker, System/mediator,
Counterpart; a fourth party for higher-order forms) under Paper 2's pre-registered
state-individuation rule. The determination structure for each is fixed BEFORE computing
(pre-registered here in the docstrings), derived from how that organization actually
coordinates its parties — not chosen for a target Φ. We compute exact IIT-4.0 system Φ and
report whatever results.

The scale's levels come from STRUCTURE, not from the seat of the mediator:
  - dyadic / no constitutive mediator        -> Φ = 0      (floor; literacy suffices)
  - parity-coupled determination (XOR-like)  -> Φ ~ 0.5
  - partial mediation (parties also coordinate directly) -> intermediate
  - strict mediation, joint determination     -> Φ = 2.0    (algorithmacy demanded)
  - higher-order (a determination binding >3 parties) -> Φ > 2.0  (4-node)

The decisive test (the human-mediated contrast class): a court or a staffing agency, with a
human in the mediator seat but the SAME determination structure as an algorithmic platform,
must land at the SAME level. If it does, the model measures triadic coordination, not algorithms.

Run:  ~/iit-playground/venv-4.0/bin/python dissertation/paper3_baseline/typology_phi.py
"""

import os
import sys

# Paper 2's instrument lives in the sibling paper2_construct dir.
_P2 = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "paper2_construct"))
if _P2 not in sys.path:
    sys.path.insert(0, _P2)

import numpy as np
import pyphi
from pyphi import new_big_phi

from phi_instrument import tpm_from_rules, cm_from_rules, system_phi_over_states

pyphi.config.PROGRESS_BARS = False
pyphi.config.PARALLEL = False


def placement(rules, n=3):
    """Compute the form's placement: max and mean system Φ over reachable states, and the
    minimum-information partition at the max-Φ state."""
    tpm, cm = tpm_from_rules(rules, n), cm_from_rules(rules, n)
    results = system_phi_over_states(tpm, cm, n)
    if not results:
        return {"max": 0.0, "mean": 0.0, "mip": "none (no evaluable states)", "n": n, "cm": cm}
    phis = [p for _, p in results]
    best_state = max(results, key=lambda r: r[1])[0]
    labels = ("W", "S", "C", "D")[:n]
    net = pyphi.Network(tpm, cm=cm, node_labels=labels)
    sub = pyphi.Subsystem(net, tuple(best_state))
    sia = new_big_phi.sia(sub)
    try:
        mip = str(sia.partition)
    except Exception:
        mip = "(unavailable)"
    return {"max": float(np.max(phis)), "mean": float(np.mean(phis)),
            "mip": mip, "n": n, "cm": cm, "best_state": best_state}


# ======================================================================================
# THE TYPOLOGY.  rules[j](x) -> node j's next value; x is the current state tuple.
# Node order: 0=W (worker/one party), 1=S (mediator), 2=C (counterpart), 3=D (4th party).
# ======================================================================================

ORGS = [
    # ---- Class 1: DYADIC BASELINES (no constitutive mediator) -----------------------
    ("Direct exchange (no mediator)", "dyadic baseline",
     # Two parties deal with each other directly; the 'system' is inert (S copies itself).
     # No third party constitutes the coordination.  W'=C, S'=S, C'=W.
     [lambda x: x[2], lambda x: x[1], lambda x: x[0]], 3),

    ("Chat with a language model", "dyadic baseline",
     # Paper 2's dyadic limit: a two-party loop, the model commits nothing coupling a third.
     # W'=S, S'=W, C'=C.
     [lambda x: x[1], lambda x: x[0], lambda x: x[2]], 3),

    # ---- Class 2: ALGORITHMIC PLATFORMS ---------------------------------------------
    ("Rideshare, solo (Uber/Lyft)", "algorithmic platform",
     # Strict mediation: driver and rider reach each other ONLY through the dispatch the
     # platform commits as a joint function of both.  W'=S, S'=W&C, C'=S.
     [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]], 3),

    ("Food delivery (courier-platform-customer)", "algorithmic platform",
     # Same strict-mediation structure for the dispatch coordination.
     [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]], 3),

    ("Freelance marketplace (Upwork)", "algorithmic platform",
     # PARTIAL mediation: the platform matches (S'=W&C), but client and freelancer then
     # coordinate directly too (each reads the other as well as the platform).
     # W'=S|C, S'=W&C, C'=S|W.
     [lambda x: x[1] | x[2], lambda x: x[0] & x[2], lambda x: x[1] | x[0]], 3),

    ("Complementary skill matching", "algorithmic platform",
     # The match pairs COMPLEMENTARY (opposite) attributes -> a parity determination.
     # W'=S, S'=W XOR C, C'=S.
     [lambda x: x[1], lambda x: x[0] ^ x[2], lambda x: x[1]], 3),

    # ---- Class 3: ALGORITHMIC-INSTITUTIONAL GATEKEEPERS -----------------------------
    ("Hiring / applicant-tracking system", "algorithmic-institutional",
     # Strict mediation: applicant and manager never meet; the ATS commits forward/reject
     # as a joint function of resume signal and configured profile.  (Paper 2's triad.)
     [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]], 3),

    ("Content moderation (creator-platform-audience)", "algorithmic-institutional",
     # Creator and audience reach each other only through the platform's allow/rank/remove
     # determination, a joint function of content and audience-policy.  Strict mediation.
     [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]], 3),

    # ---- Class 4: HUMAN-MEDIATED INTERMEDIARIES (the contrast class) ----------------
    ("Court (judge between parties)", "human-mediated",
     # Plaintiff and defendant reach each other ONLY through what the judge admits/rules,
     # a determination joint in both parties' submissions.  Human in the mediator seat;
     # SAME strict-mediation structure as Uber/ATS.  W'=S, S'=W&C, C'=S.
     [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]], 3),

    ("Healthcare staffing agency", "human-mediated",
     # PARTIAL mediation: the agency commits the placement match (S'=W&C), but the worker
     # and facility also coordinate directly once placed (each reads the other too).
     # Same structure as the freelance marketplace, human in the seat.
     [lambda x: x[1] | x[2], lambda x: x[0] & x[2], lambda x: x[1] | x[0]], 3),

    ("Real-estate broker", "human-mediated",
     # Partial mediation: the broker introduces and matches, but buyer and seller may
     # negotiate directly once introduced.  Same partial structure.
     [lambda x: x[1] | x[2], lambda x: x[0] & x[2], lambda x: x[1] | x[0]], 3),

    # ---- Higher-order (4-node): a determination binding more than three parties -----
    ("Rideshare, POOLED (driver + 2 riders)", "algorithmic platform (higher-order)",
     # The platform pools iff two compatible riders AND a driver are jointly available:
     # S' = W & C & D.  Each party follows the committed pool.  W'=S, C'=S, D'=S.
     # Node order: 0=rider1 (W), 1=platform (S), 2=rider2 (C), 3=driver (D).
     [lambda x: x[1], lambda x: x[0] & x[2] & x[3], lambda x: x[1], lambda x: x[1]], 4),

    ("Crowdwork (requester + platform + 2 workers)", "algorithmic platform (higher-order)",
     # The platform allocates a task iff the requester posts AND two workers are available
     # jointly: S' = W & C & D.  Higher-order strict mediation.
     [lambda x: x[1], lambda x: x[0] & x[2] & x[3], lambda x: x[1], lambda x: x[1]], 4),
]


if __name__ == "__main__":
    print("=" * 92)
    print("PAPER 3 — the typology placed on the triadic-demand scale (exact IIT-4.0 system Φ)")
    print("=" * 92)
    rows = []
    for name, cls, rules, n in ORGS:
        r = placement(rules, n)
        rows.append((name, cls, r))
        print(f"\n### {name}   [{cls}]   (n={n})")
        print(f"    connectivity (rows=from,cols=to):\n{r['cm']}")
        print(f"    max Φ = {r['max']:.4f}   mean Φ = {r['mean']:.4f}   MIP@max = {r['mip']}")

    print("\n" + "=" * 92)
    print("THE BASELINE — organization types sorted by triadic demand (max Φ)")
    print("=" * 92)
    for name, cls, r in sorted(rows, key=lambda t: t[2]["max"]):
        print(f"  Φ = {r['max']:5.2f}   {name:48s} [{cls}]")
    print("=" * 92)
    print("Contrast-class check: do human-mediated forms land at the same level as")
    print("algorithmic forms of the same structure?  (Court vs Uber/ATS; staffing/broker vs Upwork.)")
    print("=" * 92)
