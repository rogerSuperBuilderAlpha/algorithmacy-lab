"""Literacy-or-algorithmacy classifier: exact IIT-4.0 Φ as a structural verdict.

A coordination form is modelled as a small discrete dynamical system whose elements are the
parties — Worker (W), System/mediator (S), Counterpart (C), and any further parties. Each
party's next state is a fixed function of the current states of all parties. Exact IIT-4.0 Φ
over the system's minimum-information partition (MIP) measures whether that cause-effect
structure is irreducible along party lines.

The verdict:
    Φ_MIP = 0  ->  the form FACTORS along some party-respecting cut  ->  DYADIC  ->  LITERACY.
    Φ_MIP > 0  ->  no cut factors it; the parties are bound through the mediator  ->  TRIADIC
                   ->  ALGORITHMACY.

The test is Φ over the MIP (the least-damaging partition PyPhi finds), NOT Φ over the complete
{W}{S}{C} cut. The complete cut over-calls: it severs the genuine two-party coupling a dyad has
and so labels every coupled dyad a triad. See
``dissertation/paper2_construct/party_partition.py`` for the worked demonstration. The MIP is
itself party-respecting (nodes vs blocks of nodes), so the verdict is about party-line
factorization.

This wraps the repo's exact-Φ oracle (``proxy_audit.exact_phi``). It is a structural
CLASSIFIER, validated behaviourally at the binary contrast. It is NOT a graded readability
score: the magnitude of Φ depends on the encoding and is not a reliable scale (the dissertation
withdrew that claim). Use the binary verdict; read the magnitude as at most an ordinal hint.

Run the built-in validation controls before trusting any verdict:
    ~/iit-playground/venv-4.0/bin/python -m org_frontier.classifier.validate
"""

import os
import sys
from dataclasses import dataclass, field
from typing import Callable, Optional, Sequence

# Repo root on the path so the sibling `proxy_audit` package imports.
_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)

os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

import numpy as np
import pyphi
from pyphi import new_big_phi

from foundations.proxy_audit.exact_phi import exact_big_phi, reachable_states

pyphi.config.PROGRESS_BARS = False
pyphi.config.PARALLEL = False

# Φ below this is treated as zero (floating-point and PyPhi numerical noise).
PHI_EPS = 1e-9

DEFAULT_LABELS = ("W", "S", "C")  # worker, system/mediator, counterpart


# --------------------------------------------------------------------------------------
# Building application-layer transition matrices from per-party Boolean rules
# --------------------------------------------------------------------------------------

def tpm_from_rules(rules: Sequence[Callable], n: Optional[int] = None) -> np.ndarray:
    """Deterministic state-by-node TPM of shape (2^n, n) from per-node Boolean rules.

    ``rules[j]`` maps the current node-state tuple (little-endian: index 0 = first party)
    to node j's next value in {0, 1}. Little-endian indexing matches PyPhi and
    ``proxy_audit.exact_phi``.
    """
    n = len(rules) if n is None else n
    tpm = np.zeros((2 ** n, n))
    for s in range(2 ** n):
        cur = tuple((s >> i) & 1 for i in range(n))
        for j in range(n):
            tpm[s, j] = float(rules[j](cur))
    return tpm


def cm_from_rules(rules: Sequence[Callable], n: Optional[int] = None) -> np.ndarray:
    """Connectivity matrix: cm[i, j] = 1 iff node j's rule depends on node i (flip-test)."""
    n = len(rules) if n is None else n
    cm = np.zeros((n, n), dtype=int)
    for j in range(n):
        for i in range(n):
            for s in range(2 ** n):
                cur = list((s >> k) & 1 for k in range(n))
                flipped = cur.copy()
                flipped[i] ^= 1
                if rules[j](tuple(cur)) != rules[j](tuple(flipped)):
                    cm[i, j] = 1
                    break
    return cm


# --------------------------------------------------------------------------------------
# The Φ profile and the verdict
# --------------------------------------------------------------------------------------

