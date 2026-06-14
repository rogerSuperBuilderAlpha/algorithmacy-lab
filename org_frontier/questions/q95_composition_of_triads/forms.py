"""Q95: composing two read-recipient triads through a shared node.

Q65 chained mediators; this chains whole triads. Two read-recipient triads are composed so the recipient
of the first is the sender of the second — the output of one triadic unit becomes a party in the next.

Single read-recipient triad (sender E, mediator M, recipient R): E'=M, M'=E∧R, R'=M; Φ=2, core {E,M,R}.

Composition (5 nodes): E1, M1, S (the shared recipient-of-1 / sender-of-2), M2, R2.
  E1' = M1
  M1' = E1 ∧ S
  S'  = M1            (S is the recipient of triad 1)
  M2' = S ∧ R2        (M2 reads its sender S and recipient R2)
  R2' = M2

`disjoint_complexes` (reused from Q94) resolves the irreducible-complex lattice into disjoint maximal
complexes, so composition can be read as unification (one spanning complex), fragmentation (two), or
additive.

Imported by `probe_composition_of_triads.py`.
"""

import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.probes.lib import verdict, major_complex
from org_frontier.questions.q94_multiple_complexes.forms import max_disjoint_complexes


def single_triad():
    """The read-recipient triad: E'=M, M'=E&R, R'=M."""
    rules = [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]
    return rules, ("E", "M", "R")


def two_disjoint_triads():
    """Two independent read-recipient triads (6 nodes), for the fragmentation baseline."""
    rules = [
        lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1],
        lambda x: x[4], lambda x: x[3] & x[5], lambda x: x[4],
    ]
    return rules, ("E1", "M1", "R1", "E2", "M2", "R2")


def composed():
    """Two triads sharing a node: recipient of triad 1 = sender of triad 2 (5 nodes)."""
    rules = [
        lambda x: x[1],            # E1' = M1
        lambda x: x[0] & x[2],     # M1' = E1 & S
        lambda x: x[1],            # S'  = M1
        lambda x: x[2] & x[4],     # M2' = S & R2
        lambda x: x[3],            # R2' = M2
    ]
    return rules, ("E1", "M1", "S", "M2", "R2")


def summary(rules, labels):
    """Whole-system verdict, major-complex (label, φ), and the disjoint-complex tiling."""
    v = verdict(rules, labels)
    core, phi = major_complex(rules, labels)
    tiling = max_disjoint_complexes(rules, labels)
    return v.structure, round(float(v.max_phi), 3), tuple(core or ()), round(float(phi), 3), tiling
