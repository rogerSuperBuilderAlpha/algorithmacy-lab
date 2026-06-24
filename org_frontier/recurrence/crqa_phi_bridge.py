"""Shared bridge: CRQA behavioral features paired with the structural exact-Φ verdict.

This module is the reusable spine for the recurrence empirical line. It runs a Boolean
coordination form as a stochastic dynamical system, reads a small fixed set of CRQA features
from the sampled run, and reads the structural ground truth (major-complex core size) from
exact IIT-4.0 Φ. One form yields a labeled feature vector: the behavioral side from a sampled
trajectory, the label side from the transition matrix.

Features (one vector per form):
  det     - whole-system multidimensional recurrence determinism (md_recurrence DET)
  rr      - whole-system recurrence rate (md_recurrence RR)
  lag_var - variance of the prominent pairwise lead-lag lags (lags whose prominence clears
            PROM_FLOOR), a measure of how spread the coupling delays are
  spread  - prominence spread: count of ordered pairwise links whose prominence clears
            PROM_FLOOR, a measure of coupling breadth

Label: triadic (1) when the structural major complex has a core of three or more nodes,
dyadic (0) when the core has two. Forms whose core has fewer than two nodes are dropped: a
sub-dyadic core is neither category.

Determinism: trajectory sampling is seeded per form, so a feature vector reproduces exactly.

Scope: the forms are synthetic Boolean coordination models. Every number here is an in-silico
reading of the CRQA-to-Φ pairing, not a measurement of any field organization.
"""

import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

import numpy as np

from org_frontier.recurrence.crqa import trajectory, coupling_matrix, md_recurrence

# Feature names in the fixed column order the classifier consumes.
FEATURE_NAMES = ("det", "rr", "lag_var", "spread")

PROM_FLOOR = 0.05   # prominence above this counts a pairwise link as present
STEPS = 500         # trajectory length sampled per form
FLIP = 0.08         # per-node update noise (keeps the run exploring, not collapsing)
MAX_LAG = 10        # lead-lag search window for the coupling matrix


def crqa_features(rules, traj_seed):
    """The four CRQA features for one Boolean form, from a seeded trajectory.

    Returns a length-4 float vector in FEATURE_NAMES order. ``traj_seed`` fixes the run, so
    the vector reproduces byte-for-byte on re-run.
    """
    rng = np.random.default_rng(traj_seed)
    traj = trajectory(rules, STEPS, rng, flip=FLIP)
    md = md_recurrence(traj)
    lag, prom = coupling_matrix(traj, max_lag=MAX_LAG)
    mask = prom > PROM_FLOOR
    np.fill_diagonal(mask, False)
    lags = lag[mask]
    lag_var = float(np.var(lags)) if lags.size else 0.0
    spread = int(mask.sum())
    return [float(md["det"]), float(md["rr"]), lag_var, float(spread)]


def crqa_features_at_length(rules, traj_seed, steps):
    """The four CRQA features for one Boolean form, from a seeded trajectory of ``steps`` length.

    Same readings as ``crqa_features``, with the trajectory length passed in rather than fixed at
    the module STEPS. This is the length-sweep entry point: the same seed gives the same run, so a
    longer sweep is a prefix-stable continuation in distribution and the feature vector at each
    length reproduces byte-for-byte. Returns a length-4 float vector in FEATURE_NAMES order.
    """
    rng = np.random.default_rng(traj_seed)
    traj = trajectory(rules, steps, rng, flip=FLIP)
    md = md_recurrence(traj)
    lag, prom = coupling_matrix(traj, max_lag=MAX_LAG)
    mask = prom > PROM_FLOOR
    np.fill_diagonal(mask, False)
    lags = lag[mask]
    lag_var = float(np.var(lags)) if lags.size else 0.0
    spread = int(mask.sum())
    return [float(md["det"]), float(md["rr"]), lag_var, float(spread)]


def whole_system_recurrence(rules, traj_seed):
    """Whole-system md_recurrence (DET, RR) for one Boolean form, from a seeded trajectory.

    Returns (det, rr), the two whole-system behavioral readings that pair with whole-system Φ.
    ``traj_seed`` fixes the run, so both values reproduce byte-for-byte on re-run. This is the
    feature side of the Φ-magnitude regression: DET is the share of recurrence on deterministic
    diagonal lines, RR the gross density of revisited global states.
    """
    rng = np.random.default_rng(traj_seed)
    traj = trajectory(rules, STEPS, rng, flip=FLIP)
    md = md_recurrence(traj)
    return float(md["det"]), float(md["rr"])


