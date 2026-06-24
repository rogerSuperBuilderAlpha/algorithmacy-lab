"""Probe 305 (Q151) — hub-failure resilience: does redundant mediation keep the triadic verdict when the
spanning hub is ablated?

Question: a single hub that gates every party binds them into one triadic complex. Ablate that hub (freeze
its rule to a constant) and the mediation it supplied is gone. Does a topology with redundant mediation — a
backup hub, or a ring of non-hub nodes — keep a triadic verdict where the single hub collapses to dyadic,
and does the Φ retained after ablation track the cycle redundancy that survives the hub?

H1 (fixed before computing): a single-hub topology collapses to dyadic when its hub is ablated, while a
    two-hub (backup) or ring-backed topology of the same n retains a triadic verdict, so redundant mediation
    buys verdict resilience. Null: hub ablation leaves the single-hub verdict triadic, or collapses the
    redundant ones equally.
H2 (fixed before computing): the post-ablation Φ retained scales with the number of independent cycles the
    topology has through non-hub nodes, identifying cycle redundancy as the resilience reserve. Null:
    retained Φ is independent of non-hub cycle count.

Method: build three n = 6 topologies, each with a designated spanning hub at node 0:
    - single_hub: hub = AND of all five parties; every party reads the hub. No non-hub cycle.
    - two_hub_backup: two independent spanning hubs (each = AND of all parties); every party reads
      (hub0 OR hub1). The second hub is a backup that does not depend on the first. No non-hub cycle.
    - ring_hub: the five non-hub nodes form a directed copy-ring (each reads its predecessor); the hub
      reads two opposite ring nodes and so observes the whole ring without the ring reading it back. One
      independent cycle runs through the non-hub ring.
    Ablate node 0 by replacing its rule with the constant 0 (the hub fires for nothing). For each topology
    read the major complex and its Φ before and after ablation; the verdict is triadic iff the major-complex
    Φ exceeds eps, matching the classifier (irreducible at its best reachable state). Control = the unablated
    form of each topology, which must read triadic. Count non-hub cycles as the cyclomatic number of the
    subgraph induced by the non-hub nodes.

Determinism: numpy is seeded with 0 and the Φ library seeds its state search with
    numpy.random.default_rng(0), so re-runs reproduce exactly.

Validation gap: exact IIT-4.0 Φ on small Boolean networks. The hubs, rings, and "ablation" are synthetic
    coordination forms, not measured organizations. "Hub", "backup", "resilience", and "cycle reserve" name
    graph-and-Φ quantities, not field constructs. In-silico scope; the Φ-to-organization bridge is open. The
    empirical reading is a baseline on synthetic data.

Run:  python -m org_frontier.questions.q151_hub_failure_resilience.probe_hub_failure_resilience
"""

import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

import numpy as np
import pyphi

from org_frontier.probes.lib import verdict, major_complex
from org_frontier.classifier.classifier import cm_from_rules

# Deterministic: fix every RNG seed used downstream.
SEED = 0
np.random.seed(SEED)
pyphi.config.PROGRESS_BARS = False
pyphi.config.PARALLEL = False

EPS = 1e-6
N = 6


# --------------------------------------------------------------------------------------
# Topologies (n = 6). Node 0 is the designated spanning hub in every form.
# --------------------------------------------------------------------------------------

def single_hub(n=N):
    """One spanning hub: node 0 = AND of all parties; every party reads the hub."""
    parties = list(range(1, n))
    rules = [None] * n
    rules[0] = lambda x: int(all(x[i] for i in parties))
    for i in parties:
        rules[i] = (lambda x, i=i: x[0])
    labels = tuple(["H"] + ["p%d" % i for i in parties])
    hubs = (0,)
    return rules, labels, hubs


def two_hub_backup(n=N):
    """Two independent spanning hubs: nodes 0 and 1 each = AND of all parties; every party reads
    (hub0 OR hub1). Hub 1 is a backup that does not depend on hub 0."""
    parties = list(range(2, n))
    rules = [None] * n
    rules[0] = lambda x: int(all(x[i] for i in parties))
    rules[1] = lambda x: int(all(x[i] for i in parties))
    for i in parties:
        rules[i] = (lambda x, i=i: int(x[0] or x[1]))
    labels = tuple(["H", "H2"] + ["p%d" % i for i in parties])
    hubs = (0, 1)
    return rules, labels, hubs


