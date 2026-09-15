"""Probe — Ostrom H3: nested enterprises.

Question.  Ostrom (1990: 90, 101–102): governance "organized in multiple layers of nested enterprises." Two
           contingent-commitment triads whose delegates also answer to a federation. Is the nest one complex
           of seven, with each local triad still irreducible inside it? The Coleman paper's parents form had
           the upper layer become the core and the lower fall out.
Hypothesis. H3: core(nested) = all seven; each local triad Φ > 0 as a subsystem; unnested = two triads.
Run.       ~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.ostrom.probe_ostrom_nested
"""

from org_frontier.thinkers.ostrom import forms as F


def main():
    print("Ostrom H3 — two groups and a federation")
    control = F.run_control()
    recs = {name: F.evaluate(name) for name in ("unnested", "nested")}
    core, phi, state = F.maximal_state(F.SPECS["nested"])
    sub = {}
    for g in ("a", "b"):
        nodes = ["%s1" % g, "%s2" % g, "%s3" % g]
        sub[g] = F.subsystem_phi(F.SPECS["nested"], nodes, state) if state is not None else 0.0
        print("    local triad %s as a subsystem at state %s: Φ=%.3f" % (g, "".join(map(str, state)) if state else "-", sub[g]))
    all7 = set(recs["nested"]["core"]) == {"a1", "a2", "a3", "b1", "b2", "b3", "F"}
    locals_ok = all(v > 1e-6 for v in sub.values())
    un = recs["unnested"]
    unnested_ok = len(un["core"]) == 3 and un["phi_mip"] < 1e-9
    print("  nest is one complex of seven=%s   local triads irreducible inside=%s   unnested = two triads=%s" % (
        all7, locals_ok, unnested_ok))
    n = sum([all7, locals_ok, unnested_ok])
    status = "CONFIRMED" if n == 3 else ("PARTIAL" if n == 2 else "REFUTED")
    print("H3 (nested layers are one whole and each layer stays a whole): %s" % status)
    F.save("probe_ostrom_nested", {"control": control, "forms": recs, "nested_max_state": state,
                                   "local_subsystem_phi": sub, "H3": status})


if __name__ == "__main__":
    main()
