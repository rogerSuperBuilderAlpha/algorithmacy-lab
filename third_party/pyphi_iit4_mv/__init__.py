"""Vendored IIT-4.0 multivalued pin surface (M1: SBS-native ExplicitTPM).

Depends on the lab's stock ``pyphi @ feature/iit-4.0`` for binary IIT-4.0 Φ.
This package does **not** replace that pin for binary work. It adds an
isolated MultivaluedNetwork / SBSNativeExplicitTPM path that accepts
ternary (and small mixed-radix) state-by-state TPMs without
``int(log2(...))`` collapse.

M1 scope: TPM ingest + Network construct + preserved SBS.
Exact Φ on multivalued systems is M2+ (see ``phi_blocker``).

Enable::

    import sys
    sys.path.insert(0, "<repo>/third_party")
    from pyphi_iit4_mv import MultivaluedNetwork, SBSNativeExplicitTPM
"""

from .network import MultivaluedNetwork
from .phi_blocker import probe_exact_phi_blocker
from .tpm import SBSNativeExplicitTPM

__all__ = [
    "MultivaluedNetwork",
    "SBSNativeExplicitTPM",
    "probe_exact_phi_blocker",
]
