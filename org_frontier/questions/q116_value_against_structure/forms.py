"""Q116: strategic value against structural contribution — closing the political-economy wave.

The wave measured each party's strategic value, its Shapley value of integration (Q111). The cause-effect
wave measured each party's structural contribution, the φ_d its own distinction carries in the cause-effect
structure (Q99, Q104). This asks whether the two are the same quantity: does a party's strategic worth equal
its structural depth?

Two readings of each party's share of the coordination:
- **strategic** — normalized Shapley value of subsystem-Φ (Q111).
- **structural** — normalized singleton φ_d: the φ_d of the party's own distinction (mechanism = {party}) in
  the cause-effect structure at the integrating state (Q99).

The panel runs both across the read-recipient triad, the bidirectional principal (Q114), and the all-required
market at N = 2 and N = 3 (Q85), from the minimal symmetric case to the asymmetric and the scaled.

Imported by `probe_value_against_structure.py`.
"""

import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.questions.q111_shapley_value import forms as q111
from org_frontier.questions.q99_binding_distinction import forms as q99
from org_frontier.questions.q114_principal_rent import forms as q114
from org_frontier.questions.q85_agent_market import forms as q85


def _normalize(d):
    t = sum(d.values())
    return {k: (v / t if t else 0.0) for k, v in d.items()}


def structural_shares(rules, labels):
    """Each party's normalized singleton φ_d (the φ_d of its own distinction)."""
    _, dists = q99.ces(rules, labels)
    sing = {L: 0.0 for L in labels}
    for mech, _purview, phi_d in dists:
        if len(mech) == 1:
            sing[mech[0]] = phi_d
    return _normalize(sing)


def strategic_shares(rules, labels):
    """Each party's normalized Shapley value of integration (Q111)."""
    sv, _ = q111.shapley(rules, labels)
    return _normalize({L: sv[L] for L in labels})


def both(rules, labels):
    return structural_shares(rules, labels), strategic_shares(rules, labels)


def panel():
    """(name, rules, labels) from the minimal symmetric case to the asymmetric and the scaled."""
    return [
        ("triad", *q111.read_recipient()),
        ("principal", q114.BIDIRECTIONAL, q114.LABELS),
        ("market2", q85.all_required(2), q85.labels(2)),
        ("market3", q85.all_required(3), q85.labels(3)),
    ]


def concordant(struct, strat, labels, tol=0.01):
    """True if no party pair is ranked oppositely by the two measures (ties within tol ignored)."""
    for i in range(len(labels)):
        for j in range(i + 1, len(labels)):
            a, b = labels[i], labels[j]
            ds = strat[a] - strat[b]
            df = struct[a] - struct[b]
            if abs(ds) > tol and ds * df < 0:
                return False
    return True


def max_share_gap(struct, strat, labels):
    return max(abs(struct[L] - strat[L]) for L in labels)


def top_party(strat, labels):
    return max(labels, key=lambda L: strat[L])
