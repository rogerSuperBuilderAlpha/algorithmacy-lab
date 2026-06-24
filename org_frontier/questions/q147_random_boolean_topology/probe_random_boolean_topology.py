"""q147 — Which graph statistic predicts a triadic verdict and the size of Φ.

QUESTION
    Across an ensemble of random Boolean networks, which graph statistic of the
    dependency graph (mean degree, clustering, diameter, short-cycle density) best
    predicts whether the whole-system verdict is triadic, and how large Φ is?

H1  Triadicity probability rises with short-cycle (recurrence) density and falls with
    diameter, so recurrence-bearing topology predicts triadic verdicts better than mean
    degree alone. Null: no graph statistic separates triadic from dyadic ensembles above
    chance.

H2  Among triadic ensembles, Φ increases with the mean in-degree of the maximal-complex
    nodes, identifying high-degree nodes as the integration carriers. Null: Φ is
    uncorrelated with the core nodes' in-degree.

METHOD
    Sample random per-node Boolean rule sets at n=4 and n=5. Read each network's actual
    dependency graph with cm_from_rules (a flip-test, so a rule that ignores an input adds
    no edge). From the directed connectivity matrix compute mean degree, undirected
    clustering, undirected diameter, and short-cycle density (directed cycles of length <=3
    from traces of powers of the adjacency). Run verdict() for the triadic/dyadic call and
    max Φ, and major_complex() for the maximal-complex core. Separate the verdict with each
    statistic by point-biserial correlation; rank the statistics. Among triadic samples,
    correlate Φ against the core's mean in-degree. The control is a structured ring and a
    structured hub with hand-computable statistics.

    All sampling is seeded (numpy default_rng(0)); the run reproduces byte-identically.

RUN
    source /tmp/rvenv/bin/activate && export PYPHI_WELCOME_OFF=yes && \
    python -m org_frontier.questions.q147_random_boolean_topology.probe_random_boolean_topology

SCOPE
    Synthetic Boolean networks, exact IIT-4.0 Φ at n<=5. No field data. The graph-statistic
    results describe this in-silico ensemble. The Φ-to-organizational-value bridge is open.
"""

import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

import numpy as np

from org_frontier.probes.lib import verdict, major_complex
from org_frontier.classifier.classifier import cm_from_rules

LABELS = "ABCDE"


# ----------------------------------------------------------------------------------------
# Graph statistics of the directed dependency graph cm (cm[i, j] = 1 iff j depends on i)
# ----------------------------------------------------------------------------------------

def mean_degree(cm):
    """Mean total degree (in + out) over nodes of the directed dependency graph."""
    n = cm.shape[0]
    return float((cm.sum(axis=0) + cm.sum(axis=1)).mean()) if n else 0.0


def clustering(cm):
    """Average undirected clustering coefficient over the symmetrized graph.

    Symmetrize (an edge in either direction connects two nodes), then for each node count
    the fraction of its neighbour pairs that are themselves connected."""
    n = cm.shape[0]
    a = ((cm + cm.T) > 0).astype(int)
    np.fill_diagonal(a, 0)
    coeffs = []
    for v in range(n):
        nbrs = np.where(a[v] > 0)[0]
        k = len(nbrs)
        if k < 2:
            coeffs.append(0.0)
            continue
        sub = a[np.ix_(nbrs, nbrs)]
        links = sub.sum() / 2.0
        coeffs.append(links / (k * (k - 1) / 2.0))
    return float(np.mean(coeffs)) if coeffs else 0.0


def diameter(cm):
    """Undirected diameter: longest shortest path over the symmetrized graph.

    Disconnected graphs return n (a finite sentinel one above the largest possible finite
    diameter n-1), so a fragmented graph reads as maximally far apart."""
    n = cm.shape[0]
    a = ((cm + cm.T) > 0).astype(int)
    np.fill_diagonal(a, 0)
    INF = n + 1
    dist = np.full((n, n), INF, dtype=float)
    for v in range(n):
        dist[v, v] = 0.0
    rows, cols = np.where(a > 0)
    for i, j in zip(rows, cols):
        dist[i, j] = 1.0
    for k in range(n):  # Floyd-Warshall
        dist = np.minimum(dist, dist[:, k][:, None] + dist[k, :][None, :])
    offdiag = dist[~np.eye(n, dtype=bool)]
    if np.any(offdiag >= INF):
        return float(n)
    return float(offdiag.max()) if offdiag.size else 0.0


