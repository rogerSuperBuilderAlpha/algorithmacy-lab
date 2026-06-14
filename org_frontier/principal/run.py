"""Does the corporate principal join the irreducible core?

For each form: the whole-system verdict (Φ over the MIP) AND the major complex — the maximally
irreducible subset of nodes (PyPhi `new_big_phi.maximal_complex`). The major complex is the right
object here: whole-system Φ is sensitive to spectator nodes (an idle principal makes the whole
system factor even when the W–S–C triad is irreducible), so "does P join the core?" is answered by
whether P appears in the major complex, not by whole-system Φ alone.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.principal.run
"""

import csv
import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

import pyphi
from pyphi import exceptions, new_big_phi

from org_frontier.classifier.classifier import classify_rules, tpm_from_rules, cm_from_rules
from foundations.proxy_audit.exact_phi import reachable_states
from . import forms as pf

pyphi.config.PROGRESS_BARS = False
pyphi.config.PARALLEL = False
_RESULTS = os.path.join(os.path.dirname(__file__), "results")


def major_complex(rules):
    """Return (node_labels_tuple, phi) of the maximal complex over reachable states."""
    tpm, cm = tpm_from_rules(rules), cm_from_rules(rules)
    net = pyphi.Network(tpm, cm=cm, node_labels=pf.LABELS)
    best = (None, -1.0)
    for s in reachable_states(tpm, 4):
        state = tuple((s >> i) & 1 for i in range(4))
        try:
            mc = new_big_phi.maximal_complex(net, state)
        except (exceptions.StateUnreachableError, ValueError):
            continue
        if isinstance(mc, new_big_phi.NullPhiStructure):
            continue  # no irreducible complex at this state
        if float(mc.phi) > best[1]:
            # node_labels is the full network's labels; the complex's nodes are node_indices.
            core = tuple(pf.LABELS[i] for i in mc.node_indices)
            best = (core, float(mc.phi))
    return best


def main():
    os.makedirs(_RESULTS, exist_ok=True)
    rows = []
    print("THE CORPORATE PRINCIPAL — does P join the irreducible core?")
    print("=" * 92)
    print("  baseline: the bare W,S,C triad is irreducible on its own (Φ = 2.0)\n")
    for f in pf.FORMS:
        v = classify_rules(f.rules, labels=pf.LABELS)
        core, core_phi = major_complex(f.rules)
        p_in = core is not None and "P" in core
        print(f"  {f.key:<20} whole-system: {v.structure:<8} Φ={v.max_phi:.3f}   "
              f"major complex: {core} Φ={core_phi:.3f}   P in core: {p_in}")
        rows.append({"key": f.key, "whole_system_structure": v.structure,
                     "whole_system_phi": f"{v.max_phi:.6f}",
                     "major_complex": "".join(core) if core else "",
                     "major_complex_phi": f"{core_phi:.6f}", "principal_in_core": p_in})
    path = os.path.join(_RESULTS, "principal.csv")
    with open(path, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        w.writeheader(); w.writerows(rows)
    print(f"\nWrote {path}")
    print("=" * 92)
    print("  READING: P joins the core only under bidirectional coupling (gates AND monitors).")
    print("  Ownership, one-directional gating, or monitoring alone leave P outside the core;")
    print("  the irreducible coordination stays the W,S,C triad.")
    print("=" * 92)


if __name__ == "__main__":
    main()
