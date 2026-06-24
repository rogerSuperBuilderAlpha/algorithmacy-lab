"""q152 — Do the whole-system verdict and the major-complex membership ever disagree?

QUESTION
    Across the topologies built in studies 1-9 at matched n=5,6, does the whole-system
    verdict (triadic vs dyadic) ever disagree with the major-complex membership — a
    triadic verdict whose core excludes one or more of the parties it nominally
    coordinates? If so, the two readouts are not interchangeable diagnostics.

H1  There exist topologies (e.g. chain, large-m symmetric multihub, hub-chain) where the
    verdict is triadic yet the major complex excludes one or more parties, so the
    whole-system verdict and core membership are not interchangeable. Null: a triadic
    verdict always implies a full-party core.

H2  Verdict-complex disagreement appears exactly when a topology has a node whose Shapley
    value is zero (a zero-value party is the marker of a coordinated-but-excluded member).
    Null: zero-Shapley parties are always inside the core.

METHOD
    For every topology builder reused from studies 1-9 at n in {5,6}, read
      - verdict(rules,labels).structure        ('triadic' / 'dyadic') and .max_phi
      - major_complex(rules,labels)            -> (core label tuple, phi)
      - shapley(rules,labels)                  -> ({party: value}, total_phi)
    A topology DISAGREES when the verdict is triadic and the core omits >=1 node.
    H1 is SUPPORTED if at least one topology disagrees.
    H2 tests whether disagreement coincides with having a zero-Shapley node: it is
    CONFIRMED only if (disagree <=> has-zero-Shapley) holds for every topology, and is
    NOT SUPPORTED if any topology disagrees without a zero-Shapley node or carries a
    zero-Shapley node inside a full core.
    Control = the read-recipient / worker-system-counterpart triad, where the verdict is
    triadic and the core is the full party set.

    Results are exact IIT-4.0 Φ on synthetic Boolean coordination forms; this is an
    in-silico study of the diagnostics, not a claim about empirical organizations.

RUN
    source /tmp/rvenv/bin/activate && export PYPHI_WELCOME_OFF=yes && \
    python -m org_frontier.questions.q152_verdict_vs_complex_topology.probe_verdict_vs_complex_topology
"""

import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

import numpy as np

from org_frontier.probes.lib import verdict, major_complex
from org_frontier.questions.q111_shapley_value.forms import shapley, read_recipient

# Topology builders reused verbatim from studies 1-9.
from org_frontier.probes.probe_distributed_mediators import single_hub, two_hub
from org_frontier.probes.probe_multihub_law import sym_multihub
from org_frontier.probes.probe_scaling_zoo import ring
from org_frontier.probes.probe_topology_map import chain, pool
from org_frontier.questions.q148_multihub_chain_hierarchy.probe_multihub_chain_hierarchy import hub_chain

# Fixed seed: verdict / major_complex / shapley are exact and deterministic over the
# reachable-state enumeration; seed the RNG so any incidental randomness reproduces
# byte-for-byte on re-run.
RNG = np.random.default_rng(0)

ZERO_TOL = 1e-6  # |Shapley value| <= ZERO_TOL counts as a zero-value party


def _labels(n):
    return tuple(f"n{i}" for i in range(n))


def _topologies():
    """(name, rules, labels) for every studied topology at n in {5,6}.

    hub_chain is parameterised by (L, g) with n = L*(1+g); pick (L,g) pairs that land on
    n=5,6 with at least two hubs so the chain hierarchy is exercised.
    """
    specs = []
    for n in (5, 6):
        L = _labels(n)
        specs.append((f"chain(n={n})", chain(n), L))
        specs.append((f"ring(n={n})", ring(n), L))
        specs.append((f"pool(n={n})", pool(n), L))
        specs.append((f"single_hub(n={n})", single_hub(n), L))
        specs.append((f"two_hub(n={n})", two_hub(n), L))
        for m in range(1, n - 1):  # m hubs, n-m parties, at least one party
            specs.append((f"sym_multihub(n={n},m={m})", sym_multihub(n, m), L))
    # hub-chain hierarchies that land exactly on n=5,6
    for (Lh, g) in ((2, 2), (2, 3)):  # n = 2*3 = 6 ; n = 2*4 = 8 -> filter below
        rules, labels = hub_chain(Lh, g)
        if len(rules) in (5, 6):
            specs.append((f"hub_chain(L={Lh},g={g},n={len(rules)})", rules, labels))
    # also a 3-hub-by-1-party chain at n=6
    rules, labels = hub_chain(3, 1)  # n = 3*2 = 6
    if len(rules) == 6:
        specs.append((f"hub_chain(L=3,g=1,n=6)", rules, labels))
    return specs