def cycle_density(cm):
    """Short-cycle (recurrence) density: directed closed walks of length 1..3 per node.

    trace(A^L) counts directed closed walks of length L. Summing L=1 (self-loops),
    L=2 (mutual edges), L=3 (directed triangles) and dividing by n gives a per-node
    recurrence count, the topological substrate for feedback."""
    n = cm.shape[0]
    a = cm.astype(int)
    a2 = a @ a
    a3 = a2 @ a
    walks = np.trace(a) + np.trace(a2) + np.trace(a3)
    return float(walks) / n if n else 0.0


def core_mean_indegree(cm, core_idx):
    """Mean in-degree (number of dependencies) of the nodes in the maximal complex."""
    if not core_idx:
        return 0.0
    indeg = cm.sum(axis=0)  # column sums = in-degree
    return float(np.mean([indeg[i] for i in core_idx]))


# ----------------------------------------------------------------------------------------
# Statistics helpers (point-biserial correlation = Pearson with a 0/1 variable)
# ----------------------------------------------------------------------------------------

def pearson(x, y):
    """Pearson r and a normal-approximation two-sided p-value. Returns (r, p)."""
    x = np.asarray(x, float)
    y = np.asarray(y, float)
    n = len(x)
    if n < 3 or x.std() < 1e-12 or y.std() < 1e-12:
        return 0.0, 1.0
    r = float(np.corrcoef(x, y)[0, 1])
    r = max(min(r, 1.0 - 1e-12), -1.0 + 1e-12)
    # Fisher z normal approximation for a deterministic, dependency-free p-value.
    z = np.arctanh(r) * np.sqrt(n - 3)
    from math import erfc, sqrt
    p = erfc(abs(z) / sqrt(2.0))
    return r, float(p)


# ----------------------------------------------------------------------------------------
# Random Boolean networks
# ----------------------------------------------------------------------------------------

def _make_rule(inputs, table):
    def rule(x):
        idx = 0
        for b, i in enumerate(inputs):
            idx |= (x[i] & 1) << b
        return int(table[idx])
    return rule


def random_rules(n, rng, kmax):
    """A random per-node Boolean rule set. Each node depends on 1..kmax random inputs
    through a random truth table over those inputs."""
    rules = []
    for _ in range(n):
        k = int(rng.integers(1, kmax + 1))
        inputs = sorted(rng.choice(n, size=k, replace=False).tolist())
        table = rng.integers(0, 2, size=2 ** k)
        rules.append(_make_rule(inputs, table))
    return rules


# ----------------------------------------------------------------------------------------
# Instrument control
# ----------------------------------------------------------------------------------------

def run_control():
    """Validate verdict/Φ on the faithful triad and the graph stats on hand-checked
    structured graphs (a directed 3-ring and a 4-node hub)."""
    rules = [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]
    v = verdict(rules, ("W", "S", "C"))
    assert v.structure == "triadic", v.structure
    assert abs(v.max_phi - 2.0) < 1e-6, v.max_phi

    # Directed 3-ring A->B->C->A: each node in-deg 1, out-deg 1; one directed 3-cycle.
    ring = np.array([[0, 1, 0], [0, 0, 1], [1, 0, 0]], dtype=int)
    assert abs(mean_degree(ring) - 2.0) < 1e-9, mean_degree(ring)
    # Symmetrized ring is the triangle: clustering 1.0, diameter 1.
    assert abs(clustering(ring) - 1.0) < 1e-9, clustering(ring)
    assert abs(diameter(ring) - 1.0) < 1e-9, diameter(ring)
    # One directed 3-cycle: trace(A^3)=3 (each node on one length-3 closed walk), /3 = 1.0.
    assert abs(cycle_density(ring) - 1.0) < 1e-9, cycle_density(ring)

    # Hub: node 0 feeds 1,2,3 (no back edges). No cycles; star diameter 2.
    hub = np.zeros((4, 4), dtype=int)
    hub[0, 1] = hub[0, 2] = hub[0, 3] = 1
    assert abs(cycle_density(hub) - 0.0) < 1e-9, cycle_density(hub)
    assert abs(diameter(hub) - 2.0) < 1e-9, diameter(hub)
    assert abs(clustering(hub) - 0.0) < 1e-9, clustering(hub)

    print("CONTROL faithful triad triadic Φ=2.0; ring/hub graph stats match hand values: PASS")


# ----------------------------------------------------------------------------------------
# Main study
# ----------------------------------------------------------------------------------------

