"""Q110: reversibility of the dyad/triad boundary — is it as cheap to build a triad as to break one?

Q93 read the collapse side (fragility margin: the edits to break a triad) and Q105 the build side
(construction distance: the edits to build a triad). This compares the two distributions over the 256-form
family. Hamming distance is symmetric form to form, so the question is distributional: are triads as far
from dyads as dyads are from triads, or is the boundary thin from one side and thicker from the other?

`fragility_margin` is the minimal Hamming distance from a triadic form to any dyadic form; the construction
distance reuses Q105.

Imported by `probe_reversibility.py`.
"""

import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.questions.q105_construction_distance import forms as q105


def _hamming(a, b):
    return sum(1 for i in range(8) if a[i] != b[i])


def fragility_margin(bits, dyadic):
    """Minimal Hamming distance from a triadic form to any dyadic form."""
    return min(_hamming(bits, d) for d in dyadic)


def both_distributions():
    """Return (fragility margins over triadic forms, construction distances over dyadic forms)."""
    dyadic, triadic = q105.classify_family()
    frag = [fragility_margin(t, dyadic) for t in triadic]
    cons = [q105.construction_distance(d, triadic)[0] for d in dyadic]
    return frag, cons
