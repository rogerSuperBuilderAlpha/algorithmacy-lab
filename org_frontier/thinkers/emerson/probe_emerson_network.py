"""Probe — Emerson H1: the unbalanced C–A–B network.

Question.  Emerson (1962: 32, 37): "power resides implicitly in the other's dependency"; in the C–A–B network
           A is the more powerful because B and C depend on him and he has alternatives. Is A the whole's
           indispensable member and do the dependents add nothing?
Hypothesis. H1: advantage(A) > 0; V(A) = core Φ; V(B) = V(C) = 0.
Run.       ~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.emerson.probe_emerson_network
"""

from org_frontier.thinkers.emerson import forms as F


def main():
    print("Emerson H1 — the C–A–B network")
    control = F.run_control()
    r = F.evaluate("network")
    adv = r["advantage_A"] > 1e-6
    whole = abs(r["value_added"]["A"] - r["core_phi"]) < 1e-6
    dep0 = abs(r["value_added"]["B"]) < 1e-9 and abs(r["value_added"]["C"]) < 1e-9
    print("  A's advantage positive=%s   V(A) = core Φ=%s   dependents add nothing=%s" % (adv, whole, dep0))
    status = "CONFIRMED" if adv and whole and dep0 else ("PARTIAL" if adv else "REFUTED")
    print("H1 (power resides in the other's dependence): %s" % status)
    F.save("probe_emerson_network", {"control": control, "forms": {"network": r}, "H1": status})


if __name__ == "__main__":
    main()
