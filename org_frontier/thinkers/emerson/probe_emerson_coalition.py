"""Probe — Emerson H5: extension and coalition balance differently (operation 2 vs 4).

Question.  Emerson (1962: 37): "Operation number two reduces the power of the stronger actor, while number 4
           increases the power of weaker actors through collectivization." Do both zero A's advantage, does
           extension lower V(A), and does coalition raise V(B) and V(C)?
Hypothesis. H5: advantage(A) = 0 in both; V(A, extension) < V(A, network); V(B, C; coalition) > V(B, C; network).
Run.       ~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.emerson.probe_emerson_coalition
"""

from org_frontier.thinkers.emerson import forms as F


def main():
    print("Emerson H5 — extension against coalition")
    control = F.run_control()
    recs = {name: F.evaluate(name) for name in ("network", "extension", "coalition")}
    n, e, c = recs["network"], recs["extension"], recs["coalition"]
    bal = abs(e["advantage_A"]) < 1e-6 and abs(c["advantage_A"]) < 1e-6
    a_down = e["value_added"]["A"] < n["value_added"]["A"] - 1e-6
    weak_up = all(c["value_added"][x] > n["value_added"][x] + 1e-6 for x in ("B", "C"))
    print("  both balance=%s   extension lowers V(A) (%.3f -> %.3f)=%s   coalition raises V(B), V(C) (%.3f -> %.3f)=%s" % (
        bal, n["value_added"]["A"], e["value_added"]["A"], a_down, n["value_added"]["B"], c["value_added"]["B"], weak_up))
    if bal and a_down and weak_up:
        status = "CONFIRMED"
    elif bal and (a_down or weak_up):
        status = "PARTIAL"
    else:
        status = "REFUTED"
    print("H5 (extension reduces the strong; coalition raises the weak): %s" % status)
    F.save("probe_emerson_coalition", {"control": control, "forms": recs, "H5": status})


if __name__ == "__main__":
    main()
