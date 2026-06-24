"""q155 — Coupling-centrality threshold for major-complex membership.

QUESTION
    Is there a coupling_centrality threshold that recovers major-complex membership (in-core
    vs spectator) as a per-node binary across the corpus, and where does it fail?

H1 (fixed before computing)
    A single coupling_centrality threshold separates in-core from excluded nodes with pooled
    ROC-AUC > 0.65 across the corpus (named multiparty forms plus random forms). Null: AUC <= 0.5,
    behavioral centrality carries no membership signal.

H2 (fixed before computing)
    Recovery degrades specifically on relay/chain forms where a tightly-coupled relay node is
    excluded from the core, with chain forms contributing the most false positives per node.
    Null: errors are uniform across topologies, so chain relays are not a systematic failure mode.

METHOD
    Per-node ground truth: 1 if the node's index is in the maximal complex's node_indices (read by
    exact IIT-4.0 Φ over reachable states), else 0. Per-node score: coupling_centrality from a seeded
    stochastic trajectory of the same form. Pool all nodes across the corpus and sweep the score
    threshold to trace the ROC; report pooled AUC (Mann-Whitney form, exact). The control compares
    pooled AUC against a known-faithful instrument and against a label-shuffled null. Each form is
    tagged by topology (star / chain / reciprocal / mediator / other) from its connectivity matrix;
    H2 reads false positives per node by topology, predicting chain forms lead.

SCOPE
    The corpus is synthetic Boolean coordination models. Every number is an in-silico reading of the
    centrality-vs-membership pairing, not a measurement of any field organization.

RUN
    source /tmp/rvenv/bin/activate && export PYPHI_WELCOME_OFF=yes && \
    python -m org_frontier.questions.q155_mc_membership_threshold.probe_mc_membership_threshold
"""

import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

import numpy as np

from org_frontier.recurrence.crqa import trajectory, coupling_centrality
from org_frontier.recurrence.crqa_phi_bridge import node_membership_labels, topology_of
from org_frontier.classifier.classifier import cm_from_rules
from org_frontier.threads.coalition_structure._harness import network, complex_over_states
from org_frontier.threads.designed_mediator._harness import _rule_of_one, _rule_of_set
from org_frontier.multiparty import forms as mp

STEPS = 600
FLIP = 0.08
N_RANDOM = 80
RANDOM_SEED = 0
TRAJ_SEED_BASE = 7000


def core_indices(rules, labels):
    """The major-complex node_indices (frozenset) at the state maximizing Φ, and that Φ."""
    net, tpm = network(rules, labels)
    _, core, phi = complex_over_states(net, tpm, len(rules))
    return (frozenset() if core is None else core), float(phi)


def roc_auc(scores, labels):
    """Exact ROC-AUC by the Mann-Whitney rank statistic, with ties at 0.5.

    Returns the probability a random positive outscores a random negative. Returns nan when one
    class is empty.
    """
    scores = np.asarray(scores, dtype=float)
    labels = np.asarray(labels, dtype=int)
    pos = scores[labels == 1]
    neg = scores[labels == 0]
    if pos.size == 0 or neg.size == 0:
        return float("nan")
    order = np.argsort(scores, kind="mergesort")
    ranks = np.empty(scores.size, dtype=float)
    s_sorted = scores[order]
    i = 0
    while i < s_sorted.size:
        j = i
        while j + 1 < s_sorted.size and s_sorted[j + 1] == s_sorted[i]:
            j += 1
        ranks[order[i:j + 1]] = (i + j) / 2.0 + 1.0  # 1-based average rank over the tie block
        i = j + 1
    rank_pos = ranks[labels == 1].sum()
    n_pos, n_neg = pos.size, neg.size
    auc = (rank_pos - n_pos * (n_pos + 1) / 2.0) / (n_pos * n_neg)
    return float(auc)


