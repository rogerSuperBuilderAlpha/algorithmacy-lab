"""Q93: the strict-mediation family with single-bit perturbations and a noise-survival measure.

Each strict-mediation three-node form (sender intent S, mediator M, recipient R; M reads both outer
parties) is parametrized by eight bits: a 2-bit table for R' = tW[M-equivalent input], a 2-bit table
for the other outer read, and a 4-bit table for the mediator M' = tS[outer1 | outer2<<1]. This module
enumerates the family, perturbs each form by flipping one truth-table bit at a time, and measures how
many single-bit flips collapse a triadic form to dyadic — the structural margin to the dyadic boundary.
It also measures noise survival: the exact Φ of the form's TPM mixed toward its flipped output by a
fixed noise.

Imported by `probe_fragility_margin.py`.
"""

import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.classifier.classifier import classify_rules, tpm_from_rules
from org_frontier.probes.lib import max_phi_float
from org_frontier.proxy_bridge.bridge import add_noise

LABELS = ("W", "S", "C")          # outer W, mediator S, outer C (matches the corpus family order)


def _rules_from_bits(bits):
    """bits = (tW0,tW1, tC0,tC1, tS0,tS1,tS2,tS3). Build the strict-mediation rules.

    W' = tW[S]; C' = tC[S]; S' = tS[W | C<<1]. Node order (W, S, C) = (0, 1, 2).
    """
    tW = (bits[0], bits[1])
    tC = (bits[2], bits[3])
    tS = (bits[4], bits[5], bits[6], bits[7])
    return [
        lambda x: tW[x[1]],
        lambda x: tS[(x[0] & 1) | ((x[2] & 1) << 1)],
        lambda x: tC[x[1]],
    ]


def enumerate_family():
    """Yield (bits, rules) over the 256 strict-mediation forms (2*2*4 = 8 table bits)."""
    for w in range(4):
        for c in range(4):
            for s in range(16):
                bits = (
                    (w >> 0) & 1, (w >> 1) & 1,
                    (c >> 0) & 1, (c >> 1) & 1,
                    (s >> 0) & 1, (s >> 1) & 1, (s >> 2) & 1, (s >> 3) & 1,
                )
                yield bits, _rules_from_bits(bits)


def is_triadic(rules):
    return classify_rules(rules, labels=LABELS).structure == "triadic"


def collapse_count(bits):
    """Of the 8 single-bit flips of a form, how many turn a triadic form dyadic; and the total."""
    collapses = 0
    for b in range(8):
        flipped = tuple(v ^ (1 if i == b else 0) for i, v in enumerate(bits))
        if not is_triadic(_rules_from_bits(flipped)):
            collapses += 1
    return collapses, 8


def mediator_kind(bits):
    """Classify the mediator's 2-input table: parity (XOR/XNOR), monotone (AND/OR/NAND/NOR), or other."""
    tS = (bits[4], bits[5], bits[6], bits[7])
    if tS in ((0, 1, 1, 0), (1, 0, 0, 1)):
        return "parity"
    if tS in ((0, 0, 0, 1), (1, 1, 1, 0), (0, 1, 1, 1), (1, 0, 0, 0)):
        return "monotone"
    return "other"


def noise_phi(rules, noise=0.1):
    """Exact IIT-4.0 max Φ of the form's TPM mixed toward its flipped output by `noise`."""
    phi, _ = max_phi_float(add_noise(tpm_from_rules(rules), noise))
    return float(phi)