def run_study():
    rng = np.random.default_rng(0)
    sizes = [(4, 4, 120), (5, 4, 40)]  # (n, kmax, n_samples)

    records = []  # one dict per sampled network
    for n, kmax, nsamp in sizes:
        labels = tuple(LABELS[:n])
        for _ in range(nsamp):
            rules = random_rules(n, rng, kmax)
            cm = cm_from_rules(rules)
            v = verdict(rules, labels)
            triadic = 1 if v.structure == "triadic" else 0
            core_labels, phi = major_complex(rules, labels)
            core_idx = [labels.index(c) for c in core_labels] if core_labels else []
            records.append(dict(
                n=n,
                triadic=triadic,
                phi=float(v.max_phi),
                mc_phi=float(phi),
                mean_degree=mean_degree(cm),
                clustering=clustering(cm),
                diameter=diameter(cm),
                cycle_density=cycle_density(cm),
                core_indeg=core_mean_indegree(cm, core_idx),
            ))

    N = len(records)
    n_tri = sum(r["triadic"] for r in records)
    print(f"\nEnsemble: {N} random Boolean networks "
          f"(n=4 x120, n=5 x40); triadic {n_tri}, dyadic {N - n_tri}.\n")

    # ---- H1: which graph statistic separates triadic from dyadic ----
    y = [r["triadic"] for r in records]
    stats = ["mean_degree", "clustering", "diameter", "cycle_density"]
    h1 = {}
    print("H1  point-biserial correlation of each graph statistic with the triadic verdict")
    print(f"    {'statistic':<14}{'r vs triadic':>14}{'p':>12}")
    for s in stats:
        r, p = pearson([rec[s] for rec in records], y)
        h1[s] = (r, p)
        print(f"    {s:<14}{r:>14.3f}{p:>12.4f}")

    # Recurrence proxies = cycle_density (up) and diameter (down, expect negative r).
    cyc_r, cyc_p = h1["cycle_density"]
    dia_r, dia_p = h1["diameter"]
    deg_r, deg_p = h1["mean_degree"]
    # Best separator by absolute correlation.
    best_stat = max(stats, key=lambda s: abs(h1[s][0]))
    best_r = h1[best_stat][0]
    recurrence_beats_degree = max(abs(cyc_r), abs(dia_r)) > abs(deg_r)
    cyc_dir_ok = cyc_r > 0
    dia_dir_ok = dia_r < 0
    h1_supported = (
        recurrence_beats_degree
        and (cyc_dir_ok or dia_dir_ok)
        and min(cyc_p, dia_p) < 0.05
    )

    print(f"\n    best separator: {best_stat} (|r|={abs(best_r):.3f})")
    print(f"    cycle_density r={cyc_r:+.3f} (p={cyc_p:.4f}); "
          f"diameter r={dia_r:+.3f} (p={dia_p:.4f}); "
          f"mean_degree r={deg_r:+.3f} (p={deg_p:.4f})")
    print(f"    recurrence (cycle/diameter) beats mean degree: {recurrence_beats_degree}")

    # ---- H2: among triadic samples, Φ vs core in-degree ----
    tri = [r for r in records if r["triadic"]]
    print(f"\nH2  among {len(tri)} triadic networks: Φ vs mean in-degree of the core")
    if len(tri) >= 3:
        h2_r, h2_p = pearson([r["core_indeg"] for r in tri], [r["mc_phi"] for r in tri])
        print(f"    Pearson r(core in-degree, Φ_core) = {h2_r:+.3f}  (p={h2_p:.4f})")
        h2_supported = (h2_r > 0) and (h2_p < 0.05)
    else:
        h2_r, h2_p = 0.0, 1.0
        h2_supported = False
        print("    too few triadic samples for a correlation")

    # ---- compact summary table ----
    print("\nSummary (mean statistic by verdict):")
    print(f"    {'group':<10}{'mean_deg':>10}{'cluster':>10}{'diam':>8}"
          f"{'cyc_dens':>10}{'core_indeg':>12}{'Φ_core':>9}")
    for name, grp in [("dyadic", [r for r in records if not r["triadic"]]),
                      ("triadic", tri)]:
        if not grp:
            continue
        print(f"    {name:<10}"
              f"{np.mean([r['mean_degree'] for r in grp]):>10.2f}"
              f"{np.mean([r['clustering'] for r in grp]):>10.3f}"
              f"{np.mean([r['diameter'] for r in grp]):>8.2f}"
              f"{np.mean([r['cycle_density'] for r in grp]):>10.2f}"
              f"{np.mean([r['core_indeg'] for r in grp]):>12.2f}"
              f"{np.mean([r['mc_phi'] for r in grp]):>9.3f}")

    # ---- verdicts ----
    print()
    print("H1 (recurrence topology beats mean degree at predicting triadicity): "
          + ("SUPPORTED" if h1_supported else "REFUTED"))
    print("H2 (among triadic nets, Φ rises with core in-degree): "
          + ("SUPPORTED" if h2_supported else "REFUTED"))
    return h1_supported, h2_supported


def main():
    run_control()
    run_study()


if __name__ == "__main__":
    main()