def ring_hub(n=N):
    """A directed copy-ring of the n-1 non-hub nodes (each reads its predecessor) plus a spanning hub
    (node 0) that reads two opposite ring nodes. The ring is one cycle through non-hub nodes; the hub
    observes the whole ring but the ring does not read the hub, so freezing the hub leaves the cycle
    intact."""
    m = n - 1  # ring length
    rules = [None] * n
    rules[0] = lambda x: int(x[1] and x[1 + m // 2])
    for k in range(m):
        i = 1 + k
        pred = 1 + (k - 1) % m
        rules[i] = (lambda x, pred=pred: x[pred])
    labels = tuple(["H"] + ["r%d" % k for k in range(m)])
    hubs = (0,)
    return rules, labels, hubs


TOPOS = {"single_hub": single_hub, "two_hub_backup": two_hub_backup, "ring_hub": ring_hub}


def ablate_hub(rules, hub=0):
    """Replace the hub's rule with the constant 0 (the hub fires for nothing)."""
    r = list(rules)
    r[hub] = (lambda x: 0)
    return r


def nonhub_cycles(rules, hubs):
    """Independent cycles through non-hub nodes: cyclomatic number (E - V + C) of the undirected
    subgraph induced by the non-hub nodes of the connectivity matrix."""
    cm = cm_from_rules(rules)
    n = cm.shape[0]
    nh = [i for i in range(n) if i not in hubs]
    edges, deg = set(), set()
    for i in nh:
        for j in nh:
            if cm[i, j]:
                a, b = (i, j) if i < j else (j, i)
                edges.add((a, b))
                deg.add(i)
                deg.add(j)
    if not deg:
        return 0
    parent = {x: x for x in deg}

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for a, b in edges:
        parent[find(a)] = find(b)
    comps = len({find(x) for x in deg})
    return len(edges) - len(deg) + comps


def mc_phi(rules, labels):
    """Major-complex Φ over reachable states; the structural verdict is triadic iff Φ > EPS.
    A form with no irreducible complex returns Φ = 0.0 (read as dyadic)."""
    core, phi = major_complex(rules, labels)
    if core is None or phi < 0:
        return 0.0, None
    return float(phi), core


def structure_of(phi):
    return "triadic" if phi > EPS else "dyadic"


# --------------------------------------------------------------------------------------
# Instrument control
# --------------------------------------------------------------------------------------

def control():
    """INSTRUMENT CONTROL: the faithful triad reads 'triadic' with max_phi 2.0 and a spanning core."""
    rules = [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]
    labels = ("W", "S", "C")
    v = verdict(rules, labels)
    core, phi = major_complex(rules, labels)
    ok = (v.structure == "triadic" and abs(v.max_phi - 2.0) < 1e-6
          and set(core) == set(labels) and abs(phi - 2.0) < 1e-6)
    print("CONTROL faithful triad: structure=%s max_phi=%.3f core=%s phi=%.3f -> %s"
          % (v.structure, v.max_phi, core, phi, "PASS" if ok else "FAIL"), flush=True)
    if not ok:
        raise SystemExit("instrument control failed")


def main():
    control()
    print(flush=True)

    rows = []
    print("Hub ablation at n=%d (ablate = freeze the node-0 hub to constant 0)" % N, flush=True)
    print("%-16s %-10s %-9s %-9s %-9s %-9s %s"
          % ("topology", "nonhub_cyc", "Φ_intact", "verdict", "Φ_ablate", "verdict", "Φ_retained"),
          flush=True)
    for name in ("single_hub", "two_hub_backup", "ring_hub"):
        rules, labels, hubs = TOPOS[name]()
        cyc = nonhub_cycles(rules, hubs)
        phi0, core0 = mc_phi(rules, labels)
        phi1, core1 = mc_phi(ablate_hub(rules), labels)
        retained = phi1  # Φ that survives ablation
        rows.append(dict(name=name, cyc=cyc, phi0=phi0, phi1=phi1, retained=retained,
                         v0=structure_of(phi0), v1=structure_of(phi1), core0=core0, core1=core1))
        print("%-16s %-10d %-9.3f %-9s %-9.3f %-9s %.3f"
              % (name, cyc, phi0, structure_of(phi0), phi1, structure_of(phi1), retained), flush=True)

    print(flush=True)
    print("Cores (intact -> ablated):", flush=True)
    for r in rows:
        print("  %-16s %s -> %s" % (r["name"], r["core0"], r["core1"]), flush=True)

    print(flush=True)

    # All controls (unablated forms) must read triadic, or the resilience contrast is undefined.
    all_intact_triadic = all(r["v0"] == "triadic" for r in rows)
    print("Control: every unablated topology reads triadic? %s"
          % ("yes" if all_intact_triadic else "no"), flush=True)
    print(flush=True)

    # ---- H1: single hub collapses to dyadic; redundant forms retain triadic ----
    single = next(r for r in rows if r["name"] == "single_hub")
    redundant = [r for r in rows if r["name"] != "single_hub"]
    single_collapses = single["v1"] == "dyadic"
    redundant_retain = [r["v1"] == "triadic" for r in redundant]
    any_redundant_retains = any(redundant_retain)
    all_redundant_retain = all(redundant_retain)

    if all_intact_triadic and single_collapses and any_redundant_retains:
        h1 = "SUPPORTED"
        held = ", ".join(r["name"] for r, k in zip(redundant, redundant_retain) if k)
        lost = ", ".join(r["name"] for r, k in zip(redundant, redundant_retain) if not k)
        h1_msg = ("the single hub collapses to dyadic on ablation while %s retains triadic"
                  % held)
        if lost:
            h1_msg += ("; %s also collapses, so redundancy buys resilience only for some forms" % lost)
        else:
            h1_msg += ", so every redundant form keeps the verdict the single hub loses"
    else:
        h1 = "REFUTED"
        if not single_collapses:
            h1_msg = ("the single hub does not collapse on ablation (verdict stays %s), so the contrast "
                      "the hypothesis rests on is absent" % single["v1"])
        elif not any_redundant_retains:
            h1_msg = ("the single hub collapses but every redundant form collapses too, so redundant "
                      "mediation as built here does not buy verdict resilience")
        else:
            h1_msg = "the intact controls do not all read triadic, so the resilience contrast is undefined"
    print("H1 (redundant mediation buys verdict resilience): %s" % h1, flush=True)
    print("    %s" % h1_msg, flush=True)
    print("    ablated verdicts: %s" % {r["name"]: r["v1"] for r in rows}, flush=True)

    print(flush=True)

    # ---- H2: retained Φ scales with non-hub cycle count, identifying the cycle as THE reserve ----
    # The claim is that the non-hub cycle is what holds Φ after ablation. The decisive test is whether the
    # cycle is necessary: a form with zero non-hub cycles must retain ~0. If a zero-cycle form retains
    # substantial Φ, the reserve is something else (here a backup hub) and the cycle account fails, even if
    # retained Φ happens to rise with cycle count. So H2 needs both monotonicity AND that every zero-cycle
    # form retains ~0.
    cyc_vals = [r["cyc"] for r in rows]
    varies = len(set(cyc_vals)) > 1
    by_cyc = sorted(rows, key=lambda r: r["cyc"])
    ret_vals = [r["retained"] for r in by_cyc]
    monotone = all(ret_vals[i] <= ret_vals[i + 1] + EPS for i in range(len(ret_vals) - 1))
    zero_cyc_retained = [r["retained"] for r in rows if r["cyc"] == 0]
    cycle_necessary = all(v <= EPS for v in zero_cyc_retained)  # no retention without a non-hub cycle

    if varies and monotone and cycle_necessary:
        h2 = "CONFIRMED"
        h2_msg = ("retained Φ rises with non-hub cycle count and every zero-cycle form retains ~0, so the "
                  "non-hub cycle is necessary for retention and is the resilience reserve")
    else:
        h2 = "NOT SUPPORTED"
        if not varies:
            h2_msg = "non-hub cycle count does not vary across the forms, so the scaling cannot be read"
        elif not cycle_necessary:
            offenders = ["%s (cyc=0, retained=%.3f)" % (r["name"], r["retained"])
                         for r in rows if r["cyc"] == 0 and r["retained"] > EPS]
            h2_msg = ("a form with no non-hub cycle still retains substantial Φ (%s), so the non-hub cycle is "
                      "not necessary for retention: the reserve is the backup mediator, not the cycle, and the "
                      "cycle-count account does not hold" % "; ".join(offenders))
        else:
            h2_msg = "retained Φ is not monotone in non-hub cycle count"
    print("H2 (retained Φ scales with non-hub cycle count): %s" % h2, flush=True)
    print("    %s" % h2_msg, flush=True)
    print("    (non-hub cycles, retained Φ) by form: %s"
          % {r["name"]: (r["cyc"], round(r["retained"], 3)) for r in rows}, flush=True)


if __name__ == "__main__":
    main()
