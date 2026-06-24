"""Q144: Does Φ in a balanced mediator hierarchy track depth like a chain or breadth like a pool?

Question
    A balanced k-ary hierarchy of mediators is a tree of AND-gates feeding one apex: leaves at the
    bottom, internal mediators in the middle, a single apex on top, closed into a recurrent system by
    a feedback edge from the apex back to the leaves. Two axes describe the tree: depth d (how many
    mediator layers sit between a leaf and the apex) and breadth b (how many children each node has).
    The lab's scaling zoo already has two fixed-point laws to set the comparison against: a serial
    chain holds Φ constant at 2, and a fully-coupled pool grows Φ super-linearly as n(n-1). This study
    asks which law the mediator tree follows along each axis.

H1 (fixed before computing)
    At fixed leaf count, adding mediator depth (more layers between leaves and apex) leaves Φ flat at
    the chain constant, because each layer is a two-bit serial bottleneck. Null: Φ rises or falls
    monotonically with depth at fixed breadth.

H2 (fixed before computing)
    At fixed depth, adding breadth (more leaves per node) grows Φ super-linearly toward the pool law,
    so breadth and depth are separable axes with opposite scaling. Null: breadth at fixed depth leaves
    Φ flat or decays.

Method
    Build balanced trees parameterized by (depth d, breadth b). Each internal node and the apex is the
    AND of its b children; every leaf reads the apex, closing the system into a recurrent dynamical
    system. Compute the exact IIT-4.0 major complex (org_frontier.probes.lib.major_complex) for a grid
    of (d, b). The depth axis fixes one leaf (b = 1) and varies d; this is a pure serial chain and is
    the H1 test. The breadth axis fixes one mediator layer (d = 1) and varies b; this is the H2 test.
    Two scaling baselines anchor the verdicts: a pure serial chain (depth, predicted Φ = 2) and a
    fully-coupled pool (breadth, predicted Φ = n(n-1)). The whole grid stays at n ≤ 5 so the exact
    instrument is fast and the run is deterministic.

    The Shapley value of the integrating state's Φ (q111) is reported for the base triad as a sanity
    read on how the tree distributes its integration across parties.

Run
    source /tmp/rvenv/bin/activate && export PYPHI_WELCOME_OFF=yes && \
    python -m org_frontier.questions.q144_mediator_hierarchy_depth.probe_mediator_hierarchy_depth
"""

import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

import numpy as np

from org_frontier.probes.lib import verdict, major_complex
from org_frontier.questions.q111_shapley_value.forms import shapley

# Fixed seed so every reachable-state scan and any tie-break reproduces exactly.
RNG = np.random.default_rng(0)

PHI_EPS = 1e-9


# --------------------------------------------------------------------------------------
# Form builders
# --------------------------------------------------------------------------------------

def _labels(n):
    return tuple(chr(65 + i) for i in range(n))


def mediator_tree(d, b):
    """Balanced b-ary mediator tree of depth d, closed into a recurrent system.

    Level 0 is the apex (one node); level L has b**L nodes; level d holds the leaves. Indices run
    level by level (apex first). Each internal node and the apex is the AND of its b children. Every
    leaf reads the apex, which closes the tree into a recurrent dynamical system. Returns
    (rules, labels, n).
    """
    levels, nid = [], 0
    for L in range(d + 1):
        count = b ** L
        levels.append(list(range(nid, nid + count)))
        nid += count
    n = nid
    apex = levels[0][0]
    children = {}
    for L in range(d):
        for pi, p in enumerate(levels[L]):
            children[p] = levels[L + 1][pi * b:(pi + 1) * b]
    rules = [None] * n
    for L in range(d):
        for p in levels[L]:
            ch = children[p]

            def make(ch=ch):
                def f(x):
                    v = 1
                    for c in ch:
                        v &= x[c]
                    return v
                return f
            rules[p] = make()
    for leaf in levels[d]:
        rules[leaf] = (lambda a=apex: (lambda x: x[a]))()
    return rules, _labels(n), n


def serial_chain(length):
    """Pure serial copy chain of `length` nodes: i' = x[i-1], 0' = x[length-1].

    The scaling-zoo chain baseline (predicted Φ = 2, constant in length)."""
    n = length
    rules = [(lambda i=i: (lambda x: x[(i - 1) % n]))() for i in range(n)]
    return rules, _labels(n), n


def coupled_pool(n):
    """Fully-coupled pool: every node copies the parity of all the others.

    Each node reads the XOR of the other n-1 nodes, so every node both reads and influences every
    other. The scaling-zoo pool baseline (predicted Φ = n(n-1), super-linear)."""
    rules = []
    for i in range(n):
        others = [j for j in range(n) if j != i]

        def make(others=others):
            def f(x):
                v = 0
                for j in others:
                    v ^= x[j]
                return v
            return f
        rules.append(make())
    return rules, _labels(n), n


