"""Probe 314 (Q160) — does coupling-centrality recovery of major-complex membership hold at five
parties, where deep_pool_all's structural core excludes the worker, or does the dissociation widen
with scale?

Question: at four nodes, coupling centrality (each node's summed prominent behavioral coupling)
ranks every major-complex member above every excluded spectator in 36% of random forms. Five nodes
add a party. deep_pool_all is the worked five-node case whose irreducible core {S1,S2,C1,C2}
excludes the worker. The question is whether full-separation recovery at five nodes stays at the
four-node rate or falls, and whether the worker that structure excludes from deep_pool_all is
nonetheless among the top-coupled nodes behaviorally (a relay-style false positive).

H1 (fixed before computing): on five-node forms, coupling centrality fully separates the major
    complex from the excluded spectators in a fraction LOWER than the four-node 36% rate, so the
    dissociation widens with scale. Null: the five-node full-separation fraction matches the
    four-node rate, so scale does not widen the dissociation.
H2 (fixed before computing): the worker excluded from deep_pool_all's core is nonetheless among the
    top-coupled nodes behaviorally, a reproducible relay-style false positive (worker out-couples at
    least one core member in a majority of seeded runs). Null: the excluded worker ranks below core
    members in coupling centrality, so behavior agrees with the structural exclusion.

Method: structural ground truth is the major complex from complex_over_states (max-Φ maximal complex
    over reachable states). Behavioral ranking is coupling_centrality from a sampled trajectory.
    Forms: the named five-node forms in org_frontier.multiparty.forms (deep_pool_all and peers) plus
    inline five-node peers that place the excluded party at different indices, and a rand_form5
    ensemble of N_ENS draws. A form fully separates when every core member out-couples every
    non-member (the bridge_four `separates` predicate). The control baseline is the published
    four-node full-separation rate, 36% (org_frontier/recurrence/BRIDGE_FOUR.md). H2 is read on
    deep_pool_all across H2_SEEDS trajectories: the worker (node 0) coupling rank and how often it
    out-couples the weakest core member.

Determinism: every trajectory uses random.Random(seed) with a fixed seed; the Φ library seeds its
    reachable-state search internally. numpy.random.default_rng(0) is set once. Re-runs reproduce
    byte for byte.

Validation gap: exact IIT-4.0 Φ on small Boolean coordination forms. "worker", "spectator", "core",
    "relay", and "coupling centrality" name graph-and-Φ quantities, not measured organizations.
    In-silico scope; the Φ-to-organization bridge is open. The empirical arm (CRQA coupling
    centrality) runs on synthetic trajectories, so every separation fraction is a baseline on
    synthetic data.

Run:  python -m org_frontier.questions.q160_five_node_complex_recovery.probe_five_node_complex_recovery
"""

import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

import random

import numpy as np
import pyphi

from org_frontier.recurrence.crqa import trajectory, coupling_centrality
from org_frontier.recurrence.bridge_four import major_complex, separates, rand_form5
from org_frontier.multiparty import forms as mp

# Deterministic.
np.random.seed(0)
np.random.default_rng(0)
pyphi.config.PROGRESS_BARS = False
pyphi.config.PARALLEL = False

STEPS = 600
FLIP = 0.08
SEED = 5             # the named-form trajectory seed (matches bridge_four)
N_ENS = 40           # rand_form5 ensemble size
ENS_SEED = 1         # form-draw seed for the ensemble
ENS_TRAJ_BASE = 7000
H2_SEEDS = 20        # deep_pool_all worker-rank seeds
FOUR_NODE_RATE = 0.36  # published four-node full-separation rate (BRIDGE_FOUR.md)


# --------------------------------------------------------------------------------------
# Five-node peer forms beyond the named multiparty set, placing the excluded party at
# different indices so a separation is not a positional artifact.
# --------------------------------------------------------------------------------------

