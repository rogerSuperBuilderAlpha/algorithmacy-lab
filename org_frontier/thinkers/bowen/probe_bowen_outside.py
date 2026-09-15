"""Probe — Bowen H3: under stress the outside position costs least.

Question.  Bowen (1978: 373–374): "In periods of stress, the outside position is the most comfortable and
           most desired position." In the triangled form, put anxiety at one position at a time: which
           position's anxiety costs the whole the least Φ?
Hypothesis. H3: at ε = 0.1 and 0.2, anxiety at C alone costs strictly less than at A alone or B alone.
Run.       ~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.bowen.probe_bowen_outside
"""

from org_frontier.thinkers.bowen import forms as F


def main():
    print("Bowen H3 — anxiety at one position of the triangled form")
    control = F.run_control()
    base = F.evaluate("triangled", 0.0)["phi_mip"]
    recs, wins = {}, []
    for e in (0.1, 0.2):
        loss = {}
        for i, pos in enumerate(("A", "B", "C")):
            eps = [0.0, 0.0, 0.0]
            eps[i] = e
            r = F.evaluate("triangled", eps, base_phi=base, tag="anxiety at %s" % pos)
            recs["%s_%.2f" % (pos, e)] = r
            loss[pos] = round(base - r["phi_mip"], 6)
        least = min(loss, key=loss.get)
        strict = loss["C"] < loss["A"] - 1e-9 and loss["C"] < loss["B"] - 1e-9
        wins.append(strict)
        print("  ε=%.2f loss: A=%.3f B=%.3f C=%.3f  least=%s  C strictly least=%s" % (
            e, loss["A"], loss["B"], loss["C"], least, strict))
    status = "CONFIRMED" if all(wins) else ("PARTIAL" if any(wins) else "REFUTED")
    print("H3 (anxiety at the outsider costs the whole the least): %s" % status)
    F.save("probe_bowen_outside", {"control": control, "base_phi": base, "forms": recs, "H3": status})


if __name__ == "__main__":
    main()
