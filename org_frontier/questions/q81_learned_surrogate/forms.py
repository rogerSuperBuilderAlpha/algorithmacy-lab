"""Q81 corpus and features: the labelled outreach family and a size-invariant feature panel.

Two corpora and one feature map are defined here and reused by Q82.

- `n3_family()` yields the 256 strict-mediation three-node forms (sender intent S, mediator M,
  recipient R; no direct S<->R edge), each the outreach reading of `corpus.population.enumerate_family`.
  The exact IIT-4.0 verdict on each form is the ground-truth label.
- `larger_forms()` yields outreach forms at n = 4, 5, 6 with known verdicts, assembled from the
  breadth (Q64), chain/ring (Q66), and market (Q85) generators. This is the held-out generalization
  set: forms larger than anything the surrogate trains on.
- `intensive_features(traj)` reduces a T x n trajectory to a fixed-length vector of size-invariant
  aggregate statistics (means, extremes, and spreads over nodes and pairs), so a model trained at one
  size applies unchanged at another. The raw per-node/per-pair panel of probe #21 is not size-invariant
  and cannot cross sizes; that is the design change this study needs.

Run nothing here; imported by `probe_learned_surrogate.py`.
"""

import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

import numpy as np

from org_frontier.classifier.classifier import classify_rules, tpm_from_rules
from org_frontier.corpus.population import enumerate_family
from org_frontier.proxy_bridge.bridge import add_noise
from foundations.proxy_audit import exact_phi
from org_frontier.probes._info import entropy, mutual_information, transfer_entropy, o_information

from org_frontier.questions.q64_outreach_breadth_scaling import forms as q64
from org_frontier.questions.q66_chain_core_boundary import forms as q66
from org_frontier.questions.q85_agent_market import forms as q85

NOISE = 0.08
T = 6000


def n3_family():
    """Yield (key, rules, labels) over the 256 strict-mediation outreach forms (n=3)."""
    labels = ("S", "M", "R")
    for i, (_, rules) in enumerate(enumerate_family()):
        yield f"n3_{i:03d}", rules, labels


def larger_forms():
    """Yield (key, rules, labels, known_verdict) for held-out outreach forms at n = 4, 5, 6.

    Both classes at each size. Triadic: all-required campaigns (Q64), open chains and rings (Q66),
    all-required markets (Q85). Dyadic: substitutable and pooled campaigns (Q64), substitutable and
    one-substitutable-pair markets (Q85). The verdict is the exact-Φ ground truth recomputed below.
    """
    out = []
    # Q64 breadth: all_required(k) is triadic (n=k+2); substitutable/pooled are dyadic.
    for k in (2, 3, 4):                     # n = 4, 5, 6
        out.append((f"q64_all_required_k{k}", q64.all_required(k), q64.labels(k), "triadic"))
        out.append((f"q64_substitutable_k{k}", q64.substitutable(k), q64.labels(k), "dyadic"))
    out.append(("q64_pooled_k3", q64.pooled(3), q64.labels(3), "dyadic"))   # n = 5
    # Q66 depth: open_chain(d) and ring(d) are triadic.
    for d in (2, 3, 4):                     # n = d+2 = 4, 5, 6
        out.append((f"q66_open_chain_d{d}", q66.open_chain(d), q66.chain_labels(d), "triadic"))
        out.append((f"q66_ring_d{d}", q66.ring(d), q66.chain_labels(d), "triadic"))
    # Q85 market: all_required(N) triadic; substitutable(N) and mixed dyadic.
    for N in (2, 3, 4):                     # n = N+2 = 4, 5, 6
        out.append((f"q85_all_required_N{N}", q85.all_required(N), q85.labels(N), "triadic"))
        out.append((f"q85_substitutable_N{N}", q85.substitutable(N), q85.labels(N), "dyadic"))
    out.append(("q85_mixed_N3", q85.mixed_one_substitutable(3), q85.labels(3), "dyadic"))  # n = 5
    return out


def exact_label(rules, labels):
    """1 if the exact IIT-4.0 verdict is triadic, else 0."""
    return 1 if classify_rules(rules, labels=labels).structure == "triadic" else 0


def trajectory(rules, rng):
    """Simulate a noisy trajectory of the form (the data a cheap estimator would see)."""
    n = len(rules)
    return exact_phi.simulate_trajectory(add_noise(tpm_from_rules(rules), NOISE), n, T, rng)


FEATURE_NAMES = (
    "ent_mean", "ent_max", "ent_min", "ent_std",
    "mi_mean", "mi_max", "mi_min",
    "te_mean", "te_max",
    "oinfo_per_node",
)


def intensive_features(traj):
    """Reduce a T x n trajectory to a fixed-length, size-invariant feature vector.

    Every feature is an aggregate over nodes or node pairs, so the vector length does not depend on
    n. No feature encodes n directly: the surrogate must read structure, not size.
    """
    n = traj.shape[1]
    ent = [entropy(traj, [i]) for i in range(n)]
    pairs = [(a, b) for a in range(n) for b in range(a + 1, n)]
    mi = [mutual_information(traj, [a], [b]) for a, b in pairs]
    te = [transfer_entropy(traj, a, b) for a in range(n) for b in range(n) if a != b]
    oinfo = o_information(traj, list(range(n))) / n      # per-node, to keep it intensive
    return [
        float(np.mean(ent)), float(np.max(ent)), float(np.min(ent)), float(np.std(ent)),
        float(np.mean(mi)), float(np.max(mi)), float(np.min(mi)),
        float(np.mean(te)), float(np.max(te)),
        float(oinfo),
    ]


def build_n3_matrix(rng):
    """Return (X, y, keys) over the 256-form n=3 outreach family with intensive features."""
    X, y, keys = [], [], []
    for key, rules, labels in n3_family():
        y.append(exact_label(rules, labels))
        X.append(intensive_features(trajectory(rules, rng)))
        keys.append(key)
    return np.array(X), np.array(y), keys


def build_larger_matrix(rng):
    """Return (X, y, keys) over the held-out n = 4, 5, 6 outreach forms."""
    X, y, keys = [], [], []
    for key, rules, labels, _claimed in larger_forms():
        y.append(exact_label(rules, labels))          # recompute the exact label, do not trust the tag
        X.append(intensive_features(trajectory(rules, rng)))
        keys.append(key)
    return np.array(X), np.array(y), keys
