"""Q105: construction distance — the minimal edit that builds a triad from a dyad.

Q93 read the fragility margin, how many single-bit flips collapse a triadic form. This reads the dual: how
many flips build a triadic form from a dyadic one. The 256 strict-mediation forms are the 8-bit points of a
hypercube (a 2-bit read for each outer party off the mediator, a 4-bit mediator function), and a single-bit
flip moves to a Hamming-adjacent form, so the construction distance of a dyadic form is its minimum Hamming
distance to any triadic form.

The eight bits, in order: the worker's read (bits 0-1), the counterpart's read (bits 2-3), and the
mediator's two-input function (bits 4-7). Bits 4-7 are the mediator's; bits 0-3 are the parties' reads.

Imported by `probe_construction_distance.py`.
"""

import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.questions.q93_fragility_margin import forms as q93

MEDIATOR_BITS = (4, 5, 6, 7)


def classify_family():
    """Return (dyadic_bits_list, triadic_bits_set) over the 256-form family."""
    dyadic, triadic = [], []
    for bits, rules in q93.enumerate_family():
        (triadic if q93.is_triadic(rules) else dyadic).append(bits)
    return dyadic, triadic


def _hamming(a, b):
    return sum(1 for i in range(8) if a[i] != b[i])


def construction_distance(bits, triadic):
    """Minimal Hamming distance from a dyadic form to any triadic form, and the set of bit positions that
    achieve a distance-1 build (empty if distance > 1)."""
    dmin = min(_hamming(bits, t) for t in triadic)
    one_step_bits = set()
    if dmin == 1:
        for t in triadic:
            if _hamming(bits, t) == 1:
                one_step_bits.add(next(i for i in range(8) if bits[i] != t[i]))
    return dmin, one_step_bits


def broadcast_bits():
    """The broadcast form's 8-bit encoding: W'=S, C'=S, S'=W (mediator ignores the counterpart)."""
    # tW = (0,1): W' = S ;  tC = (0,1): C' = S ;  tS over (W | C<<1): S' = W  -> (0,1,0,1)
    return (0, 1, 0, 1, 0, 1, 0, 1)
