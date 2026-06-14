"""Q104: the load-bearing distinction — which element of the structure carries the integration.

Q93 found the verdict fragile to a single bit-flip. This reads the cause-effect analogue: which distinction
holds the integration, and which edge, removed, collapses it. For the read-recipient triad the joint
distinction {E, R} → {M} carries φ_d equal to the system Φ; knocking out the edge that enables it (the
mediator's read of a party) should collapse the verdict, while a downstream edge should not.

`distinctions_by_phi` returns the distinctions ranked by φ_d; `knockouts` recomputes the verdict after
removing each of the triad's edges.

Imported by `probe_load_bearing.py`.
"""

import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.probes.lib import verdict
from org_frontier.questions.q99_binding_distinction import forms as q99

LABELS = ("E", "M", "R")


def read_recipient():
    return [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]], LABELS


def distinctions_by_phi(rules, labels):
    """(mechanism, effect purview, φ_d) sorted by descending φ_d, with the system Φ."""
    phi, dists = q99.ces(rules, labels)
    return round(float(phi), 3), sorted(dists, key=lambda d: -d[2])


# Edge knockouts of the read-recipient triad. Each removes one read by collapsing the rule.
KNOCKOUTS = {
    # mediator's reads of the parties — the edges that enable the joint distinction
    "M_reads_R": [lambda x: x[1], lambda x: x[0], lambda x: x[1]],            # M' = E  (drop R->M)
    "M_reads_E": [lambda x: x[1], lambda x: x[2], lambda x: x[1]],            # M' = R  (drop E->M)
    # downstream reads — the parties reading the mediator
    "E_reads_M": [lambda x: x[0], lambda x: x[0] & x[2], lambda x: x[1]],     # E' = E  (drop M->E)
    "R_reads_M": [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[2]],     # R' = R  (drop M->R)
}


def knockout_verdicts():
    """Verdict and Φ after each edge knockout."""
    out = {}
    for name, rules in KNOCKOUTS.items():
        v = verdict(rules, LABELS)
        out[name] = (v.structure, round(float(v.max_phi), 3))
    return out
