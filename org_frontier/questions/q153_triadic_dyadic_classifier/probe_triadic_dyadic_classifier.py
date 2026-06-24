"""q153 — Can a few CRQA features classify a form's exact-Φ verdict as triadic vs dyadic?

QUESTION
    A form has a behavioral signature (CRQA features read from a sampled run) and a structural
    ground truth (the major-complex core size read from exact IIT-4.0 Φ). Does a small set of
    CRQA features — whole-system md_recurrence DET and RR, the variance of the prominent
    pairwise lags, and the prominence spread (count of pairwise links above a floor) — classify
    the structural verdict triadic (3+ node core) versus dyadic (2 node core) across the corpus?

H1  A logistic classifier on those four features separates triadic from dyadic forms with
    held-out accuracy above the majority-class baseline. Null: held-out accuracy is at or below
    the majority-class baseline (no behavioral signal beyond guessing the larger class). A
    label-shuffled classifier is the control and should land at the baseline.

H2  The single most predictive feature is the prominence spread (coupling breadth: the count of
    pairwise links above the floor), carrying the largest-magnitude standardized coefficient.
    Null: whole-system DET (behavioral richness) carries the largest coefficient.

METHOD
    Corpus: the 3-node forms_library plus a random 3-node ensemble (rand_form) and a random
    4-node ensemble (rand_form4). Each form is labeled triadic/dyadic by its major-complex core
    size (>=3 vs ==2); sub-dyadic cores are dropped. Triadic forms are rare among random wirings,
    so the pool is balanced to a fixed dyadic:triadic ratio (all triadic forms kept, dyadic forms
    sampled with a fixed seed) to make accuracy a meaningful metric against a near-even baseline.
    Features come from the shared bridge module crqa_phi_bridge. A logistic regression on
    standardized features is scored by 5-fold stratified cross-validation. The control repeats
    the cross-validation on shuffled labels. H1 is SUPPORTED if real held-out accuracy exceeds
    the majority-class baseline. H2 is CONFIRMED if the spread coefficient has the largest
    magnitude in a full-corpus fit.

    Control = the worker-system-counterpart triad [x[1], x[0]&x[2], x[1]] with labels (W,S,C):
    verdict triadic, max_phi 2.0, full 3-node core (label triadic).

    Every number is exact IIT-4.0 Φ on synthetic Boolean coordination forms. This is an in-silico
    study of the CRQA-to-Φ bridge, not a measurement of any field organization.

RUN
    source /tmp/rvenv/bin/activate && export PYPHI_WELCOME_OFF=yes && \
    python -m org_frontier.questions.q153_triadic_dyadic_classifier.probe_triadic_dyadic_classifier
"""

import os
import random
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import StratifiedKFold
from sklearn.preprocessing import StandardScaler

from org_frontier.probes.lib import verdict, major_complex
from org_frontier.corpus.forms_library import FORMS
from org_frontier.recurrence.crqa_experiments import rand_form
from org_frontier.recurrence.bridge_four import rand_form4, major_complex as major_complex_n
from org_frontier.recurrence.crqa_phi_bridge import (
    crqa_features, core_label, FEATURE_NAMES)

# ---- fixed configuration (all RNG seeded so the run reproduces byte-for-byte) -------------
N_RAND3 = 120          # random 3-node forms drawn
N_RAND4 = 120          # random 4-node forms drawn
DYADIC_PER_TRIADIC = 1.5   # balance ratio: dyadic kept per triadic (baseline ~0.60)
RAND3_SEED = 0
RAND4_SEED = 1
DYADIC_SAMPLE_SEED = 42    # which dyadic forms survive the balance
ORDER_SEED = 7             # corpus row order (does not affect stratified CV result)
CV_SEED = 0
SHUFFLE_SEED = 7

# trajectory seeds: a distinct fixed seed per pool member, so features are deterministic.
TRAJ_SEED_LIBRARY = 100    # forms_library member i -> 100 + i
TRAJ_SEED_RAND3 = 1000     # random 3-node form k -> 1000 + k
TRAJ_SEED_RAND4 = 2000     # random 4-node form k -> 2000 + k


def _build_pool():
    """The full labeled pool before balancing: list of (label, traj_seed, rules)."""
    pool = []
    # curated 3-node corpus
    for i, f in enumerate(FORMS):
        core, _ = major_complex(f.rules, ("W", "S", "C"))
        lab = core_label(core)
        if lab is not None:
            pool.append((lab, TRAJ_SEED_LIBRARY + i, f.rules))
    # random 3-node ensemble
    rng = random.Random(RAND3_SEED)
    for k in range(N_RAND3):
        rules = rand_form(rng)
        core, _ = major_complex_n(rules, 3)
        lab = core_label(core)
        if lab is not None:
            pool.append((lab, TRAJ_SEED_RAND3 + k, rules))
    # random 4-node ensemble
    rng = random.Random(RAND4_SEED)
    for k in range(N_RAND4):
        rules = rand_form4(rng)
        core, _ = major_complex_n(rules, 4)
        lab = core_label(core)
        if lab is not None:
            pool.append((lab, TRAJ_SEED_RAND4 + k, rules))
    return pool


