"""Bridge: coded determination rules -> TPM -> exact-Φ verdict -> coder-disagreement Φ CI.

A coded account of a coordination names, for each party, a Boolean determination rule: the
party's next state as a function of the current states of all parties. The rules are encoded
into a deterministic state-by-node TPM, classified by exact IIT-4.0 Φ over the MIP, and read as
a structural verdict (dyadic -> literacy, triadic -> algorithmacy). Φ is not reimplemented; this
module wraps `org_frontier.classifier` and `org_frontier.probes.lib`.

Coding is done by people, and people disagree. Each coder supplies their own reading of the same
account: a per-party rule set. Two coders who read the account identically agree perfectly; two
who disagree on which bits or states are active produce different rule sets and so different Φ
readings. This module propagates that disagreement into a Φ confidence interval by bootstrapping
over the coders, weighting the resample by Krippendorff-alpha agreement, and reporting the
percentile CI of the resulting Φ distribution.

The construct: a single coded account yields not one Φ but a Φ interval whose width reflects how
much the coders disagree. Perfect agreement collapses the interval to a point.

Validation controls (run the probe):
  - decoupled rule set reads dyadic;
  - fully-coupled (faithful triad) rule set reads triadic with max Φ_MIP = 2.0;
  - perfect agreement (alpha = 1) returns a degenerate CI [phi, phi].

All inputs are synthetic coded rule sets, not measured worker states.
"""

import os
import sys
from typing import Callable, Dict, List, Optional, Sequence, Tuple

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

import numpy as np

from org_frontier.classifier.classifier import classify_rules, PHI_EPS
from org_frontier.probes.lib import verdict

DEFAULT_LABELS = ("W", "S", "C")


# --------------------------------------------------------------------------------------
# Rules -> TPM -> verdict (the deterministic core)
# --------------------------------------------------------------------------------------

def rule_to_phi(rules: Sequence[Callable],
                labels: Sequence[str] = DEFAULT_LABELS) -> Dict:
    """Encode coded determination rules into a TPM and read the exact-Φ verdict.

    Returns {structure, competence, max_phi, n_irreducible}. Wraps the classifier's
    `classify_rules`; the TPM is built by `tpm_from_rules` inside it. Deterministic.
    """
    v = classify_rules(rules, labels=labels)
    return {
        "structure": v.structure,
        "competence": v.competence,
        "max_phi": float(v.max_phi),
        "n_irreducible": int(v.n_states_irreducible),
    }


# --------------------------------------------------------------------------------------
# Coder disagreement and Krippendorff alpha
# --------------------------------------------------------------------------------------

def krippendorff_alpha(codings: np.ndarray) -> float:
    """Krippendorff's alpha for nominal data on a (n_coders, n_items) integer matrix.

    Each column is one coding unit (e.g. one active-bit decision); each row is a coder's
    label for every unit. Returns 1.0 for perfect agreement, 0.0 for chance-level agreement,
    and may go negative for systematic disagreement. NaN-free for fully coded matrices.
    """
    codings = np.asarray(codings)
    n_coders, n_items = codings.shape
    if n_coders < 2:
        return 1.0
    # Observed disagreement: mean over items of the fraction of disagreeing coder pairs.
    do_terms = []
    for j in range(n_items):
        col = codings[:, j]
        pairs = 0
        disagree = 0
        for a in range(n_coders):
            for b in range(a + 1, n_coders):
                pairs += 1
                if col[a] != col[b]:
                    disagree += 1
        if pairs:
            do_terms.append(disagree / pairs)
    do = float(np.mean(do_terms)) if do_terms else 0.0
    # Expected disagreement: probability two values drawn at random (over the whole pooled
    # set of labels) differ.
    flat = codings.reshape(-1)
    vals, counts = np.unique(flat, return_counts=True)
    total = counts.sum()
    p = counts / total
    de = float(1.0 - np.sum(p ** 2))
    if de < 1e-12:
        # No variance in the pooled labels: everyone used one value -> perfect agreement.
        return 1.0
    return float(1.0 - do / de)


