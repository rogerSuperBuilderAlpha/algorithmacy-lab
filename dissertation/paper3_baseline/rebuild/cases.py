"""Paper 3 rebuild — the five case-study models (exact IIT-4.0 system Φ).

Each of the five real organizations in the case studies is modeled as an application-layer
Worker–System–Counterpart system (a fourth party for the higher-order case) under Paper 2's
pre-registered individuation rule. The determination structure for each is fixed here, BEFORE
computing, from the documented coordination mechanism in
`research/organization_mechanisms.md` — not chosen for a target Φ.

The slate is a diverse-case theoretical-sampling design (Seawright & Gerring 2008): vary the
determination structure, hold party count fixed across cases 1–4. The two equal-Φ pairs
(Uber ≈ exchange at 2.00; Upwork ≈ ManpowerGroup at 0.83) differ on the mediator's seat, not its
structure — the structure-not-seat headline. Case 5 (MTurk) extends to a determination binding
more than three parties.

Run:  ~/iit-playground/venv-4.0/bin/python dissertation/paper3_baseline/rebuild/cases.py
"""

import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)

from phi_core import placement


# rules[j](x) -> node j's next value. Node order: 0=W (worker/one party), 1=S (mediator),
# 2=C (counterpart), 3=D (fourth party, higher-order only).

CASES = [
    ("Uber (ride-hailing)", "strict mediation", "transportation", "algorithmic",
     # Driver and rider reach each other only through the platform's joint dispatch; off-app
     # contact is contractually restricted. W'=S, S'=W∧C, C'=S.
     [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]], 3),

    ("NYSE / Nasdaq (securities exchange)", "strict mediation", "financial markets", "market institution",
     # Buyer and seller never transact directly; the exchange commits the match (and the CCP novates).
     # Same strict-mediation structure as Uber, different seat. W'=S, S'=W∧C, C'=S.
     [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]], 3),

    ("Upwork (freelance marketplace)", "partial mediation", "professional services", "algorithmic",
     # The platform matches, but client and freelancer coordinate directly on-platform; only the
     # off-platform channel is policed. W'=S∨C, S'=W∧C, C'=S∨W.
     [lambda x: x[1] | x[2], lambda x: x[0] & x[2], lambda x: x[1] | x[0]], 3),

    ("ManpowerGroup (staffing firm)", "partial mediation", "staffing", "human-institutional",
     # The agency commits the placement (employer of record), but the client directs the day-to-day
     # work on-site — a continuous direct channel. Same structure as Upwork, different seat.
     [lambda x: x[1] | x[2], lambda x: x[0] & x[2], lambda x: x[1] | x[0]], 3),

    ("Amazon Mechanical Turk (crowdwork)", "higher-order strict mediation", "crowdwork", "algorithmic",
     # Requester and workers connect only through the platform; a single HIT can bind many workers,
     # and Amazon sits in the payment path. One determination binds >3 parties. S'=W∧C∧D.
     [lambda x: x[1], lambda x: x[0] & x[2] & x[3], lambda x: x[1], lambda x: x[1]], 4),
]


if __name__ == "__main__":
    print("=" * 96)
    print("PAPER 3 rebuild — the five case-study models (exact IIT-4.0 system Φ)")
    print("=" * 96)
    rows = []
    for name, structure, industry, seat, rules, n in CASES:
        r = placement(rules, n)
        rows.append((name, structure, industry, seat, r, n))
        print(f"\n### {name}   [{structure}; {industry}; {seat}]   (n={n})")
        print(f"    max Φ = {r['max']:.4f}   mean Φ = {r['mean']:.4f}   "
              f"MIP@max = {r['mip']}   reachable = {r['n_reachable']}")

    print("\n" + "=" * 96)
    print("THE FIVE CASES — placed by structure (max Φ)")
    print("=" * 96)
    for name, structure, industry, seat, r, n in sorted(rows, key=lambda t: t[4]["max"]):
        print(f"  Φ = {r['max']:5.2f}   {name:42s} [{structure:28s}] {seat}")
    print("=" * 96)
    print("Equal-Φ seat-contrast pairs (structure sets the score, not the seat):")
    print("  2.00 : Uber (algorithmic)  ==  NYSE/Nasdaq (market institution)")
    print("  0.83 : Upwork (algorithmic)  ==  ManpowerGroup (human-institutional)")
    print("  3.00 : Amazon Mechanical Turk — higher-order (n=4), cross-node Φ not strictly comparable")
