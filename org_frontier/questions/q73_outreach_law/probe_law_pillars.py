"""Probe Q73 (H1-H5) — the outreach-coordination law, re-derived in one place from keystone forms.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.questions.q73_outreach_law.probe_law_pillars
"""
import csv, os
from org_frontier.probes.lib import verdict, major_complex
from org_frontier.questions.q73_outreach_law import forms as F

L3, L4 = ("E", "M", "R"), ("E", "M", "R1", "R2")
LR = ("E", "A1", "A2", "R")


def main():
    print("PROBE Q73 (H1-H5) — outreach-coordination law pillars")
    print("=" * 72)
    rr = verdict(F.READ_RECIPIENT, L3); bc = verdict(F.BROADCAST, L3); os_ = verdict(F.ONE_SHOT, L3)
    ar = verdict(F.ALL_REQUIRED, L4); su = verdict(F.SUBSTITUTABLE, L4)
    ringcore, ringphi = major_complex(F.RING4, LR)
    print(f"  joint-determination: read_recipient {rr.structure} Φ={rr.max_phi:.2f} | broadcast {bc.structure}")
    print(f"  liveness:            read_recipient {rr.structure} vs one_shot {os_.structure} (same wiring, R live vs frozen)")
    print(f"  non-substitutability:all_required {ar.structure} Φ={ar.max_phi:.2f} vs substitutable {su.structure}")
    print(f"  closure binds all:   ring core={ringcore} Φ={ringphi:.2f}")
    # law pillars
    p1 = rr.structure == "triadic" and bc.structure == "dyadic"           # joint determination
    p2 = rr.structure == "triadic" and os_.structure == "dyadic"          # liveness decides (same wiring)
    p3 = ar.structure == "triadic" and su.structure == "dyadic"           # substitutability collapses
    p4 = set(ringcore or ()) == set(LR) and ringphi > 2.0 + 1e-9          # closure binds the whole
    # P5 (structural-not-cheap: noise-robust, proxy-irrecoverable) is NOT re-derived here. It is carried
    # from the registered Q71 and Q72 checks; this probe only re-derives P1-P4.
    rederived = p1 and p2 and p3 and p4
    print("=" * 72)
    print(f"  P1 joint determination: {p1} | P2 liveness decides: {p2} | P3 substitutability collapses: {p3}")
    print(f"  P4 closure binds the whole: {p4}")
    print(f"  P5 structural-not-cheap: CARRIED from q71/q72 (asserted, not re-derived here)")
    print(f"  OUTREACH-COORDINATION LAW pillars hold: {rederived}")  # P1-P4 re-derived here; P5 carried
    print(f"  Q73 VERDICT: {'CONFIRMED' if rederived else 'REFUTED'}")
    d_ = os.path.join(os.path.dirname(__file__), "results"); os.makedirs(d_, exist_ok=True)
    with open(os.path.join(d_, "law_pillars.csv"), "w", newline="") as f:
        w = csv.writer(f); w.writerow(["pillar", "status"])
        for i, p in enumerate([p1, p2, p3, p4], 1): w.writerow([f"P{i}", "rederived" if p else "FAILED"])
        w.writerow(["P5", "carried_from_q71_q72"])


if __name__ == "__main__":
    main()
