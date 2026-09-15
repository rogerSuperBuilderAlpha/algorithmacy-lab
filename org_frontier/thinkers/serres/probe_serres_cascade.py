"""Probe — Serres H4: the last position.

Question.  Serres (1982: 4): "In the parasitic chain, the last to come tries to supplant his predecessor. ...
           A given parasite seeks to eject the parasite on the level immediately superior to his own." Each
           level takes from the one above and is stopped by the one below. Where is the complex, and whose
           deletion costs most?
Hypothesis. H4: cascade core ⊇ {R, N}, excludes F and T; share(N) ≥ share(R); share(T) = 0.
Run.       ~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.serres.probe_serres_cascade
"""

from org_frontier.thinkers.serres import forms as F


def main():
    print("Serres H4 — the reactive cascade")
    control = F.run_control()
    rec = F.evaluate("cascade")
    sh = F.shares("cascade")
    core = set(rec["core"])
    at_last = {"R", "N"} <= core and not (core & {"F", "T"})
    order = sh["N"] >= sh["R"] - 1e-9 and abs(sh["T"]) < 1e-9
    print("  complex at the last position=%s   share(N)≥share(R) and share(T)=0 → %s" % (at_last, order))
    n = int(at_last) + int(order)
    status = "CONFIRMED" if n == 2 else ("PARTIAL" if n == 1 else "REFUTED")
    print("H4 (the last to come wins the game): %s" % status)
    F.save("probe_serres_cascade", {"control": control, "form": rec, "shares": sh, "H4": status})


if __name__ == "__main__":
    main()
