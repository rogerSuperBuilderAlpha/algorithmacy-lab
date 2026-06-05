"""Shared helpers for Q51 implication back-channel probes."""

import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.classifier.classifier import cm_from_rules
from org_frontier.probes.lib import verdict

LABELS = ("W", "S", "C")
CANON = [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]

IMPLICATION_INDICES = {2, 4, 11, 13}
MAX_PHI = 2.0
LIVE_INDICES = {1, 2}
PHI_TOL = 1e-6


def instrument_control():
    v = verdict(CANON, LABELS)
    assert v.structure == "triadic" and abs(v.max_phi - MAX_PHI) < PHI_TOL, "control failed"
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


def worker_backchannel(rules):
    old_w = rules[0]
    return [lambda x, ow=old_w: ow(x) & x[2], rules[1], rules[2]]


def symmetric_backchannel(rules):
    old_w, old_c = rules[0], rules[2]
    return [
        lambda x, ow=old_w: ow(x) & x[2],
        rules[1],
        lambda x, oc=old_c: oc(x) & x[0],
    ]


def edge_count(rules):
    return int(cm_from_rules(rules).sum())


def implication_forms(predicate):
    from org_frontier.corpus.population import enumerate_family

    for label, rules in enumerate_family():
        if s_index(label) not in IMPLICATION_INDICES:
            continue
        iw, ic = w_index(label), c_index(label)
        if predicate(iw, ic):
            yield label, rules
