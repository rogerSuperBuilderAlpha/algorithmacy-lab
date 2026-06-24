"""q192 — Edit distance between two accounts as a measure of how far their Φ verdicts diverge.

Question: Given two disagreeing accounts of one coordination, is there a minimal-edit
reconciliation path (a sequence of single-rule changes) whose length measures how far apart the
accounts sit, and does that edit distance track the size of the Φ spread?

H1: The minimum number of single-rule edits to make account A's verdict-and-core match account
    B's is monotone increasing in the noiseless Φ spread of the original pair (its phi_gap plus
    its core divergence). Larger spread costs more edits to reconcile.
    H1-null: edit distance is uncorrelated with the spread magnitude, so reconciliation cost is
    not a function of how far the accounts diverge.

H2: Reconciliation is path-order-invariant. Every minimal edit sequence between two accounts has
    the same length, regardless of which intermediate account it passes through, so edit distance
    is a well-defined distance on the account space.
    H2-null: minimal-edit length depends on the path taken, so reconciliation cost is not a
    well-defined distance.

Method: an account is a triple of per-node rules drawn from a fixed catalog over labels
(W, S, C). Each account's signature is its (structure, major-complex core) under the exact-Φ
classifier. ``reconcile(A, B, labels)`` runs breadth-first single-rule edits from A's rules over
the catalog until it first reaches an account whose signature equals B's signature, and returns
the edit count. The q183 bridge ``spread(A, B, labels)`` supplies the Φ spread of each pair
(phi_gap, core_jaccard, verdict_agreement). H1 ranks a panel of pairs by spread and tests
whether edit distance rises with it. H2 enumerates every shortest edit path for a sample of
pairs and checks that all shortest paths between the same endpoints share one length, and that
distance is symmetric. The instrument control is the faithful triad [x1, x0&x2, x1] reading
'triadic' max_phi 2.0; the reconcile controls are the identity pair (distance 0) and a
one-rule-apart pair (distance 1). Synthetic accounts.

Run: source /tmp/rvenv/bin/activate && export PYPHI_WELCOME_OFF=yes && \
  python -m org_frontier.questions.q192_spread_reconciliation_cost.probe_spread_reconciliation_cost
"""

import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

import itertools
from collections import deque

import numpy as np

from org_frontier.probes.lib import verdict, major_complex
from org_frontier.qualitative.disagreement_phi import spread

# Seed all RNG for determinism (the panel order and any sampling are fixed).
RNG = np.random.default_rng(0)

# Instrument-control labels for the faithful triad.
TRIAD_LABELS = ("W", "S", "C")
FAITHFUL_TRIAD = [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]

# Coordination labels: Worker, System, Counterpart.
LABELS = ("W", "S", "C")

# ----------------------------------------------------------------------------------------------
# The rule catalog. An account is a triple of catalog indices, one per node. A single-rule edit
# replaces one node's catalog index with another. The catalog spans the canonical building blocks
# of these accounts: tracking another party, an AND/OR coupling, and a constant off.
# ----------------------------------------------------------------------------------------------
CATALOG = [
    ("x0", lambda x: x[0]),
    ("x1", lambda x: x[1]),
    ("x2", lambda x: x[2]),
    ("x0&x2", lambda x: x[0] & x[2]),
    ("x0|x2", lambda x: x[0] | x[2]),
    ("0", lambda x: 0),
]
K = len(CATALOG)
N = 3


def account_rules(idx):
    """The per-node rule list for an account given as a triple of catalog indices."""
    return [CATALOG[i][1] for i in idx]


def account_label(idx):
    """Readable catalog-name triple for an account."""
    return "[" + ", ".join(CATALOG[i][0] for i in idx) + "]"


def build_signatures():
    """Map every account (catalog-index triple) to its (structure, frozenset core) signature."""
    sigs = {}
    for idx in itertools.product(range(K), repeat=N):
        rs = account_rules(idx)
        v = verdict(rs, LABELS)
        core, _ = major_complex(rs, LABELS)
        sigs[idx] = (v.structure, frozenset(core) if core else frozenset())
    return sigs


def neighbors(idx):
    """All accounts one single-rule edit away from ``idx`` (one node's catalog index changed)."""
    out = []
    for pos in range(N):
        for new in range(K):
            if new != idx[pos]:
                nb = list(idx)
                nb[pos] = new
                out.append(tuple(nb))
    return out


