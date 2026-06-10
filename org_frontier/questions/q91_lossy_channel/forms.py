"""Q91: the read-recipient triad with a lossy channel on the mediator's read of the recipient.

Every read in the corpus is exact, and Q79 made the mediator's commit stochastic (it sometimes ignores
the recipient). Q91 degrades the input instead: the mediator always uses the recipient, but reads it
through a binary symmetric channel of error e, so R reaches M flipped with probability e. At e = 0 the
channel is perfect; at e = 0.5 it carries no information about R; at e = 1 it carries R perfectly inverted.

The mediator reads the worker perfectly and the recipient through the channel:
    P(M'=1 | E, R) = E * [ (1-e)·R + e·(1-R) ]
with E' = M and R' = M deterministic. The result is a stochastic state-by-node TPM whose exact Φ is read
by `max_phi_float`.

Imported by `probe_lossy_channel.py`.
"""

import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

import numpy as np

LABELS = ("E", "M", "R")           # node order E=0, M=1, R=2
ERRORS = [0.0, 0.1, 0.2, 0.25, 0.3, 0.4, 0.5]


def lossy_tpm(e):
    """Stochastic state-by-node TPM for channel error e on the mediator's read of R."""
    tpm = np.zeros((8, 3), dtype=float)
    for s in range(8):
        E, M, R = s & 1, (s >> 1) & 1, (s >> 2) & 1
        p_R_seen = (1 - e) * R + e * (1 - R)       # probability M reads R as 1 through the channel
        tpm[s, 0] = M                              # E' = M
        tpm[s, 1] = E * p_R_seen                   # M' = E AND (R through the channel)
        tpm[s, 2] = M                              # R' = M
    return tpm
