"""q149 — the Shapley split of subsystem Φ across topologies: does the 2/3 mediator rent hold?

Question: the read-recipient triad splits its Φ so the mediator captures about two-thirds of the
total Shapley value (the "mediator rent"). Does that rent survive as topology changes? When mediation
is carried by one hub, two hubs, m symmetric hubs, or distributed over a ring or an all-required pool,
how much of the subsystem Φ does the hub/mediator set capture, and how is the rest split among parties?

H1: The Shapley share captured by hub/mediator nodes falls monotonically from the single-hub triad
    (~2/3) toward equal shares as mediation distributes across more hubs, so distributing mediation
    distributes the rent. Null: the hub share is constant across topologies.

H2: In symmetric topologies (ring, pool) Shapley values are equal across all nodes to within tolerance,
    so structural symmetry forces value symmetry independent of n. Null: a symmetric topology yields
    unequal Shapley values.

Method: apply shapley() (Shapley value of subsystem Φ at the all-ones integrating state, value of a
coalition S = Φ of the subsystem on S) to single_hub, two_hub, sym_multihub(m), ring, and pool at
n in {5, 6}. For the hub topologies report the per-node value share and the hub-vs-party split, and
track the per-hub share as the number of hubs grows. For the symmetric topologies test whether all
node values are equal to within tolerance. Control: the read-recipient triad, where the mediator is
known to capture ~2/3 of the total.

Scope: in-silico. All forms are synthetic Boolean coordination models, not measured organizations.
The result characterizes how an exact-Φ Shapley split behaves across these topology families; it does
not measure value capture in any real group. No worker is measured.

Run:
  source /tmp/rvenv/bin/activate && export PYPHI_WELCOME_OFF=yes && \
  python -m org_frontier.questions.q149_topology_shapley_split.probe_topology_shapley_split
"""

import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

import numpy as np

from org_frontier.probes.lib import verdict
from org_frontier.questions.q111_shapley_value.forms import shapley, read_recipient
from org_frontier.probes.probe_distributed_mediators import single_hub, two_hub
from org_frontier.probes.probe_multihub_law import sym_multihub
from org_frontier.probes.probe_scaling_zoo import ring
from org_frontier.probes.probe_topology_map import pool

# Fixed seed: the Shapley computation is exact and deterministic, but seed the RNG so any
# incidental randomness reproduces byte-for-byte on re-run.
RNG = np.random.default_rng(0)

TOL = 1e-3  # tolerance for "equal Shapley values" (values are rounded to 3 decimals)


def _labels(n):
    return tuple(f"n{i}" for i in range(n))


def _split(values, hub_idx, labels):
    """Sum of Shapley value over hub nodes and over party nodes, plus the hub fraction of total."""
    hub_set = {labels[i] for i in hub_idx}
    hub_sum = sum(v for k, v in values.items() if k in hub_set)
    party_sum = sum(v for k, v in values.items() if k not in hub_set)
    total = hub_sum + party_sum
    frac = hub_sum / total if total > 1e-9 else 0.0
    return hub_sum, party_sum, frac


def instrument_control():
    """Validate the machinery on two known cases before computing anything new."""
    # 1. The faithful worker-system-counterpart triad reads 'triadic' at max_phi 2.0.
    v = verdict([lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]], ("W", "S", "C"))
    assert v.structure == "triadic", v.structure
    assert abs(v.max_phi - 2.0) < 1e-6, v.max_phi

    # 2. The read-recipient triad splits Φ so the mediator M captures ~2/3 of the total.
    rules, labels = read_recipient()
    vals, total = shapley(rules, labels)
    assert abs(total - 2.0) < 1e-6, total
    m_frac = vals["M"] / total
    assert abs(m_frac - 2.0 / 3.0) < 1e-3, m_frac
    assert abs(vals["E"] - vals["R"]) < 1e-6, vals  # the two outer parties are symmetric
    print(
        f"CONTROL read-recipient triad: total Φ={total:.3f}, mediator M share="
        f"{m_frac:.3f} (~2/3), outer parties E=R={vals['E']:.3f}: PASS"
    )
    return m_frac