def core_label(core):
    """Map a major-complex core (a tuple of member labels/indices) to triadic/dyadic/None.

    1 = triadic (core size >= 3), 0 = dyadic (core size == 2), None = sub-dyadic (drop).
    """
    size = len(core) if core else 0
    if size >= 3:
        return 1
    if size == 2:
        return 0
    return None


def node_membership_labels(core, n):
    """Per-node binary membership in the major complex.

    ``core`` is the iterable of node indices the maximal complex includes (its node_indices).
    Returns a length-``n`` list with 1 for an in-core node and 0 for an excluded spectator.
    """
    members = set(core) if core else set()
    return [1 if i in members else 0 for i in range(n)]


def topology_of(cm):
    """Coarse topology class of a Boolean form from its connectivity matrix ``cm`` (n x n,
    1 = i feeds j). Off-diagonal edges only; self-loops are ignored.

    Returns one of 'star', 'chain', 'reciprocal', 'mediator', or 'other':
      reciprocal - some pair i,j feeds each other (cm[i,j] and cm[j,i]) and no further structure
                   dominates; mutual coupling is the defining motif.
      star       - one node is the unique source/sink hub for the others (a high-degree center
                   with the rest only attached to it).
      chain      - the edges form a single directed path with no branching (each interior node
                   has one in and one out among the others).
      mediator   - a single node lies on the only paths between two otherwise unconnected halves
                   (an articulation node) without being a pure star hub.
      other      - none of the above.
    """
    import numpy as np
    A = np.asarray(cm, dtype=int).copy()
    n = A.shape[0]
    np.fill_diagonal(A, 0)
    if A.sum() == 0:
        return "other"
    # reciprocal: any mutual edge
    mutual = [(i, j) for i in range(n) for j in range(i + 1, n) if A[i, j] and A[j, i]]
    # undirected degree
    U = ((A + A.T) > 0).astype(int)
    deg = U.sum(0)
    # star: one hub adjacent to every other node, leaves adjacent only to the hub
    for h in range(n):
        leaves = [k for k in range(n) if k != h]
        if all(U[h, k] for k in leaves) and all(deg[k] == 1 for k in leaves):
            return "star"
    if mutual:
        return "reciprocal"
    # chain: connected, every node degree <= 2, exactly two endpoints of degree 1
    nonzero = [k for k in range(n) if deg[k] > 0]
    if nonzero and all(deg[k] <= 2 for k in nonzero):
        endpoints = [k for k in nonzero if deg[k] == 1]
        # single path: edge count == nodes-1 over the touched nodes, two endpoints
        edges = int(U[np.triu_indices(n, 1)].sum())
        if len(endpoints) == 2 and edges == len(nonzero) - 1:
            return "chain"
    # mediator: an articulation node whose removal disconnects the rest
    def _components(mask_nodes):
        seen = set()
        comps = 0
        for s in mask_nodes:
            if s in seen:
                continue
            comps += 1
            stack = [s]
            while stack:
                u = stack.pop()
                if u in seen:
                    continue
                seen.add(u)
                for v in mask_nodes:
                    if v not in seen and U[u, v]:
                        stack.append(v)
        return comps
    touched = [k for k in range(n) if deg[k] > 0]
    if len(touched) >= 3:
        base = _components(touched)
        for m in touched:
            rest = [k for k in touched if k != m]
            if rest and _components(rest) > base:
                return "mediator"
    return "other"


# ---------------------------------------------------------------------------------------------
# Directed-edge orientation: transfer entropy and DCRP peak-lag sign
# ---------------------------------------------------------------------------------------------

