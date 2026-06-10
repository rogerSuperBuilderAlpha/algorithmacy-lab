"""Q107: repairing a damaged triad — is repair lever-specific or can it route around the damage?

A triadic form damaged on one lever — its binding broken (the mediator stops reading a party) or its
liveness broken (a party stops reading the mediator) — goes dyadic. The repair question is whether the
cheapest fix must restore the damaged lever, or whether editing a different lever restores the triad.

Using the 256-form encoding (worker read bits 0-1, counterpart read bits 2-3, mediator function bits 4-7),
the read-recipient triad is (0,1, 0,1, 0,0,0,1). Binding damage makes the mediator function independent of
the counterpart (the broadcast); liveness damage makes the counterpart's read of the mediator constant.
Repair distance and the bits that achieve it are read with Q105's construction-distance machinery.

Imported by `probe_repair.py`.
"""

import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.questions.q105_construction_distance import forms as q105

# bit ranges by lever, in the strict-mediation encoding
COUNTERPART_READ_BITS = (2, 3)      # the counterpart's read of the mediator (a liveness lever)
MEDIATOR_BITS = (4, 5, 6, 7)        # the mediator's two-input function (the binding lever)

READ_RECIPIENT = (0, 1, 0, 1, 0, 0, 0, 1)        # triadic
BINDING_DAMAGED = (0, 1, 0, 1, 0, 1, 0, 1)       # mediator ignores the counterpart (broadcast)
LIVENESS_DAMAGED = (0, 1, 0, 0, 0, 0, 0, 1)      # counterpart's read of the mediator made constant

DAMAGE = {
    "binding_damaged": (BINDING_DAMAGED, MEDIATOR_BITS),
    "liveness_damaged": (LIVENESS_DAMAGED, COUNTERPART_READ_BITS),
}


def repair(bits, triadic):
    """Minimal repair distance to a triadic form and the bits achieving a distance-1 repair."""
    return q105.construction_distance(bits, triadic)