def main():
    control_frac = instrument_control()
    print("=" * 78)
    print("q149 — Shapley split of subsystem Φ across topologies")
    print("=" * 78)

    # ---- Hub topologies: track the hub/mediator value share -------------------------
    # For each, hub_idx names the mediator node(s); the rest are parties.
    hub_rows = []  # (label, n, n_hubs, total, hub_sum, party_sum, hub_frac, per_hub)
    print("\nHub topologies — hub-vs-party Shapley split (share of total Φ):")
    print(
        f"  {'topology':<16}{'n':<4}{'hubs':<6}{'Φ_total':<10}{'hub_sum':<10}"
        f"{'party_sum':<11}{'hub_share':<11}{'per_hub'}"
    )
    for n in (5, 6):
        # single hub: 1 mediator (node 0)
        specs = [("single_hub", single_hub(n), [0], 1)]
        # two hub: 2 mediators (nodes 0,1)
        specs.append(("two_hub", two_hub(n), [0, 1], 2))
        # symmetric multihub with m hubs, sweep m so mediation distributes over more hubs
        for m in range(1, n - 1):  # m hubs, n-m parties, at least one party
            specs.append((f"sym_multihub(m={m})", sym_multihub(n, m), list(range(m)), m))
        for name, rules, hub_idx, n_hubs in specs:
            labels = _labels(n)
            vals, total = shapley(rules, labels)
            hub_sum, party_sum, frac = _split(vals, hub_idx, labels)
            per_hub = hub_sum / n_hubs if n_hubs else 0.0
            hub_rows.append((name, n, n_hubs, total, hub_sum, party_sum, frac, per_hub))
            print(
                f"  {name:<16}{n:<4}{n_hubs:<6}{total:<10.3f}{hub_sum:<10.3f}"
                f"{party_sum:<11.3f}{frac:<11.3f}{per_hub:<.3f}"
            )

    # ---- Symmetric topologies: test value equality across all nodes -----------------
    sym_rows = []  # (name, n, total, spread, equal)
    print("\nSymmetric topologies — spread of Shapley values across nodes:")
    print(f"  {'topology':<10}{'n':<4}{'Φ_total':<10}{'min_val':<10}{'max_val':<10}{'spread':<10}{'equal'}")
    for n in (5, 6):
        for name, build in (("ring", ring), ("pool", pool)):
            labels = _labels(n)
            vals, total = shapley(build(n), labels)
            vlist = list(vals.values())
            spread = max(vlist) - min(vlist)
            equal = spread <= TOL
            sym_rows.append((name, n, total, spread, equal))
            print(
                f"  {name:<10}{n:<4}{total:<10.3f}{min(vlist):<10.3f}{max(vlist):<10.3f}"
                f"{spread:<10.3f}{equal}"
            )

    # ---- H1 verdict -----------------------------------------------------------------
    # H1 claims the hub SHARE falls monotonically from the single-hub triad (~2/3) toward
    # equal shares as the number of hubs grows. Build, per n, the sequence of hub shares
    # ordered by the number of hubs (single_hub then sym_multihub m=1,2,... and two_hub),
    # and test whether the per-node hub advantage shrinks as mediation distributes.
    #
    # The clean monotone series at fixed n is sym_multihub(m) for m=1..n-2: as m rises, more
    # nodes are hubs, and "equal shares" means hub_share -> n_hubs/n. The right quantity is
    # the hub PER-NODE share relative to the equal-share baseline; if distributing the rent
    # works, the per-hub share should fall toward total/n as m grows.
    print("\nH1 — does the per-hub Shapley share fall as mediation distributes?")
    h1_ok = True
    h1_detail = []
    for n in (5, 6):
        series = [r for r in hub_rows if r[1] == n and r[0].startswith(("single_hub", "sym_multihub"))]
        # order by number of hubs
        series.sort(key=lambda r: r[2])
        per_hub_seq = [r[7] for r in series]
        equal_share = series[0][3] / n  # total/n at this n (total is ~constant within a family build)
        # monotone non-increasing per-hub share?
        mono = all(per_hub_seq[i + 1] <= per_hub_seq[i] + TOL for i in range(len(per_hub_seq) - 1))
        # and the first (single hub) per-hub share exceeds the last (most-distributed)?
        falls = per_hub_seq[0] > per_hub_seq[-1] + TOL
        h1_detail.append((n, per_hub_seq, mono, falls))
        print(
            f"  n={n}: per-hub share by hub count {[round(x, 3) for x in per_hub_seq]}"
            f"  monotone_down={mono}  falls={falls}"
        )
        if not (mono and falls):
            h1_ok = False

    # ---- H2 verdict -----------------------------------------------------------------
    h2_ok = all(equal for (_, _, _, _, equal) in sym_rows)
    print("\nH2 — are ring and pool Shapley values equal across all nodes (within tol)?")
    for name, n, total, spread, equal in sym_rows:
        print(f"  {name:<10} n={n}: spread={spread:.3f}  equal={equal}")

    print("=" * 78)
    print(f"  Control mediator share = {control_frac:.3f} (read-recipient ~2/3 rent).")
    h1_verdict = "SUPPORTED" if h1_ok else "REFUTED"
    h2_verdict = "SUPPORTED" if h2_ok else "REFUTED"
    print(
        "H1 (per-hub Shapley share falls monotonically as mediation distributes): "
        f"{h1_verdict}"
    )
    print(
        "H2 (symmetric topologies ring/pool yield equal Shapley values within tol): "
        f"{h2_verdict}"
    )
    print("=" * 78)


if __name__ == "__main__":
    main()
