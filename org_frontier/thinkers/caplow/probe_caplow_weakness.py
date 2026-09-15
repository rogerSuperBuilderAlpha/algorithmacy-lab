"""Probe — Caplow H2: strength is weakness.

Question.  Caplow (1956, A.4) and the experimental literature after Vinacke & Arkoff (1957): the strongest
           member is the one most often excluded from the coalitions that form. Counting membership over
           the coalitions that BIND across all eight types, is A a member less often than B and than C?
Hypothesis. H2 (Caplow): count(A) < count(B) and count(A) < count(C).
Method.    The 24 coalition forms; membership counts over binding coalitions; core-inclusion counts over
           all 24 forms reported alongside.
Run.       ~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.caplow.probe_caplow_weakness
"""

from org_frontier.thinkers.caplow import forms as F


def main():
    print("Caplow H2 — strength is weakness")
    control = F.run_control()
    recs = F.evaluate_types(pre=False)
    binding = [r for r in recs.values() if r["binds"]]
    count = {m: sum(1 for r in binding if m in r["pair"]) for m in "ABC"}
    in_core = {m: sum(1 for r in recs.values() if m in r["core"]) for m in "ABC"}
    print("  binding coalitions=%d: %s" % (len(binding), ",".join(r["form"] for r in binding)))
    print("  membership in binding coalitions: A=%d B=%d C=%d" % (count["A"], count["B"], count["C"]))
    print("  in the core across all 24 coalition forms: A=%d B=%d C=%d" % (in_core["A"], in_core["B"], in_core["C"]))
    ok = count["A"] < count["B"] and count["A"] < count["C"]
    status = "CONFIRMED" if ok else "REFUTED"
    print("H2 (A is in fewer binding coalitions than B and than C): %s" % status)
    F.save("probe_caplow_weakness", {"control": control, "forms": recs, "binding_count": count,
                                      "core_count": in_core, "H2": status})


if __name__ == "__main__":
    main()
