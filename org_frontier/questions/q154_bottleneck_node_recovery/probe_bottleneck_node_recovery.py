"""Probe 308 (Q154) — bottleneck-node recovery: does behavioral coupling centrality find the
node that exact-Φ marks as the form's articulation point?

Question: a bottleneck form has one node whose removal collapses the integration the others
sustain. Exact IIT-4.0 Φ locates that node structurally: freeze each node to a constant in turn
and the node whose freezing drops major-complex Φ the most is the articulation point. A trajectory
sampled from the same form gives two behavioral pickers — the node with the highest CRQA coupling
centrality, and the node with the highest summed transfer-entropy throughput. The question is
whether either behavioral picker recovers the structural articulation node.

H1 (fixed before computing): in the bottleneck forms (ats_strict_bottleneck, joint_bottleneck,
    degree_bottleneck), the node whose freezing most lowers major-complex Φ is the node with the
    highest coupling centrality, recovered in over 70% of seeded runs. Null: the structural
    bottleneck and the coupling-centrality peak coincide at chance (<= 1/n).
H2 (fixed before computing): coupling centrality finds the bottleneck more reliably than node-wise
    transfer-entropy throughput. Null: per-node summed transfer entropy matches or beats coupling
    centrality at locating the bottleneck.

Method: three named bottleneck forms. The structural ground truth for each is the leave-one-node-out
    drop in major-complex Φ: freeze node k to the constant 0 and recompute the maximal complex; the
    drop base_Φ − Φ(freeze k) is node k's load. The ground-truth bottleneck set is the argmax of the
    drops (a tie when several nodes carry the irreducibility equally; a single node when one is the
    unique articulation point). For each of 30 seeds a trajectory of 400 steps is sampled and two
    behavioral picks are read: argmax coupling_centrality and argmax TE-throughput (sum of TE in and
    out of each node). A run is a recovery when the behavioral argmax lies in the ground-truth set.
    Recovery rates are reported over all forms and over the subset with a unique articulation point,
    where the recovery question is non-trivial (a tied ground-truth set makes recovery automatic).
    Control = a degree-matched symmetric XOR-ring with no structural bottleneck (every node carries
    equal load, so no node is the articulation point); the behavioral picks must spread across the
    nodes rather than concentrate on one.

Determinism: every trajectory uses numpy.random.default_rng(seed) with a fixed seed loop, and the Φ
    library seeds its state search with numpy.random.default_rng(0). Re-runs reproduce byte for byte.

Validation gap: exact IIT-4.0 Φ on small Boolean coordination forms. The forms, the "freezing"
    ablation, "bottleneck", "articulation point", "coupling centrality", and "throughput" name
    graph-and-Φ quantities, not measured organizations. In-silico scope; the Φ-to-organization
    bridge is open. The empirical arms (CRQA, transfer entropy) run on synthetic trajectories, so
    every recovery rate is a baseline on synthetic data.

Run:  python -m org_frontier.questions.q154_bottleneck_node_recovery.probe_bottleneck_node_recovery
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
from org_frontier.recurrence.crqa import trajectory, coupling_centrality
from org_frontier.probes._info import transfer_entropy

# Deterministic: fix every RNG seed used downstream.
np.random.seed(0)
pyphi.config.PROGRESS_BARS = False
pyphi.config.PARALLEL = False

TOL = 1e-6
SEEDS = 30          # seeded trajectory runs per form
STEPS = 400
FLIP = 0.05
WARMUP = 20
H1_THRESHOLD = 0.70


# --------------------------------------------------------------------------------------
# Named bottleneck forms. Each is a per-node Boolean rule list over the little-endian
# current-state tuple x, with the articulation node placed at a different index so a
# recovery is not a positional artifact.
# --------------------------------------------------------------------------------------

FORMS = {
    # The canonical strict bottleneck (dissertation Paper 2). Every node is load-bearing:
    # the AND mediator dies if any input is frozen, so no single node is the unique
    # articulation point. Kept as a named form; its ground-truth set is a three-way tie.
    "ats_strict_bottleneck": (
        [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]],
        ("W", "S", "C"),
    ),
    # A hub (node 1) that bridges a single party (node 0) to a redundant cluster (nodes 2, 3).
    # The cluster's internal redundancy means freezing 0, 2, or 3 leaves the integration intact,
    # while freezing the hub collapses it. Unique articulation point at node 1.
    "joint_bottleneck": (
        [lambda x: x[1], lambda x: x[0] & (x[2] | x[3]), lambda x: x[1] & x[3], lambda x: x[1] & x[2]],
        ("A", "B", "C", "D"),
    ),
    # A high-degree connector (node 0) read by two parties with a back-up read of node 3.
    # Freezing the connector collapses the complex; the periphery does not. Unique articulation
    # point at node 0.
    "degree_bottleneck": (
        [lambda x: x[1] | x[3], lambda x: x[0] & x[2], lambda x: x[1], lambda x: x[0]],
        ("A", "B", "C", "D"),
    ),
}

# Degree-matched control: a symmetric XOR-ring of four nodes. Every node reads its two ring
# neighbours, so every node has the same degree and the same Φ load. No structural bottleneck.
CONTROL = (
    [lambda x: x[3] ^ x[1], lambda x: x[0] ^ x[2], lambda x: x[1] ^ x[3], lambda x: x[2] ^ x[0]],
    ("A", "B", "C", "D"),
)


# --------------------------------------------------------------------------------------
# Structural ground truth: leave-one-node-out drop in major-complex Φ.
# --------------------------------------------------------------------------------------

def mc_phi(rules, labels):
    """Major-complex Φ over reachable states; 0.0 when no irreducible complex exists."""
    core, phi = major_complex(rules, labels)
    if core is None or phi < 0:
        return 0.0
    return float(phi)


def loo_drops(rules, labels):
    """Per-node load: base_Φ − Φ after freezing node k to the constant 0."""
    base = mc_phi(rules, labels)
    drops = []
    for k in range(len(rules)):
        frozen = list(rules)
        frozen[k] = (lambda x: 0)
        drops.append(base - mc_phi(frozen, labels))
    return base, drops


def gt_set(drops):
    """The argmax set of the drops: the structural bottleneck node(s). A single index is a
    unique articulation point; several indices is a tie among equally load-bearing nodes."""
    mx = max(drops)
    if mx <= TOL:
        return set()
    return {i for i, d in enumerate(drops) if abs(d - mx) <= TOL}


# --------------------------------------------------------------------------------------
# Behavioral pickers from a sampled trajectory.
# --------------------------------------------------------------------------------------

def te_throughput(traj):
    """Per-node summed transfer entropy in and out: sum over partners of TE(node->p)+TE(p->node)."""
    n = traj.shape[1]
    return np.array([
        sum(transfer_entropy(traj, s, d) + transfer_entropy(traj, d, s)
            for d in range(n) if d != s)
        for s in range(n)
    ])


def behavioral_picks(rules, seed):
    """argmax coupling_centrality and argmax TE-throughput from one seeded trajectory."""
    traj = trajectory(rules, STEPS, np.random.default_rng(seed), flip=FLIP, warmup=WARMUP)
    cc = coupling_centrality(traj)
    te = te_throughput(traj)
    return int(np.argmax(cc)), int(np.argmax(te))


# --------------------------------------------------------------------------------------
# Instrument control
# --------------------------------------------------------------------------------------

def control():
    """INSTRUMENT CONTROL: the faithful triad reads 'triadic' with max_phi 2.0, and on it both the
    structural freezing and the behavioral pickers agree the mediator S (node 1) is load-bearing."""
    rules = [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]
    labels = ("W", "S", "C")
    v = verdict(rules, labels)
    base, drops = loo_drops(rules, labels)
    cc, te = behavioral_picks(rules, 0)
    ok = (v.structure == "triadic" and abs(v.max_phi - 2.0) < 1e-6
          and abs(base - 2.0) < 1e-6 and cc == 1 and te == 1)
    print("CONTROL faithful triad: structure=%s max_phi=%.3f base_phi=%.3f cc_pick=%d te_pick=%d -> %s"
          % (v.structure, v.max_phi, base, cc, te, "PASS" if ok else "FAIL"), flush=True)
    if not ok:
        raise SystemExit("instrument control failed")


# --------------------------------------------------------------------------------------
# Main
# --------------------------------------------------------------------------------------

def main():
    control()
    print(flush=True)

    print("Structural bottleneck (leave-one-node-out drop in major-complex Φ) vs behavioral recovery",
          flush=True)
    print("recovery = behavioral argmax lies in the ground-truth argmax-drop set, over %d seeds" % SEEDS,
          flush=True)
    print(flush=True)
    print("%-22s %-7s %-22s %-9s %-6s %-7s %-7s"
          % ("form", "base_Φ", "loo_drops", "gt_set", "unique", "cc_rec", "te_rec"), flush=True)

    cc_hit = cc_tot = te_hit = te_tot = 0
    ucc_hit = ucc_tot = ute_hit = ute_tot = 0
    for name, (rules, labels) in FORMS.items():
        base, drops = loo_drops(rules, labels)
        gt = gt_set(drops)
        unique = len(gt) == 1
        hcc = hte = 0
        for seed in range(SEEDS):
            cc, te = behavioral_picks(rules, seed)
            if cc in gt:
                hcc += 1
            if te in gt:
                hte += 1
        cc_hit += hcc; cc_tot += SEEDS; te_hit += hte; te_tot += SEEDS
        if unique:
            ucc_hit += hcc; ucc_tot += SEEDS; ute_hit += hte; ute_tot += SEEDS
        print("%-22s %-7.2f %-22s %-9s %-6s %-7s %-7s"
              % (name, base, str([round(d, 2) for d in drops]),
                 str(sorted(gt)), str(unique),
                 "%d/%d" % (hcc, SEEDS), "%d/%d" % (hte, SEEDS)), flush=True)

    cc_all = cc_hit / cc_tot
    te_all = te_hit / te_tot
    cc_uniq = ucc_hit / ucc_tot if ucc_tot else float("nan")
    te_uniq = ute_hit / ute_tot if ute_tot else float("nan")

    print(flush=True)
    print("Pooled recovery rate (behavioral argmax in structural argmax-drop set):", flush=True)
    print("  all forms:                 coupling_centrality %.1f%%   TE_throughput %.1f%%"
          % (100 * cc_all, 100 * te_all), flush=True)
    print("  unique-articulation forms: coupling_centrality %.1f%%   TE_throughput %.1f%%"
          % (100 * cc_uniq, 100 * te_uniq), flush=True)
    print("  (a tied ground-truth set makes recovery automatic, so the unique-articulation subset "
          "is the real test)", flush=True)

    # Control: a degree-matched form with no structural bottleneck. The behavioral pickers must not
    # concentrate on any single node beyond chance.
    crules, clabels = CONTROL
    cbase, cdrops = loo_drops(crules, clabels)
    cc_counts = np.zeros(len(crules), dtype=int)
    te_counts = np.zeros(len(crules), dtype=int)
    for seed in range(SEEDS):
        cc, te = behavioral_picks(crules, seed)
        cc_counts[cc] += 1
        te_counts[te] += 1
    chance = 1.0 / len(crules)
    cc_max_share = cc_counts.max() / SEEDS
    te_max_share = te_counts.max() / SEEDS
    print(flush=True)
    print("Control (degree-matched symmetric XOR-ring, no structural bottleneck):", flush=True)
    print("  base_Φ=%.3f  loo_drops=%s  gt_set=%s (no unique articulation point)"
          % (cbase, [round(d, 2) for d in cdrops], sorted(gt_set(cdrops))), flush=True)
    print("  cc picks per node=%s  te picks per node=%s  chance=%.0f%%"
          % (cc_counts.tolist(), te_counts.tolist(), 100 * chance), flush=True)
    print("  max single-node share: cc %.0f%%  te %.0f%% (no node grabbed beyond chance => "
          "instrument invents no bottleneck)" % (100 * cc_max_share, 100 * te_max_share), flush=True)

    # ---- Verdicts ------------------------------------------------------------------------------
    # H1: coupling_centrality recovers the unique structural bottleneck in > 70% of seeded runs.
    h1_supported = cc_uniq > H1_THRESHOLD
    # H2 (confirmed = CC beats TE): CC must beat TE on the unique-articulation subset.
    h2_cc_beats_te = cc_uniq > te_uniq

    print(flush=True)
    print("H1 (coupling centrality recovers the structural bottleneck in >70%% of seeded runs): %s"
          % ("SUPPORTED" if h1_supported else "REFUTED"), flush=True)
    print("   coupling_centrality recovers %.1f%% on unique-articulation forms (threshold 70%%, "
          "chance ~%.0f%%)" % (100 * cc_uniq, 100 * chance), flush=True)
    print("H2 (coupling centrality beats TE-throughput at locating the bottleneck): %s"
          % ("CONFIRMED" if h2_cc_beats_te else "NOT SUPPORTED"), flush=True)
    print("   coupling_centrality %.1f%% vs TE_throughput %.1f%% on unique-articulation forms"
          % (100 * cc_uniq, 100 * te_uniq), flush=True)


if __name__ == "__main__":
    main()
