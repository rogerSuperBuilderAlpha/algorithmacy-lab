"""Q146 — small-world rewiring and Φ: does integration peak at intermediate rewiring?

QUESTION
    Starting from a conjunctive ring and rewiring edges toward random shortcuts
    (Watts-Strogatz style), does whole-system Φ rise, fall, or hold as the rewiring
    probability p climbs from lattice (p=0) to random (p=1)?

H1  Φ is non-monotone in p with a small-world peak at intermediate p: a few shortcuts
    add integration before randomness destroys the balanced bottleneck, so mean max-Φ_MIP
    at some interior p exceeds both the pure ring (p=0) and the random graph (p=1).
    Null: Φ is monotone in p, with no interior peak.

H2  The verdict stays triadic across the whole rewiring sweep at fixed n=6 even as the
    core membership churns: topology shifts the major complex without flipping the
    dyadic/triadic verdict.
    Null: rewiring flips the verdict to dyadic at some p.

METHOD
    Build a conjunctive ring on n=6: each node's next state is the AND of its two ring
    neighbours' current states. Rewire endpoints Watts-Strogatz style — for each of a
    node's two input edges, with probability p replace the source with a uniformly random
    distinct source (in-degree of 2 preserved, no self-loops, no duplicate inputs). Sweep
    p in {0, 0.1, 0.25, 0.5, 1}. p=0 is the deterministic ring (one config, the lattice
    control); interior p and p=1 are averaged over a fixed seed sweep. For each network,
    read the whole-system verdict (structure, max Φ_MIP over reachable states) and the
    major complex (core membership, its Φ). p=1 random wiring is the disorder control.

    All randomness is seeded (numpy default_rng) so the run reproduces byte-for-byte.

    H1 verdict: SUPPORTED iff mean max-Φ_MIP at some interior p strictly exceeds both the
    p=0 ring value and the p=1 mean. H2 verdict: SUPPORTED iff every evaluated network is
    triadic (no p flips the verdict to dyadic).

    In-silico only: these are synthetic Boolean networks, not measured systems. No
    empirical organisation is wired here; the validation gap to real coordination data is
    open.

RUN
    source /tmp/rvenv/bin/activate && export PYPHI_WELCOME_OFF=yes && \
      python -m org_frontier.questions.q146_smallworld_rewire_phi.probe_smallworld_rewire_phi
"""

import os
import sys

import numpy as np

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.probes.lib import verdict, major_complex

N = 6
LABELS = tuple("N%d" % i for i in range(N))
P_VALUES = (0.0, 0.1, 0.25, 0.5, 1.0)
SEEDS = (0, 1, 2)          # seed sweep for stochastic p (interior and p=1)
BASE_SEED = 20260623       # offset so each (p, seed) draws an independent stream
EPS = 1e-9


def ring_inputs():
    """Conjunctive ring: node i reads its two ring neighbours (i-1, i+1) mod N."""
    return {i: [(i - 1) % N, (i + 1) % N] for i in range(N)}


def rewire(p, rng):
    """Watts-Strogatz endpoint rewiring with in-degree 2 preserved.

    For each input edge of each node, with probability p replace its source with a
    uniformly random source that is not the node itself and not already an input.
    Returns the per-node input lists.
    """
    ins = ring_inputs()
    for d in range(N):
        for k in range(len(ins[d])):
            if rng.random() < p:
                cur = set(ins[d])
                choices = [c for c in range(N) if c != d and c not in cur]
                if choices:
                    ins[d][k] = int(rng.choice(choices))
    return ins


def rules_from_inputs(ins):
    """Per-node Boolean rules: each node = AND of its (current) input sources."""
    def mk(srcs):
        srcs = tuple(srcs)

        def f(x, srcs=srcs):
            r = 1
            for s in srcs:
                r &= x[s]
            return r

        return f

    return [mk(ins[i]) for i in range(N)]


def evaluate(ins):
    """(structure, max_phi, core_tuple, core_phi) for one wiring."""
    rules = rules_from_inputs(ins)
    v = verdict(rules, LABELS)
    core, core_phi = major_complex(rules, LABELS)
    return v.structure, float(v.max_phi), core, float(core_phi)