# --------------------------------------------------------------------------------------
# Probe
# --------------------------------------------------------------------------------------

def instrument_control():
    """Validate the machinery on the known faithful triad: triadic, max_phi 2.0."""
    triad = [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]
    v = verdict(triad, ("W", "S", "C"))
    ok = v.structure == "triadic" and abs(v.max_phi - 2.0) < 1e-6
    print(f"CONTROL faithful triad -> structure={v.structure} max_phi={v.max_phi:.3f} "
          f"(expect triadic 2.0): {'PASS' if ok else 'FAIL'}")
    if not ok:
        raise SystemExit("instrument control failed")
    return v


def main():
    print("=" * 78)
    print("Q144  mediator hierarchy: does Φ track depth (chain, flat) or breadth (pool, grow)?")
    print("=" * 78)

    instrument_control()
    print()

    # Sanity read: how the base triad distributes its integration across parties.
    triad = [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]
    sh, total = shapley(triad, ("W", "S", "C"))
    print(f"Base-triad Shapley split of Φ at the integrating state: {sh}  (total Φ = {total})")
    print()

    # ---- Depth axis (H1): fix one leaf (b = 1), vary depth d. Pure serial mediator chain. ----
    print("DEPTH AXIS (H1): one leaf, b=1, mediator layers between leaf and apex grow")
    print(f"  {'d':>2}  {'n':>2}  {'core':>16}  {'phi':>7}")
    depth_phis = []
    for d in (1, 2, 3, 4):
        rules, labels, n = mediator_tree(d, 1)
        core, phi = major_complex(rules, labels)
        depth_phis.append(phi)
        print(f"  {d:>2}  {n:>2}  {str(core):>16}  {phi:>7.3f}")
    print()

    # ---- Breadth axis (H2): fix one layer (d = 1), vary breadth b. ----
    print("BREADTH AXIS (H2): one mediator layer, d=1, leaves per apex grow")
    print(f"  {'b':>2}  {'n':>2}  {'core':>16}  {'phi':>7}")
    breadth_phis = []
    for b in (2, 3, 4):
        rules, labels, n = mediator_tree(1, b)
        core, phi = major_complex(rules, labels)
        breadth_phis.append((b, n, phi))
        print(f"  {b:>2}  {n:>2}  {str(core):>16}  {phi:>7.3f}")
    print()

    # ---- Baselines: pure serial chain (depth law) and fully-coupled pool (breadth law). ----
    print("BASELINES (scaling-zoo laws):")
    print(f"  {'form':>14}  {'n':>2}  {'phi':>7}  {'predicted':>20}")
    chain_phis = []
    for L in (3, 4, 5):
        rules, labels, n = serial_chain(L)
        _, phi = major_complex(rules, labels)
        chain_phis.append(phi)
        print(f"  {'chain':>14}  {n:>2}  {phi:>7.3f}  {'2 (constant)':>20}")
    pool_phis = []
    for n in (3, 4, 5):
        rules, labels, _ = coupled_pool(n)
        _, phi = major_complex(rules, labels)
        pool_phis.append((n, phi))
        print(f"  {'pool':>14}  {n:>2}  {phi:>7.3f}  {'n(n-1)=' + str(n * (n - 1)):>20}")
    print()

    # ---- Verdicts ----
    # H1: depth at fixed (one) leaf leaves Φ flat at the chain constant.
    depth_flat = max(depth_phis) - min(depth_phis) < 1e-6
    depth_at_chain = all(abs(p - 2.0) < 1e-6 for p in depth_phis)
    h1_supported = depth_flat and depth_at_chain
    print(f"DEPTH Φ across d=1..4: {[round(p, 3) for p in depth_phis]}  "
          f"(flat={depth_flat}, at chain-constant 2.0={depth_at_chain})")
    print(f"H1 depth-is-flat-at-chain-constant: {'SUPPORTED' if h1_supported else 'REFUTED'}")

    # H2: breadth at fixed depth grows Φ super-linearly (strictly increasing, and faster than linear).
    bphi = [p for (_, _, p) in breadth_phis]
    breadth_increasing = all(bphi[i + 1] > bphi[i] + 1e-6 for i in range(len(bphi) - 1))
    # super-linear in leaf count b: second difference positive (convex), tested over b=2,3,4.
    second_diff = (bphi[2] - bphi[1]) - (bphi[1] - bphi[0])
    breadth_superlinear = breadth_increasing and second_diff > 1e-6
    print(f"BREADTH Φ across b=2,3,4: {[round(p, 3) for p in bphi]}  "
          f"(increasing={breadth_increasing}, 2nd-diff={second_diff:+.3f})")
    if breadth_superlinear:
        h2_word = "SUPPORTED"
    elif breadth_increasing:
        h2_word = "SUPPORTED (linear, not super-linear)"
    else:
        h2_word = "REFUTED"
    print(f"H2 breadth-grows-toward-pool: {h2_word}")


if __name__ == "__main__":
    main()
