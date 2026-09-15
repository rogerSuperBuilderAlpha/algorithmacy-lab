"""Probe — Emerson H4: status-giving (operation 3).

Question.  Emerson (1962: 35): balance by "'giving status' to A" — A increases his investment in goals
           mediated by B. A comes to read B alone. Is the A–B relation balanced while C stays dependent?
Hypothesis. H4: V(A) = V(B); {A, B} ⊆ core; V(C) = 0.
Run.       ~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.emerson.probe_emerson_status
"""

from org_frontier.thinkers.emerson import forms as F


def main():
    print("Emerson H4 — status-giving")
    control = F.run_control()
    recs = {name: F.evaluate(name) for name in ("network", "status")}
    s = recs["status"]
    eq = abs(s["value_added"]["A"] - s["value_added"]["B"]) < 1e-6
    both = {"A", "B"} <= set(s["core"])
    c0 = abs(s["value_added"]["C"]) < 1e-9
    print("  V(A) = V(B)=%s   A and B in core=%s   C adds nothing=%s" % (eq, both, c0))
    n = sum([eq, both, c0])
    status = "CONFIRMED" if n == 3 else ("PARTIAL" if n == 2 else "REFUTED")
    print("H4 (status-giving balances the A–B relation only): %s" % status)
    F.save("probe_emerson_status", {"control": control, "forms": recs, "H4": status})


if __name__ == "__main__":
    main()
