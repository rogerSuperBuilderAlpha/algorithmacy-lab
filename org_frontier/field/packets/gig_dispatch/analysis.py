"""The gig-dispatch field-study analysis — runnable now, completed with elicited rules later.

This holds the pre-registered candidate model and the sensitivity battery the field study will run, so
a researcher can see the machinery and the predicted verdicts before collecting a single interview, then
replace the candidate rules with the elicited ones (step 4) and recompute. The four sensitivity forces
are the ones the verdict turns on; the interview guide and coding scheme are built to gather the evidence
that decides between them.

Run from the repo root:
    PYPHI_WELCOME_OFF=true PYTHONPATH=. python org_frontier/field/packets/gig_dispatch/analysis.py
"""

import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.threads.mediation_boundary._probe import probe, show

# Node order: 0 = D (driver), 1 = S (dispatch system), 2 = R (rider).
L = ("D", "S", "R")


def validate_instrument():
    """Step 6 — the two canonical controls must pass before any verdict is trusted."""
    decoupled = probe([lambda x: x[0], lambda x: x[1], lambda x: x[2]], L)   # no coupling -> dyadic
    coupled = probe([lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]], L)   # full triad -> triadic
    ok = decoupled["phi"] == 0.0 and coupled["phi"] > 0.0
    print(f"STEP 6 instrument controls: decoupled Φ={decoupled['phi']} (must be 0), "
          f"coupled Φ={coupled['phi']} (must be >0) -> {'PASS' if ok else 'FAIL'}")
    return ok


# ---------------------------------------------------------------------------------------------
# STEP 4/5 — the pre-registered candidate model. REPLACE each rule with the elicited one and its
# evidence (see coding_scheme.md). Until then these encode the hypothesis in pre_registration.md.
# ---------------------------------------------------------------------------------------------
CANDIDATE = {
    "D": lambda x: x[1],            # driver acts on the assigned match (D <- S)   [ELICIT]
    "S": lambda x: x[0] & x[2],     # dispatch commits a match reading driver and rider (S = D & R) [ELICIT]
    "R": lambda x: x[1],            # rider takes the offered match/price (R <- S)  [ELICIT]
}


def verdict(rules_dict, labels=L):
    return probe([rules_dict[k] for k in labels], labels)


def main():
    if not validate_instrument():
        print("instrument failed — do not read any verdict"); return

    print("\nSTEP 7 the verdict under the pre-registered candidate model (S commits, reading both parties):")
    show("candidate S=D&R", [CANDIDATE[k] for k in L], L)

    print("\nSTEP 8 the sensitivity battery — the four forces the verdict turns on:")
    print("  (the field study determines, from evidence, which of these the real arrangement is)")
    show("substitutable driver  S=(D1|D2)&R",
         [lambda x: x[1], lambda x: (x[0] | x[3]) & x[2], lambda x: x[1], lambda x: x[1]],
         ("D1", "S", "R", "D2"))
    show("pass-through  S=D (relay)", [lambda x: x[0], lambda x: x[0], lambda x: x[1]], L)
    show("store-not-commit  S stores, the human decides",
         [lambda x: x[1], lambda x: x[0], lambda x: x[1] & x[2]], L)
    show("spectator  support agent idle",
         [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1], lambda x: x[1]],
         ("D", "S", "R", "X"))
    print("\n  read: triadic (algorithmacy) under a true commit reading both; dyadic (literacy) if the")
    print("  driver is substitutable or the system only relays; a spectator sinks whole-Φ, so read the core.")


if __name__ == "__main__":
    main()
