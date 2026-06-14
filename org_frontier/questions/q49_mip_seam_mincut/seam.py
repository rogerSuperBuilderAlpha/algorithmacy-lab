"""Q49 — seam-reading helpers shared by the probes.

The seam of a coordination form is read from the minimum-information-partition (MIP) tie set at the
form's max-Φ reachable state. PyPhi returns one MIP representative plus the full tie set (`sia.ties`);
this module reads which parties are severed as a singleton across the tied two-part partitions.

For n=3 every two-part partition is a 1+2 split, so each names exactly one severed singleton:
`{W,SC}` -> W, `{WS,C}` -> C, `{S,WC}` -> S. A tie set holding only the complete partition `{W,S,C}`
gives an empty seam set.
"""

import os
import re
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

import pyphi
from pyphi import new_big_phi

from org_frontier.classifier.classifier import classify_rules, tpm_from_rules, cm_from_rules

pyphi.config.PROGRESS_BARS = False
pyphi.config.PARALLEL = False

LABELS = ("W", "S", "C")
PHI_EPS = 1e-9

_TWO_PART = re.compile(r"2 parts:\s*\{([^}]*)\}")


def _singleton_of(part_line, labels):
    """Given a partition repr line, return the severed singleton label, or None.

    A two-part line reads `2 parts: {W,SC}` — the groups are comma-separated, each group a run of
    labels. Return the label that stands alone as its own group.
    """
    m = _TWO_PART.search(part_line)
    if not m:
        return None
    groups = [g for g in m.group(1).split(",")]
    # Each group is a concatenation of single-character labels (W, S, C). A singleton group has len 1.
    singles = [g for g in groups if len(g) == 1]
    return singles[0] if len(singles) == 1 and len(groups) == 2 else (singles[0] if singles else None)


def mip_ties(rules, labels=LABELS):
    """Return (verdict, sia, tie_lines) for a form, read at its max-Φ reachable state.

    `tie_lines` is the list of first-line partition reprs of the tied MIPs. Returns (verdict, None, [])
    if the form is dyadic (no MIP to read)."""
    v = classify_rules(rules, labels=labels)
    if v.structure != "triadic" or v.mip_state is None:
        return v, None, []
    tpm, cm = tpm_from_rules(rules), cm_from_rules(rules)
    net = pyphi.Network(tpm, cm=cm, node_labels=labels)
    sub = pyphi.Subsystem(net, tuple(v.mip_state))
    sia = new_big_phi.sia(sub)
    lines = [str(t.partition).splitlines()[0].strip() for t in sia.ties]
    return v, sia, lines


def seam_set(rules, labels=LABELS):
    """The set of parties severed as a singleton by some tied two-part MIP. Empty if dyadic or if the
    tie set holds only the complete partition."""
    _, _, lines = mip_ties(rules, labels=labels)
    out = set()
    for line in lines:
        s = _singleton_of(line, labels)
        if s is not None:
            out.add(s)
    return out


def coupling_degree(rules, labels=LABELS):
    """Total connectivity-matrix degree (in + out, to other parties) per label, self-loops excluded."""
    cm = cm_from_rules(rules)
    n = cm.shape[0]
    deg = {}
    for x in range(n):
        d = sum(cm[x, j] + cm[j, x] for j in range(n) if j != x)
        deg[labels[x]] = int(d)
    return deg


def mincut_set(rules, labels=LABELS):
    """The connectivity min-cut singleton set: the parties minimizing total crossing-edge degree."""
    deg = coupling_degree(rules, labels=labels)
    lo = min(deg.values())
    return {p for p, d in deg.items() if d == lo}
