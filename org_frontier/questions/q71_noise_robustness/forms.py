"""Q71 forms: noisy versions of the outreach triad, for robustness of the verdict under stochastic update."""
import os, sys
_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

import numpy as np
from org_frontier.classifier.classifier import tpm_from_rules

LABELS = ("E", "M", "R")
READ_RECIPIENT = [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]  # triadic, Φ=2.0
BROADCAST = [lambda x: x[1], lambda x: x[0], lambda x: x[1]]              # dyadic, Φ=0


def noisy_tpm(rules, eps):
    """State-by-node TPM with each deterministic bit flipped with probability eps."""
    det = np.asarray(tpm_from_rules(rules), dtype=float)
    return det * (1.0 - eps) + (1.0 - det) * eps
