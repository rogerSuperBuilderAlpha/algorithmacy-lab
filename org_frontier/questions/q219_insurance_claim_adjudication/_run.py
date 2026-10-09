"""Q219 shared runner: classify one form, print its verdict, core and per-state Φ, write a CSV.

Used by probe_457 … probe_460. The decision rules themselves live in each probe, as fixed in methods.md.
"""

import csv
import os

from org_frontier.probes.lib import verdict, major_complex
from org_frontier.questions.q219_insurance_claim_adjudication.forms import LABELS

PHI_EPS = 1e-9
RESULTS = os.path.join(os.path.dirname(__file__), "results")


def state_str(s):
    return "".join(str(int(b)) for b in s) if s is not None else "-"


def run_form(name, rules):
    """Return a dict with verdict, max Φ, MIP, core, core Φ, and the per-state profile; print it."""
    v = verdict(rules, LABELS)
    core, core_phi = major_complex(rules, LABELS)
    core = tuple(core) if core else ()
    irreducible = [s for s, p in v.phi_profile if p > PHI_EPS]
    core_txt = "{" + ",".join(core) + "}" if core else "(none)"
    print(f"  {name:<22} {v.structure:<8} max Φ_MIP={v.max_phi:.4f}  MIP={v.mip_partition}  "
          f"core={core_txt} core Φ={core_phi:.4f}")
    print(f"  {'':<22} per-state Φ_MIP (C,E,A): "
          + "  ".join(f"{state_str(s)}:{p:.4f}" for s, p in v.phi_profile))
    print(f"  {'':<22} irreducible states: {len(irreducible)}/{v.n_states_evaluated} "
          f"[{' '.join(state_str(s) for s in irreducible)}]")
    return {
        "form": name, "structure": v.structure, "max_phi": v.max_phi, "mip": v.mip_partition,
        "core": core, "core_txt": core_txt, "core_phi": float(core_phi),
        "profile": list(v.phi_profile), "irreducible": irreducible,
        "n_states": v.n_states_evaluated,
    }


def triadic_full(r):
    return r["structure"] == "triadic" and set(r["core"]) == set(LABELS)


def write_csv(fname, rows):
    os.makedirs(RESULTS, exist_ok=True)
    path = os.path.join(RESULTS, fname)
    with open(path, "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["form", "structure", "max_phi", "mip", "core", "core_phi", "n_states",
                    "n_irreducible", "irreducible_states", "phi_profile"])
        for r in rows:
            w.writerow([r["form"], r["structure"], f"{r['max_phi']:.6f}", r["mip"], r["core_txt"],
                        f"{r['core_phi']:.6f}", r["n_states"], len(r["irreducible"]),
                        " ".join(state_str(s) for s in r["irreducible"]),
                        " ".join(f"{state_str(s)}:{p:.6f}" for s, p in r["profile"])])
    return path
