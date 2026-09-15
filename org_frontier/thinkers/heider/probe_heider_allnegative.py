"""Probe — Heider H3: the all-negative triad is a third kind.

Question.  Heider (1946: 110): the case with three negative relations "does not seem to constitute a good
           psychological balance, since it is too indetermined." Cartwright & Harary count it unbalanced;
           Davis (1967) counts it clusterable. Does −−− differ structurally from ++− (Φ, core size,
           attractor count), or are they one structure?
Hypothesis. H3 (Heider): they differ. Lab prior: identical — −−− flips to ++− by complementing one person.
Method.    mmm and ppm; Φ_MIP, core, attractors.
Run.       ~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.heider.probe_heider_allnegative
"""

from org_frontier.thinkers.heider import forms as F


def main():
    print("Heider H3 — the all-negative triad against the one-negative triad")
    control = F.run_control()
    recs = {}
    for name in ("ppm", "mmm"):
        signs = F.NAMED[name]
        recs[name] = F.evaluate(name, F.triad(signs), F.TRIAD_LABELS, F.TRIAD_EDGES, signs)
        print(F.line(recs[name]))
    a, b = recs["ppm"], recs["mmm"]
    same_phi = abs(a["phi_mip"] - b["phi_mip"]) < 1e-9
    same_core = len(a["core"]) == len(b["core"])
    same_att = len(a["attractors"]) == len(b["attractors"]) and a["n_cycles"] == b["n_cycles"]
    print("  same Φ_MIP=%s  same core size=%s  same attractor count=%s (ppm %d, mmm %d)"
          % (same_phi, same_core, same_att, len(a["attractors"]), len(b["attractors"])))
    status = "REFUTED" if (same_phi and same_core and same_att) else "CONFIRMED"
    print("H3 (−−− is structurally distinct from ++−): %s" % status)
    F.save("probe_heider_allnegative", {"control": control, "forms": recs, "H3": status})


if __name__ == "__main__":
    main()
