"""Probe 133 (R1) — does peer coupling keep parties in the core at intermediate hub counts?

Question: at intermediate mediator counts the parties drop from the core while the hubs hold it (#128).
Is that because the parties only reach the rest through the hubs? Hypothesis: giving the parties peer
edges — each party reading the other parties as well as the hubs — keeps them in the core at the
intermediate m where they otherwise drop. Method: build a symmetric m-hub with added party-to-party
coupling and compare its core at the intermediate m to the plain symmetric m-hub.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.probes.probe_party_peer_coupling
"""

import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from .lib import major_complex
from .probe_multihub_law import sym_multihub


def sym_multihub_peers(n, m):
    """Symmetric m-hub where each party also reads the other parties (peer coupling)."""
    hubs = list(range(m))
    parties = list(range(m, n))
    rules = [None] * n
    for h in hubs:
        oh = [x for x in hubs if x != h]
        rules[h] = (lambda x, oh=oh: int(all(x[i] for i in parties) and all(x[i] for i in oh)))
    for p in parties:
        op = [x for x in parties if x != p]
        rules[p] = (lambda x, op=op: int(all(x[i] for i in hubs) and all(x[i] for i in op)))
    return rules


def main():
    print("PROBE 133 (R1) — party peer coupling at intermediate hub counts")
    print("=" * 64)
    print(f"  {'n':<4}{'m':<4}{'variant':<22}{'Φ':<9}{'core size':<11}{'full core'}")
    for n, m in ((5, 3), (6, 3), (6, 4)):
        for name, build in (("plain m-hub", sym_multihub), ("m-hub + peer edges", sym_multihub_peers)):
            core, phi = major_complex(build(n, m), tuple(f"x{i}" for i in range(n)))
            sz = len(core) if core else 0
            print(f"  {n:<4}{m:<4}{name:<22}{phi:<9.3f}{sz:<11}{sz == n}")
    print("=" * 64)
    print("  Reading: if peer edges restore the full core at the intermediate m, the parties dropped only")
    print("  because they reached the group through the hubs alone; a lateral tie among them keeps each")
    print("  pivotal. If they still drop, the center-periphery effect is deeper than missing peer links.")
    print("=" * 64)


if __name__ == "__main__":
    main()