def transfer_entropy_binary(source, target):
    """Time-lag-1 transfer entropy from a binary ``source`` series to a binary ``target`` series.

    TE(source -> target) = I(target_{t+1} ; source_t | target_t), the reduction in uncertainty
    about the target's next state from knowing the source's current state once the target's own
    current state is held fixed. The estimate uses the plug-in (maximum-likelihood) joint counts
    over the three binary variables (target_t, source_t, target_{t+1}); it is non-negative and in
    bits.

    A directed read edge i -> j (j's rule depends on i) makes TE(i -> j) large because i_t carries
    information about j_{t+1} beyond j_t. The reverse TE(j -> i) need not vanish on a coupled pair,
    so orientation is read from the SIGN of the difference TE(i->j) - TE(j->i), not from either
    value alone.
    """
    s = np.asarray(source, dtype=int).ravel()
    t = np.asarray(target, dtype=int).ravel()
    tp = t[1:]          # target_{t+1}
    tc = t[:-1]         # target_t
    sc = s[:-1]         # source_t
    n = tp.size
    if n == 0:
        return 0.0
    # joint counts over (tc, sc, tp), each binary -> 8 cells
    joint = np.zeros((2, 2, 2), dtype=float)
    for a, b, c in zip(tc, sc, tp):
        joint[a, b, c] += 1.0
    p = joint / n
    te = 0.0
    for a in range(2):
        for b in range(2):
            for c in range(2):
                pabc = p[a, b, c]
                if pabc <= 0.0:
                    continue
                p_ab = p[a, b, :].sum()       # P(tc=a, sc=b)
                p_ac = p[a, :, c].sum()       # P(tc=a, tp=c)
                p_a = p[a, :, :].sum()        # P(tc=a)
                denom = p_ab * p_ac
                if denom <= 0.0:
                    continue
                te += pabc * np.log2((pabc * p_a) / denom)
    return float(max(te, 0.0))


def te_orients_edge(traj, i, j):
    """True when transfer entropy orients the directed edge i -> j correctly.

    The edge i -> j means j's rule reads i, so i leads j. TE reads the edge correctly when
    TE(i -> j) > TE(j -> i). Ties (equal TE) count as a miss.
    """
    te_ij = transfer_entropy_binary(traj[:, i], traj[:, j])
    te_ji = transfer_entropy_binary(traj[:, j], traj[:, i])
    return te_ij > te_ji


def dcrp_orients_edge(traj, i, j, max_lag=10):
    """True when the DCRP peak-lag sign orients the directed edge i -> j correctly.

    Uses ``peak`` on the ordered pair (i, j): a positive peak lag means i leads j, which is the
    correct orientation for the edge i -> j. Lag 0 (synchronous) counts as a miss.
    """
    from org_frontier.recurrence.crqa import peak
    lag, _prom = peak(traj[:, i], traj[:, j], max_lag=max_lag)
    return lag > 0


# ---------------------------------------------------------------------------------------------
# Designed-mediator harness: matched interested vs faithful mediators on one wiring graph
# ---------------------------------------------------------------------------------------------
#
# The triad is W' = S, C' = S, S' = f(W, S, C): the mediator reads both parties and its own
# previous state. Every form here uses that one wiring graph, so the connectivity matrix is
# identical across forms and the structural exact-Φ core is the only thing that can differ.
#
# A mediator's rule is a truth table tt over (W, S, C), indexed tt[4*W + 2*S + C].
# Faithful   : tt symmetric under swapping the two parties, f(W,S,C) == f(C,S,W). The rule
#              treats the parties as interchangeable, so it commits a joint determination of the
#              two warrants and serves neither party's agenda.
# Interested : tt asymmetric under that swap. The rule weights one party's warrant over the
#              other's, so it serves an objective (an agenda favoring that party) instead of a
#              neutral joint determination.
# The harness keeps only forms whose rule reads all three inputs and whose major-complex core is
# the full {W, S, C}, so a matched interested form and a matched faithful form share both wiring
# graph and structural Φ-core. Any separation between them is then behavioral, not structural.

from itertools import product as _product

from org_frontier.classifier.classifier import cm_from_rules as _cm_from_rules

MED_LABELS = ("W", "S", "C")     # node 0 = W, node 1 = S (mediator), node 2 = C


def mediator_rules(tt):
    """The triad W' = S, C' = S, S' = tt[4*W + 2*S + C], as a list of per-node lambdas."""
    f = lambda w, s, c: tt[4 * w + 2 * s + c]
    return [lambda x: x[1], lambda x, f=f: f(x[0], x[1], x[2]), lambda x: x[1]]


def _reads_all(tt):
    """True when the mediator's rule depends on W, on S, and on C (full in-degree)."""
    cm = _cm_from_rules(mediator_rules(tt))
    return bool(cm[0, 1] and cm[1, 1] and cm[2, 1])


def _is_faithful(tt):
    """True when the rule is symmetric under swapping the two parties (W <-> C)."""
    f = lambda w, s, c: tt[4 * w + 2 * s + c]
    return all(
        f(w, s, c) == f(c, s, w)
        for w in (0, 1) for s in (0, 1) for c in (0, 1)
    )


