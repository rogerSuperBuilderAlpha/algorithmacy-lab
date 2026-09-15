"""Probe — Emerson H3: network extension (operation 2).

Question.  Emerson (1962: 37): "The C-A-B network is balanced through the addition of a third relation (C-B)
           in operation number two, but it is still just a power network." Does the B–C tie zero A's
           advantage while leaving three co-members with equal value added?
Hypothesis. H3: advantage(A) = 0; core = {A, B, C}; all V equal.
Run.       ~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.emerson.probe_emerson_extension
"""

from org_frontier.thinkers.emerson import forms as F


def main():
    print("Emerson H3 — extension: closing the C–A–B network")
    control = F.run_control()
    recs = {name: F.evaluate(name) for name in ("network", "extension")}
    e = recs["extension"]
    bal = abs(e["advantage_A"]) < 1e-6
    a_in = "A" in e["core"]
    all3 = set(e["core"]) == {"A", "B", "C"}
    vals = list(e["value_added"].values())
    equal = all(abs(v - vals[0]) < 1e-6 for v in vals)
    print("  A's advantage zero=%s   A in core=%s   core is all three=%s   equal V=%s" % (bal, a_in, all3, equal))
    n = sum([a_in, all3, equal])
    status = "CONFIRMED" if bal and n == 3 else ("PARTIAL" if bal and n >= 1 else "REFUTED")
    print("H3 (extension balances and keeps three actors): %s" % status)
    F.save("probe_emerson_extension", {"control": control, "forms": recs, "H3": status})


if __name__ == "__main__":
    main()