# --------------------------------------------------------------------------------------
# Coder-weighted Φ confidence interval
# --------------------------------------------------------------------------------------

def _phi_of(rules: Sequence[Callable], labels: Sequence[str]) -> float:
    return float(verdict(rules, labels).max_phi)


def phi_ci(coder_phis: Sequence[float],
           coder_codings: Optional[np.ndarray] = None,
           n_boot: int = 800,
           ci: float = 0.95,
           rng: Optional[np.random.Generator] = None) -> Dict:
    """Φ confidence interval propagated from coder disagreement.

    `coder_phis[k]` is coder k's max-Φ_MIP reading of one account (obtained by running that
    coder's rule-set through `rule_to_phi`; see `phi_ci_from_rules` for the rule-set entry
    point). The CI is a studentized bootstrap-t interval over the coder panel: it resamples
    coders with replacement, studentizes each resample by its own standard error, and inverts
    the bootstrap distribution of the t-statistic. The bootstrap-t is calibrated at small coder
    counts where the plain percentile bootstrap under-covers.

    `coder_codings`, when given, is a (n_coders, n_units) integer matrix of active-bit
    decisions; its Krippendorff alpha is reported. Perfect agreement (alpha = 1, all readings
    identical) returns the degenerate CI [phi, phi].

    Returns {phi_point, ci_low, ci_high, alpha, coder_phis, degenerate}. `phi_point` is the mean
    of the per-coder Φ readings (the consensus point estimate).
    """
    if rng is None:
        rng = np.random.default_rng(0)
    coder_phis = np.asarray(coder_phis, dtype=float)
    n_coders = len(coder_phis)

    if coder_codings is not None:
        alpha = krippendorff_alpha(coder_codings)
    else:
        alpha = 1.0 if np.allclose(coder_phis, coder_phis[0], atol=PHI_EPS) else 0.0

    point = float(np.mean(coder_phis))
    se = float(np.std(coder_phis, ddof=1) / np.sqrt(n_coders)) if n_coders > 1 else 0.0

    # Degenerate: one coder, perfect agreement on identical readings, or zero spread.
    if (n_coders < 2 or se < PHI_EPS
            or (alpha >= 1.0 - 1e-9 and np.allclose(coder_phis, coder_phis[0], atol=PHI_EPS))):
        return {
            "phi_point": point,
            "ci_low": point,
            "ci_high": point,
            "alpha": float(alpha),
            "coder_phis": coder_phis.tolist(),
            "degenerate": True,
        }

    a = (1.0 - ci) / 2.0
    tstars = np.empty(n_boot, dtype=float)
    for b in range(n_boot):
        idx = rng.integers(0, n_coders, size=n_coders)
        bs = coder_phis[idx]
        bse = float(np.std(bs, ddof=1) / np.sqrt(n_coders))
        tstars[b] = (float(np.mean(bs)) - point) / bse if bse > PHI_EPS else 0.0
    t_lo = float(np.quantile(tstars, a))
    t_hi = float(np.quantile(tstars, 1.0 - a))
    lo = point - t_hi * se
    hi = point - t_lo * se
    return {
        "phi_point": point,
        "ci_low": lo,
        "ci_high": hi,
        "alpha": float(alpha),
        "coder_phis": coder_phis.tolist(),
        "degenerate": False,
    }


def phi_ci_from_rules(coder_rule_sets: Sequence[Sequence[Callable]],
                      labels: Sequence[str] = DEFAULT_LABELS,
                      coder_codings: Optional[np.ndarray] = None,
                      n_boot: int = 800,
                      ci: float = 0.95,
                      rng: Optional[np.random.Generator] = None) -> Dict:
    """`phi_ci` entry point that takes per-coder rule sets, reads each to its max Φ_MIP via the
    classifier, then propagates the disagreement. Φ is not reimplemented."""
    coder_phis = [_phi_of(r, labels) for r in coder_rule_sets]
    return phi_ci(coder_phis, coder_codings=coder_codings, n_boot=n_boot, ci=ci, rng=rng)
