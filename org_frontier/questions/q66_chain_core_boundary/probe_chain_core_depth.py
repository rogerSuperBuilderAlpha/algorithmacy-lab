"""Probe Q66-H1/H2 — open-chain core is the recipient-facing pair, size two, at every depth.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.questions.q66_chain_core_boundary.probe_chain_core_depth
"""
import csv, os
from org_frontier.probes.lib import verdict, major_complex
from org_frontier.questions.q66_chain_core_boundary.forms import open_chain, chain_labels, check_controls


def main():
    print("PROBE Q66-H1/H2 — open-chain core across depth")
    print("=" * 64)
    print(check_controls(verdict))
    rows, all_pair, all_size2 = [], True, True
    for d in (2, 3, 4):
        lab = chain_labels(d)
        core, phi = major_complex(open_chain(d), lab)
        cs = set(core or ())
        expect = {f"A{d}", "R"}
        is_pair = cs == expect
        size2 = len(core or ()) == 2
        all_pair &= is_pair; all_size2 &= size2
        print(f"  d={d} (n={d+2})  core={core}  Φ={phi:.4f}  =={{A{d},R}}:{is_pair}  size2:{size2}")
        rows.append((d, d + 2, "|".join(core or ()), f"{phi:.6f}", is_pair, size2))
    print("=" * 64)
    print(f"  core is recipient-pair at every depth: {all_pair}")
    print(f"  core size two at every depth: {all_size2}")
    print(f"  H1 VERDICT: {'CONFIRMED' if all_pair else 'REFUTED'}")
    print(f"  H2 VERDICT: {'CONFIRMED' if all_size2 else 'REFUTED'}")
    d_ = os.path.join(os.path.dirname(__file__), "results"); os.makedirs(d_, exist_ok=True)
    with open(os.path.join(d_, "chain_core_depth.csv"), "w", newline="") as f:
        w = csv.writer(f); w.writerow(["d", "n", "core", "phi", "is_recipient_pair", "size2"]); w.writerows(rows)


if __name__ == "__main__":
    main()
