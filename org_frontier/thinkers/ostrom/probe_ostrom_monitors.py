"""Probe — Ostrom H1: the monitors are the appropriators.

Question.  Ostrom (1990: 90, 95): monitors "are the appropriators"; monitoring is "a by-product" of use. The
           Coleman paper found that an effective sanction drops the sanctioned party out of the complex.
           When every appropriator both complies and sanctions, is every compliance node in the structure?
Hypothesis. H1: {c1, c2, c3} ⊆ core(mutual); A ∉ core(coleman_closed).
Run.       ~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.ostrom.probe_ostrom_monitors
"""

from org_frontier.thinkers.ostrom import forms as F


def main():
    print("Ostrom H1 — mutual monitoring against Coleman's closed norm")
    control = F.run_control()
    recs = {name: F.evaluate(name) for name in ("coleman_closed", "mutual")}
    all_in = {"c1", "c2", "c3"} <= set(recs["mutual"]["core"])
    a_out = "A" not in recs["coleman_closed"]["core"]
    print("  every appropriator's compliance in the core=%s   Coleman's A outside=%s" % (all_in, a_out))
    status = "CONFIRMED" if all_in and a_out else ("PARTIAL" if all_in else "REFUTED")
    print("H1 (the monitored are in the structure when they are also the monitors): %s" % status)
    F.save("probe_ostrom_monitors", {"control": control, "forms": recs, "H1": status})


if __name__ == "__main__":
    main()
