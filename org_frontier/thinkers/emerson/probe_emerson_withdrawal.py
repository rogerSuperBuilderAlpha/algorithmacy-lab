"""Probe — Emerson H2: withdrawal (operation 1).

Question.  Emerson (1962: 35): balance "through motivational withdrawal by B, the weaker member." B stops
           reading A. Does B leave the complex, and does A's advantage go to zero?
Hypothesis. H2: B ∉ core(withdrawal); advantage(A) = 0.
Run.       ~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.emerson.probe_emerson_withdrawal
"""

from org_frontier.thinkers.emerson import forms as F


def main():
    print("Emerson H2 — withdrawal")
    control = F.run_control()
    recs = {name: F.evaluate(name) for name in ("network", "withdrawal")}
    w = recs["withdrawal"]
    out = "B" not in w["core"]
    bal = abs(w["advantage_A"]) < 1e-6
    print("  B leaves the complex=%s   A's advantage zero=%s" % (out, bal))
    status = "CONFIRMED" if out and bal else ("PARTIAL" if out or bal else "REFUTED")
    print("H2 (withdrawal balances): %s" % status)
    F.save("probe_emerson_withdrawal", {"control": control, "forms": recs, "H2": status})


if __name__ == "__main__":
    main()
