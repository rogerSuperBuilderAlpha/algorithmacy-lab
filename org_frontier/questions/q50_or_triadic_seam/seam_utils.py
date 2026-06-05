"""Shared helpers for Q50 OR triadic seam probes."""

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
from org_frontier.probes.lib import verdict

pyphi.config.PROGRESS_BARS = False
pyphi.config.PARALLEL = False

LABELS = ("W", "S", "C")
CANON = [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]

OR_INDEX = 7
SYMMETRIC_INDICES = {1, 7, 8, 14}
IMPLICATION_INDICES = {2, 4, 11, 13}
MAX_PHI = 2.0
CONSTANT_INDICES = {0, 3}
LIVE_INDICES = {1, 2}

_TWO_PART = re.compile(r"2 parts:\s*\{([^}]*)\}")


def instrument_control():
    v = verdict(CANON, LABELS)
    assert v.structure == "triadic" and abs(v.max_phi - MAX_PHI) < 1e-6, "control failed"
    assert v.mip_partition == "2 parts: {W,SC}", f"control MIP {v.mip_partition!r}"
    return v


def w_index(label):
    return int(label[1])


def c_index(label):
    return int(label.split("_C")[1])


def s_index(label):
    return int(label.split("_S")[1].split("_")[0])


def matched_live_reads(iw, ic):
    return iw == ic and iw in LIVE_INDICES


def complementary_reads(iw, ic):
    return {iw, ic} == LIVE_INDICES and iw != ic


def _singleton_of(part_line):
    m = _TWO_PART.search(part_line)
    if not m:
        return None
    groups = [g for g in m.group(1).split(",")]
    singles = [g for g in groups if len(g) == 1]
    return singles[0] if len(singles) == 1 and len(groups) == 2 else (singles[0] if singles else None)


def seam_set(rules, labels=LABELS):
    v = classify_rules(rules, labels=labels)
    if v.structure != "triadic" or v.mip_state is None:
        return set()
    tpm, cm = tpm_from_rules(rules), cm_from_rules(rules)
    net = pyphi.Network(tpm, cm=cm, node_labels=labels)
    sub = pyphi.Subsystem(net, tuple(v.mip_state))
    sia = new_big_phi.sia(sub)
    out = set()
    for tie in sia.ties:
        line = str(tie.partition).splitlines()[0].strip()
        s = _singleton_of(line)
        if s is not None:
            out.add(s)
    return out


def or_forms():
    from org_frontier.corpus.population import enumerate_family

    for label, rules in enumerate_family():
        if s_index(label) == OR_INDEX:
            yield label, rules
