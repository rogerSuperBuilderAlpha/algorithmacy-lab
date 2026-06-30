"""Probe 368 (Q214) — classifying the literature's triad types with the bypass-counterfactual.

The brokerage and sociology literature names many third parties and draws one line over and over: the third
who joins two others versus the third who profits by keeping them apart. q213's bypass-counterfactual
(classifier/contingency.py) gives that line a computable criterion. This probe models the canonical triad
types as small Boolean forms and classifies each necessary (intrinsic) / contingent / partial / reducible.

Templates (labels A, M, C; M is the third party tested):
  relay       A'=C, M'=A, C'=M ; bypass C reads A          -> contingent (a maintained/mandated pass-through)
  conjunctive A'=M, M'=A&C, C'=M ; bypass C reads A         -> intrinsic (an integrating mediator)
  additive    A'=M, M'=A&C, C'=M ; bypass C'=M|A            -> partial (integrator + parallel back-channel)
  free        A'=C, M'=A, C'=A ; bypass C reads A           -> reducible (already sidelined)

Hypotheses (fixed before computing, see hypotheses.md):
  H1 — the gaudens family (gaudens, separans, divide-et-impera, structural hole, bridge) classify contingent.
  H2 — the iungens splits: integrating -> necessary, self-liquidating -> reducible.
  H3 — integrators (Simmelian mediator, two-sided platform) classify necessary.
  H4 — Gould-Fernandez roles sort by group boundary (coordinator reducible; gatekeeper/representative/liaison
       contingent; itinerant partial).
  H5 — boundary: a Heider-balance signed-sentiment triad is mutual, not mediated; the test does not apply.

Validation gap: stylized n=3 Boolean models with exact Φ; a classification of theoretical triad types, not a
measurement of any organization.

Run:  python -m org_frontier.questions.q214_triadic_classification.probe_triadic_classification
"""

import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.probes.lib import verdict, major_complex  # noqa: E402
from org_frontier.classifier.contingency import contingency_test  # noqa: E402


def _relay():
    return ("A", "M", "C"), [lambda x: x[2], lambda x: x[0], lambda x: x[1]], "M", "C", "A", "replace"


def _conjunctive():
    return ("A", "M", "C"), [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]], "M", "C", "A", "replace"


def _additive():
    return ("A", "M", "C"), [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]], "M", "C", "A", "add"


def _free():
    return ("A", "M", "C"), [lambda x: x[2], lambda x: x[0], lambda x: x[0]], "M", "C", "A", "replace"


TEMPLATES = {"relay": _relay, "conjunctive": _conjunctive, "additive": _additive, "free": _free}

# (name, theory cite-key, template, predicted kind)
TYPES = [
    ("simmelian_mediator", "simmel1950", "conjunctive", "intrinsic"),
    ("tertius_gaudens", "obstfeld2014", "relay", "contingent"),
    ("tertius_separans", "lee2023", "relay", "contingent"),
    ("divide_et_impera", "simmel1950", "relay", "contingent"),
    ("tertius_iungens_integrating", "obstfeld2005", "conjunctive", "intrinsic"),
    ("tertius_iungens_selfliquidating", "obstfeld2005", "free", "reducible"),
    ("conduit_unmandated", "obstfeld2014", "free", "reducible"),
    ("conduit_mandated", "obstfeld2014", "relay", "contingent"),
    ("gf_coordinator", "gould1989", "free", "reducible"),
    ("gf_gatekeeper", "gould1989", "relay", "contingent"),
    ("gf_representative", "gould1989", "relay", "contingent"),
    ("gf_liaison", "gould1989", "relay", "contingent"),
    ("gf_itinerant", "gould1989", "additive", "partial"),
    ("structural_hole_broker", "burt1992", "relay", "contingent"),
    ("granovetter_bridge", "granovetter1973", "relay", "contingent"),
    ("two_sided_platform", "rochet2003", "conjunctive", "intrinsic"),
    ("gatekeeping_platform", "hagiu2009", "relay", "contingent"),
    ("market_maker", "rubinstein1987", "additive", "partial"),
    ("arbitrageur_friction", "rubinstein1987", "relay", "contingent"),
]

