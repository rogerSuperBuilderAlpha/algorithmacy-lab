"""Q123: is the verdict reproducible and config-invariant? Answering critical-review T6.

The critical review charged that "exact IIT-4.0 Φ" is one config of an unpinned, mutable build: the PyPhi
pin is a moving branch with no commit hash, the verdict's config (SYSTEM_CUTS, REPERTOIRE_DISTANCE, ...) is
unreported, and a reviewer flagged SYSTEM_CUTS = 3.0_STYLE as a sign the verdict is not canonical 4.0.

This study pins the build, records the config, and tests whether the binary verdict is invariant to the
contested knobs across the whole 256-form family. It also corrects the review on one point: SYSTEM_CUTS is a
legacy IIT-3.0 option that the IIT-4.0 system-Φ path (`pyphi.new_big_phi`) never reads.

`BUILD_COMMIT` is the pinned PyPhi commit at the time of record. The probe re-reads the live config and the
verdict under each config override, so the recorded values are verifiable against the environment.

Imported by `probe_reproducibility.py`.
"""

import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

import pyphi

from org_frontier.questions.q93_fragility_margin import forms as q93
from org_frontier.questions.q111_shapley_value import forms as q111
from org_frontier.classifier.classifier import classify_rules

# The pinned build at the time of record (replace the moving-branch requirement with this commit).
BUILD_COMMIT = "b78d0e342d37175cbd55cf35a6d52ae035b4c50f"

# The config knobs the IIT-4.0 system-Φ path reads, plus the legacy knob the review flagged.
VERDICT_CONFIG_KEYS = (
    "IIT_VERSION", "SYSTEM_PARTITION_TYPE", "REPERTOIRE_DISTANCE",
    "CES_DISTANCE", "SYSTEM_CUTS", "SHORTCIRCUIT_SIA", "PARALLEL",
)


def live_config():
    return {k: getattr(pyphi.config, k, "(absent)") for k in VERDICT_CONFIG_KEYS}


def family_verdicts(override=None):
    """The structure verdict for each of the 256 strict-mediation forms, under an optional config override."""
    fam = list(q93.enumerate_family())
    if override:
        with pyphi.config.override(**override):
            return [classify_rules(r, labels=q93.LABELS).structure for _, r in fam]
    return [classify_rules(r, labels=q93.LABELS).structure for _, r in fam]


def disagreements(a, b):
    return sum(1 for x, y in zip(a, b) if x != y)


def alt_measure_admissibility():
    """On the canonical triad, count alternative repertoire-distance measures that run AND give Φ > 0.

    Returns (n_alternatives, n_admissible_and_nondegenerate, detail). The 4.0-canonical
    GENERALIZED_INTRINSIC_DIFFERENCE is excluded; an admissible-and-nondegenerate alternative would be a
    config cell that could carry a different non-degenerate verdict.
    """
    from pyphi.metrics import distribution as dist
    rules, labels = q111.read_recipient()
    measures = sorted(dist.measures.all())
    alts = [m for m in measures if m != "GENERALIZED_INTRINSIC_DIFFERENCE"]
    nondegenerate = 0
    detail = {}
    for m in alts:
        try:
            with pyphi.config.override(REPERTOIRE_DISTANCE=m):
                v = classify_rules(rules, labels=labels)
            phi = float(v.max_phi)
            detail[m] = ("ran", round(phi, 3), v.structure)
            if phi > 1e-9:
                nondegenerate += 1
        except Exception as e:
            detail[m] = ("error", type(e).__name__, None)
    return len(alts), nondegenerate, detail
