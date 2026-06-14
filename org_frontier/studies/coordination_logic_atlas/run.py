"""Run the 50-experiment coordination-logic atlas, write results/atlas.csv, print the report.

Validates the instrument on its two canonical controls first; refuses to run if either fails.

Run from the repo root with the venv active:  python -m org_frontier.studies.coordination_logic_atlas.run
"""

import csv
import os
import sys

from .atlas import (EXPERIMENTS, THEME_ORDER, THEME_TITLE, run_experiment,
                    validate_instrument)

_RESULTS = os.path.join(os.path.dirname(__file__), "results")


def main() -> int:
    print("=" * 92)
    print("COORDINATION-LOGIC ATLAS — 50 experiments on what makes a coordination form irreducible")
    print("=" * 92)

    if not validate_instrument():
        print("  INSTRUMENT CONTROL FAILED — refusing to run. Do not trust any verdict.")
        return 1
    print("  Instrument validated (factoring control -> dyadic, irreducible control -> triadic).\n")

    results = [run_experiment(e) for e in EXPERIMENTS]

    matched = sum(r.matched for r in results)
    surprises = [r for r in results if not r.matched]
    novel = [r for r in results if not r.anchor]
    novel_matched = sum(r.matched for r in novel)

    print("  Primary verdict = whole-system Φ over the MIP (the lab's classifier). The major")
    print("  complex (core + its Φ) is reported alongside to show which parties stay irreducible")
    print("  when the whole system factors — the verdict/complex split.\n")
    for theme in THEME_ORDER:
        rows = [r for r in results if r.theme == theme]
        print(THEME_TITLE[theme])
        print(f"  {'id':<5}{'experiment':<48}{'pred':<8}{'verdict':<9}{'sysΦ':<8}{'core':<13}{'coreΦ'}")
        for r in rows:
            core = "".join(r.core) if r.core else "—"
            flag = "" if r.matched else "  <-- SURPRISE"
            print(f"  {r.eid:<5}{r.name[:46]:<48}{r.predict:<8}{r.structure:<9}"
                  f"{r.max_phi:<8.3f}{core:<13}{r.core_phi:.3f}{flag}")
        print()

    print("=" * 92)
    print(f"  {len(results)} experiments | predictions matched: {matched}/{len(results)} "
          f"| novel (non-anchor): {novel_matched}/{len(novel)} matched")
    if surprises:
        print(f"  {len(surprises)} surprise(s) where the verdict defied the pre-registered prediction:")
        for r in surprises:
            print(f"    {r.eid} {r.name[:60]}: predicted {r.predict}, got {r.structure} (Φ={r.max_phi:.3f})")
    else:
        print("  No surprises: every verdict matched its pre-registered prediction.")
    print("=" * 92)

    os.makedirs(_RESULTS, exist_ok=True)
    path = os.path.join(_RESULTS, "atlas.csv")
    with open(path, "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["id", "theme", "experiment", "n_nodes", "predict", "binds", "core",
                    "core_phi", "core_size", "whole_system_structure", "whole_system_phi",
                    "n_irreducible_states", "matched", "anchor", "rationale"])
        for r in results:
            w.writerow([r.eid, r.theme, r.name, r.n, r.predict, r.binds,
                        "".join(r.core) if r.core else "", f"{r.core_phi:.6f}", r.core_size,
                        r.structure, f"{r.max_phi:.6f}", r.n_irreducible,
                        r.matched, r.anchor, r.rationale])
    print(f"  Wrote {os.path.relpath(path, os.getcwd())}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
