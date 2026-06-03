"""Proxy bridge: can a cheap time-series estimate recover the literacy/algorithmacy verdict?

The survey's central finding: on real systems exact Φ is intractable, so neuroscience estimates a
proxy from finite time series and reports a lower bound. Organizational coordination also produces
time series (messages, handoffs, decisions). This module tests whether a proxy estimated from
simulated trajectories of a coordination form preserves the binary verdict that exact IIT-4.0 Φ
gives on the form's structure.

Pipeline per form:
  1. Build the deterministic application-layer TPM from the form's Boolean rules.
  2. Add output noise (the repo's model: tpm_noisy = tpm*(1-noise) + (1-tpm)*noise), so trajectories
     explore states the way noisy real data does.
  3. Estimate the ΦID-based proxy Φ_R (CCS redundancy) from a simulated trajectory — reusing
     phiid_vs_phi.phiid_measure, the same estimator validated in this repo's data-style study.
  4. Compare to the exact structural verdict (classifier on the deterministic form) and to exact Φ
     recomputed on the noisy TPM (apples-to-apples reference).

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.proxy_bridge.run
"""

import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

import numpy as np

from org_frontier.classifier.classifier import tpm_from_rules, cm_from_rules, classify, PHI_EPS
from phiid_vs_phi.phiid_measure import phi_r_integration
from proxy_audit import exact_phi


def add_noise(tpm_sbn, noise):
    """Mix a deterministic state-by-node TPM toward the flipped output by `noise`."""
    return tpm_sbn * (1.0 - noise) + (1.0 - tpm_sbn) * noise


def exact_phi_max_noisy(tpm_noisy, cm, n, rng, traj_len=2000):
    """Exact IIT-4.0 max system Φ on the noisy TPM (all states reachable when noise>0)."""
    mean_phi, max_phi, _ = exact_phi.network_phi(tpm_noisy, cm, n, rng)
    return max_phi


def proxy_for_form(rules, noise, rng, traj_len=8000):
    """Return (structure, exact_phi_det_max, exact_phi_noisy_max, proxy_phi_r, proxy_phi_wms).

    structure          : 'triadic'/'dyadic' from the deterministic form (the ground truth).
    exact_phi_det_max  : max exact Φ on the deterministic form.
    exact_phi_noisy_max: max exact Φ on the noisy TPM (reference).
    proxy_phi_r        : ΦID Φ_R (CCS) estimated from the simulated noisy trajectory.
    proxy_phi_wms      : uncorrected whole-minus-sum Φ (the candidate_audit's best-tracking proxy),
                         estimated from the same trajectory — the proxy's strongest form.
    """
    n = len(rules)
    tpm_det = tpm_from_rules(rules)
    cm = cm_from_rules(rules)

    verdict = classify(tpm_det, cm)
    tpm_noisy = add_noise(tpm_det, noise)
    phi_noisy = exact_phi_max_noisy(tpm_noisy, cm, n, rng, traj_len)
    phi_r, phi_wms = phi_r_integration(tpm_noisy, n, rng, traj_len=traj_len)

    return verdict.structure, verdict.max_phi, phi_noisy, phi_r, phi_wms
