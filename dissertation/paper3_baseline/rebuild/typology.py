"""Paper 3 rebuild — placing a typology of organization types on the triadic-demand scale.

Each organization is modeled as an application-layer Worker–System–Counterpart system (a
fourth party for higher-order forms) under Paper 2's pre-registered state-individuation rule.
The determination structure for each is fixed before computing, written in the docstring from
how that organization actually coordinates its parties, not chosen for a target Φ. Exact
IIT-4.0 system Φ is computed and whatever results is reported.

The scale's levels come from structure, not from the seat of the mediator. A court and an
algorithmic platform of the same strict-mediation structure land at the same Φ. The equality
is true by construction, and that is the point: the model is indifferent to whether the
mediator is a person or software once the determination structure is fixed.

Run:  ~/iit-playground/venv-4.0/bin/python dissertation/paper3_baseline/rebuild/typology.py
"""

import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)

from phi_core import placement


# Node order: 0=W (worker/one party), 1=S (mediator), 2=C (counterpart), 3=D (fourth party).
# rules[j](x) -> node j's next value; x is the current state tuple.

ORGS = [
    # ---- Class 1: dyadic baselines (no constitutive mediator) ------------------------
    ("Direct exchange (no mediator)", "dyadic baseline",
     # Parties deal directly; the system is inert. W'=C, S'=S, C'=W.
     [lambda x: x[2], lambda x: x[1], lambda x: x[0]], 3),

    ("Chat with a language model", "dyadic baseline",
     # Paper 2's dyadic limit: a two-party loop, nothing couples a third. W'=S, S'=W, C'=C.
     [lambda x: x[1], lambda x: x[0], lambda x: x[2]], 3),

    # ---- Class 2: algorithmic platforms ---------------------------------------------
    ("Rideshare, solo (Uber/Lyft)", "algorithmic platform",
     # Strict mediation: driver and rider reach each other only through the dispatch the
     # platform commits as a joint function of both. W'=S, S'=W∧C, C'=S.
     [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]], 3),

    ("Food delivery (courier-platform-customer)", "algorithmic platform",
     [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]], 3),

    ("Freelance marketplace (Upwork)", "algorithmic platform",
     # Partial mediation: the platform matches, but client and freelancer also coordinate
     # directly. W'=S∨C, S'=W∧C, C'=S∨W.
     [lambda x: x[1] | x[2], lambda x: x[0] & x[2], lambda x: x[1] | x[0]], 3),

    ("Complementary skill matching", "algorithmic platform",
     # The match pairs complementary attributes, a parity determination. W'=S, S'=W⊕C, C'=S.
     [lambda x: x[1], lambda x: x[0] ^ x[2], lambda x: x[1]], 3),

    # ---- Class 3: algorithmic-institutional gatekeepers -----------------------------
    ("Hiring / applicant-tracking system", "algorithmic-institutional",
     # Strict mediation: applicant and manager never meet; the ATS commits forward/reject
     # jointly. W'=S, S'=W∧C, C'=S.
     [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]], 3),

    ("Content moderation (creator-platform-audience)", "algorithmic-institutional",
     [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]], 3),

    # ---- Class 4: human-mediated intermediaries (the contrast class) ----------------
    ("Court (judge between parties)", "human-mediated",
     # Plaintiff and defendant reach each other only through the judge's rulings, joint in
     # both submissions. Human in the seat; same strict-mediation structure. W'=S, S'=W∧C, C'=S.
     [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]], 3),

    ("Healthcare staffing agency", "human-mediated",
     # Partial mediation: the agency matches, but worker and facility also coordinate directly
     # once placed. Same structure as the freelance marketplace, human in the seat.
     [lambda x: x[1] | x[2], lambda x: x[0] & x[2], lambda x: x[1] | x[0]], 3),

    ("Real-estate broker", "human-mediated",
     [lambda x: x[1] | x[2], lambda x: x[0] & x[2], lambda x: x[1] | x[0]], 3),

    # ---- Higher-order (4-node): a determination binding more than three parties ------
    ("Rideshare, POOLED (driver + 2 riders)", "algorithmic platform (higher-order)",
     # The platform pools iff two riders and a driver are jointly available: S'=W∧C∧D.
     # Each party follows the committed pool. Node order: 0=rider1, 1=platform, 2=rider2, 3=driver.
     [lambda x: x[1], lambda x: x[0] & x[2] & x[3], lambda x: x[1], lambda x: x[1]], 4),

    ("Crowdwork (requester + platform + 2 workers)", "algorithmic platform (higher-order)",
     # The platform allocates iff the requester posts and two workers are jointly available:
     # S'=W∧C∧D. Higher-order strict mediation.
     [lambda x: x[1], lambda x: x[0] & x[2] & x[3], lambda x: x[1], lambda x: x[1]], 4),
]


if __name__ == "__main__":
    print("=" * 92)
    print("PAPER 3 rebuild — the typology placed on the triadic-demand scale (exact IIT-4.0 Φ)")
    print("=" * 92)
    rows = []
    for name, cls, rules, n in ORGS:
        r = placement(rules, n)
        rows.append((name, cls, r))
        print(f"\n### {name}   [{cls}]   (n={n})")
        print(f"    max Φ = {r['max']:.4f}   mean Φ = {r['mean']:.4f}   "
              f"MIP@max = {r['mip']}   reachable={r['n_reachable']}")

    print("\n" + "=" * 92)
    print("THE BASELINE — organization types sorted by triadic demand (max Φ)")
    print("=" * 92)
    for name, cls, r in sorted(rows, key=lambda t: t[2]["max"]):
        print(f"  Φ = {r['max']:5.2f}   {name:48s} [{cls}]")
    print("=" * 92)
    print("Contrast-class check: human-mediated forms should land at the same level as")
    print("algorithmic forms of the same structure (court vs Uber/ATS; staffing/broker vs Upwork).")
