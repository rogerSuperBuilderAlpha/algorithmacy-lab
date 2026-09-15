"""Probe — Latour H4: the citizen-gun.

Question.  Latour (1994: 31–34): the Neutral Tool (the gun "merely an intermediary") and Autonomous Destiny
           (human action "no more than an intermediary") are symmetrical myths; translation makes "a third
           agent ... a citizen-gun" in which "responsibility for action must be shared." Does the translation
           form bind citizen, gun, and act, and does each myth drop the party it demotes?
Hypothesis. H4 (Latour): translation core {C, G, X}; neutral_tool core excludes G; autonomous core excludes C.
Method.    Three forms on (C, G, X).
Run.       ~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.latour.probe_latour_gun
"""

from org_frontier.thinkers.latour import forms as F


def main():
    print("Latour H4 — the citizen-gun in three readings")
    control = F.run_control()
    recs = {name: F.evaluate(name, rules, F.GUN_LABELS) for name, rules in F.GUN.items()}
    trans_all = set(recs["translation"]["core"]) == {"C", "G", "X"}
    tool_drops_gun = "G" not in recs["neutral_tool"]["core"]
    auto_drops_citizen = "C" not in recs["autonomous"]["core"]
    print("  translation binds all three=%s  neutral tool drops the gun=%s  autonomous destiny drops the citizen=%s"
          % (trans_all, tool_drops_gun, auto_drops_citizen))
    n_myths = int(tool_drops_gun) + int(auto_drops_citizen)
    if trans_all and n_myths == 2:
        status = "CONFIRMED"
    elif trans_all and n_myths == 1:
        status = "PARTIAL"
    else:
        status = "REFUTED"
    print("H4 (translation binds citizen, gun, and act; each myth drops the party it demotes): %s" % status)
    F.save("probe_latour_gun", {"control": control, "forms": recs, "H4": status})


if __name__ == "__main__":
    main()
