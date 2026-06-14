"""Q117: a Φ-free necessary-and-sufficient test for triadicity on the strict-mediation family.

The program reads the verdict with exact IIT-4.0 Φ. This asks whether a predicate computed without Φ, from
the form's truth tables alone, reproduces that verdict on the whole 256-form strict-mediation family (Q93).

Three predicates over a form's eight bits (worker read tW, counterpart read tC, mediator table tS):

- `cycle_present` — the effective feedback cycle: the mediator depends on both outer parties, and both outer
  parties depend on the mediator. Pure topology, read off which inputs each table actually uses.
- `phi_free_verdict` — the cycle plus a logical composition condition: a parity mediator (XOR/XNOR) always
  binds; a non-parity mediator binds iff the outer reads' phase alignment matches the mediator's symmetry
  under swapping its two inputs.
- `q93.is_triadic` — the exact-Φ oracle, the ground truth.

`compare_family` runs all three across the family and returns the confusion of each Φ-free predicate against
the oracle, with the breakdown over the full-cycle forms.

Imported by `probe_phi_free_test.py`.
"""

import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.questions.q93_fragility_margin import forms as q93

PARITY = ((0, 1, 1, 0), (1, 0, 0, 1))      # XOR, XNOR


def _tables(bits):
    return (bits[0], bits[1]), (bits[2], bits[3]), (bits[4], bits[5], bits[6], bits[7])


def _mediator_uses_both(tS):
    dep_w = (tS[0] != tS[1]) or (tS[2] != tS[3])
    dep_c = (tS[0] != tS[2]) or (tS[1] != tS[3])
    return dep_w, dep_c


def cycle_present(bits):
    """Topology only: the effective feedback cycle through all three parties.

    Both outer parties read the mediator (tW, tC non-constant) and the mediator reads both outer parties.
    """
    tW, tC, tS = _tables(bits)
    e_ws = tW[0] != tW[1]                   # worker effectively reads the mediator
    e_cs = tC[0] != tC[1]                   # counterpart effectively reads the mediator
    dep_w, dep_c = _mediator_uses_both(tS)  # mediator effectively reads both outer parties
    return e_ws and e_cs and dep_w and dep_c


def phi_free_verdict(bits):
    """Cycle plus the logical composition condition. True predicts triadic."""
    if not cycle_present(bits):
        return False
    tW, tC, tS = _tables(bits)
    if tS in PARITY:
        return True                         # a parity mediator always binds the cycle
    w_identity = (tW == (0, 1))             # worker copies vs inverts the mediator
    c_identity = (tC == (0, 1))
    antisymmetric = (tS[1] != tS[2])        # mediator asymmetric under swapping its two inputs
    return (w_identity == c_identity) != antisymmetric


def compare_family():
    """Confusion of each Φ-free predicate against the exact-Φ oracle, with the full-cycle breakdown."""
    res = {
        "n": 0, "triadic": 0,
        "cycle": {"tp": 0, "fp": 0, "fn": 0, "tn": 0},
        "full": {"tp": 0, "fp": 0, "fn": 0, "tn": 0},
        "cycle_forms": {"triadic": 0, "dyadic": 0},
    }
    for bits, rules in q93.enumerate_family():
        res["n"] += 1
        truth = q93.is_triadic(rules)
        res["triadic"] += truth
        for key, pred in (("cycle", cycle_present(bits)), ("full", phi_free_verdict(bits))):
            cell = "tp" if (truth and pred) else "fn" if (truth and not pred) else \
                   "fp" if (not truth and pred) else "tn"
            res[key][cell] += 1
        if cycle_present(bits):
            res["cycle_forms"]["triadic" if truth else "dyadic"] += 1
    return res
