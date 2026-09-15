"""Probe — Hegel H3: the real middle is one the extremes return through.

Question.  Hegel: in the rational syllogism "the subject joins itself together with itself by means of this
           mediation" (EL §182); the real middle "unites them in and for themselves" (SL 641). If one extreme
           is read by the middle but does not read it back, is it united?
Hypothesis. H3: half_return core = {A, M}; syllogism core = {A, M, B}.
Run.       ~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.hegel.probe_hegel_return
"""

from org_frontier.thinkers.hegel import forms as F


def main():
    print("Hegel H3 — the extreme that returns through the middle, and the one that does not")
    control = F.run_control()
    recs = {name: F.evaluate(name) for name in ("syllogism", "half_return")}
    a = set(recs["half_return"]["core"]) == {"A", "M"}
    b = set(recs["syllogism"]["core"]) == {"A", "M", "B"}
    print("  half_return core is {A,M}=%s   syllogism core is {A,M,B}=%s" % (a, b))
    status = "CONFIRMED" if (a and b) else "REFUTED"
    print("H3 (an extreme is united only if it returns to itself through the middle): %s" % status)
    F.save("probe_hegel_return", {"control": control, "forms": recs, "H3": status})


if __name__ == "__main__":
    main()
