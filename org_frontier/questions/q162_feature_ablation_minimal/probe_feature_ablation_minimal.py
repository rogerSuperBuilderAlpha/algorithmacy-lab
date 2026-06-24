"""Probe 316 (Q162) — minimal CRQA feature set for the joint structural verdict, and whether
multidimensional whole-system recurrence is necessary beyond pairwise coupling features.

QUESTION
    A Boolean coordination form yields three structural facts from its exact IIT-4.0 major
    complex: the triadic/dyadic verdict (core size >= 3 vs == 2), the membership count (how many
    nodes the core includes), and the bottleneck status (whether one node uniquely dominates the
    leave-one-node-out drop in major-complex Φ, or the articulation is tied/absent). A CRQA
    reading of a sampled run produces several candidate feature families. Which minimal family set
    recovers all three facts jointly, and does whole-system multidimensional recurrence add signal
    beyond pairwise coupling statistics?

    Three feature families are read from one seeded trajectory per form:
      A  coupling prominence stats  - prominence summary of the pairwise coupling matrix plus
                                      node centrality and the prominence spread (11 columns).
      B  md_recurrence              - whole-system multidimensional recurrence DET and RR (2).
      C  transfer entropy           - directed lag-1 TE summary over ordered node pairs (6).

H1 (fixed before computing)
    The coupling-prominence family A alone matches the full set A+B (which adds md_recurrence) on
    held-out joint-verdict accuracy within 3 points. Null: dropping md_recurrence lowers held-out
    joint accuracy by more than 3 points, so whole-system recurrence carries non-redundant signal
    the pairwise coupling statistics miss.

H2 (fixed before computing)
    Adding the transfer-entropy family C to the CRQA set (A+B) yields no held-out joint-accuracy
    gain beyond 3 points, so CRQA and TE are behaviorally redundant for the structural verdict.
    Null: the transfer-entropy features raise held-out joint accuracy beyond A+B by more than
    3 points.

METHOD
    Forms: the curated 3-node forms_library plus the named multiparty forms (n in {3,4,5}), pooled
    with a seeded random-wiring ensemble (each node an arbitrary Boolean function of the others,
    n in {3,4,5}). Every form is labeled by exact IIT-4.0 Φ:
      td        - 1 if major-complex core size >= 3, else 0 (dyadic). Sub-dyadic forms (core < 2)
                  are dropped: a sub-dyadic core is neither category.
      msize     - the core size (membership count), an integer class.
      bneck     - 1 if the leave-one-node-out drop in major-complex Φ has a unique argmax above
                  tolerance (a single structural articulation node), else 0 (tie or none).
    The joint label is the triple (td, msize, bneck). Joint accuracy on a form counts only when
    all three are recovered.

    Classifier: a deterministic 1-nearest-neighbor over z-scored features, trained on a held-out
    split of the random ensemble and the curated corpus, evaluated on the held-out random forms.
    The split is a fixed index partition (no RNG in the split), so the held-out set is identical
    across feature sets and the comparison is a clean ablation. Each of the three labels is
    predicted by its own 1-NN over the same feature columns; joint accuracy is the fraction of
    held-out forms with all three labels correct.

    Feature sets compared, all on the identical train/test split:
      A      coupling prominence only
      B      md_recurrence only
      A+B    coupling prominence + md_recurrence  (the full CRQA set)
      A+B+C  full CRQA + transfer entropy
    H1 reads A vs A+B. H2 reads A+B vs A+B+C.

    Control = the worker-system-counterpart triad [x[1], x[0]&x[2], x[1]] with labels (W, S, C):
    structural verdict triadic, max_phi 2.0, full {W, S, C} core (msize 3), and the mediator S
    (node 1) is the coupling-centrality argmax of its sampled run.

    H1 is SUPPORTED if held-out joint accuracy of A is within 3 points of A+B (the md_recurrence
    drop is at most 3 points). H2 is CONFIRMED if A+B+C does not beat A+B by more than 3 points.
    Either is reported REFUTED / NOT SUPPORTED when the computed gap exceeds 3 points.

    Determinism: every trajectory uses numpy.random.default_rng(seed) with a fixed seed; the
    random ensemble uses numpy.random.default_rng(ENSEMBLE_SEED); the Φ library seeds its state
    search with numpy.random.default_rng(0). The train/test split is a fixed index partition.
    Re-runs reproduce byte for byte.

    Validation gap: exact IIT-4.0 Φ on small synthetic Boolean coordination forms. "Verdict",
    "membership", "bottleneck", "coupling prominence", "recurrence", and "transfer entropy" name
    graph-and-Φ quantities, not measured organizations. In-silico scope; the Φ-to-organization
    bridge is open. The CRQA and TE arms run on synthetic trajectories, so every accuracy is a
    baseline on synthetic data.

RUN
    source /tmp/rvenv/bin/activate && export PYPHI_WELCOME_OFF=yes && \
    python -m org_frontier.questions.q162_feature_ablation_minimal.probe_feature_ablation_minimal
"""