def _balance(pool):
    """Keep all triadic forms; sample dyadic forms to the fixed ratio. Deterministic."""
    tri = [p for p in pool if p[0] == 1]
    dy = [p for p in pool if p[0] == 0]
    random.Random(DYADIC_SAMPLE_SEED).shuffle(dy)
    n_dy = int(round(len(tri) * DYADIC_PER_TRIADIC))
    sel = tri + dy[:n_dy]
    random.Random(ORDER_SEED).shuffle(sel)
    return sel, len(tri), len(dy)


def _features_and_labels(sel):
    X = [crqa_features(rules, seed) for (_lab, seed, rules) in sel]
    y = [lab for (lab, _seed, _rules) in sel]
    return np.array(X, dtype=float), np.array(y, dtype=int)


def _cv_accuracy(X, y):
    """Mean 5-fold stratified held-out accuracy of a standardized logistic classifier."""
    skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=CV_SEED)
    accs = []
    for tr_i, te_i in skf.split(X, y):
        sc = StandardScaler().fit(X[tr_i])
        clf = LogisticRegression(max_iter=2000, random_state=0).fit(
            sc.transform(X[tr_i]), y[tr_i])
        accs.append(clf.score(sc.transform(X[te_i]), y[te_i]))
    return float(np.mean(accs))


def instrument_control():
    """Validate the machinery on the known worker-system-counterpart triad."""
    rules = [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]
    labels = ("W", "S", "C")
    v = verdict(rules, labels)
    core, phi = major_complex(rules, labels)
    assert v.structure == "triadic", v.structure
    assert abs(v.max_phi - 2.0) < 1e-6, v.max_phi
    assert set(core) == set(labels), core
    assert core_label(core) == 1, core
    # the feature extractor returns a finite length-4 vector for the control form
    feats = crqa_features(rules, TRAJ_SEED_LIBRARY)
    assert len(feats) == len(FEATURE_NAMES), feats
    assert all(np.isfinite(feats)), feats
    print(
        f"CONTROL worker-system-counterpart triad: verdict={v.structure}, "
        f"max_phi={v.max_phi:.3f}, core={core} (label=triadic): PASS"
    )


def main():
    instrument_control()
    print("=" * 88)
    print("q153 — CRQA features classifying the triadic-vs-dyadic exact-Φ verdict")
    print("=" * 88)

    pool = _build_pool()
    sel, n_tri_pool, n_dy_pool = _balance(pool)
    X, y = _features_and_labels(sel)

    n = len(y)
    n_tri = int(y.sum())
    n_dy = n - n_tri
    baseline = max(y.mean(), 1.0 - y.mean())

    print(
        f"pool: {n_tri_pool} triadic + {n_dy_pool} dyadic forms; "
        f"balanced corpus: n={n} ({n_tri} triadic, {n_dy} dyadic), "
        f"majority-class baseline={baseline:.4f}"
    )

    real_acc = _cv_accuracy(X, y)
    ys = y.copy()
    np.random.default_rng(SHUFFLE_SEED).shuffle(ys)
    shuffle_acc = _cv_accuracy(X, ys)

    # full-corpus fit for the standardized coefficients
    sc = StandardScaler().fit(X)
    clf = LogisticRegression(max_iter=2000, random_state=0).fit(sc.transform(X), y)
    coefs = clf.coef_[0]
    abs_coefs = np.abs(coefs)
    top_idx = int(np.argmax(abs_coefs))
    top_name = FEATURE_NAMES[top_idx]

    print("-" * 88)
    print(f"  {'metric':<34}{'value'}")
    print(f"  {'5-fold held-out accuracy (real)':<34}{real_acc:.4f}")
    print(f"  {'5-fold held-out accuracy (shuffled)':<34}{shuffle_acc:.4f}")
    print(f"  {'majority-class baseline':<34}{baseline:.4f}")
    print("-" * 88)
    print(f"  {'feature':<12}{'standardized coef':<20}{'|coef|'}")
    for name, c in zip(FEATURE_NAMES, coefs):
        mark = "  <- largest" if name == top_name else ""
        print(f"  {name:<12}{c:<20.4f}{abs(c):.4f}{mark}")
    print("=" * 88)

    # ---- H1 ---------------------------------------------------------------------------
    h1_supported = real_acc > baseline
    print(
        f"H1 summary: real held-out accuracy {real_acc:.4f} "
        f"{'>' if h1_supported else '<='} baseline {baseline:.4f}; "
        f"shuffle control {shuffle_acc:.4f}."
    )
    # ---- H2 ---------------------------------------------------------------------------
    h2_confirmed = top_name == "spread"
    print(
        f"H2 summary: largest standardized coefficient is '{top_name}' "
        f"(|coef|={abs_coefs[top_idx]:.4f})."
    )
    print("=" * 88)

    print(
        "H1 CRQA features beat the majority baseline: "
        + ("SUPPORTED" if h1_supported else "REFUTED")
    )
    print(
        "H2 prominence spread is the most predictive feature: "
        + ("CONFIRMED" if h2_confirmed else "NOT SUPPORTED")
    )


if __name__ == "__main__":
    main()
