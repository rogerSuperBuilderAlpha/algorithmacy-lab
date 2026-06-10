"""Q103: how the cause-effect structure changes under the program's operations.

Each operation has a known effect on the verdict: substitution collapses the triad (Q70), a tracking
memory preserves it while shifting the core to {M, R, Mem} (Q92), and recipient-side delegation puts the
triage agent in the core (Q68). This reads whether the cause-effect structure follows: whether
substitution empties the structure, and whether memory and delegation restructure it so the new party
enters the joint mechanism.

`joint_parties` returns the set of parties that appear in any higher-order (joint) distinction of a form,
with the dual type — the structural footprint of the coordination.

Imported by `probe_structure_under_operations.py`.
"""

import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.questions.q99_binding_distinction import forms as q99
from org_frontier.questions.q64_outreach_breadth_scaling import forms as q64
from org_frontier.questions.q92_stateful_mediator import forms as q92
from org_frontier.questions.q68_triage_gating import forms as q68

OPERATIONS = {
    "baseline_read_recipient": q99.read_recipient(),
    "substitution": (q64.substitutable(2), q64.labels(2)),
    "tracking_memory": q92.tracking_memory(),
    "delegation_triage": (q68.BIDIRECTIONAL, q68.LABELS),
}


def joint_parties(rules, labels):
    """Return (system_phi, dual_type, set of parties in any joint distinction of the integrated
    structure). The structure is integrated only when system Φ > 0; a factored form (Φ = 0) carries no
    joint mechanism binding the whole even if stray distinctions remain."""
    phi, dists = q99.ces(rules, labels)
    jp = set()
    if phi > 1e-9:
        for m, _p, _pd in dists:
            if len(m) >= 2:
                jp |= set(m)
    dtype = q99.dual_type(dists) if phi > 1e-9 else "none"
    return round(float(phi), 3), dtype, jp
