"""Paper 3 rebuild — the dyadic negative-control class (does the instrument return Φ=0?).

The five corporate cases in cases.py all score Φ>0 (partial, strict, higher-order). A classifier
that only ever returns "triad" is worthless. This file is the falsification class: five real
coordination forms an analyst would judge DYADIC — the third element conveys but does not
constitute, or the parties reach each other directly, or there is no real third party — modeled
faithfully and pre-registered BEFORE computing. The prediction is Φ=0 (moderated dyad). Any case
that does NOT come up dyadic is reported as a finding, not hidden.

The five span the ways a moderated dyad arises (Paper 2's conditions failing):
  1. Telecom voice call — a direct channel / route-around (parties talk directly; carrier inert).
  2. Email — carry, not commit (the provider forwards; the recipient's state does not gate routing).
  3. Enterprise SaaS tool — two-party human-machine; no counterpart coupled (Paper 2's dyadic limit).
  4. Craigslist — a listing board the parties route past, transacting directly off-platform.
  5. Payment processor — the boundary case: the parties struck the deal directly; the processor
     settles. Coded two ways to show where the dyad/triad line falls.

Run: ~/iit-playground/venv-4.0/bin/python dissertation/paper3_baseline/rebuild/dyadic_cases.py
"""

import os, sys
_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)

from phi_core import placement

# Node order: 0=W (party A / worker), 1=S (intermediary), 2=C (party B / counterpart).

DYADIC = [
    ("Telecom voice call (AT&T/Verizon)", "direct channel / route-around", "telecom",
     # The carrier connects the parties, then they talk directly on an open line; the carrier is
     # the inert medium. Parties read each other; S does not commit a joint determination.
     # W'=C, S'=S, C'=W.
     [lambda x: x[2], lambda x: x[1], lambda x: x[0]]),

    ("Email provider (Gmail/Microsoft)", "carry, not commit", "communications",
     # Store-and-forward: the provider carries the sender's message to the recipient the sender
     # addressed; the recipient's state does not enter the routing. Pass-through mediator.
     # W'=S, S'=W, C'=S.
     [lambda x: x[1], lambda x: x[0], lambda x: x[1]]),

    ("Enterprise SaaS tool (e.g. a CRM a worker uses)", "two-party, counterpart decoupled", "software",
     # A worker and a tool, no third party coordinated — Paper 2's dyadic limit (chat with a model).
     # W'=S, S'=W, C'=C.
     [lambda x: x[1], lambda x: x[0], lambda x: x[2]]),

    ("Craigslist (classified listings)", "route-around (parties transact off-platform)", "marketplace",
     # The board displays a poster's listing; a responder sees it and contacts the poster directly,
     # and the two transact off-platform. The platform carries the listing; the parties keep a
     # direct channel. W'=S∨C, S'=W, C'=S∨W.
     [lambda x: x[1] | x[2], lambda x: x[0], lambda x: x[1] | x[0]]),

    ("Payment processor — agreed deal (Visa/Stripe)", "boundary: parties chose each other", "payments",
     # The buyer and seller struck the deal directly (a direct channel); the processor authorizes
     # and settles as a joint function of both. The coordination between the parties is theirs;
     # the processor moves the value. W'=C∨S, S'=W∧C, C'=W∨S.
     [lambda x: x[2] | x[1], lambda x: x[0] & x[2], lambda x: x[0] | x[1]]),
]

# A rival coding for the payment processor, to show where the dyad/triad line falls: if the parties
# did NOT choose each other and reach each other only through the processor's authorization (no
# direct channel), it is strict mediation, Φ=2.00 — a different organization (e.g. a processor that
# also matches), not the agreed-deal case above.
RIVAL = [
    ("Payment processor — processor matches (no direct channel)", "rival: strict mediation", "payments",
     [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]),
]


def run(rows, header):
    print("\n" + "=" * 96)
    print(header)
    print("=" * 96)
    out = []
    for name, structure, industry, rules in rows:
        r = placement(rules, 3)
        verdict = "MODERATED DYAD" if r["max"] <= 1e-9 else "NOT DYADIC (Φ>0)"
        out.append((name, structure, r, verdict))
        print(f"\n### {name}   [{structure}; {industry}]")
        print(f"    max Φ = {r['max']:.4f}   mean Φ = {r['mean']:.4f}   MIP@max = {r['mip']}   "
              f"reachable = {r['n_reachable']}")
        print(f"    -> {verdict}")
    return out


if __name__ == "__main__":
    rows = run(DYADIC, "PAPER 3 — the dyadic negative-control class (predicted Φ=0)")
    run(RIVAL, "RIVAL CODING (the boundary: same domain, no direct channel -> strict mediation)")
    print("\n" + "=" * 96)
    print("SUMMARY — did the cases we judged dyadic come up dyadic?")
    print("=" * 96)
    n_dyad = sum(1 for _, _, r, _ in rows if r["max"] <= 1e-9)
    for name, structure, r, verdict in sorted(rows, key=lambda t: t[2]["max"]):
        print(f"  Φ = {r['max']:5.2f}   {verdict:18s} {name}")
    print(f"\n  {n_dyad} of {len(rows)} came up dyadic (Φ=0). Any Φ>0 case is a finding to report, "
          f"not hide.")
