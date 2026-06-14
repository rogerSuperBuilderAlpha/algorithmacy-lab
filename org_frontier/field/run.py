"""Run the 10 mock organizations through the exact-Φ instrument and report the field demo.

Validates the instrument on its two canonical controls first; refuses to run if either fails.
For each mock it prints the whole-system verdict, the major complex, and — where a sensitivity
variant is defined — the verdict under the alternative encoding and whether it flips.

Run from the repo root with the venv active:  python -m org_frontier.field.run
"""

import csv
import os
import sys

from .mocks import MOCKS
from org_frontier.classifier.classifier import classify_rules
from org_frontier.probes.lib import major_complex
from org_frontier.classifier.validate import factoring_control, irreducible_control

_RESULTS = os.path.join(os.path.dirname(__file__), "results")


def _verdict(parties, rules):
    v = classify_rules(rules, parties)
    core, core_phi = major_complex(list(rules), parties)
    return v.structure, round(v.max_phi, 3), ("".join(core) if core else "—"), round(max(core_phi, 0.0), 3)


def main() -> int:
    print("=" * 96)
    print("FIELD PROTOCOL DEMO — 10 mock organizations through the exact-Φ instrument")
    print("=" * 96)
    fac = classify_rules(factoring_control())
    irr = classify_rules(irreducible_control())
    if not (fac.structure == "dyadic" and irr.structure == "triadic"):
        print("  INSTRUMENT CONTROL FAILED — refusing to run.")
        return 1
    print("  Instrument validated (factoring -> dyadic, irreducible -> triadic).")
    print("  These are STIPULATED models of invented organizations. They demonstrate the protocol;")
    print("  they measure no real organization. See PROTOCOL.md and FINDINGS.md.\n")

    rows = []
    matched = 0
    flips = []
    for m in MOCKS:
        struct, sysphi, core, corephi = _verdict(m.parties, m.rules)
        ok = struct == m.predict
        matched += ok
        flag = "" if ok else "  <-- computed verdict overturns the pre-registered reading"
        print(f"  {m.mid}  {m.org}")
        print(f"      parties {','.join(m.parties)} | predicted {m.predict} | "
              f"verdict {struct.upper()} (Φ={sysphi}) | core {core} (Φ={corephi}){flag}")
        srow = {"sensitivity": "", "sens_verdict": "", "sens_flips": ""}
        if m.sensitivity:
            s = m.sensitivity
            s_struct, s_sysphi, s_core, s_corephi = _verdict(s.parties, s.rules)
            flipped = s_struct != struct
            if flipped:
                flips.append((m.mid, m.org, struct, s_struct, s.name))
            print(f"      sensitivity [{s.name}]: {s_struct.upper()} (Φ={s_sysphi}, core {s_core}) "
                  f"— {'FLIPS' if flipped else 'holds'}")
            srow = {"sensitivity": s.name, "sens_verdict": s_struct,
                    "sens_flips": flipped}
        print()
        rows.append({"id": m.mid, "org": m.org, "parties": " ".join(m.parties),
                     "predict": m.predict, "verdict": struct, "system_phi": sysphi,
                     "core": core, "core_phi": corephi, "matched": ok, **srow})

    print("=" * 96)
    print(f"  {len(MOCKS)} mock organizations | verdict matched the pre-registered reading: "
          f"{matched}/{len(MOCKS)}")
    triadic = sum(r["verdict"] == "triadic" for r in rows)
    print(f"  {triadic} triadic (algorithmacy), {len(rows) - triadic} dyadic (literacy)")
    if flips:
        print(f"  {len(flips)} sensitivity flip(s) — a defensible re-encoding changed the verdict:")
        for mid, org, a, b, name in flips:
            print(f"    {mid} {org}: {a} -> {b} under [{name}]")
    print("=" * 96)

    os.makedirs(_RESULTS, exist_ok=True)
    path = os.path.join(_RESULTS, "field_mocks.csv")
    with open(path, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=["id", "org", "parties", "predict", "verdict",
                                           "system_phi", "core", "core_phi", "matched",
                                           "sensitivity", "sens_verdict", "sens_flips"])
        w.writeheader()
        w.writerows(rows)
    print(f"  Wrote {os.path.relpath(path, os.getcwd())}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