import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

import numpy as np
import pyphi
from pyphi import new_big_phi, exceptions

from org_frontier.probes.lib import verdict
from org_frontier.classifier.classifier import tpm_from_rules, cm_from_rules
from foundations.proxy_audit.exact_phi import reachable_states
from org_frontier.recurrence.crqa import trajectory, coupling_centrality
from org_frontier.recurrence.crqa_phi_bridge import (
    coupling_prominence_features,
    md_recurrence_features,
    transfer_entropy_features,
)
from org_frontier.corpus.forms_library import FORMS as FORMS3
from org_frontier.multiparty import forms as mp

pyphi.config.PROGRESS_BARS = False
pyphi.config.PARALLEL = False

# ---- fixed configuration (all RNG seeded so the run reproduces byte-for-byte) -------------
TOL = 1e-6
STEPS = 400
WARMUP = 20
FLIP = 0.08
MAX_LAG = 10
ENSEMBLE_SEED = 162
N_RANDOM = {3: 80, 4: 50}          # random forms drawn per node count
TRAJ_SEED_BASE = 7000              # per-form trajectory seed offset
TEST_FRACTION = 0.40               # held-out fraction of the random ensemble
WITHIN = 3.0 / 100.0               # 3-point tolerance for H1 / H2 (accuracy in [0,1])


# --------------------------------------------------------------------------------------
# Structural ground truth (fixed) read by exact IIT-4.0 Φ.
# --------------------------------------------------------------------------------------

def core_indices(rules, labels):
    """(core_index_tuple, phi) of the maximal complex, max over reachable states."""
    n = len(rules)
    tpm, cm = tpm_from_rules(rules), cm_from_rules(rules)
    net = pyphi.Network(tpm, cm=cm, node_labels=labels)
    best = (None, -1.0)
    for s in reachable_states(tpm, n):
        state = tuple((s >> i) & 1 for i in range(n))
        try:
            mc = new_big_phi.maximal_complex(net, state)
        except (exceptions.StateUnreachableError, ValueError):
            continue
        if isinstance(mc, new_big_phi.NullPhiStructure):
            continue
        if float(mc.phi) > best[1]:
            best = (tuple(mc.node_indices), float(mc.phi))
    return best


def mc_phi(rules, labels):
    """Major-complex Φ over reachable states; 0.0 when no irreducible complex exists.

    Reads the phi from ``core_indices`` (one maximal-complex sweep), so the base form and the
    leave-one-out variants use the identical exact-Φ search.
    """
    _, phi = core_indices(rules, labels)
    return float(phi) if phi is not None and phi > 0 else 0.0


def bottleneck_unique(rules, labels, base):
    """1 if the leave-one-node-out drop in mc Φ has a unique argmax above tolerance, else 0.

    ``base`` is the form's major-complex Φ, passed in from the already-computed structural label so
    the base search is not repeated. Each leave-one-out variant freezes one node to a constant and
    re-reads the exact major-complex Φ.
    """
    drops = []
    for k in range(len(rules)):
        frozen = list(rules)
        frozen[k] = (lambda x: 0)
        drops.append(base - mc_phi(frozen, labels))
    mx = max(drops)
    if mx <= TOL:
        return 0
    winners = [i for i, d in enumerate(drops) if abs(d - mx) <= TOL]
    return 1 if len(winners) == 1 else 0


# --------------------------------------------------------------------------------------
# Random-wiring ensemble (seeded).
# --------------------------------------------------------------------------------------

def random_wiring(n, rng):
    """Each node an arbitrary Boolean function of all the others — a topologically diverse family."""
    rules = [None] * n
    for i in range(n):
        ins = tuple(j for j in range(n) if j != i)
        table = rng.integers(0, 2, 2 ** len(ins))
        rules[i] = (lambda x, ins=ins, t=table:
                    int(t[sum((x[ins[k]] & 1) << k for k in range(len(ins)))]))
    return rules


# --------------------------------------------------------------------------------------
# Feature extraction (one trajectory per form, all three families).
# --------------------------------------------------------------------------------------

