"""Shared helpers for Q60 Thompson back-channel interdependence typing probes."""

import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.classifier.classifier import cm_from_rules  # noqa: E402
from org_frontier.probes.lib import verdict  # noqa: E402
from org_frontier.questions.q43_thompson_interdependence.probe_thompson_primitives import (  # noqa: E402
    has_feedback_cycle,
)
from org_frontier.questions.q56_symmetric_complete_mip.mip_geometry_utils import (  # noqa: E402
    PHI_TOL,
    instrument_control,
)
from org_frontier.questions.q57_channel_direction_mip.direction_mip_utils import (  # noqa: E402
    back_channel_recipient,
)
from org_frontier.questions.q59_directed_cut_edges.cut_edge_utils import (  # noqa: E402
    COUNTERPART_ONLY_EXCL,
    COUNTERPART_ONLY_TIED,
    WORKER_ONLY_EXCL,
    WORKER_ONLY_TIED,
    edge_detail_rows,
    expected_templates,
)

LABELS = ("W", "S", "C")
MAX_PHI = 2.0
PANEL_SIZE = 16


def return_path_type(rules, recipient):
    """Q43 return-path sequential vs reciprocal typing on back-channel forms."""
    cm = cm_from_rules(rules)
    if recipient == "W":
        if cm[1, 2] and not cm[0, 2]:
            return "sequential"
        return "other"
    if recipient == "C":
        if cm[0, 2]:
            return "reciprocal"
        return "other"
    return "other"


def template_matches_type(thompson_type, only_tied, only_excl):
    """True iff edge templates match the Thompson subpanel class."""
    if thompson_type == "sequential":
        return only_tied == WORKER_ONLY_TIED and only_excl == WORKER_ONLY_EXCL
    if thompson_type == "reciprocal":
        return only_tied == COUNTERPART_ONLY_TIED and only_excl == COUNTERPART_ONLY_EXCL
    return False


def enriched_panel():
    """Sixteen ceiling pairs with Thompson typing and verdict fields."""
    rows = []
    for row in edge_detail_rows():
        rules = row["rules"]
        recipient = back_channel_recipient(row["topology"])
        v = verdict(rules, LABELS)
        thompson = return_path_type(rules, recipient)
        exp_tied, exp_excl = expected_templates(row["topology"])
        rows.append({
            **row,
            "recipient": recipient,
            "thompson_type": thompson,
            "structure": v.structure,
            "max_phi": float(v.max_phi),
            "mip_partition": v.mip_partition,
            "feedback_cycle": has_feedback_cycle(rules),
            "only_tied": row["only_tied"],
            "only_excl": row["only_excl"],
            "expected_tied": exp_tied,
            "expected_excl": exp_excl,
            "template_match": template_matches_type(
                thompson, row["only_tied"], row["only_excl"]
            ),
            "recipient_match": (
                (recipient == "W" and thompson == "sequential")
                or (recipient == "C" and thompson == "reciprocal")
            ),
        })
    return rows