PEER_FORMS = {
    # A clean relay chain W -> S1 -> S2 -> S3 -> C. Each node copies its predecessor's prior state.
    # The ends are tightly coupled to their neighbor only; the core (if any) sits in the interior.
    "relay_chain5": (
        [lambda x: x[0], lambda x: x[0], lambda x: x[1], lambda x: x[2], lambda x: x[3]],
        ("W", "S1", "S2", "S3", "C"),
    ),
    # A hub (node 2) joining two parties on each side; both sides must clear the hub jointly.
    "central_hub5": (
        [lambda x: x[2], lambda x: x[2], lambda x: (x[0] & x[1]) & (x[3] & x[4]),
         lambda x: x[2], lambda x: x[2]],
        ("A", "B", "H", "C", "D"),
    ),
    # Pooled match requiring the worker AND both counterparts, with a decoupled spectator (node 4).
    # The spectator is a self-loop outside the coordination, so the core should exclude it.
    "pool_with_spectator5": (
        [lambda x: x[1], lambda x: x[0] & x[2] & x[3], lambda x: x[1], lambda x: x[1],
         lambda x: x[4]],
        ("W", "S", "C1", "C2", "X"),
    ),
}


def named_five_node_forms():
    """The named multiparty five-node forms plus the inline peers, as (name, rules, labels)."""
    out = []
    for f in mp.FORMS:
        if len(f.rules) == 5:
            out.append((f.key, f.rules, f.labels))
    for name, (rules, labels) in PEER_FORMS.items():
        out.append((name, rules, labels))
    return out


# --------------------------------------------------------------------------------------
# Instrument control
# --------------------------------------------------------------------------------------

def control():
    """INSTRUMENT CONTROL: the faithful triad [x1, x0&x2, x1] reads major complex {W,S,C} with
    Φ = 2.0, and on a sampled trajectory the mediator S (node 1) out-couples both endpoints, so
    coupling centrality fully separates the (full-system) core from no excluded node — the
    `separates` predicate returns None when the core is everyone, which is the documented behavior.
    The control validates that major_complex reads Φ=2.0 'triadic' and that coupling_centrality
    ranks S top."""
    rules = [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]
    labels = ("W", "S", "C")
    core, phi = major_complex(rules, 3)
    core = sorted(core)
    traj = trajectory(rules, STEPS, random.Random(0), flip=0.05)
    cen = coupling_centrality(traj)
    s_top = int(np.argmax(cen)) == 1
    ok = (core == [0, 1, 2] and abs(phi - 2.0) < 1e-6 and s_top)
    print("CONTROL faithful triad: core=%s phi=%.3f S_top_coupled=%s -> %s"
          % ([labels[i] for i in core], phi, s_top, "PASS" if ok else "FAIL"), flush=True)
    if not ok:
        raise SystemExit("instrument control failed")


# --------------------------------------------------------------------------------------
# Main
# --------------------------------------------------------------------------------------

def run_named():
    """Full-separation over the named five-node forms. Returns (hits, total) over forms whose core
    is a strict, non-empty subset (where separation is a real test)."""
    print("Named five-node forms: major complex vs coupling-centrality separation (seed %d)" % SEED,
          flush=True)
    print("%-22s %-6s %-14s %-7s %s" % ("form", "Φ", "core", "split", "note"), flush=True)
    hits = total = 0
    for name, rules, labels in named_five_node_forms():
        core, phi = major_complex(rules, 5)
        core = sorted(core)
        traj = trajectory(rules, STEPS, random.Random(SEED), flip=FLIP)
        cen = coupling_centrality(traj)
        sep = separates(cen, core, 5)
        coremembers = "".join(labels[i] for i in core) or "-"
        if sep is None:
            note = "core is all/none (n/a)"
            split = "n/a"
        else:
            total += 1
            hits += int(sep)
            split = "yes" if sep else "no"
            note = "core out-couples rest" if sep else "mixed"
        print("%-22s %-6.2f %-14s %-7s %s"
              % (name, phi, coremembers, split, note), flush=True)
    print("  full separation on testable named forms: %d/%d" % (hits, total), flush=True)
    print(flush=True)
    return hits, total


