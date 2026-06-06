"""Shared helpers for Q62 excluded outer singleton cut signal probes."""

import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.probes.lib import verdict  # noqa: E402
from org_frontier.questions.q56_symmetric_complete_mip.mip_geometry_utils import (  # noqa: E402
    OUTER_C,
    OUTER_W,
    PHI_TOL,
    instrument_control,
)
from org_frontier.questions.q57_channel_direction_mip.direction_mip_utils import (  # noqa: E402
    back_channel_recipient,
    enriched_rows,
    excluded_outer_cut,
    norm_fields,
    tied_outer_cut,
)
from org_frontier.questions.q60_thompson_backchannel.thompson_backchannel_utils import (  # noqa: E402
    MAX_PHI,
    return_path_type,
)
from org_frontier.questions.q61_seam_return_typing.seam_return_utils import (  # noqa: E402
    official_singleton,
)

LABELS = ("W", "S", "C")
PANEL_SIZE = 16

PARTITION_TO_SINGLETON = {
    OUTER_W: "W",
    OUTER_C: "C",
}


def excluded_singleton(row):
    """Singleton party from Q57 excluded (non-tied) outer cut."""
    tied = tied_outer_cut(row)
    if tied is None:
        return None
    excl = excluded_outer_cut(tied)
    return PARTITION_TO_SINGLETON.get(excl)


def complement_match(tied, excluded):
    """True iff excluded singleton is complement of tied singleton."""
    return (
        (tied == "W" and excluded == "C")
        or (tied == "C" and excluded == "W")
    )


def inverse_type_match(excluded, thompson_type):
    """True iff excluded inversely tracks return-path type."""
    return (
        (excluded == "C" and thompson_type == "sequential")
        or (excluded == "W" and thompson_type == "reciprocal")
    )


def direct_type_match(excluded, thompson_type):
    """True iff excluded tracks type the same way tied seam does."""
    return (
        (excluded == "W" and thompson_type == "sequential")
        or (excluded == "C" and thompson_type == "reciprocal")
    )


def joint_signature(tied, thompson_type, excluded):
    """Hashable triple for joint-label counting."""
    return (tied, thompson_type, excluded)


def enriched_panel():
    """Sixteen ceiling pairs with tied, excluded, and return-path fields."""
    rows = []
    for row in enriched_rows():
        rules = row["rules"]
        recipient = back_channel_recipient(row["topology"])
        tied = official_singleton(row)
        excluded = excluded_singleton(row)
        thompson = return_path_type(rules, recipient)
        nf = norm_fields(row)
        v = verdict(rules, LABELS)
        rows.append({
            **row,
            "recipient": recipient,
            "tied_singleton": tied,
            "excluded_singleton": excluded,
            "thompson_type": thompson,
            "complement_match": complement_match(tied, excluded),
            "inverse_type_match": inverse_type_match(excluded, thompson),
            "direct_type_match": direct_type_match(excluded, thompson),
            "joint": joint_signature(tied, thompson, excluded),
            "excl_norm": nf["excl_norm"],
            "structure": v.structure,
            "max_phi": float(v.max_phi),
            "mip_partition": v.mip_partition,
        })
    return rows