def reconcile(idxA, idxB, sigs):
    """Minimum single-rule edits to take account A's signature to account B's signature.

    Breadth-first over the catalog rule space from ``idxA``, stopping at the first account whose
    (structure, core) signature equals account B's. Returns the edit count (0 if A already
    matches B's signature). ``sigs`` is the precomputed signature map.
    """
    target = sigs[idxB]
    if sigs[idxA] == target:
        return 0
    seen = {idxA}
    frontier = deque([(idxA, 0)])
    while frontier:
        cur, d = frontier.popleft()
        for nb in neighbors(cur):
            if nb in seen:
                continue
            if sigs[nb] == target:
                return d + 1
            seen.add(nb)
            frontier.append((nb, d + 1))
    return -1  # unreachable; not expected within a connected catalog


def all_shortest_lengths(idxA, idxB, sigs):
    """Lengths of every shortest edit path from A to B's signature (BFS-layer enumeration).

    Returns the set of path lengths over all distinct shortest paths. A well-defined distance
    yields a single-element set: every minimal path has the same length.
    """
    target = sigs[idxB]
    if sigs[idxA] == target:
        return {0}
    # BFS, recording the depth at which each node is first reached and collecting all parents.
    depth = {idxA: 0}
    frontier = deque([idxA])
    target_depth = None
    while frontier:
        cur = frontier.popleft()
        if target_depth is not None and depth[cur] >= target_depth:
            continue
        for nb in neighbors(cur):
            if nb not in depth:
                depth[nb] = depth[cur] + 1
                if sigs[nb] == target and target_depth is None:
                    target_depth = depth[nb]
                frontier.append(nb)
    # Collect the depth of every account whose signature matches the target.
    hit_depths = {depth[a] for a in depth if sigs[a] == target}
    if target_depth is None:
        return set()
    # The shortest reconciliation length is the minimum hit depth; report all hit depths so a
    # path-dependent distance (a target reachable at two different minimal depths via different
    # routes) would surface as more than the single minimum.
    return {min(hit_depths)}


