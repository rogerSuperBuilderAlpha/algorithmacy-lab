"""Probe — Burt H1: closure removes the broker, for both benefits.

Question.  Burt (1992: 18, 30): the hole is "an insulator"; "the structural holes that generate information
           benefits also generate control benefits." A tie between the two contacts: does it remove the
           information broker (E = X AND Y) and the control broker (E = X OR Y) alike?
Hypothesis. H1 (Burt): under closure both leave the core or add nothing.
Method.    open / closed forms for each broker; V(E) = coreΦ(whole) − coreΦ(without E). Also the q214
           one-sided replace bypass via contingency_test.
Run.       ~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.burt.probe_burt_closure
"""

from org_frontier.classifier.contingency import contingency_test
from org_frontier.thinkers.burt import forms as F


def main():
    print("Burt H1 — closure by cohesion against the information broker and the control broker")
    control = F.run_control()
    recs = {name: F.evaluate(name, sp) for name, sp in F.h1_forms().items()}
    q214 = {}
    for broker in ("info", "control"):
        labels, rules = F.compile_spec(F.h1_forms()["%s_open" % broker])
        r = contingency_test(rules, labels, "E", downstream="Y", upstream="X", mode="replace")
        q214[broker] = {"kind": r.kind, "margin": round(r.margin, 6)}
        print("  q214 one-sided replace bypass, %s broker: %s margin=%.3f" % (broker, r.kind, r.margin))
    gone = {b: ("E" not in recs["%s_closed" % b]["core"]) or recs["%s_closed" % b]["value_added"] <= 1e-9
            for b in ("info", "control")}
    print("  broker removed by symmetric closure: info=%s control=%s" % (gone["info"], gone["control"]))
    n = sum(gone.values())
    status = "CONFIRMED" if n == 2 else ("PARTIAL" if n == 1 else "REFUTED")
    print("H1 (closure removes both the information and the control broker): %s" % status)
    F.save("probe_burt_closure", {"control": control, "forms": recs, "q214_bypass": q214, "removed": gone, "H1": status})


if __name__ == "__main__":
    main()