def instrument_control():
    """Validate the machinery on the known triad before computing anything new."""
    rules = [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]
    labels = ("W", "S", "C")
    v = verdict(rules, labels)
    core, phi = major_complex(rules, labels)
    assert v.structure == "triadic", v.structure
    assert abs(v.max_phi - 2.0) < 1e-6, v.max_phi
    assert set(core) == set(labels), core           # full-party core
    assert abs(phi - 2.0) < 1e-6, phi
    # read_recipient is the same triad under different labels; its Shapley values are all
    # strictly positive, so the control carries NO zero-value party and the core is full.
    rr_rules, rr_labels = read_recipient()
    vals, total = shapley(rr_rules, rr_labels)
    assert abs(total - 2.0) < 1e-6, total
    n_zero = sum(1 for x in vals.values() if abs(x) <= ZERO_TOL)
    assert n_zero == 0, vals
    print(
        f"CONTROL read-recipient/worker-system-counterpart triad: verdict={v.structure}, "
        f"max_phi={v.max_phi:.3f}, core={core} (full), zero-Shapley parties={n_zero}: PASS"
    )


def main():
    instrument_control()
    print("=" * 92)
    print("q152 — whole-system verdict vs major-complex membership across studied topologies (n=5,6)")
    print("=" * 92)
    print(
        f"  {'topology':<26}{'n':<3}{'verdict':<9}{'maxΦ':<8}"
        f"{'core_size':<11}{'full?':<7}{'zeroShap':<9}{'disagree'}"
    )

    rows = []
    for name, rules, labels in _topologies():
        n = len(rules)
        v = verdict(rules, labels)
        core, _cphi = major_complex(rules, labels)
        core = core or ()
        vals, _tot = shapley(rules, labels)
        n_zero = sum(1 for x in vals.values() if abs(x) <= ZERO_TOL)
        full = len(core) == n
        triadic = v.structure == "triadic"
        disagree = triadic and not full          # triadic verdict, party excluded from core
        rows.append((name, n, triadic, full, n_zero, disagree))
        print(
            f"  {name:<26}{n:<3}{v.structure:<9}{v.max_phi:<8.3f}"
            f"{len(core):<11}{('yes' if full else 'no'):<7}{n_zero:<9}{('YES' if disagree else 'no')}"
        )

    n_disagree = sum(1 for r in rows if r[5])
    n_total = len(rows)

    # ---- H1: does any triadic topology exclude a party? -----------------------------
    h1_supported = n_disagree > 0
    print("-" * 92)
    print(
        f"H1 summary: {n_disagree}/{n_total} studied topologies are triadic-verdict "
        f"yet exclude >=1 party from the major complex."
    )

    # ---- H2: is disagreement exactly the presence of a zero-Shapley node? -----------
    # Confirmed only if (disagree <=> has-zero-Shapley) holds for every topology.
    biconditional_holds = all((r[5]) == (r[4] > 0) for r in rows)
    disagree_no_zero = [r[0] for r in rows if r[5] and r[4] == 0]
    zero_but_full = [r[0] for r in rows if (not r[5]) and r[4] > 0 and r[2]]
    h2_confirmed = biconditional_holds and h1_supported

    print(
        f"H2 summary: disagree<=>has-zero-Shapley holds for all topologies: {biconditional_holds}. "
        f"Triadic-exclusions with NO zero-Shapley node: {len(disagree_no_zero)} "
        f"({', '.join(disagree_no_zero) if disagree_no_zero else 'none'}). "
        f"Zero-Shapley nodes sitting inside a full triadic core: {len(zero_but_full)} "
        f"({', '.join(zero_but_full) if zero_but_full else 'none'})."
    )
    print("=" * 92)

    print(
        "H1 verdict-complex disagreement exists: "
        + ("SUPPORTED" if h1_supported else "REFUTED")
    )
    print(
        "H2 disagreement is exactly the zero-Shapley marker: "
        + ("CONFIRMED" if h2_confirmed else "NOT SUPPORTED")
    )


if __name__ == "__main__":
    main()