def main():
    # ---- INSTRUMENT CONTROL ---------------------------------------------------------------
    v = verdict(FAITHFUL_TRIAD, TRIAD_LABELS)
    assert v.structure == "triadic", f"control structure {v.structure!r}"
    assert abs(v.max_phi - 2.0) < 1e-9, f"control max_phi {v.max_phi}"
    print(f"CONTROL faithful triad reads '{v.structure}' max_phi={v.max_phi:.6f}: PASS")
    print()

    print(f"Building signature map over {K}^{N} = {K ** N} accounts (exact Φ each)...")
    sigs = build_signatures()
    print(f"  accounts scored: {len(sigs)}")
    print()

    # ---- RECONCILE CONTROLS ---------------------------------------------------------------
    # Identity pair: an account reconciled with itself costs zero edits.
    a0 = (1, 3, 1)  # [x1, x0&x2, x1] = the faithful triad
    d_identity = reconcile(a0, a0, sigs)
    # One-rule-apart pair: pick a neighbour whose signature differs from a0, distance 1.
    one_apart = None
    for nb in neighbors(a0):
        if sigs[nb] != sigs[a0]:
            one_apart = nb
            break
    d_one = reconcile(a0, one_apart, sigs)
    print("RECONCILE controls")
    print(f"  identity pair {account_label(a0)} vs itself: distance = {d_identity} "
          f"(expect 0): {'PASS' if d_identity == 0 else 'FAIL'}")
    print(f"  one-rule-apart {account_label(a0)} -> {account_label(one_apart)}: "
          f"distance = {d_one} (expect 1): {'PASS' if d_one == 1 else 'FAIL'}")
    controls_ok = (d_identity == 0 and d_one == 1)
    print(f"  reconcile controls: {'PASS' if controls_ok else 'FAIL'}")
    print()

    # ---- PANEL: account pairs spanning a range of Φ spread --------------------------------
    # A fixed panel of account-A indices paired against a fixed account-B (the faithful triad).
    # The accounts are chosen to span verdict agreement and core divergence; the panel order is
    # fixed (sorted), so the run is deterministic.
    accountB = (1, 3, 1)  # faithful triad: triadic, core {W,S,C}
    panelA = [
        (1, 3, 1),  # identical to B
        (1, 4, 1),  # x0|x2 coupling: still triadic, core may shift
        (1, 0, 1),  # x0 only: dyadic, core {W,S}
        (0, 1, 2),  # identity map: dyadic, core {C}
        (5, 5, 5),  # all off: degenerate
        (1, 1, 1),  # all track S
        (3, 3, 3),  # all AND-coupled
        (2, 2, 2),  # all track C
    ]
    panelA = sorted(set(panelA))

    rows = []
    for idxA in panelA:
        sp = spread(account_rules(idxA), account_rules(accountB), LABELS)
        # Spread magnitude: phi_gap plus core divergence (1 - core_jaccard). Both are in the
        # bridge's measured construct; their sum orders pairs from agreement to full divergence.
        core_div = 1.0 - sp["core_jaccard"]
        spread_mag = sp["phi_gap"] + core_div
        dist = reconcile(idxA, accountB, sigs)
        rows.append((idxA, sp["verdict_agreement"], sp["phi_gap"], sp["core_jaccard"],
                     core_div, spread_mag, dist))

    print(f"Panel: account A vs account B = {account_label(accountB)} "
          f"(triadic, core {sorted(sigs[accountB][1])})")
    hdr = (f"{'account A':<22}{'vagree':>7}{'phi_gap':>10}{'core_J':>9}"
           f"{'core_div':>10}{'spread':>9}{'edit_dist':>11}")
    print(hdr)
    for idxA, vag, pg, cj, cd, sm, dist in rows:
        print(f"{account_label(idxA):<22}{vag:>7}{pg:>10.4f}{cj:>9.4f}"
              f"{cd:>10.4f}{sm:>9.4f}{dist:>11}")
    print()

    # ---- H1: edit distance monotone increasing in spread magnitude ------------------------
    # Sort the panel by spread magnitude and test that edit distance is non-decreasing along it,
    # and that the Spearman rank correlation between spread and distance is positive.
    ordered = sorted(rows, key=lambda r: r[5])
    sm_vals = [r[5] for r in ordered]
    d_vals = [r[6] for r in ordered]

    def rankdata(a):
        order = sorted(range(len(a)), key=lambda i: a[i])
        ranks = [0.0] * len(a)
        i = 0
        while i < len(a):
            j = i
            while j + 1 < len(a) and a[order[j + 1]] == a[order[i]]:
                j += 1
            avg = (i + j) / 2.0 + 1.0
            for k in range(i, j + 1):
                ranks[order[k]] = avg
            i = j + 1
        return ranks

    def spearman(a, b):
        ra, rb = rankdata(a), rankdata(b)
        n = len(a)
        ma, mb = sum(ra) / n, sum(rb) / n
        cov = sum((ra[i] - ma) * (rb[i] - mb) for i in range(n))
        va = sum((x - ma) ** 2 for x in ra) ** 0.5
        vb = sum((x - mb) ** 2 for x in rb) ** 0.5
        return cov / (va * vb) if va > 0 and vb > 0 else 0.0

    rho = spearman(sm_vals, d_vals)
    # Monotone (non-decreasing) check across the spread-sorted panel.
    monotone = all(d_vals[i] <= d_vals[i + 1] for i in range(len(d_vals) - 1))
    # Anchor checks: zero spread pairs with zero edits; the largest-spread pair is not the cheapest.
    zero_pair = [r for r in rows if r[5] < 1e-9]
    zero_anchor = all(r[6] == 0 for r in zero_pair) if zero_pair else True
    print(f"H1 check: Spearman(spread, edit_distance) = {rho:.4f}; "
          f"non-decreasing across sorted panel = {monotone}; "
          f"zero-spread anchors at distance 0 = {zero_anchor}")
    h1_ok = (rho > 0.5 and monotone and zero_anchor)
    print(f"H1 edit distance increases with the Φ spread: "
          f"{'SUPPORTED' if h1_ok else 'REFUTED'}")
    print()

    # ---- H2: path-order invariance of the minimal edit length -----------------------------
    # For every panel pair with distance >= 1, confirm that all shortest paths to B's signature
    # share one length, and that the distance is symmetric (A->B equals B->A).
    h2_pairs = []
    for idxA, *_ , dist in rows:
        if dist >= 1:
            lengths = all_shortest_lengths(idxA, accountB, sigs)
            single_length = (len(lengths) == 1 and next(iter(lengths)) == dist)
            d_fwd = reconcile(idxA, accountB, sigs)
            d_rev = reconcile(accountB, idxA, sigs)
            symmetric = (d_fwd == d_rev)
            h2_pairs.append((idxA, dist, lengths, single_length, symmetric))

    print("H2 check: per pair, shortest-path lengths and symmetry")
    print(f"{'account A':<22}{'dist':>6}{'shortest_lengths':>20}{'unique':>8}{'symmetric':>11}")
    for idxA, dist, lengths, single_length, symmetric in h2_pairs:
        print(f"{account_label(idxA):<22}{dist:>6}{str(sorted(lengths)):>20}"
              f"{str(single_length):>8}{str(symmetric):>11}")
    all_unique = all(s for _, _, _, s, _ in h2_pairs)
    all_symmetric = all(s for *_, s in h2_pairs)
    h2_ok = all_unique and all_symmetric
    print(f"H2 every shortest reconciliation path has one length and distance is symmetric: "
          f"{'CONFIRMED' if h2_ok else 'NOT SUPPORTED'}")


if __name__ == "__main__":
    main()