def enumerate_mediators():
    """All full-input, full-core triad mediators on the one wiring graph, split by interestedness.

    Returns (faithful, interested): two lists of 8-bit truth tables. Every form reads all three
    inputs and has the full {W, S, C} major-complex core, so the two pools are matched on wiring
    graph and on structural Φ-core. Faithful rules are symmetric in the two parties; interested
    rules are asymmetric (they serve one party's agenda).
    """
    from org_frontier.probes.lib import major_complex
    faithful, interested = [], []
    for tt in _product((0, 1), repeat=8):
        if not _reads_all(tt):
            continue
        core, _ = major_complex(mediator_rules(tt), MED_LABELS)
        if tuple(core) != MED_LABELS:
            continue
        (faithful if _is_faithful(tt) else interested).append(tt)
    return faithful, interested


def outgoing_prominence(tt, traj_seed, steps=STEPS, flip=FLIP, max_lag=MAX_LAG):
    """Mean DCRP prominence on the mediator's two outgoing edges (S->W and S->C).

    The mediator is node 1; its outgoing edges run to the parties it determines. A high
    prominence means the parties' states reliably recur at a fixed lag behind the mediator's,
    the behavioral trace of the mediator steering them. ``traj_seed`` fixes the sampled run so
    the value reproduces byte-for-byte.
    """
    rng = np.random.default_rng(traj_seed)
    traj = trajectory(mediator_rules(tt), steps, rng, flip=flip)
    _, prom = coupling_matrix(traj, max_lag=max_lag)
    return float((prom[1, 0] + prom[1, 2]) / 2.0)


# ---------------------------------------------------------------------------------------------
# Feature families for verdict-recovery ablation
# ---------------------------------------------------------------------------------------------
#
# Three named families read from one seeded trajectory, each a fixed-length summary vector so a
# classifier consumes the same columns for any node count n. The families are kept separable so an
# ablation can hold one out and read the held-out accuracy of the rest.

from org_frontier.recurrence.crqa import coupling_centrality as _coupling_centrality


def _summ5(vals):
    """A fixed five-number summary of a value list: mean, std, max, min, and count above floor.

    Reduces a variable-length per-pair or per-node quantity to a fixed-width feature block so the
    same columns describe any node count. Empty input yields zeros.
    """
    a = np.asarray(vals, dtype=float).ravel()
    if a.size == 0:
        return [0.0, 0.0, 0.0, 0.0, 0.0]
    above = float((a > PROM_FLOOR).sum())
    return [float(a.mean()), float(a.std()), float(a.max()), float(a.min()), above]


def coupling_prominence_features(traj, max_lag=MAX_LAG):
    """Family A: prominence statistics of the pairwise coupling matrix plus node centrality.

    Reads only the prominence side of ``coupling_matrix`` and the behavioral centrality, no
    whole-system recurrence. Returns a fixed 11-vector: a five-number summary of the off-diagonal
    prominences, a five-number summary of the node centralities, and the prominence spread (count
    of ordered links above PROM_FLOOR).
    """
    _, prom = coupling_matrix(traj, max_lag=max_lag)
    off = prom.copy()
    np.fill_diagonal(off, np.nan)
    flat = off[~np.isnan(off)]
    cc = _coupling_centrality(traj, max_lag=max_lag, prom_floor=PROM_FLOOR)
    mask = prom > PROM_FLOOR
    np.fill_diagonal(mask, False)
    spread = float(mask.sum())
    return _summ5(flat) + _summ5(cc) + [spread]


def md_recurrence_features(traj):
    """Family B: whole-system multidimensional recurrence — md_recurrence DET and RR.

    Returns a fixed 2-vector. This is the whole-system behavioral reading that pairs with
    whole-system Φ; it carries information no pairwise coupling statistic sees.
    """
    md = md_recurrence(traj)
    return [float(md["det"]), float(md["rr"])]


def transfer_entropy_features(traj):
    """Family C: transfer-entropy statistics over ordered node pairs.

    For every ordered pair (i, j) the lag-1 binary TE(i -> j) is computed. Returns a fixed
    6-vector: a five-number summary of the directed TE values plus the mean absolute net flow
    mean(|TE(i->j) - TE(j->i)|) over unordered pairs, a measure of how directed the coupling is.
    """
    n = traj.shape[1]
    te = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            te[i, j] = transfer_entropy_binary(traj[:, i], traj[:, j])
    off = [te[i, j] for i in range(n) for j in range(n) if i != j]
    net = [abs(te[i, j] - te[j, i]) for i in range(n) for j in range(i + 1, n)]
    net_mean = float(np.mean(net)) if net else 0.0
    return _summ5(off) + [net_mean]
