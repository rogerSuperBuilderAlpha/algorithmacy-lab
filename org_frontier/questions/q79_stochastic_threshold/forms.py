"""Q79 forms: stochastic agent commit. M reads the recipient with probability p, else ignores it.
State-by-node TPM over (E=bit0, M=bit1, R=bit2). E'=M, R'=M deterministic; M' is the p-mixture of
E&R (reads recipient) and E (broadcast)."""
import os, sys
_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")
import numpy as np


def stochastic_tpm(p):
    tpm = np.zeros((8, 3), dtype=float)
    for s in range(8):
        E, M, R = s & 1, (s >> 1) & 1, (s >> 2) & 1
        tpm[s, 0] = M                          # E' = M
        tpm[s, 1] = p * (E & R) + (1 - p) * E  # M' = E&R w.p. p, else E
        tpm[s, 2] = M                          # R' = M
    return tpm
