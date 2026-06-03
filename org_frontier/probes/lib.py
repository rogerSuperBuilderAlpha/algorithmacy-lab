"""Shared helpers for the probe loop: whole-system verdict and the major complex, for any n."""

import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

import pyphi
from pyphi import new_big_phi

from org_frontier.classifier.classifier import classify_rules, tpm_from_rules, cm_from_rules
from proxy_audit.exact_phi import reachable_states

pyphi.config.PROGRESS_BARS = False
pyphi.config.PARALLEL = False


def verdict(rules, labels):
    """Whole-system classifier verdict (Φ over the MIP)."""
    return classify_rules(rules, labels=labels)


def major_complex(rules, labels):
    """(core_label_tuple, phi) of the maximal complex, max over reachable states."""
    n = len(rules)
    tpm, cm = tpm_from_rules(rules), cm_from_rules(rules)
    net = pyphi.Network(tpm, cm=cm, node_labels=labels)
    best = (None, -1.0)
    for s in reachable_states(tpm, n):
        state = tuple((s >> i) & 1 for i in range(n))
        try:
            mc = new_big_phi.maximal_complex(net, state)
            if float(mc.phi) > best[1]:
                best = (tuple(labels[i] for i in mc.node_indices), float(mc.phi))
        except Exception:
            continue
    return best
