"""Probe — Granovetter H4: damage.

Question.  Granovetter (1973: 1366): "removal of the average weak tie would do more 'damage' to transmission
           probabilities than would that of the average strong one." Two strong dyads and a weak bridge:
           cut the bridge, or cut a within-dyad strong tie — which costs more transmission, and which costs
           more integration?
Hypothesis. H4: cutting the bridge costs more on both measures.
Run.       ~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.granovetter.probe_granovetter_damage
"""

from org_frontier.thinkers.granovetter import forms as F

fs = frozenset
LABELS = ("a1", "a2", "b1", "b2")
BASE = {fs({"a1", "a2"}): F.STRONG, fs({"b1", "b2"}): F.STRONG, fs({"a2", "b1"}): F.WEAK}


def main():
    print("Granovetter H4 — cut the weak bridge, or cut a strong tie")
    control = F.run_control()
    recs = {}
    lab, ties = F.graph(LABELS, BASE)
    recs["base"] = F.evaluate("base", lab, ties)
    for name, cut in (("cut_bridge", fs({"a2", "b1"})), ("cut_strong", fs({"a1", "a2"}))):
        t = dict(BASE)
        del t[cut]
        lab, ties = F.graph(LABELS, t)
        recs[name] = F.evaluate(name, lab, ties)
    b = recs["base"]
    dmg = {}
    for k in ("cut_bridge", "cut_strong"):
        dmg[k] = {"reach_lost": b["reach_pairs"] - recs[k]["reach_pairs"],
                  "core_phi_lost": round(b["core_phi"] - recs[k]["core_phi"], 6)}
    more_reach = dmg["cut_bridge"]["reach_lost"] > dmg["cut_strong"]["reach_lost"]
    more_phi = dmg["cut_bridge"]["core_phi_lost"] > dmg["cut_strong"]["core_phi_lost"] + 1e-9
    print("  damage — cut bridge: reach −%d, coreΦ −%.3f | cut strong: reach −%d, coreΦ −%.3f" % (
        dmg["cut_bridge"]["reach_lost"], dmg["cut_bridge"]["core_phi_lost"],
        dmg["cut_strong"]["reach_lost"], dmg["cut_strong"]["core_phi_lost"]))
    n = int(more_reach) + int(more_phi)
    status = "CONFIRMED" if n == 2 else ("PARTIAL" if n == 1 else "REFUTED")
    print("H4 (the weak bridge's removal does more damage than a strong tie's, on transmission and integration): %s" % status)
    F.save("probe_granovetter_damage", {"control": control, "forms": recs, "damage": dmg, "H4": status})


if __name__ == "__main__":
    main()
