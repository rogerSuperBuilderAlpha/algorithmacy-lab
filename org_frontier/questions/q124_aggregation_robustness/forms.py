"""Q124: is the verdict robust to the state-aggregation rule? Answering critical-review F1/T4.

The sharpest IIT-methodological objection (the reviewer rated it fatal): the verdict reads Φ_MIP at the
single most-integrated reachable state (a max over states), and for many triadic forms only the all-ones state
integrates, so a different aggregation, a min, a mean, or a stationary-distribution weighting, might call the
form dyadic. If so, the verdict would be a property of one cherry-picked state, not of the form.

This tests the charge directly. For each triadic form it recomputes the verdict under four aggregations of the
per-state Φ_MIP profile: max (the classifier's rule), mean (uniform over reachable states), stationary
(weighted by the deterministic dynamics' long-run occupancy), and min (the strict every-state rule). It also
confirms no dyadic form gains a triadic verdict under any aggregation.

Imported by `probe_aggregation_robustness.py`.
"""

import os
import sys
from collections import Counter

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.questions.q93_fragility_margin import forms as q93
from org_frontier.classifier.classifier import classify_rules, phi_profile, tpm_from_rules, cm_from_rules

EPS = 1e-9


def _next(tpm, n, s):
    return sum(int(round(tpm[s, j])) << j for j in range(n))


def stationary_occupancy(tpm, n):
    """Long-run occupancy of each state under the deterministic dynamics, from a uniform start over states."""
    occ = Counter()
    for s0 in range(2 ** n):
        seen = []
        s = s0
        while s not in seen:
            seen.append(s)
            s = _next(tpm, n, s)
        cycle = seen[seen.index(s):]
        for c in cycle:
            occ[c] += 1.0 / len(cycle)
    total = sum(occ.values())
    return {k: v / total for k, v in occ.items()}


def aggregations(rules):
    """The Φ of a form under max / mean / stationary / min aggregation over its reachable-state Φ profile."""
    n = len(rules)
    tpm, cm = tpm_from_rules(rules), cm_from_rules(rules)
    prof = phi_profile(tpm, cm)                       # [(state_tuple, phi), ...] over reachable states
    phis = [p for _, p in prof]
    occ = stationary_occupancy(tpm, n)
    stat = 0.0
    for state_tuple, phi in prof:
        s = sum(int(state_tuple[i]) << i for i in range(n))
        stat += occ.get(s, 0.0) * phi
    return {
        "max": max(phis),
        "mean": sum(phis) / len(phis),
        "stationary": stat,
        "min": min(phis),
    }


def classify_family():
    """Return (triadic_forms, dyadic_forms) as lists of (bits, rules)."""
    triadic, dyadic = [], []
    for bits, rules in q93.enumerate_family():
        (triadic if classify_rules(rules, labels=q93.LABELS).structure == "triadic" else dyadic).append(
            (bits, rules))
    return triadic, dyadic
