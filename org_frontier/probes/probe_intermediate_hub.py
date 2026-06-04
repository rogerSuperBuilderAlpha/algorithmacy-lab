"""Probe 128 (N1) — why does an intermediate hub count drop members from the core?

Question: a symmetric m-hub raises Φ as m grows, yet at intermediate m the core is not full — some nodes
drop while Φ rises (#119). Which nodes drop, and why? Hypothesis: the dropped nodes are the parties, which
lose pivotality once the hub cluster is large enough to carry the integration on its own. Method: at the m
where the core is not full (n=6, m=3 and m=4), read the major complex and label each in/out node as a hub
or a party.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.probes.probe_intermediate_hub
"""

import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from .lib import major_complex
from .probe_multihub_law import sym_multihub


def main():
    print("PROBE 128 (N1) — which nodes drop at an intermediate hub count")
    print("=" * 68)
    for n, ms in ((5, (3,)), (6, (3, 4))):
        for m in ms:
            labels = tuple([f"H{i}" for i in range(m)] + [f"P{i}" for i in range(n - m)])
            core, phi = major_complex(sym_multihub(n, m), labels)
            core = core or ()
            hubs_in = [c for c in core if c.startswith("H")]
            parties_in = [c for c in core if c.startswith("P")]
            hubs_out = [f"H{i}" for i in range(m) if f"H{i}" not in core]
            parties_out = [f"P{i}" for i in range(n - m) if f"P{i}" not in core]
            print(f"  n={n} m={m}: Φ={phi:.2f} core={list(core)}")
            print(f"           hubs in={hubs_in} out={hubs_out} | parties in={parties_in} out={parties_out}")
    print("=" * 68)
    print("  Reading: if the dropped nodes are the parties while the hubs stay, the hub cluster carries the")
    print("  integration once it is large enough and the peripheral parties lose their pivotal hold. If")
    print("  hubs drop too, the fragmentation is more than a center-periphery effect.")
    print("=" * 68)


if __name__ == "__main__":
    main()
