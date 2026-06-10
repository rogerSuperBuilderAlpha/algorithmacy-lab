"""Q108: controllability — which party, varied alone, steers the verdict, and how finely.

A designer who can set one party's reads while the others stay fixed has a control over the verdict. This
varies each party's function of the read-recipient triad (encoded over the 256-form family) and counts how
many of its settings give a triadic verdict. A party is a control node if both verdicts are reachable by
varying only its function.

The eight bits: worker's read (0-1), counterpart's read (2-3), mediator's two-input function (4-7). The
read-recipient triad is (0,1, 0,1, 0,0,0,1). Varying the worker or counterpart sweeps 4 one-input
functions; varying the mediator sweeps 16 two-input functions.

Imported by `probe_controllability.py`.
"""

import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.questions.q93_fragility_margin import forms as q93

READ_RECIPIENT = (0, 1, 0, 1, 0, 0, 0, 1)
PARTY_BITS = {
    "worker": (0, 1),
    "counterpart": (2, 3),
    "mediator": (4, 5, 6, 7),
}


def control_sweep(base, bit_positions):
    """Vary the bits at `bit_positions` over all settings, holding the rest of `base` fixed; return the
    list of (setting, is_triadic) over the 2^len(bit_positions) settings."""
    k = len(bit_positions)
    out = []
    for v in range(2 ** k):
        bits = list(base)
        for j, pos in enumerate(bit_positions):
            bits[pos] = (v >> j) & 1
        out.append((v, q93.is_triadic(q93._rules_from_bits(tuple(bits)))))
    return out
