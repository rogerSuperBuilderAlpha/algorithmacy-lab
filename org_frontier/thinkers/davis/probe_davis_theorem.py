"""Probe — Davis H1: Theorem 1 on the four signed triangles.

Question.  Davis (1967: 181): "A signed graph is clusterable if and only if it contains no cycle with exactly
           one negative line." With k camps available, which triangles have a rest state?
Hypothesis. H1: at k ≥ 3, ppp, pmm, mmm rest and ppm does not; at k = 2, mmm does not.
Run.       ~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.davis.probe_davis_theorem
"""

from org_frontier.thinkers.davis import forms as F


def main():
    print("Davis H1 — rest states of the four triangles at k = 2, 3, 4")
    control = F.run_control()
    recs = {}
    for name, signs in F.NAMED.items():
        for k in (2, 3, 4):
            r = F.dynamics(3, F.TRIAD_EDGES, signs, k)
            recs["%s_k%d" % (name, k)] = r
            print(F.dyn_line(r, name))
    ok = all(recs["%s_k%d" % (n, k)]["n_rest"] > 0 for n in ("ppp", "pmm", "mmm") for k in (3, 4))
    ok = ok and all(recs["ppm_k%d" % k]["n_rest"] == 0 for k in (2, 3, 4))
    ok = ok and recs["mmm_k2"]["n_rest"] == 0
    print("  clusterable triangles rest at k≥3, ppm never, mmm not at k=2: %s" % ok)
    status = "CONFIRMED" if ok else "REFUTED"
    print("H1 (no cycle with exactly one negative line): %s" % status)
    F.save("probe_davis_theorem", {"control": control, "forms": recs, "H1": status})


if __name__ == "__main__":
    main()
