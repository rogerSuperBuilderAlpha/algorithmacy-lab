"""Probe Q66-H3/H4 — closing the chain into a ring binds the whole structure at higher Φ.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.questions.q66_chain_core_boundary.probe_ring_core
"""
import csv, os
from org_frontier.probes.lib import verdict, major_complex
from org_frontier.questions.q66_chain_core_boundary.forms import open_chain, ring, chain_labels, check_controls


def main():
    print("PROBE Q66-H3/H4 — closed ring core")
    print("=" * 64)
    print(check_controls(verdict))
    rows, all_full, all_higher = [], True, True
    for d in (2, 3):
        lab = chain_labels(d)
        rcore, rphi = major_complex(ring(d), lab)
        ocore, ophi = major_complex(open_chain(d), lab)
        full = set(rcore or ()) == set(lab)
        higher = (rphi or 0) > 2.0 + 1e-9 and abs((ophi or 0) - 2.0) < 1e-6
        all_full &= full; all_higher &= higher
        print(f"  d={d} (n={d+2})  ring core={rcore} Φ={rphi:.4f} full:{full} | open Φ={ophi:.4f}")
        rows.append((d, d + 2, "|".join(rcore or ()), f"{rphi:.6f}", full, f"{ophi:.6f}"))
    print("=" * 64)
    print(f"  ring core is full set at d=2,3: {all_full}")
    print(f"  ring Φ exceeds open-chain 2.0 at d=2,3: {all_higher}")
    print(f"  H3 VERDICT: {'CONFIRMED' if all_full else 'REFUTED'}")
    print(f"  H4 VERDICT: {'CONFIRMED' if all_higher else 'REFUTED'}")
    d_ = os.path.join(os.path.dirname(__file__), "results"); os.makedirs(d_, exist_ok=True)
    with open(os.path.join(d_, "ring_core.csv"), "w", newline="") as f:
        w = csv.writer(f); w.writerow(["d", "n", "ring_core", "ring_phi", "ring_full", "open_phi"]); w.writerows(rows)


if __name__ == "__main__":
    main()