GAUDENS_FAMILY = {"tertius_gaudens", "tertius_separans", "divide_et_impera",
                  "structural_hole_broker", "granovetter_bridge"}
DISPLAY = {"intrinsic": "necessary", "contingent": "contingent", "partial": "partial", "reducible": "reducible"}


def main():
    print("PROBE 368 (Q214) — classifying the literature's triad types")
    print("=" * 92)

    # ---- instrument control ----
    labels, rules, party, dn, up, mode = _conjunctive()
    v0 = verdict(rules, labels)
    ctrl = v0.structure == "triadic" and abs(v0.max_phi - 2.0) < 1e-6
    print("  control  conjunctive triad : %s Φ=%.6f %s"
          % (v0.structure, v0.max_phi, "PASS" if ctrl else "FAIL"))
    assert ctrl, "instrument control failed; aborting"
    print("  %-32s %-15s %-11s %6s" % ("triad type", "theory", "class", "margin"))

    results = {}
    for name, key, tmpl, _exp in TYPES:
        labels, rules, party, dn, up, mode = TEMPLATES[tmpl]()
        r = contingency_test(rules, labels, party, downstream=dn, upstream=up, mode=mode)
        results[name] = r
        print("  %-32s %-15s %-11s %6.3f" % (name, key, DISPLAY[r.kind], r.margin))

    # ---- H5 boundary: Heider balance triad ----
    bal = [lambda x: x[1] & x[2], lambda x: x[0] & x[2], lambda x: x[0] & x[1]]
    vb = verdict(bal, ("P", "Q", "R"))
    bcore, bphi = major_complex(bal, ("P", "Q", "R"))
    forced = contingency_test(bal, ("P", "Q", "R"), "Q", downstream="R", upstream="P", mode="replace")
    print("  %-32s %-15s %s Φ=%.3f core=%s  (mutual: every party reads both others)"
          % ("heider_balance (boundary)", "heider1946", vb.structure, vb.max_phi, bcore))
    print("    forcing the test removes an existing edge, not a forbidden one -> spurious '%s' (margin %.3f)"
          % (DISPLAY[forced.kind], forced.margin))

    print("=" * 92)
    # ---- verdicts ----
    h1 = all(results[n].kind == "contingent" and abs(results[n].margin - 2.0) < 1e-6 for n in GAUDENS_FAMILY)
    h2 = (results["tertius_iungens_integrating"].kind == "intrinsic"
          and results["tertius_iungens_selfliquidating"].kind == "reducible")
    h3 = (results["simmelian_mediator"].kind == "intrinsic" and results["simmelian_mediator"].margin < 1e-9
          and results["two_sided_platform"].kind == "intrinsic")
    h4 = (results["gf_coordinator"].kind == "reducible"
          and results["gf_gatekeeper"].kind == "contingent"
          and results["gf_representative"].kind == "contingent"
          and results["gf_liaison"].kind == "contingent"
          and results["gf_itinerant"].kind == "partial")
    # the balanced triad is symmetric (all three in core), not a mediated triad with a forbidden edge
    h5 = vb.structure == "triadic" and set(bcore) == {"P", "Q", "R"}

    print("  H1 (gaudens family all contingent, margin 2.0): %s" % _v(h1))
    print("  H2 (iungens splits: integrating necessary, self-liquidating reducible): %s" % _v(h2))
    print("  H3 (integrators necessary: Simmelian mediator, two-sided platform): %s" % _v(h3))
    print("  H4 (Gould-Fernandez roles sort by group boundary): %s" % _v(h4))
    print("  H5 (Heider balance triad is mutual, not mediated; test N/A): %s" % _v(h5))
    print("=" * 92)


def _v(b):
    return "SUPPORTED" if b else "REFUTED"


if __name__ == "__main__":
    main()
