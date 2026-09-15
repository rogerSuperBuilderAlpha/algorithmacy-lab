"""Probe — Burt H3: advantage falls with constraint.

Question.  Burt (1992: 54–55): aggregate constraint C_i = Σ_j (p_ij + Σ_q p_iq p_qj)² rises with the ties
           among one's contacts, and advantage falls with it. Ego with three contacts and 0, 1, 2 (path), 3
           (triangle) ties among them: is E's value added strictly decreasing in C_E?
Hypothesis. H3 (Burt): V(E) strictly decreasing over k = 0..3.
Run.       ~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.burt.probe_burt_constraint
"""

from org_frontier.thinkers.burt import forms as F


def main():
    print("Burt H3 — value added against Burt's constraint, three contacts, 0..3 ties among them")
    control = F.run_control()
    recs = {name: F.evaluate(name, sp) for name, sp in F.h3_forms().items()}
    ks = ["k0", "k1", "k2", "k3"]
    V = [recs[k]["value_added"] for k in ks]
    C = [recs[k]["constraint"] for k in ks]
    strict = all(V[i] > V[i + 1] + 1e-9 for i in range(3))
    weak = all(V[i] >= V[i + 1] - 1e-9 for i in range(3))
    print("  C_E: %s   V(E): %s   strictly decreasing=%s  non-increasing=%s"
          % (", ".join("%.3f" % c for c in C), ", ".join("%.3f" % v for v in V), strict, weak))
    status = "CONFIRMED" if strict else ("PARTIAL" if weak else "REFUTED")
    print("H3 (value added falls strictly with constraint): %s" % status)
    F.save("probe_burt_constraint", {"control": control, "forms": recs, "C": C, "V": V, "H3": status})


if __name__ == "__main__":
    main()
