"""Shared helpers for Q61 MIP seam vs return-path typing probes."""

import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.probes.lib import verdict  # noqa: E402
from org_frontier.questions.q49_mip_seam_mincut.seam import seam_set  # noqa: E402
from org_frontier.questions.q56_symmetric_complete_mip.mip_geometry_utils import (  # noqa: E402
    OUTER_C,
    OUTER_W,
    PHI_TOL,
    instrument_control,
)
from org_frontier.questions.q57_channel_direction_mip.direction_mip_utils import (  # noqa: E402
    back_channel_recipient,
    enriched_rows,
    tied_outer_cut,
)
from org_frontier.questions.q60_thompson_backchannel.thompson_backchannel_utils import (  # noqa: E402
    MAX_PHI,
    return_path_type,
)

LABELS = ("W", "S", "C")
PANEL_SIZE = 16

PARTITION_TO_SINGLETON = {
    OUTER_W: "W",
    OUTER_C: "C",
}


def official_singleton(row):
    """Singleton party from Q57 official tied outer cut."""
    tied = tied_outer_cut(row)
    if tied is None:
        return None
    return PARTITION_TO_SINGLETON.get(tied)


def seam_type_match(singleton, thompson_type):
    """True iff official singleton seam aligns with return-path type."""
    return (
        (singleton == "W" and thompson_type == "sequential")
        or (singleton == "C" and thompson_type == "reciprocal")
    )


def enriched_panel():
    """Sixteen ceiling pairs with singleton seam and return-path typing."""
    rows = []
    for row in enriched_rows():
        rules = row["rules"]
        recipient = back_channel_recipient(row["topology"])
        singleton = official_singleton(row)
        thompson = return_path_type(rules, recipient)
        v = verdict(rules, LABELS)
        seams = seam_set(rules, LABELS)
        rows.append({
            **row,
            "recipient": recipient,
            "singleton": singleton,
            "thompson_type": thompson,
            "seam_match": seam_type_match(singleton, thompson),
            "structure": v.structure,
            "max_phi": float(v.max_phi),
            "mip_partition": v.mip_partition,
            "seam_set": seams,
            "seam_set_ok": seams == {singleton} if singleton else False,
        })
    return rows