@dataclass
class Verdict:
    """The classifier's output for one coordination form."""
    competence: str               # "literacy" or "algorithmacy"
    structure: str                # "dyadic" or "triadic"
    max_phi: float                # max Φ_MIP over reachable states
    mip_state: Optional[tuple]    # the state achieving max_phi
    mip_partition: str            # repr of the minimum-information partition at that state
    n_states_evaluated: int
    n_states_irreducible: int     # reachable states with Φ_MIP > PHI_EPS
    phi_profile: list = field(default_factory=list)  # [(state, phi), ...]
    labels: tuple = DEFAULT_LABELS

    def __str__(self) -> str:
        head = (f"{self.structure.upper():>9}  ->  demands {self.competence.upper()}   "
                f"(max Φ_MIP = {self.max_phi:.6f} over {self.n_states_evaluated} reachable "
                f"states; {self.n_states_irreducible} irreducible)")
        if self.mip_state is not None:
            head += f"\n           max-Φ state {self.mip_state}, MIP cut: {self.mip_partition}"
        return head


def phi_profile(tpm_sbn: np.ndarray, cm: np.ndarray, n: Optional[int] = None):
    """Exact IIT-4.0 Φ_MIP for each reachable state. Returns [(state_tuple, phi), ...]."""
    n = cm.shape[0] if n is None else n
    out = []
    for s in reachable_states(tpm_sbn, n):
        state = tuple((s >> i) & 1 for i in range(n))
        phi = exact_big_phi(tpm_sbn, cm, state)
        if phi is not None:
            out.append((state, float(phi)))
    return out


def _mip_partition_repr(tpm_sbn, cm, state, labels) -> str:
    """Repr of the minimum-information partition at one state."""
    try:
        net = pyphi.Network(tpm_sbn, cm=cm, node_labels=labels[:cm.shape[0]])
        sub = pyphi.Subsystem(net, tuple(state))
        # First line is the human-readable cut (e.g. "2 parts: {W,SC}"); the rest is a matrix.
        return str(new_big_phi.sia(sub).partition).splitlines()[0].strip()
    except Exception as e:  # partition repr is informational only
        return f"(unavailable: {e})"


def classify(tpm_sbn: np.ndarray, cm: np.ndarray,
             labels: Sequence[str] = DEFAULT_LABELS,
             eps: float = PHI_EPS) -> Verdict:
    """Classify a coordination form given its state-by-node TPM and connectivity matrix.

    A form is TRIADIC (-> algorithmacy) if it is irreducible (Φ_MIP > eps) in at least one
    reachable state; otherwise DYADIC (-> literacy). The verdict is read at the system's
    most-integrated reachable state, matching the dissertation's instrument.
    """
    n = cm.shape[0]
    profile = phi_profile(tpm_sbn, cm, n)
    if not profile:
        return Verdict("literacy", "dyadic", 0.0, None, "(no reachable states)",
                       0, 0, [], tuple(labels[:n]))
    max_state, max_phi = max(profile, key=lambda r: r[1])
    n_irreducible = sum(1 for _, p in profile if p > eps)
    triadic = max_phi > eps
    mip = _mip_partition_repr(tpm_sbn, cm, max_state, tuple(labels)) if triadic else "(factors)"
    return Verdict(
        competence="algorithmacy" if triadic else "literacy",
        structure="triadic" if triadic else "dyadic",
        max_phi=max_phi,
        mip_state=max_state if triadic else None,
        mip_partition=mip,
        n_states_evaluated=len(profile),
        n_states_irreducible=n_irreducible,
        phi_profile=profile,
        labels=tuple(labels[:n]),
    )


def classify_rules(rules: Sequence[Callable],
                   labels: Sequence[str] = DEFAULT_LABELS,
                   eps: float = PHI_EPS) -> Verdict:
    """Convenience: classify a form given per-party Boolean rules."""
    tpm = tpm_from_rules(rules)
    cm = cm_from_rules(rules)
    return classify(tpm, cm, labels=labels, eps=eps)