def run_ensemble():
    """Full-separation over a rand_form5 ensemble. Returns (hits, total)."""
    print("Random five-node ensemble: %d draws (form seed %d), trajectory seeds %d.."
          % (N_ENS, ENS_SEED, ENS_TRAJ_BASE), flush=True)
    rng = random.Random(ENS_SEED)
    hits = total = 0
    for k in range(N_ENS):
        rules = rand_form5(rng)
        core, phi = major_complex(rules, 5)
        core = sorted(core)
        traj = trajectory(rules, STEPS, random.Random(ENS_TRAJ_BASE + k), flip=FLIP)
        cen = coupling_centrality(traj)
        sep = separates(cen, core, 5)
        if sep is not None:
            total += 1
            hits += int(sep)
    rate = hits / total if total else float("nan")
    print("  full separation: %d/%d testable forms = %.1f%%" % (hits, total, 100 * rate), flush=True)
    print(flush=True)
    return hits, total


def run_worker_h2():
    """H2: is the worker excluded from deep_pool_all's core among the top-coupled nodes?
    Returns (above_count, n_seeds, mean_rank, core)."""
    f = [x for x in mp.FORMS if x.key == "deep_pool_all"][0]
    core, phi = major_complex(f.rules, 5)
    core = sorted(core)
    worker = 0  # node 0 = W
    print("H2 — deep_pool_all worker (node W) coupling rank (Φ=%.2f, core=%s, excludes W)"
          % (phi, "".join(f.labels[i] for i in core)), flush=True)
    above = 0
    ranks = []
    for seed in range(H2_SEEDS):
        traj = trajectory(f.rules, STEPS, random.Random(seed), flip=FLIP)
        cen = coupling_centrality(traj)
        rank = int((cen > cen[worker]).sum())  # 0 = top, 4 = bottom (of 5)
        ranks.append(rank)
        if cen[worker] > min(cen[c] for c in core):
            above += 1
    mean_rank = float(np.mean(ranks))
    print("  worker out-couples the weakest core member in %d/%d seeds; mean worker rank %.2f "
          "(0=top of 5, 4=bottom)" % (above, H2_SEEDS, mean_rank), flush=True)
    print(flush=True)
    return above, H2_SEEDS, mean_rank, core


def main():
    control()
    print(flush=True)

    named_hits, named_total = run_named()
    ens_hits, ens_total = run_ensemble()

    # Pooled five-node full-separation fraction (named testable forms + ensemble).
    tot = named_total + ens_total
    hit = named_hits + ens_hits
    five_rate = hit / tot if tot else float("nan")
    print("Pooled five-node full-separation fraction (named + ensemble): %d/%d = %.1f%%"
          % (hit, tot, 100 * five_rate), flush=True)
    print("  four-node baseline (control, BRIDGE_FOUR.md): %.0f%%" % (100 * FOUR_NODE_RATE),
          flush=True)
    print(flush=True)

    above, n_seeds, mean_rank, core = run_worker_h2()

    # ---- Verdicts ------------------------------------------------------------------------------
    # H1: the five-node full-separation fraction is LOWER than the four-node 36% rate.
    h1_supported = five_rate < FOUR_NODE_RATE
    # H2: the excluded worker is among the top-coupled nodes (out-couples a core member in a
    # majority of seeds). REFUTED when it ranks below core members (behavior agrees with structure).
    h2_supported = above > n_seeds / 2

    print("H1 (five-node full-separation fraction is LOWER than the four-node 36%% rate, dissociation "
          "widens with scale): %s" % ("SUPPORTED" if h1_supported else "REFUTED"), flush=True)
    print("   five-node %.1f%% vs four-node %.0f%% (pooled %d/%d testable forms)"
          % (100 * five_rate, 100 * FOUR_NODE_RATE, hit, tot), flush=True)
    print("H2 (the excluded worker is nonetheless among the top-coupled nodes, a relay-style false "
          "positive): %s" % ("SUPPORTED" if h2_supported else "REFUTED"), flush=True)
    print("   worker out-couples the weakest core member in %d/%d seeds, mean rank %.2f of 5 — "
          "behavior %s the structural exclusion"
          % (above, n_seeds, mean_rank,
             "contradicts" if h2_supported else "agrees with"), flush=True)


if __name__ == "__main__":
    main()