def all_features(rules, traj_seed):
    """Return (A, B, C) feature blocks for one seeded trajectory of the form."""
    rng = np.random.default_rng(traj_seed)
    traj = trajectory(rules, STEPS, rng, flip=FLIP, warmup=WARMUP)
    A = coupling_prominence_features(traj, max_lag=MAX_LAG)
    B = md_recurrence_features(traj)
    C = transfer_entropy_features(traj)
    return A, B, C


# --------------------------------------------------------------------------------------
# Corpus assembly with the joint structural label (td, msize, bneck).
# --------------------------------------------------------------------------------------

def labelled_form(rules, labels, traj_seed):
    """Build a record with features and the joint structural label, or None if sub-dyadic."""
    ci, phi = core_indices(rules, labels)
    size = len(ci) if ci else 0
    if size < 2:
        return None
    td = 1 if size >= 3 else 0
    base = float(phi) if phi is not None and phi > 0 else 0.0
    bn = bottleneck_unique(rules, labels, base)
    A, B, C = all_features(rules, traj_seed)
    return {"td": td, "msize": size, "bneck": bn, "A": A, "B": B, "C": C}


def build_data():
    """Curated records and random-ensemble records, each with features and the joint label."""
    curated = []
    raw = [(f.rules, ("W", "S", "C")) for f in FORMS3]
    raw += [(f.rules, f.labels) for f in mp.FORMS]
    for idx, (rules, labels) in enumerate(raw):
        rec = labelled_form(rules, labels, TRAJ_SEED_BASE + idx)
        if rec is not None:
            curated.append(rec)

    ensemble = []
    rng = np.random.default_rng(ENSEMBLE_SEED)
    seed = TRAJ_SEED_BASE + 1000
    for n, count in N_RANDOM.items():
        labels = tuple(f"x{i}" for i in range(n))
        for _ in range(count):
            rules = random_wiring(n, rng)
            rec = labelled_form(rules, labels, seed)
            seed += 1
            if rec is not None:
                ensemble.append(rec)
    return curated, ensemble


# --------------------------------------------------------------------------------------
# Deterministic 1-NN over z-scored feature columns.
# --------------------------------------------------------------------------------------

def _select(rec, families):
    """Concatenate the chosen feature families of one record into a single vector."""
    out = []
    for fam in families:
        out.extend(rec[fam])
    return np.asarray(out, dtype=float)


def _zscore_fit(X):
    """Column means and stds for z-scoring (std floored at TOL to avoid divide-by-zero)."""
    mu = X.mean(axis=0)
    sd = X.std(axis=0)
    sd = np.where(sd < TOL, 1.0, sd)
    return mu, sd


def _nn_predict(Xtr, ytr, Xte):
    """1-nearest-neighbor label for each test row (Euclidean over z-scored columns).

    Ties in distance resolve to the lowest training index (np.argmin is deterministic), so the
    prediction reproduces exactly.
    """
    preds = []
    for x in Xte:
        d = np.sum((Xtr - x) ** 2, axis=1)
        preds.append(ytr[int(np.argmin(d))])
    return np.asarray(preds)


def joint_accuracy(train, test, families):
    """Held-out joint accuracy of a feature set: all of (td, msize, bneck) recovered.

    Each label is predicted by its own 1-NN over the same z-scored feature columns. The split is
    fixed by the caller, so the comparison across feature sets is a clean ablation.
    """
    Xtr = np.array([_select(r, families) for r in train])
    Xte = np.array([_select(r, families) for r in test])
    mu, sd = _zscore_fit(Xtr)
    Xtr = (Xtr - mu) / sd
    Xte = (Xte - mu) / sd
    correct = np.ones(len(test), dtype=bool)
    per = {}
    for lab in ("td", "msize", "bneck"):
        ytr = np.array([r[lab] for r in train])
        yte = np.array([r[lab] for r in test])
        pred = _nn_predict(Xtr, ytr, Xte)
        hit = (pred == yte)
        per[lab] = float(hit.mean())
        correct &= hit
    return float(correct.mean()), per


# --------------------------------------------------------------------------------------
# Instrument control.
# --------------------------------------------------------------------------------------