def instrument_control():
    """Validate the machinery on the known faithful triad before the real sweep."""
    triad = [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]
    v = verdict(triad, ("W", "S", "C"))
    ok = (v.structure == "triadic") and (abs(v.max_phi - 2.0) < 1e-6)
    status = "PASS" if ok else "FAIL"
    print(
        "CONTROL faithful triad [x1, x0&x2, x1]: verdict=%s max_phi=%.6f "
        "(expect triadic / 2.0) ... %s" % (v.structure, v.max_phi, status)
    )
    if not ok:
        raise SystemExit("instrument control failed; aborting")


def main():
    print("PROBE Q146 — small-world rewiring and Φ (conjunctive ring, n=%d)" % N)
    print("=" * 78)
    instrument_control()
    print()

    # ------------------------------------------------------------------ sweep
    rows = []          # (p, seed, structure, max_phi, core_size, core_phi, core_str)
    per_p_phi = {}     # p -> list of max_phi
    all_triadic = True

    for p in P_VALUES:
        seeds = (0,) if p == 0.0 else SEEDS    # p=0 is deterministic: one config
        phis = []
        for seed in seeds:
            rng = np.random.default_rng(BASE_SEED + seed)
            ins = ring_inputs() if p == 0.0 else rewire(p, rng)
            structure, max_phi, core, core_phi = evaluate(ins)
            phis.append(max_phi)
            core_str = "{" + ",".join(core) + "}" if core else "(none)"
            rows.append((p, seed, structure, max_phi, len(core) if core else 0,
                         core_phi, core_str))
            if structure != "triadic":
                all_triadic = False
        per_p_phi[p] = phis

    # ------------------------------------------------------------------ table
    print("per-network results (Watts-Strogatz endpoint rewiring of a conjunctive ring):")
    print("-" * 78)
    print("    p   seed  verdict    maxΦ_MIP  core_size  core_Φ   core")
    for (p, seed, structure, max_phi, csize, core_phi, core_str) in rows:
        print("  %4.2f   %2d   %-8s  %8.4f   %4d      %7.4f  %s"
              % (p, seed, structure, max_phi, csize, core_phi, core_str))

    print()
    print("mean max-Φ_MIP by rewiring probability p:")
    print("-" * 78)
    print("     p    n_seeds   mean_maxΦ_MIP")
    means = {}
    for p in P_VALUES:
        phis = per_p_phi[p]
        m = float(np.mean(phis))
        means[p] = m
        print("  %5.2f     %2d        %10.4f" % (p, len(phis), m))

    # ------------------------------------------------------------------ H1
    ring_phi = means[0.0]
    rand_phi = means[1.0]
    interior = {p: means[p] for p in P_VALUES if 0.0 < p < 1.0}
    peak_p = max(interior, key=interior.get)
    peak_phi = interior[peak_p]
    h1_supported = (peak_phi > ring_phi + EPS) and (peak_phi > rand_phi + EPS)

    print()
    print("H1 — non-monotone small-world peak in Φ:")
    print("    ring (p=0) mean max-Φ_MIP     = %.4f" % ring_phi)
    print("    random (p=1) mean max-Φ_MIP   = %.4f" % rand_phi)
    print("    interior peak at p=%.2f       = %.4f" % (peak_p, peak_phi))
    print("    peak exceeds BOTH ring and random: %s" % h1_supported)
    h1_word = "SUPPORTED" if h1_supported else "REFUTED"
    print("H1 non-monotone small-world Φ peak: %s" % h1_word)

    # ------------------------------------------------------------------ H2
    print()
    print("H2 — verdict holds triadic across the whole sweep:")
    print("    every evaluated network triadic: %s" % all_triadic)
    cores = sorted({r[6] for r in rows})
    print("    distinct major-complex cores observed: %d (%s)"
          % (len(cores), "core churn" if len(cores) > 1 else "stable core"))
    h2_word = "SUPPORTED" if all_triadic else "REFUTED"
    print("H2 verdict stays triadic under rewiring: %s" % h2_word)


if __name__ == "__main__":
    main()
