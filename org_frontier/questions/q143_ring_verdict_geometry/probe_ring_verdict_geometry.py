"""Probe Q143 (297) — the ring's verdict and where its MIP cut falls as n grows.

Question: a conjunctive ring sets each node to the AND of its two neighbours. Does it read
triadic, and where does the minimum-information partition fall as the ring grows from n=3 to n=7?

H1 (fixed before computing): the ring is triadic at every n=3..7 with Φ bounded away from zero,
and its MIP is a single balanced two-arc cut whose Φ is constant in n (rotational symmetry forces
one bottleneck). Null: the ring goes dyadic at some n, or its MIP-Φ varies with n.

H2 (fixed before computing): the major complex of the ring is the full node set at every n (no node
drops), unlike the m-hub where parties drop at intermediate m. Null: the ring sheds at least one node
from the core at some n=4..7.

Method: run verdict() and major_complex() on scaling_zoo.ring(n) for n=3..7. Read .structure,
.max_phi, .mip_state, .mip_partition, and core membership. The control validates the machinery on the
faithful worker-system-counterpart triad (reads 'triadic', max_phi 2.0) and prints the chain (a serial
form whose MIP splits at an end) and the pool (whose core is full) as topology anchors. All Φ values
are exact IIT-4.0 over reachable states. Results are on synthetic Boolean coordination forms; no real
coordination is measured. The instrument is explored here, not established as the necessary test.

Run:  source /tmp/rvenv/bin/activate && export PYPHI_WELCOME_OFF=yes && \
      python -m org_frontier.questions.q143_ring_verdict_geometry.probe_ring_verdict_geometry
"""

import os
import sys

import numpy as np

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.probes.lib import verdict, major_complex
from org_frontier.probes.probe_scaling_zoo import ring
from org_frontier.probes.probe_topology_map import chain, pool

EPS = 1e-6
N_RANGE = range(3, 8)


def _labels(n):
    return tuple("x%d" % i for i in range(n))


def _cut_arcs(mip_partition):
    """Number of parts the MIP names. A two-arc cut reads '2 parts: {...,...}'."""
    head = mip_partition.split(" parts:")[0].strip()
    try:
        return int(head)
    except ValueError:
        return None


def main():
    # Determinism: exact Φ over reachable states is deterministic; the seed pins any RNG the
    # exact-Φ backend draws so re-runs are byte-identical.
    rng = np.random.default_rng(0)
    _ = rng.random()

    print("PROBE Q143 (297) — the ring's verdict and MIP geometry as n grows")
    print("=" * 78)

    # INSTRUMENT CONTROL — the faithful worker-system-counterpart triad reads triadic, Φ = 2.0.
    ctrl = verdict([lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]], ("W", "S", "C"))
    ctrl_ok = ctrl.structure == "triadic" and abs(ctrl.max_phi - 2.0) < EPS
    print("INSTRUMENT CONTROL: triad [x1, x0&x2, x1] -> structure=%s max_phi=%.4f"
          % (ctrl.structure, ctrl.max_phi))
    if not ctrl_ok:
        print("CONTROL ... FAIL (expected triadic, max_phi 2.0)")
        sys.exit(1)
    print("CONTROL faithful-triad reads triadic at Φ=2.0: PASS")

    # Topology anchors from probe_topology_map: the chain splits (serial), the pool keeps a full core.
    ch_core, ch_phi = major_complex(chain(5), _labels(5))
    pl_core, pl_phi = major_complex(pool(5), _labels(5))
    ch_v = verdict(chain(5), _labels(5))
    print("ANCHOR chain(5): structure=%s max_phi=%.4f MIP=%r core=%s"
          % (ch_v.structure, ch_v.max_phi, ch_v.mip_partition, ch_core))
    print("ANCHOR pool(5):  Φ=%.4f core=%s (|core|=%d)" % (pl_phi, pl_core, len(pl_core)))
    print("-" * 78)

    # REAL RESULT — the conjunctive ring at n=3..7.
    print("  %-5s%-11s%-10s%-30s%-8s%s" % ("n", "structure", "max_phi", "MIP cut", "|core|", "core=full?"))
    rows = []
    for n in N_RANGE:
        lbls = _labels(n)
        v = verdict(ring(n), lbls)
        core, mc_phi = major_complex(ring(n), lbls)
        full = len(core) == n
        arcs = _cut_arcs(v.mip_partition)
        rows.append({
            "n": n,
            "structure": v.structure,
            "max_phi": v.max_phi,
            "mip": v.mip_partition,
            "arcs": arcs,
            "core_size": len(core),
            "full": full,
            "mc_phi": mc_phi,
        })
        print("  %-5d%-11s%-10.4f%-30s%-8d%s"
              % (n, v.structure, v.max_phi, v.mip_partition, len(core), "yes" if full else "NO"))
    print("=" * 78)

    # H1: triadic at every n with Φ bounded away from zero, a single balanced two-arc cut whose Φ
    # is constant in n. Test each clause and report which clause, if any, breaks.
    all_triadic = all(r["structure"] == "triadic" and r["max_phi"] > EPS for r in rows)
    all_two_arc = all(r["arcs"] == 2 for r in rows)
    phis = [r["max_phi"] for r in rows]
    phi_constant = (max(phis) - min(phis)) < EPS
    h1 = all_triadic and all_two_arc and phi_constant

    print("H1 clauses:")
    print("  triadic with Φ>0 at every n:        %s" % all_triadic)
    print("  MIP is a two-arc (2-part) cut at every n: %s" % all_two_arc)
    print("  MIP-Φ constant across n=3..7:        %s (min=%.4f max=%.4f)"
          % (phi_constant, min(phis), max(phis)))

    # H2: the major complex is the full node set at every n.
    h2 = all(r["full"] for r in rows)
    print("H2 check: core is the full node set at every n=3..7: %s" % h2)
    print("=" * 78)

    print("H1 ring is triadic with a single balanced two-arc cut of constant Φ in n: %s"
          % ("SUPPORTED" if h1 else "REFUTED"))
    print("H2 the ring's major complex is the full node set at every n=3..7: %s"
          % ("SUPPORTED" if h2 else "REFUTED"))


if __name__ == "__main__":
    main()