def control():
    """INSTRUMENT CONTROL: the faithful worker-system-counterpart triad reads structurally
    triadic with max_phi 2.0 and full {W, S, C} core (msize 3), and the mediator S (node 1) is
    the coupling-centrality argmax of its sampled run."""
    rules = [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]
    labels = ("W", "S", "C")
    v = verdict(rules, labels)
    ci, phi = core_indices(rules, labels)
    rng = np.random.default_rng(TRAJ_SEED_BASE)
    traj = trajectory(rules, STEPS, rng, flip=FLIP, warmup=WARMUP)
    cc = coupling_centrality(traj, max_lag=MAX_LAG)
    cc_pick = int(np.argmax(cc))
    ok = (v.structure == "triadic" and abs(v.max_phi - 2.0) < TOL
          and set(ci) == {0, 1, 2} and abs(phi - 2.0) < TOL and cc_pick == 1)
    print("CONTROL faithful triad: structure=%s max_phi=%.3f core=%s msize=%d cc_pick=%d -> %s"
          % (v.structure, v.max_phi, str(ci), len(ci), cc_pick, "PASS" if ok else "FAIL"),
          flush=True)
    if not ok:
        raise SystemExit("instrument control failed")


# --------------------------------------------------------------------------------------
# Main.
# --------------------------------------------------------------------------------------

def main():
    control()
    print("=" * 92, flush=True)
    print("q162 — minimal CRQA feature set for the joint structural verdict (td, msize, bneck)",
          flush=True)
    print("=" * 92, flush=True)

    curated, ensemble = build_data()
    print("corpus: %d curated forms + %d random-ensemble forms (sub-dyadic dropped)"
          % (len(curated), len(ensemble)), flush=True)

    # Fixed index partition of the random ensemble: last TEST_FRACTION held out.
    n_test = int(round(len(ensemble) * TEST_FRACTION))
    test = ensemble[len(ensemble) - n_test:]
    ens_train = ensemble[:len(ensemble) - n_test]
    train = curated + ens_train
    n_tri = sum(r["td"] for r in test)
    n_bn = sum(r["bneck"] for r in test)
    print("train: %d forms (curated %d + random %d); held-out test: %d random forms"
          % (len(train), len(curated), len(ens_train), len(test)), flush=True)
    print("held-out test label mix: triadic %d/%d, unique-bottleneck %d/%d, msize classes %s"
          % (n_tri, len(test), n_bn, len(test),
             str(sorted(set(r["msize"] for r in test)))), flush=True)
    print(flush=True)

    sets = [
        ("A      (coupling prominence)", ("A",)),
        ("B      (md_recurrence)", ("B",)),
        ("A+B    (full CRQA)", ("A", "B")),
        ("A+B+C  (CRQA + transfer entropy)", ("A", "B", "C")),
    ]
    results = {}
    print("Held-out joint accuracy by feature set (1-NN, identical train/test split)", flush=True)
    print("-" * 92, flush=True)
    print("  %-34s %-8s %-8s %-8s %-8s" % ("feature set", "joint", "td", "msize", "bneck"),
          flush=True)
    for name, fams in sets:
        joint, per = joint_accuracy(train, test, fams)
        results[fams] = joint
        print("  %-34s %-8.3f %-8.3f %-8.3f %-8.3f"
              % (name, joint, per["td"], per["msize"], per["bneck"]), flush=True)
    print("-" * 92, flush=True)
    print(flush=True)

    acc_A = results[("A",)]
    acc_AB = results[("A", "B")]
    acc_ABC = results[("A", "B", "C")]
    md_drop = acc_AB - acc_A          # how much A loses by dropping md_recurrence
    te_gain = acc_ABC - acc_AB        # how much C adds on top of CRQA

    print("A joint %.3f ; A+B joint %.3f ; md_recurrence drop (A+B - A) = %.3f"
          % (acc_A, acc_AB, md_drop), flush=True)
    print("A+B joint %.3f ; A+B+C joint %.3f ; transfer-entropy gain (A+B+C - A+B) = %.3f"
          % (acc_AB, acc_ABC, te_gain), flush=True)
    print(flush=True)

    # ---- Verdicts ------------------------------------------------------------------------
    # H1: coupling prominence alone matches the full CRQA set within 3 points.
    h1 = md_drop <= WITHIN
    print("H1 (coupling prominence A within 3 pts of full CRQA A+B): %s"
          % ("SUPPORTED" if h1 else "REFUTED"), flush=True)
    print("    md_recurrence drop %.3f (%.1f pts); within tolerance %.3f: %s"
          % (md_drop, md_drop * 100, WITHIN, md_drop <= WITHIN), flush=True)

    # H2: adding transfer entropy yields no held-out gain beyond 3 points.
    h2 = te_gain <= WITHIN
    print("H2 (transfer entropy adds no held-out joint accuracy beyond CRQA): %s"
          % ("CONFIRMED" if h2 else "NOT SUPPORTED"), flush=True)
    print("    transfer-entropy gain %.3f (%.1f pts); within tolerance %.3f: %s"
          % (te_gain, te_gain * 100, WITHIN, te_gain <= WITHIN), flush=True)


if __name__ == "__main__":
    main()
