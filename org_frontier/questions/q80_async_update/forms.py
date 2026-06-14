"""Q80 forms: keystone outreach forms under asynchronous update.

Asynchronous update is modelled as a stochastic TPM in which one node (chosen uniformly) applies its rule
each step while the others hold: P(node j'=1) = (1/n) f_j(state) + (1 - 1/n) current_j. The synchronous
deterministic TPM is the f_j; the hold term is the node's current value.
"""
import os, sys
_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")
import numpy as np
from org_frontier.classifier.classifier import tpm_from_rules

READ_RECIPIENT = ([lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]], ("E", "M", "R"))
BROADCAST = ([lambda x: x[1], lambda x: x[0], lambda x: x[1]], ("E", "M", "R"))
ALL_REQUIRED = ([lambda x: x[1], lambda x: x[0] & x[2] & x[3], lambda x: x[1], lambda x: x[1]], ("E", "M", "R1", "R2"))


def async_tpm(rules):
    det = np.asarray(tpm_from_rules(rules), dtype=float)
    nstates, n = det.shape
    out = det.copy()
    for s in range(nstates):
        for j in range(n):
            cur = (s >> j) & 1
            out[s, j] = (1.0 / n) * det[s, j] + (1.0 - 1.0 / n) * cur
    return out
