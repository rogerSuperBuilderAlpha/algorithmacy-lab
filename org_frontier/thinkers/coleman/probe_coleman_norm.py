"""Probe — Coleman H1: closure makes the norm effective.

Question.  Coleman (1988: S105–S106): without a B–C tie "they cannot combine forces to sanction A ... A's
           actions can continue unabated"; with closure "B and C can combine to provide a collective
           sanction." A yields only to a joint sanction. Is compliance a fixed point, and are B and C one?
Hypothesis. H1: (1,1,1) fixed in norm_closed, not in norm_open; B, C in one complex in norm_closed.
Run.       ~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.coleman.probe_coleman_norm
"""

from org_frontier.thinkers.coleman import forms as F


def main():
    print("Coleman H1 — the norm, open and closed")
    control = F.run_control()
    recs = {name: F.evaluate(name) for name in ("norm_open", "norm_closed")}
    fixed_closed = "111" in recs["norm_closed"]["fixed_points"]
    fixed_open = "111" in recs["norm_open"]["fixed_points"]
    together = {"B", "C"} <= set(recs["norm_closed"]["core"])
    print("  compliance fixed: open=%s closed=%s   B and C one complex under closure=%s" % (
        fixed_open, fixed_closed, together))
    if fixed_closed and not fixed_open and together:
        status = "CONFIRMED"
    elif fixed_closed and not fixed_open:
        status = "PARTIAL"
    else:
        status = "REFUTED"
    print("H1 (closure lets the sanctioners combine and the norm hold): %s" % status)
    F.save("probe_coleman_norm", {"control": control, "forms": recs, "H1": status})


if __name__ == "__main__":
    main()
