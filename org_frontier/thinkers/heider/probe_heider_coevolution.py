"""Probe — Heider H4: attitudes and relations influence each other.

Question.  Heider's first sentence (1946: 107): "Attitudes towards persons and causal unit formations
           influence each other." In a six-element form where the three relations are elements too —
           attitudes by signed majority with hold, each relation becoming positive when its two persons
           agree — does the major complex contain attitudes and relations together?
Hypothesis. H4: the core has at least one attitude node and at least one relation node.
Method.    coevolving(); Φ_MIP, major complex, attractors. Six nodes: about four minutes.
Run.       ~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.heider.probe_heider_coevolution
"""

from org_frontier.thinkers.heider import forms as F


def main():
    print("Heider H4 — attitudes and relations as one form (six elements)")
    control = F.run_control()
    rec = F.evaluate("coevolving", F.coevolving(), F.COEVOLVING_LABELS)
    core = rec["core"]
    att = [c for c in core if c in ("p", "o", "q")]
    rel = [c for c in core if c.startswith("L")]
    print("  coevolving     Φ_MIP=%.6f  core=%s coreΦ=%.3f  attitudes in core=%s relations in core=%s  "
          "attractors: %d fixed, %d cycles"
          % (rec["phi_mip"], tuple(core), rec["core_phi"], att, rel, rec["n_fixed"], rec["n_cycles"]))
    status = "CONFIRMED" if (att and rel) else "REFUTED"
    print("H4 (the core joins attitudes and relations): %s" % status)
    F.save("probe_heider_coevolution", {"control": control, "form": rec, "H4": status})


if __name__ == "__main__":
    main()