def best_threshold(scores, labels):
    """The score threshold (>= rule) maximizing balanced accuracy, with that balanced accuracy."""
    scores = np.asarray(scores, dtype=float)
    labels = np.asarray(labels, dtype=int)
    cands = np.unique(np.concatenate([scores, [scores.min() - 1.0, scores.max() + 1.0]]))
    best = (-1.0, float("nan"))
    P = max(int((labels == 1).sum()), 1)
    N = max(int((labels == 0).sum()), 1)
    for t in cands:
        pred = (scores >= t).astype(int)
        tpr = int(((pred == 1) & (labels == 1)).sum()) / P
        tnr = int(((pred == 0) & (labels == 0)).sum()) / N
        bal = (tpr + tnr) / 2.0
        if bal > best[0]:
            best = (bal, float(t))
    return best[1], best[0]


def rand_form(rng, n):
    """A random n-node Boolean form (same generator family as bridge_four, numpy RNG API)."""
    rules = []
    for _ in range(n):
        ins = [i for i in range(n) if rng.random() < 0.45] or [int(rng.integers(0, n))]
        if len(ins) == 1:
            rules.append(_rule_of_one(int(rng.integers(0, 4)), ins[0]))
        else:
            tt = [int(rng.integers(0, 2)) for _ in range(2 ** len(ins))]
            rules.append(_rule_of_set(tt, ins))
    return rules


def per_node_rows(rules, labels, traj_seed):
    """One row per node: (score, membership, topology). Trajectory and core both seeded/exact."""
    n = len(rules)
    rng = np.random.default_rng(traj_seed)
    traj = trajectory(rules, STEPS, rng, flip=FLIP)
    cen = coupling_centrality(traj)
    core, _ = core_indices(rules, labels)
    lab = node_membership_labels(core, n)
    topo = topology_of(cm_from_rules(rules))
    return [(float(cen[i]), int(lab[i]), topo) for i in range(n)]


def instrument_control():
    """Validate the AUC machinery and the membership read on a known case.

    The faithful triad reads verdict 'triadic' with max_phi 2.0 and a full three-node core, so every
    node is in-core. A perfectly separable toy ROC must read AUC 1.0; a label-shuffled null must read
    AUC near 0.5. Prints 'CONTROL ... PASS'.
    """
    from org_frontier.probes.lib import verdict, major_complex
    rules = [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]
    L = ("W", "S", "C")
    v = verdict(rules, L)
    core_labels, phi = major_complex(rules, L)
    assert v.structure == "triadic" and abs(v.max_phi - 2.0) < 1e-9, (v.structure, v.max_phi)
    assert set(core_labels) == set(L), core_labels  # all three nodes in-core
    # AUC machinery: a perfectly separable case and a tied case.
    assert abs(roc_auc([0.1, 0.2, 0.9, 1.0], [0, 0, 1, 1]) - 1.0) < 1e-9
    assert abs(roc_auc([5.0, 5.0, 5.0, 5.0], [0, 1, 0, 1]) - 0.5) < 1e-9
    # label-shuffled null on a real-looking score set is near chance
    rng = np.random.default_rng(0)
    s = rng.random(200)
    y = (rng.random(200) < 0.5).astype(int)
    null_auc = roc_auc(s, y)
    assert 0.4 < null_auc < 0.6, null_auc
    print(f"CONTROL faithful triad reads triadic Φ=2.0 full core; AUC machinery 1.000/0.500, "
          f"shuffled null {null_auc:.3f}: PASS")


def main():
    instrument_control()
    print()

    rows = []   # (key, n, topo, [(score, label)...])
    # Named multiparty forms. Seed by enumeration order so it reproduces regardless of PYTHONHASHSEED.
    for fi, f in enumerate(mp.FORMS):
        n = len(f.rules)
        seed = TRAJ_SEED_BASE + fi
        pr = per_node_rows(f.rules, f.labels, seed)
        rows.append((f.key, n, pr[0][2], [(s, l) for s, l, _ in pr]))

    # Random forms (n in {3,4,5}), one fixed seed stream.
    rng = np.random.default_rng(RANDOM_SEED)
    for k in range(N_RANDOM):
        n = int(rng.integers(3, 6))
        rules = rand_form(rng, n)
        labels = tuple("ABCDE"[:n])
        pr = per_node_rows(rules, labels, TRAJ_SEED_BASE + 100000 + k)
        rows.append((f"rand{k:02d}", n, pr[0][2], [(s, l) for s, l, _ in pr]))

    # Pool nodes.
    scores, labels, topos = [], [], []
    for key, n, topo, nr in rows:
        for s, l in nr:
            scores.append(s)
            labels.append(l)
            topos.append(topo)
    scores = np.array(scores)
    labels = np.array(labels)
    topos = np.array(topos)

    n_nodes = scores.size
    n_pos = int((labels == 1).sum())
    n_neg = int((labels == 0).sum())

    auc = roc_auc(scores, labels)
    thr, bal = best_threshold(scores, labels)

    # Label-shuffled null AUC (deterministic permutation).
    rng2 = np.random.default_rng(RANDOM_SEED)
    perm = rng2.permutation(labels)
    null_auc = roc_auc(scores, perm)

    print("POOLED MEMBERSHIP RECOVERY (per-node, corpus = 9 named + 80 random forms)")
    print(f"  nodes pooled        : {n_nodes}  (in-core {n_pos}, spectator {n_neg})")
    print(f"  pooled ROC-AUC      : {auc:.3f}")
    print(f"  label-shuffled null : {null_auc:.3f}")
    print(f"  best threshold (>=) : {thr:.4f}  balanced-acc {bal:.3f}")
    print()

    # Per-topology AUC and false-positive rate at the pooled threshold.
    print("PER-TOPOLOGY BREAKDOWN (threshold from the pooled sweep)")
    print(f"  {'topology':<11} {'nodes':>5} {'core':>5} {'spec':>5} {'AUC':>7} {'FP/node':>8} "
          f"{'FP':>4}")
    topo_order = ["star", "chain", "reciprocal", "mediator", "other"]
    fp_per_node = {}
    for t in topo_order:
        m = topos == t
        if not m.any():
            continue
        s_t, l_t = scores[m], labels[m]
        a_t = roc_auc(s_t, l_t)
        pred = (s_t >= thr).astype(int)
        fp = int(((pred == 1) & (l_t == 0)).sum())
        nn = int(m.sum())
        fpn = fp / nn
        fp_per_node[t] = fpn
        core_n = int((l_t == 1).sum())
        spec_n = int((l_t == 0).sum())
        a_str = "  n/a " if np.isnan(a_t) else f"{a_t:6.3f}"
        print(f"  {t:<11} {nn:>5} {core_n:>5} {spec_n:>5} {a_str:>7} {fpn:>8.3f} {fp:>4}")
    print()

    # ---- H1 verdict ----
    h1 = auc > 0.65
    print(f"H1 (single coupling-centrality threshold recovers membership at pooled AUC>0.65): "
          f"{'SUPPORTED' if h1 else 'REFUTED'}  [AUC={auc:.3f}, null={null_auc:.3f}]")

    # ---- H2 verdict ----
    # Predicted failure class is 'chain': it should have the highest false-positives-per-node.
    if "chain" in fp_per_node:
        chain_fpn = fp_per_node["chain"]
        others = {t: v for t, v in fp_per_node.items() if t != "chain"}
        max_other = max(others.values()) if others else 0.0
        h2 = chain_fpn >= max_other and chain_fpn > 0
        worst = max(fp_per_node, key=fp_per_node.get)
        print(f"H2 (chain/relay forms are the systematic false-positive class): "
              f"{'CONFIRMED' if h2 else 'NOT SUPPORTED'}  "
              f"[chain FP/node={chain_fpn:.3f}, worst topology={worst} "
              f"@ {fp_per_node[worst]:.3f}]")
    else:
        print("H2 (chain/relay forms are the systematic false-positive class): NOT SUPPORTED  "
              "[no chain forms in corpus]")


if __name__ == "__main__":
    main()
